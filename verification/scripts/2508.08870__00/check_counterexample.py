#!/usr/bin/env python3
"""
Referee verification for attack 2508.08870__00 (Conjecture 1.5 of arXiv:2508.08870,
Alon-Pinchasi: generic d-norm distinct-distances lower bound (d-o(1))n for
d-dimensional point sets).

The writeup claims the conjecture is FALSE for every d>=2, via:
  - planar counterexample: two parallel arithmetic progressions
        P_m = {(i,0): 0<=i<m} u {(i,1): 0<=i<m},  n=2m,
    with at most 3m-2 = (3/2)n - 2 distinct distances in EVERY norm;
  - general-d counterexample: P_m = A_m + S with A_m = {0,...,(m-1)} e_1,
    S = {+-e_2,...,+-e_d}, n = 2(d-1)m, with at most
    (2r^2+1)m - (r^2+1) distinct distances (r = d-1), i.e. coefficient
    r + 1/(2r) = d-1+1/(2(d-1)) < d.

We verify, with EXACT rational arithmetic:
  1. |P-P| and the sign-class count (|P-P|-1)/2 match the writeup's formulas.
  2. The point sets are d-dimensional (affine span = R^d), i.e. they do NOT
     all lie in an affine hyperplane.
  3. For many random centrally-symmetric polytope norms (gauge given by
     ||v|| = max_i |<u_i, v>| with random rational u_i -- a genuine norm when
     the u_i span), the exact number of distinct distances equals/undercuts
     the claimed bound, and its ratio to n stays below d by a fixed gap.
  4. Sanity check of the universal bound D(P) <= (|P-P|-1)/2 on random sets.
"""
import itertools, random
from fractions import Fraction

random.seed(20260903)


def diffset(P):
    return {tuple(a - b for a, b in zip(p, q)) for p in P for q in P if p != q}


def affine_dim(P):
    # rank of {p - p0} over the rationals, by exact Gaussian elimination
    P = [tuple(map(Fraction, p)) for p in P]
    vecs = [tuple(a - b for a, b in zip(p, P[0])) for p in P[1:]]
    rows = [list(v) for v in vecs]
    rank, ncols = 0, len(P[0])
    for col in range(ncols):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pr = rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][col] != 0:
                f = rows[i][col] / pr[col]
                rows[i] = [a - f * b for a, b in zip(rows[i], pr)]
        rank += 1
    return rank


def random_polytope_norm(d, nfacets=25):
    """Random symmetric polytope norm ||v|| = max_i |<u_i,v>| (exact)."""
    U = []
    while True:
        U = [tuple(Fraction(random.randint(-1000, 1000), 997) for _ in range(d))
             for _ in range(nfacets)]
        # ensure the u_i span R^d so this is a norm (definite)
        if affine_dim([tuple([0] * d)] + U) == d:
            return lambda v: max(abs(sum(a * b for a, b in zip(u, v))) for u in U)


def distinct_distances(P, norm):
    return len({norm(v) for v in diffset(P)})


def planar_example(m):
    return [(i, 0) for i in range(m)] + [(i, 1) for i in range(m)]


def general_example(d, m):
    r = d - 1
    P = []
    for i in range(m):
        for j in range(r):
            for s in (1, -1):
                p = [0] * d
                p[0] = i
                p[1 + j] = s
                P.append(tuple(p))
    return P


print("=== 1. Planar counterexample: two parallel APs ===")
for m in [3, 5, 10, 25, 60]:
    P = planar_example(m)
    n = len(P)
    D = diffset(P)
    classes = len(D) // 2  # nonzero diffs pair v/-v; 0 not in diffset here
    assert n == 2 * m
    assert len(D) == 6 * m - 4, (m, len(D))          # (2m-1)*3 - 1 (0 excluded)
    assert classes == 3 * m - 2, (m, classes)
    assert affine_dim(P) == 2                        # noncollinear
    best = 0
    for trial in range(6):
        norm = random_polytope_norm(2)
        dd = distinct_distances(P, norm)
        assert dd <= 3 * m - 2, (m, dd)
        best = max(best, dd)
    print(f"  m={m:3d} n={n:4d}: |P-P\\0|={len(D)}, sign classes={classes} "
          f"= 1.5n-2; max distinct distances over 6 random norms = {best} "
          f"(ratio {best/n:.3f}n; conjecture claims >= (2-o(1))n)")

print("\n=== 2. General-d counterexample P = A_m + S ===")
for d, m in [(2, 10), (3, 6), (3, 12), (4, 5), (5, 4)]:
    r = d - 1
    P = general_example(d, m)
    n = len(P)
    assert n == 2 * r * m
    D = diffset(P)
    assert len(D) == (2 * m - 1) * (2 * r * r + 1) - 1, (d, m, len(D))
    classes = len(D) // 2
    bound = (2 * r * r + 1) * m - (r * r + 1)
    assert classes == bound, (d, m, classes, bound)
    assert affine_dim(P) == d
    norm = random_polytope_norm(d)
    dd = distinct_distances(P, norm)
    assert dd <= bound
    coef = Fraction(bound, n)
    print(f"  d={d} m={m:3d} n={n:4d}: |P-P\\0|={len(D)}, classes={classes}, "
          f"bound coeff={float(coef):.4f} (= d-1+1/(2(d-1)) - O(1/n); d={d}); "
          f"random-norm distinct distances={dd} (ratio {dd/n:.3f}n)")

print("\n=== 3. Gap check: bound/n vs conjectured d ===")
for d in range(2, 8):
    r = d - 1
    coef = r + Fraction(1, 2 * r)
    print(f"  d={d}: asymptotic coefficient {float(coef):.4f} < d, "
          f"gap = {float(d - coef):.4f} (claimed 1 - 1/(2(d-1)) = "
          f"{1 - 1/(2*r):.4f})")
    assert d - coef == 1 - Fraction(1, 2 * r) > 0

print("\n=== 4. Sanity: universal bound D <= (|P-P|-1)/2 on random sets ===")
for trial in range(20):
    d = random.choice([2, 3])
    P = list({tuple(random.randint(-6, 6) for _ in range(d))
              for _ in range(random.randint(4, 12))})
    norm = random_polytope_norm(d)
    D = diffset(P)
    assert distinct_distances(P, norm) <= len(D) // 2
print("  ok (20 random sets)")

print("\nAll checks passed.")
