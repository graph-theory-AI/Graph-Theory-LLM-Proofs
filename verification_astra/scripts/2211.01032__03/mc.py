"""Monte Carlo for E[F_n], E[F^hit], E[F^avoid] in the signed-rotation model of K_n,
and the equivalence with the writeup's 'A canonical + V_u iid uniform on H_d' model."""
import sys, os, math, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V, faces_components

GAMMA = 0.5772156649015329


def sample_true(n, rng):
    """the model as stated: uniform rotation + iid fair signature"""
    P = np.argsort(rng.random((n, n - 1)), axis=1)
    tw = np.zeros((n, n), dtype=np.int64)
    iu = np.triu_indices(n, 1)
    tw[iu] = rng.integers(0, 2, size=len(iu[0]))
    tw = tw + tw.T
    return build_A(n, tw), build_V(n, P)


def sample_H(n, rng):
    """the writeup's reduced model: A canonical, V_u iid uniform on H_d.
    V_u = random cyclic order + random side bits."""
    N = 2 * n * (n - 1)
    # canonical A: (u,v,s) <-> (v,u,s)
    A = np.empty(N, dtype=np.int64)
    u = np.repeat(np.arange(n), n - 1)
    slot = np.tile(np.arange(n - 1), n)
    v = slot + (slot >= u)
    tgt_slot = u - (u > v)
    for s in (0, 1):
        A[(u * (n - 1) + slot) * 2 + s] = (v * (n - 1) + tgt_slot) * 2 + s
    P = np.argsort(rng.random((n, n - 1)), axis=1)
    b = rng.integers(0, 2, size=(n, n - 1))            # side-relabelling bits
    V = np.empty(N, dtype=np.int64)
    base = (np.arange(n) * (n - 1))[:, None]
    bp = np.take_along_axis(b, P, axis=1)
    cur = (base + P) * 2 + (1 ^ bp)
    nxt = (base + np.roll(P, -1, axis=1)) * 2 + np.roll(bp, -1, axis=1)
    V[cur.ravel()] = nxt.ravel()
    V[nxt.ravel()] = cur.ravel()
    return A, V


def run(n, reps, rng, sampler):
    Ftot = 0.0; Fhit = 0.0; F2 = 0.0
    lens = {}
    for _ in range(reps):
        A, V = sampler(n, rng)
        lab, f = faces_components(A, V)
        Ftot += f; F2 += f * f
        # faces meeting vertex 0: flags (0,*,*) occupy ids [0, 2(n-1))
        h = len(np.unique(lab[0:2 * (n - 1)]))
        Fhit += h
    return Ftot / reps, Fhit / reps, math.sqrt(max(F2 / reps - (Ftot / reps) ** 2, 0) / reps)


if __name__ == "__main__":
    rng = np.random.default_rng(12345)
    print("== equivalence check: stated model vs writeup's H-model ==")
    for n in (4, 5, 6, 8):
        reps = 200000 if n <= 6 else 100000
        a = run(n, reps, np.random.default_rng(1), sample_true)
        b = run(n, reps, np.random.default_rng(2), sample_H)
        print(f" n={n}: E[F] true={a[0]:.5f}+-{a[2]:.5f}   H-model={b[0]:.5f}+-{b[2]:.5f}"
              f"   |  E[F^hit] true={a[1]:.5f} H={b[1]:.5f}")

    print("\n== E[F_n] vs the claimed bound ln n + 1/4 + gamma/2 ==")
    print(f"{'n':>5} {'reps':>8} {'E[F]':>9} {'se':>7} {'E[Fhit]':>9} {'E[Favoid]':>10} "
          f"{'1+H(n-2)/2':>11} {'.5ln n-.75':>11} {'ln n+.25+g/2':>13}")
    for n, reps in [(5, 200000), (10, 100000), (20, 60000), (40, 30000),
                    (80, 12000), (160, 4000), (320, 1200), (640, 300)]:
        t0 = time.time()
        EF, EH, se = run(n, reps, rng, sample_true)
        Hn2 = sum(1.0 / j for j in range(1, n - 1))
        print(f"{n:5d} {reps:8d} {EF:9.4f} {se:7.4f} {EH:9.4f} {EF-EH:10.4f} "
              f"{1+Hn2/2:11.4f} {0.5*math.log(n)-0.75:11.4f} "
              f"{math.log(n)+0.25+GAMMA/2:13.4f}   [{time.time()-t0:.0f}s]")
