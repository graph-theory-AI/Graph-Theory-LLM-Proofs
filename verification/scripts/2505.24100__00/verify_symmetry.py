#!/usr/bin/env python3
"""
Symmetry-reduced verification for larger k (referee check for 2505.24100__00).

G_k = K_k box C_m, m = 2k-1.  Aut(G_k) contains S_k (permuting columns) x D_m
(rotating/reflecting levels); this subgroup acts transitively on vertices, and
every unordered non-edge is equivalent under it to one of:
    {(0,0),(0,q)} for q = 2..k-1   (same column), or
    {(0,0),(1,q)} for q = 1..k-1   (different columns).
Hence:
  * G_k has an induced C_{2k} iff it has one through vertex (0,0);
  * the non-edge/induced-P_{2k} property holds for all non-edges iff it holds
    for the 2k-3 representatives above.
The writeup's explicit Section-2 path is still checked for ALL non-edges
(that check is cheap).
"""
import sys
from verify import (build, has_induced_path_between, writeup_path,
                    is_induced_path)

def exists_induced_cycle_through_0(adj, N, L):
    """Induced cycle of length exactly L through vertex 0 (no minimality
    restriction on other vertices). Returns witness or None."""
    s = 0
    stack = [([s, v], {s, v}) for v in adj[s]]
    while stack:
        path, pset = stack.pop()
        u = path[-1]
        if len(path) == L:
            if s in adj[u] and path[1] < path[-1]:
                return path
            continue
        for w in adj[u]:
            if w == s or w in pset:
                continue
            nb = adj[w]
            ok = True
            for p in path[:-1]:
                if p in nb:
                    if p == s and len(path) + 1 == L:
                        continue
                    ok = False
                    break
            if ok:
                stack.append((path + [w], pset | {w}))
    return None

def main():
    ks = [int(a) for a in sys.argv[1:]] or [7]
    for k in ks:
        m = 2 * k - 1
        L = 2 * k
        V, idx, adj = build(k)
        N = len(V)

        def adjfun(u, v):
            return idx[v] in adj[idx[u]]

        print(f"k={k}: G = K_{k} box C_{m}, n={N} (symmetry-reduced checks)")
        w = exists_induced_cycle_through_0(adj, N, L)
        if w:
            print(f"  FATAL: induced C_{L} through (0,0): {[V[u] for u in w]}")
        else:
            print(f"  OK: no induced C_{L} through (0,0); by vertex-transitivity, "
                  f"G has no induced C_{L}")
        wm = exists_induced_cycle_through_0(adj, N, m)
        print(f"  sanity: induced C_{m} through (0,0) exists: {wm is not None} "
              f"(expected True)")

        reps = ([((0, 0), (0, q)) for q in range(2, k)]
                + [((0, 0), (1, q)) for q in range(1, k)])
        for x, y in reps:
            assert not adjfun(x, y), (x, y)
            ok = has_induced_path_between(adj, N, idx[x], idx[y], L)
            print(f"  non-edge orbit rep {x},{y}: induced P_{L} found: {ok}")
            if not ok:
                print("  FATAL")
        # explicit writeup path for ALL non-edges (cheap, no symmetry needed)
        from itertools import combinations
        bad = 0
        tot = 0
        for u, v in combinations(range(N), 2):
            if v in adj[u]:
                continue
            tot += 1
            p = writeup_path(k, V[u], V[v])
            if not (len(p) == L and p[0] == V[u] and p[-1] == V[v]
                    and is_induced_path(adjfun, p)):
                bad += 1
                print(f"  EXPLICIT-PATH FAIL for {V[u]},{V[v]}")
        print(f"  OK: writeup's explicit path induced for all {tot} non-edges "
              f"(failures: {bad})")
        print()

if __name__ == "__main__":
    main()
