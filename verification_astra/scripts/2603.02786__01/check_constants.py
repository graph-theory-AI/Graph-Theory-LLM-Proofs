"""Numerically confirm S(n) = sum_{p<=n} p(n-p) ~ (1/6) n^3/ln n and n^2*pi(n) ~ n^3/ln n."""
from sympy import sieve
import math
sieve.extend(10**8)
ps = list(sieve._list)
print(f"{'n':>10} {'S(n)/(n^3/ln n)':>18} {'n^2 pi(n)/(n^3/ln n)':>22} {'S/(n^2 pi)':>12}")
for n in [10**4, 10**5, 10**6, 10**7, 10**8]:
    S = 0; cnt = 0
    for p in ps:
        if p > n: break
        S += p*(n-p); cnt += 1
    base = n**3/math.log(n)
    print(f"{n:>10} {S/base:>18.5f} {n*n*cnt/base:>22.5f} {S/(n*n*cnt):>12.5f}")
print("limits: 1/6 =", 1/6, "; 1 ; 1/6")
