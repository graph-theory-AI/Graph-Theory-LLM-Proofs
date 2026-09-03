#!/usr/bin/env python3
"""Direct random tests of the writeup's Lemma 2 and Lemma 3.

Lemma 2: a_0=1, (a_k) nonnegative nonincreasing log-concave
         =>  sum_{k>=1} a_k/k >= ln(sum_{k>=0} a_k).
Lemma 3: L nonnegative integer r.v. => E[H_L] <= log2(E[L]+1).
Also: sanity-check that Lemma 2 FAILS for some non-log-concave sequences
(to show the hypothesis is load-bearing) and H_m <= log2(m+1) for all m.
"""
import math, random

def harm(m):
    return sum(1.0 / k for k in range(1, m + 1))

def lemma2_holds(a):
    lhs = sum(a[k] / k for k in range(1, len(a)))
    rhs = math.log(sum(a))
    return lhs >= rhs - 1e-12, lhs, rhs

rng = random.Random(99)

# H_m <= log2(m+1)
for m in range(0, 2000):
    assert harm(m) <= math.log2(m + 1) + 1e-12, m
print("H_m <= log2(m+1) holds for m = 0..1999")

# Lemma 2 random tests: build log-concave nonincreasing via nonincreasing ratios
fails = 0
for _ in range(200000):
    m = rng.randint(1, 12)
    ratios = sorted([rng.random() for _ in range(m)], reverse=True)
    a = [1.0]
    for r in ratios:
        a.append(a[-1] * r)
    # optionally truncate to introduce trailing zeros
    if rng.random() < 0.2:
        cut = rng.randint(1, m)
        a = a[:cut] + [0.0] * (m + 1 - cut)
    ok, lhs, rhs = lemma2_holds(a)
    if not ok:
        fails += 1
        print("LEMMA2 FAIL", a, lhs, rhs)
assert fails == 0
print("Lemma 2: 200000 random log-concave sequences, 0 failures")

# show hypothesis is load-bearing: find non-log-concave counterexample
found = None
for _ in range(100000):
    m = rng.randint(2, 8)
    a = [1.0] + sorted([rng.random() for _ in range(m)], reverse=True)
    ok, lhs, rhs = lemma2_holds(a)
    lc = all(a[k] ** 2 >= a[k - 1] * a[k + 1] - 1e-15 for k in range(1, m))
    if not ok and not lc:
        found = (a, lhs, rhs)
        break
print("non-log-concave counterexample to (8):",
      "found (hypothesis is load-bearing)" if found else "none found")

# Lemma 3 random tests
fails = 0
for _ in range(200000):
    m = rng.randint(1, 15)
    w = [rng.random() for _ in range(m + 1)]
    s = sum(w)
    p = [x / s for x in w]
    EH = sum(p[k] * harm(k) for k in range(m + 1))
    EL = sum(p[k] * k for k in range(m + 1))
    if EH > math.log2(EL + 1) + 1e-12:
        fails += 1
        print("LEMMA3 FAIL", p, EH, math.log2(EL + 1))
assert fails == 0
print("Lemma 3: 200000 random distributions, 0 failures")
print("ALL CHECKS PASSED")
