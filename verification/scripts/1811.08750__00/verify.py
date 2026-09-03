#!/usr/bin/env python3
"""Referee verification for attack 1811.08750__00.

Checks, by brute force on small instances:
  A. The degenerate counterexample: ex(G, K1, {K2}) = n for every graph G.
  B. Identity (1): tau(Y) = min_S (|S| + e(Y-S)).
  C. Poljak-style reduction (2): tau(X) = e(Y) + tau(Y) where X replaces each
     edge uv of Y by a path u-a-b-v (double subdivision); X is triangle-free.
  D. Cone identity (3): for triangle-free X and Q = cone(X),
     z(Q) := max edges of a triangle-free subgraph of Q = e(Q) - tau(X),
     and omega(Q) <= 3.
  E. Inequality (4): M^r z(Q) <= W_m(R) <= M^r z(Q) + r M^{r-1} C(q,3)
     for R = (complete r-partite with parts of size M) join Q, m = r+2,
     W_m(R) = max # of K_m in a K_{m+1}-free subgraph of R.
  F. Blow-up identity (5): ex(G^{(s)}, K_m, {K_k}) = s^m ex(G, K_m, {K_k}).
  G. Numeric spot-check of the amplification arithmetic in section 2.3.
"""
import itertools, random
from math import comb, ceil

random.seed(20260902)

# ---------- basic helpers (graphs as (n, set of frozenset edges)) ----------

def all_cliques(n, edges, k):
    """All k-cliques (as vertex tuples) of graph on vertices 0..n-1."""
    adj = [[False]*n for _ in range(n)]
    for e in edges:
        u, v = tuple(e)
        adj[u][v] = adj[v][u] = True
    out = []
    for c in itertools.combinations(range(n), k):
        if all(adj[a][b] for a, b in itertools.combinations(c, 2)):
            out.append(c)
    return out

def tau_bruteforce(n, edges):
    """Minimum vertex cover by increasing size."""
    for k in range(n + 1):
        for S in itertools.combinations(range(n), k):
            Sset = set(S)
            if all(e & Sset for e in edges):
                return k
    raise AssertionError

def max_target_count_forbidden_free(n, edges, target_k, forbid_k):
    """max over edge-subsets H of #(K_target in H) s.t. H has no K_forbid.
    Bitmask brute force over subsets of the edge set."""
    E = sorted(tuple(sorted(e)) for e in edges)
    idx = {e: i for i, e in enumerate(E)}
    def cliq_mask(c):
        m = 0
        for a, b in itertools.combinations(c, 2):
            m |= 1 << idx[(a, b)]
        return m
    targets = [cliq_mask(c) for c in all_cliques(n, edges, target_k)]
    forbids = [cliq_mask(c) for c in all_cliques(n, edges, forbid_k)]
    best = -1
    for mask in range(1 << len(E)):
        if any(mask & f == f for f in forbids):
            continue
        cnt = sum(1 for t in targets if mask & t == t)
        if cnt > best:
            best = cnt
    return best

def random_graph(n, p):
    return set(frozenset(e) for e in itertools.combinations(range(n), 2)
               if random.random() < p)

# ---------- A. degenerate counterexample ----------

def check_A():
    # ex(G,K1,{K2}) = max #vertices over K2-free subgraphs (V',E') of G.
    # Enumerate all subgraphs (vertex subset + edge subset within it).
    for trial in range(20):
        n = random.randint(1, 6)
        edges = random_graph(n, 0.5)
        best = 0
        for r in range(n + 1):
            for V in itertools.combinations(range(n), r):
                Vs = set(V)
                sub = [e for e in edges if e <= Vs]
                # K2-free subgraph must have empty edge set; count K1 copies
                best = max(best, len(V))  # empty edge subset always allowed
                # (any edge subset containing an edge is not K2-free)
        assert best == n, (n, best)
    print("A. ex(G,K1,{K2}) = n verified on 20 random graphs (n<=6).")

