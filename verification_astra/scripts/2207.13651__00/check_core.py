"""
Referee checks for attacks_retry/2207.13651__00 (Fox-Luo-Pham Property (*) conjecture).

Checks:
 A. the half-interval decomposition:  deg_H(v) = b_v + #{cross nbrs u : U_u+U_v >= 1}   (eq. 6)
 B. q_{v,k}(C) = Pr(deg_H(v)=k | C) = 1{b_v<=k<=b_v+r_v}/(r_v+1)                        (eq. 7/8)
 C. E[Q_k] = n/(d+1) and E[m_k] = n/(d+1)                                               (eq. 18)
 D. spacing moments E B_r^j = j!/((r+1)...(r+j)) and the mgf bound (5)
 E. binomial tail  Pr(Bin(d,1/2) < d/4) <= e^{-d/16}                                    (eq. 9)
 F. Finner / read-R product Holder inequality (2), random numerical instances
 G. end-to-end Monte Carlo of max_k |m_k - mu| on adversarial graphs
"""
import itertools, math, random
import numpy as np
import networkx as nx
from math import comb, lgamma, exp, log, factorial

rng = np.random.default_rng(20260917)

def H_degrees(G, x):
    n = G.number_of_nodes()
    deg = np.zeros(n, dtype=int)
    for u, v in G.edges():
        if x[u] + x[v] >= 1.0:
            deg[u] += 1; deg[v] += 1
    return deg

# ---------------- A: decomposition identity -----------------------------------
def check_A(trials=400):
    bad = 0
    for _ in range(trials):
        d = rng.integers(1, 7)
        n = int(rng.integers(d+1, 14))
        try:
            G = nx.random_regular_graph(int(d), n, seed=int(rng.integers(1 << 30)))
        except Exception:
            continue
        C = rng.integers(0, 2, size=n)
        U = rng.random(n)
        x = (C + U) / 2.0
        deg = H_degrees(G, x)
        for v in G.nodes():
            r_v = sum(1 for u in G[v] if C[u] != C[v])
            b_v = 0 if C[v] == 0 else (G.degree(v) - r_v)
            cross = sum(1 for u in G[v] if C[u] != C[v] and U[u] + U[v] >= 1.0)
            if deg[v] != b_v + cross:
                bad += 1
    return bad

# ---------------- B: q_{v,k} = Pr(deg=k | C) ----------------------------------
def check_B(d=6, reps=200000):
    """Single vertex, fixed r cross-neighbours, exact Monte-Carlo of Pr(deg=k|C)."""
    out = []
    for C_v in (0, 1):
        for r in range(0, d+1):
            b = 0 if C_v == 0 else (d - r)
            Uv = rng.random(reps)
            Ucross = rng.random((reps, r)) if r > 0 else np.zeros((reps, 0))
            cnt = (Ucross + Uv[:, None] >= 1.0).sum(axis=1)
            deg = b + cnt
            for k in range(0, d+1):
                emp = (deg == k).mean()
                q = (1.0/(r+1)) if (b <= k <= b + r) else 0.0
                out.append((C_v, r, k, emp, q, abs(emp-q)))
    return out

# ---------------- C: E[Q_k] = n/(d+1) -----------------------------------------
def check_C_exact(d):
    """E over r~Bin(d,1/2) and C_v~Ber(1/2) of q_{v,k}; should be 1/(d+1) for all k."""
    res = []
    for k in range(0, d+1):
        tot = 0.0
        for r in range(0, d+1):
            pr = comb(d, r) * 0.5**d
            # C_v = 0 : b=0, active iff 0<=k<=r
            q0 = (1.0/(r+1)) if (0 <= k <= r) else 0.0
            # C_v = 1 : b=d-r, active iff d-r<=k<=d
            q1 = (1.0/(r+1)) if (d - r <= k <= d) else 0.0
            tot += pr * 0.5 * (q0 + q1)
        res.append((k, tot, 1.0/(d+1), abs(tot - 1.0/(d+1))))
    return res

