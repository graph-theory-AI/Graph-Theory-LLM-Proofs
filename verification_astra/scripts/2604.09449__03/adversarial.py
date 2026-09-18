"""Adversarial (hill-climbing) search for labellings that violate Lemma 4 / Proposition 6,
plus a numerical confirmation of Lemma 3 (Hobby-Rice, d=2) on step functions."""
import itertools, math, random
import numpy as np

def B(d): return math.ceil(math.log2(d)) + 2 if d >= 2 else 2
def l1(v): return float(np.abs(v).sum())

def objective(H, r, d, mode):
    P = list(itertools.permutations(range(r)))
    sums = np.array([H[np.arange(r), p].sum(axis=0) for p in P])
    if mode == "prop6":
        mean = H.reshape(-1, d).sum(axis=0)/r
        best = min(l1(s-mean) for s in sums)
        return best/(3*d*B(d))
    else:  # lemma4 : worst pair
        worst = 0.0
        n = len(sums)
        for i in range(n):
            for j in range(i, n):
                mid = (sums[i]+sums[j])/2
                bm = min(l1(s-mid) for s in sums)
                worst = max(worst, bm)
        return worst/(3*d)

def normalize(H):
    nrm = np.abs(H).sum(axis=-1, keepdims=True)
    nrm[nrm == 0] = 1
    return H/nrm

def search(r, d, mode, iters=400, restarts=6, seed=0):
    rng = np.random.default_rng(seed)
    best_overall = 0.0
    for _ in range(restarts):
        H = normalize(rng.standard_normal((r, r, d)))
        cur = objective(H, r, d, mode)
        T = 0.6
        for it in range(iters):
            H2 = H.copy()
            i, j = rng.integers(r), rng.integers(r)
            H2[i, j] = H2[i, j] + T*rng.standard_normal(d)
            H2 = normalize(H2)
            v = objective(H2, r, d, mode)
            if v >= cur:
                H, cur = H2, v
            T *= 0.995
        best_overall = max(best_overall, cur)
    return best_overall

def hobby_rice_d2(r=6, trials=30, seed=1, grid=400):
    """Numerically confirm Lemma 3 for d=2 step functions: a 2-cut halving set exists."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(trials):
        v = rng.standard_normal((r, 2))
        tot = v.sum(axis=0)
        def integ(t):   # integral of f over [0,t]
            k = int(math.floor(t)); k = min(k, r); frac = t-k
            s = v[:k].sum(axis=0)
            if k < r: s = s + frac*v[k]
            return s
        # A = [0,t1] u [t2,r]  or  A = [t1,t2]
        best = 1e9
        ts = np.linspace(0, r, grid+1)
        for a in ts:
            for b in ts:
                if b < a: continue
                A1 = integ(b)-integ(a)                     # [a,b]
                A2 = tot - A1                              # complement (2 cuts)
                for A in (A1, A2):
                    best = min(best, float(np.abs(A-tot/2).max()))
        worst = max(worst, best)
    return worst

if __name__ == "__main__":
    # Parameters below are the ones actually run for the report (each block kept under ~2 min).
    print("== adversarial hill-climb: max ratio attained/bound (>1 would refute) ==", flush=True)
    for r, d, mode, it, rs, sd in [(4,1,"lemma4",200,3,7),(4,2,"lemma4",200,3,7),
                                   (5,1,"prop6",300,3,7),(5,2,"prop6",300,3,7),
                                   (6,1,"prop6",200,2,11),(6,3,"prop6",200,2,11)]:
        print(f"  r={r} d={d} {mode}: best ratio {search(r,d,mode,it,rs,sd):.3f}", flush=True)
    print("== Lemma 3 (Hobby-Rice) d=2, r=6: worst residual over random step fns (grid 200) ==", flush=True)
    print(f"  max residual = {hobby_rice_d2(trials=8, grid=200):.5f}  (grid resolution is 0.03)", flush=True)
