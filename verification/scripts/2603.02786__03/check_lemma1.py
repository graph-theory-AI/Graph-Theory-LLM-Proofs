#!/usr/bin/env python3
"""Exhaustive check of Lemma 1 of the writeup for 2603.02786__03.

Lemma 1 (writeup): P_d = {a_d, a_d+d, ..., a_d+(n-1)d}, hull H_d = [a_d, a_d+(n-1)d],
core C_d = [a_d+L, a_d+(n-1)d-L].  If P_d and P_e are disjoint and the cores
intersect, then a_d != a_e (mod gcd(d,e)).

Equivalently (what we test): if a_d == a_e (mod gcd(d,e)) and the cores
intersect, then P_d and P_e intersect.

The writeup uses L = k^2 >= d*e >= lcm(d,e).  The proof only needs
L >= lcm(d,e)/2, so we test with the *tightest* margin M = ceil(lcm(d,e)/2);
since the writeup's cores (larger margin) are subsets of these cores, validity
with margin M implies validity with margin k^2.

We exhaustively range over all relative offsets of the two progressions.
"""
from math import gcd, ceil
import sys

def lcm(a, b):
    return a * b // gcd(a, b)

def check_pair(d, e, n, margin=None):
    """Exhaustively check the lemma for differences d, e with n terms each."""
    g = gcd(d, e)
    l = lcm(d, e)
    M = margin if margin is not None else (l + 1) // 2  # ceil(lcm/2)
    hull_d = (n - 1) * d
    hull_e = (n - 1) * e
    # cores nonempty?
    if hull_d - 2 * M <= 0 or hull_e - 2 * M <= 0:
        return None  # skip: cores empty, lemma vacuous
    a_d = 0
    P_d = set(range(0, n * d, d))
    violations = 0
    tested = 0
    # relative offset range: all positions where cores could intersect, plus slack
    lo = -(hull_e) - 3 * M - 2 * l
    hi = hull_d + 3 * M + 2 * l
    for a_e in range(lo, hi + 1):
        # congruent phases?
        if (a_e - a_d) % g != 0:
            continue
        # cores intersect?
        cd = (a_d + M, a_d + hull_d - M)
        ce = (a_e + M, a_e + hull_e - M)
        if max(cd[0], ce[0]) > min(cd[1], ce[1]):
            continue
        tested += 1
        P_e = set(range(a_e, a_e + n * e, e))
        if not (P_d & P_e):
            violations += 1
            print(f"  VIOLATION: d={d}, e={e}, n={n}, a_e={a_e}")
    return tested, violations

def main():
    total_tested = 0
    total_viol = 0
    pairs_checked = 0
    # small differences, tight margin ceil(lcm/2)
    cases = []
    for d in range(1, 13):
        for e in range(d + 1, 13):
            cases.append((d, e))
    # semiprime pairs relevant to the writeup (2p, 2q, 3p, 5p etc.)
    cases += [(14, 22), (14, 21), (14, 35), (21, 33), (22, 33), (35, 55),
              (14, 26), (21, 35), (10, 14), (15, 21), (6, 10), (6, 15), (10, 15)]
    for (d, e) in cases:
        l = lcm(d, e)
        M = (l + 1) // 2
        # choose n so both cores are nonempty: (n-1)*d > 2M
        n = max(2 * M // d + 3, 5)
        res = check_pair(d, e, n)
        if res is None:
            print(f"pair ({d},{e}): skipped (empty cores)")
            continue
        t, v = res
        pairs_checked += 1
        total_tested += t
        total_viol += v
        status = "OK" if v == 0 else "FAIL"
        print(f"pair ({d},{e}) n={n} margin={M}: {t} congruent core-overlap offsets tested, {v} violations [{status}]")
    print()
    print(f"TOTAL: {pairs_checked} pairs, {total_tested} configurations tested, {total_viol} violations")
    if total_viol == 0:
        print("LEMMA 1 VERIFIED on all tested configurations.")
    else:
        print("LEMMA 1 FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    main()
