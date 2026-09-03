#!/usr/bin/env python3
"""Verification script for referee report on attack 1710.10663__00.

Checks, independently of the writeup:
  A. Two-point Chebyshev radius identity: min_z max(d(x,z),d(y,z)) = ceil(d(x,y)/2).
  B. Plotkin double-counting identity sum_{i<k} d(x_i,x_k) = sum_j a_j(M-a_j),
     and the bound <= n*floor(M^2/4), on random codes.
  C. Balanced-column construction: pairwise distances all equal 2*C(M-2,w-1),
     relative distance 2w(M-w)/(M(M-1)), matching the writeup's case formulas.
  D. Constants:
       paper (arXiv:1710.10663v2, Thm 1):  c_L = 2^{-L} * floor(L/2) * C(L-1, floor(L/2))
       catalog extraction:                  c_L' = 2^{-floor(L/2)} * C(L, floor(L/2))
       writeup's guessed intended constant: c_L~ = 2^{-L-1} * floor(L/2) * C(L, floor(L/2))
     Verify c_L == c_L~ for all even L (writeup's diagnosis correct),
     c_2 = 1/4 (consistent with paper's own maxcode_2(eps) = 1/(4 eps)+O(1)),
     catalog c_2' = 1 (the mistranscription the writeup refutes).
  E. tau_2 from the paper's formula (1/2 - C(2k,k)/2^{2k+1} with k=1) equals 1/4.
"""
import itertools
from fractions import Fraction
from math import comb, ceil
import random

ok = True

def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        ok = False

# ---------- A. two-point radius identity ----------
def dH(x, y):
    return sum(a != b for a, b in zip(x, y))

bad = 0
for n in range(1, 9):
    for x in itertools.product((0, 1), repeat=n):
        y0 = tuple(0 for _ in range(n))  # wlog x vs 0...0 by symmetry; but do full pairs for n<=5
        pass
for n in range(1, 6):
    pts = list(itertools.product((0, 1), repeat=n))
    for x, y in itertools.combinations(pts, 2):
        r = min(max(dH(x, z), dH(y, z)) for z in pts)
        if r != ceil(dH(x, y) / 2):
            bad += 1
check("A: min_z max(d(x,z),d(y,z)) == ceil(d(x,y)/2) for all pairs, n<=5", bad == 0)

# ---------- B. Plotkin identity on random codes ----------
random.seed(1)
bad = 0
for trial in range(200):
    n = random.randint(1, 12)
    M = random.randint(2, 10)
    C = [tuple(random.randint(0, 1) for _ in range(n)) for _ in range(M)]
    s = sum(dH(x, y) for x, y in itertools.combinations(C, 2))
    a = [sum(x[j] for x in C) for j in range(n)]
    s2 = sum(aj * (M - aj) for aj in a)
    if s != s2 or s > n * (M * M // 4):
        bad += 1
check("B: sum pairwise distances == sum a_j(M-a_j) <= n*floor(M^2/4), 200 random codes", bad == 0)

# ---------- C. balanced-column construction ----------
bad = 0
for M in range(2, 10):
    w = M // 2
    cols = list(itertools.combinations(range(M), w))
    n = len(cols)  # C(M, w)
    code = [tuple(1 if i in A else 0 for A in cols) for i in range(M)]
    dists = {dH(x, y) for x, y in itertools.combinations(code, 2)}
    expect = 2 * comb(M - 2, w - 1)
    rel = Fraction(expect, n)
    rel_expect = Fraction(2 * w * (M - w), M * (M - 1))
    case = Fraction(M, 2 * (M - 1)) if M % 2 == 0 else Fraction(M + 1, 2 * M)
    if dists != {expect} or rel != rel_expect or rel != case:
        bad += 1
        print("  mismatch at M =", M, dists, expect, rel, rel_expect, case)
check("C: equidistant construction, distance 2*C(M-2,w-1), relative 2w(M-w)/(M(M-1)), M=2..9", bad == 0)

# tau_2(M) - 1/4 as claimed
bad = 0
for M in range(2, 40):
    tau2M = (Fraction(M, 4 * (M - 1)) if M % 2 == 0 else Fraction(M + 1, 4 * M))
    gap = tau2M - Fraction(1, 4)
    expect = Fraction(1, 4 * (M - 1)) if M % 2 == 0 else Fraction(1, 4 * M)
    if gap != expect:
        bad += 1
check("C': tau_2(M) - 1/4 == 1/(4(M-1)) (M even) or 1/(4M) (M odd)", bad == 0)

# ---------- D. constants ----------
def c_paper(L):    # arXiv:1710.10663v2 Theorem 1 (verbatim from TeX source)
    return Fraction(L // 2 * comb(L - 1, L // 2), 2 ** L)

def c_catalog(L):  # catalog extraction (prompt.md)
    return Fraction(comb(L, L // 2), 2 ** (L // 2))

def c_writeup(L):  # writeup's guessed "intended" constant
    return Fraction((L // 2) * comb(L, L // 2), 2 ** (L + 1))

check("D1: paper c_L == writeup's guessed constant for ALL even L in 2..40",
      all(c_paper(L) == c_writeup(L) for L in range(2, 41, 2)))
check("D2: paper c_2 == 1/4  (=> maxcode_2 = (1/4)/eps + O(1), matches paper's Levenshtein line)",
      c_paper(2) == Fraction(1, 4))
check("D3: catalog c_2 == 1  (the value the writeup refutes)",
      c_catalog(2) == 1)
check("D4: catalog constant differs from paper constant for every even L in 2..40",
      all(c_catalog(L) != c_paper(L) for L in range(2, 41, 2)))
print("     paper c_L for L=2,4,6,8:", [c_paper(L) for L in (2, 4, 6, 8)])
print("     catalog c_L for L=2,4,6,8:", [c_catalog(L) for L in (2, 4, 6, 8)])

# ---------- E. tau_2 ----------
k = 1  # L = 2k with L=2
tau2 = Fraction(1, 2) - Fraction(comb(2 * k, k), 2 ** (2 * k + 1))
check("E: paper's tau_2 = 1/2 - C(2,1)/2^3 == 1/4", tau2 == Fraction(1, 4))

print()
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
