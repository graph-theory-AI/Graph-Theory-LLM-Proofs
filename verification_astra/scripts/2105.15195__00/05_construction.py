"""Check Section 5 (the matching upper bound, i.e. the CFP construction) numerically.

Colouring: n gets colour floor(log_b log n) mod r, with b = b_0.  Equivalently blocks
[N_k, N_{k+1}) with N_k = ceil(e^{b^k}).  Claim: for each colour i,
  Sigma(A_i) is contained in the union over k = i mod r of [N_k, N_{k+1}^2],
whose upper logarithmic density is C_r = b^{r-1}/(2r).

We (a) recompute the upper density of V_i = union_{k=i mod r} [b^k, 2 b^{k+1}] directly,
(b) verify b_0 > 2^{1/(r-1)} so that consecutive same-colour intervals are disjoint,
(c) verify the containment Sigma([m,n]) subset [m, binom(n+1,2)] used for the bound.
"""
import itertools
import math

import numpy as np
from scipy.optimize import brentq


def b0(r, lam=2.0):
    f = lambda b: b**r - lam * r * b + r - 1
    hi = 2.0
    while f(hi) < 0:
        hi *= 2
    return brentq(f, lam ** (1.0 / (r - 1)) + 1e-14, hi, xtol=1e-15, rtol=1e-15)


print("(a) upper density of V_i = U_{k = i mod r} [b^k, 2 b^{k+1}]  vs  C_r\n")
print(f"{'r':>3} {'b_0':>14} {'C_r=b^(r-1)/2r':>16} {'measured upper density':>24} "
      f"{'2^{1/(r-1)}':>12} {'disjoint?':>10}")
for r in range(2, 9):
    b = b0(r)
    C = b ** (r - 1) / (2 * r)
    K = 400
    ivs = [(b ** k, 2 * b ** (k + 1)) for k in range(0, K) if k % r == 0]
    # merge (should be disjoint)
    merged = []
    for a, bb in ivs:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], bb))
        else:
            merged.append((a, bb))
    disjoint = len(merged) == len(ivs)
    tot = 0.0
    best = 0.0
    for a, bb in merged:
        tot += bb - a
        if bb > b ** (K // 2):
            best = max(best, tot / bb)
    print(f"{r:>3} {b:14.10f} {C:16.12f} {best:24.12f} {2**(1.0/(r-1)):12.6f} {str(disjoint):>10}")

print("\n(b) Sigma([m,n]) subset [m, n(n+1)/2 - (m-1)m/2]:  brute force on small intervals")
bad = 0
for m in range(1, 9):
    for n in range(m, 14):
        elems = list(range(m, n + 1))
        sums = set()
        for k in range(1, len(elems) + 1):
            for c in itertools.combinations(elems, k):
                sums.add(sum(c))
        if min(sums) != m or max(sums) != sum(elems):
            bad += 1
print("   OK" if bad == 0 else f"   FAILED {bad}")

print("\n(c) the writeup's claim that Sigma(A_i) sums with largest summand in block k are "
      "< N_{k+1}^2:  sum_{n<N} n = N(N-1)/2 < N^2  -- trivially true.")
