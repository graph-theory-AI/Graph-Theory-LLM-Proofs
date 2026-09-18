"""Check the writeup's Lemma 3 ("prime-block interval lemma") computationally.

Lemma 3 claims: for fixed kappa>0 and n large, if A is a set of primes in [n,2n] with
|A| >= kappa*n/log n, then  [n(log n)^3, n^2/(log n)^3] cap Z  is contained in Sigma(A).

Two things are checked:
 (1) The stated interval is EMPTY unless n >= (log n)^6, i.e. n >~ 5e8, so the lemma has
     no finite content in any computationally reachable range.  We report the threshold.
 (2) The qualitative content -- dense prime sets in [n,2n] have Sigma(A) containing an
     interval [c1*n*polylog, c2*n^2/polylog] -- is checked by exact bitset DP for
     n up to a few thousand, for A = all primes and for random kappa-fractions.
 (3) The internal parameter inequalities of the proof (h <= m/8, H+ell <= s/2, ...) are
     evaluated to see at which n they become valid.
"""
import math

from sympy import primerange, nextprime


def sigma_bitset(A):
    """bit j of the returned int is 1 iff j is a subset sum of A (0 included)."""
    S = 1
    for a in A:
        S |= S << a
    return S


def longest_interval(S, lo, hi):
    """longest run of consecutive 1-bits of S inside [lo,hi]; returns (start,end) inclusive."""
    best = (0, -1)
    cur = None
    for j in range(lo, hi + 1):
        if (S >> j) & 1:
            if cur is None:
                cur = j
        else:
            if cur is not None:
                if j - cur > best[1] - best[0] + 1:
                    best = (cur, j - 1)
                cur = None
    if cur is not None and hi - cur + 1 > best[1] - best[0] + 1:
        best = (cur, hi)
    return best


print("(1) emptiness threshold of the claimed interval [n(log n)^3, n^2/(log n)^3]:")
n = 10
while n * math.log(n) ** 3 >= n ** 2 / math.log(n) ** 3:
    n = int(n * 1.2) + 1
print(f"    the interval is non-empty only for n >= about {n:.3e} "
      f"(log n = {math.log(n):.2f}); below that Lemma 3 is vacuous.\n")

print("(2) exact subset sums of dense prime sets in [n,2n] (bitset DP):")
print(f"{'n':>6} {'#primes':>8} {'|A|':>6} {'kappa':>7} {'sum':>12} "
      f"{'longest interval in Sigma(A)':>34} {'as multiples of n':>26}")
import random
random.seed(11)
for n in [200, 500, 1000, 2000, 3000]:
    P = list(primerange(n, 2 * n + 1))
    for frac in [1.0, 0.5, 0.25]:
        A = sorted(random.sample(P, max(2, int(len(P) * frac))))
        tot = sum(A)
        S = sigma_bitset(A)
        a, b = longest_interval(S, 1, tot)
        kappa = len(A) * math.log(n) / n
        print(f"{n:>6} {len(P):>8} {len(A):>6} {kappa:7.3f} {tot:>12} "
              f"[{a}, {b}]".rjust(0).ljust(0) + f"   ->  [{a/n:.2f} n, {b/n**2:.3f} n^2]")

print("\n(3) when do the proof's internal inequalities hold?  (kappa = 1/(2r))")
print(f"{'r':>3} {'n':>12} {'m=kappa n/log n':>16} {'h=ceil(8p/m)':>13} {'h<=m/8':>7} "
      f"{'s>=m/(2h)':>11} {'H=ceil(2p/s)':>13} {'H+h<=s/2':>9}")
for r in [2, 3]:
    kappa = 1.0 / (2 * r)
    for n in [10**4, 10**6, 10**8, 10**10, 10**12, 10**15]:
        m = kappa * n / math.log(n)
        p = 3 * n  # a prime in (2n,4n)
        h = math.ceil(8 * p / m)
        s = m / (2 * h)
        H = math.ceil(2 * p / s)
        print(f"{r:>3} {n:>12.0e} {m:16.3e} {h:13.1f} {str(h <= m/8):>7} "
              f"{s:11.3e} {H:13.1f} {str(H + h <= s/2):>9}")
