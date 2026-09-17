"""Exhaustive check of Lemma 2.1 of attacks_retry/2106.03261__01/output.md.

Claim: in PG(2,q) with the nondegenerate symmetric form
   <(z,x,y),(z',x',y')> = z y' + y z' + x x',
if ten pairwise distinct projective points A..J realise the 14 Petersen edges
other than ij (table (2.1)), then <I,J> = 0 automatically.

We enumerate ALL ordered triples (A,B,C) of distinct projective points, close up
D,E,F,G,H,I,J by the perp construction, and check the conclusion.
"""
import sys, itertools
import numpy as np

def points(q):
    pts = []
    for z in range(q):
        for x in range(q):
            for y in range(q):
                v = (z, x, y)
                if v == (0, 0, 0):
                    continue
                # canonical representative: first nonzero coordinate == 1
                for c in v:
                    if c % q:
                        inv = pow(int(c), q - 2, q)
                        break
                w = tuple((inv * t) % q for t in v)
                if w == v:
                    pts.append(v)
    return np.array(sorted(set(pts)), dtype=np.int64)

def canon(V, q):
    """Canonicalise rows of V (n,3); rows must be nonzero."""
    V = V % q
    out = V.copy()
    lead = np.zeros(len(V), dtype=np.int64)
    found = np.zeros(len(V), dtype=bool)
    for k in range(3):
        m = (~found) & (V[:, k] % q != 0)
        lead[m] = V[m, k]
        found |= m
    inv = np.array([pow(int(t), q - 2, q) if t % q else 0 for t in lead], dtype=np.int64)
    out = (V * inv[:, None]) % q
    return out, found

M = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=np.int64)

def bil(U, V, q):
    return (U @ M @ V.T) % q if U.ndim == 2 and V.ndim == 2 else None

def bil_rows(U, V, q):
    return np.einsum('ij,jk,ik->i', U, M, V) % q

def perp(U, V, q):
    """point spanning span(U,V)^perp, rowwise; zero row iff U,V dependent."""
    MU = (U @ M.T) % q
    MV = (V @ M.T) % q
    return np.cross(MU, MV) % q

def run(q):
    P = points(q)
    npts = len(P)
    tot_admissible = 0
    tot_violations = 0
    tot_nondistinct_nonorth = 0
    for ia in range(npts):
        A = P[ia]
        for ib in range(npts):
            if ib == ia:
                continue
            B = P[ib]
            C = P[np.arange(npts) != ia]
            C = C[np.any(C != B, axis=1)]
            m = len(C)
            Ar = np.repeat(A[None, :], m, axis=0)
            Br = np.repeat(B[None, :], m, axis=0)
            D = perp(Ar, Br, q)
            E = perp(Ar, C, q)
            F = perp(Br, C, q)
            ok = (D.any(axis=1) & E.any(axis=1) & F.any(axis=1))
            G = perp(C, D, q)
            H = perp(Br, E, q)
            I = perp(Ar, F, q)
            ok &= (G.any(axis=1) & H.any(axis=1) & I.any(axis=1))
            J = perp(G, H, q)
            ok &= J.any(axis=1)
            if not ok.any():
                continue
            pts = [Ar, Br, C, D, E, F, G, H, I, J]
            cpts = []
            for X in pts:
                Xc, f = canon(X, q)
                cpts.append(Xc)
            distinct = np.ones(m, dtype=bool)
            for s, t in itertools.combinations(range(10), 2):
                distinct &= np.any(cpts[s] != cpts[t], axis=1)
            good = ok & distinct
            ip = bil_rows(I, J, q)
            tot_admissible += int(good.sum())
            tot_violations += int(((ip != 0) & good).sum())
            tot_nondistinct_nonorth += int(((ip != 0) & ok & (~distinct)).sum())
    return npts, tot_admissible, tot_violations, tot_nondistinct_nonorth

for q in [5, 7, 11, 13]:
    npts, adm, viol, nd = run(q)
    print(f"q={q:3d}  proj.points={npts:5d}  admissible(10 distinct pts, all closures defined)={adm:9d}"
          f"  VIOLATIONS(<I,J> != 0)={viol}   (non-distinct configs with <I,J>!=0: {nd})")
