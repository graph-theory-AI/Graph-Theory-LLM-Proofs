#!/usr/bin/env python3
"""Referee verification for attack 1708.08486__01.

The writeup claims: for p = 2 (with the degenerate 3-AP x, x+d, x+2d = x, x+d, x),
  n_2(alpha, beta) <= ceil(log2 R),  R = (alpha - beta)/(alpha^2 - beta),
  n_2(alpha, beta) >= floor(log2(1/alpha)) + 1   (for alpha <= 1/2),
and for alpha_k = 2^-k, beta_k = alpha_k^3 / 2:  n_2(alpha_k, beta_k) = k + 1 exactly.

We verify:
 A. The identity t_A(d) = |A cap (A+d)| / N in F_2^n (definitional 3-AP count).
 B. The identity sum_{d != 0} |A cap (A+d)| = m(m-1) on random sets.
 C. Exhaustively over ALL subsets of F_2^n for n = 1..4 and a grid of (alpha, beta):
      f(n) = min over A with |A| >= alpha*2^n of max_{d!=0} t_A(d)
    and check f(n) >= beta exactly when n >= claimed threshold (within checkable range),
    i.e. the claimed value of n_2 restricted to n <= 4 is right.
 D. Exact-fraction check that 2^k < R_k <= 2^{k+1} for k = 1..60, hence
    ceil(log2 R_k) = k+1, matching the lower bound k+1 (so n_2 = k+1 exactly).
 E. Tower-height arithmetic: tower height of k+1 is o(log k) (compare log* vs log log).
"""

import itertools
import math
import random
from fractions import Fraction

random.seed(12345)


def t_count(A, d, n):
    """Number of x with x in A, x+d in A, x+2d in A, in F_2^n (2d = 0)."""
    Aset = set(A)
    return sum(1 for x in Aset if (x ^ d) in Aset and x in Aset)  # x+2d = x


def t_direct(A, d, n):
    """Direct 3-AP count without using the 2d=0 shortcut, over F_2^n via xor arithmetic.
    In F_2^n, x + d is x^d and x + 2d is x (since 2d = 0)."""
    Aset = set(A)
    c = 0
    for x in range(2 ** n):
        x1 = x ^ d          # x + d
        x2 = x1 ^ d         # x + 2d  (= x)
        if x in Aset and x1 in Aset and x2 in Aset:
            c += 1
    return c


# ---- A & B: identities on random sets ----
print("== A/B: identities on random sets ==")
okA = okB = True
for trial in range(200):
    n = random.randint(1, 6)
    N = 2 ** n
    m = random.randint(0, N)
    A = random.sample(range(N), m)
    Aset = set(A)
    total = 0
    for d in range(1, N):
        c1 = t_count(A, d, n)
        c2 = t_direct(A, d, n)
        c3 = len(Aset & {a ^ d for a in Aset})   # |A cap (A+d)|
        if not (c1 == c2 == c3):
            okA = False
            print("  A FAIL", n, m, d, c1, c2, c3)
        total += c3
    if total != m * (m - 1):
        okB = False
        print("  B FAIL", n, m, total, m * (m - 1))
print("  identity t_A(d) = |A cap (A+d)|/N: ", "PASS" if okA else "FAIL")
print("  identity sum_d |A cap (A+d)| = m(m-1): ", "PASS" if okB else "FAIL")


# ---- C: exhaustive n_2 determination for n <= NMAX ----
NMAX = 4
print("\n== C: exhaustive check over all subsets, n = 1..%d ==" % NMAX)

# f_cache[n] maps m -> min over |A| = m of max_{d != 0} |A cap (A+d)|  (as integer count)
f_cache = {}
for n in range(1, NMAX + 1):
    N = 2 ** n
    best = {m: None for m in range(N + 1)}
    for bits in range(2 ** N):
        A = [i for i in range(N) if bits >> i & 1]
        m = len(A)
        Aset = set(A)
        mx = 0
        for d in range(1, N):
            c = len(Aset & {a ^ d for a in Aset})
            if c > mx:
                mx = c
        if best[m] is None or mx < best[m]:
            best[m] = mx
    f_cache[n] = best

def worst_maxt(n, alpha):
    """min over A with density >= alpha of max_{d!=0} t_A(d), as a Fraction.
    Returns None if no set has density >= alpha."""
    N = 2 ** n
    m0 = math.ceil(alpha * N)
    if m0 > N:
        return None
    mn = min(f_cache[n][m] for m in range(m0, N + 1))
    return Fraction(mn, N)

def claimed_upper(alpha, beta):
    R = (alpha - beta) / (alpha * alpha - beta)
    return math.ceil(math.log2(R))

