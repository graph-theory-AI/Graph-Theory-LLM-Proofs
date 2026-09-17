"""Geometry helpers shared by the orthogonality-graph checks."""
import numpy as np
from itertools import combinations
from math import gcd, pi, sqrt

np.random.seed(11)

# ---------- line sets ----------
def primitive_lines(B):
    """lines spanned by nonzero integer vectors with entries in [-B, B], one rep per line."""
    seen = {}
    for x in range(-B, B + 1):
        for y in range(-B, B + 1):
            for z in range(-B, B + 1):
                if (x, y, z) == (0, 0, 0):
                    continue
                g = gcd(gcd(abs(x), abs(y)), abs(z))
                v = (x // g, y // g, z // g)
                w = tuple(-c for c in v)
                key = max(v, w)
                seen[key] = np.array(key, dtype=float)
    return list(seen.values())


def peres_directions():
    """Peres' 33 directions (a Kochen-Specker set)."""
    s = sqrt(2.0)
    base = []
    base += [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for perm in [(0, 1, 1), (1, 0, 1), (1, 1, 0)]:
        for sg in [1, -1]:
            v = list(perm)
            idx = [i for i in range(3) if v[i] == 1]
            v[idx[1]] = sg
            base.append(tuple(v))
    for a in [1, -1]:
        for b in [1, -1]:
            base.append((1, a, b))
    for perm in [(s, 1, 1), (1, s, 1), (1, 1, s)]:
        for sa in [1, -1]:
            for sb in [1, -1]:
                v = list(perm)
                j = [i for i in range(3) if v[i] == 1]
                v[j[0]] *= sa
                v[j[1]] *= sb
                base.append(tuple(v))
    # dedupe up to sign
    out = []
    for v in base:
        a = np.array(v, dtype=float)
        a = a / np.linalg.norm(a)
        if not any(abs(abs(a @ b) - 1) < 1e-9 for b in out):
            out.append(a)
    return out


def ortho_graph(vecs, tol=1e-9):
    n = len(vecs)
    U = np.array([v / np.linalg.norm(v) for v in vecs])
    edges = [(i, j) for i, j in combinations(range(n), 2) if abs(U[i] @ U[j]) < tol]
    return U, edges


# ---------- (A) projection colouring ----------
def projection_check(U, edges, trials=200):
    """returns best lambda over random generic z"""
    n = len(U)
    best = 0.0
    for _ in range(trials):
        z = np.random.randn(3)
        z /= np.linalg.norm(z)
        d = U @ z
        if np.min(np.abs(d)) < 1e-6:
            continue
        Us = U * np.sign(d)[:, None]          # u_L . z > 0
        V = Us - (Us @ z)[:, None] * z        # project onto z^perp
        if np.min(np.linalg.norm(V, axis=1)) < 1e-9:
            continue
        # angles in the plane z^perp
        e1 = np.cross(z, np.array([1.0, 0.0, 0.0]))
        if np.linalg.norm(e1) < 1e-6:
            e1 = np.cross(z, np.array([0.0, 1.0, 0.0]))
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(z, e1)
        ang = np.arctan2(V @ e2, V @ e1)      # in (-pi, pi]
        col = (ang % (2 * pi)) * 4 / (2 * pi)  # circle of circumference 4
        lam = min(min(abs(col[i] - col[j]) % 4, 4 - (abs(col[i] - col[j]) % 4)) for i, j in edges)
        best = max(best, lam)
    return best


