#!/usr/bin/env python3
"""Exhaustive check of Conjecture 9.1 (arXiv:2506.07264) on all connected
unicyclic graphs of order n <= NMAX whose unique cycle has odd length.

For each such graph G (obtained as tree + one extra edge, over all
non-isomorphic trees and all non-edges), compute s+(G), s-(G) and verify:
  k = 3 mod 4  =>  s+ > n > s-
  k = 1 mod 4  =>  s+ < n < s-
"""
import itertools
import networkx as nx
import numpy as np

NMAX = 12
TOL = 1e-9

def unique_cycle_length(G):
    """G is unicyclic (connected, |E|=|V|); return length of its unique cycle."""
    cyc = nx.find_cycle(G)
    return len(cyc)

total = 0
odd_total = 0
min_margin = None
min_example = None
violations = []

for n in range(3, NMAX + 1):
    seen = set()
    count_n = 0
    for T in nx.nonisomorphic_trees(n):
        nodes = list(T.nodes())
        for u, v in itertools.combinations(nodes, 2):
            if T.has_edge(u, v):
                continue
            G = T.copy()
            G.add_edge(u, v)
            # canonical certificate to dedupe (not required for correctness)
            cert = nx.weisfeiler_lehman_graph_hash(G, iterations=4)
            key = (cert, tuple(sorted(dict(G.degree()).values())))
            if key in seen:
                # WL hash can rarely collide; still verify (cheap) rather than skip
                pass
            seen.add(key)
            total += 1
            k = unique_cycle_length(G)
            if k % 2 == 0:
                continue
            odd_total += 1
            count_n += 1
            A = nx.to_numpy_array(G)
            ev = np.linalg.eigvalsh(A)
            sp = float(np.sum(ev[ev > TOL] ** 2))
            sm = float(np.sum(ev[ev < -TOL] ** 2))
            # sanity: s+ + s- = 2|E| = 2n
            assert abs(sp + sm - 2 * n) < 1e-6, (n, k, sp, sm)
            if k % 4 == 3:
                ok = sp > n + TOL and n > sm + TOL
                margin = min(sp - n, n - sm)
            else:  # k % 4 == 1
                ok = sp < n - TOL and n < sm - TOL
                margin = min(n - sp, sm - n)
            if not ok:
                violations.append((n, k, sorted(G.edges()), sp, sm))
            if min_margin is None or margin < min_margin:
                min_margin = margin
                min_example = (n, k, sp, sm)
    print(f"n={n}: checked {count_n} odd-cycle unicyclic graphs (with iso duplicates)")

print(f"\nTotal unicyclic graphs generated (with duplicates): {total}")
print(f"Odd-cycle cases checked: {odd_total}")
print(f"Violations: {len(violations)}")
for v in violations[:10]:
    print("  VIOLATION:", v)
print(f"Minimum margin over all checks: {min_margin:.6g} at (n,k,s+,s-)={min_example}")
