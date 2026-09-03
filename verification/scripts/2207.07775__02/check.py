#!/usr/bin/env python3
"""
Verification script for attack 2207.07775__02 (Conjecture 5.4 of Fox-Wigderson,
"Ramsey multiplicity and the Turan coloring", arXiv:2207.07775v3).

The writeup claims to DISPROVE the conjecture using H = (K_1 join C_m) + t leaves,
with m = 2t+5, interpreting "(k,t)-generalized lollipop" as "any k-critical graph
plus t pendant edges".

The paper's actual definition (Section 5.3 "Other open problems"):
  H is a (k,t)-generalized lollipop if it has t vertices and contains a K_k
  whose deletion yields a forest (equivalently: K_k with attached trees,
  t-k tree vertices total).

Checks performed (pure Python, no external deps):
 A. Internal checks of the writeup's construction (k=4 wheel case):
    1. H0 = K_1 v C_m (m = 2t+5) has chromatic number 4 and is 4-critical
       in the strong sense (every single-edge deletion is 3-colorable).
    2. v(H) = m+1+t, e(H) = 2m+t.
    3. q_rand = 2^(1-e) < q_Tur = 3^(1-v), i.e. 2m+t-1 > (m+t)*log2(3),
       and the writeup's algebra 5t+9 > (8/5)(3t+5) with log2(3) < 8/5.
 B. Internal check of the k>=5 family: K_{k-3} v C_m is k-critical (small cases)
    with the claimed edge count (k-2)m + C(k-3,2).
 C. Interpretation check against the paper's definition:
    - the writeup's H contains NO K_4 at all, hence is not a
      (4,*)-generalized lollipop under the paper's definition;
    - for genuine (4,t)-generalized lollipops (K_4 + trees, t vertices total),
      e(H) = t+2, and the random coloring does NOT beat the Turan coloring
      once t >= 5, so the writeup's obstruction vanishes for the real family.
"""

import itertools, math, sys


# ---------- tiny graph toolkit ----------

def edges_set(edges):
    return {frozenset(e) for e in edges}


def neighbors(vertices, E):
    adj = {u: set() for u in vertices}
    for e in E:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    return adj


def is_c_colorable(vertices, E, c):
    adj = neighbors(vertices, E)
    order = sorted(vertices, key=lambda u: -len(adj[u]))
    color = {}

    def bt(i, maxused):
        if i == len(order):
            return True
        u = order[i]
        used = {color[w] for w in adj[u] if w in color}
        # symmetry breaking: allow at most one fresh color
        for col in range(min(maxused + 1, c)):
            if col not in used:
                color[u] = col
                if bt(i + 1, max(maxused, col + 1)):
                    return True
                del color[u]
        return False

    return bt(0, 0)


def chromatic_number(vertices, E, ub=8):
    for c in range(1, ub + 1):
        if is_c_colorable(vertices, E, c):
            return c
    return None


def is_k_critical_strong(vertices, E, k):
    """chi=k and every single-edge deletion is (k-1)-colorable
    (this implies every proper subgraph is (k-1)-colorable)."""
    if chromatic_number(vertices, E) != k:
        return False
    for e in E:
        E2 = E - {e}
        if not is_c_colorable(vertices, E2, k - 1):
            return False
    return True


def max_clique_size(vertices, E):
    adj = neighbors(vertices, E)
    best = 0
    verts = sorted(vertices, key=lambda u: -len(adj[u]))

    def expand(cand, size):
        nonlocal best
        if size > best:
            best = size
        for i, u in enumerate(cand):
            if size + len(cand) - i <= best:
                return
            expand([w for w in cand[i + 1:] if w in adj[u]], size + 1)

    expand(verts, 0)
    return best


def is_forest(vertices, E):
    parent = {u: u for u in vertices}

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    for e in E:
        u, v = tuple(e)
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def is_generalized_lollipop(vertices, E, k):
    """Paper's definition: contains a K_k whose deletion yields a forest."""
    for clique in itertools.combinations(vertices, k):
        if all(frozenset(p) in E for p in itertools.combinations(clique, 2)):
            S = set(clique)
            rest = [u for u in vertices if u not in S]
            E_rest = {e for e in E if not (e & S)}
            if is_forest(rest, E_rest):
                return True
    return False


