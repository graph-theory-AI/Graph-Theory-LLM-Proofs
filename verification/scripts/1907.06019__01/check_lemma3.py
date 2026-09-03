#!/usr/bin/env python3
"""Check Lemma 3 (rigidity): if A: Wedge^p H -> Wedge^{p+1} H and
B: Wedge^q H -> Wedge^{q+1} H satisfy A(x)^y = (-1)^p x^B(y) for all x,y,
and p+q+2 <= m = dim H, then A = B = L_h for some h in H.

We build the linear system in the entries of (A,B) whose solutions are exactly
the pairs satisfying the identity on basis elements (equivalent, by bilinearity,
to the identity for all x,y), compute its nullspace dimension, and verify:
  (a) every (L_h, L_h) lies in the solution space (sign sanity check), and
  (b) the nullspace dimension equals m (so solutions = {(L_h,L_h)} exactly).
Also probes m = p+q+1 to show the hypothesis p+q+2<=m is sharp (nullity > m).
"""
import itertools
import numpy as np

def inversions(A, B):
    return sum(1 for a in A for b in B if a > b)

def wedge_monomial(K, L):
    """e_K ^ e_L -> (sign, K union L) or None."""
    if set(K) & set(L):
        return None
    sign = (-1) ** inversions(K, L)
    return sign, tuple(sorted(set(K) | set(L)))

def basis(m, k):
    return list(itertools.combinations(range(m), k))

def build_system(m, p, q):
    Bp = basis(m, p); Bp1 = basis(m, p + 1)
    Bq = basis(m, q); Bq1 = basis(m, q + 1)
    Btop = basis(m, p + q + 1)
    idx_top = {T: i for i, T in enumerate(Btop)}
    nA = len(Bp1) * len(Bp)   # A[K1, I]
    nB = len(Bq1) * len(Bq)   # B[L1, J]
    rows = []
    for iI, I in enumerate(Bp):
        for iJ, J in enumerate(Bq):
            row_block = np.zeros((len(Btop), nA + nB))
            # A(e_I) ^ e_J = sum_K1 A[K1,I] e_K1 ^ e_J
            for iK1, K1 in enumerate(Bp1):
                w = wedge_monomial(K1, J)
                if w:
                    sg, T = w
                    row_block[idx_top[T], iK1 * len(Bp) + iI] += sg
            # -(-1)^p e_I ^ B(e_J)
            for iL1, L1 in enumerate(Bq1):
                w = wedge_monomial(I, L1)
                if w:
                    sg, T = w
                    row_block[idx_top[T], nA + iL1 * len(Bq) + iJ] -= ((-1) ** p) * sg
            rows.append(row_block)
    return np.vstack(rows), Bp, Bp1, Bq, Bq1

def Lh_vector(m, p, q, h):
    """Vector encoding (A,B) = (L_h, L_h) in the unknown ordering above."""
    Bp = basis(m, p); Bp1 = basis(m, p + 1)
    Bq = basis(m, q); Bq1 = basis(m, q + 1)
    v = np.zeros(len(Bp1) * len(Bp) + len(Bq1) * len(Bq))
    for iI, I in enumerate(Bp):
        for a in range(m):
            w = wedge_monomial((a,), I)
            if w:
                sg, T = w
                v[Bp1.index(T) * len(Bp) + iI] += h[a] * sg
    off = len(Bp1) * len(Bp)
    for iJ, J in enumerate(Bq):
        for a in range(m):
            w = wedge_monomial((a,), J)
            if w:
                sg, T = w
                v[off + Bq1.index(T) * len(Bq) + iJ] += h[a] * sg
    return v

def check(m, p, q):
    M, *_ = build_system(m, p, q)
    rank = np.linalg.matrix_rank(M)
    nullity = M.shape[1] - rank
    # sanity: (L_h,L_h) in kernel for random h
    rng = np.random.default_rng(0)
    resid = max(np.abs(M @ Lh_vector(m, p, q, rng.standard_normal(m))).max()
                for _ in range(3))
    status = "OK" if (nullity == m and resid < 1e-9) else "MISMATCH"
    print(f"m={m} p={p} q={q} (p+q+2<={m}? {p+q+2<=m}): nullity={nullity} "
          f"(expected {m} iff hypothesis holds), Lh residual={resid:.1e} -> "
          f"{status if p+q+2<=m else f'nullity={nullity} (sharpness probe)'}")
    return (nullity == m and resid < 1e-9) if p + q + 2 <= m else True

if __name__ == "__main__":
    ok = True
    for (m, p, q) in [(4,1,1), (5,1,1), (5,1,2), (6,1,2), (6,2,2), (7,2,2), (6,1,3), (7,2,3), (5,0,2), (5,0,0)]:
        ok &= check(m, p, q)
    # sharpness probes: p+q+2 = m+1
    for (m, p, q) in [(3,1,1), (4,1,2), (5,2,2)]:
        check(m, p, q)
    print("ALL OK" if ok else "FAILURES FOUND")
