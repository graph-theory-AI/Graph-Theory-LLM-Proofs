#!/usr/bin/env python3
"""Further checks for 1907.06019__00.

A. Step-3 expansion identity: for random f and random x, y in Lambda^k U,
     (e0^x + f(x)) ^ (e0^y + f(y))
       = e0 ^ ( x^f(y) + (-1)^{k+1} y^f(x) )  +  f(x)^f(y)
   (exact integer arithmetic; U = span(e1..e_{n-1})).

B. Boundary counterexample (Section 4 of the writeup): for n = 2r,
   W = Lambda^r H with H a hyperplane has dim = C(n-1, r-1), is
   self-annihilating, and is annihilated by NO nonzero vector v
   (hence is not v ^ Lambda^{r-1} V). Checked for r = 2, 3, 4.

C. End-to-end for n = 7, r = 3 (k = 2, m = 6): every solution f of the
   symmetry condition (2) has the form a ^ . (from rigidity_lemma.py);
   here we take random a, set W = {e0^x + a^x}, and verify by brute
   force that W is self-annihilating, dim W = C(6,2) = 15, and
   W = (e0 + a) ^ Lambda^2 V.

D. Step-1 echelon check on a scrambled star: take W = v ^ Lambda^{r-1}V
   in a random integer basis, row-reduce in decreasing binary-weight
   order, and confirm the leading supports form an intersecting family
   (indeed a star) of size C(n-1, r-1).
"""

import random
from fractions import Fraction
from itertools import combinations

random.seed(20260902)


def wedge_sign(S, T):
    if set(S) & set(T):
        return 0
    inv = sum(1 for s in S for t in T if s > t)
    return -1 if inv % 2 else 1


def wedge(u, v):
    """Wedge of dicts {sorted tuple: coeff}."""
    out = {}
    for S, a in u.items():
        for T, b in v.items():
            s = wedge_sign(S, T)
            if s:
                M = tuple(sorted(S + T))
                out[M] = out.get(M, 0) + s * a * b
    return {M: c for M, c in out.items() if c}


def scal(c, u):
    return {S: c * a for S, a in u.items()}


def add(*forms):
    out = {}
    for f in forms:
        for S, a in f.items():
            out[S] = out.get(S, 0) + a
    return {S: a for S, a in out.items() if a}


def rand_form(n, deg, lo=-4, hi=4, ground=None):
    ground = ground if ground is not None else range(n)
    return {S: random.randint(lo, hi) for S in combinations(ground, deg)}


# ---------- A. step-3 expansion identity ----------
def check_expansion(n, r, trials=20):
    k = r - 1
    U = range(1, n)
    for _ in range(trials):
        # random f as a table on basis monomials of Lambda^k U
        ftab = {L: rand_form(n, k + 1, ground=U)
                for L in combinations(U, k)}

        def f(x):
            out = {}
            for L, c in x.items():
                for J, d in ftab[L].items():
                    out[J] = out.get(J, 0) + c * d
            return {J: c for J, c in out.items() if c}

        x = rand_form(n, k, ground=U)
        y = rand_form(n, k, ground=U)
        e0 = {(0,): 1}
        lhs = wedge(add(wedge(e0, x), f(x)), add(wedge(e0, y), f(y)))
        rhs = add(
            wedge(e0, add(wedge(x, f(y)),
                          scal((-1) ** (k + 1), wedge(y, f(x))))),
            wedge(f(x), f(y)))
        if lhs != rhs:
            return False
    return True


# ---------- exact rank / span helpers ----------
def rref_rows(vectors, keyorder):
    """Exact RREF of a list of dict-vectors; keys ordered by keyorder
    (a list of keys, earliest = pivot preference). Returns list of
    (pivot_key, dict) rows."""
    pos = {kk: i for i, kk in enumerate(keyorder)}
    pivots = []  # (pivot_key, row)
    for v in vectors:
        r = {kk: Fraction(c) for kk, c in v.items() if c}
        for pk, prow in pivots:
            if pk in r:
                factor = r[pk] / prow[pk]
                for cc, vv in prow.items():
                    nv = r.get(cc, Fraction(0)) - factor * vv
                    if nv:
                        r[cc] = nv
                    else:
                        r.pop(cc, None)
        if r:
            pk = min(r, key=lambda kk: pos[kk])
            pivots.append((pk, r))
    return pivots


def span_dim(vectors):
    keys = sorted({kk for v in vectors for kk in v})
    return len(rref_rows(vectors, keys))


