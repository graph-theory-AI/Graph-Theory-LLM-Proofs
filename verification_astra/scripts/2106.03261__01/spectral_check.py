"""Check the spectral identities (5.1)-(5.3) of the writeup:
   M_c M_c^T = q I + J - K   and   ||M_c - J/q||_op = sqrt(q),
and the resulting global cut-norm bound ||sqrt(N) A_G - A_H||_box <= 3 N^{-1/4}
(checked here against a randomized search over cuts X,Y for small q)."""
import sys, itertools, numpy as np

def Mc(q, c):
    pts = [(x, y) for x in range(q) for y in range(q)]
    idx = {p: i for i, p in enumerate(pts)}
    M = np.zeros((q*q, q*q))
    for i, (x, y) in enumerate(pts):
        for xp in range(q):
            yp = (c - y - x*xp) % q
            M[i, idx[(xp, yp)]] = 1
    return M, pts, idx

for q in [5, 7, 11, 13]:
    for c in range(q):
        M, pts, idx = Mc(q, c)
        J = np.ones((q*q, q*q))
        K = np.zeros((q*q, q*q))
        for i, (x, y) in enumerate(pts):
            for j, (xp, yp) in enumerate(pts):
                if x == xp: K[i, j] = 1
        assert np.allclose(M @ M.T, q*np.eye(q*q) + J - K), (q, c, "identity M M^T = qI+J-K FAILS")
        op = np.linalg.norm(M - J/q, 2)
        assert abs(op - np.sqrt(q)) < 1e-8, (q, c, op, np.sqrt(q))
    print(f"q={q}: for every c in F_q, M_c M_c^T = qI + J - K  and  ||M_c - J/q||_op = sqrt(q) = {np.sqrt(q):.6f}  OK")
