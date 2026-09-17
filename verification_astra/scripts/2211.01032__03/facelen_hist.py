"""Full histogram of AVOIDING-face lengths vs the writeup's bound (11)/(12).

bound:  E G_k  <=  (n-1)(n-2) q^{k-2} / (2 k D^2),   q = 1-1/(n-2), D = n-2-R,
        R = ceil(4 log2 n),  plus E[bad] <= 1/n.
"""
import sys, os, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V
from trace_test import sample, labels

def hist(n, reps, rng):
    R = math.ceil(4 * math.log2(n)); D = n - 2 - R; q = 1 - 1.0 / (n - 2)
    vert = np.arange(2 * n * (n - 1)) // (2 * (n - 1))
    maxlen = (n - 1) * (n - 2) + 1
    Hgood = np.zeros(maxlen + 1); Hbad = np.zeros(maxlen + 1)
    Fh = 0.0; Ftot = 0.0; sanity = True
    for _ in range(reps):
        A, V = sample(n, rng)
        lab = labels(A, V)
        uniq, inv = np.unique(lab, return_inverse=True)
        nf = len(uniq); Ftot += nf
        cnt = np.bincount(inv * n + vert, minlength=nf * n).reshape(nf, n)
        flen = cnt.sum(axis=1) // 2
        if flen.sum() != n * (n - 1):
            sanity = False
        loads = cnt // 2
        avoid = loads[:, 0] == 0
        Fh += nf - int(avoid.sum())
        mx = loads.max(axis=1)
        g = avoid & (mx <= R); b = avoid & (mx > R)
        np.add.at(Hgood, flen[g], 1); np.add.at(Hbad, flen[b], 1)
    return R, D, q, Hgood / reps, Hbad / reps, Ftot / reps, Fh / reps, sanity


if __name__ == "__main__":
    for n, reps in [(30, 20000), (50, 8000)]:
        t0 = time.time()
        rng = np.random.default_rng(20260917 + n)
        R, D, q, Hg, Hb, EF, EFh, sane = hist(n, reps, rng)
        ks = np.arange(len(Hg))
        with np.errstate(divide='ignore', invalid='ignore'):
            bd = (n - 1) * (n - 2) * q ** (ks - 2) / (2 * np.maximum(ks, 1) * D ** 2)
        print(f"\n=== n={n} reps={reps} R={R} D={D} q={q:.5f}  ({time.time()-t0:.0f}s) "
              f"length-sum sanity={sane} ===")
        print(f"  E[F]={EF:.4f}  E[F^hit]={EFh:.4f}  E[F^avoid]={Hg.sum()+Hb.sum():.4f} "
              f" (good {Hg.sum():.4f}, bad {Hb.sum():.5f}; bound (10) = {1/n:.4f})")
        print(f"  {'k-range':>14} {'obs E G_k':>12} {'bound (11)':>12} {'ratio':>8}")
        edges = [3, 10, 30, 60, 100, 150, 200, 300, 400, 600, 900, 1400, len(Hg)]
        for a, b in zip(edges[:-1], edges[1:]):
            o = Hg[a:b].sum(); bb = bd[a:b].sum()
            if o == 0 and bb < 1e-12:
                continue
            print(f"  [{a:5d},{b:5d}) {o:12.5f} {bb:12.5f} {o/bb if bb>0 else float('inf'):8.2f}"
                  f"{'   <<< VIOLATION' if o > bb*1.0 and o > 3/reps else ''}")
        print(f"  TOTAL good     {Hg.sum():12.5f} {bd[3:].sum():12.5f} {Hg.sum()/bd[3:].sum():8.2f}")
        # exact per-k worst offenders
        w = [(int(k), Hg[k], bd[k]) for k in range(3, len(Hg)) if Hg[k] > bd[k] and Hg[k] > 2.5/reps]
        print(f"  per-k violations (obs>bound, >=3 events): {len(w)} of "
              f"{sum(1 for k in range(3,len(Hg)) if Hg[k]>0)} occupied k; "
              f"worst ratios: {sorted([(round(x[1]/x[2],1), x[0]) for x in w], reverse=True)[:6]}")
