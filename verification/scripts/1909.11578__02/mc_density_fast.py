"""Vectorized unconditioned Monte Carlo estimate of mu_{1/3}(F_n).

F_n = { S subset Z_n : longest cyclic run of ones > longest cyclic run of zeros }.
Confirms the density is polynomially small (~n^{-1.7} asymptotically for k=3),
far above any stretched-exponential k^{-c n^delta} scale.
"""
import numpy as np, math

def max_cyclic_run_rows(M):
    """M: boolean (B, n). Returns per-row length of longest CYCLIC run of True,
    via iterated AND with the cyclic shift (run length = number of iterations
    until the row dies; all-True rows -> n)."""
    B, n = M.shape
    cur = M.copy()
    r = np.zeros(B, dtype=np.int32)
    it = 0
    alive = cur.any(axis=1)
    while alive.any():
        it += 1
        if it > n:  # all-True rows never die
            r[alive] = n
            break
        r[alive] = it
        cur = cur & np.roll(cur, 1, axis=1)
        alive = cur.any(axis=1)
    return r

if __name__ == "__main__":
    rng = np.random.default_rng(7)
    p = 1.0 / 3.0
    for n, trials in ((50, 1_000_000), (100, 1_000_000), (200, 1_000_000), (400, 1_000_000)):
        hits = 0
        done = 0
        B = 100_000
        while done < trials:
            b = min(B, trials - done)
            X = rng.random((b, n)) < p          # True = element in S (prob 1/3)
            ones = max_cyclic_run_rows(X)
            zeros = max_cyclic_run_rows(~X)
            hits += int(np.sum(ones > zeros))
            done += b
        mu = hits / trials
        se = math.sqrt(max(mu * (1 - mu), 1e-15) / trials)
        print(f"n={n:4d}: mu_hat={mu:.4e} +- {se:.1e} (hits={hits}/{trials}); "
              f"n^-1.71={n**-1.71:.2e}; exp(-sqrt(n))={math.exp(-math.sqrt(n)):.2e}")