# ---------- B. identity (1) ----------

def check_B():
    for trial in range(60):
        n = random.randint(1, 7)
        edges = random_graph(n, 0.5)
        t = tau_bruteforce(n, edges)
        m = min(len(S) + sum(1 for e in edges if not (e & set(S)))
                for k in range(n + 1) for S in itertools.combinations(range(n), k))
        assert t == m, (n, edges, t, m)
    print("B. tau(Y) = min_S(|S|+e(Y-S)) verified on 60 random graphs (n<=7).")

# ---------- C. Poljak double subdivision ----------

def double_subdivide(n, edges):
    E = sorted(tuple(sorted(e)) for e in edges)
    N = n
    new_edges = set()
    for (u, v) in E:
        a, b = N, N + 1
        N += 2
        new_edges |= {frozenset((u, a)), frozenset((a, b)), frozenset((b, v))}
    return N, new_edges

def check_C():
    for trial in range(25):
        n = random.randint(2, 5)
        edges = random_graph(n, 0.6)
        if not edges:
            continue
        N, xe = double_subdivide(n, edges)
        assert not all_cliques(N, xe, 3), "X not triangle-free!"
        tx = tau_bruteforce(N, xe)
        ty = tau_bruteforce(n, edges)
        assert tx == len(edges) + ty, (n, edges, tx, ty)
    print("C. tau(X) = e(Y) + tau(Y) and X triangle-free verified (25 random Y, n<=5).")

# ---------- D. cone identity ----------

def cone(n, edges):
    c = n
    ne = set(edges) | {frozenset((c, v)) for v in range(n)}
    return n + 1, ne

def random_triangle_free(n, p):
    while True:
        e = random_graph(n, p)
        if not all_cliques(n, e, 3):
            return e

def check_D():
    for trial in range(12):
        n = random.randint(3, 6)
        xe = random_triangle_free(n, 0.5)
        qn, qe = cone(n, xe)
        # triangles of Q are exactly {c,u,v} for uv in E(X)
        tris = all_cliques(qn, qe, 3)
        assert len(tris) == len(xe)
        assert all(n in t for t in tris)
        # omega(Q) <= 3
        assert not all_cliques(qn, qe, 4)
        z = max_target_count_forbidden_free(qn, qe, 2, 3)
        tx = tau_bruteforce(n, xe)
        assert z == len(qe) - tx, (n, xe, z, len(qe), tx)
    print("D. z(cone(X)) = e(Q) - tau(X), omega(Q)<=3 verified (12 random triangle-free X, n<=6).")

def check_D_pipeline():
    # end-to-end tiny instance: Y=K3 -> X -> Q
    n, edges = 3, {frozenset((0, 1)), frozenset((0, 2)), frozenset((1, 2))}
    N, xe = double_subdivide(n, edges)
    tx = tau_bruteforce(N, xe)
    assert tx == 3 + 2 == 5, tx           # e(Y)+tau(Y) = 3+2
    qn, qe = cone(N, xe)
    z = max_target_count_forbidden_free(qn, qe, 2, 3)
    assert z == len(qe) - tx == 18 - 5 == 13, (z, len(qe), tx)
    print(f"D'. pipeline Y=K3: tau(X)={tx}, e(Q)={len(qe)}, z(Q)={z} (= e(Q)-tau(X)).")

# ---------- E. inequality (4) ----------

def join_complete_multipartite(r, M, qn, qe):
    """R = B v Q, B complete r-partite with parts of size M, Q appended after."""
    n = r * M + qn
    parts = [list(range(i * M, (i + 1) * M)) for i in range(r)]
    edges = set()
    for i in range(r):
        for j in range(i + 1, r):
            for a in parts[i]:
                for b in parts[j]:
                    edges.add(frozenset((a, b)))
    qoff = r * M
    for e in qe:
        u, v = tuple(e)
        edges.add(frozenset((u + qoff, v + qoff)))
    for b in range(qoff):
        for v in range(qn):
            edges.add(frozenset((b, v + qoff)))
    return n, edges