def same_span(vs1, vs2):
    return (span_dim(vs1) == span_dim(vs2) == span_dim(vs1 + vs2))


# ---------- B. boundary counterexample ----------
def check_boundary(r):
    n = 2 * r
    H = range(1, n)  # hyperplane e1..e_{n-1}
    basis = [{S: 1} for S in combinations(H, r)]
    from math import comb
    dim_ok = len(basis) == comb(n - 1, r - 1)
    sa_ok = all(not wedge(basis[i], basis[j])
                for i in range(len(basis)) for j in range(len(basis)))
    # v ^ w = 0 for all w in basis: linear system in v-coeffs a_0..a_{n-1}
    rows = []
    for w in basis:
        coeffs = {}
        for i in range(n):
            for S, c in wedge({(i,): 1}, w).items():
                coeffs.setdefault(S, [0] * n)[i] = c
        rows.extend({j: col[j] for j in range(n) if col[j]}
                    for col in coeffs.values())
    ann_dim = n - len(rref_rows(rows, list(range(n))))
    return dim_ok, sa_ok, ann_dim


# ---------- C. end-to-end star reconstruction ----------
def check_end_to_end(n, r):
    k = r - 1
    U = list(range(1, n))
    a = {(i,): random.randint(-3, 3) for i in U}
    a = {S: c for S, c in a.items() if c}
    e0 = {(0,): 1}
    Wbasis = [add(wedge(e0, {L: 1}), wedge(a, {L: 1}))
              for L in combinations(U, k)]
    from math import comb
    dim_ok = span_dim(Wbasis) == comb(n - 1, r - 1)
    sa_ok = all(not wedge(u, w) for u in Wbasis for w in Wbasis)
    v = add(e0, a)
    star = [wedge(v, {Z: 1}) for Z in combinations(range(n), k)]
    return dim_ok, sa_ok, same_span(Wbasis, star)


# ---------- D. echelon leading supports of a scrambled star ----------
def check_echelon(n, r):
    from math import comb
    v = add({(0,): 1}, {(i,): random.randint(-3, 3) for i in range(1, n)})
    star = [wedge(v, {Z: 1}) for Z in combinations(range(1, n), r - 1)]
    d = span_dim(star)
    # random invertible-ish integer recombination
    mixed = []
    for _ in range(len(star)):
        mixed.append(add(*[scal(random.randint(-3, 3), w) for w in star]))
    if span_dim(mixed) != d:
        mixed = star  # fall back (unlucky singular mix)
    weight = lambda S: sum(2 ** i for i in S)
    keyorder = sorted(combinations(range(n), r), key=weight, reverse=True)
    piv = rref_rows(mixed, keyorder)
    leads = [pk for pk, _ in piv]
    inter_ok = all(set(A) & set(B) for A in leads for B in leads)
    common = set.intersection(*(set(A) for A in leads)) if leads else set()
    return len(leads) == comb(n - 1, r - 1), inter_ok, sorted(common)


def main():
    from math import comb
    print("A. Step-3 expansion identity (random exact tests):")
    for (n, r) in [(5, 2), (7, 3), (9, 4)]:
        print(f"   n={n}, r={r}: identity holds on 20 random trials:",
              check_expansion(n, r))

    print("B. Boundary n=2r counterexample W = Lambda^r H:")
    for r in (2, 3, 4):
        dim_ok, sa_ok, ann_dim = check_boundary(r)
        print(f"   r={r}, n={2*r}: dim W = C(n-1,r-1): {dim_ok}, "
              f"self-annihilating: {sa_ok}, "
              f"dim of annihilating vectors = {ann_dim} (expect 0, "
              f"so NOT a star): {'OK' if ann_dim == 0 else 'FAIL'}")

    print("C. End-to-end graph form (n=7, r=3): W = {e0^x + a^x}:")
    dim_ok, sa_ok, eq_ok = check_end_to_end(7, 3)
    print(f"   dim W = C(6,2) = 15: {dim_ok}, self-annihilating: {sa_ok}, "
          f"W == (e0+a)^Lambda^2 V: {eq_ok}")

    print("D. Leading supports of a scrambled star (echelon check):")
    for (n, r) in [(7, 3), (9, 4)]:
        size_ok, inter_ok, common = check_echelon(n, r)
        print(f"   n={n}, r={r}: |leads| = C(n-1,r-1): {size_ok}, "
              f"intersecting: {inter_ok}, common element(s): {common}")


if __name__ == "__main__":
    main()
