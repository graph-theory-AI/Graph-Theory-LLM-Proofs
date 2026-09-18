"""Checks of the Section-6 mechanism and of the auxiliary lemmas."""
import itertools, math, random
import numpy as np
import networkx as nx
from verify_construction import H, red, blue, n
from build_instance import girth

S = 6           # length of the H-corridors
M = 100 * 36    # length of the long corridors (= 100 g^2 with g = 6)

# ---- weighted model of G on the split vertices only -------------------------
W = nx.Graph()
V = list(H.nodes())
for v in V:
    W.add_edge((v, 'R'), (v, 'B'), weight=1)
for u, v in itertools.combinations(V, 2):
    e = (min(u, v), max(u, v))
    if e in red:
        W.add_edge((u, 'R'), (v, 'R'), weight=S)
    elif e in blue:
        W.add_edge((u, 'B'), (v, 'B'), weight=S)
    else:
        W.add_edge((u, 'R'), (v, 'R'), weight=M)
dW = dict(nx.all_pairs_dijkstra_path_length(W))
D = {(u, v): dW[(u, 'R')][(v, 'R')] for u in V for v in V}

print("=== distance facts in G ===")
print("red edges  : d_G(u_R,v_R) values =", sorted({D[(u, v)] for (u, v) in red}), " (claim: S =", S, ")")
print("blue edges : d_G(u_R,v_R) values =", sorted({D[(u, v)] for (u, v) in blue}), " (claim: S+2 =", S + 2, ")")

# alternating (colour-changing) non-backtracking paths: cost should be S*t + t - 1
def colour(e):
    e = (min(e), max(e))
    return 'R' if e in red else 'B'

def alternating_paths(t):
    out = []
    for v0 in V:
        stack = [([v0], None)]
        while stack:
            path, lastc = stack.pop()
            if len(path) == t + 1:
                out.append(tuple(path)); continue
            x = path[-1]
            for y in H[x]:
                if y in path:
                    continue
                c = colour((x, y))
                if lastc is not None and c == lastc:
                    continue
                stack.append((path + [y], c))
    return out

for t in range(1, 5):
    ps = alternating_paths(t)
    if not ps:
        print(f"t={t}: no alternating paths"); continue
    vals = {D[(p[0], p[-1])] - (S * t + t - 1) for p in ps}
    dh = {nx.shortest_path_length(H, p[0], p[-1]) for p in ps}
    print(f"t={t}: #alt paths={len(ps)}  d_G(u_R,v_R) - (S t + t - 1) in {sorted(vals)}  d_H(ends) in {sorted(dh)}")

# monochromatic paths of length t : cost should be S t  (red) or S t + 2 (blue)
def mono_paths(t, col):
    out = []
    for v0 in V:
        stack = [[v0]]
        while stack:
            path = stack.pop()
            if len(path) == t + 1:
                out.append(tuple(path)); continue
            x = path[-1]
            for y in H[x]:
                if y in path or colour((x, y)) != col:
                    continue
                stack.append(path + [y])
    return out

for col in ('R', 'B'):
    for t in (2, 3):
        ps = mono_paths(t, col)
        vals = sorted({D[(p[0], p[-1])] for p in ps})
        print(f"mono {col} paths length {t}: #={len(ps)} d_G(u_R,v_R) in {vals} (claim {S*t} resp {S*t+2})")

# ---- how well can ANY edge weighting of H additively approximate D? ---------
print()
print("=== best additive approximation of D by an edge weighting of H ===")
E_H = sorted((min(u, v), max(u, v)) for u, v in H.edges())
idx = {e: i for i, e in enumerate(E_H)}

def max_err(lam):
    Wl = nx.Graph()
    Wl.add_nodes_from(V)
    for e, i in idx.items():
        Wl.add_edge(e[0], e[1], weight=max(lam[i], 0.0))
    dl = dict(nx.all_pairs_dijkstra_path_length(Wl))
    return max(abs(dl[u][v] - D[(u, v)]) for u in V for v in V)

rng = random.Random(7)
lam0 = np.array([float(D[e]) for e in E_H])       # natural guess lambda_e = d_G(u_R,v_R)
print("lambda_e = d_G(u_R,v_R):      max additive error =", max_err(lam0))
print("lambda_e = S for every edge:  max additive error =", max_err(np.full(len(E_H), float(S))))

# local search (coordinate descent + random restarts)
best = None
for restart in range(6):
    lam = lam0.copy() if restart == 0 else np.array([rng.uniform(S - 2, S + 4) for _ in E_H])
    cur = max_err(lam)
    for it in range(60):
        improved = False
        for i in range(len(E_H)):
            for step in (1.0, 0.5, 0.25, -0.25, -0.5, -1.0):
                trial = lam.copy(); trial[i] = max(trial[i] + step, 0.0)
                val = max_err(trial)
                if val < cur - 1e-9:
                    lam, cur = trial, val; improved = True
        if not improved:
            break
    if best is None or cur < best[0]:
        best = (cur, lam.copy())
print("best max additive error found over all weightings:", round(best[0], 4))
print("   (s = alternation length available here is tiny because girth(H) = 6;")
print("    the writeup's bound needs girth >= 10000, so this only exhibits the mechanism.)")
