"""Direct test of the cut-discrepancy claim (13) of attacks_retry/2106.03261__00/output.md:
   max_{S,T} | e_{G_q}(S,T)/n^{3/2} - e_{D_q}(S,T)/n^2 |  <=  3 sqrt(q)/(q-1) + 1/q,
where D_q is the complete balanced blow-up of the Petersen graph on the same classes and
e(.,.) counts ORDERED adjacent pairs.  We maximise over S,T by alternating greedy ascent
from many random starts (a lower bound on the max), plus the exact SDP-free spectral bound.
"""
import random, sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/',1)[0])
from build import build, PV, PE, structure

def matrices(q, twisted=True):
    D = build(q, twisted=twisted)
    verts = [z for v in PV for z in D['V'][v]]
    idx = {z:i for i,z in enumerate(verts)}
    cls = {}
    for v in PV:
        for z in D['V'][v]: cls[z] = v
    n = len(verts)
    A = np.zeros((n,n))
    for z, nbrs in D['adj'].items():
        for w in nbrs: A[idx[z], idx[w]] = 1
    # complete blow-up of P on the same classes
    B = np.zeros((n,n))
    ci = np.array([PV.index(cls[z]) for z in verts])
    padj = np.zeros((10,10))
    for (u,v) in PE:
        padj[PV.index(u), PV.index(v)] = 1; padj[PV.index(v), PV.index(u)] = 1
    B = padj[np.ix_(ci,ci)]
    return A, B, n, D

def greedy_max(K, restarts=60, seed=0):
    """maximise |1_S^T K 1_T| over S,T by alternating optimisation"""
    rng = np.random.default_rng(seed)
    n = K.shape[0]; best = 0.0
    for _ in range(restarts):
        s = (rng.random(n) < 0.5).astype(float)
        for _it in range(60):
            t = (K.T @ s > 0).astype(float)
            s2 = (K @ t > 0).astype(float)
            if np.array_equal(s2, s): break
            s = s2
        best = max(best, abs(s @ K @ t))
        # also the negative direction
        s = (rng.random(n) < 0.5).astype(float)
        for _it in range(60):
            t = (K.T @ s < 0).astype(float)
            s2 = (K @ t < 0).astype(float)
            if np.array_equal(s2, s): break
            s = s2
        best = max(best, abs(s @ K @ t))
    return best

if __name__ == '__main__':
    for q in [int(a) for a in sys.argv[1:]] or [11,31,41]:
        A,B,n,D = matrices(q, twisted=True)
        K = A/ n**1.5 - B / n**2
        got = greedy_max(K, restarts=80, seed=q)
        claim = 3*q**0.5/(q-1) + 1.0/q
        # exact spectral upper bound on the cut norm of K (Grothendieck-free):
        specbd = np.linalg.svd(K, compute_uv=False)[0] * n
        print(f"q={q} n={n}: greedy max |e_G(S,T)/n^1.5 - e_D(S,T)/n^2| = {got:.6f}; "
              f"writeup bound (13) = {claim:.6f}; crude spectral upper bd = {specbd:.6f}; "
              f"ok={got <= claim + 1e-12}")
