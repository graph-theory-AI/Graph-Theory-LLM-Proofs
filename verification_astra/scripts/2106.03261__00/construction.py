"""Explicit construction of G_q from attacks_retry/2106.03261__00/output.md and
brute-force verification of all its claimed properties.

q = 11^r, k = (q-1)/10, F_q^* split into 10 classes I_v of size k (one per Petersen
vertex).  V_v = {(x,y) : x in I_v, 2y != x^2}.  For uv in E(Petersen),
(x,y) ~ (x',y')  iff  y + y' = x x' + c_uv,  with c = 1 exactly on {a3,b3}.
"""
import itertools, random, sys
from collections import defaultdict

# ---------------- finite field GF(11^r), r = 1 or 2 ----------------
class GF:
    def __init__(self, p, r, modpoly=None):
        self.p, self.r, self.q = p, r, p**r
        if r == 1:
            self.mul = lambda a, b: (a*b) % p
            self.add = lambda a, b: (a+b) % p
            self.sub = lambda a, b: (a-b) % p
            self.elts = list(range(p))
        else:
            assert r == 2
            # GF(11^2) = F_11[t]/(t^2 - c) with c a non-residue; element a0 + a1 t <-> a0 + p*a1
            self.c = modpoly
            def add(a, b):
                return ((a % p + b % p) % p) + p*(((a//p) + (b//p)) % p)
            def sub(a, b):
                return ((a % p - b % p) % p) + p*(((a//p) - (b//p)) % p)
            def mul(a, b):
                a0, a1 = a % p, a//p
                b0, b1 = b % p, b//p
                return ((a0*b0 + self.c*a1*b1) % p) + p*((a0*b1 + a1*b0) % p)
            self.add, self.sub, self.mul = add, sub, mul
            self.elts = list(range(p*p))
        self.zero = 0
        self.one = 1
        # additive inverse and the element "2"
        self.two = self.add(self.one, self.one)

PETERSEN_V = ['a0','a1','a2','a3','a4','b0','b1','b2','b3','b4']
def petersen_edges():
    E = []
    for i in range(5):
        E.append(('a%d'%i, 'a%d'%((i+1) % 5)))
        E.append(('a%d'%i, 'b%d'%i))
        E.append(('b%d'%i, 'b%d'%((i+2) % 5)))
    return sorted({tuple(sorted(e)) for e in E})

PE = petersen_edges()
assert len(PE) == 15

def build(q_r, twisted=True, shuffle_classes=False, seed=0):
    p = 11
    F = GF(p, q_r, modpoly=2 if q_r == 2 else None)   # t^2 = 2, 2 is a non-residue mod 11
    q = F.q
    k = (q-1)//10
    assert 10*k == q-1
    nz = [e for e in F.elts if e != 0]
    if shuffle_classes:
        random.Random(seed).shuffle(nz)
    I = {v: set(nz[i*k:(i+1)*k]) for i, v in enumerate(PETERSEN_V)}
    xclass = {}
    for v in PETERSEN_V:
        for x in I[v]:
            xclass[x] = v
    # vertices
    V = {}
    for v in PETERSEN_V:
        lst = []
        for x in I[v]:
            x2 = F.mul(x, x)
            for y in F.elts:
                if F.mul(F.two, y) != x2:
                    lst.append((x, y))
        V[v] = lst
    cmap = {}
    for e in PE:
        cmap[e] = F.one if (twisted and set(e) == {'a3','b3'}) else F.zero
    adjP = defaultdict(set)
    for u, v in PE:
        adjP[u].add(v); adjP[v].add(u)
    # adjacency
    adj = defaultdict(set)
    for (u, v) in PE:
        c = cmap[(u, v)]
        for (x, y) in V[u]:
            for xp in I[v]:
                # y' = x x' - y + c
                yp = F.add(F.sub(F.mul(x, xp), y), c)
                if F.mul(F.two, yp) != F.mul(xp, xp):
                    adj[(x, y)].add((xp, yp))
                    adj[(xp, yp)].add((x, y))
    return dict(F=F, q=q, k=k, I=I, xclass=xclass, V=V, adj=adj, adjP=adjP, cmap=cmap)

def check_basic(D):
    F, q, k, V, adj = D['F'], D['q'], D['k'], D['V'], D['adj']
    verts = [z for v in PETERSEN_V for z in V[v]]
    n = len(verts)
    m = len(V['a0'])
    degs = [len(adj[z]) for z in verts]
    ne = sum(degs)//2
    print(f"q={q} k={k} n={n} (expected (q-1)^2={(q-1)**2}) m={m} (expected k(q-1)={k*(q-1)})")
    print(f"  degrees: min={min(degs)} max={max(degs)}  claimed range [3k-6,3k]=[{3*k-6},{3*k}]")
    print(f"  edges={ne}  (3/20)n^1.5={0.15*n**1.5:.1f}  Delta<=(3/10)sqrt(n)={0.3*n**0.5:.1f}")
    ok_deg = all(max(3*k-6, 0) <= d <= 3*k for d in degs)
    # per-pair degree
    bad = 0
    for (u, v) in PE:
        for z in V[u]:
            d = len(adj[z] & set(V[v]))
            if not (k-2 <= d <= k):
                bad += 1
    print(f"  per-required-pair degree outside [k-2,k]: {bad}")
    # C4-free / triangle-free via common-neighbour counts
    cn = defaultdict(int)
    for z in verts:
        nb = sorted(adj[z])
        for a, b in itertools.combinations(nb, 2):
            cn[(a, b)] += 1
    maxcn = max(cn.values()) if cn else 0
    c4 = sum(1 for kk, vv in cn.items() if vv >= 2)
    tri = sum(1 for (a, b), vv in cn.items() if b in adj[a])
    print(f"  max common neighbours over non-adjacent-in-list pairs = {maxcn}; pairs with >=2 common nbrs (=> C4) : {c4}")
    print(f"  triangles (counted once) : {tri}")
    # density of required pairs
    dens = [len(adj[z] & set(V[v]))/m for (u, v) in PE[:1] for z in V[u][:1]]
    print(f"  p = n^-1/2 = {n**-0.5:.6f}; typical pair density ~ {k/m:.6f}")
    return dict(n=n, m=m, ne=ne, c4=c4, tri=tri, ok_deg=ok_deg, verts=verts)

def count_canonical(D, limit=None):
    """Backtracking count of canonical Petersen copies (one vertex per class)."""
    V, adj = D['V'], D['adj']
    order = ['a0','a1','a2','a3','a4','b0','b1','b2','b3','b4']
    pos = {v: i for i, v in enumerate(order)}
    prev_nbrs = {v: [u for (u, w) in [(e[0], e[1]) for e in PE] + [(e[1], e[0]) for e in PE]
                     if w == v and pos[u] < pos[v]] for v in order}
    total = 0
    assign = {}
    def rec(i):
        nonlocal total
        if i == len(order):
            total += 1
            return
        v = order[i]
        cand = None
        for u in prev_nbrs[v]:
            s = adj[assign[u]] & set(V[v])
            cand = s if cand is None else (cand & s)
        if cand is None:
            cand = V[v]
        for z in cand:
            assign[v] = z
            rec(i+1)
        assign.pop(v, None)
    rec(0)
    return total

if __name__ == '__main__':
    for r in (1, 2):
        for tw in (True, False):
            print("="*70)
            print(f"r={r}  twisted={tw}")
            D = build(r, twisted=tw)
            info = check_basic(D)
            cc = count_canonical(D)
            print(f"  CANONICAL PETERSEN COPIES = {cc}")
