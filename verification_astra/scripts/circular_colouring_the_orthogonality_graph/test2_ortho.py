"""Finite subgraphs of the orthogonality graph O (lines through 0 in R^3, adjacent iff
perpendicular).

Checks:
  (A) the projection colouring of section 3 of the writeup: pick a generic unit z, set
      v_L = u_L - (u_L.z) z with u_L.z > 0, colour by angle on a circle of circumference 4;
      verify every edge gets circular distance > 1, report lambda = min distance and the
      resulting bound chi_c <= 4/lambda < 4.
  (B) exact chi_c of random induced subgraphs, checked against 4 and against the
      vertex-count bound chi_c <= 4 - 1/floor((n+1)/4).
  (C) the Peres 33-direction Kochen-Specker configuration: verify chi = 4 and exhibit an
      explicit homomorphism to a circular clique K_{p/q} with p/q < 4.
"""
import random
from fractions import Fraction
from itertools import combinations
from math import gcd, atan2, pi, sqrt
import numpy as np

from circ import chi_c, to_nbrs, hom_exists, common_neighbour_property

random.seed(11)
np.random.seed(11)


from geom import primitive_lines, peres_directions, ortho_graph, projection_check

# ---------- run ----------
print("=== (A)+(B) random finite subgraphs of O from integer vectors ===")
LINES = primitive_lines(3)
print(f"lines with coordinates in [-3,3]: {len(LINES)}")
U_all, E_all = ortho_graph(LINES)
print(f"orthogonality graph on them: {len(E_all)} edges")

adj_all = {i: set() for i in range(len(LINES))}
for i, j in E_all:
    adj_all[i].add(j)
    adj_all[j].add(i)

bad_prop2 = 0
bad_count = 0
worst = Fraction(0)
worst_info = None
results = []
attempts = 0
while len(results) < 60 and attempts < 40000:
    attempts += 1
    n = random.randint(6, 13)
    # grow a connected-ish random vertex subset
    start = random.randrange(len(LINES))
    S = {start}
    frontier = set(adj_all[start])
    while len(S) < n and frontier:
        v = random.choice(sorted(frontier))
        S.add(v)
        frontier |= adj_all[v]
        frontier -= S
    S = sorted(S)
    if len(S) < 6:
        continue
    idx = {v: i for i, v in enumerate(S)}
    sub_edges = [(idx[i], idx[j]) for i, j in E_all if i in idx and j in idx]
    if not sub_edges:
        continue
    m = len(S)
    nbrs = to_nbrs(m, sub_edges)
    c = chi_c(nbrs, m)
    k = (m + 1) // 4
    bound = Fraction(4) - Fraction(1, k) if k >= 1 else Fraction(4)
    ok_prop2 = c < 4
    ok_count = c <= bound
    if not ok_prop2:
        bad_prop2 += 1
        print("   PROP 2 VIOLATION", m, sub_edges, c)
    if not ok_count:
        bad_count += 1
        print("   COUNT-BOUND VIOLATION", m, sub_edges, c, bound)
    if c > worst:
        worst = c
        worst_info = (m, len(sub_edges))
    results.append((m, len(sub_edges), c, bound))

print(f"subgraphs tested: {len(results)}; Prop.2 violations: {bad_prop2}; count-bound violations: {bad_count}")
print(f"largest chi_c seen among them: {worst} (n={worst_info[0]}, m={worst_info[1]} edges)")
from collections import Counter
print("chi_c multiset:", Counter(str(r[2]) for r in results))

print("\n=== (A) projection colouring on the whole integer-vector orthogonality graph ===")
lam = projection_check(U_all, E_all, trials=60)
print(f"best lambda over random z: {lam:.6f}  ->  chi_c <= 4/lambda = {4/lam:.6f}  (< 4 iff lambda > 1)")

print("\n=== (C) Peres 33-direction Kochen-Specker configuration ===")
P = peres_directions()
UP, EP = ortho_graph(P)
print(f"vertices: {len(P)}, edges: {len(EP)}")
lamP = projection_check(UP, EP, trials=400)
print(f"best lambda over random z: {lamP:.6f} -> chi_c <= {4/lamP:.6f}")
nbrsP = to_nbrs(len(P), EP)
print("common-neighbour property:", common_neighbour_property(nbrsP, len(P)))
# triangles / KS property
tri = sum(1 for a, b, c in combinations(range(len(P)), 3)
          if (nbrsP[a] >> b & 1) and (nbrsP[a] >> c & 1) and (nbrsP[b] >> c & 1))
print("triangles (orthogonal bases):", tri)
for f in [Fraction(3, 1), Fraction(7, 2), Fraction(11, 3), Fraction(15, 4), Fraction(19, 5),
          Fraction(23, 6), Fraction(31, 8), Fraction(4, 1)]:
    ok = hom_exists(nbrsP, len(P), f.numerator, f.denominator)
    print(f"   Peres -> K_{{{f.numerator}/{f.denominator}}} ({float(f):.4f}): {ok}")
