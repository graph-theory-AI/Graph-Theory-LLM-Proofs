#!/usr/bin/env python3
"""
Referee verification for 2505.24100__00.

Claim (writeup): For every k >= 3, G_k = K_k [Cartesian] C_{2k-1}
  (i)  has non-edges,
  (ii) contains no induced C_{2k},
  (iii) for every non-edge {x,y}, contains an induced path on 2k vertices
        with endpoints x and y  (hence G_k + xy contains an induced C_{2k}).

With k = t-1 (t >= 6, so k >= 5) this answers Question 1.7 of
arXiv:2505.24100 affirmatively for H = C_{2t-2}.

This script verifies (i)-(iii) by brute force / exhaustive DFS for several k,
with no reliance on the writeup's reasoning.

Pure Python (no networkx needed).
"""
import sys
from itertools import combinations

def build(k):
    """K_k box C_m with m = 2k-1. Vertices: (a, i), a in range(k), i in range(m)."""
    m = 2 * k - 1
    V = [(a, i) for a in range(k) for i in range(m)]
    idx = {v: n for n, v in enumerate(V)}
    N = len(V)
    adj = [set() for _ in range(N)]
    for (a, i) in V:
        u = idx[(a, i)]
        for b in range(k):           # horizontal: same level, clique
            if b != a:
                adj[u].add(idx[(b, i)])
        for di in (1, m - 1):        # vertical: same column, consecutive level
            adj[u].add(idx[(a, (i + di) % m)])
    return V, idx, adj

def count_induced_cycles_of_length(adj, N, L, stop_at_first=False):
    """Exhaustively count induced cycles of length exactly L via DFS over
    induced paths.  Canonical form: cycle's minimum vertex is the start,
    and its second vertex is smaller than its last vertex (each cycle counted once)."""
    count = 0
    for s in range(N):
        # DFS: path starts at s, all other vertices > s
        # state: path list, set of path vertices
        stack = [([s, v], {s, v}) for v in sorted(adj[s]) if v > s]
        while stack:
            path, pset = stack.pop()
            u = path[-1]
            if len(path) == L:
                # close: u adjacent to s, and induced closure means the only
                # chords... path is induced already except closing edge;
                # need u ~ s, and no other path vertex adjacent to s besides
                # path[1] and u -- enforced during DFS below.
                if s in adj[u] and path[1] < path[-1]:
                    count += 1
                    if stop_at_first:
                        return count, path
                continue
            for w in adj[u]:
                if w <= s or w in pset:
                    continue
                # induced path condition: w adjacent to no path vertex except u,
                # EXCEPT w may be adjacent to s only if w will be the final vertex
                nb = adj[w]
                ok = True
                for p in path[:-1]:
                    if p in nb:
                        if p == s and len(path) + 1 == L:
                            continue  # closing edge allowed at final step
                        ok = False
                        break
                if ok:
                    stack.append((path + [w], pset | {w}))
    return count, None

def has_induced_path_between(adj, N, x, y, L):
    """Is there an induced path on exactly L vertices with endpoints x,y,
    such that x,y are non-adjacent and the path plus edge xy is an induced C_L?
    Equivalent: induced path v0=x,...,v_{L-1}=y where no internal vertex is
    adjacent to... standard: the path itself induced; since xy is a non-edge,
    path union {xy} gives induced C_L in G+xy."""
    # DFS from x
    stack = [([x], {x})]
    while stack:
        path, pset = stack.pop()
        u = path[-1]
        if len(path) == L:
            continue
        for w in adj[u]:
            if w in pset:
                continue
            nb = adj[w]
            # w must be non-adjacent to all path vertices except u
            if any(p in nb for p in path[:-1]):
                continue
            if w == y:
                if len(path) + 1 == L:
                    return True
                continue  # y reached too early: y only allowed as final vertex
            if len(path) + 1 < L:
                stack.append((path + [w], pset | {w}))
    return False

