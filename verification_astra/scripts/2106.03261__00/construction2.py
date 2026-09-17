"""Explicit construction of G_q from attacks_retry/2106.03261__00/output.md and
brute-force verification of its claimed properties.

q = 11^r, k = (q-1)/10, F_q^* split into 10 classes I_v of size k (one per Petersen
vertex).  V_v = {(x,y) : x in I_v, 2y != x^2}.  For uv in E(Petersen),
(x,y) ~ (x',y')  iff  y + y' = x x' + c_uv,  with c = 1 exactly on {a3,b3}.
Usage: python3 construction2.py [r] [seed]
"""
import itertools, random, sys, time
from collections import defaultdict

class GF:
    def __init__(self, p, r, c=None):
        self.p, self.r, self.q = p, r, p**r
        if r == 1:
            self.add = lambda a, b: (a+b) % p
            self.sub = lambda a, b: (a-b) % p
            self.mul = lambda a, b: (a*b) % p
            self.elts = list(range(p))
        else:
            assert r == 2 and c is not None      # F_p[t]/(t^2-c), c a non-residue
            self.add = lambda a, b: ((a % p + b % p) % p) + p*(((a//p)+(b//p)) % p)
            self.sub = lambda a, b: ((a % p - b % p) % p) + p*(((a//p)-(b//p)) % p)
            def mul(a, b):
                a0, a1, b0, b1 = a % p, a//p, b % p, b//p
                return ((a0*b0 + c*a1*b1) % p) + p*((a0*b1 + a1*b0) % p)
            self.mul = mul
            self.elts = list(range(p*p))
        self.two = self.add(1, 1)

PV = ['a0','a1','a2','a3','a4','b0','b1','b2','b3','b4']
PE = sorted({tuple(sorted(e)) for i in range(5) for e in
             [('a%d'%i,'a%d'%((i+1)%5)), ('a%d'%i,'b%d'%i), ('b%d'%i,'b%d'%((i+2)%5))]})
assert len(PE) == 15

def build(r, twisted=True, seed=None):
    p = 11
    F = GF(p, r, c=2 if r == 2 else None)     # 2 is a non-residue mod 11
    q, k = F.q, (F.q-1)//10
    nz = [e for e in F.elts if e != 0]
    if seed is not None:
        random.Random(seed).shuffle(nz)
    I = {v: nz[i*k:(i+1)*k] for i, v in enumerate(PV)}
    V = {v: [(x, y) for x in I[v] for y in F.elts if F.mul(F.two, y) != F.mul(x, x)]
         for v in PV}
    cmap = {e: (1 if (twisted and set(e) == {'a3','b3'}) else 0) for e in PE}
    adjc = defaultdict(dict)
    for (u, v) in PE:
        c = cmap[(u, v)]
        for z in V[u]: adjc[z].setdefault(v, set())
        for z in V[v]: adjc[z].setdefault(u, set())
        for (x, y) in V[u]:
            for xp in I[v]:
                yp = F.add(F.sub(F.mul(x, xp), y), c)
                if F.mul(F.two, yp) != F.mul(xp, xp):
                    adjc[(x, y)][v].add((xp, yp))
                    adjc[(xp, yp)][u].add((x, y))
    adj = {z: set().union(*d.values()) if d else set() for z, d in adjc.items()}
    return dict(F=F, q=q, k=k, I=I, V=V, adj=adj, adjc=adjc, cmap=cmap)

def check_basic(D):
    q, k, V, adj, adjc = D['q'], D['k'], D['V'], D['adj'], D['adjc']
    verts = [z for v in PV for z in V[v]]
    n, m = len(verts), len(V['a0'])
    degs = [len(adj[z]) for z in verts]
    ne = sum(degs)//2
    print(f"  n={n} (claim (q-1)^2={(q-1)**2})  m={m} (claim k(q-1)={k*(q-1)})  |E|={ne}")
    print(f"  deg range [{min(degs)},{max(degs)}]; claim [3k-6,3k]=[{3*k-6},{3*k}]; "
          f"(3/10)sqrt(n)={0.3*n**0.5:.2f}; (3/20)n^1.5={0.15*n**1.5:.1f}")
    bad = sum(1 for (u, v) in PE for z in V[u] if not (k-2 <= len(adjc[z][v]) <= k)) \
        + sum(1 for (u, v) in PE for z in V[v] if not (k-2 <= len(adjc[z][u]) <= k))
    print(f"  #(vertex,required-pair) with class-degree outside [k-2,k]: {bad}")
    cn = defaultdict(int)
    for z in verts:
        for a, b in itertools.combinations(sorted(adj[z]), 2):
            cn[(a, b)] += 1
    c4 = sum(1 for vv in cn.values() if vv >= 2)
    tri = sum(1 for (a, b), vv in cn.items() if b in adj[a])
    print(f"  max #common nbrs of a vertex pair = {max(cn.values()) if cn else 0}"
          f" -> #pairs with >=2 (C4 witnesses) = {c4};  #triangles = {tri}")
    print(f"  p=n^-1/2={n**-0.5:.6f};  mean required-pair density="
          f"{sum(len(adjc[z][v]) for (u,v) in PE for z in V[u])/(15*m*m):.6f}")
    return n, m

ORDER = ['a0','a1','a2','a3','a4','b0','b2','b4','b1','b3']
def count_canonical(D, cap=None):
    V, adjc = D['V'], D['adjc']
    pos = {v: i for i, v in enumerate(ORDER)}
    nbrP = defaultdict(list)
    for (u, v) in PE:
        nbrP[u].append(v); nbrP[v].append(u)
    prev = {v: [u for u in nbrP[v] if pos[u] < pos[v]] for v in ORDER}
    total = 0
    found = []
    assign = {}
    L = len(ORDER)
    def rec(i):
        nonlocal total
        if i == L:
            total += 1
            if len(found) < 3:
                found.append(dict(assign))
            return
        v = ORDER[i]
        ps = prev[v]
        if not ps:
            cand = V[v]
        else:
            cand = adjc[assign[ps[0]]][v]
            for u in ps[1:]:
                cand = cand & adjc[assign[u]][v]
                if not cand:
                    return
        for z in cand:
            assign[v] = z
            rec(i+1)
            if cap and total >= cap:
                return
        assign.pop(v, None)
    rec(0)
    return total, found

def verify_copy(D, cp):
    """independently re-check a claimed canonical copy against the edge rule"""
    F, cmap = D['F'], D['cmap']
    ok = True
    for (u, v) in PE:
        (x, y), (xp, yp) = cp[u], cp[v]
        lhs = F.add(y, yp)
        rhs = F.add(F.mul(x, xp), cmap[(u, v)])
        if lhs != rhs:
            ok = False
    return ok

if __name__ == '__main__':
    r = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else None
    for tw in (True, False):
        print("="*72)
        print(f"r={r}  q={11**r}  twisted={tw}  seed={seed}")
        t = time.time()
        D = build(r, twisted=tw, seed=seed)
        check_basic(D)
        tot, found = count_canonical(D)
        print(f"  CANONICAL PETERSEN COPIES = {tot}   [{time.time()-t:.1f}s]")
        for cp in found:
            print("    sample copy:", {k: v for k, v in sorted(cp.items())},
                  "re-verified:", verify_copy(D, cp))