def check_E():
    # Q = cone(P3): X = path 0-1-2, tau(X)=1
    xn, xe = 3, {frozenset((0, 1)), frozenset((1, 2))}
    qn, qe = cone(xn, xe)              # q=4, e(Q)=5
    z = max_target_count_forbidden_free(qn, qe, 2, 3)
    assert z == 4, z
    Cq = comb(qn, 3)                   # = 4
    for (m, M) in [(3, 2), (3, 3), (4, 1), (4, 2)]:
        r = m - 2
        rn, re = join_complete_multipartite(r, M, qn, qe)
        W = max_target_count_forbidden_free(rn, re, m, m + 1)
        lo = M**r * z
        hi = M**r * z + r * M**(r - 1) * Cq
        assert lo <= W <= hi, (m, M, W, lo, hi)
        print(f"E. m={m}, M={M}: W_{m}(R)={W}, bounds [{lo}, {hi}] hold "
              f"(R: {rn} vertices, {len(re)} edges).")
    # arithmetic of the floor recovery: M = 2 r Cq + 1 => r Cq / M < 1/2
    for r in range(1, 6):
        for Cq_ in [1, 4, 10, 120]:
            M = 2 * r * Cq_ + 1
            assert r * M**(r-1) * Cq_ * 2 < M**r
    print("E'. with M = 2 r C_q + 1 the additive slack r M^{r-1} C_q < M^r / 2 (checked r<=5).")

# ---------- F. blow-up identity (5) ----------

def blow_up(n, edges, s):
    N = n * s
    ne = set()
    for e in edges:
        u, v = tuple(e)
        for i in range(s):
            for j in range(s):
                ne.add(frozenset((u * s + i, v * s + j)))
    return N, ne

def check_F():
    cases = [
        # (name, n, edges, m, k, s)
        ("K3",   3, {frozenset(e) for e in [(0,1),(0,2),(1,2)]}, 2, 3, 2),
        ("paw",  4, {frozenset(e) for e in [(0,1),(0,2),(1,2),(2,3)]}, 2, 3, 2),
        ("K4-e", 4, {frozenset(e) for e in [(0,1),(0,2),(1,2),(1,3),(2,3)]}, 2, 3, 2),
        ("K4",   4, {frozenset(e) for e in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]}, 3, 4, 2),
    ]
    for name, n, edges, m, k, s in cases:
        base = max_target_count_forbidden_free(n, edges, m, k)
        N, be = blow_up(n, edges, s)
        if len(be) > 22:
            print(f"F. {name}: skipped blow-up ({len(be)} edges too many)")
            continue
        blown = max_target_count_forbidden_free(N, be, m, k)
        assert blown == s**m * base, (name, base, blown)
        print(f"F. {name}: ex(G,K{m},K{k})={base}, ex(G^({s}),...)={blown} = {s}^{m}*{base}.")

# ---------- G. amplification arithmetic ----------

def check_G():
    from math import log
    for (m, eps) in [(2, 0.5), (3, 0.25), (4, 1.0), (5, 0.1)]:
        for p in [5, 10, 50]:
            a = ceil(m / eps)
            L = ceil(4 ** (1 / eps))
            s = L * p**a
            N = p * s
            # s^eps >= 4 p^m   and   N^(m-eps) <= s^m / 4, in log form
            assert eps * log(s) >= log(4) + m * log(p) - 1e-9
            assert (m - eps) * log(N) <= m * log(s) - log(4) + 1e-9, (m, eps, p)
    print("G. amplification arithmetic N^(m-eps) <= s^m/4 verified for sample (m,eps,p).")

if __name__ == "__main__":
    check_A(); check_B(); check_C(); check_D(); check_D_pipeline()
    check_E(); check_F(); check_G()
    print("ALL CHECKS PASSED")
