"""Shared construction code for refereeing 2304.03567__03.

Builds the core K and the recursive networks F_h of the writeup, plus B_h.
"""
import itertools, random
from collections import defaultdict

# ---------- two-linkage instances (already "normalized" per section 2.1) ----------
G_NO = dict(V=['s1','s2','z','t1','t2'],
            A=[('s1','z'),('s2','z'),('z','t1'),('z','t2')])
G_YES = dict(V=['s1','t1','s2','t2'],
             A=[('s1','t1'),('s2','t2')])

def reach(adj, src, forbidden=frozenset()):
    seen={src}; st=[src]
    while st:
        u=st.pop()
        for v in adj.get(u,()):
            if v not in seen and v not in forbidden:
                seen.add(v); st.append(v)
    return seen

def adj_of(arcs):
    d=defaultdict(list)
    for u,v in arcs: d[u].append(v)
    return d

def two_linkage_answer(G):
    """brute force: vertex-disjoint s1->t1 and s2->t2"""
    V,A = G['V'], G['A']; ad=adj_of(A)
    def simple_paths(s,t):
        out=[]
        def go(u,path,onpath):
            if u==t: out.append(tuple(path)); return
            for v in ad.get(u,()):
                if v not in onpath:
                    path.append(v); onpath.add(v); go(v,path,onpath)
                    path.pop(); onpath.discard(v)
        go(s,[s],{s}); return out
    P1=simple_paths('s1','t1'); P2=simple_paths('s2','t2')
    for p in P1:
        for q in P2:
            if not (set(p)&set(q)): return True
    return False

def normalized_ok(G):
    V,A=G['V'],G['A']; ad=adj_of(A)
    rad=adj_of([(v,u) for u,v in A])
    if any(v in ('s1','s2') for u,v in A): return False,'indeg source'
    if any(u in ('t1','t2') for u,v in A): return False,'outdeg sink'
    if 't1' not in reach(ad,'s1'): return False,'no s1->t1'
    if 't2' not in reach(ad,'s2'): return False,'no s2->t2'
    from_s = reach(ad,'s1')|reach(ad,'s2')
    to_t   = reach(rad,'t1')|reach(rad,'t2')
    for v in V:
        if v not in from_s or v not in to_t: return False,'vertex %s'%v
    return True,'ok'

# ---------- the core K (section 2.2) ----------
def core_arcs(G, tag, a, b, ell, r):
    """arcs of a core copy; G-interior vertices are ('G',tag,v)."""
    g=lambda v:('G',tag,v)
    A=[(g(u),g(v)) for u,v in G['A']]
    A += [(a,g('s1')),(g('s1'),a),(b,g('t2')),(g('t2'),b),
          (g('t2'),g('s1')),(g('t1'),ell),(r,g('s2'))]
    return A, [g(v) for v in G['V']]

# ---------- recursive network F_h (section 4) ----------
class DSU:
    def __init__(s): s.p={}
    def find(s,x):
        s.p.setdefault(x,x)
        while s.p[x]!=x: s.p[x]=s.p[s.p[x]]; x=s.p[x]
        return x
    def union(s,x,y):
        x,y=s.find(x),s.find(y)
        if x!=y: s.p[x]=y

def build_F(G,h):
    """returns (vertices, arcs, marked[list indexed by binary string], a_port, b_port)"""
    dsu=DSU(); arcs=[]; verts=set(); marked={}
    def A_(w): return ('A',w)
    def B_(w): return ('B',w)
    def rec(w,d):
        verts.add(A_(w)); verts.add(B_(w))
        if d==0:
            z=('Z',w); verts.add(z); marked[w]=z
            arcs.extend([(A_(w),z),(z,A_(w)),(z,B_(w)),(B_(w),z)])
        else:
            rec(w+'0',d-1); rec(w+'1',d-1)
            dsu.union(B_(w+'0'), A_(w+'1'))          # b^L = a^R
            ell=A_(w+'0'); r=B_(w+'1')                # ell = a^L, r = b^R
            ca,cv=core_arcs(G,w,A_(w),B_(w),ell,r)
            arcs.extend(ca); verts.update(cv)
    rec('',h)
    f=dsu.find
    V={f(v) for v in verts}
    Arc={(f(u),f(v)) for u,v in arcs}
    M={w:f(z) for w,z in marked.items()}
    return V,sorted(Arc),M,f(A_('')),f(B_(''))

def hypercube_requests(M,h):
    R=[]
    keys=sorted(M)
    for u in keys:
        for i in range(h):
            v=u[:i]+('1' if u[i]=='0' else '0')+u[i+1:]
            if u<v: R.append((M[u],M[v]))
    return R

# ---------- B_h (section 5) ----------
def build_B(h):
    V=[]; E=[]
    for L in range(h+1):
        V += [''.join(s) for s in itertools.product('01',repeat=L)] if L>0 else ['']
    for w in V:
        if len(w)<h:
            E += [(w,w+'0'),(w,w+'1'),(w+'0',w+'1')]
    marked={w:w for w in V if len(w)==h}
    return V,E,marked

# ---------- evaluation ----------
def realized(order, arcs, marked_list, requests):
    """order: list of vertices; arcs: directed arcs of the (bi)digraph.
    Returns number of requests forward-connected."""
    pos={v:i for i,v in enumerate(order)}
    out=defaultdict(list)
    for u,v in arcs:
        if pos[u]<pos[v]: out[u].append(v)
    idx={v:i for i,v in enumerate(marked_list)}
    reachbits={}
    for v in sorted(order,key=lambda x:-pos[x]):
        b=0
        if v in idx: b |= 1<<idx[v]
        for w in out.get(v,()): b |= reachbits[w]
        reachbits[v]=b
    cnt=0
    for x,y in requests:
        if (reachbits[x]>>idx[y])&1 or (reachbits[y]>>idx[x])&1: cnt+=1
    return cnt

def is_strong(V,arcs):
    ad=adj_of(arcs); rad=adj_of([(v,u) for u,v in arcs])
    s=next(iter(V))
    return reach(ad,s)==set(V) and reach(rad,s)==set(V)
