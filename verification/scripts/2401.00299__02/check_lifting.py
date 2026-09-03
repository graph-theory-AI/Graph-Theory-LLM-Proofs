"""Verification script for 2401.00299__02.

Checks, by brute force on small cases:
  1. f_{0,2}(m): number of partitions of Q_m into singletons and coordinate
     2-faces (squares), for m = 1..4; distribution of a_L over singleton sets L.
  2. f_2(d): number of partitions of Q_d into coordinate 2-faces, d = 2..5.
  3. The lifting construction of the writeup: for m = 2, 3, take every ordered
     4-tuple of {0,2}-partitions of Q_m sharing the same singleton set L
     (for the best L) and build the claimed partition of Q_{m+2}; verify that
     each result is a genuine partition of Q_{m+2} into coordinate 2-faces and
     that distinct 4-tuples give distinct partitions (injectivity).
  4. The inequalities f_2(m+2) >= a_L^4 >= (f_{0,2}(m)/2^{2^m})^4 numerically,
     and the upper bound f_2(d) <= (d+1)^{2^{d-1}}.
"""
from itertools import combinations, product
from collections import defaultdict
from math import comb

def squares(d):
    """All coordinate 2-faces of Q_d as frozensets of vertices (ints 0..2^d-1)."""
    out = []
    for i, j in combinations(range(d), 2):
        bi, bj = 1 << i, 1 << j
        for base in range(1 << d):
            if base & bi or base & bj:
                continue
            out.append(frozenset({base, base | bi, base | bj, base | bi | bj}))
    return out

def partitions_02(m):
    """All partitions of Q_m into singletons + squares.
    Returned as list of (frozenset_of_squares, frozenset_of_singletons)."""
    sqs = squares(m)
    nverts = 1 << m
    # DFS over collections of pairwise-disjoint squares (rest = singletons).
    results = []
    def rec(start, used, chosen):
        results.append((frozenset(chosen),
                        frozenset(v for v in range(nverts) if v not in used)))
        for k in range(start, len(sqs)):
            s = sqs[k]
            if used & s:
                continue
            rec(k + 1, used | s, chosen + [s])
    rec(0, frozenset(), [])
    return results

def f2_partitions(d):
    """All partitions of Q_d into squares (exact cover), as frozensets of squares."""
    sqs = squares(d)
    nverts = 1 << d
    # index: squares containing vertex v
    by_vertex = defaultdict(list)
    for s in sqs:
        for v in s:
            by_vertex[v].append(s)
    results = []
    def rec(used, chosen):
        if len(used) == nverts:
            results.append(frozenset(chosen))
            return
        v = min(x for x in range(nverts) if x not in used)  # smallest uncovered
        for s in by_vertex[v]:
            if not (used & s):
                rec(used | s, chosen + [s])
    rec(frozenset(), [])
    return results

print("=== f_{0,2}(m) and a_L distribution ===")
best = {}
p02 = {}
for m in [1, 2, 3, 4]:
    parts = partitions_02(m)
    p02[m] = parts
    byL = defaultdict(int)
    for sq, L in parts:
        byL[L] += 1
    aL, Lstar = max((v, k) for k, v in byL.items())
    best[m] = (Lstar, aL)
    print(f"m={m}: f_02={len(parts)}, #distinct L={len(byL)} (<= 2^{1<<m}={2**(1<<m)}), "
          f"max a_L={aL} at |L|={len(Lstar)}")

print()
print("=== f_2(d) by exact cover ===")
f2 = {}
for d in [2, 3, 4, 5]:
    parts = f2_partitions(d)
    f2[d] = parts
    n = 1 << (d - 1)
    print(f"d={d}: f_2={len(parts)}  (upper bound (d+1)^n = {(d+1)**n})")
    assert len(parts) <= (d + 1) ** n, "UPPER BOUND VIOLATED"
    # each partition uses exactly 2^d / 4 squares
    for P in parts:
        assert len(P) == (1 << d) // 4

print()
print("=== Lifting construction: build, validate, injectivity ===")
def lift(tuple4, L, m):
    """Given (P_00,P_01,P_10,P_11) partitions of Q_m (square-sets) with singleton
    set L, build the square partition of Q_{m+2} = Q_m x Q_2
    (vertex encoding: x + (z << m))."""
    out = []
    for zi, (sqset, _) in enumerate(tuple4):
        for C in sqset:
            out.append(frozenset(x + (zi << m) for x in C))
    for x in L:
        out.append(frozenset(x + (z << m) for z in range(4)))
    return frozenset(out)

def is_square_partition(P, dtot):
    """Check P is a partition of Q_dtot into coordinate 2-faces."""
    allv = set()
    sqset = set(squares(dtot))
    for part in P:
        if part not in sqset:
            return False
        if allv & part:
            return False
        allv |= part
    return len(allv) == (1 << dtot)

for m in [2, 3]:
    Lstar, aL = best[m]
    pool = [(sq, L) for sq, L in p02[m] if L == Lstar]
    assert len(pool) == aL
    images = set()
    for tuple4 in product(pool, repeat=4):
        P = lift(tuple4, Lstar, m)
        assert is_square_partition(P, m + 2), f"NOT A VALID SQUARE PARTITION (m={m})"
        images.add(P)
    print(f"m={m}: a_L={aL}, built {aL**4} tuples -> {len(images)} distinct valid "
          f"square partitions of Q_{m+2}; injective: {len(images) == aL**4}")
    assert len(images) == aL ** 4, "INJECTIVITY FAILS"
    # constructed partitions are among the exhaustive list
    allf2 = set(f2[m + 2])
    assert images <= allf2, "constructed partition not found in exhaustive census"
    print(f"      all images appear in exhaustive f_2({m+2}) census "
          f"({len(images)} <= {len(allf2)}); lemma bound f_2({m+2}) >= a_L^4: "
          f"{len(allf2)} >= {aL**4}: {len(allf2) >= aL**4}")

print()
print("=== Lemma inequality (2) with pigeonhole, numerically ===")
for m in [1, 2, 3]:
    fv = len(p02[m])
    rhs = (fv / 2 ** (1 << m)) ** 4
    lhs = len(f2[m + 2])
    print(f"m={m}: f_2(m+2)={lhs} >= (f_02(m)/2^(2^m))^4 = {rhs:.6g}: {lhs >= rhs}")
    assert lhs >= rhs

print()
print("All checks passed.")
