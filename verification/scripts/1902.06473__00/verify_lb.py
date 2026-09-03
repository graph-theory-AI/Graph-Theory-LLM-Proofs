#!/usr/bin/env python3
"""Check of writeup's inequality (18)  ln e(P) <= LB(P) <= 2 ln e(P)
(= Theorem 2 of arXiv:1902.06473, Kahn-Kim + CFJJM) and of the final
claim (3):  LB(P)/2 <= QLB(P) <= LB(P)/ln 2, with QLB computed via the
exact linear-extension formula F(P).

H(P) = min_{z in C(P)} -(1/n) sum ln z_i is computed with scipy SLSQP
(maximize sum ln z_i subject to chain constraints).
"""
import math, random
import numpy as np
from scipy.optimize import minimize
from verify_main import all_posets, F_and_exts, random_poset
from verify_qh_montecarlo import maximal_chains

def entropy(rel, n):
    chains = maximal_chains(rel, n)
    cons = [{'type': 'ineq',
             'fun': (lambda z, ch=ch: 1.0 - sum(z[v] for v in ch))}
            for ch in chains]
    x0 = np.full(n, 1.0 / n)
    res = minimize(lambda z: -np.sum(np.log(z)), x0,
                   bounds=[(1e-9, 1.0)] * n, constraints=cons,
                   method='SLSQP', options={'maxiter': 500, 'ftol': 1e-12})
    assert res.success, res.message
    return -np.sum(np.log(res.x)) / n   # H(P) in nats

def main():
    # sanity: paper's Figure 2 example: poset ({a,b,c}, b<=a) has H = (2/3) ln 2
    Hex = entropy(frozenset({(1, 0)}), 3)
    print(f"paper example entropy: computed {Hex:.6f}, expected {2/3*math.log(2):.6f}")
    assert abs(Hex - 2 / 3 * math.log(2)) < 1e-6

    worst = dict(lb_lo=float('inf'), lb_hi=float('inf'),
                 f_lo=float('inf'), f_hi=float('inf'))
    count = 0

    def check(rel, n):
        nonlocal count
        F, e = F_and_exts(rel, list(range(n)))
        lnE = math.log(e)
        LB = n * (math.log(n) - entropy(rel, n))
        Ff = float(F)
        worst['lb_lo'] = min(worst['lb_lo'], LB - lnE)          # ln e <= LB
        worst['lb_hi'] = min(worst['lb_hi'], 2 * lnE - LB)      # LB <= 2 ln e
        worst['f_lo'] = min(worst['f_lo'], Ff - LB / 2)         # LB/2 <= F
        worst['f_hi'] = min(worst['f_hi'], LB / math.log(2) - Ff)  # F <= LB/ln2
        for key, val in worst.items():
            assert val > -1e-6, (key, val, rel)
        count += 1

    for n in range(2, 6):
        for rel in all_posets(n):
            check(rel, n)
    rng = random.Random(7)
    for n, trials in [(6, 200), (7, 100)]:
        for _ in range(trials):
            check(random_poset(n, rng.choice([0.15, 0.3, 0.5]), rng), n)

    print(f"{count} posets checked (exhaustive n=2..5 + random n=6,7)")
    print(f"min slack LB - ln e      = {worst['lb_lo']:.6f}")
    print(f"min slack 2 ln e - LB    = {worst['lb_hi']:.6f}")
    print(f"min slack F - LB/2       = {worst['f_lo']:.6f}")
    print(f"min slack LB/ln2 - F     = {worst['f_hi']:.6f}")
    print("ALL CHECKS PASSED")

if __name__ == '__main__':
    main()
