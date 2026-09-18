#!/usr/bin/env python3
"""Independent check of Section 4 (the rank lower bound) of the writeup.

For an actual equivalence cover produced by the Section-2 construction we build
    M_{uv} = prod_l (c_l(u) - c_l(v))
with random real labels, and check
  (i)  M_{uv} = 0  iff  u = v or uv in E,
  (ii) rank(M) <= 2^t,
  (iii) the 2s x 2s submatrix N_{ij} = M_{i,(s+j) mod n} is triangular with
        nonzero diagonal, hence rank 2s,
  (iv) therefore 2s <= 2^t, i.e. t >= ceil(log2(2s)) = r+1.
Also checks the writeup's minor against Alon's Theorem 1.1 (1986) hypothesis.
"""
import itertools
import numpy as np
from construction_check import cover_divisible, cyc_dist, edges_cycle_power

rng = np.random.default_rng(12345)
print(f"{'n':>4} {'k':>3} {'s':>3} {'t':>3} {'2^t':>6} {'rank M':>7} {'rank N':>7} {'2s':>4}"
      f" {'zero-pattern':>13} {'triangular':>11} {'Alon 1.1 hyp':>13}")
for k in [1, 2, 3, 4, 5, 7, 8, 9, 15]:
    s = k + 1
    for m in [2, 3]:
        n = m * s
        if n > 60:
            continue
        layers, r = cover_divisible(n, k)
        t = len(layers)
        # component labels; vertices in no listed part are their own singleton
        C = np.zeros((n, t))
        for li, parts in enumerate(layers):
            lab = {}
            for pi, Q in enumerate(parts):
                for v in Q:
                    lab[v] = pi
            nxt = len(parts)
            for v in range(n):
                if v not in lab:
                    lab[v] = nxt
                    nxt += 1
            vals = rng.normal(size=nxt)
            for v in range(n):
                C[v, li] = vals[lab[v]]
        M = np.ones((n, n))
        for l in range(t):
            M *= (C[:, l][:, None] - C[:, l][None, :])
        E = edges_cycle_power(n, k)
        pat_ok = True
        for u in range(n):
            for v in range(n):
                should_be_zero = (u == v) or ((min(u, v), max(u, v)) in E)
                if should_be_zero != (abs(M[u, v]) < 1e-12):
                    pat_ok = False
        N = np.array([[M[i, (s + j) % n] for j in range(2 * s)] for i in range(2 * s)])
        tri_ok = all(abs(N[i, j]) < 1e-12 for i in range(2 * s) for j in range(2 * s) if i > j)
        diag_ok = all(abs(N[i, i]) > 1e-12 for i in range(2 * s))
        # Alon Thm 1.1 hypothesis for u_i = i, w_i = (s+i) mod n, i = 0..2s-1
        u_ = list(range(2 * s))
        w_ = [(s + i) % n for i in range(2 * s)]
        alon = all(
            (min(u_[i], w_[i]), max(u_[i], w_[i])) not in E and u_[i] != w_[i]
            for i in range(2 * s)
        ) and all(
            u_[i] == w_[j] or (min(u_[i], w_[j]), max(u_[i], w_[j])) in E
            for i in range(2 * s) for j in range(i + 1, 2 * s)
        )
        rM = np.linalg.matrix_rank(M, tol=1e-9)
        rN = np.linalg.matrix_rank(N, tol=1e-9)
        print(f"{n:4d} {k:3d} {s:3d} {t:3d} {2**t:6d} {rM:7d} {rN:7d} {2*s:4d}"
              f" {str(pat_ok):>13} {str(tri_ok and diag_ok):>11} {str(alon):>13}")
        assert pat_ok and tri_ok and diag_ok and rN == 2 * s and rM <= 2 ** t and 2 * s <= 2 ** t
print("\nall assertions passed")
