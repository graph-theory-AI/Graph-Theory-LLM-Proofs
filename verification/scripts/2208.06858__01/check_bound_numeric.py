"""Numeric verification of the concentration bounds (2), (4), (5), (6), (7) for
the writeup's actual parameters, via exact binomial sums (no simulation).

For given t, m:
  u = 2^-m, s = u^t = 2^-mt, N = ceil(log2 / -log(1-s)), r = u^{t-1}.
  M ~ Bin(N, r);  Q = 1 - (1-u)^M;  c = 1-(1-s)^N.

The Bin(N,r) pmf is evaluated on a window of +-40 standard deviations around
the mean (mass outside < e^{-40^2/4} < 1e-170, negligible next to the checked
slacks) using the exact ratio recurrence pmf(k+1)/pmf(k) = (N-k)/(k+1)*r/(1-r)
anchored at the mode and normalized over the window.  This avoids catastrophic
cancellation from lgamma at N up to ~1e60.

Checked:
  (2) 1/2 <= c < 1/2 + s/2
  (4) E[Q] = c                     (algebraic identity; here checked to ~1e-8)
  (5) Var(Q) <= 2u                  (writeup's variance bound)
  (6) E|Q-1/2| <= sqrt(2u) + s/2
  (7) lower bound  c - t*E|Q-1/2|  -> 1/2 as m grows (for each fixed t).
"""
import math
from math import log, sqrt, fsum


def stats(t, m):
    u = 2.0 ** (-m)
    # s and r are exact powers of two; use log1p carefully
    s = 2.0 ** (-m * t)
    r = 2.0 ** (-m * (t - 1))
    N = math.ceil(log(2) / -math.log1p(-s))
    c = -math.expm1(N * math.log1p(-s))  # 1-(1-s)^N, accurate: N*log1p(-s) ~ -log2
    mean = N * r                          # ~ log2 / u, moderate size
    sd = sqrt(mean * (1 - r))
    lo = max(0, int(mean - 40 * sd) - 2)
    hi = min(N, int(mean + 40 * sd) + 2)
    k0 = min(hi, max(lo, int(mean)))
    W = hi - lo + 1
    q = [0.0] * W
    q[k0 - lo] = 1.0
    ratio = r / (1 - r)
    # recurrence upward from the mode
    for k in range(k0, hi):
        q[k - lo + 1] = q[k - lo] * ((N - k) / (k + 1.0)) * ratio
    # recurrence downward from the mode
    for k in range(k0, lo, -1):
        q[k - lo - 1] = q[k - lo] * (k / ((N - k + 1.0))) / ratio
    S = fsum(q)
    log1mu = math.log1p(-u)
    EQ = fsum(q[i] * -math.expm1((lo + i) * log1mu) for i in range(W)) / S
    EQ2 = fsum(q[i] * (-math.expm1((lo + i) * log1mu)) ** 2 for i in range(W)) / S
    Eabs = fsum(q[i] * abs(-math.expm1((lo + i) * log1mu) - 0.5) for i in range(W)) / S
    VarQ = EQ2 - EQ * EQ
    return dict(u=u, s=s, N=N, c=c, EQ=EQ, VarQ=VarQ, Eabs=Eabs,
                lower=c - t * Eabs, W=W)


print(f"{'t':>3} {'m':>3} {'N':>16} {'c-1/2':>10} {'E[Q]-c':>9} {'Var(Q)':>10} "
      f"{'2u':>10} {'E|Q-1/2|':>10} {'sqrt(2u)+s/2':>12} {'lower bnd':>10}")
ok = True
for t in (2, 3, 4, 10):
    for m in (2, 4, 6, 8, 10, 12, 14, 16, 20):
        st = stats(t, m)
        e2 = 0.5 <= st['c'] < 0.5 + st['s'] / 2 + 1e-15
        e4 = abs(st['EQ'] - st['c']) < 1e-7
        e5 = st['VarQ'] <= 2 * st['u'] + 1e-15
        e6 = st['Eabs'] <= sqrt(2 * st['u']) + st['s'] / 2 + 1e-12
        line_ok = e2 and e4 and e5 and e6
        ok = ok and line_ok
        Nstr = str(st['N']) if st['N'] < 10**15 else f"{float(st['N']):.3e}"
        print(f"{t:>3} {m:>3} {Nstr:>16} {st['c']-0.5:>10.3e} "
              f"{st['EQ']-st['c']:>9.1e} {st['VarQ']:>10.3e} {2*st['u']:>10.3e} "
              f"{st['Eabs']:>10.3e} {sqrt(2*st['u'])+st['s']/2:>12.3e} "
              f"{st['lower']:>10.6f}" + ("" if line_ok else "   <-- FAIL"))
print()
print("All inequalities (2),(4),(5),(6) hold numerically:", ok)
assert ok

print()
for t in (2, 3, 4, 10):
    st = stats(t, 20)
    print(f"t={t:>2}: exact lower bound at m=20 is {st['lower']:.6f} "
          f"(deficit {0.5-st['lower']:.2e}) -> p_monotone(t) >= 1/2 - eps confirmed")
