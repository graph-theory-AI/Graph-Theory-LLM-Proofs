"""Numerically probe the writeup's Lemma 1 (== Conlon-Fox-Pham's Lemma 7, generalised to r>=3,
which is their Conjecture 10's real obstruction).

Model.  A configuration is an increasing sequence x_0<x_1<... -> oo of breakpoints on the
t-scale (the positions of the maximal monochromatic runs of the colour word) plus colours
c_j in [r].  Run j contributes the interval [x_j, lambda*x_{j+1}] to U_{c_j}.  This is
exactly the structure of Lemma 1 (J_k=[t_k,lambda t_{k+1}]; a maximal run f..l of colour i
contributes [t_f, lambda t_{l+1}]).

Claim under test:  min over configurations of  max_i limsup_T |U_i cap [0,T]|/T
                   == C_{r,lambda} = inf_{q>1} (1-1/(lambda q))/(1-q^{-r}) = b^{r-1}/(lambda r).

Finding a configuration strictly below C_{r,lambda} would DISPROVE Lemma 1.
|U cap[0,T]|/T has local maxima only at right endpoints of connected components, so we
evaluate only there.
"""
import sys

import numpy as np
from scipy.optimize import brentq, minimize

RNG = np.random.default_rng(20260917)


def b0(r, lam):
    f = lambda b: b**r - lam * r * b + r - 1
    hi = 2.0
    while f(hi) < 0:
        hi *= 2
    return brentq(f, lam ** (1.0 / (r - 1)) + 1e-14, hi, xtol=1e-15, rtol=1e-15)


def Cstar(r, lam):
    return b0(r, lam) ** (r - 1) / (lam * r)


def max_density(logratios, colors, r, lam, nper=30, tail=8):
    """max over colours of the (limsup) upper density, for the log-periodic configuration."""
    P = len(logratios)
    logx = np.concatenate(([0.0], np.cumsum(np.tile(logratios, nper))))
    cols = np.tile(colors, nper)
    loglam = np.log(lam)
    left = logx[:-1]
    right = logx[1:] + loglam
    cutoff = logx[max(0, (nper - tail) * P)]
    worst = 0.0
    for i in range(r):
        idx = np.where(cols == i)[0]
        if idx.size == 0:
            continue
        a = left[idx]
        b = right[idx]
        # merge overlapping intervals (they are sorted by left endpoint)
        starts = [a[0]]
        ends = [b[0]]
        for j in range(1, idx.size):
            if a[j] <= ends[-1]:
                if b[j] > ends[-1]:
                    ends[-1] = b[j]
            else:
                starts.append(a[j])
                ends.append(b[j])
        starts = np.exp(np.array(starts))
        ends = np.exp(np.array(ends))
        tot = np.cumsum(ends - starts)
        sel = ends >= np.exp(cutoff)
        if sel.any():
            worst = max(worst, float(np.max(tot[sel] / ends[sel])))
    return worst


def optimise(r, lam, P, ntrials, colors=None, maxiter=1500):
    best = (np.inf, None, None)
    for _ in range(ntrials):
        cols = np.array(colors) if colors is not None else RNG.integers(0, r, size=P)
        z0 = RNG.uniform(0.05, 1.6, size=P)
        obj = lambda z: max_density(np.abs(z) + 1e-9, cols, r, lam)
        res = minimize(obj, z0, method="Nelder-Mead",
                       options={"maxiter": maxiter, "xatol": 1e-9, "fatol": 1e-12})
        val = max_density(np.abs(res.x) + 1e-9, cols, r, lam, nper=60, tail=12)
        if val < best[0]:
            best = (val, np.abs(res.x), cols)
    return best


if __name__ == "__main__":
    lam = 2.0
    print("Lemma 1 test: minimise max_i (upper density) over configurations; compare to C_r\n",
          flush=True)
    for r in [2, 3, 4, 5]:
        C = Cstar(r, lam)
        b = b0(r, lam)
        v_cyc = max_density(np.full(r, np.log(b)), np.arange(r), r, lam, nper=60, tail=12)
        print(f"r={r}:  C_r={C:.10f}  b_0={b:.8f}   cyclic/equal-ratio config -> "
              f"{v_cyc:.10f}  (gap {v_cyc-C:+.2e})", flush=True)
        overall = np.inf
        for P in range(1, 2 * r + 2):
            nt = 200 if P <= 3 else (120 if P <= 6 else 80)
            val, z, cols = optimise(r, lam, P, nt)
            overall = min(overall, val)
            flag = "   <<<< BEATS C_r"if val < C - 1e-6 else ""
            print(f"    P={P:2d}: best {val:.10f}  (C_r{val-C:+.2e})  ratios="
                  f"{np.round(np.exp(z),4).tolist()}  colours={cols.tolist()}{flag}",
                  flush=True)
        print(f"  => r={r}: best found over all searched periods {overall:.10f} vs C_r "
              f"{C:.10f}  -> {'NO counterexample' if overall > C - 1e-6 else 'COUNTEREXAMPLE'}\n",
              flush=True)
