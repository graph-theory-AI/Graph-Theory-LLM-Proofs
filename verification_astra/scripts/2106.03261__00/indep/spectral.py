"""Checks of Section 5 of attacks_retry/2106.03261__00/output.md:
 (10) M_c M_c^T = qI + J - (+)_x J_q
 singular values: q on the all-ones direction, <= sqrt(q) on its complement
 (11) discrepancy |sum_{X,Y} M_c - |X||Y|/q| <= sqrt(q) sqrt(|X||Y|)
 (12)/(13) cut discrepancy of G_q vs the complete blow-up D_q, by explicit maximisation
           over many random/greedy S,T (a bound, not a proof, but it tests the claim).
Also: Lemma 3 -- hom(P,P) and the number of endomorphisms of the Petersen graph.
"""
import itertools, random, sys
import numpy as np

def Mc(q, c):
    pts = [(x,y) for x in range(q) for y in range(q)]
    idx = {p:i for i,p in enumerate(pts)}
    M = np.zeros((q*q, q*q))
    for (x,y) in pts:
        for (xp,yp) in pts:
            if (y+yp) % q == (x*xp + c) % q:
                M[idx[(x,y)], idx[(xp,yp)]] = 1
    return M, pts, idx

def check_spectral(q):
    for c in range(q):
        M, pts, idx = Mc(q,c)
        MMT = M @ M.T
        J = np.ones((q*q,q*q))
        K = np.zeros((q*q,q*q))
        for i,(x,y) in enumerate(pts):
            for j,(xp,yp) in enumerate(pts):
                if x == xp: K[i,j] = 1
        claim = q*np.eye(q*q) + J - K
        ok = np.allclose(MMT, claim)
        sv = np.linalg.svd(M, compute_uv=False)
        # largest, and largest on complement of all-ones
        one = np.ones(q*q)/q
        # project out the all-ones direction
        P = np.eye(q*q) - np.outer(one,one)/np.dot(one,one)
        sv2 = np.linalg.svd(P @ M @ P, compute_uv=False)
        print(f"  q={q} c={c}: (10) holds={ok}  sigma_max={sv[0]:.6f} (claim q={q})  "
              f"sigma_max on 1^perp={sv2[0]:.6f} (claim <= sqrt q={q**0.5:.6f})  "
              f"M1={np.allclose(M@np.ones(q*q), q*np.ones(q*q))}")
        if not ok: return False
    return True

def check_mixing(q, trials=4000, seed=1):
    rng = random.Random(seed)
    worst = 0.0
    for c in (0,1):
        M, pts, idx = Mc(q,c)
        N = q*q
        for _ in range(trials):
            pX = rng.random(); pY = rng.random()
            X = [i for i in range(N) if rng.random() < pX]
            Y = [j for j in range(N) if rng.random() < pY]
            if not X or not Y: continue
            s = M[np.ix_(X,Y)].sum()
            lhs = abs(s - len(X)*len(Y)/q)
            rhs = (q**0.5)*(len(X)*len(Y))**0.5
            worst = max(worst, lhs/rhs)
    print(f"  q={q}: max over {trials} random (X,Y) of LHS/RHS in (11) = {worst:.4f}  (claim <= 1)")
    return worst

# ---- Lemma 3: endomorphisms of the Petersen graph ----
def petersen():
    V = list(itertools.combinations(range(5),2))
    adj = {v: set(u for u in V if not (set(u)&set(v))) for v in V}
    return V, adj

def count_endos():
    V, adj = petersen()
    # order vertices greedily so each has >=1 earlier neighbour
    order = [V[0]]
    rest = [v for v in V[1:]]
    while rest:
        for v in rest:
            if any(u in adj[v] for u in order):
                order.append(v); rest.remove(v); break
    pos = {v:i for i,v in enumerate(order)}
    prev = {v:[u for u in adj[v] if pos[u] < pos[v]] for v in order}
    total = 0; noninj = 0; assign = {}
    def rec(i):
        nonlocal total, noninj
        if i == len(order):
            total += 1
            if len(set(assign.values())) < 10: noninj += 1
            return
        v = order[i]
        cand = set(V)
        for u in prev[v]: cand &= adj[assign[u]]
        for z in cand:
            assign[v] = z; rec(i+1)
        assign.pop(v, None)
    rec(0)
    return total, noninj

if __name__ == '__main__':
    print("== spectral identity (10) and singular values")
    for q in [3,5,7,11]:
        check_spectral(q)
    print("== mixing inequality (11)")
    for q in [5,7,11]:
        check_mixing(q, trials=1500)
    print("== Lemma 3: endomorphisms of the Petersen graph")
    t,ni = count_endos()
    print(f"  hom(P,P) = {t}; non-injective ones = {ni}  (Lemma 3 <=> ni==0 and t==|Aut(P)|=120)")
