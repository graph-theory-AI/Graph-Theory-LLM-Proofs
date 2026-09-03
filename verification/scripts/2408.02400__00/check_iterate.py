"""Directly verify the first Mycielski iterate of the seed:
G_5 = mu(G) on 27 vertices must have omega=4, zeta=5, chi=8 (k=5 instance).
Also confirm G_5 has an optimal cochromatic partition with an independent part.
"""
import itertools
from graphlib import (from_edges, mycielski, zeta, chromatic_number,
                      clique_number, independence_number,
                      has_independent_part_optimal)

n = 13
D = {1, 5, 8, 12}
edges = [(x, y) for x in range(n) for y in range(x + 1, n)
         if (x - y) % n not in D]           # G = complement of circulant F
G = from_edges(n, edges)

M = mycielski(G)
print(f"|V(mu(G))| = {M[0]}  (claimed 27)")
print(f"omega(mu(G)) = {clique_number(M)}  (claimed 4)")
print(f"alpha(mu(G)) = {independence_number(M)}")
z = zeta(M, ub=6)
print(f"zeta(mu(G)) = {z}  (claimed 5)")
c = chromatic_number(M)
print(f"chi(mu(G)) = {c}  (claimed 8)")
print(f"optimal cochromatic partition with independent part exists: "
      f"{has_independent_part_optimal(M)}  (claimed True)")
