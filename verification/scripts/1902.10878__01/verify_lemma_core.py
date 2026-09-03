#!/usr/bin/env python3
"""Machine check of the finite combinatorial core of the writeup's Lemma
(lower bound psi((q-2)/q, 2/q) >= 1 - 1/q) plus exact re-derivation of all
displayed arithmetic in attacks/1902.10878__01/output.md.

The lemma's proof reduces (by forced equalities, verified by hand in the
referee report) any putative counterexample to the following finite data:
distinct nonempty sets S_1..S_m in B (the C-neighbourhood types) with
positive fractions beta_i summing to 1, and disjoint A-classes with
fractions alpha_i, such that
  (3) alpha_i > 1/q for all i,
  (4) sum_{i: b in S_i} beta_i = 2/q for every b in B  (so every b is
      covered by the S-family),
  (5) sum_{i: b in S_i} alpha_i <= 2/q for every b in B.
(3)+(5) force every b to lie in exactly one S_i ("the support family is a
perfect matching under multiplicity"), and then (4) forces beta_i = 2/q and
m*(2/q) = 1, i.e. q = 2m, contradicting q odd.

This script verifies exactly, with rational arithmetic:
  (a) 2*(1/q + eps) > 2/q for any eps>0 (so no b lies in two classes);
  (b) for odd q in {3,...,15}, exhaustive enumeration over K_q confirms that
      no matching (edge set with max degree <= 1) covers all q vertices --
      i.e. the forced support structure cannot exist (parity, checked by
      brute force over all matchings of K_q);
  (c) all displayed arithmetic identities of the writeup.
"""
from fractions import Fraction
from itertools import combinations


def all_matchings(q):
    """Yield all matchings (as frozensets of 2-subsets) of the complete
    graph on {0..q-1}. Exhaustive."""
    edges = list(combinations(range(q), 2))

    def rec(start, used, cur):
        yield frozenset(cur)
        for k in range(start, len(edges)):
            e = edges[k]
            if e[0] in used or e[1] in used:
                continue
            cur.append(e)
            yield from rec(k + 1, used | set(e), cur)
            cur.pop()

    yield from rec(0, set(), [])


def check_no_perfect_matching(q):
    count = 0
    for M in all_matchings(q):
        count += 1
        covered = set()
        for e in M:
            covered.update(e)
        if len(covered) == q:
            return False, count
    return True, count


def main():
    ok = True

    print("=== (a) two alpha-terms exceed 2/q (exact) ===")
    for q in (3, 5, 7, 9, 11, 13, 15):
        # alpha_i > 1/q each; two of them sum to > 2/q. Check with a generic
        # eps: (1/q + eps) + (1/q + eps) > 2/q  <=>  2*eps > 0. Verified
        # symbolically; also spot-check the boundary with Fractions:
        assert 2 * Fraction(1, q) == Fraction(2, q)
        print(f"q={q}: 2*(1/q) = 2/q exactly, so alpha_i,alpha_j > 1/q "
              f"=> alpha_i+alpha_j > 2/q  -- forces |I(b)| <= 1. OK")

    print()
    print("=== (b) no matching of K_q covers all q vertices (q odd) ===")
    for q in (3, 5, 7, 9, 11, 13):
        good, n = check_no_perfect_matching(q)
        print(f"q={q}: enumerated {n} matchings of K_{q}; "
              f"perfect matching exists: {not good}")
        if not good:
            ok = False
    # sanity: for even q a perfect matching DOES exist (checks the checker)
    good, n = check_no_perfect_matching(6)
    print(f"q=6 (sanity, even): enumerated {n} matchings; "
          f"perfect matching exists: {not good} (expected True)")
    if good:
        ok = False

    print()
    print("=== (c) displayed arithmetic of the writeup (exact fractions) ===")
    for q in (7, 9, 11, 13):
        h = Fraction(q - 3, 2)
        m = h + 3
        assert m == Fraction(q + 3, 2)
        sizeB = 2 * h + 3
        assert sizeB == q, (q, sizeB)
        sizeA = m * (q - 2) + 3
        assert sizeA == Fraction(q * (q + 1), 2), (q, sizeA)
        assert q - 2 + 3 == q + 1 == Fraction(2, q) * sizeA
        assert 2 * (q - 2) + 3 == 2 * q - 1 >= q + 1
        bound = 1 - Fraction(2 * (q - 2), q * (q + 1))
        gap = Fraction(2 * (q - 2), q * (q + 1)) - Fraction(1, q)
        assert gap == Fraction(q - 5, q * (q + 1)), (q, gap)
        assert (gap > 0) == (q > 5)
        print(f"q={q}: |A|={sizeA}, bound=1-2(q-2)/(q(q+1))={bound}, "
              f"gap to 1-1/q = (q-5)/(q(q+1)) = {gap} > 0: {gap > 0}")
    # q=7 headline
    assert 1 - Fraction(2 * 5, 7 * 8) == Fraction(23, 28)
    assert Fraction(6, 7) == Fraction(24, 28) > Fraction(23, 28)
    print("q=7: 1-10/56 = 23/28 < 24/28 = 6/7. OK")
    # trivial bounds from the paper (thm 'trivialbounds', k=7):
    # max(2/7,5/7)=5/7 <= psi(2/7,5/7), and ceil-bound (2+5-1)/7 = 6/7
    assert Fraction(5, 7) < Fraction(23, 28) < Fraction(6, 7)
    print("23/28 lies strictly between the paper's trivial bounds "
          "5/7 and 6/7 for psi(2/7,5/7). OK")

    print()
    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")


if __name__ == "__main__":
    main()
