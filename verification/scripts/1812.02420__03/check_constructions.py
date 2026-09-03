#!/usr/bin/env python3
"""Verify the writeup's positive constructions for Problem 5.40 (arXiv:1812.02420).

Property to verify for a digraph D on vertex set C([k],b):
    for EVERY nonempty family F of b-subsets:
        D[F] acyclic  <=>  intersection(F) != empty
(Digons count as directed cycles; digraphs loopless, per the source paper.)

Checks:
  1. k=b+1 (directed (b+1)-cycle on the complements of singletons), b=1..5: exhaustive.
  2. b=1 (complete bidirected digraph on singletons), k=1..5: exhaustive.
  3. b=2 construction of the writeup (cyclic order; digon between disjoint pairs,
     A={x,a} -> B={x,c} iff a <_x c where <_x reads the cyclic order starting
     after x): exhaustive over ALL 2^C(k,2)-1 nonempty families for k=2..6.
"""
import itertools, sys
sys.setrecursionlimit(10000)

def has_dicycle(verts, arcs):
    adj = {v: [] for v in verts}
    vs = set(verts)
    for (i, j) in arcs:
        if i in vs and j in vs:
            adj[i].append(j)
    color = {v: 0 for v in verts}
    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and dfs(v):
                return True
        color[u] = 2
        return False
    return any(color[v] == 0 and dfs(v) for v in verts)

def check_property(vertices, arcs, max_family=None):
    """Exhaustively check the iff over all nonempty subfamilies. Returns list of violations."""
    viol = []
    n = len(vertices)
    for r in range(1, (max_family or n) + 1):
        for fam in itertools.combinations(vertices, r):
            nonempty = bool(frozenset.intersection(*fam))
            acyclic = not has_dicycle(fam, arcs)
            if acyclic != nonempty:
                viol.append((fam, nonempty, acyclic))
    return viol

# ---------- 1. k = b+1 ----------
print("== k = b+1 : directed cycle ==")
for b in range(1, 6):
    k = b + 1
    Bs = [frozenset(set(range(1, k+1)) - {i}) for i in range(1, k+1)]
    arcs = {(Bs[i], Bs[(i+1) % k]) for i in range(k)}
    viol = check_property(Bs, arcs)
    print(f"  b={b}, k={k}: {'OK' if not viol else f'VIOLATIONS {viol[:3]}'}")
    assert not viol

# ---------- 2. b = 1 ----------
print("== b = 1 : complete bidirected digraph ==")
for k in range(1, 6):
    Bs = [frozenset({i}) for i in range(1, k+1)]
    arcs = {(A, B) for A in Bs for B in Bs if A != B}
    viol = check_property(Bs, arcs)
    print(f"  b=1, k={k}: {'OK' if not viol else f'VIOLATIONS {viol[:3]}'}")
    assert not viol

# ---------- 3. b = 2 ----------
print("== b = 2 : writeup's cyclic-order construction ==")
def build_b2(k):
    elems = list(range(1, k+1))          # cyclic order 1,2,...,k
    pos = {e: i for i, e in enumerate(elems)}
    def less_x(x, a, c):
        # order on [k]\{x} starting immediately after x in cyclic order
        ra = (pos[a] - pos[x]) % k
        rc = (pos[c] - pos[x]) % k
        return ra < rc
    Bs = [frozenset(p) for p in itertools.combinations(elems, 2)]
    arcs = set()
    for A, B in itertools.combinations(Bs, 2):
        if not (A & B):
            arcs.add((A, B)); arcs.add((B, A))     # digon
        else:
            (x,) = A & B
            (a,) = A - {x}
            (c,) = B - {x}
            if less_x(x, a, c):
                arcs.add((A, B))
            else:
                arcs.add((B, A))
    return Bs, arcs

for k in range(2, 7):
    Bs, arcs = build_b2(k)
    viol = check_property(Bs, arcs)
    n_fams = 2**len(Bs) - 1
    print(f"  b=2, k={k}: {n_fams} families checked: "
          f"{'OK' if not viol else f'VIOLATIONS e.g. {viol[:2]}'}")
    assert not viol

print("\nAll positive constructions VERIFIED exhaustively.")
