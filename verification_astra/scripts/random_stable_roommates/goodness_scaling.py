"""Measure Q(B_K) (failure of the writeup's 'goodness' condition for the collection of
all F-cycles of length in [2,K]) as a function of n and K.
Writeup eq.(22) claims Q(B_K) = O(K^2 a/S + K^2/S^2) ~ K^2 log n / n.
Chin-Michelen's analogous bad event D_1 is bounded by n^{-1+4 alpha} ~ K^4/n.
"""
import sys, math
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from planted_sim import sample_x, sample_scores, build_F, cycles_of

def run(n, trials, Ks, seed=3):
    rng = np.random.default_rng(seed)
    part = np.arange(n) ^ 1
    fail = {K: [0, 0] for K in Ks}   # partner-collision, blocking
    meanC = {K: 0.0 for K in Ks}
    for t in range(trials):
        x, S, tries, _ = sample_x(n, rng)
        U = sample_scores(n, x, rng)
        f, F, has = build_F(n, x, U)
        cyc = cycles_of(F, has, n)
        uf = U[np.arange(n), f]
        for K in Ks:
            C = [v for c in cyc if 2 <= len(c) <= K for v in c]
            meanC[K] += sum(1 for c in cyc if 2 <= len(c) <= K)
            Cs = set(C)
            if any(part[v] in Cs for v in C):
                fail[K][0] += 1
                continue
            Ca = np.array(C, dtype=int)
            if len(Ca) > 1:
                sub = U[np.ix_(Ca, Ca)] < uf[Ca][:, None]
                np.fill_diagonal(sub, False)
                if (sub & sub.T).any():
                    fail[K][1] += 1
    print(f"n={n} trials={trials}")
    print("   K   Q(B_K)    partner  block    K^2/n    K^4/n   Q(B_K)/(K^2/n)  E[C_K]")
    for K in Ks:
        p = (fail[K][0] + fail[K][1]) / trials
        print(f"  {K:3d}  {p:7.4f}   {fail[K][0]:5d}  {fail[K][1]:5d}  {K*K/n:8.4f} {K**4/n:9.3f}"
              f"     {p/(K*K/n):8.3f}     {meanC[K]/trials:6.3f}")

if __name__ == "__main__":
    n = int(sys.argv[1]); trials = int(sys.argv[2])
    Ks = [int(s) for s in sys.argv[3].split(',')]
    run(n, trials, Ks, seed=int(sys.argv[4]) if len(sys.argv) > 4 else 3)
