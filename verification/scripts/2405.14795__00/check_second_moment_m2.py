#!/usr/bin/env python3
"""Exact second-moment ratio for m=2 rainbow stackings, and threshold asymptotics.

For m=2 the writeup's quantities are exactly computable:
  E[X^2]/(E X)^2 = E_pi prod_{orbits of pi-hat} (1 + (r-1)^{1-2l}),
where pi-hat is the action of pi on unordered pairs and l runs over orbit sizes
(orbit of size l  <->  component of B = cycle with 2l edges, whose proper
r-edge-coloring count is (r-1)^{2l} + (r-1)).

We enumerate cycle types (partitions of n) and use the classical orbit-size
decomposition of the pair action:
  - within a cycle of length a: (a-1)/2 orbits of size a (a odd);
    (a-2)/2 orbits of size a plus one of size a/2 (a even);
  - between two distinct cycles of lengths a,b: gcd(a,b) orbits of size lcm(a,b).

Also solves l_n(x) = (m-1) log n! + N log p_m(x) = 0 numerically and compares
rho_m(n) - m N/(2 log n!) with (2m-1)/6.
"""
import math
from math import gcd, lcm, comb, log, log1p

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0:
        yield []
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest

def orbit_multiset(part):
    """multiset of orbit sizes of the pair action, as dict size->count"""
    orb = {}
    def add(l, c=1):
        orb[l] = orb.get(l, 0) + c
    # collect multiplicities
    mult = {}
    for a in part: mult[a] = mult.get(a, 0) + 1
    lens = sorted(mult)
    for a in lens:
        ma = mult[a]
        # within-cycle orbits, per cycle
        if a >= 2:
            if a % 2 == 1:
                add(a, ma * (a - 1) // 2)
            else:
                add(a, ma * (a - 2) // 2)
                add(a // 2, ma)
        # between two cycles of same length a
        if ma >= 2:
            add(a, a * comb(ma, 2))  # gcd(a,a)=a orbits of size lcm=a
    for i, a in enumerate(lens):
        for b in lens[i+1:]:
            add(lcm(a, b), gcd(a, b) * mult[a] * mult[b])
    return orb

def class_size_log(part, logfact_n):
    mult = {}
    for a in part: mult[a] = mult.get(a, 0) + 1
    denom = 0.0
    for a, ma in mult.items():
        denom += ma * log(a) + math.lgamma(ma + 1)
    return logfact_n - denom  # log of #permutations with this cycle type

def second_moment_ratio_m2(n, r):
    N = comb(n, 2)
    logfact = math.lgamma(n + 1)
    total = 0.0
    log_r1 = log(r - 1)
    for part in partitions(n):
        orb = orbit_multiset(part)
        lw = class_size_log(part, logfact) - logfact  # log prob of class
        for l, c in orb.items():
            lw += c * log1p((r - 1) ** (1 - 2 * l)) if l < 20 else 0.0
        total += math.exp(lw)
    return total

def mu(n, r, m=2):
    N = comb(n, 2)
    return math.exp((m - 1) * math.lgamma(n + 1) + N * sum(log1p(-j / r) for j in range(1, m)))

def solve_rho(n, m):
    N = comb(n, 2)
    logfact = math.lgamma(n + 1)
    def ell(x):
        return (m - 1) * logfact + N * sum(log1p(-j / x) for j in range(1, m))
    lo, hi = float(m), 10.0 * m * N / (2 * logfact) + 10
    while ell(lo) > 0: lo = (lo + m - 1) / 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if ell(mid) < 0: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

if __name__ == "__main__":
    print("=== m=2 exact second-moment ratio E[X^2]/(E X)^2 near threshold ===")
    for n in (20, 30, 40):
        rho = solve_rho(n, 2)
        print(f"n={n}: first-moment root rho_2(n) = {rho:.4f}; "
              f"m N/(2 log n!) + 1/2 = {2*comb(n,2)/(2*math.lgamma(n+1)) + 0.5:.4f}")
        for r in (int(rho) - 1, int(rho), int(rho) + 1, int(rho) + 2, int(rho) + 4):
            if r < 2: continue
            ratio = second_moment_ratio_m2(n, r)
            m_ = mu(n, r)
            lb = 1.0 / ratio  # Cauchy-Schwarz lower bound on P(X>0)
            print(f"   r={r:3d}: mu={m_:.4g}  EX^2/(EX)^2={ratio:.6f}  P(X>0)>={lb:.6f}")
    print()
    print("=== rho_m(n) - mN/(2 log n!) -> (2m-1)/6 ? ===")
    for m in (2, 3, 5):
        for n in (10**3, 10**4, 10**5, 10**6):
            rho = solve_rho(n, m)
            base = m * comb(n, 2) / (2 * math.lgamma(n + 1))
            print(f"  m={m} n={n:>8}: rho - mN/(2 log n!) = {rho - base:.5f}   (2m-1)/6 = {(2*m-1)/6:.5f}")
