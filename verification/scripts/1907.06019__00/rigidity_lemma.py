#!/usr/bin/env python3
"""Verify the rigidity lemma of the writeup for 1907.06019__00.

Lemma: for dim U = m >= 2k+2, k >= 1, the linear maps
f : Lambda^k U -> Lambda^{k+1} U satisfying
    x ^ f(y) = (-1)^k y ^ f(x)   for all x, y in Lambda^k U      (2)
are exactly f(x) = a ^ x for a in U (an m-dimensional space of maps).

We build the linear system for the unknown coefficients c_{J,L}
(f(e_L) = sum_J c_{J,L} e_J over (k+1)-sets J) imposed by (2) on all
basis pairs (x, y) = (e_I, e_L), compute its exact nullspace dimension
by rational Gaussian elimination, check the dimension equals m, and
check every map x -> e_a ^ x satisfies the system exactly (so the
nullspace *is* {a ^ . : a in U}).

Also probes the boundary m = 2k+1 (lemma hypothesis violated) to see
whether the conclusion survives there.
"""

from fractions import Fraction
from itertools import combinations


def wedge_sign(S, T):
    """Sign of e_S ^ e_T = sign * e_{S union T} for sorted tuples S, T.
    Returns 0 if they intersect."""
    if set(S) & set(T):
        return 0
    # count inversions: pairs (s, t) with s in S, t in T, s > t
    inv = sum(1 for s in S for t in T if s > t)
    return -1 if inv % 2 else 1


def rigidity_system(m, k):
    """Rows of the linear system in unknowns c_{J,L}."""
    ksets = list(combinations(range(m), k))
    k1sets = list(combinations(range(m), k + 1))
    unknown = {(J, L): idx for idx, (J, L) in
               enumerate((J, L) for J in k1sets for L in ksets)}
    nunk = len(unknown)
    sgn = (-1) ** k
    rows = []
    for I in ksets:
        for L in ksets:
            # e_I ^ f(e_L) - (-1)^k e_L ^ f(e_I) = 0, coefficientwise
            coeffs = {}  # (2k+1)-set M -> {unknown_idx: coeff}
            for J in k1sets:
                s = wedge_sign(I, J)
                if s:
                    M = tuple(sorted(I + J))
                    coeffs.setdefault(M, {})
                    d = coeffs[M]
                    u = unknown[(J, L)]
                    d[u] = d.get(u, 0) + s
                s = wedge_sign(L, J)
                if s:
                    M = tuple(sorted(L + J))
                    coeffs.setdefault(M, {})
                    d = coeffs[M]
                    u = unknown[(J, I)]
                    d[u] = d.get(u, 0) - sgn * s
            for M, d in coeffs.items():
                d = {u: c for u, c in d.items() if c}
                if d:
                    rows.append(d)
    return rows, nunk, ksets, k1sets, unknown


def rank_sparse(rows, ncols):
    """Exact rank of a sparse integer matrix by rational elimination."""
    pivots = {}  # col -> row (dict col->Fraction)
    rank = 0
    for row in rows:
        r = {c: Fraction(v) for c, v in row.items()}
        while r:
            c = min(r)
            if c in pivots:
                p = pivots[c]
                factor = r[c] / p[c]
                for cc, vv in p.items():
                    nv = r.get(cc, Fraction(0)) - factor * vv
                    if nv:
                        r[cc] = nv
                    else:
                        r.pop(cc, None)
            else:
                pivots[c] = r
                rank += 1
                break
    return rank


def check_star_maps_satisfy(m, k, rows, ksets, k1sets, unknown):
    """Check every f_a(x) = e_a ^ x satisfies all equations exactly."""
    for a in range(m):
        # c_{J,L} for f_a
        vec = {}
        for L in ksets:
            s = wedge_sign((a,), L)
            if s:
                J = tuple(sorted((a,) + L))
                vec[unknown[(J, L)]] = s
        for row in rows:
            tot = sum(coef * vec.get(u, 0) for u, coef in row.items())
            if tot != 0:
                return False
    return True


def main():
    cases = [(4, 1), (5, 1), (6, 1), (6, 2), (7, 2)]
    boundary = [(3, 1), (5, 2)]  # m = 2k+1: hypothesis fails
    for m, k in cases + boundary:
        rows, nunk, ksets, k1sets, unknown = rigidity_system(m, k)
        rk = rank_sparse(rows, nunk)
        null_dim = nunk - rk
        stars_ok = check_star_maps_satisfy(m, k, rows, ksets, k1sets, unknown)
        tag = "LEMMA CASE" if m >= 2 * k + 2 else "BOUNDARY (m=2k+1)"
        verdict = ("OK" if (null_dim == m and stars_ok) else
                   ("nullspace dim != m" if stars_ok else "star maps FAIL"))
        print(f"{tag}: m={m}, k={k}: unknowns={nunk}, rank={rk}, "
              f"nullspace dim={null_dim} (expect {m}), "
              f"star maps satisfy system: {stars_ok} -> {verdict}")


if __name__ == "__main__":
    main()
