"""Checks of Section 5 of attacks_retry/2106.03261__00/output.md:
  (10)  M_c M_c^T = qI + J - blockdiag(J_q)  and sigma_2(M_c) <= sqrt(q)
  (13)  sup_{S,T} | e_G(S,T)/n^{3/2} - e_D(S,T)/n^2 |  (Definition 1.3 discrepancy)
"""
import numpy as np, random, sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from construction2 import build, PV, PE

def spectral(q=11):
    idx = {(x,y): x*q+y for x in range(q) for y in range(q)}
    for c in (0,1):
        M = np.zeros((q*q, q*q))
        for x in range(q):
            for y in range(q):
                for xp in range(q):
                    yp = (x*xp + c - y) % q
                    M[idx[(x,y)], idx[(xp,yp)]] = 1
        MMt = M @ M.T
        J = np.ones((q*q,q*q))
        BD = np.zeros((q*q,q*q))
        for x in range(q):
            BD[x*q:(x+1)*q, x*q:(x+1)*q] = 1
        claim = q*np.eye(q*q) + J - BD
        sv = np.sort(np.linalg.svd(M, compute_uv=False))[::-1]
        print(f"  c={c}: (10) holds exactly: {np.allclose(MMt, claim)};"
              f" row sums all q: {np.allclose(M.sum(1), q)};"
              f" sigma_1={sv[0]:.4f} (q={q}), sigma_2={sv[1]:.4f} (sqrt q={q**0.5:.4f})")

def discrepancy(r=2, trials=4000, seed=0):
    D = build(r, twisted=True)
    V, adjc = D['V'], D['adjc']
    q = D['q']
    verts = [z for v in PV for z in V[v]]
    n, m = len(verts), len(V['a0'])
    cls = {z: v for v in PV for z in V[v]}
    adj = D['adj']
    rnd = random.Random(seed)
    worst = 0.0
    # adversarial-ish choices: whole classes, unions of classes, random sets
    def disc(S, T):
        Sset, Tset = set(S), set(T)
        eg = sum(1 for z in Sset for w in adj[z] if w in Tset)
        cntS = {v: 0 for v in PV}; cntT = {v: 0 for v in PV}
        for z in Sset: cntS[cls[z]] += 1
        for z in Tset: cntT[cls[z]] += 1
        ed = sum(cntS[u]*cntT[v] + cntS[v]*cntT[u] for (u,v) in PE)
        return abs(eg/n**1.5 - ed/n**2)
    tests = []
    tests.append((verts, verts))
    for v in PV:
        tests.append((V[v], verts))
    for (u,v) in PE:
        tests.append((V[u], V[v]))
    for _ in range(trials):
        p1, p2 = rnd.random(), rnd.random()
        S = [z for z in verts if rnd.random() < p1]
        T = [z for z in verts if rnd.random() < p2]
        tests.append((S, T))
    for S, T in tests:
        worst = max(worst, disc(S, T))
    bound = 3*q**0.5/(q-1) + 1/q
    print(f"  q={q} n={n}: max observed discrepancy over {len(tests)} (S,T) pairs = {worst:.6f}")
    print(f"  writeup's proved bound (13) = 3 sqrt(q)/(q-1) + 1/q = {bound:.6f}")
    print(f"  hom(P,D)/n^10 >= (m/n)^10 = {(m/n)**10:.3e}; hom(P,G)/n^2.5 = 0")

if __name__ == '__main__':
    print("Spectral identity (10) and singular values:")
    spectral(11)
    spectral(13)
    print("Discrepancy (Definition 1.3, eq (1.1)):")
    discrepancy(1, trials=2000)
    discrepancy(2, trials=60)
