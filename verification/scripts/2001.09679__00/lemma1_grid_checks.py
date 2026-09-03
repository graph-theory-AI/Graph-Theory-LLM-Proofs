#!/usr/bin/env python3
"""Referee checks for Lemma 1 of the writeup for 2001.09679__00.

Lemma 1(1): edge-isoperimetry of the m x m grid:  |dQ(A)| >= c * mu(A) / m
            (writeup states it with side Theta(L); here side = m plays the
            role of 40L+1, so the claim is |dQ(A)| >= c*mu/side).
Lemma 1(2): with a port P = interval of ell vertices centred on a side, and
            perpendicular paths of length ell, the disagreement count obeys
            D(A) <= |dQ(A)| + mu(A)/ell.

We verify both EXHAUSTIVELY on small grids (all 2^(m*m) subsets for m<=4),
and on a large random + structured sample for m = 5, 6.
"""
import itertools
import random

random.seed(12345)


def grid_edges(m):
    E = []
    for x in range(m):
        for y in range(m):
            if x + 1 < m:
                E.append(((x, y), (x + 1, y)))
            if y + 1 < m:
                E.append(((x, y), (x, y + 1)))
    return E


def boundary(A, E):
    return sum(1 for (u, v) in E if (u in A) != (v in A))


def check_grid(m, exhaustive, n_samples=200000, ell=None):
    V = [(x, y) for x in range(m) for y in range(m)]
    E = grid_edges(m)
    M = m * m
    if ell is None:
        ell = max(1, m // 3)
    # port: interval of ell vertices centred on the bottom side (y = 0)
    x0 = (m - ell) // 2
    port = [(x0 + i, 0) for i in range(ell)]

    min_ratio1 = float("inf")   # min over A of |dQ(A)| * m / mu(A)
    worst1 = None
    max_viol2 = -float("inf")   # max over A of D(A) - (|dQ(A)| + mu/ell)
    worst2 = None

    def subsets():
        if exhaustive:
            for mask in range(1, 2 ** M - 1):
                yield {V[i] for i in range(M) if (mask >> i) & 1}
        else:
            # random subsets of many densities + structured ones
            for _ in range(n_samples):
                p = random.random()
                A = {v for v in V if random.random() < p}
                if 0 < len(A) < M:
                    yield A
            # rectangles and half planes
            for x1, x2 in itertools.combinations(range(m + 1), 2):
                for y1, y2 in itertools.combinations(range(m + 1), 2):
                    A = {(x, y) for (x, y) in V if x1 <= x < x2 and y1 <= y < y2}
                    if 0 < len(A) < M:
                        yield A

    for A in subsets():
        mu = min(len(A), M - len(A))
        b = boundary(A, E)
        r1 = b * m / mu
        if r1 < min_ratio1:
            min_ratio1, worst1 = r1, (len(A), b)
        # Lemma 1(2)
        state1 = len(A) >= M / 2
        D = sum(1 for v in port if (v in A) != state1)
        viol = D - (b + mu / ell)
        if viol > max_viol2:
            max_viol2, worst2 = viol, (len(A), b, D)

    tag = "exhaustive" if exhaustive else "sampled"
    print(f"m={m} ({tag}), M={M}, port length ell={ell}:")
    print(f"  Lemma 1(1): min |dQ(A)|*m/mu(A) = {min_ratio1:.4f}  (worst |A|,|dQ|={worst1})")
    print(f"  Lemma 1(2): max D - (|dQ| + mu/ell) = {max_viol2:.4f}  "
          f"({'OK (<=0)' if max_viol2 <= 1e-9 else 'VIOLATED'})  worst (|A|,|dQ|,D)={worst2}")
    return min_ratio1, max_viol2


if __name__ == "__main__":
    ok = True
    for m in (2, 3, 4):
        r1, v2 = check_grid(m, exhaustive=True)
        ok &= (r1 > 0.9) and (v2 <= 1e-9)
    for m in (5, 6):
        r1, v2 = check_grid(m, exhaustive=False)
        ok &= (r1 > 0.9) and (v2 <= 1e-9)
    print("\nOVERALL:", "PASS" if ok else "FAIL")
