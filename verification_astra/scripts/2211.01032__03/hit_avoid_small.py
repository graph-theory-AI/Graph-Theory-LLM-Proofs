"""Exact E[F^hit] / E[F^avoid] for small n vs the writeup's bound (2): 1 + H_{n-2}/2."""
import sys, os, itertools
from fractions import Fraction
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V

def labels(A, V):
    N = len(A); sigma = A[V]
    m = np.arange(N, dtype=np.int64); s = sigma.copy()
    for _ in range(int(np.ceil(np.log2(N))) + 1):
        m = np.minimum(m, m[s]); s = s[s]
    lab = np.minimum(m, m[A])
    for _ in range(3):
        lab = np.minimum(lab, lab[A]); lab = np.minimum(lab, lab[V])
    return lab

for n in (3, 4):
    slots = list(range(n - 1))
    rots = [[0] + list(p) for p in itertools.permutations(slots[1:])]
    iu = [(u, v) for u in range(n) for v in range(u + 1, n)]
    vert = np.arange(2 * n * (n - 1)) // (2 * (n - 1))
    hit = 0; av = 0; cnt = 0
    for Ps in itertools.product(rots, repeat=n):
        P = np.array(Ps, dtype=np.int64); V = build_V(n, P)
        for bits in itertools.product((0, 1), repeat=len(iu)):
            tw = np.zeros((n, n), dtype=np.int64)
            for (u, v), b in zip(iu, bits):
                tw[u, v] = tw[v, u] = b
            A = build_A(n, tw)
            lab = labels(A, V)
            uniq, inv = np.unique(lab, return_inverse=True)
            nf = len(uniq)
            c = np.bincount(inv * n + vert, minlength=nf * n).reshape(nf, n)
            a = int((c[:, 0] == 0).sum())
            av += a; hit += nf - a; cnt += 1
    H = sum(Fraction(1, j) for j in range(1, n - 1))
    print(f"n={n}: E[F^hit]={Fraction(hit,cnt)}={hit/cnt:.6f}  bound (2) 1+H_(n-2)/2 = "
          f"{1+H/2} = {float(1+H/2):.6f}   {'OK' if Fraction(hit,cnt) <= 1+H/2 else 'VIOLATED'}"
          f"   E[F^avoid]={Fraction(av,cnt)}={av/cnt:.6f}")
