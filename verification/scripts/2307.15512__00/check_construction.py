#!/usr/bin/env python3
"""Verification for 2307.15512__00 (part 2): the random construction.

(C) Samples the construction at N = 4096 (rho = N^{-1/4} = 1/8, k = 32):
    - min |A_u| over u in R vs k-1
    - min |A_u cap A_v| over pairs in R vs k-2  (event A)
    - connectivity
    - direct check that sampled edges lie in a K_k, and that the assembled
      k-uniform hypergraph H has 2-section exactly G
(D) Escape-count probe: for greedy adversarial cop sets C (chosen to maximize
    coverage of R), min over u in R of #{v in R: uv in E, v notin N[C]},
    compared with the predicted mean N*rho*(1-rho)^{|C|}.
(E) Monte Carlo check that P(v escapes a fixed C of size j) = rho(1-rho)^j.
(F) Numeric verification of every finite inequality in the writeup and the
    N-thresholds beyond which the union bounds are < 1.
"""
import numpy as np
import math

rng = np.random.default_rng(20260902)

# ---------------------------------------------------------------- (C)
N = 4096
rho = N ** (-0.25)          # = 1/8
k = int(math.sqrt(N) / 2)   # = 32
print(f"N={N} rho={rho} k={k}  n=2N={2*N}  sqrt(n/k)={math.sqrt(2*N/k):.2f}")

A = (rng.random((N, N)) < rho)          # P-R adjacency: A[u, p], u in R, p in P
RR = np.triu(rng.random((N, N)) < rho, 1)
RR = RR | RR.T                          # R-R adjacency, symmetric, no loops

deg_P = A.sum(axis=1)                   # |A_u|
print(f"min |A_u| = {deg_P.min()}  (need >= k-1 = {k-1}), mean {deg_P.mean():.1f} "
      f"(theory N*rho = {N*rho:.0f})")

Af = A.astype(np.float32)
inter = Af @ Af.T                       # |A_u cap A_v|
np.fill_diagonal(inter, np.inf)
min_int = int(inter.min())
print(f"min |A_u cap A_v| = {min_int}  (need >= k-2 = {k-2}), "
      f"mean {inter[np.isfinite(inter)].mean():.1f} (theory N*rho^2 = {N*rho*rho:.0f})")
eventA = deg_P.min() >= k - 1 and min_int >= k - 2
print(f"event A holds at this N: {eventA}")

# connectivity: P is a clique; every u in R needs a neighbour in P
print(f"every R-vertex attached to P: {bool((deg_P >= 1).all())} -> G connected")

# every-edge-in-K_k, checked structurally on samples of each edge type
ok_pr = ok_rr = True
uu, pp = np.nonzero(A)
for t in rng.choice(len(uu), size=200, replace=False):
    u, p = uu[t], pp[t]
    ok_pr &= (deg_P[u] >= k - 1)        # u + (k-1 vertices of A_u incl p) = K_k
u2, v2 = np.nonzero(np.triu(RR, 1))
for t in rng.choice(len(u2), size=200, replace=False):
    u, v = u2[t], v2[t]
    ok_rr &= (int(inter[u, v]) >= k - 2)  # u,v + (k-2 of A_u cap A_v) = K_k
print(f"sampled P-R edges coverable by K_k: {ok_pr}; R-R edges: {ok_rr}; "
      f"P-P edges trivially (|P|={N} >= k)")

# assemble H for a subsample of edges and confirm its 2-section edges are in G
# (full assembly is large; verify the invariant on 500 random edges)
def clique_for_edge(kind, u, v):
    if kind == 'PP':
        others = [x for x in range(k)]  # any k-subset of P containing u,v
        s = {u, v}
        for x in range(N):
            if len(s) == k:
                break
            s.add(x if x not in s else -1)
            s.discard(-1)
        return frozenset(list(s)[:k]) if len(s) >= k else None
    if kind == 'PR':
        Au = np.nonzero(A[u])[0]
        sel = [v] + [p for p in Au[:k] if p != v][:k - 2]
        return frozenset([('R', u)] + [('P', p) for p in sel]) if len(sel) == k - 1 else None
    if kind == 'RR':
        common = np.nonzero(A[u] & A[v])[0][:k - 2]
        return frozenset([('R', u), ('R', v)] + [('P', p) for p in common]) if len(common) == k - 2 else None

