"""Brute-force check of the writeup's Lemma 2 (Dias da Silva-Hamidoune / Erdos-Heilbronn):

  B subset of F_p, |B|=s, 1<=k<=s, k(s-k) >= p-1  ==>  every element of F_p is a sum of
  k DISTINCT members of B.

We also check the sharpness bookkeeping: |k^B| >= min(p, k(s-k)+1).
Also verifies the auxiliary claim used inside the proof: the sums of k distinct integers
from {0,...,s-1} fill exactly [C(k,2), C(k,2)+k(s-k)], and the explicit choice of d_i
given in the writeup is legal (distinct, increasing, <= s-1, correct sum).
"""
import itertools
from math import comb

import numpy as np

RNG = np.random.default_rng(7)
PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def kfold_distinct_sums(B, k, p):
    return {sum(c) % p for c in itertools.combinations(B, k)}


fails = 0
tested = 0
tight = 0
for p in PRIMES:
    for s in range(2, min(p, 12) + 1):
        for trial in range(12):
            B = sorted(RNG.choice(p, size=s, replace=False).tolist())
            for k in range(1, s + 1):
                got = kfold_distinct_sums(B, k, p)
                lb = min(p, k * (s - k) + 1)
                tested += 1
                if len(got) < lb:
                    print("DdSH lower bound VIOLATED", p, B, k, len(got), lb)
                    fails += 1
                if k * (s - k) >= p - 1:
                    tight += 1
                    if len(got) != p:
                        print("LEMMA 2 FAILS:", p, B, k, sorted(got))
                        fails += 1
print(f"Lemma 2 brute force: {tested} (p,B,k) cases, {tight} of them satisfying "
      f"k(s-k)>=p-1; failures = {fails}")

# sums of k distinct elements of {0,...,s-1}
bad = 0
for s in range(1, 13):
    for k in range(1, s + 1):
        sums = {sum(c) for c in itertools.combinations(range(s), k)}
        lo, hi = comb(k, 2), comb(k, 2) + k * (s - k)
        if sums != set(range(lo, hi + 1)):
            print("interval-of-sums claim fails", s, k)
            bad += 1
print(f"'sums of k distinct elements of [0,s-1] fill [C(k,2), C(k,2)+k(s-k)]': "
      f"{'OK' if bad == 0 else 'FAILED'}")

# the writeup's explicit d_i choice
bad = 0
for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 101, 211]:
    for s in range(2, 60):
        for k in range(1, s + 1):
            if k * (s - k) < p - 1:
                continue
            q, u = divmod(p - 1, k)
            d = [i - 1 + q for i in range(1, k - u + 1)] + \
                [i + q for i in range(k - u + 1, k + 1)]
            ok = (len(set(d)) == k and d == sorted(d) and min(d) >= 0 and max(d) <= s - 1
                  and sum(d) == p - 1 + comb(k, 2))
            if not ok:
                print("explicit d_i choice fails", p, s, k, d, max(d), s - 1)
                bad += 1
print(f"writeup's explicit choice of d_1<...<d_k: {'OK in all valid ranges' if bad==0 else 'FAILED %d times' % bad}")
