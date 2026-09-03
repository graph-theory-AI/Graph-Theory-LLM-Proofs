#!/usr/bin/env python3
"""Verify the counterexample constructions in attacks/2604.09449__00/output.md.

The paper (arXiv:2604.09449, both v1 and v2, Section 1) defines, for a subgraph
G' of G and h: E(G) -> R^k:

    f_h(G') = || h(G') - (e(G')/e(G)) * h(G) ||_1 ,   h(G') = sum_{e in G'} h(e).

For a perfect matching M of K_{n,n}: e(M) = n, e(K_{n,n}) = n^2, so the
centering coefficient is 1/n — exactly definition (1) of the writeup.

The writeup takes n = k (k even) and claims, for EVERY perfect matching M_pi:
  (A) h(x_i y_j) = s_j e_i          (s_j = +1 for j<=k/2 else -1):  f_h = k
  (B) h(x_i y_j) = e_i if j<=k/2 else 0:                            f_h = k/2
  (C) h(x_i y_j) = s_j u_i, u_i = (e_i - 1/k)/(2(1-1/k)):           f_h = k/(2(1-1/k))
      with all row sums and column sums of h equal to 0.
It also claims ||h(e)||_1 <= 1 in all three cases, and for (A) the l2 norm of
the matching sum is sqrt(k) and the l_infty norm is 1.
"""
import itertools
from fractions import Fraction

def l1(v):  return sum(abs(x) for x in v)
def l2sq(v): return sum(x * x for x in v)
def linf(v): return max(abs(x) for x in v)

def f_h(h, matching, k, n):
    """f_h(M) = || sum_{e in M} h(e) - (1/n) sum_{all e} h(e) ||_1 (exact rationals)."""
    tot = [Fraction(0)] * k
    for (i, j), vec in h.items():
        for c in range(k):
            tot[c] += vec[c]
    msum = [Fraction(0)] * k
    for (i, j) in matching:
        for c in range(k):
            msum[c] += h[(i, j)][c]
    return l1([msum[c] - Fraction(tot[c], n) for c in range(k)])

def basis(i, k, scale=Fraction(1)):
    return tuple(scale if c == i else Fraction(0) for c in range(k))

def run(k):
    assert k % 2 == 0
    n = k
    s = [Fraction(1) if j < k // 2 else Fraction(-1) for j in range(k)]

    # (A) signed construction
    hA = {(i, j): tuple(s[j] if c == i else Fraction(0) for c in range(k))
          for i in range(n) for j in range(n)}
    # (B) nonnegative construction
    hB = {(i, j): (basis(i, k) if j < k // 2 else tuple(Fraction(0) for _ in range(k)))
          for i in range(n) for j in range(n)}
    # (C) row/column-balanced construction
    denom = 2 * (1 - Fraction(1, k))
    u = [tuple(((Fraction(1) if c == i else Fraction(0)) - Fraction(1, k)) / denom
               for c in range(k)) for i in range(k)]
    hC = {(i, j): tuple(s[j] * u[i][c] for c in range(k))
          for i in range(n) for j in range(n)}

    # edge-label norm constraint ||h(e)||_1 <= 1
    for name, h in (("A", hA), ("B", hB), ("C", hC)):
        mx = max(l1(v) for v in h.values())
        assert mx <= 1, (name, mx)
        print(f"k={k} [{name}] max ||h(e)||_1 = {mx}  (<=1 OK)")

    # (C): row and column sums vanish
    for i in range(n):
        rs = [sum(hC[(i, j)][c] for j in range(n)) for c in range(k)]
        assert all(x == 0 for x in rs)
    for j in range(n):
        cs = [sum(hC[(i, j)][c] for i in range(n)) for c in range(k)]
        assert all(x == 0 for x in cs)
    print(f"k={k} [C] all row sums and column sums of h are 0  OK")

    # (A): total sum is zero
    totA = [sum(hA[(i, j)][c] for i in range(n) for j in range(n)) for c in range(k)]
    assert all(x == 0 for x in totA)
    print(f"k={k} [A] total label sum over E(K_kk) = 0  OK")

    valsA, valsB, valsC = set(), set(), set()
    l2A, linfA = set(), set()
    for pi in itertools.permutations(range(n)):
        M = [(i, pi[i]) for i in range(n)]
        valsA.add(f_h(hA, M, k, n))
        valsB.add(f_h(hB, M, k, n))
        valsC.add(f_h(hC, M, k, n))
        msum = [sum(hA[e][c] for e in M) for c in range(k)]
        l2A.add(l2sq(msum))
        linfA.add(linf(msum))

    expC = Fraction(k) / denom
    print(f"k={k} [A] f_h values over all {n}! matchings: {sorted(valsA)}  (claimed {{{k}}})")
    print(f"k={k} [B] f_h values: {sorted(valsB)}  (claimed {{{Fraction(k,2)}}})")
    print(f"k={k} [C] f_h values: {sorted(valsC)}  (claimed {{{expC}}})")
    print(f"k={k} [A] ||sum||_2^2 values: {sorted(l2A)} (claimed {{{k}}}), "
          f"||sum||_inf values: {sorted(linfA)} (claimed {{1}})")
    assert valsA == {Fraction(k)}
    assert valsB == {Fraction(k, 2)}
    assert valsC == {expC}
    assert l2A == {Fraction(k)} and linfA == {Fraction(1)}
    print(f"k={k}: ALL CLAIMS VERIFIED\n")

for k in (2, 4, 6, 8):
    run(k)
print("Done: every claim of the writeup's three constructions verified exactly.")
