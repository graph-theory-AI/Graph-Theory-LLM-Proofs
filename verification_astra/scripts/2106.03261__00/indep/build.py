"""Independent re-implementation of the construction in attacks_retry/2106.03261__00/output.md.

Petersen P: vertices a0..a4, b0..b4; edges a_i a_{i+1}, a_i b_i, b_i b_{i+2} (mod 5).
q prime = 1 mod 10 (odd char), k=(q-1)/10, F_q^* = disjoint union of I_v, |I_v|=k.
V_v = {(x,y) in F_q^2 : x in I_v, 2y != x^2}.
For uv in E(P): (x,y)~(x',y') iff y+y' = x x' + c_uv, c=1 exactly on {a3,b3} (twisted).
"""
import itertools, random, sys
from collections import defaultdict

PV = ['a0','a1','a2','a3','a4','b0','b1','b2','b3','b4']
_E = []
for i in range(5):
    _E.append(('a%d'%i,'a%d'%((i+1)%5)))
    _E.append(('a%d'%i,'b%d'%i))
    _E.append(('b%d'%i,'b%d'%((i+2)%5)))
PE = sorted({tuple(sorted(e)) for e in _E})
assert len(PE)==15, PE
PADJ = defaultdict(set)
for u,v in PE:
    PADJ[u].add(v); PADJ[v].add(u)
assert all(len(PADJ[v])==3 for v in PV)

def petersen_check():
    """confirm our labelling really is the Petersen graph, via networkx"""
    try:
        import networkx as nx
    except ImportError:
        return None
    G = nx.Graph(); G.add_nodes_from(PV); G.add_edges_from(PE)
    return nx.is_isomorphic(G, nx.petersen_graph())

def build(q, twisted=True, seed=None, perm=None):
    assert (q-1) % 10 == 0 and q % 2 == 1
    k = (q-1)//10
    nz = list(range(1,q))
    if seed is not None:
        random.Random(seed).shuffle(nz)
    order = perm if perm is not None else PV
    I = {v: nz[i*k:(i+1)*k] for i,v in enumerate(order)}
    inv2 = pow(2, q-2, q)
    V = {v: [(x,y) for x in I[v] for y in range(q) if (2*y) % q != (x*x) % q] for v in PV}
    c = {e: (1 if (twisted and set(e)=={'a3','b3'}) else 0) for e in PE}
    # class-restricted adjacency
    A = {z: defaultdict(set) for v in PV for z in V[v]}
    Vset = {v: set(V[v]) for v in PV}
    for (u,v) in PE:
        cc = c[(u,v)]
        for (x,y) in V[u]:
            for xp in I[v]:
                yp = (x*xp - y + cc) % q
                if (2*yp) % q != (xp*xp) % q:
                    A[(x,y)][v].add((xp,yp))
                    A[(xp,yp)][u].add((x,y))
    adj = {z: set().union(*d.values()) if d else set() for z,d in A.items()}
    return dict(q=q,k=k,I=I,V=V,Vset=Vset,A=A,adj=adj,c=c)

