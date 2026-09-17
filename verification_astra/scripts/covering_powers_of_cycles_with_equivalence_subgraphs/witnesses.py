#!/usr/bin/env python3
"""Print and verify explicit small witnesses of the writeup's Section-2 cover."""
from construction_check import cover_divisible, check, edges_cycle_power

for (n, k) in [(8, 3), (12, 3), (16, 7), (24, 7), (32, 15)]:
    L, r = cover_divisible(n, k)
    print(f"--- n={n} k={k}: {len(L)} layers (trivial bounds: k+1={k+1}, 2k={2*k}) ---")
    for i, parts in enumerate(L):
        print("  layer", i, [sorted(Q) for Q in parts])
    msg = check(n, k, L, "witness")
    print("  valid equivalence cover?", "YES" if msg is None else msg,
          " |E| =", len(edges_cycle_power(n, k)))
