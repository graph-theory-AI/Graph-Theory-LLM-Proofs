"""Exhaustive-word search for a counterexample to the writeup's Lemma 1 (lambda = 2).

Uses the exact self-similar limsup from 06_geometric_exact.py.  For every period length
P and every colour word up to rotation + colour permutation -- so ALL the NON-CYCLIC
patterns that Conlon-Fox-Pham's Lemma 7 argument cannot handle are included -- the
log-gaps are optimised by multi-start Nelder-Mead.

A value strictly below C_r = b_0^{r-1}/(2r) would disprove Lemma 1 and hence the
writeup's whole lower bound.
"""
import itertools
import importlib.util
import math
import os

import numpy as np
from scipy.optimize import minimize

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "gex", os.path.join(_here, "06_geometric_exact.py"))
gex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gex)
upper_density, b0, Cstar = gex.upper_density, gex.b0, gex.Cstar

RNG = np.random.default_rng(2718281)


def canonical_words(r, P):
    """proper cyclic words on exactly r colours, up to rotation and colour permutation"""
    seen, out = set(), []
    for w in itertools.product(range(r), repeat=P):
        if any(w[j] == w[(j + 1) % P] for j in range(P)):
            continue
        if len(set(w)) < r:            # fewer active colours -> covered by smaller r
            continue
        best = None
        for rot in range(P):
            ww = w[rot:] + w[:rot]
            for perm in itertools.permutations(range(r)):
                key = tuple(perm[c] for c in ww)
                if best is None or key < best:
                    best = key
        if best in seen:
            continue
        seen.add(best)
        out.append(np.array(w))
    return out


def optimise_word(w, r, ntrials, b):
    P = len(w)
    best = (np.inf, None)
    starts = [np.full(P, math.log(math.log(b)))]
    starts += [RNG.uniform(-2.0, 1.0, size=P) for _ in range(ntrials)]
    for z0 in starts:
        res = minimize(lambda z: upper_density(np.exp(z), w, r), z0,
                       method="Nelder-Mead",
                       options={"maxiter": 2500, "xatol": 1e-11, "fatol": 1e-14})
        v = upper_density(np.exp(res.x), w, r)
        if v < best[0]:
            best = (v, np.exp(np.exp(res.x)))
    return best


if __name__ == "__main__":
    for r in [2, 3, 4, 5]:
        C, b = Cstar(r), b0(r)
        print(f"\n=== r={r}:  b_0={b:.10f}   C_r={C:.12f} ===", flush=True)
        overall = np.inf
        Pmax = {2: 8, 3: 7, 4: 6, 5: 6}[r]
        for P in range(2, Pmax + 1):
            words = canonical_words(r, P)
            if not words:
                continue
            nt = 120 if P <= 4 else (30 if P <= 6 else 10)
            bw, bv, bg = None, np.inf, None
            for w in words:
                v, g = optimise_word(w, r, nt, b)
                if v < bv:
                    bv, bw, bg = v, w.copy(), g
            overall = min(overall, bv)
            flag = "   <<<< BELOW C_r" if bv < C - 1e-9 else ""
            print(f"  P={P}: {len(words):4d} words  min={bv:.12f}  ({bv - C:+.3e})  "
                  f"word={bw.tolist()} ratios={np.round(bg, 5).tolist()}{flag}", flush=True)
        print(f"  => r={r}: overall min {overall:.12f} vs C_r {C:.12f}  -> "
              f"{'NO counterexample' if overall > C - 1e-9 else '*** COUNTEREXAMPLE ***'}",
              flush=True)
