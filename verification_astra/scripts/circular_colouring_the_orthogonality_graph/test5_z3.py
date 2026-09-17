"""Fully independent check with z3, and with the orthogonality graph rebuilt from scratch
in EXACT integer arithmetic (no floating point anywhere).

For the finite subgraph O_B of O spanned by all lines through the origin with primitive
integer direction vectors of sup-norm <= B, decide G -> K_{p/q} for several p/q.

G -> K_{p/q} means: x : V -> {0,...,p-1} with q <= (x_v - x_u) mod p <= p-q on every edge.
"""
import sys
from math import gcd
from itertools import combinations
from fractions import Fraction
from z3 import Int, Solver, And, Or, sat, unsat


def p_(*a):
    print(*a)
    sys.stdout.flush()


def lines(B):
    """primitive integer direction vectors, one per line, exact integer arithmetic."""
    seen = set()
    for x in range(-B, B + 1):
        for y in range(-B, B + 1):
            for z in range(-B, B + 1):
                if (x, y, z) == (0, 0, 0):
                    continue
                g = gcd(gcd(abs(x), abs(y)), abs(z))
                v = (x // g, y // g, z // g)
                seen.add(max(v, tuple(-c for c in v)))
    return sorted(seen)


def graph(B):
    V = lines(B)
    E = [(i, j) for i, j in combinations(range(len(V)), 2)
         if V[i][0] * V[j][0] + V[i][1] * V[j][1] + V[i][2] * V[j][2] == 0]
    return V, E


def z3_hom(n, E, p, q, timeout_ms=600000):
    s = Solver()
    s.set("timeout", timeout_ms)
    x = [Int(f"x{i}") for i in range(n)]
    for v in x:
        s.add(And(v >= 0, v <= p - 1))
    s.add(x[0] == 0)  # translation automorphism of K_{p/q}
    for u, v in E:
        d = x[v] - x[u]
        s.add(Or(And(d >= q, d <= p - q), And(d <= -q, d >= -(p - q))))
    r = s.check()
    return r


# sanity: C5 -> K_{5/2} sat, C5 -> K_{7/3} unsat; K4 -> K_{4/1} sat, K4 -> K_{11/3} unsat
C5 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
K4 = list(combinations(range(4), 2))
p_("sanity checks:")
p_(f"  C5 -> K_5/2 : {z3_hom(5, C5, 5, 2)}   (expect sat)")
p_(f"  C5 -> K_7/3 : {z3_hom(5, C5, 7, 3)}   (expect unsat)")
p_(f"  K4 -> K_4/1 : {z3_hom(4, K4, 4, 1)}   (expect sat)")
p_(f"  K4 -> K_11/3: {z3_hom(4, K4, 11, 3)}  (expect unsat)")

for B in (2, 3):
    V, E = graph(B)
    n = len(V)
    p_(f"\n=== O_{B}: lines with primitive integer direction, sup-norm <= {B} ===")
    p_(f"n = {n} vertices, {len(E)} edges (exact integer dot products)")
    for f in [Fraction(3, 1), Fraction(7, 2), Fraction(18, 5), Fraction(11, 3),
              Fraction(15, 4), Fraction(4, 1)]:
        r = z3_hom(n, E, f.numerator, f.denominator)
        p_(f"   -> K_{{{f.numerator}/{f.denominator}}} = {float(f):.5f} : {r}")
