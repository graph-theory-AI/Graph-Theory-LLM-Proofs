"""Binned analysis of the saved G_k histograms against equation (11).

For a bin [k1,k2):   N_bin = observed total count of good avoiding faces,
                     B_bin = reps * C * sum_{k in bin} q^{k-2}/k.
A one-sided 99.9% Poisson upper confidence limit on N_bin is compared to B_bin.
(11) is violated in a bin iff the Poisson LOWER limit on N_bin exceeds B_bin.
"""
import sys, math
import numpy as np

def poisson_bounds(N, alpha=0.001):
    if N > 500:                      # normal approximation, plenty accurate here
        z = 3.09023
        return N - z * math.sqrt(N), N + z * math.sqrt(N)
    """one-sided (1-alpha) limits on the Poisson mean given count N,
    via the chi-square relation, using a normal-approx-free bisection on the cdf."""
    from math import lgamma, log, exp
    def cdf(mu, k):      # P(X <= k)
        if mu <= 0: return 1.0
        s = 0.0
        term = math.exp(-mu)
        s = term
        for i in range(1, k + 1):
            term *= mu / i
            s += term
        return s
    # upper limit: largest mu with P(X<=N) >= alpha
    lo, hi = 0.0, max(10.0, N + 10 * math.sqrt(N + 1) + 20)
    while cdf(hi, N) > alpha: hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        if cdf(mid, N) > alpha: lo = mid
        else: hi = mid
    up = lo
    # lower limit: smallest mu with P(X>=N) >= alpha  i.e. P(X<=N-1) <= 1-alpha
    if N == 0: return 0.0, up
    lo2, hi2 = 0.0, up
    for _ in range(200):
        mid = (lo2 + hi2) / 2
        if cdf(mid, N - 1) > 1 - alpha: lo2 = mid
        else: hi2 = mid
    return lo2, up

def analyse(n, seed, reps):
    Gk = np.load(f"Gk_n{n}_s{seed}.npy")
    R = math.ceil(4 * math.log2(n)); D = n - 2 - R
    q = 1 - 1.0 / (n - 2); C = (n - 1) * (n - 2) / (2.0 * D * D)
    bound_k = np.array([C * q ** (k - 2) / k if k >= 3 else 0.0 for k in range(len(Gk))])
    print(f"\n### n={n} reps={reps}  R={R} D={D} C={C:.4f}  "
          f"predicted slack (D/(n-2))^2 = {(D/(n-2))**2:.4f}")
    print(f"{'bin':>14} {'count':>9} {'bound*reps':>12} {'ratio':>8} "
          f"{'99.9% Poisson CI on count':>28} {'verdict':>10}")
    edges = [3, 5, 10, 20, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500, 700, 1000, len(Gk)]
    for a, b in zip(edges[:-1], edges[1:]):
        N = int(Gk[a:b].sum())
        B = reps * bound_k[a:b].sum()
        if B <= 0 and N == 0: continue
        lo, up = poisson_bounds(N)
        ratio = N / B if B > 0 else float('inf')
        verdict = "VIOLATED" if lo > B else "ok"
        print(f"  [{a:5d},{b:5d}) {N:9d} {B:12.2f} {ratio:8.4f} "
              f"[{lo:11.2f},{up:11.2f}] {verdict:>10}")
    # per-k worst with a Poisson lower limit
    worst = []
    for k in range(3, len(Gk)):
        N = int(Gk[k]); B = reps * bound_k[k]
        if N == 0 or B <= 0: continue
        lo, up = poisson_bounds(N)
        worst.append((N / B, k, N, B, lo))
    worst.sort(reverse=True)
    print("  worst individual k (ratio, count, bound*reps, 99.9% Poisson lower limit):")
    for ratio, k, N, B, lo in worst[:8]:
        print(f"     k={k:6d} cnt={N:6d} bound*reps={B:10.4f} ratio={ratio:8.3f} "
              f"lower={lo:9.4f} {'VIOLATED' if lo > B else 'ok (noise)'}")

if __name__ == "__main__":
    for (n, seed, reps) in eval(sys.argv[1]):
        analyse(n, seed, reps)
