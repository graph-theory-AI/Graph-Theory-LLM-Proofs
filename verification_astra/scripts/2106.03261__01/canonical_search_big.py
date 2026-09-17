"""Exhaustive canonical-Petersen-copy search in G_q for larger q (two-stage pruning).

Same construction as graph_check.py.  Reports, for the twisted graph (c_ij=1) and
for the control (all c=0):
  - number of canonical 'Petersen minus ij' configurations
  - the distribution of <I,J> = y_I + y_J + x_I x_J over them
  - number of canonical Petersen copies
Also re-verifies C4-freeness (max codegree <= 1) with a fast numpy routine.
"""
import sys, itertools
from collections import defaultdict
import numpy as np

LAB = "abcdefghij"
KN = {'a': (1,2), 'b': (1,3), 'c': (1,4), 'd': (4,5), 'e': (3,5),
      'f': (2,5), 'g': (2,3), 'h': (2,4), 'i': (3,4), 'j': (1,5)}
EDGES = [(u, v) for u, v in itertools.combinations(LAB, 2) if not (set(KN[u]) & set(KN[v]))]
ESET = {frozenset(e) for e in EDGES}
ADJ = {r: sorted(s for s in LAB if frozenset((r, s)) in ESET) for r in LAB}
assert all(len(ADJ[r]) == 3 for r in LAB) and len(EDGES) == 15

def cst(r, s, tw): return 1 if (tw and {r, s} == {'i', 'j'}) else 0

def c4_check(q, tw):
    idx = {r: k for k, r in enumerate(LAB)}
    T = {r: [x for x in range(q) if x % 10 == idx[r]] for r in LAB}
    cls = {x: r for r in LAB for x in T[r]}
    adj = defaultdict(list)
    for x in range(q):
        r = cls[x]
        for y in range(q):
            for s in ADJ[r]:
                c = cst(r, s, tw)
                for xp in T[s]:
                    adj[(x, y)].append((xp, (c - y - x * xp) % q))
    seen = defaultdict(int)
    mx = 0
    for w, nb in adj.items():
        for a, b in itertools.combinations(sorted(nb), 2):
            seen[(a, b)] += 1
            if seen[(a, b)] > mx: mx = seen[(a, b)]
    m = sum(len(v) for v in adj.values()) // 2
    return mx, m, max(len(v) for v in adj.values())

def search(q, tw):
    idx = {r: k for k, r in enumerate(LAB)}
    T = {r: np.array([x for x in range(q) if x % 10 == idx[r]], dtype=np.int64) for r in LAB}
    inc = {r: np.zeros(q, dtype=bool) for r in LAB}
    for r in LAB: inc[r][T[r]] = True
    inv = np.array([0] + [pow(t, q - 2, q) for t in range(1, q)], dtype=np.int64)
    parents = [('d','a','b'), ('e','a','c'), ('f','b','c'),
               ('g','c','d'), ('h','b','e'), ('i','a','f'), ('j','g','h')]
    def clos(x1,y1,c1, x2,y2,c2):
        d = (x1 - x2) % q
        z = (((c1 - c2) - (y1 - y2)) % q * inv[d]) % q
        t = (c1 - y1 - x1 * z) % q
        return z, t, (d == 0)
    ys = np.arange(q, dtype=np.int64)
    Xb = np.repeat(T['b'], q); Yb = np.tile(ys, len(T['b']))
    Xc = np.repeat(T['c'], q); Yc = np.tile(ys, len(T['c']))
    tot_minus, tot_full = 0, 0
    dist = defaultdict(int)
    for xa in T['a']:
        for ya in ys:
            # stage 1: valid B (D = kappa(A,B) in T_d)
            zd, td, bad = clos(xa, ya, cst('a','d',tw), Xb, Yb, cst('b','d',tw))
            ok1 = (~bad) & inc['d'][zd]
            if not ok1.any(): continue
            xb_, yb_, xd_, yd_ = Xb[ok1], Yb[ok1], zd[ok1], td[ok1]
            for k in range(len(xb_)):
                xb, yb, xd, yd = xb_[k], yb_[k], xd_[k], yd_[k]
                P = {'a': (np.full(Xc.shape, xa), np.full(Xc.shape, ya)),
                     'b': (np.full(Xc.shape, xb), np.full(Xc.shape, yb)),
                     'c': (Xc, Yc),
                     'd': (np.full(Xc.shape, xd), np.full(Xc.shape, yd))}
                ok = np.ones(Xc.shape, dtype=bool)
                for (new, p1, p2) in parents[1:]:
                    x1, y1 = P[p1]; x2, y2 = P[p2]
                    z, t, bd = clos(x1, y1, cst(p1,new,tw), x2, y2, cst(p2,new,tw))
                    ok &= (~bd) & inc[new][z % q]
                    P[new] = (z, t)
                    if not ok.any(): break
                if not ok.any(): continue
                xi, yi = P['i']; xj, yj = P['j']
                val = (yi + yj + xi * xj) % q
                tot_minus += int(ok.sum())
                for v in np.unique(val[ok]): dist[int(v)] += int((val[ok] == v).sum())
                tot_full += int((ok & (val == cst('i','j',tw))).sum())
    return tot_minus, tot_full, dict(sorted(dist.items()))

if __name__ == "__main__":
    for q in [int(a) for a in sys.argv[1:]] or [101]:
        for tw in (True, False):
            mx, m, dmax = c4_check(q, tw)
            tm, tf, dd = search(q, tw)
            print(f"q={q} twisted={tw}: N={q*q} maxcodeg={mx} (C4-free={mx<=1}) e(G)={m} "
                  f"e/N^1.5={m/(q*q)**1.5:.6f} Delta={dmax} (sqrt N={q})")
            print(f"   Petersen-minus-ij canonical configs = {tm};  <I,J> distribution = {dd}")
            print(f"   canonical PETERSEN copies = {tf}   (needs <I,J> = {cst('i','j',tw)})")
