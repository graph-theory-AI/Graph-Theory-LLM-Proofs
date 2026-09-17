"""Fast, decision-relevant referee checks for attacks_retry/2207.13651__00.
Run: python3 -u referee_fast.py
"""
import itertools, math, sys
import numpy as np, networkx as nx
from math import comb, factorial, log, exp
from scipy.stats import binom
rng = np.random.default_rng(20260917)

def Hdeg(G, x):
    deg = np.zeros(G.number_of_nodes(), dtype=int)
    for u, v in G.edges():
        if x[u] + x[v] >= 1.0:
            deg[u] += 1; deg[v] += 1
    return deg

print("== (1) eq.(6) decomposition deg_H(v)=b_v+#{cross u: U_u+U_v>=1} ==")
bad = 0; tested = 0
for _ in range(300):
    d = int(rng.integers(1, 7)); n = int(rng.integers(d + 2, 16))
    if (n * d) % 2: n += 1
    try: G = nx.random_regular_graph(d, n, seed=int(rng.integers(1 << 30)))
    except Exception: continue
    C = rng.integers(0, 2, size=n); U = rng.random(n)
    deg = Hdeg(G, (C + U) / 2.0)
    for v in G.nodes():
        r = sum(1 for u in G[v] if C[u] != C[v])
        b = 0 if C[v] == 0 else d - r
        cross = sum(1 for u in G[v] if C[u] != C[v] and U[u] + U[v] >= 1.0)
        tested += 1
        bad += (deg[v] != b + cross)
print(f"   vertices tested {tested}, violations {bad}")

print("== (2) eq.(7): q_{v,k}=1{b<=k<=b+r}/(r+1) equals Pr(deg=k|C) (exact quadrature) ==")
worst = 0.0
xs = np.linspace(0, 1, 200001)
for d in [3, 6, 9]:
    for Cv in (0, 1):
        for r in range(0, d + 1):
            b = 0 if Cv == 0 else d - r
            for k in range(0, d + 1):
                j = k - b
                # P(Bin(r, u) = j) integrated over u ~ U[0,1]
                p = np.trapz(comb(r, j) * xs**j * (1 - xs)**(r - j), xs) if 0 <= j <= r else 0.0
                q = 1.0 / (r + 1) if (b <= k <= b + r) else 0.0
                worst = max(worst, abs(p - q))
print(f"   max |Pr(deg=k|C) - q_v,k| = {worst:.3e}")

print("== (3) eq.(18)/(19): E_C Q_k = n/(d+1) exactly ==")
for d in [1, 2, 3, 5, 8, 13, 20, 33]:
    err = 0.0
    for k in range(d + 1):
        tot = 0.0
        for r in range(d + 1):
            pr = comb(d, r) * 0.5**d
            q0 = 1.0 / (r + 1) if 0 <= k <= r else 0.0
            q1 = 1.0 / (r + 1) if d - r <= k <= d else 0.0
            tot += pr * 0.5 * (q0 + q1)
        err = max(err, abs(tot - 1.0 / (d + 1)))
    print(f"   d={d:3d}  max_k |E q_v,k - 1/(d+1)| = {err:.3e}")

print("== (4) Section 4 conditional independence: perturbing one U_v (v in V_a)")
print("      must not change deg_H(w) for other w in V_a ==")
bad = 0
for _ in range(300):
    d = int(rng.integers(2, 6)); n = int(rng.integers(d + 2, 16))
    if (n * d) % 2: n += 1
    try: G = nx.random_regular_graph(d, n, seed=int(rng.integers(1 << 30)))
    except Exception: continue
    C = rng.integers(0, 2, size=n); U = rng.random(n)
    deg = Hdeg(G, (C + U) / 2.0)
    for a in (0, 1):
        Va = [v for v in G.nodes() if C[v] == a]
        if len(Va) < 2: continue
        w = Va[0]; U2 = U.copy(); U2[w] = rng.random()
        deg2 = Hdeg(G, (C + U2) / 2.0)
        for v in Va:
            if v != w and deg[v] != deg2[v]: bad += 1
print(f"   violations {bad}")

