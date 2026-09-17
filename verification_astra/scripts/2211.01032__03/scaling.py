"""E[F_n] for the non-orientable model (uniform rotation + iid fair signature),
and the writeup's finite-n bound
   B(n) = 1 + H_{n-2}/2  +  C(n) * sum_{k>=3} q^{k-2}/k  +  1/n
plus its asymptotic form ln n + 1/4 + gamma/2.
Also the split E[F^hit] (bound (2)) / E[F^avoid] (bound (12)).
"""
import sys, os, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V
GAMMA = 0.5772156649015329

def EF(n, reps, rng):
    N = 2 * n * (n - 1)
    it = int(np.ceil(np.log2(N))) + 1
    tot = 0; tot2 = 0
    for _ in range(reps):
        P = np.argsort(rng.random((n, n - 1)), axis=1)
        tw = np.zeros((n, n), dtype=np.int64)
        iu = np.triu_indices(n, 1)
        tw[iu] = rng.integers(0, 2, size=len(iu[0]))
        tw = tw + tw.T
        A = build_A(n, tw); V = build_V(n, P)
        sigma = A[V]
        m = np.arange(N, dtype=np.int64); s = sigma.copy()
        for _ in range(it):
            m = np.minimum(m, m[s]); s = s[s]
        lab = np.minimum(m, m[A])
        f = int(np.count_nonzero(lab == np.arange(N)))
        tot += f; tot2 += f * f
    mu = tot / reps
    sd = math.sqrt(max(tot2 / reps - mu * mu, 0) / reps)
    return mu, sd

if __name__ == "__main__":
    rng = np.random.default_rng(2024)
    print(f"{'n':>6} {'reps':>7} {'E[F]':>9} {'+-':>7} {'lnn+1/4+g/2':>12} "
          f"{'finite-n bound':>15} {'(E[F]-lnn)':>11}")
    for n, reps in [(20, 20000), (50, 20000), (100, 8000), (200, 3000),
                    (400, 800), (800, 200), (1600, 60)]:
        t0 = time.time()
        mu, sd = EF(n, reps, rng)
        R = math.ceil(4 * math.log2(n)); D = n - 2 - R
        q = 1 - 1.0 / (n - 2)
        ser = q ** -2 * (-math.log(1 - q) - q - q * q / 2)
        Hn2 = sum(1.0 / j for j in range(1, n - 1))
        B = 1 + Hn2 / 2 + ((n - 1) * (n - 2) / (2 * D * D)) * ser + 1.0 / n if D > 0 else float('nan')
        print(f"{n:6d} {reps:7d} {mu:9.4f} {sd:7.4f} {math.log(n)+0.25+GAMMA/2:12.4f} "
              f"{B:15.4f} {mu-math.log(n):11.4f}   ({time.time()-t0:.0f}s)", flush=True)
