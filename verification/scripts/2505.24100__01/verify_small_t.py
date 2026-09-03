#!/usr/bin/env python3
"""
Repair check for the writeup's step 4 citation slip (2505.24100__01).

The writeup cites Theorem 1.6 of arXiv:2505.24100 for 3 <= t <= 13, but the
paper states Theorem 1.6 only for t >= 5.  The cases t = 3 (C_4) and t = 4
(C_6) are instead covered by Observation 1.5 of the same paper:
  - the icosahedron is C_4-induced-saturated;
  - C_5 x C_5 (Cartesian product) is C_6-induced-saturated.
Induced saturation implies the deletion-only property needed by Question 1.8.
Here we verify the deletion-only property of both graphs by brute force.

Run:  uv run --with networkx python3 verify_small_t.py
"""

import sys
import networkx as nx


def has_chordless_cycle_of_length(G, m):
    return any(len(c) == m for c in nx.chordless_cycles(G, length_bound=m))


def check(name, G, m):
    n = G.number_of_nodes()
    print(f"  --- {name}: n = {n}, target C_{m} ---")
    if has_chordless_cycle_of_length(G, m):
        print(f"    FATAL: contains an induced C_{m}")
        return False
    print(f"    no induced C_{m}: OK")
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if not has_chordless_cycle_of_length(H, m):
            print(f"    FATAL: G - {e} has no induced C_{m}")
            return False
    print(f"    G - e has an induced C_{m} for all {G.number_of_edges()} "
          f"edges: OK")
    return True


def main():
    ok = check("icosahedron (t=3)", nx.icosahedral_graph(), 4)
    c5 = nx.cycle_graph(5)
    ok &= check("C5 x C5 Cartesian product (t=4)",
                nx.cartesian_product(c5, c5), 6)
    print()
    print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