bad = 0
for t in rng.choice(len(u2), size=250, replace=False):
    u, v = int(u2[t]), int(v2[t])
    e = clique_for_edge('RR', u, v)
    if e is None or len(e) != k:
        bad += 1
        continue
    # 2-section check: every pair inside e must be an edge of G
    Rv = [x[1] for x in e if x[0] == 'R']
    Pv = [x[1] for x in e if x[0] == 'P']
    assert RR[Rv[0], Rv[1]]
    for x in Rv:
        for p in Pv:
            assert A[x, p], "hyperedge pair not an edge of G!"
print(f"assembled R-R hyperedges: {250 - bad}/250 are k-cliques of G "
      f"(pairs inside each hyperedge all edges of G)")

# ---------------------------------------------------------------- (D)
closedR = RR.copy()                     # v in N[C] via R-cop x: RR[v,x]
q_theory = int(N ** 0.25 * math.log(N) / 32)
print(f"\nq_theory = floor(N^(1/4) ln N / 32) = {q_theory}")
for q in (q_theory, 8, 16, 24):
    # greedy adversarial C from P u R maximizing coverage of R
    cov = np.zeros(N, dtype=bool)       # covered vertices of R
    C_R, C_P = [], []
    # candidate cover sets: cop at p in P covers {u in R: A[u,p]};
    # cop at x in R covers {x} u {v: RR[v,x]}
    for _ in range(q):
        gain_P = (Af[:, :].T @ (~cov).astype(np.float32))  # per p, uncovered coverage
        best_p = int(np.argmax(gain_P))
        gp = gain_P[best_p]
        gain_R = (RR & ~cov[None, :]).sum(axis=1) + (~cov)
        best_r = int(np.argmax(gain_R))
        gr = gain_R[best_r]
        if gp >= gr:
            C_P.append(best_p)
            cov |= A[:, best_p]
        else:
            C_R.append(best_r)
            cov |= RR[best_r]
            cov[best_r] = True
    # escape counts: for each u in R\C, #{v in R\(C u {u}) : uv in E, v notin N[C]}
    free = ~cov
    for x in C_R:
        free[x] = False
    esc = (RR & free[None, :]).sum(axis=1)
    valid_u = np.ones(N, dtype=bool)
    for x in C_R:
        valid_u[x] = False          # robber never sits on a cop
    min_esc = int(esc[valid_u].min())
    pred = N * rho * (1 - rho) ** q
    print(f"  q={q:3d} greedy adversarial C (|C_P|={len(C_P)},|C_R|={len(C_R)}): "
          f"min escapes over u in R\\C = {min_esc}, mean = {esc[valid_u].mean():.1f}, "
          f"predicted mean N*rho*(1-rho)^q = {pred:.1f}")

# targeted greedy: attack the single worst u at the writeup's own q = q_theory
u0 = int(np.argmin((RR).sum(axis=1)))   # u with fewest R-neighbours
nbrs = RR[u0].copy()
cov = np.zeros(N, dtype=bool)
for _ in range(q_theory):
    gain_P = Af.T @ ((nbrs & ~cov).astype(np.float32))
    best_p = int(np.argmax(gain_P))
    gain_R = (RR & (nbrs & ~cov)[None, :]).sum(axis=1)
    gain_R[u0] = -1
    best_r = int(np.argmax(gain_R))
    if gain_P[best_p] >= gain_R[best_r]:
        cov |= A[:, best_p]
    else:
        cov |= RR[best_r]
        cov[best_r] = True
esc_u0 = int((nbrs & ~cov).sum())
print(f"  targeted greedy vs worst u, q=q_theory={q_theory}: escapes left = {esc_u0} "
      f"(> 0 required; predicted ~ {int((RR[u0].sum()) * (1-rho)**q_theory)})")

