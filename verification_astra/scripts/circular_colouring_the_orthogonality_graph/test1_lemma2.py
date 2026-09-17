"""Sanity checks on chi_c, then a brute-force / random test of Lemma 2 (finite case):

   G has the common-neighbour property (every pair of vertices, possibly equal,
   has a common neighbour) and chi_c(G) < 4  ==>  chi_c(G) = 4 - 1/k, k a positive integer.
"""
import random
from fractions import Fraction
from itertools import combinations
from circ import chi_c, to_nbrs, common_neighbour_property, circ_clique_adj

random.seed(20260917)

# ---------- sanity checks ----------
def graph_from_edges(n, edges):
    return to_nbrs(n, edges), n

tests = []
# C5
tests.append(("C5", 5, [(i, (i + 1) % 5) for i in range(5)], Fraction(5, 2)))
# K4
tests.append(("K4", 4, list(combinations(range(4), 2)), Fraction(4, 1)))
# C7^2 = K_{7/2}
K72 = [(a, b) for a in range(7) for b in range(a + 1, 7) if 2 <= (b - a) % 7 <= 5]
tests.append(("K_{7/2}", 7, K72, Fraction(7, 2)))
# Petersen
pet = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + \
      [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
tests.append(("Petersen", 10, pet, Fraction(3, 1)))
# K_{11/3}
K113 = [(a, b) for a in range(11) for b in range(a + 1, 11) if 3 <= (b - a) % 11 <= 8]
tests.append(("K_{11/3}", 11, K113, Fraction(11, 3)))

print("=== sanity checks on chi_c ===")
for name, n, edges, expect in tests:
    got = chi_c(*graph_from_edges(n, edges))
    print(f"{name:10s} chi_c = {got}  expected {expect}  {'OK' if got == expect else 'MISMATCH'}")

# ---------- Lemma 2 finite case ----------
def allowed(v):
    """is v of the form 4 - 1/k (k >= 1) or >= 4 ?"""
    if v >= 4:
        return True
    r = 4 - v            # = 1/k
    return r.numerator == 1


print("\n=== Lemma 2 finite case: random graphs with the common-neighbour property ===")
found = 0
tested = 0
violations = []
spectrum = {}
for trial in range(200000):
    n = random.randint(4, 10)
    p = random.uniform(0.35, 0.85)
    edges = [(u, v) for u, v in combinations(range(n), 2) if random.random() < p]
    nbrs = to_nbrs(n, edges)
    if not common_neighbour_property(nbrs, n):
        continue
    found += 1
    if found > 4000:
        break
    c = chi_c(nbrs, n)
    tested += 1
    spectrum[c] = spectrum.get(c, 0) + 1
    if not allowed(c):
        violations.append((n, edges, c))

print(f"graphs with the common-neighbour property tested: {tested}")
print("observed chi_c values (value: count):")
for k in sorted(spectrum):
    print(f"   {k} = {float(k):.4f}   x{spectrum[k]}")
print(f"violations of Lemma 2: {len(violations)}")
for v in violations[:5]:
    print("   VIOLATION", v)

# ---------- exhaustive check on all graphs with <= 6 vertices ----------
print("\n=== exhaustive: ALL graphs on 5 and 6 vertices with the common-neighbour property ===")
for n in (5, 6):
    pairs = list(combinations(range(n), 2))
    bad = 0
    cnt = 0
    spec = {}
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        nbrs = to_nbrs(n, edges)
        if not common_neighbour_property(nbrs, n):
            continue
        cnt += 1
        c = chi_c(nbrs, n)
        spec[c] = spec.get(c, 0) + 1
        if not allowed(c):
            bad += 1
            print("   VIOLATION", n, edges, c)
    print(f"n={n}: {cnt} graphs with the property; spectrum {sorted((str(k), v) for k, v in spec.items())}; violations={bad}")
