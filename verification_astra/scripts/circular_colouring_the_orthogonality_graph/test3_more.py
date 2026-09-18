"""Further checks (each result printed as soon as it is obtained).

 (1) the 25-ray Peres-type Kochen-Specker configuration (a non-3-colourable finite
     subgraph of O): its exact chi_c -- must be < 4 by Prop. 2, and <= 4 - 1/6 by the
     vertex-count bound.
 (2) larger finite subgraphs of O built from integer vectors: homomorphism into
     circular cliques of ratio < 4 (Prop. 2).
 (3) K_{(4k-1)/k} has the common-neighbour property and chi_c = 4 - 1/k (Lemma 2 is
     not vacuous), for k = 1,2,3.
 (4) equation (3) of section 4: in K_{(4k-1)/k}, N(a) cap N(a+2k-1) = {a+3k-1}.
"""
import sys
from fractions import Fraction
from math import gcd

from circ import (chi_c, to_nbrs, hom_exists, common_neighbour_property,
                  circ_clique_adj, fractions_upto)
from geom import peres_directions, ortho_graph, primitive_lines, projection_check


def p(*a):
    print(*a)
    sys.stdout.flush()


p("=== (1) the 25-ray Kochen-Specker configuration ===")
P = peres_directions()
UP, EP = ortho_graph(P)
n = len(P)
nbrsP = to_nbrs(n, EP)
p(f"n={n}, edges={len(EP)}")
lo, hi = Fraction(3), Fraction(7, 2)
cands = [f for f in fractions_upto(n) if lo < f <= hi]
p(f"candidate ratios in (3, 7/2] with numerator <= {n}: {[str(c) for c in cands]}")
exact = None
for f in cands:
    ok = hom_exists(nbrsP, n, f.numerator, f.denominator)
    p(f"   -> K_{{{f.numerator}/{f.denominator}}} ({float(f):.5f}): {ok}")
    if ok:
        exact = f
        break
p(f"chi_c(KS25) = {exact} = {float(exact):.6f}   (chi_c > 3 since K_3 hom fails, see test2)")
k = (n + 1) // 4
p(f"Prop. 2 (chi_c < 4): {exact < 4}")
p(f"count bound 4 - 1/{k} = {Fraction(4)-Fraction(1,k)}: {exact <= Fraction(4)-Fraction(1,k)}")
lam = projection_check(UP, EP, trials=600)
p(f"projection colouring: best lambda = {lam:.6f} (>1 required) -> chi_c <= {4/lam:.6f}")

p("\n=== (2) larger subgraphs of O from integer vectors ===")
for B in (2, 3):
    L = primitive_lines(B)
    U, E = ortho_graph(L)
    m = len(L)
    nb = to_nbrs(m, E)
    lam = projection_check(U, E, trials=300)
    p(f"B={B}: {m} lines, {len(E)} edges; common-neighbour property: "
      f"{common_neighbour_property(nb, m)}; projection lambda = {lam:.6f} "
      f"-> chi_c <= {4/lam:.6f}")
    for f in [Fraction(3, 1), Fraction(7, 2)]:
        ok = hom_exists(nb, m, f.numerator, f.denominator)
        p(f"    -> K_{{{f.numerator}/{f.denominator}}} ({float(f):.4f}): {ok}")

p("\n=== (3) circular cliques K_{(4k-1)/k} ===")
for k in (1, 2, 3):
    pp, q = 4 * k - 1, k
    adj = circ_clique_adj(pp, q)
    p(f"k={k}: K_{{{pp}/{q}}} common-neighbour property: "
      f"{common_neighbour_property(adj, pp)}, chi_c = {chi_c(adj, pp)} "
      f"(expected {Fraction(pp,q)})")

p("\n=== (4) section 4 identity: N(a) cap N(a+2k-1) = {a+3k-1} in K_{(4k-1)/k} ===")
allok = True
for k in range(1, 12):
    pp, q = 4 * k - 1, k
    adj = circ_clique_adj(pp, q)
    for a in range(pp):
        b = (a + 2 * k - 1) % pp
        if adj[a] & adj[b] != 1 << ((a + 3 * k - 1) % pp):
            allok = False
            p(f"   FAIL k={k} a={a}")
p(f"identity holds for k = 1..11: {allok}")