# ---------- constructions ----------

def wheel_plus_leaves(t):
    m = 2 * t + 5
    V0 = list(range(m)) + ["c"]
    E0 = edges_set([(i, (i + 1) % m) for i in range(m)]
                   + [("c", i) for i in range(m)])
    V = V0 + [f"leaf{j}" for j in range(t)]
    E = E0 | edges_set([("c", f"leaf{j}") for j in range(t)])
    return (V0, E0), (V, E), m


ok = True

print("=== A. Writeup's k=4 construction (internal checks) ===")
for t in range(0, 4):
    (V0, E0), (V, E), m = wheel_plus_leaves(t)
    chi = chromatic_number(V0, E0)
    crit = is_k_critical_strong(V0, E0, 4)
    v, e = len(V), len(E)
    v_claim, e_claim = m + 1 + t, 2 * m + t
    lhs = 2 * m + t - 1            # random-coloring exponent, e-1
    rhs = (m + t) * math.log2(3)   # Turan-coloring exponent, (v-1)log2 3
    rand_beats = lhs > rhs
    print(f"t={t} m={m}: chi(H0)={chi} 4-critical={crit} "
          f"v={v}(claim {v_claim}) e={e}(claim {e_claim}) "
          f"random beats Turan: {rand_beats}  [{lhs} > {rhs:.4f}]")
    ok &= (chi == 4 and crit and v == v_claim and e == e_claim and rand_beats)
    # writeup's algebra: 5t+9 > (8/5)(3t+5) and log2 3 < 8/5
    ok &= (5 * t + 9 > 1.6 * (3 * t + 5)) and (math.log2(3) < 1.6)

print()
print("=== B. K_(k-3) v C_m is k-critical (small cases) ===")
for k in (5, 6):
    for m in (5, 7):
        V = list(range(m)) + [f"k{i}" for i in range(k - 3)]
        E = edges_set([(i, (i + 1) % m) for i in range(m)])
        Kp = [f"k{i}" for i in range(k - 3)]
        E |= edges_set(itertools.combinations(Kp, 2))
        E |= edges_set([(u, j) for u in Kp for j in range(m)])
        chi = chromatic_number(V, E)
        crit = is_k_critical_strong(V, E, k)
        e0, e0_claim = len(E), (k - 2) * m + math.comb(k - 3, 2)
        print(f"k={k} m={m}: chi={chi} {k}-critical={crit} "
              f"e0={e0} (claim {e0_claim})")
        ok &= (chi == k and crit and e0 == e0_claim)

print()
print("=== C. Interpretation check against the paper's definition ===")
for t in range(0, 4):
    _, (V, E), m = wheel_plus_leaves(t)
    omega = max_clique_size(V, E)
    glp = is_generalized_lollipop(V, E, 4)
    print(f"t={t} m={m}: max clique of H = {omega} (contains K_4: {omega >= 4}); "
          f"H is a (4,{len(V)})-generalized lollipop per paper: {glp}")
    ok &= (omega == 3 and not glp)

print()
print("--- genuine (4,t)-generalized lollipops: random vs Turan ---")
print("H = K_4 + attached trees on t vertices total: e(H) = 6 + (t-4) = t+2.")
print("Random beats Turan iff e-1 > (t-1)*log2(3), i.e. t+1 > 1.585(t-1).")
for t in (4, 5, 6, 8, 10, 20, 50):
    lhs, rhs = t + 1, (t - 1) * math.log2(3)
    print(f"  t={t}: e-1={lhs}, (t-1)log2 3={rhs:.3f} -> "
          f"random beats Turan: {lhs > rhs}")

# sanity: the paper's lollipop L_{4,10} (K_4 + pendant path) IS a
# (4,10)-generalized lollipop under the paper's definition
V = [0, 1, 2, 3] + [f"p{j}" for j in range(6)]
E = edges_set(itertools.combinations(range(4), 2))
prev = 3
for j in range(6):
    E |= edges_set([(prev, f"p{j}")])
    prev = f"p{j}"
print(f"  L_(4,10) is a (4,10)-generalized lollipop per paper: "
      f"{is_generalized_lollipop(V, E, 4)}")
ok &= is_generalized_lollipop(V, E, 4)

print()
print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
