"""(a) Extra sanity checks on the z3 encoding, stressing circular cliques themselves.
   (b) Push the lower bound: O_4 (primitive integer directions of sup-norm <= 4).

Reported statuses are z3's: 'sat', 'unsat' or 'unknown' (timeout). Only 'unsat' counts
as a negative result.
"""
import sys
from fractions import Fraction
from itertools import combinations
from test6_exact import graph, z3_hom, p_


def clique_edges(p, q):
    return [(a, b) for a in range(p) for b in range(a + 1, p) if q <= (b - a) % p <= p - q]


p_("=== encoding sanity checks on circular cliques ===")
for (p1, q1), (p2, q2), expect in [((7, 2), (7, 2), "sat"),
                                   ((11, 3), (7, 2), "unsat"),
                                   ((7, 2), (11, 3), "sat"),
                                   ((15, 4), (11, 3), "unsat"),
                                   ((11, 3), (15, 4), "sat"),
                                   ((4, 1), (15, 4), "unsat"),
                                   ((5, 2), (5, 2), "sat"),
                                   ((7, 3), (5, 2), "sat"),
                                   ((5, 2), (7, 3), "unsat")]:
    E = clique_edges(p1, q1)
    r = str(z3_hom(p1, E, p2, q2, timeout_ms=120000))
    p_(f"   K_{{{p1}/{q1}}} -> K_{{{p2}/{q2}}} : {r}  (expect {expect})  "
       f"{'OK' if r == expect else '*** MISMATCH ***'}")

p_("\n=== (b) O_4 ===")
V, E = graph(4)
n = len(V)
p_(f"O_4: n={n} lines, |E|={len(E)} edges")
for f in [Fraction(11, 3), Fraction(15, 4), Fraction(19, 5), Fraction(4, 1)]:
    r = z3_hom(n, E, f.numerator, f.denominator, timeout_ms=900000)
    p_(f"   -> K_{{{f.numerator}/{f.denominator}}} = {float(f):.6f} : {r}")
