"""Decisive Monte-Carlo test of the writeup's equation (11).

(11)  Pr(a fixed flag a in S lies in a GOOD AVOIDING face of length k)
          <=  q^{k-2} / (2 D^2),        q = 1-1/(n-2),  D = n-2-R,  R = ceil(4 log2 n)

Rooting at flags (|S| = 2(n-1)(n-2)) this is equivalent to

      E G_k  <=  C(n) * q^{k-2} / k,    C(n) = (n-1)(n-2)/(2 D^2)

where G_k = # good avoiding faces of length k.  We estimate E G_k from full
embeddings of the ACTUAL model (uniform rotation + iid fair signature), with
Poisson/CLT upper confidence limits, and also test the cumulative tails
  T_K = sum_{k>=K} G_k   vs   C(n) * sum_{k>=K} q^{k-2}/k.
"""
import sys, os, math, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V

def sample(n, rng):
    P = np.argsort(rng.random((n, n - 1)), axis=1)
    tw = np.zeros((n, n), dtype=np.int64)
    iu = np.triu_indices(n, 1)
    tw[iu] = rng.integers(0, 2, size=len(iu[0]))
    tw = tw + tw.T
    return build_A(n, tw), build_V(n, P)

def labels(A, V):
    N = len(A)
    sigma = A[V]
    m = np.arange(N, dtype=np.int64)
    s = sigma.copy()
    for _ in range(int(np.ceil(np.log2(max(N, 2)))) + 1):
        m = np.minimum(m, m[s]); s = s[s]
    lab = np.minimum(m, m[A])
    for _ in range(3):
        lab = np.minimum(lab, lab[A]); lab = np.minimum(lab, lab[V])
    return lab

def run(n, reps, seed=12345, R=None, progress=0):
    d = n - 1
    if R is None:
        R = math.ceil(4 * math.log2(n))
    D = n - 2 - R
    q = 1 - 1.0 / (n - 2)
    C = (n - 1) * (n - 2) / (2.0 * D * D)
    rng = np.random.default_rng(seed)
    vert = np.arange(2 * n * (n - 1)) // (2 * (n - 1))
    maxlen = n * (n - 1)
    Gk = np.zeros(maxlen + 2)          # counts of good avoiding faces, by length
    Gk2 = np.zeros(maxlen + 2)         # per-rep second moment, for the CLT on tails
    Fh = Fa = Ftot = Bbad = 0.0
    Fh2 = 0.0
    tails_per_rep = []                 # per-rep sum_{k>=K} G_k for a few K
    t0 = time.time()
    for it in range(reps):
        A, V = sample(n, rng)
        lab = labels(A, V)
        uniq, inv = np.unique(lab, return_inverse=True)
        nf = len(uniq)
        Ftot += nf
        cnt = np.bincount(inv * n + vert, minlength=nf * n).reshape(nf, n)
        loads = cnt // 2
        flen = loads.sum(axis=1)
        avoid = loads[:, 0] == 0
        maxload = loads.max(axis=1)
        good = avoid & (maxload <= R)
        nav = int(avoid.sum())
        Fa += nav; Fh += nf - nav; Fh2 += (nf - nav) ** 2
        Bbad += int((avoid & (maxload > R)).sum())
        gl = flen[good]
        if gl.size:
            h = np.bincount(gl, minlength=maxlen + 2)
            Gk += h
            Gk2 += h.astype(float) ** 2
        if progress and (it + 1) % progress == 0:
            print(f"    n={n} {it+1}/{reps}  {time.time()-t0:.0f}s", flush=True)
    return dict(n=n, reps=reps, R=R, D=D, q=q, C=C,
                Gk=Gk, Gk2=Gk2, EF=Ftot/reps, EFhit=Fh/reps, EFhit2=Fh2/reps,
                EFavoid=Fa/reps, EB=Bbad/reps, secs=time.time()-t0)

def report(r):
    n, reps, q, C, D, R = r['n'], r['reps'], r['q'], r['C'], r['D'], r['R']
    Gk, Gk2 = r['Gk'], r['Gk2']
    bound = np.array([C * q ** (k - 2) / k if k >= 3 else np.inf
                      for k in range(len(Gk))])
    obs = Gk / reps
    sd = np.sqrt(np.maximum(Gk2 / reps - obs ** 2, 0) / reps)
    print(f"\n=== n={n}  reps={reps}  R={R} D={D} C={C:.4f}  ({r['secs']:.0f}s) ===")
    Hn2 = sum(1.0 / j for j in range(1, n - 1))
    ser = sum(q ** (k - 2) / k for k in range(3, 2000000))
    b12 = C * ser + 1.0 / n
    print(f"  E[F]       = {r['EF']:.4f}")
    print(f"  E[F^hit]   = {r['EFhit']:.4f}  vs (2) 1+H_(n-2)/2 = {1+Hn2/2:.4f}  "
          f"{'OK' if r['EFhit'] <= 1+Hn2/2 else '*** VIOLATED ***'}")
    print(f"  E[F^avoid] = {r['EFavoid']:.4f}  vs (12) = {b12:.4f}  "
          f"{'OK' if r['EFavoid'] <= b12 else '*** VIOLATED ***'}")
    print(f"  E[B] bad avoiding = {r['EB']:.6f}  vs (10) 1/n = {1.0/n:.6f}")
    # per-k
    ks = [k for k in range(3, len(Gk)) if Gk[k] > 0]
    print(f"  good-avoiding face lengths observed: k in [{min(ks)},{max(ks)}], "
          f"total count {int(Gk.sum())}")
    rows = []
    for k in ks:
        # Poisson-ish 99.9% upper limit on the count, then compare to bound
        cnt = Gk[k]
        lo = obs[k] - 3.29 * sd[k]     # 99.9% one-sided lower limit on E G_k
        rows.append((obs[k] / bound[k], k, cnt, obs[k], sd[k], bound[k], lo))
    rows.sort(reverse=True)
    print("   worst-10 k by ratio obs/bound  (k, count, obs, sd, bound, ratio, 99.9%-LCL):")
    for ratio, k, cnt, o, s, b, lo in rows[:10]:
        flag = "  <-- LCL EXCEEDS BOUND" if lo > b else ""
        print(f"     k={k:6d} cnt={int(cnt):7d} obs={o:.3e} sd={s:.1e} bound={b:.3e} "
              f"ratio={ratio:7.3f} LCL={lo:.3e}{flag}")
    # cumulative tails
    print("   cumulative tails  sum_{k>=K} :")
    cum_obs = np.cumsum(obs[::-1])[::-1]
    cum_b = np.cumsum(np.where(np.isfinite(bound), bound, 0.0)[::-1])[::-1]
    for K in [3, 5, 10, 20, 30, 50, 75, 100, 150, 200, 300, 500]:
        if K < len(Gk):
            print(f"     K={K:4d}: obs={cum_obs[K]:.5f}  bound={cum_b[K]:.5f}  "
                  f"ratio={cum_obs[K]/max(cum_b[K],1e-300):8.4f}")
    return rows

if __name__ == "__main__":
    n = int(sys.argv[1]); reps = int(sys.argv[2])
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 12345
    r = run(n, reps, seed, progress=max(reps // 10, 1))
    rows = report(r)
    np.save(f"Gk_n{n}_s{seed}.npy", r['Gk'])
    np.save(f"Gk2_n{n}_s{seed}.npy", r['Gk2'])
    json.dump({k: float(v) for k, v in r.items() if k not in ('Gk', 'Gk2')},
              open(f"summary_n{n}_s{seed}.json", "w"), indent=1)
