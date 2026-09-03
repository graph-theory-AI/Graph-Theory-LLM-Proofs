#!/usr/bin/env python3
"""
Second verification pass for attack 1601.01886__00 (needs networkx).

  (V1) Validate the EST 3-branch criterion pathwidth solver against the exact
       subset-DP vertex-separation on ALL non-isomorphic trees with <= 10
       vertices, and check Corollary 3 (lambda(T) <= 2 pw(T) - 1, pw >= 1)
       by brute force on the same trees.
  (V2) Exact subset-DP pathwidth of R_3 (n = 22): expect 2.
  (V3) Path-deletion claims used in the writeup's Lemmas 4 and 5 lower bounds,
       checked over ALL paths (vertex pairs) of the tree:
         - in R_h (2 <= h <= 7): every path avoids some canonical copy of R_{h-2};
         - in D_h (1 <= h <= 6): every path avoids some canonical copy of R_{h-1}.
"""
import itertools, sys
from math import inf
sys.setrecursionlimit(1000000)
from verify import build_R, build_D, pathwidth_dp, pathwidth_est, lambda_brute

# ---------------------------------------------------------------- (V1)
import networkx as nx
print("== (V1) EST vs subset-DP + Corollary 3, all trees n<=10 ==")
total = 0
worst = {}
for n in range(2, 11):
    for T in nx.nonisomorphic_trees(n):
        adj = {v: set(T.neighbors(v)) for v in T.nodes}
        a = pathwidth_dp(adj)
        b = pathwidth_est(adj)
        assert a == b, f"EST mismatch n={n} dp={a} est={b} {sorted(T.edges)}"
        l = lambda_brute(adj)
        assert l <= 2 * a - 1, f"Cor3 violated n={n} pw={a} lambda={l} {sorted(T.edges)}"
        worst[a] = max(worst.get(a, -1), l)
        total += 1
print(f"  {total} trees checked: EST solver == subset DP on all;"
      f" lambda <= 2 pw - 1 on all.")
print(f"  max lambda observed per pathwidth: {worst} (Corollary 3 bound: pw p -> 2p-1)")

# ---------------------------------------------------------------- (V2)
print("== (V2) exact subset-DP pathwidth of R_3 (n=22) ==")
adjR3, _ = build_R(3)
pwv = pathwidth_dp(adjR3)
print(f"  pw(R_3) = {pwv} (expect 2)  {'OK' if pwv == 2 else 'FAIL'}")
assert pwv == 2

# ---------------------------------------------------------------- (V3)
def build_R_with_copies(h):
    """Build R_h; return adj, root, and dict level j -> list of vertex sets of
    the canonical copies of R_j inside R_h."""
    counter = itertools.count()
    adj = {}
    copies = {j: [] for j in range(h + 1)}
    def newv():
        v = next(counter); adj[v] = set(); return v
    def add(u, v): adj[u].add(v); adj[v].add(u)
    def rec(hh):
        if hh == 0:
            r = newv()
            copies[0].append(frozenset([r]))
            return r, frozenset([r])
        s1, c1 = rec(hh - 1)
        s2, c2 = rec(hh - 1)
        x = newv(); r = newv()
        add(r, x); add(x, s1); add(x, s2)
        vs = c1 | c2 | {x, r}
        copies[hh].append(frozenset(vs))
        return r, frozenset(vs)
    root, _ = rec(h)
    return adj, root, copies

def tree_path_vertices(adj, u, v):
    # BFS parents from u
    from collections import deque
    par = {u: None}
    dq = deque([u])
    while dq:
        a = dq.popleft()
        if a == v: break
        for b in adj[a]:
            if b not in par:
                par[b] = a; dq.append(b)
    path = [v]
    while par[path[-1]] is not None:
        path.append(par[path[-1]])
    return set(path)

print("== (V3) every path leaves an intact canonical sub-copy ==")
for h in range(2, 8):
    adj, root, copies = build_R_with_copies(h)
    targets = copies[h - 2]
    verts = sorted(adj)
    bad = 0
    for u, v in itertools.combinations(verts, 2):
        pv = tree_path_vertices(adj, u, v)
        if not any(pv.isdisjoint(c) for c in targets):
            bad += 1
    # also single-vertex paths
    for u in verts:
        if not any(u not in c for c in targets):
            bad += 1
    print(f"  R_{h} (n={len(verts)}): paths violating 'some R_{h-2} copy intact': {bad}"
          f"  {'OK' if bad == 0 else 'FAIL'}")
    assert bad == 0

def build_D_with_copies(h):
    adjL, rL, copL = build_R_with_copies(h)
    adjR_, rR, copR = build_R_with_copies(h)
    off = max(adjL) + 1
    adj = {v: set(ns) for v, ns in adjL.items()}
    for v, ns in adjR_.items():
        adj[v + off] = {u + off for u in ns}
    adj[rL].add(rR + off); adj[rR + off].add(rL)
    copies = {}
    for j in copL:
        copies[j] = list(copL[j]) + [frozenset(x + off for x in c) for c in copR[j]]
    return adj, copies

for h in range(1, 7):
    adj, copies = build_D_with_copies(h)
    targets = copies[h - 1]
    verts = sorted(adj)
    bad = 0
    for u, v in itertools.combinations(verts, 2):
        pv = tree_path_vertices(adj, u, v)
        if not any(pv.isdisjoint(c) for c in targets):
            bad += 1
    print(f"  D_{h} (n={len(verts)}): paths violating 'some R_{h-1} copy intact': {bad}"
          f"  {'OK' if bad == 0 else 'FAIL'}")
    assert bad == 0

print("VERIFY2: ALL CHECKS PASSED")
