"""Refined check F: interior density of the runsort permuton.

For y-strips (c,d) and a safety margin delta away from the boundary curve
x_c(y) = y e^{1-y}, compare:
  - empirical mass of {(x,y): y in (c,d), x < x_c(c) - delta}   (curve increasing => x_c(c) = min over strip)
    vs theory  e^{y-1} integrated:  int_c^d e^{y-1} (x_c(c)-delta) dy
  - x-uniformity across 10 bins of (0, x_c(c)-delta)
  - near-boundary mass in (x_c(c)-delta, x_c(d)+delta) vs theory (atom (1-y) + interior sliver)
Also: mass strictly above x_c(d)+delta should be ~0 (support check).
"""
import numpy as np

rng = np.random.default_rng(7)
N = 1_000_000
TRIALS = 8
delta = 0.02
strips = [(0.15, 0.20), (0.40, 0.45), (0.60, 0.65), (0.85, 0.90)]

acc = {s: {"low": 0, "mid": 0, "hi": 0, "tot": 0, "hist": np.zeros(10)} for s in strips}

for t in range(TRIALS):
    pi = rng.permutation(N) + 1
    starts = np.empty(N, dtype=bool)
    starts[0] = True
    starts[1:] = pi[:-1] > pi[1:]
    run_id = np.cumsum(starts) - 1
    A = pi[starts][run_id]
    order = np.lexsort((np.arange(N), A))
    sigma = pi[order]
    xs = np.arange(1, N + 1) / N
    ys = sigma / N
    for (c, d) in strips:
        sel = (ys >= c) & (ys < d)
        x_s = xs[sel]
        lo_cut = c * np.exp(1 - c) - delta
        hi_cut = d * np.exp(1 - d) + delta
        a = acc[(c, d)]
        a["tot"] += sel.sum()
        a["low"] += (x_s < lo_cut).sum()
        a["mid"] += ((x_s >= lo_cut) & (x_s <= hi_cut)).sum()
        a["hi"] += (x_s > hi_cut).sum()
        a["hist"] += np.histogram(x_s[x_s < lo_cut], bins=10, range=(0, lo_cut))[0]

tot = TRIALS * N
print(f"n={N}, trials={TRIALS}, delta={delta}")
for (c, d) in strips:
    a = acc[(c, d)]
    lo_cut = c * np.exp(1 - c) - delta
    hi_cut = d * np.exp(1 - d) + delta
    # theory: interior mass below lo_cut = int_c^d e^{y-1} * lo_cut dy
    th_low = lo_cut * (np.exp(d - 1) - np.exp(c - 1))
    # theory near-boundary band: atom int_c^d (1-y) dy + interior sliver int_c^d e^{y-1}(min(x_c(y),hi_cut)-lo_cut) dy
    yy = np.linspace(c, d, 20001)
    th_mid = np.trapezoid((1 - yy) + np.exp(yy - 1) * (yy * np.exp(1 - yy) - lo_cut), yy)
    emp_low = a["low"] / tot
    emp_mid = a["mid"] / tot
    emp_hi = a["hi"] / tot
    dens = a["hist"] / a["low"] * 10
    emp_density = emp_low / ((d - c) * lo_cut)
    th_density = (np.exp(d - 1) - np.exp(c - 1)) / (d - c)
    print(f"\nstrip y in ({c},{d}):  x-cut {lo_cut:.4f}")
    print(f"  interior mass  emp {emp_low:.6f}  theory {th_low:.6f}  rel.err {abs(emp_low-th_low)/th_low:.4f}")
    print(f"  implied density emp {emp_density:.5f}  vs e^(y-1) avg {th_density:.5f}")
    print(f"  near-boundary band mass emp {emp_mid:.6f}  theory {th_mid:.6f}")
    print(f"  mass above curve+delta   emp {emp_hi:.2e}  (should be ~0)")
    print(f"  x-uniformity, 10 bins (should be ~1): {np.array2string(dens, precision=3)}")
    print(f"     max |bin-1| = {np.max(np.abs(dens-1)):.4f}")
print("\nDONE")