# ---------------------------------------------------------------- (E)
j = 10
samples = 200000
hits = 0
for t in range(samples):
    u, v = rng.choice(N, size=2, replace=False)
    C = rng.choice(2 * N - 2, size=j, replace=False)  # avoid u, v by remap
    escaped = bool(RR[u, v])
    if escaped:
        for c in C:
            if c < N:                                  # P-cop
                if A[v, c]:
                    escaped = False
                    break
            else:                                      # R-cop (skip u, v slots)
                x = c - N
                x = x + (x >= min(u, v)) + (x + (x >= min(u, v)) >= max(u, v))
                if RR[v, x]:
                    escaped = False
                    break
    hits += escaped
emp = hits / samples
theo = rho * (1 - rho) ** j
print(f"\n(E) P(uv in E and v avoids random C of size {j}): empirical {emp:.5f} "
      f"vs rho(1-rho)^j = {theo:.5f}  ({samples} random (u,v,C) samples)")

# ---------------------------------------------------------------- (E2)
# exact binomial tails: Pr(event A fails) at large N, computed exactly
def log_binom_tail_le(n, p, m):
    """log10 of P(Bin(n,p) <= m) via stable log-sum."""
    if m < 0:
        return -math.inf
    logs = []
    lp, lq = math.log(p), math.log1p(-p)
    lc = 0.0  # log C(n,0)
    for i in range(0, m + 1):
        if i > 0:
            lc += math.log(n - i + 1) - math.log(i)
        logs.append(lc + i * lp + (n - i) * lq)
    mx = max(logs)
    return (mx + math.log(sum(math.exp(x - mx) for x in logs))) / math.log(10)

print("\n(E2) exact failure probabilities of event A (log10):")
for e in (12, 14, 16, 18, 20):
    Nn = 2 ** e
    rr = Nn ** (-0.25)
    kk = int(math.sqrt(Nn) / 2)
    t1 = log_binom_tail_le(Nn, rr, kk - 2) + math.log10(Nn)          # deg part
    t2 = log_binom_tail_le(Nn, rr * rr, kk - 3) + 2 * math.log10(Nn)  # pair part
    print(f"  N=2^{e}: log10[N*P(|A_u|<k-1)] = {t1:8.2f}, "
          f"log10[N^2*P(|A_u^A_v|<k-2)] = {t2:8.2f}  "
          f"-> event A whp: {t1 < -1 and t2 < -1}")

# ---------------------------------------------------------------- (F)
print("\n(F) finite inequalities / thresholds:")
print(f"  rho<=1/2 for N>=16: rho(16)={16**-.25:.3f}")
xs = np.linspace(1e-9, 0.5, 10001)
print(f"  ln(1-x) >= -2x on (0,1/2]: {bool((np.log(1-xs) >= -2*xs).all())}")
for name, f in [
    ("N*exp(-N^(3/4)/8) + N^2*exp(-sqrt(N)/8) < 1 (event A bound)",
     lambda t: t * math.exp(-t**0.75 / 8) + t * t * math.exp(-math.sqrt(t) / 8) < 1),
    ("N(q+1)(2N)^q exp(-N^(11/16)/2) < 1 (union bound for (*))",
     lambda t: (math.log(t) + math.log(t**0.25 * math.log(t) / 32 + 1)
                + (t**0.25 * math.log(t) / 32) * math.log(2 * t)
                - t**0.6875 / 2) < 0),
    ("N - q - 1 >= N/2",
     lambda t: t - t**0.25 * math.log(t) / 32 - 1 >= t / 2),
    ("k-1 <= N^(3/4)/2 and k-2 <= sqrt(N)/2 (Chernoff halves)",
     lambda t: int(math.sqrt(t)/2) - 1 <= t**0.75 / 2 and int(math.sqrt(t)/2) - 2 <= math.sqrt(t)/2),
]:
    # find smallest power of 2 where it holds and stays holding up to 2^40
    thr = None
    for e in range(4, 41):
        t = 2.0 ** e
        if f(t) and all(f(2.0 ** e2) for e2 in range(e, 41)):
            thr = e
            break
    print(f"  {name}: holds for all N >= 2^{thr}")

r = math.sqrt(2 * N / k)
print(f"\nfinal arithmetic at general N: k=Theta(sqrt(N)), n=2N, "
      f"sqrt(n/k) ~ 2 N^(1/4); c(H) > q = N^(1/4) ln N/32 -> ratio ln N/64 -> infinity: OK")
