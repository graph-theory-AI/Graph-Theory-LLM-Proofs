"""Check the constants: b_0 root, C_r = b^(r-1)/(2r), the (1-1/2b)(1+1/(2rb-r)) form,
the 2^r vs 2r transcription, b_0 > 2^{1/(r-1)}, and C_{r,lambda} = inf_q D_{r,lambda}(q).
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
import mpmath as mp

mp.mp.dps = 40


def b0(r, lam=2.0):
    f = lambda b: b**r - lam * r * b + r - 1
    # unique root > 1 ; bracket
    lo = 1.0 + 1e-12
    hi = 2.0
    while f(hi) < 0:
        hi *= 2
    return brentq(f, max(lo, lam ** (1.0 / (r - 1))), hi, xtol=1e-15, rtol=1e-15)


def D(r, lam, q):
    return (1 - 1.0 / (lam * q)) / (1 - q ** (-float(r)))


print(f"{'r':>3} {'b0':>16} {'b^(r-1)/(2r)':>16} {'(1-1/2b)(1+1/(2rb-r))':>22} "
      f"{'2^r version':>16} {'inf_q D_{r,2}':>16} {'2^{1/(r-1)}':>12}")
for r in range(2, 11):
    b = b0(r)
    c1 = b ** (r - 1) / (2 * r)
    c2 = (1 - 1 / (2 * b)) * (1 + 1 / (2 * r * b - r))
    c3 = (1 - 1 / (2 * b)) * (1 + 1 / (2.0 ** r * b - r))
    res = minimize_scalar(lambda q: D(r, 2.0, q), bounds=(1.0000001, 100), method="bounded",
                          options={"xatol": 1e-12})
    print(f"{r:>3} {b:16.12f} {c1:16.12f} {c2:22.12f} {c3:16.12f} {res.fun:16.12f} "
          f"{2 ** (1.0/(r-1)):12.6f}  minimizer q*={res.x:.10f}")

print()
print("r=2 exact check: b0 =", b0(2), " 2+sqrt3 =", 2 + np.sqrt(3))
print("c2 =", b0(2) / 4, " (2+sqrt3)/4 =", (2 + np.sqrt(3)) / 4)
print()
print("lambda -> 2 continuity of C_{r,lambda} = b_{r,lambda}^{r-1}/(lambda r):")
for r in [2, 3, 5]:
    row = []
    for lam in [1.5, 1.9, 1.99, 1.999, 2.0]:
        b = b0(r, lam)
        row.append(f"lam={lam}: {b**(r-1)/(lam*r):.10f}")
    print(f"  r={r}: " + "   ".join(row))