def structure(D, verbose=True):
    q,k,V,adj,A = D['q'],D['k'],D['V'],D['adj'],D['A']
    verts = [z for v in PV for z in V[v]]
    n = len(verts); m = len(V['a0'])
    degs = [len(adj[z]) for z in verts]
    ne = sum(degs)//2
    # per-required-pair degrees
    pd = []
    for (u,v) in PE:
        for z in V[u]: pd.append(len(A[z][v]))
        for z in V[v]: pd.append(len(A[z][u]))
    # codegrees -> C4 / triangles
    cod = defaultdict(int)
    for z in verts:
        nb = sorted(adj[z])
        for a,b in itertools.combinations(nb,2):
            cod[(a,b)] += 1
    maxcod = max(cod.values()) if cod else 0
    ntri = sum(1 for (a,b),t in cod.items() if b in adj[a])
    # pair densities
    dens = []
    for (u,v) in PE:
        e = sum(len(A[z][v]) for z in V[u])
        dens.append(e/(m*m))
    res = dict(n=n,m=m,ne=ne,mindeg=min(degs),maxdeg=max(degs),
               minpd=min(pd),maxpd=max(pd),maxcod=maxcod,ntri=ntri,
               dmin=min(dens),dmax=max(dens))
    if verbose:
        print(f"  q={q} k={k}: n={n} (claim (q-1)^2={(q-1)**2})  m={m} (claim k(q-1)={k*(q-1)})")
        print(f"    deg in [{min(degs)},{max(degs)}]  claim [3k-6,3k]=[{3*k-6},{3*k}]  "
              f"Delta<=(3/10)sqrt(n)={0.3*n**0.5:.3f}")
        print(f"    per-pair deg in [{min(pd)},{max(pd)}]  claim [k-2,k]=[{k-2},{k}]")
        print(f"    e={ne}   e/n^1.5={ne/n**1.5:.6f}  (claim -> 3/20=0.15)")
        print(f"    max codegree={maxcod} (C4-free iff <=1)   triangles={ntri}")
        print(f"    pair density in [{min(dens):.8f},{max(dens):.8f}]  p=n^-1/2={n**-0.5:.8f}  1/q={1/q:.8f}")
    return res

ORDER = ['a0','a1','a2','a3','a4','b0','b2','b4','b1','b3']
def count_canonical(D, collect=0):
    V,A = D['V'],D['A']
    pos = {v:i for i,v in enumerate(ORDER)}
    prev = {v:[u for u in PADJ[v] if pos[u]<pos[v]] for v in ORDER}
    total=0; samples=[]; assign={}
    L=len(ORDER)
    def rec(i):
        nonlocal total
        if i==L:
            total+=1
            if len(samples)<collect: samples.append(dict(assign))
            return
        v=ORDER[i]; ps=prev[v]
        if not ps: cand=V[v]
        else:
            cand=A[assign[ps[0]]][v]
            for u in ps[1:]:
                cand = cand & A[assign[u]][v]
                if not cand: return
        for z in cand:
            assign[v]=z; rec(i+1)
        assign.pop(v,None)
    rec(0)
    return total, samples

def verify_copy(D, cp):
    q,c = D['q'], D['c']
    bad=[]
    for (u,v) in PE:
        (x,y),(xp,yp) = cp[u],cp[v]
        if (y+yp) % q != (x*xp + c[(u,v)]) % q: bad.append((u,v))
    inclasses = all(cp[v] in D['Vset'][v] for v in PV)
    distinct = len(set(cp.values()))==10
    return (not bad) and inclasses and distinct, bad

def count_hom(D):
    """count ALL homomorphisms P -> G_q (not just canonical), by backtracking."""
    V,adj = D['V'],D['adj']
    allv = [z for v in PV for z in V[v]]
    pos = {v:i for i,v in enumerate(ORDER)}
    prev = {v:[u for u in PADJ[v] if pos[u]<pos[v]] for v in ORDER}
    total=0; assign={}
    L=len(ORDER)
    def rec(i):
        nonlocal total
        if i==L: total+=1; return
        v=ORDER[i]; ps=prev[v]
        if not ps: cand=allv
        else:
            cand=adj[assign[ps[0]]]
            for u in ps[1:]:
                cand = cand & adj[assign[u]]
                if not cand: return
        for z in cand:
            assign[v]=z; rec(i+1)
        assign.pop(v,None)
    rec(0)
    return total

if __name__ == '__main__':
    print("labelling is the Petersen graph:", petersen_check())
    qs = [int(a) for a in sys.argv[1:]] or [11,31,41]
    for q in qs:
        for tw in (True, False):
            print(f"--- q={q} twisted={tw}")
            D = build(q, twisted=tw)
            structure(D)
            t,s = count_canonical(D, collect=2)
            print(f"    CANONICAL PETERSEN COPIES = {t}")
            for cp in s:
                print("      sample:", dict(sorted(cp.items())), "recheck:", verify_copy(D,cp))
            h = count_hom(D)
            print(f"    hom(P,G_q) = {h}")