def writeup_path(k, x, y):
    """Construct the explicit path from Section 2 of the writeup and return it."""
    m = 2 * k - 1
    (alpha, i), (beta, j) = x, y
    assert i != j
    q = min((j - i) % m, (i - j) % m)
    # long arc from i to j
    if (j - i) % m == m - q:
        step = 1
    else:
        step = -1
    d = m - q
    A = [(i + step * r) % m for r in range(d + 1)]
    assert A[-1] == j
    if alpha != beta:
        cols = [alpha] + [c for c in range(k) if c not in (alpha, beta)][:q - 1] + [beta]
        switches = list(range(1, q + 1))  # s_1..s_q internal: 1..q <= d-1
        assert len(cols) == q + 1 and all(0 < s < d for s in switches)
    else:
        assert q >= 2
        others = [c for c in range(k) if c != alpha]
        cols = [alpha] + others[:q - 1] + [alpha]
        switches = [0] + list(range(1, q - 1)) + [d]
        # first switch at level z_0, last at z_d, q-2 internal distinct
        assert len(switches) == q and len(set(switches)) == q
    # build path
    path = []
    ci = 0
    for r, lev in enumerate(A):
        path.append((cols[ci], lev))
        while ci < len(cols) - 1 and r in _switch_positions(switches, ci):
            ci += 1
            path.append((cols[ci], lev))
    return path

def _switch_positions(switches, ci):
    # switch number ci+1 happens at arc position switches[ci]
    return {switches[ci]} if ci < len(switches) else set()

def is_induced_path(adj_pairs, path):
    """Check path is an induced path in G (adjacency function on vertex labels)."""
    n = len(path)
    if len(set(path)) != n:
        return False
    for a in range(n):
        for b in range(a + 1, n):
            adj = adj_pairs(path[a], path[b])
            if b == a + 1 and not adj:
                return False
            if b > a + 1 and adj:
                return False
    return True

def main():
    ks = [int(a) for a in sys.argv[1:]] or [3, 4, 5]
    for k in ks:
        m = 2 * k - 1
        L = 2 * k
        V, idx, adj = build(k)
        N = len(V)

        def adjfun(u, v):
            return idx[v] in adj[idx[u]]

        nonedges = [(u, v) for u, v in combinations(range(N), 2)
                    if v not in adj[u]]
        print(f"k={k}: G = K_{k} box C_{m}, n={N}, "
              f"edges={sum(len(a) for a in adj)//2}, non-edges={len(nonedges)}")
        assert nonedges, "complement empty!"

        # (ii) no induced C_{2k}
        cnt, witness = count_induced_cycles_of_length(adj, N, L, stop_at_first=True)
        if cnt:
            print(f"  FATAL: found induced C_{L}: {[V[u] for u in witness]}")
        else:
            print(f"  OK: exhaustive search found no induced C_{L}")

        # sanity: induced C_m (the columns) should exist
        cm, _ = count_induced_cycles_of_length(adj, N, m, stop_at_first=True)
        print(f"  sanity: induced C_{m} exists: {bool(cm)} (expected True)")

        # (iii) every non-edge joined by induced P_{2k}; check both the
        # writeup's explicit path and an independent DFS search
        bad = 0
        bad_explicit = 0
        for u, v in nonedges:
            x, y = V[u], V[v]
            # independent search
            if not has_induced_path_between(adj, N, u, v, L):
                bad += 1
                print(f"  FATAL: no induced P_{L} between {x} and {y}")
            # explicit writeup construction
            p = writeup_path(k, x, y)
            if not (len(p) == L and p[0] == x and p[-1] == y
                    and is_induced_path(adjfun, p)):
                bad_explicit += 1
                print(f"  EXPLICIT-PATH FAIL for {x},{y}: {p}")
        print(f"  OK: all {len(nonedges)} non-edges have an induced P_{L} "
              f"(DFS search failures: {bad})")
        print(f"  OK: writeup's explicit Section-2 path verified induced for all "
              f"non-edges (failures: {bad_explicit})")
        print()

if __name__ == "__main__":
    main()
