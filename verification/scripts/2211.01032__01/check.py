#!/usr/bin/env python3
"""Referee checks for attack 2211.01032__01 (Conjecture 9.1 of arXiv:2211.01032).

The writeup claims to DISPROVE:  for any p(n), a.a.s. G ~ G(n,p) has E_rho[F] = O(log n),
via isolated K_2 components at p = 1/n, under a purely ADDITIVE face count over components.

The source paper (v3, Section 7, just before Theorem 1.10's proof) defines faces of a
disconnected map as  F_paper = (sum of faces over components) - c + 1,  so any tree
component contributes ZERO net.  We check:

 1. Dart-model face count of an isolated K_2 (writeup: exactly 1 face, always).
 2. E[#isolated edges] in G(n,1/n): formula C(n,2)*p*(1-p)^(2n-4) ~ e^{-2} n / 2,
    plus concentration by Monte Carlo, and Var = O(n) empirically.
 3. The p = log n/(4n) expectation ~ (1/8) sqrt(n) log n.
 4. Under the paper's convention, Monte Carlo estimate of E[F_paper] for G(n,1/n)
    (per-graph expected faces over random rotations), vs the additive count:
    additive is Theta(n), paper's is small -- so the refutation only hits the
    additive strawman, not the paper's statistic.
"""
import math, random
from itertools import combinations

random.seed(20260902)

# ---------------------------------------------------------------- dart model
def random_embedding_faces_by_component(adj, rng):
    """adj: dict v -> list of neighbors (simple graph). Returns (total_faces_additive,
    n_components) for one uniformly random rotation system, faces counted per component
    (each component in its own surface)."""
    # darts: (u,v) ordered pairs for each edge
    darts = []
    for u in adj:
        for v in adj[u]:
            darts.append((u, v))
    # rotation: for each vertex, random cyclic order of incident darts
    nxt = {}  # rotation successor of dart at its tail vertex
    for u in adj:
        inc = [(u, v) for v in adj[u]]
        rng.shuffle(inc)
        k = len(inc)
        for i in range(k):
            nxt[inc[i]] = inc[(i + 1) % k]
    # face permutation phi(d) = nxt[reverse(d)]  (one standard convention)
    seen = set()
    faces = 0
    for d in darts:
        if d in seen:
            continue
        faces += 1
        cur = d
        while cur not in seen:
            seen.add(cur)
            u, v = cur
            cur = nxt[(v, u)]
    # count components (of vertices with degree >= 1 plus isolated vertices)
    comp = 0
    vis = set()
    for s in adj:
        if s in vis:
            continue
        comp += 1
        stack = [s]
        while stack:
            x = stack.pop()
            if x in vis:
                continue
            vis.add(x)
            stack.extend(adj[x])
    return faces, comp

# Check 1: isolated K2 always has exactly 1 face
rng = random.Random(1)
adj = {0: [1], 1: [0]}
vals = set()
for _ in range(100):
    f, c = random_embedding_faces_by_component(adj, rng)
    vals.add((f, c))
print("Check 1  K_2 (faces, components) over 100 random embeddings:", vals,
      " -> paper-convention net contribution F - c + 1 =",
      {f - c + 1 for f, c in vals})

# sanity: triangle should always give 2 faces (sphere), path P3 gives 1 face
adj = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
print("        triangle:", {random_embedding_faces_by_component(adj, rng) for _ in range(50)})
adj = {0: [1], 1: [0, 2], 2: [1]}
print("        path P3 :", {random_embedding_faces_by_component(adj, rng) for _ in range(50)})

# ---------------------------------------------------- Check 2: isolated edges in G(n,1/n)
def gnp_adj(n, p, rng):
    adj = {i: [] for i in range(n)}
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < p:
                adj[u].append(v)
                adj[v].append(u)
    return adj

def isolated_edges(adj):
    return sum(1 for u in adj for v in adj[u]
               if u < v and len(adj[u]) == 1 and len(adj[v]) == 1)

n = 3000
p = 1.0 / n
mu_exact = math.comb(n, 2) * p * (1 - p) ** (2 * n - 4)
mu_asym = math.exp(-2) * n / 2
trials = 40
xs = []
rng = random.Random(7)
for _ in range(trials):
    xs.append(isolated_edges(gnp_adj(n, p, rng)))
mean = sum(xs) / trials
var = sum((x - mean) ** 2 for x in xs) / (trials - 1)
print(f"\nCheck 2  n={n}, p=1/n: exact E[X] = {mu_exact:.2f}, asymptotic e^-2 n/2 = {mu_asym:.2f}")
print(f"        Monte Carlo over {trials} trials: mean X = {mean:.2f}, sample var = {var:.1f}"
      f"  (var/n = {var/n:.3f}),  X/n mean = {mean/n:.5f} vs e^-2/2 = {math.exp(-2)/2:.5f}")

# covariance formula re-derivation for disjoint pairs
q = p * (1 - p) ** (2 * (n - 2))
joint = p * p * (1 - p) ** (4 * n - 12)
cov = joint - q * q
print(f"        disjoint-pair Cov = {cov:.3e}; writeup q^2((1-p)^-4 - 1) = "
      f"{q*q*((1-p)**-4 - 1):.3e}; n^-3 = {n**-3:.3e}")

# ---------------------------------------------------- Check 3: p = log n / (4n)
n3 = 10 ** 6
p3 = math.log(n3) / (4 * n3)
mu3 = math.comb(n3, 2) * p3 * (1 - p3) ** (2 * n3 - 4)
pred3 = math.sqrt(n3) * math.log(n3) / 8
print(f"\nCheck 3  n=1e6, p=log n/(4n): exact E[X] = {mu3:.1f}, "
      f"claimed (1/8) sqrt(n) log n = {pred3:.1f}, ratio = {mu3/pred3:.4f}")

# ---------------------------------------------------- Check 4: paper convention vs additive
print("\nCheck 4  G(n,1/n): additive faces vs paper's F - c + 1 "
      "(one random embedding per sampled graph)")
rng = random.Random(99)
for n4 in (200, 400, 800, 1600):
    p4 = 1.0 / n4
    add_tot, pap_tot, iso_tot, reps = 0, 0, 0, 12
    for _ in range(reps):
        adj4 = gnp_adj(n4, p4, rng)
        f, c = random_embedding_faces_by_component(adj4, rng)
        # An isolated vertex embeds in the sphere with 1 face (0 darts -> dart model
        # counted 0); add those so 'additive' counts one sphere per component.
        f += sum(1 for v in adj4 if not adj4[v])
        add_tot += f
        pap_tot += f - c + 1
        iso_tot += isolated_edges(adj4)
    print(f"        n={n4}: mean additive F = {add_tot/reps:7.1f}  (log n = {math.log(n4):.2f}),"
          f" mean isolated K2 = {iso_tot/reps:6.1f},"
          f" mean paper F-c+1 = {pap_tot/reps:6.2f}")
