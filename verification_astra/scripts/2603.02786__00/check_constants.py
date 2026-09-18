"""Constants / asymptotics used in the writeup (Sections 1, 5, 8)."""
from sympy import primerange, integrate, Rational, symbols, S
import math

x = symbols('x')
u = symbols('u')
# 2 * int_0^1 (1-u^2) du  -> claimed 4/3
I1 = 2*integrate(1-u**2, (u, 0, 1))
# 2 * int_0^1 (1-u^2/2) du -> the paper's 5/3 (pairwise-only savings), sanity check
I2 = 2*integrate(1-u**2/2, (u, 0, 1))
print("2*int_0^1 (1-u^2)du   =", I1)
print("2*int_0^1 (1-u^2/2)du =", I2)
# (5.9): 2*int_eps^1 (1-u^2) du = 4/3 - 2eps + (2/3) eps^3
eps = symbols('eps')
print("2*int_eps^1 (1-u^2)du =", (2*integrate(1-u**2,(u,eps,1))).expand())

# PNT-based sums: n*pi(sqrt n) ~ 2 T_n ; sum_{p<=sqrt n} p^2 ~ (2/3) T_n
for N in [10**6, 10**7, 10**8, 10**9, 10**10]:
    X = int(math.isqrt(N))
    ps = list(primerange(2, X+1))
    pi = len(ps); s2 = sum(p*p for p in ps)
    T = N**1.5/math.log(N)
    print(f"n=1e{round(math.log10(N))}: n*pi(x)/T={N*pi/T:.4f} (->2)   sum p^2/T={s2/T:.4f} (->2/3={2/3:.4f})"
          f"   (n*pi - sum p^2)/T={(N*pi-s2)/T:.4f} (->4/3)")