# ---------------- D: spacing moments + mgf bound (5) --------------------------
def check_D():
    rows = []
    for r in range(1, 40):
        for j in range(1, 6):
            exact = factorial(j) / np.prod([r + i for i in range(1, j+1)])
            # Beta(1,r) moment by numeric integration
            xs = np.linspace(0, 1, 200001)
            dens = r * (1 - xs)**(r - 1)
            num = np.trapz(xs**j * dens, xs)
            rows.append((r, j, exact, num, abs(exact-num)))
    # mgf bound (5):  log E e^{theta d B_r} <= theta d/(r+1) + 32 theta^2, r>=d/4, |theta|<=1/8
    viol = []
    for d in [4, 8, 16, 32, 64, 128, 512, 2048]:
        for r in range(max(1, d//4), d+1):
            for theta in np.linspace(-0.125, 0.125, 41):
                xs = np.linspace(0, 1, 400001)
                dens = r * (1 - xs)**(r - 1)
                lhs = log(np.trapz(np.exp(theta*d*xs)*dens, xs))
                rhs = theta*d/(r+1) + 32*theta**2
                if lhs > rhs + 1e-9:
                    viol.append((d, r, theta, lhs, rhs))
    return rows, viol

# ---------------- E: binomial tail --------------------------------------------
def check_E():
    from scipy.stats import binom
    viol = []
    for d in range(1, 4001):
        # Pr(Bin(d,1/2) < d/4)
        thr = d/4.0
        kmax = math.ceil(thr) - 1
        p = binom.cdf(kmax, d, 0.5) if kmax >= 0 else 0.0
        if p > exp(-d/16.0) + 1e-15:
            viol.append((d, p, exp(-d/16.0)))
    return viol

# ---------------- F: Finner / read-R Holder -----------------------------------
def check_F(trials=3000):
    """E prod f_i <= prod (E f_i^R)^{1/R} when every coordinate is read <= R times."""
    worst = 0.0
    viol = 0
    for _ in range(trials):
        N = int(rng.integers(2, 5))      # number of coordinates, each uniform on {0..S-1}
        S = int(rng.integers(2, 4))
        M = int(rng.integers(2, 6))      # number of functions
        sets = [tuple(sorted(rng.choice(N, size=int(rng.integers(1, N+1)), replace=False))) for _ in range(M)]
        R = max(max(sum(1 for A in sets if j in A) for j in range(N)), 1)
        fs = [rng.random(tuple(S for _ in A)) + 0.05 for A in sets]
        # exhaustive expectation over the product space
        tot = 0.0
        for z in itertools.product(range(S), repeat=N):
            pr = (1.0/S)**N
            val = 1.0
            for A, f in zip(sets, fs):
                val *= f[tuple(z[j] for j in A)]
            tot += pr*val
        rhs = 1.0
        for A, f in zip(sets, fs):
            rhs *= (float(np.mean(f**R)))**(1.0/R)
        if tot > rhs*(1+1e-9):
            viol += 1
        worst = max(worst, tot/rhs)
    return viol, worst

# ---------------- G: end-to-end Monte Carlo -----------------------------------
def disjoint_cliques(n, d):
    assert n % (d+1) == 0
    G = nx.Graph()
    for i in range(n//(d+1)):
        G = nx.union(G, nx.complete_graph(range(i*(d+1), (i+1)*(d+1))))
    return G

def check_G(G, trials=300, label=""):
    n = G.number_of_nodes(); d = G.degree(0)
    mu = n/(d+1)
    worst = 0.0
    means = np.zeros(d+1)
    for _ in range(trials):
        x = rng.random(n)
        deg = H_degrees(G, x)
        m = np.bincount(deg, minlength=d+1)[:d+1]
        means += m
        worst = max(worst, np.abs(m - mu).max()/mu)
    means /= trials
    return dict(label=label, n=n, d=d, mu=mu, max_rel_dev=worst,
                mean_min=means.min(), mean_max=means.max())

if __name__ == "__main__":
    print("=== A: decomposition identity deg_H(v) = b_v + cross-count ===")
    print("  violations:", check_A())

    print("\n=== B: q_{v,k} = Pr(deg=k|C)  (d=6, 2e5 MC reps) ===")
    rows = check_B()
    print("  max |empirical - formula| =", max(r[5] for r in rows))
    print("  worst row:", max(rows, key=lambda r: r[5]))

    print("\n=== C: E[q_{v,k}] = 1/(d+1) exactly ===")
    for d in [1,2,3,5,8,13,20]:
        r = check_C_exact(d)
        print(f"  d={d:3d}  max |E Q_k/n - 1/(d+1)| = {max(t[3] for t in r):.3e}")

    print("\n=== D: spacing moments and mgf bound (5) ===")
    rows, viol = check_D()
    print("  max |exact - numeric| moment error:", max(r[4] for r in rows))
    print("  violations of (5):", len(viol), viol[:5])

    print("\n=== E: Pr(Bin(d,1/2)<d/4) <= e^{-d/16} ===")
    v = check_E()
    print("  violations for d=1..4000:", len(v), v[:5])

    print("\n=== F: read-R product Holder (2) ===")
    viol, worst = check_F()
    print("  violations:", viol, " worst ratio LHS/RHS:", worst)

    print("\n=== G: end-to-end Monte Carlo ===")
    for G, lab in [(disjoint_cliques(300, 9), "50 x K10"),
                   (disjoint_cliques(600, 19), "30 x K20"),
                   (nx.random_regular_graph(10, 300, seed=1), "random 10-reg n=300"),
                   (nx.complete_bipartite_graph(150, 150), "K_{150,150}")]:
        print("  ", check_G(G, trials=200, label=lab))
