"""Sanity test: does the writeup's twisted-affine-polarity method 'prove too much'?
C5 is PROVED countable by Conlon-Fox-Sudakov-Zhao [7]/Example 2.12, so the same
construction applied to F = C5 must NOT kill all canonical copies.
Generic version of the construction for an arbitrary F and one twisted edge."""
import sys, itertools
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/',1)[0])
from construction2 import GF

def build_generic(F_edges, F_verts, r, twist_edge, p=11):
    FF = GF(p, r, c=2 if r == 2 else None)
    q = FF.q
    t = len(F_verts)
    assert (q-1) % t == 0, (q, t)
    k = (q-1)//t
    nz = [e for e in FF.elts if e != 0]
    I = {v: nz[i*k:(i+1)*k] for i, v in enumerate(F_verts)}
    V = {v: [(x, y) for x in I[v] for y in FF.elts if FF.mul(FF.two, y) != FF.mul(x, x)]
         for v in F_verts}
    cmap = {e: (1 if set(e) == set(twist_edge) else 0) for e in F_edges}
    adjc = defaultdict(dict)
    for (u, v) in F_edges:
        c = cmap[(u, v)]
        for z in V[u]: adjc[z].setdefault(v, set())
        for z in V[v]: adjc[z].setdefault(u, set())
        for (x, y) in V[u]:
            for xp in I[v]:
                yp = FF.add(FF.sub(FF.mul(x, xp), y), c)
                if FF.mul(FF.two, yp) != FF.mul(xp, xp):
                    adjc[(x, y)][v].add((xp, yp)); adjc[(xp, yp)][u].add((x, y))
    return FF, q, k, V, adjc

def count(F_edges, F_verts, V, adjc):
    nbr = defaultdict(list)
    for u, v in F_edges:
        nbr[u].append(v); nbr[v].append(u)
    order = list(F_verts)
    pos = {v: i for i, v in enumerate(order)}
    prev = {v: [u for u in nbr[v] if pos[u] < pos[v]] for v in order}
    tot = 0; assign = {}
    def rec(i):
        nonlocal tot
        if i == len(order):
            tot += 1; return
        v = order[i]; ps = prev[v]
        cand = V[v] if not ps else adjc[assign[ps[0]]][v]
        for u in ps[1:]:
            cand = cand & adjc[assign[u]][v]
        for z in cand:
            assign[v] = z; rec(i+1)
        assign.pop(v, None)
    rec(0)
    return tot

for r in (1, 2):
    Fv = ['v0','v1','v2','v3','v4']
    Fe = [('v%d'%i, 'v%d'%((i+1) % 5)) for i in range(5)]
    for tw in [('v0','v1'), None]:
        FF, q, k, V, adjc = build_generic(Fe, Fv, r, tw if tw else ('zz','zz'))
        n = sum(len(V[v]) for v in Fv); m = len(V['v0'])
        c = count(Fe, Fv, V, adjc)
        pred = m**5 * (k/m)**5
        print(f"C5, q={q}, k={k}, n={n}, m={m}, twisted={tw is not None}: "
              f"canonical C5 copies = {c}  (regular-approximation prediction ~ {pred:.1f})")
