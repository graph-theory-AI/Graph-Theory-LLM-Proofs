"""Exact chi_c of O_2 (the 49 lines with primitive integer direction of sup-norm <= 2),
via z3, by scanning every candidate ratio p/q (lowest terms, p <= 49) in (7/2, 11/3].

Self-contained: rebuilds the graph in exact integer arithmetic.
"""
import sys
from fractions import Fraction
from math import gcd
from itertools import combinations
from z3 import Int, Solver, And, Or


def p_(*a):
    print(*a)
    sys.stdout.flush()


def lines(B):
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


def z3_hom(n, E, p, q, timeout_ms=300000):
    s = Solver()
    s.set("timeout", timeout_ms)
    x = [Int(f"x{i}") for i in range(n)]
    for v in x:
        s.add(And(v >= 0, v <= p - 1))
    s.add(x[0] == 0)
    for u, v in E:
        d = x[v] - x[u]
        s.add(Or(And(d >= q, d <= p - q), And(d <= -q, d >= -(p - q))))
    return s.check()


if __name__ == "__main__":
    V, E = graph(2)
    n = len(V)
    p_(f"O_2: n={n}, |E|={len(E)}")
    cands = sorted({Fraction(p, q) for q in range(1, n // 2 + 1)
                    for p in range(2 * q, n + 1)
                    if gcd(p, q) == 1 and Fraction(7, 2) < Fraction(p, q) <= Fraction(11, 3)})
    p_(f"{len(cands)} candidate ratios in (7/2, 11/3]")
    for f in cands:
        r = z3_hom(n, E, f.numerator, f.denominator)
        p_(f"   K_{{{f.numerator}/{f.denominator}}} = {float(f):.6f} : {r}")
        if str(r) == "sat":
            p_(f"\n==> chi_c(O_2) = {f} = {float(f):.6f}")
            break