print("== (5) eq.(5): log E e^{theta d B_r} <= theta d/(r+1) + 32 theta^2 for r>=d/4, |theta|<=1/8 ==")
viol = []
xs = np.linspace(0, 1, 400001)
for d in [4, 8, 16, 32, 64, 128, 512, 2048, 8192]:
    for r in sorted(set([max(1, d // 4), d // 3, d // 2, d - 1, d])):
        if r < 1: continue
        dens = r * (1 - xs)**(r - 1)
        for th in np.linspace(-0.125, 0.125, 51):
            lhs = log(np.trapz(np.exp(th * d * xs) * dens, xs))
            rhs = th * d / (r + 1) + 32 * th * th
            if lhs > rhs + 1e-8: viol.append((d, r, float(th), lhs, rhs))
print(f"   violations {len(viol)} {viol[:3]}")
print("   spacing moments E B_r^j = j!/prod(r+i):")
mx = 0.0
for r in range(1, 30):
    dens = r * (1 - xs)**(r - 1)
    for j in range(1, 6):
        ex = factorial(j) / np.prod([r + i for i in range(1, j + 1)])
        num = np.trapz(xs**j * dens, xs)
        mx = max(mx, abs(ex - num))
print(f"   max abs error {mx:.3e}")

print("== (6) eq.(9): Pr(Bin(d,1/2) < d/4) <= e^{-d/16} ==")
viol = [(d, binom.cdf(math.ceil(d / 4.0) - 1, d, 0.5), exp(-d / 16))
        for d in range(1, 3001)
        if binom.cdf(math.ceil(d / 4.0) - 1, d, 0.5) > exp(-d / 16) + 1e-15]
print(f"   violations for d=1..3000: {len(viol)} {viol[:3]}")

print("== (7) eq.(2) Finner/read-R Holder, exhaustive on small product spaces ==")
viol = 0; worst = 0.0
for _ in range(4000):
    N = int(rng.integers(2, 5)); S = int(rng.integers(2, 4)); M = int(rng.integers(2, 6))
    sets = [tuple(sorted(rng.choice(N, size=int(rng.integers(1, N + 1)), replace=False))) for _ in range(M)]
    R = max(max(sum(1 for A in sets if j in A) for j in range(N)), 1)
    fs = [rng.random(tuple(S for _ in A)) + 0.02 for A in sets]
    tot = 0.0
    for z in itertools.product(range(S), repeat=N):
        val = 1.0
        for A, f in zip(sets, fs): val *= f[tuple(z[j] for j in A)]
        tot += val * (1.0 / S)**N
    rhs = 1.0
    for A, f in zip(sets, fs): rhs *= float(np.mean(f**R))**(1.0 / R)
    if tot > rhs * (1 + 1e-9): viol += 1
    worst = max(worst, tot / rhs)
print(f"   violations {viol}, worst LHS/RHS ratio {worst:.6f}")

print("== (8) eq.(17): Var(Q_k(C)) vs sub-gaussian proxy (bound implies Var <= 8n/d) ==")
def Qvec(G, C, d):
    Q = np.zeros(d + 1)
    for v in G.nodes():
        r = sum(1 for u in G[v] if C[u] != C[v])
        b = 0 if C[v] == 0 else d - r
        Q[b:b + r + 1] += 1.0 / (r + 1)
    return Q
def cliques(n, d):
    G = nx.Graph()
    for i in range(n // (d + 1)):
        G.add_edges_from(itertools.combinations(range(i * (d + 1), (i + 1) * (d + 1)), 2))
    return G
for (G, d, lab) in [(cliques(300, 9), 9, "30 x K10"), (cliques(420, 19), 19, "21 x K20"),
                    (nx.random_regular_graph(10, 300, seed=1), 10, "rand 10-reg n=300"),
                    (nx.complete_bipartite_graph(100, 100), 100, "K_100,100")]:
    n = G.number_of_nodes()
    A = np.array([Qvec(G, rng.integers(0, 2, size=n), d) for _ in range(3000)])
    print(f"   {lab}: n={n} d={d} mu={n/(d+1):.2f} meanQ in [{A.mean(0).min():.2f},{A.mean(0).max():.2f}]"
          f" VarQ in [{A.var(0).min():.3f},{A.var(0).max():.3f}]  bound 8n/d={8*n/d:.1f}")

print("== (9) end-to-end: max_k |m_k-mu|/mu in the model ==")
for (G, d, lab) in [(cliques(300, 9), 9, "30 x K10"), (cliques(420, 19), 19, "21 x K20"),
                    (nx.random_regular_graph(10, 300, seed=1), 10, "rand 10-reg n=300"),
                    (nx.complete_bipartite_graph(100, 100), 100, "K_100,100")]:
    n = G.number_of_nodes(); mu = n / (d + 1); w = 0.0; acc = np.zeros(d + 1)
    T = 300
    for _ in range(T):
        m = np.bincount(Hdeg(G, rng.random(n)), minlength=d + 1)[:d + 1]
        acc += m; w = max(w, np.abs(m - mu).max() / mu)
    print(f"   {lab}: mu={mu:.2f} mean m_k in [{(acc/T).min():.2f},{(acc/T).max():.2f}] worst rel dev {w:.3f}")
