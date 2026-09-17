"""EXACT test of the writeup's Lemma 1 (== the r>=3 generalisation of Conlon-Fox-Pham's
Lemma 7, which is the real content of their Conjecture 10).

Lemma 1 claim:  for any t_0<t_1<... -> oo and any labels gamma_k in [r], with
J_k = [t_k, lambda t_{k+1}] and U_i = union of J_k over gamma_k = i,

        max_i  limsup_T |U_i cap [0,T]| / T   >=   C_{r,lambda} = b^{r-1}/(lambda r).

Only the MAXIMAL MONOCHROMATIC RUNS of the label word matter: a run of colour i spanning
block indices f..l contributes exactly the interval [t_f, lambda t_{l+1}].  So in the
continuum limit a configuration is:  run boundaries x_0<x_1<x_2<... (x_j = t at the start
of run j) with colours c_j (c_j != c_{j+1}), and run j contributes [x_j, lambda x_{j+1}].

We search over LOG-PERIODIC configurations: log-gaps g_1..g_P>0 and colours c_1..c_P,
repeated with log-period Lambda = sum(g).  For such a configuration the upper density is
computed EXACTLY (no truncation): the picture is self-similar with linear ratio
rho = e^Lambda, so if colour i's merged components in one period have linear endpoints
(a_1,b_1),...,(a_q,b_q) then the density at b_j is

    [ sum_{j'<=j} (b_j' - a_j')  +  (sum_all (b-a)) / (rho - 1) ] / b_j ,

and the limsup is the max over j.  (The previous referee run truncated at 60 periods,
which reported a bogus "counterexample" at density 1/2 for configurations with all gaps
-> 0; those are exactly the configurations where every run merges into ONE unbounded
component, whose true density is 1.  The exact formula below gets this right.)

Finding max_i density < C_r would DISPROVE Lemma 1 and hence the writeup.
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import brentq, minimize

RNG = np.random.default_rng(20260917)
LOGLAM = math.log(2.0)          # lambda = 2
LAM = 2.0


def b0(r, lam=LAM):
    f = lambda b: b ** r - lam * r * b + r - 1
    hi = 2.0
    while f(hi) < 0:
        hi *= 2
    return brentq(f, lam ** (1.0 / (r - 1)) + 1e-14, hi, xtol=1e-16, rtol=8.9e-16)


def Cstar(r, lam=LAM):
    return b0(r, lam) ** (r - 1) / (lam * r)


def upper_density(gaps, colors, r, lam=LAM):
    """EXACT max_i limsup density for the log-periodic configuration.

    gaps[j] = log(x_{j+1}/x_j) for j in one period; colors[j] = colour of run j.
    Returns max over colours of the exact limsup upper density (1.0 if some colour's
    intervals merge into a single unbounded component).  All exponentials are taken
    relative to the component being evaluated, so no overflow is possible.
    """
    P = len(gaps)
    gaps = np.clip(np.asarray(gaps, dtype=float), 1e-12, 40.0)
    Lam = float(gaps.sum())
    if Lam <= 0:
        return 1.0
    loglam = math.log(lam)
    y = np.concatenate(([0.0], np.cumsum(gaps)))

    def Y(j):                      # log x_j for any integer j
        q, s = divmod(j, P)
        return y[s] + q * Lam

    worst = 0.0
    for i in range(r):
        idx = [j for j in range(P) if colors[j] == i]
        if not idx:
            continue
        nxt = {}
        prev = {}
        for a, j in enumerate(idx):
            nxt[j] = idx[(a + 1) % len(idx)] + (P if a + 1 == len(idx) else 0)
            prev[j] = idx[a - 1] - (P if a == 0 else 0)
        merges = {j: (Y(nxt[j]) <= Y(j + 1) + loglam + 1e-15) for j in idx}
        if all(merges.values()):
            return 1.0                      # one unbounded component -> density 1
        comps = []
        for j in idx:
            if merges[prev[j] % P]:
                continue                    # j is not a component start
            l = j
            while merges[l % P]:
                l = nxt[l % P] + (l - l % P)
            comps.append((Y(j), Y(l + 1) + loglam))
        if not comps:
            return 1.0
        comps.sort()
        la = np.array([c[0] for c in comps])      # log left endpoints
        lb = np.array([c[1] for c in comps])      # log right endpoints
        # evaluate the density at the right endpoint of each component, everything
        # measured relative to that endpoint so exponentials stay in [0,1].
        for jj in range(len(comps)):
            ref = lb[jj]
            # components of this period with right endpoint <= ref
            cur = np.exp(lb[:jj + 1] - ref) - np.exp(la[:jj + 1] - ref)
            # all earlier periods: total per-period length scaled by e^{-m Lam}, m>=1
            per = (np.exp(lb - ref) - np.exp(la - ref)).sum()
            tail = per * math.exp(-Lam) / (1.0 - math.exp(-Lam))
            worst = max(worst, float(cur.sum() + tail))
    return min(worst, 1.0)


def search(r, P, ntrials, colors=None):
    best = (np.inf, np.zeros(P), np.zeros(P, dtype=int))
    words = ([np.array(colors)] if colors is not None
             else [np.array(w) for w in itertools.product(range(r), repeat=P)
                   if all(w[j] != w[(j + 1) % P] for j in range(P)) and min(w) == 0])
    if not words:
        return (np.inf, np.zeros(P), np.zeros(P, dtype=int))
    for w in words:
        for _ in range(ntrials):
            z0 = RNG.uniform(-1.5, 1.2, size=P)
            obj = lambda z: upper_density(np.exp(z), w, r)
            res = minimize(obj, z0, method="Nelder-Mead",
                           options={"maxiter": 4000, "xatol": 1e-11, "fatol": 1e-14})
            v = upper_density(np.exp(res.x), w, r)
            if v < best[0]:
                best = (v, np.exp(res.x), w.copy())
    return best


if __name__ == "__main__":
    print("Exact test of Lemma 1 (lambda = 2).  Searching for max_i density < C_r.\n")
    for r in [2, 3, 4, 5]:
        C = Cstar(r)
        b = b0(r)
        cyc = upper_density(np.full(r, math.log(b)), np.arange(r), r)
        print(f"r={r}:  b_0={b:.10f}  C_r={C:.12f}   cyclic equal-ratio config gives "
              f"{cyc:.12f}  (diff {cyc - C:+.2e})", flush=True)
        overall = np.inf
        for P in range(2, min(3 * r, 9) + 1):
            nt = 400 if P <= 4 else (120 if P <= 6 else 40)
            v, g, w = search(r, P, nt)
            if not np.isfinite(v):
                print(f"    P={P}: no valid colour word (no proper cyclic word with "
                      f"{r} colours)", flush=True)
                continue
            overall = min(overall, v)
            flag = "  <<<< BELOW C_r" if v < C - 1e-9 else ""
            print(f"    P={P}: min over all colour words = {v:.12f}  ({v - C:+.3e})"
                  f"  run-ratios={np.round(np.exp(g), 5).tolist()} word={w.tolist()}{flag}",
                  flush=True)
        verdict = "NO counterexample" if overall > C - 1e-9 else "*** COUNTEREXAMPLE ***"
        print(f"  => r={r}: best found {overall:.12f}  vs C_r {C:.12f}  -> {verdict}\n",
              flush=True)
