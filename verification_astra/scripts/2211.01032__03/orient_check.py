"""Convention check: with an all-positive (orientable) signature the flag model
must reproduce the classical orientable face count F = #cycles(pi o iota)."""
import sys, os, itertools
from fractions import Fraction
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import build_A, build_V, faces_components, orientable_faces, is_orientable

for n in (4, 5):
    slots = list(range(n - 1))
    rots = [[0] + list(p) for p in itertools.permutations(slots[1:])]
    tot = 0; cnt = 0; bad = 0
    zero = np.zeros((n, n), dtype=np.int64)     # all +1 signature
    for Ps in itertools.product(rots, repeat=n):
        P = np.array(Ps, dtype=np.int64)
        # the all-orientable signature in this code's convention:
        for tw in (zero, np.ones((n, n), dtype=np.int64) - np.eye(n, dtype=np.int64)):
            if is_orientable(n, tw):
                break
        A = build_A(n, tw); V = build_V(n, P)
        _, f = faces_components(A, V)
        g = orientable_faces(n, P)
        if f != g: bad += 1
        tot += f; cnt += 1
    print(f"n={n}: {cnt} rotations, mismatches vs permutation model = {bad}, "
          f"E[F | orientable signature] = {Fraction(tot,cnt)} = {tot/cnt:.6f}")
