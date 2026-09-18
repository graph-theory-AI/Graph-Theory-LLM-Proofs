"""
Second referee script for 2207.13651__00.
 H. Var(m_k) vs the claimed sub-gaussian proxy ~ n/d (writeup eq. 14/15) and FLP's 17n/(d+1).
 I. Var(Q_k(C)) vs the claimed proxy 8n/d from eq. (17)  (Var <= 2*sigma^2 = 8n/d).
 J. Conditional-independence claim of Section 4 (structural, exact check).
 K. Clique-union stress test of Q_k: per-clique contribution and its mean (=1).
 L. Empirical mgf check of (14): log E e^{lambda (m_k - Q_k)} <= C n lambda^2/d.
"""
import numpy as np, networkx as nx, itertools
from math import comb

rng = np.random.default_rng(7)

def H_deg_counts(G, x, d):
    n = G.number_of_nodes()
    deg = np.zeros(n, dtype=int)
    for u, v in G.edges():
        if x[u] + x[v] >= 1.0:
            deg[u] += 1; deg[v] += 1
    return deg, np.bincount(deg, minlength=d+1)[:d+1]

def cliques(n, d):
    G = nx.Graph()
    for i in range(n//(d+1)):
        G.add_edges_from(itertools.combinations(range(i*(d+1), (i+1)*(d+1)), 2))
    return G

# ---- H: variance of m_k ----
def var_mk(G, d, trials=4000):
    n = G.number_of_nodes()
    M = np.zeros((trials, d+1))
    for t in range(trials):
        x = rng.random(n)
        _, m = H_deg_counts(G, x, d)
        M[t] = m
    return M.mean(axis=0), M.var(axis=0)

# ---- I: variance of Q_k(C) ----
def Q_of_C(G, C, d):
    n = G.number_of_nodes()
    Q = np.zeros(d+1)
    for v in G.nodes():
        r = sum(1 for u in G[v] if C[u] != C[v])
        b = 0 if C[v] == 0 else d - r
        Q[b:b+r+1] += 1.0/(r+1)
    return Q

def var_Qk(G, d, trials=4000):
    n = G.number_of_nodes()
    A = np.zeros((trials, d+1))
    for t in range(trials):
        C = rng.integers(0, 2, size=n)
        A[t] = Q_of_C(G, C, d)
    return A.mean(axis=0), A.var(axis=0)

# ---- J: structural check: given C and U on the other side, degrees on one side
#        depend only on own label (exact, by re-randomising own labels) ----
def check_J(trials=200):
    bad = 0
    for _ in range(trials):
        d = int(rng.integers(2, 6)); n = int(rng.integers(d+2, 14))
        if (n*d) % 2: n += 1
        try: G = nx.random_regular_graph(d, n, seed=int(rng.integers(1<<30)))
        except Exception: continue
        C = rng.integers(0,2,size=n); U = rng.random(n)
        x = (C+U)/2
        deg,_ = H_deg_counts(G, x, d)
        a = 0
        Va = [v for v in G.nodes() if C[v]==a]
        if len(Va) < 2: continue
        # perturb the label of ONE vertex of V_a; degrees of the OTHER V_a vertices must not change
        w = Va[0]; U2 = U.copy(); U2[w] = rng.random()
        x2 = (C+U2)/2
        deg2,_ = H_deg_counts(G, x2, d)
        for v in Va:
            if v != w and deg[v] != deg2[v]:
                bad += 1
    return bad

# ---- K: clique-union exact E[per-clique Q contribution] ----
def check_K(d):
    out = []
    for k in range(d+1):
        tot = 0.0
        for s in range(d+2):           # s = |V_0 cap clique|,  Bin(d+1,1/2)
            pr = comb(d+1, s)*0.5**(d+1)
            c = 0.0
            r0 = d+1-s                 # r_v for a V_0 vertex
            if s > 0 and 0 <= k <= r0: c += s/(r0+1)
            r1 = s                     # r_v for a V_1 vertex
            if (d+1-s) > 0 and (d-r1) <= k <= d: c += (d+1-s)/(r1+1)
            tot += pr*c
        out.append((k, tot))
    return out

# ---- L: empirical mgf of m_k - Q_k given C ----
def check_L(G, d, k, lam_list, trials=6000):
    n = G.number_of_nodes()
    C = rng.integers(0,2,size=n)
    Q = Q_of_C(G, C, d)[k]
    vals = []
    for _ in range(trials):
        U = rng.random(n)
        x = (C+U)/2
        _, m = H_deg_counts(G, x, d)
        vals.append(m[k]-Q)
    vals = np.array(vals)
    rows = []
    for lam in lam_list:
        emp = np.log(np.mean(np.exp(lam*vals)))
        rows.append((lam, emp, 132*(n/d)*lam**2))
    return Q, vals.mean(), vals.var(), rows

if __name__ == "__main__":
    for (n, d, lab) in [(300, 9, "30 x K10"), (180, 5, "30 x K6")]:
        G = cliques(n, d)
        mm, vv = var_mk(G, d, trials=3000)
        print(f"H: {lab}: n={n} d={d}  mu={n/(d+1):.2f}  mean m_k in [{mm.min():.2f},{mm.max():.2f}]"
              f"  Var(m_k) in [{vv.min():.2f},{vv.max():.2f}]  vs 17n/(d+1)={17*n/(d+1):.1f}  n/d={n/d:.1f}")
        qm, qv = var_Qk(G, d, trials=3000)
        print(f"I: {lab}:  mean Q_k in [{qm.min():.2f},{qm.max():.2f}] (mu={n/(d+1):.2f})"
              f"  Var(Q_k) in [{qv.min():.2f},{qv.max():.2f}]  vs 8n/d={8*n/d:.1f}")
    G = nx.random_regular_graph(8, 240, seed=3)
    mm, vv = var_mk(G, 8, trials=3000)
    print(f"H: random 8-reg n=240: mean m_k in [{mm.min():.2f},{mm.max():.2f}] (mu={240/9:.2f}) "
          f" Var in [{vv.min():.2f},{vv.max():.2f}] vs 17n/(d+1)={17*240/9:.1f}")
    print("J: violations of conditional-independence structure:", check_J())
    for d in [3, 6, 11]:
        r = check_K(d)
        print(f"K: d={d}: per-clique E[Q_k] for k=0..d:", [f"{t[1]:.4f}" for t in r], "(should all be 1)")
    G = cliques(300, 9)
    Q, mean, var, rows = check_L(G, 9, 4, [-0.08,-0.04,0.04,0.08])
    print(f"L: clique-union n=300,d=9,k=4: Q_k={Q:.3f}, E[m_k-Q_k]={mean:.3f}, Var={var:.3f} (n/d={300/9:.1f})")
    for lam, emp, bound in rows:
        print(f"   lambda={lam:+.2f}  log E e^(lam*(m-Q))={emp:+.5f}   bound C1*n/d*lam^2={bound:.5f}  ok={emp<=bound}")