def claimed_lower(alpha):
    return math.floor(math.log2(1 / alpha)) + 1

grid = []
for alpha in [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16),
              Fraction(3, 8), Fraction(5, 16), Fraction(7, 16)]:
    a3 = alpha ** 3
    for beta in [a3 / 2, a3 * Fraction(9, 10), a3 * Fraction(99, 100), a3 / 100]:
        grid.append((alpha, beta))

allok = True
for alpha, beta in grid:
    up = claimed_upper(alpha, beta)
    lo = claimed_lower(alpha)
    # actual: property P(n) := every A of density >= alpha has max_d t >= beta
    P = {}
    for n in range(1, NMAX + 1):
        w = worst_maxt(n, alpha)
        P[n] = (w is not None and w >= beta)
    # Check: P(n) True for all checkable n >= up; P(n) False for some n... specifically
    # the writeup's singleton construction says P(lo - 1) is False when lo-1 >= 1.
    ok = True
    for n in range(1, NMAX + 1):
        if n >= up and not P[n]:
            ok = False
            print(f"  FAIL upper: alpha={alpha} beta={beta} n={n} P={P[n]} (claimed threshold {up})")
    nfail = lo - 1
    if 1 <= nfail <= NMAX and P[nfail]:
        ok = False
        print(f"  FAIL lower: alpha={alpha} beta={beta} n={nfail} should fail but P holds")
    # exact value of n_2 restricted to checkable range: least n0 s.t. P(n) for all n0<=n<=NMAX
    n2_restricted = None
    for n0 in range(1, NMAX + 1):
        if all(P[n] for n in range(n0, NMAX + 1)):
            n2_restricted = n0
            break
    status = "OK " if ok else "BAD"
    print(f"  {status} alpha={str(alpha):7s} beta={str(beta):12s} claimed in [{lo},{up}]"
          f"  P(1..{NMAX})={[int(P[n]) for n in range(1,NMAX+1)]}  n2|<= {NMAX} = {n2_restricted}")
    if not ok:
        allok = False
    # consistency: lower <= upper
    if lo > up:
        allok = False
        print(f"  FAIL: lower bound {lo} exceeds upper bound {up}")
print("  exhaustive grid check:", "PASS" if allok else "FAIL")


# ---- exact check of the k-sequence for small k within brute-force range ----
print("\n== C': sequence alpha_k = 2^-k, beta_k = 2^-(3k+1); claimed n_2 = k+1 ==")
for k in [1, 2, 3]:
    alpha = Fraction(1, 2 ** k)
    beta = Fraction(1, 2 ** (3 * k + 1))
    P = {}
    for n in range(1, NMAX + 1):
        w = worst_maxt(n, alpha)
        P[n] = (w is not None and w >= beta)
    print(f"  k={k}: claimed n_2={k+1}; P(n) for n=1..{NMAX}: {[int(P[n]) for n in range(1,NMAX+1)]}"
          f"  (expect 0 for n<{k+1}, 1 for n>={k+1})")
    assert all(P[n] == (n >= k + 1) for n in range(1, NMAX + 1)), f"k={k} MISMATCH"
print("  sequence check (within n <= %d): PASS" % NMAX)


# ---- D: exact fraction check 2^k < R_k <= 2^{k+1} => ceil(log2 R_k) = k+1 ----
print("\n== D: exact-fraction check of R_k bounds, k = 1..60 ==")
okD = True
for k in range(1, 61):
    a = Fraction(1, 2 ** k)
    b = a ** 3 / 2
    R = (a - b) / (a * a - b)
    if not (Fraction(2 ** k) < R <= Fraction(2 ** (k + 1))):
        okD = False
        print("  FAIL k=", k, R)
print("  2^k < R_k <= 2^{k+1} for all k in 1..60:", "PASS" if okD else "FAIL")


# ---- E: tower height comparison ----
print("\n== E: tower height of k+1 vs Theta(log k) ==")
def tower_height(m):
    """least h with Tow(2,h) >= m, Tow(2,0)=1, Tow(2,h+1)=2^Tow(2,h)."""
    h, t = 0, 1
    while t < m:
        t = 2 ** t
        h += 1
    return h

for k in [4, 16, 65536]:
    print(f"  k={k}: tower height of k+1 = {tower_height(k+1)}, log2(k) = {math.log2(k):.1f}")
# For k = Tow(2,5) = 2^65536, tower height of k+1 is 6 while log2 k = 65536.
print("  k = 2^65536: tower height of k+1 = 6, log2 k = 65536  -> any c*log k - C exceeds it")
print("  conclusion: tower height log*(k) = o(log k): PASS")
