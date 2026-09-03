"""Exhaustive computation of the threshold Ramsey multiplicity m(P_k) for
small k, by iterating over ALL 2-colorings of K_{r(P_k)}.

m(P_4): r=5, 2^10 colorings.  m(P_5): r=6, 2^15 colorings.
Uses bitmask tricks: each unlabeled P_k copy -> edge bitmask; a copy is
monochromatic in coloring g (red edge set as bitmask) iff mask & g == mask
(all red) or mask & g == 0 (all blue).
"""
import itertools
from math import factorial


def edge_index(n):
    idx = {}
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            idx[(i, j)] = c
            c += 1
    return idx, c


def path_masks(n, k):
    idx, m = edge_index(n)
    masks = []
    for perm in itertools.permutations(range(n), k):
        if perm[0] > perm[-1]:
            continue
        mask = 0
        for a, b in zip(perm, perm[1:]):
            if a > b:
                a, b = b, a
            mask |= 1 << idx[(a, b)]
        masks.append(mask)
    return masks, m


def m_path(k):
    n = k + k // 2 - 1
    masks, m = path_masks(n, k)
    best = None
    best_g = None
    for g in range(1 << (m - 1)):  # fix one edge blue (color-swap symmetry)
        cnt = 0
        for mask in masks:
            x = mask & g
            if x == mask or x == 0:
                cnt += 1
                if best is not None and cnt >= best:
                    break
        if best is None or cnt < best:
            best, best_g = cnt, g
    return n, best, best_g, len(masks)


if __name__ == "__main__":
    for k in (4, 5):
        n, best, g, ncop = m_path(k)
        print(f"k={k}: r(P_k)={n}, #P_k copies in K_n={ncop}, "
              f"exhaustive m(P_k)={best} (red-edge bitmask of a minimizer: {g:b})")
