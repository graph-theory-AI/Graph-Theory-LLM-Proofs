"""Direct tests of the load-bearing inequalities of the writeup:
 (2)  E[F^hit]  <= 1 + H_{n-2}/2
 (5)  Pr(T > t) <= q^t,  q = 1-1/(n-2)
 (9)/(10) Pr(start flag in a BAD avoiding face) <= (n-1) 2^{-R};  E[B] <= 1/n
 (11) Pr(start flag in a GOOD avoiding face of length k) <= q^{k-2}/(2 D^2)
 (12) E[F^avoid] <= (n-1)(n-2)/(2D^2) * sum_{k>=3} q^{k-2}/k + 1/n
"""
import sys, os, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V

GAMMA = 0.5772156649015329


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
    # canonicalise once more (lab is already a component min after the merge?)
    for _ in range(3):
        lab = np.minimum(lab, lab[A]); lab = np.minimum(lab, lab[V])
    return lab


def analyse(n, reps, rng, R=None):
    d = n - 1
    if R is None:
        R = math.ceil(4 * math.log2(n))
    D = n - 2 - R
    q = 1 - 1.0 / (n - 2)
    vert = np.arange(2 * n * (n - 1)) // (2 * (n - 1))
    Fh = 0.0; Fa = 0.0; Ftot = 0.0; Bbad = 0.0
    Gk = {}
    Tsurv = np.zeros(4 * n + 1)
    ntr = 0
    for _ in range(reps):
        A, V = sample(n, rng)
        lab = labels(A, V)
        uniq, inv = np.unique(lab, return_inverse=True)
        nf = len(uniq)
        Ftot += nf
        # per-face: flags at each vertex
        cnt = np.bincount(inv * n + vert, minlength=nf * n).reshape(nf, n)
        flen = cnt.sum(axis=1) // 2
        loads = cnt // 2
        avoid = loads[:, 0] == 0
        maxload = loads.max(axis=1)
        good = avoid & (maxload <= R)
        bad = avoid & (maxload > R)
        Fa += int(avoid.sum()); Fh += nf - int(avoid.sum())
        Bbad += int(bad.sum())
        for k, g in zip(flen[good], good[good]):
            Gk[int(k)] = Gk.get(int(k), 0) + 1
        # survival of a few random traces
        S = np.nonzero(vert[A] != 0)[0]
        S = S[vert[S] != 0]
        for a0 in rng.choice(S, size=6, replace=False):
            b0 = A[a0]; cur = int(a0); t = 0
            while True:
                z = V[cur]; t += 1
                if z == b0:
                    break
                cur = int(A[z])
                if vert[cur] == 0:
                    break
            ntr += 1
            Tsurv[:min(t, len(Tsurv) - 1)] += 1   # T > 0..t-1
    return dict(n=n, reps=reps, R=R, D=D, q=q,
                EF=Ftot / reps, EFhit=Fh / reps, EFavoid=Fa / reps,
                EB=Bbad / reps, Gk={k: v / reps for k, v in sorted(Gk.items())},
                Tsurv=Tsurv / max(ntr, 1), ntr=ntr)


if __name__ == "__main__":
    rng = np.random.default_rng(777)
    for n, reps in [(12, 4000), (25, 2000), (50, 800)]:
        t0 = time.time()
        r = analyse(n, reps, rng)
        n_, q, D, R = r['n'], r['q'], r['D'], r['R']
        Hn2 = sum(1.0 / j for j in range(1, n - 1))
        bound12 = ((n - 1) * (n - 2) / (2 * D ** 2)) * sum(q ** (k - 2) / k for k in range(3, 200000)) + 1.0 / n
        print(f"\n=== n={n} reps={reps}  R={R} D={D} ({time.time()-t0:.0f}s) ===")
        print(f"  E[F]        = {r['EF']:.4f}    (claimed bound ln n + 1/4 + g/2 = {math.log(n)+0.25+GAMMA/2:.4f})")
        print(f"  E[F^hit]    = {r['EFhit']:.4f}    bound (2) 1+H_(n-2)/2 = {1+Hn2/2:.4f}   "
              f"{'OK' if r['EFhit'] <= 1+Hn2/2 else '***VIOLATED***'}")
        print(f"  E[F^avoid]  = {r['EFavoid']:.4f}    bound (12) = {bound12:.4f}   "
              f"{'OK' if r['EFavoid'] <= bound12 else '***VIOLATED***'}")
        print(f"  E[B] (bad avoiding faces) = {r['EB']:.5f}   bound (10) = {1.0/n:.5f}")
        # (11) per-k check, expressed as E G_k <= (n-1)(n-2) q^{k-2} / (2 k D^2)
        worst = None
        for k, v in r['Gk'].items():
            b = (n - 1) * (n - 2) * q ** (k - 2) / (2 * k * D ** 2)
            ratio = v / b
            if worst is None or ratio > worst[1]:
                worst = (k, ratio, v, b)
        print(f"  worst k for E G_k vs bound (11): k={worst[0]} observed={worst[2]:.5f} "
              f"bound={worst[3]:.5f} ratio={worst[1]:.3f}")
        # (5)
        bad5 = [(t, r['Tsurv'][t], q ** t) for t in range(0, min(3 * n, len(r['Tsurv'])))
                if r['Tsurv'][t] > q ** t + 3 * math.sqrt(max(q**t,1e-9) / max(r['ntr'],1))]
        print(f"  (5) Pr(T>t)<=q^t : {'OK' if not bad5 else 'violated at t='+str([b[0] for b in bad5[:5]])}"
              f"   e.g. t={n}: obs={r['Tsurv'][n]:.4f} vs q^n={q**n:.4f}")
