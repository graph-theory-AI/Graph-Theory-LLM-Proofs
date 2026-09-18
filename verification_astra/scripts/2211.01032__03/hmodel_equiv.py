"""Check the writeup's model reduction (Section 1):

  (rotation uniform, iid fair edge signatures)   ==distribution of F==
  (A canonical: (u,v,s)<->(v,u,s);  V_u iid UNIFORM on H_d)

H_d is enumerated by brute force (no use of the writeup's parametrisation or of
its count |H_d| = 2^{d-1}(d-1)!).
"""
import sys, os, math, collections
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V
from exposure import perfect_matchings, one_cycle

def enumerate_H(d):
    pts = list(range(2 * d))
    J = tuple((2 * i, 2 * i + 1) for i in range(d))
    return [W for W in perfect_matchings(pts) if one_cycle(J, W, d)]

def nfaces(A, V):
    N = len(A); sigma = A[V]
    m = np.arange(N, dtype=np.int64); s = sigma.copy()
    for _ in range(int(np.ceil(np.log2(N))) + 1):
        m = np.minimum(m, m[s]); s = s[s]
    lab = np.minimum(m, m[A])
    return int(np.count_nonzero(lab == np.arange(N)))

def direct_dist(n, reps, rng):
    c = collections.Counter()
    iu = np.triu_indices(n, 1)
    for _ in range(reps):
        P = np.argsort(rng.random((n, n - 1)), axis=1)
        tw = np.zeros((n, n), dtype=np.int64)
        tw[iu] = rng.integers(0, 2, size=len(iu[0])); tw = tw + tw.T
        c[nfaces(build_A(n, tw), build_V(n, P))] += 1
    return c

def hmodel_dist(n, reps, rng, H):
    d = n - 1
    c = collections.Counter()
    ones = np.ones((n, n), dtype=np.int64)
    A = build_A(n, ones)                       # canonical: (u,v,s)<->(v,u,s)
    # sanity: A must be an involution pairing (u,v,s) with (v,u,s)
    assert np.array_equal(A[A], np.arange(len(A)))
    N = 2 * n * (n - 1)
    for _ in range(reps):
        V = np.empty(N, dtype=np.int64)
        for u in range(n):
            W = H[rng.integers(len(H))]
            for (p, r) in W:
                fp = (u * (n - 1) + p // 2) * 2 + (p % 2)
                fr = (u * (n - 1) + r // 2) * 2 + (r % 2)
                V[fp] = fr; V[fr] = fp
        c[nfaces(A, V)] += 1
    return c

if __name__ == "__main__":
    rng = np.random.default_rng(99)
    for n, reps in [(4, 200000), (5, 200000), (6, 120000)]:
        H = enumerate_H(n - 1)
        print(f"n={n}: |H_{n-1}| = {len(H)} (predicted {2**(n-2)*math.factorial(n-2)})")
        a = direct_dist(n, reps, rng)
        b = hmodel_dist(n, reps, rng, H)
        ks = sorted(set(a) | set(b))
        tv = 0.5 * sum(abs(a[k] / reps - b[k] / reps) for k in ks)
        ma = sum(k * a[k] for k in ks) / reps
        mb = sum(k * b[k] for k in ks) / reps
        print("   F:        " + " ".join(f"{k:>8d}" for k in ks))
        print("   direct:   " + " ".join(f"{a[k]/reps:8.5f}" for k in ks))
        print("   H-model:  " + " ".join(f"{b[k]/reps:8.5f}" for k in ks))
        print(f"   total variation = {tv:.5f}   E[F]: direct {ma:.5f} vs H-model {mb:.5f}"
              f"   (MC sd ~ {1/math.sqrt(reps):.5f})", flush=True)
