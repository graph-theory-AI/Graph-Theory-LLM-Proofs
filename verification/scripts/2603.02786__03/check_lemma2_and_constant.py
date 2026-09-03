#!/usr/bin/env python3
"""Checks for Lemma 2 (weighted multiplicity <= 1) and the constant 6619/5400.

Part A: brute-force the combinatorial deduction of Lemma 2.
  At a point x, the set of cores C_{ap} (a in {2,3,5}, p prime > 5) containing x
  must satisfy the constraints implied by Lemma 1:
    (i)  within a family a: phases alpha_{ap} mod a pairwise distinct
         => at most a cores of family a contain x;
    (ii) across families a != b: cores C_{ap}, C_{bq} both containing x with
         p != q would have gcd(ap,bq)=1, forcing disjoint cores => p must equal q.
  We enumerate ALL set systems {P_2, P_3, P_5} of primes from a pool obeying
  (i) |P_a| <= a and (ii) p != q forbidden across distinct nonempty families,
  and maximize N = sum_a lambda_a |P_a|.  Lemma 2 claims max N = 1.

Part B: exact rational arithmetic for the constant, and the simpler 9/16 bound.

Part C: numeric check of S(x) ~ x^2/(2 ln x) and of the constant in (4) at
  finite k (sieve up to 10^7).
"""
from fractions import Fraction
from itertools import combinations
from math import log

# ---------- Part A ----------
def part_a():
    lam = {2: Fraction(1, 2), 3: Fraction(1, 3), 5: Fraction(1, 6)}
    pool = [7, 11, 13, 17, 19, 23]  # primes > 5 (pool size 6 > 5 = max family size)
    best = Fraction(0)
    best_cfg = None
    fams = [2, 3, 5]
    # enumerate subsets P_a with |P_a| <= a
    def subsets(maxsize):
        out = [()]
        for r in range(1, maxsize + 1):
            out.extend(combinations(pool, r))
        return out
    S2, S3, S5 = subsets(2), subsets(3), subsets(5)
    count = 0
    for P2 in S2:
        for P3 in S3:
            for P5 in S5:
                Ps = {2: set(P2), 3: set(P3), 5: set(P5)}
                # cross-family constraint: for a != b, p in P_a, q in P_b => p == q
                ok = True
                for a in fams:
                    for b in fams:
                        if a >= b:
                            continue
                        for p in Ps[a]:
                            for q in Ps[b]:
                                if p != q:
                                    ok = False
                if not ok:
                    continue
                count += 1
                N = sum(lam[a] * len(Ps[a]) for a in fams)
                if N > best:
                    best = N
                    best_cfg = (P2, P3, P5)
    print(f"Part A: enumerated {count} admissible configurations")
    print(f"  max weighted multiplicity N = {best} (claim: <= 1), achieved at {best_cfg}")
    assert best <= 1, "LEMMA 2 VIOLATED"
    print("  LEMMA 2 deduction VERIFIED (max = %s)." % best)

# ---------- Part B ----------
def part_b():
    lam = {2: Fraction(1, 2), 3: Fraction(1, 3), 5: Fraction(1, 6)}
    total = Fraction(1)
    for a, l in lam.items():
        total += l * Fraction(a - 1, a * a)
    print(f"\nPart B: 1 + sum lambda_a (a-1)/a^2 = {total} = {float(total):.6f}")
    assert total == Fraction(6619, 5400), "constant mismatch"
    print("  matches 6619/5400 exactly; 6619/5400 > 1:", total > 1)
    print("  6619/10800 =", float(Fraction(6619, 10800)), "> 1/2:", Fraction(6619, 10800) > Fraction(1, 2))
    # simpler bound in section 6: only a=2 with weight 1/2
    simple = Fraction(1) + Fraction(1, 2) * Fraction(1, 4)
    print(f"  simpler (2p only): 1 + (1/2)(1/4) = {simple}; halved: {simple/2} = {float(simple/2)} (claim 9/16 = {float(Fraction(9,16))})")
    assert simple / 2 == Fraction(9, 16)
    print("  9/16 claim verified.")

# ---------- Part C ----------
def sieve_primes(limit):
    import numpy as np
    is_p = np.ones(limit + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i::i] = False
    return np.nonzero(is_p)[0]

def part_c():
    import numpy as np
    K = 10 ** 7
    primes = sieve_primes(K)
    primes_sum = np.cumsum(primes.astype(np.int64))
    def S(x):
        import bisect
        idx = np.searchsorted(primes, x, side='right')
        return int(primes_sum[idx - 1]) if idx > 0 else 0
    for k in (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
        ref = k * k / (2 * log(k))
        ratio = S(k) / ref
        # constant of inequality (4): [S(k) + sum_a lambda_a (a-1) S(k/a)] / (k^2/(2 ln k))
        lam = {2: 0.5, 3: 1 / 3, 5: 1 / 6}
        val = S(k) + sum(lam[a] * (a - 1) * S(k // a) for a in lam)
        c4 = val / ref
        print(f"  k={k:>9}: S(k)/(k^2/(2 ln k)) = {ratio:.4f}; (4)-constant = {c4:.4f}  (limit 6619/5400 = {6619/5400:.4f})")
    print("  (Both exceed 1 at all finite k shown; S(x)*2ln x/x^2 -> 1 from above, so the")
    print("   finite-k lower-bound constant is even larger than the asymptotic one.)")

if __name__ == "__main__":
    part_a()
    part_b()
    print("\nPart C: sums of primes (sieve to 10^7)")
    part_c()
