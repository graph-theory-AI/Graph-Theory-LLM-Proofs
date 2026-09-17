"""Check the writeup's closed forms and asymptotic consequences.

(a) N_k(d) = sum_{r<d}(k-1)^r equals ((k-1)^d - 1)/(k-2) for k >= 3 and d for k = 2.
(b) d_min = min{d : n <= N_k(d)} equals the boxed formula (3):
        n              if k = 2,
        ceil(log((k-2)n+1)/log(k-1))  if k >= 3.
(c) N_k(d) <= k^{d-1}, hence D >= 1 + log n / log k.
"""
from math import log, ceil
from fractions import Fraction

def Nk(k, d):
    return sum((k - 1) ** r for r in range(d))

bad_a = bad_b = bad_c = []
bad_a, bad_b, bad_c = [], [], []
for k in range(2, 60):
    for d in range(1, 40):
        v = Nk(k, d)
        if k == 2:
            if v != d: bad_a.append((k, d))
        else:
            if v != ((k - 1) ** d - 1) // (k - 2): bad_a.append((k, d))
        if v > k ** (d - 1):
            bad_c.append((k, d, v, k ** (d - 1)))
for k in range(2, 40):
    for n in range(1, 4000):
        dmin = 1
        while Nk(k, dmin) < n:
            dmin += 1
        if k == 2:
            f = n
        else:
            # exact integer ceiling of log((k-2)n+1)/log(k-1)
            t = (k - 2) * n + 1
            f = 0
            p = 1
            while p < t:
                p *= (k - 1); f += 1
            if f == 0: f = 1   # t == 1 happens only for n = ... ; keep d >= 1
        if dmin != f:
            bad_b.append((k, n, dmin, f))
print("(a) closed form failures:", bad_a[:10], len(bad_a))
print("(b) d_min formula failures:", bad_b[:10], len(bad_b))
print("(c) N_k(d) <= k^{d-1} failures:", bad_c[:10], len(bad_c))

# float version of formula (3) as literally written, to detect rounding traps
mismatch = []
for k in range(3, 30):
    for n in range(1, 2000):
        dmin = 1
        while Nk(k, dmin) < n:
            dmin += 1
        f = ceil(log((k - 2) * n + 1) / log(k - 1))
        if f != dmin:
            mismatch.append((k, n, dmin, f))
print("(b') float evaluation of (3) mismatches:", mismatch[:10], len(mismatch))
