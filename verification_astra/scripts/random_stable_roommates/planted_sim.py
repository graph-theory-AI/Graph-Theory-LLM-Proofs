"""Simulate the writeup's planted distribution Q and test its structural claims.

Q: fix M = {(2i,2i+1)}; thresholds x ~ density prop. to f(x)=prod_{pairs not in M}(1-x_v x_w)
   on [0,1]^n; off-matching score pairs (U_vw,U_wv) iid uniform on the unit square minus
   [0,x_v) x [0,x_w).

Sampling of x: rejection from mu_n (x_v = S E_v / T, S ~ chi_n, E_v iid Exp(1)) with
acceptance W(x)/e^{9/4}, where log W = S^2/2 + sum_{v<w, not in M} log(1-x_v x_w).
This is exactly the writeup's (4)+(5).

Tested claims:
 (a) E[# directed k-cycles of F] = 1/k        (writeup eq. (18) with j=1)
 (b) E[(C_K)_j] = lambda_K^j                  (writeup eq. (18))
 (c) E[2^{-C_K}] ~ e^{-lambda_K/2}            (writeup eq. (21))
 (d) Q(B_K) small                             (writeup eq. (22))
 (e) m_n = E_mu[W] -> sqrt(e)                 (writeup eq. (6))
"""
import sys, math
import numpy as np

def sample_x(n, rng, max_tries=20000):
    """rejection sampler for the planted threshold law"""
    iu = np.triu_indices(n, 1)
    # mask of pairs in M (matching = (0,1),(2,3),...)
    inM = (iu[1] == iu[0] + 1) & (iu[0] % 2 == 0)
    notM = ~inM
    tries = 0
    accW = []
    while True:
        tries += 1
        S = math.sqrt(rng.chisquare(n))
        E = rng.exponential(size=n)
        x = S * E / E.sum()
        if x.max() >= 1.0:
            accW.append(0.0); continue
        P = np.outer(x, x)[iu][notM]
        logW = 0.5 * S * S + np.log1p(-P).sum()
        W = math.exp(logW)
        accW.append(W)
        if rng.random() < W / math.exp(9 / 4):
            return x, S, tries, accW
        if tries > max_tries:
            raise RuntimeError("rejection failed")

def sample_scores(n, x, rng):
    """U[v,w] = v's score for w; conditional law given M stable."""
    U = rng.random((n, n))
    # resample violating off-matching pairs: U[v,w]<x[v] and U[w,v]<x[w]
    part = np.arange(n) ^ 1
    for _ in range(200):
        bad = (U < x[:, None]) & (U.T < x[None, :])
        np.fill_diagonal(bad, False)
        bad[np.arange(n), part] = False
        bad = np.triu(bad, 1)
        idx = np.argwhere(bad)
        if idx.size == 0:
            break
        U[idx[:, 0], idx[:, 1]] = rng.random(len(idx))
        U[idx[:, 1], idx[:, 0]] = rng.random(len(idx))
    return U

def build_F(n, x, U):
    part = np.arange(n) ^ 1
    cand = U < x[:, None]          # cand[w,v] : w prefers v to M(w)
    mask = cand.T                  # mask[v,w] : w is a candidate for v
    np.fill_diagonal(mask, False)
    mask[np.arange(n), part] = False
    Um = np.where(mask, U, np.inf)
    f = Um.argmin(axis=1)
    has = np.isfinite(Um.min(axis=1))
    F = part[f]
    return f, F, has

def cycles_of(F, has, n):
    colour = np.zeros(n, dtype=np.int8)
    out = []
    for s in range(n):
        if colour[s]:
            continue
        path, pos = [], {}
        v = s
        while colour[v] == 0 and has[v]:
            colour[v] = 1; pos[v] = len(path); path.append(v)
            v = int(F[v])
        if has[path[-1] if path else s] and colour[v] == 1 and v in pos:
            c = path[pos[v]:]
            if len(c) >= 2:
                out.append(c)
        for u in path:
            colour[u] = 2
    return out

def run(n, trials, Kmax, seed=1):
    rng = np.random.default_rng(seed)
    part = np.arange(n) ^ 1
    cyc_count = np.zeros(Kmax + 1)
    CK_hist = {K: [] for K in range(2, Kmax + 1)}
    badpartner = 0; badblock = 0
    Ws = []
    for t in range(trials):
        x, S, tries, accW = sample_x(n, rng)
        Ws.extend(accW)
        U = sample_scores(n, x, rng)
        f, F, has = build_F(n, x, U)
        cyc = cycles_of(F, has, n)
        for c in cyc:
            if len(c) <= Kmax:
                cyc_count[len(c)] += 1
        for K in range(2, Kmax + 1):
            CK_hist[K].append(sum(1 for c in cyc if 2 <= len(c) <= K))
        # goodness of the full <=Kmax collection
        C = [v for c in cyc if len(c) <= Kmax for v in c]
        Cs = set(C)
        if any(part[v] in Cs for v in C):
            badpartner += 1
        else:
            uf = U[np.arange(n), f]
            Ca = np.array(C)
            if len(Ca) > 1:
                sub = U[np.ix_(Ca, Ca)] < uf[Ca][:, None]
                np.fill_diagonal(sub, False)
                if (sub & sub.T).any():
                    badblock += 1
    print(f"n={n} trials={trials}")
    print(f"  mean W over mu_n proposals (should -> sqrt(e)=1.64872): {np.mean(Ws):.4f}  "
          f"(n proposals={len(Ws)})")
    print("  k :  E[#k-cycles]   1/k     ratio")
    for k in range(2, min(Kmax, 12) + 1):
        e = cyc_count[k] / trials
        print(f"  {k:2d}: {e:10.4f}  {1/k:8.4f}  {e*k:7.3f}")
    print("  K : E[2^{-C_K}]   e^{-lam_K/2}   ratio    E[C_K]   lam_K")
    for K in range(2, Kmax + 1):
        if K not in (2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, Kmax):
            continue
        lam = sum(1.0 / k for k in range(2, K + 1))
        v = np.mean([2.0 ** (-c) for c in CK_hist[K]])
        print(f"  {K:3d}: {v:10.5f}  {math.exp(-lam/2):11.5f}  {v/math.exp(-lam/2):7.3f}  "
              f"{np.mean(CK_hist[K]):8.4f} {lam:7.4f}")
    print(f"  goodness failures out of {trials}: partner-collision {badpartner}, "
          f"blocking {badblock}   (K<={Kmax})")

if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
        seed=int(sys.argv[4]) if len(sys.argv) > 4 else 1)
