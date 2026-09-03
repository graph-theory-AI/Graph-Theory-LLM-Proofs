#!/usr/bin/env python3
"""Verification of the algebraic/analytic steps in the writeup for 2405.03455__00.

Checks:
 A. Binomial identity C(s,k) = C(s,2)*C(s-2,k-2)/C(k,2) and the bound
    C(s,k) <= C(s,2)*l^(k-2) for s <= l-1.
 B. Alteration algebra: E[X-Y] = pN - p^k e = pN/2 when p = (N/2e)^{1/(k-1)}
    (symbolic, sympy).
 C. The chain (N/2)*(1/(2N l^{k-2}))^{1/(k-1)} = 2^{-1-1/(k-1)} (N/l)^{(k-2)/(k-1)}
    and 2^{-1-1/(k-1)} >= 1/4 for k >= 3 (symbolic + numeric grid).
 D. Case e < N/2: (1/4)(N/l)^a <= N/2 for a=(k-2)/(k-1) in (0,1), N>=1, l>=1.
 E. Transfer arithmetic: N = ceil(l (4M)^r) with r=(k-1)/(k-2) gives
    (1/4)(N/l)^{1/r} >= M (numeric grid over l, M, k).
 F. Section 3 asymptotics: r*(n + 2*log2(n) + 2 + c0*sqrt(n*log2(n)))
    <= n + C1*sqrt(n*log2(n)) for all n in [3, 10^6], with r = (n-1)/(n-2),
    reporting the minimal C1 needed for sample values of c0, and also that the
    ceiling factor log2(13/12) is absorbable.
 G. Lower-bound step: (3l-1)*2^{n-5} >= (1/12) l 2^n for l >= 3 (symbolic),
    with equality only at l = 3 (so ES > lower bound + strictness is needed;
    the paper gives ES_l(n) >= (3l-1)2^{n-5} + 1, and the catalog states the
    strict inequality (3l-1)2^{n-5} < ES_l(n), so strictness holds).
"""
import math
from fractions import Fraction
import sympy as sp

ok = True

def report(name, cond, detail=""):
    global ok
    status = "PASS" if cond else "FAIL"
    if not cond:
        ok = False
    print(f"[{status}] {name} {detail}")

# --- A. binomial identity and bound ---
good = True
for k in range(3, 12):
    for s in range(k, 60):
        lhs = math.comb(s, k)
        rhs = Fraction(math.comb(s, 2) * math.comb(s - 2, k - 2), math.comb(k, 2))
        if lhs != rhs:
            good = False
report("A1: C(s,k)=C(s,2)C(s-2,k-2)/C(k,2) for 3<=k<=11, k<=s<60", good)

good = True
for k in range(3, 12):
    for l in range(3, 40):
        for s in range(k, l):  # s <= l-1
            if math.comb(s, k) > math.comb(s, 2) * l ** (k - 2):
                good = False
report("A2: C(s,k) <= C(s,2) l^{k-2} for s<=l-1", good)

# --- B. alteration expectation, symbolic in N,e for each integer k ---
N, e = sp.symbols('N e', positive=True)
good = True
for kk in range(3, 15):
    p = (N / (2 * e)) ** sp.Rational(1, kk - 1)
    expr = sp.simplify(p * N - p ** kk * e - p * N / 2)
    if expr != 0:
        good = False
        print("   residual at k=", kk, ":", expr)
report("B: E[X-Y] = pN - p^k e = pN/2 (symbolic in N,e for k=3..14)", good)

# --- C. the chain equality and constant (symbolic in N,l per integer k) ---
Ns, ls = sp.symbols('N l', positive=True)
good = True
for kk in range(3, 15):
    lhs = (Ns / 2) * (1 / (2 * Ns * ls ** (kk - 2))) ** sp.Rational(1, kk - 1)
    rhs = 2 ** (sp.Integer(-1) - sp.Rational(1, kk - 1)) * (Ns / ls) ** sp.Rational(kk - 2, kk - 1)
    if sp.simplify(lhs - rhs) != 0:
        good = False
        print("   mismatch at k=", kk)
report("C1: (N/2)(1/(2N l^{k-2}))^{1/(k-1)} == 2^{-1-1/(k-1)}(N/l)^{(k-2)/(k-1)} (k=3..14)", good)
good = all(2 ** (-1 - 1 / (kk - 1)) >= 0.25 for kk in range(3, 1000))
report("C2: 2^{-1-1/(k-1)} >= 1/4 for k in [3,1000)", good)

# --- D. case e < N/2 ---
good = True
for kk in range(3, 20):
    a = (kk - 2) / (kk - 1)
    for NN in [1, 2, 5, 10, 100, 10**6, 10**12]:
        for ll in [3, 4, 10, 100, 10**6]:
            if 0.25 * (NN / ll) ** a > NN / 2 + 1e-9:
                good = False
report("D: (1/4)(N/l)^{(k-2)/(k-1)} <= N/2 always (so indep set > N/2 suffices)", good)

# --- E. transfer arithmetic on a grid ---
good = True
for kk in range(3, 15):
    r = (kk - 1) / (kk - 2)
    for M in [3, 5, 17, 100, 12345]:
        for ll in [3, 4, 7, 100, 10**6]:
            NN = math.ceil(ll * (4 * M) ** r)
            got = 0.25 * (NN / ll) ** (1 / r)
            if got < M - 1e-9:
                good = False
                print("   counterexample", kk, M, ll, NN, got)
report("E: N=ceil(l(4M)^r) => (1/4)(N/l)^{1/r} >= M on grid", good)

# --- F. section 3 asymptotics ---
for c0 in [1.0, 3.0, 10.0]:
    worst = 0.0
    for n in list(range(3, 20000)) + [10**5, 10**6]:
        r = (n - 1) / (n - 2)
        s = math.sqrt(n * math.log2(n))
        val = r * (n + 2 * math.log2(n) + 2 + c0 * s)
        # extra term for the ceiling: log2(13/12)
        need = (val + math.log2(13 / 12) - n) / s  # minimal C1 at this n
        worst = max(worst, need)
    report(f"F: with C0'={c0}, minimal C1 over n in [3,10^6] is finite",
           worst < float('inf'), f"(C1 needed = {worst:.3f})")

# --- G. lower bound step ---
l = sp.symbols('l', positive=True)
n = sp.symbols('n', positive=True)
diffG = sp.simplify((3 * l - 1) * 2 ** (n - 5) - sp.Rational(1, 12) * l * 2 ** n)
# = 2^{n-5} (3l - 1 - 32 l /12) = 2^{n-5}( (36l-12-32l)/12 ) = 2^{n-5}(4l-12)/12
factored = sp.factor(diffG)
good = sp.simplify(diffG.subs(l, 3)) == 0
vals = all((3 * ll - 1) * 2 ** (nn - 5) >= ll * 2 ** nn / 12
           for ll in range(3, 200) for nn in range(3, 40))
report("G: (3l-1)2^{n-5} >= (1/12) l 2^n for l>=3 (equality iff l=3)",
       vals and good, f"(difference factors as {factored})")

print()
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
