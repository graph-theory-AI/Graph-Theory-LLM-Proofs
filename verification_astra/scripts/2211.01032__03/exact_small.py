"""Exact enumeration of E[F_n] for n=3,4 (and the H-model equivalence check)."""
import sys, os, itertools
from fractions import Fraction
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V, faces_components, is_orientable


def exact_EF(n):
    slots = list(range(n - 1))
    # cyclic orders at a vertex: fix slot 0 first -> (n-2)! representatives
    rots = [ [0] + list(p) for p in itertools.permutations(slots[1:]) ]
    iu = [(u, v) for u in range(n) for v in range(u + 1, n)]
    tot = Fraction(0); cnt = 0
    tot_no = Fraction(0); cnt_no = 0
    hist = {}
    for Ps in itertools.product(rots, repeat=n):
        P = np.array(Ps, dtype=np.int64)
        V = build_V(n, P)
        for bits in itertools.product((0, 1), repeat=len(iu)):
            tw = np.zeros((n, n), dtype=np.int64)
            for (u, v), b in zip(iu, bits):
                tw[u, v] = tw[v, u] = b
            A = build_A(n, tw)
            _, f = faces_components(A, V)
            tot += f; cnt += 1
            hist[f] = hist.get(f, 0) + 1
            if not is_orientable(n, tw):
                tot_no += f; cnt_no += 1
    return Fraction(tot, cnt), Fraction(tot_no, cnt_no), hist, cnt


for n in (3, 4, 5):
    if n == 5:
        break
    EF, EFno, hist, cnt = exact_EF(n)
    print(f"n={n}: {cnt} embeddings, E[F]={EF} = {float(EF):.6f}; "
          f"E[F | non-orientable]={EFno} = {float(EFno):.6f}; hist={sorted(hist.items())}")
