#!/usr/bin/env python3
"""
Independent verification for attack 2009.12189__00.

The writeup claims: the planar dual G of the Tutte graph H (46-vertex cubic,
3-connected, planar, non-Hamiltonian) is a 25-vertex plane triangulation with
va_f(G) >= 88/43 > 2, via the dual LP weighting z_v = (d(v)-2)/43, whose
feasibility is equivalent to  max_F sum_{v in F}(d(v)-2) <= 43  over all
induced forests F of G.

Checks performed here, all independent of the writeup's reasoning:
  (A) H := networkx.tutte_graph() is simple, cubic, planar, 3-connected,
      46 vertices, 69 edges.
  (B) H has NO Hamiltonian cycle  (exhaustive backtracking with forced-edge
      propagation over edge in/out decisions; complete search).
  (C) The plane dual G of H has 25 vertices, 69 edges, is simple and planar
      (69 = 3*25 - 6 edges + simple + planar => maximal planar triangulation),
      min degree >= 3; degree sequence and sum(d(v)-2) = 88 reported.
  (D) M := max over induced forests F of G of w(F) = sum_{v in F} (d(v)-2)
      computed by exhaustive branch-and-bound.  Writeup needs M <= 43.
      ALSO: a(G) := max size of an induced forest (same B&B, unit weights).
  (E) Direct search for a partition of V(G) into two induced forests
      (backtracking with undoable union-find) -- writeup claims none exists.
  (F) The actual LP value va_f(G) via column generation:
      restricted master LP (scipy linprog / HiGHS) + exact pricing by B&B
      max-weight induced forest.  Reports primal value and a verified dual
      bound.  Writeup predicts va_f(G) >= 88/43 ~ 2.04651.
"""

import fractions
import itertools
import sys
import time

import networkx as nx

sys.setrecursionlimit(100000)


# ---------------------------------------------------------------- (A) Tutte graph
def check_tutte_graph():
    H = nx.tutte_graph()
    assert H.number_of_nodes() == 46, H.number_of_nodes()
    assert H.number_of_edges() == 69, H.number_of_edges()
    assert set(d for _, d in H.degree()) == {3}
    assert nx.is_connected(H)
    planar, emb = nx.check_planarity(H)
    assert planar
    assert nx.node_connectivity(H) == 3, "not 3-connected"
    assert all(H.has_edge(u, v) is True for u, v in H.edges())
    # simple graph class already; no self loops
    assert all(u != v for u, v in H.edges())
    print("(A) Tutte graph: 46 vertices, 69 edges, cubic, planar, 3-connected: OK")
    return H, emb


# ---------------------------------------------------------------- (B) Hamiltonicity
def is_hamiltonian(H):
    """Complete search for a Hamiltonian cycle in a cubic graph via edge
    in/out decisions with propagation. Returns True iff one exists."""
    n = H.number_of_nodes()
    nodes = list(H.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    edges = [(idx[u], idx[v]) for u, v in H.edges()]
    m = len(edges)
    inc = [[] for _ in range(n)]  # edge ids incident to each vertex
    for ei, (u, v) in enumerate(edges):
        inc[u].append(ei)
        inc[v].append(ei)

    # state[e]: 0 undecided, 1 in, -1 out
    state = [0] * m
    deg_in = [0] * n   # incident edges decided 'in'
    deg_out = [0] * n  # incident edges decided 'out'
    parent = list(range(n))  # union-find over 'in' edges, undoable (no path compr.)
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    class FoundHam(Exception):
        pass

    trail = []  # explicit undo records

    def set_edge2(ei, val, queue):
        if state[ei] == val:
            return True
        if state[ei] != 0:
            return False
        u, v = edges[ei]
        if val == 1:
            if deg_in[u] >= 2 or deg_in[v] >= 2:
                return False
            ru, rv = find(u), find(v)
            if ru == rv:
                if sum(deg_in) == 2 * (n - 1) and deg_in[u] == 1 and deg_in[v] == 1:
                    raise FoundHam()
                return False
            state[ei] = 1
            deg_in[u] += 1
            deg_in[v] += 1
            if rank[ru] < rank[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            bumped = False
            if rank[ru] == rank[rv]:
                rank[ru] += 1
                bumped = True
            trail.append((ei, 1, u, v, rv, ru, bumped))
        else:
            if deg_out[u] >= 1 or deg_out[v] >= 1:
                return False
            state[ei] = -1
            deg_out[u] += 1
            deg_out[v] += 1
            trail.append((ei, -1, u, v, None, None, False))
        queue.append(u)
        queue.append(v)
        return True

    def rollback2(mark):
        while len(trail) > mark:
            ei, val, u, v, rv, ru, bumped = trail.pop()
            state[ei] = 0
            if val == 1:
                deg_in[u] -= 1
                deg_in[v] -= 1
                parent[rv] = rv
                if bumped:
                    rank[ru] -= 1
            else:
                deg_out[u] -= 1
                deg_out[v] -= 1

    nodes_searched = [0]

    def search():
        nodes_searched[0] += 1
        # pick an undecided edge, preferably incident to a constrained vertex
        pick = -1
        for v in range(n):
            if deg_in[v] == 1:
                for ei in inc[v]:
                    if state[ei] == 0:
                        pick = ei
                        break
                if pick >= 0:
                    break
        if pick < 0:
            for ei in range(m):
                if state[ei] == 0:
                    pick = ei
                    break
        if pick < 0:
            # all edges decided; deg_in==2 everywhere means union of cycles;
            # a Ham cycle would have been caught when closed. So not Ham here.
            return False
        for val in (1, -1):
            mark = len(trail)
            q = []
            ok = set_edge2(pick, val, q) and propagate2(q)
            if ok:
                if search():
                    return True
            rollback2(mark)
        return False

    def propagate2(queue):
        while queue:
            v = queue.pop()
            und = [ei for ei in inc[v] if state[ei] == 0]
            if deg_in[v] > 2 or deg_in[v] + len(und) < 2:
                return False
            if deg_in[v] == 2:
                for ei in und:
                    if not set_edge2(ei, -1, queue):
                        return False
            elif deg_in[v] + len(und) == 2:
                for ei in und:
                    if not set_edge2(ei, 1, queue):
                        return False
        return True

    try:
        found = search()
    except FoundHam:
        return True, nodes_searched[0]
    return found, nodes_searched[0]


# ---------------------------------------------------------------- (C) dual
def build_dual(H, emb):
    seen = set()
    faces = []
    halfedge_face = {}
    for u in H:
        for v in emb.neighbors_cw_order(u):
            if (u, v) not in seen:
                face = emb.traverse_face(u, v, mark_half_edges=seen)
                i = len(faces)
                faces.append(face)
                for j in range(len(face)):
                    a = face[j]
                    b = face[(j + 1) % len(face)]
                    halfedge_face[(a, b)] = i
    G = nx.Graph()
    G.add_nodes_from(range(len(faces)))
    for u, v in H.edges():
        f1 = halfedge_face[(u, v)]
        f2 = halfedge_face[(v, u)]
        assert f1 != f2, "bridge in 3-connected cubic graph?!"
        assert not G.has_edge(f1, f2), "dual not simple (multi-edge)"
        G.add_edge(f1, f2)
    return G, faces


# ------------------------------------------- (D) max-weight induced forest (B&B)
def max_weight_induced_forest(G, weight):
    """Exhaustive branch & bound. weight: dict v -> number (>0).
    Returns (best_value, best_set, nodes)."""
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    n = len(nodes)
    pos = {v: i for i, v in enumerate(nodes)}
    adj = [[pos[u] for u in G.neighbors(v)] for v in nodes]
    w = [weight[v] for v in nodes]
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + w[i]

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    in_set = [False] * n
    best = [0, []]
    cnt = [0]

    def rec(i, cur):
        cnt[0] += 1
        if cur > best[0]:
            best[0] = cur
            best[1] = [nodes[j] for j in range(n) if in_set[j]]
        if i == n or cur + suffix[i] <= best[0]:
            return
        v = i
        # try including v
        nbrs_in = [u for u in adj[v] if in_set[u]]
        roots = [find(u) for u in nbrs_in]
        if len(set(roots)) == len(roots):  # no two nbrs already connected
            # union v with each root (v becomes representative)
            saved = [(r, parent[r]) for r in roots]
            for r in roots:
                parent[r] = v
            in_set[v] = True
            rec(i + 1, cur + w[v])
            in_set[v] = False
            for r, p in reversed(saved):
                parent[r] = p
            parent[v] = v
        # try excluding v
        rec(i + 1, cur)

    rec(0, 0)
    return best[0], best[1], cnt[0]


def check_forest(G, S):
    return nx.is_forest(G.subgraph(S))


# ------------------------------------------- (E) partition into two induced forests
def two_forest_partition(G):
    """Backtracking: color vertices A/B, no monochromatic cycle.
    Returns a partition (A,B) or None (complete search)."""
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    n = len(nodes)
    pos = {v: i for i, v in enumerate(nodes)}
    adj = [[pos[u] for u in G.neighbors(v)] for v in nodes]
    color = [-1] * n
    parent = [list(range(n)), list(range(n))]  # per color union-find

    def find(c, x):
        p = parent[c]
        while p[x] != x:
            x = p[x]
        return x

    def rec(i):
        if i == n:
            return True
        v = i
        for c in (0, 1) if i > 0 else (0,):  # fix color of first vertex (symmetry)
            nbrs_same = [u for u in adj[v] if color[u] == c]
            roots = [find(c, u) for u in nbrs_same]
            if len(set(roots)) == len(roots):
                saved = [(r, parent[c][r]) for r in roots]
                for r in roots:
                    parent[c][r] = v
                color[v] = c
                if rec(i + 1):
                    return True
                color[v] = -1
                for r, p in reversed(saved):
                    parent[c][r] = p
                parent[c][v] = v
        return False

    if rec(0):
        A = [nodes[i] for i in range(n) if color[i] == 0]
        B = [nodes[i] for i in range(n) if color[i] == 1]
        return A, B
    return None


# ------------------------------------------- (F) LP column generation for va_f
def va_f_lp(G):
    from scipy.optimize import linprog

    nodes = sorted(G.nodes())
    n = len(nodes)
    vi = {v: i for i, v in enumerate(nodes)}
    # start with singleton forests
    cols = [frozenset([v]) for v in nodes]
    colset = set(cols)
    it = 0
    while True:
        it += 1
        # master: min sum x_F  s.t.  sum_{F ni v} x_F >= 1, x >= 0
        A_ub = []
        for i, v in enumerate(nodes):
            row = [-1.0 if v in F else 0.0 for F in cols]
            A_ub.append(row)
        b_ub = [-1.0] * n
        c = [1.0] * len(cols)
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, None), method="highs")
        assert res.status == 0, res.message
        primal = res.fun
        duals = [-y for y in res.ineqlin.marginals]  # y_v >= 0
        # pricing: max-weight induced forest under weights y
        wt = {v: max(duals[vi[v]], 0.0) for v in nodes}
        val, S, _ = max_weight_induced_forest(G, wt)
        if val <= 1.0 + 1e-9:
            # dual feasible (up to tol): va_f >= sum duals; primal = upper bound
            return primal, sum(duals), cols, it
        F = frozenset(S)
        if F in colset:
            # numerical stall; perturb by returning current bounds
            return primal, None, cols, it
        cols.append(F)
        colset.add(F)


def main():
    t0 = time.time()
    H, emb = check_tutte_graph()

    print("(B) exhaustive Hamiltonian-cycle search on Tutte graph ...")
    t = time.time()
    ham, nodes_searched = is_hamiltonian(H)
    print(f"(B) Hamiltonian cycle exists: {ham}  "
          f"(search nodes: {nodes_searched}, {time.time()-t:.1f}s)")
    assert ham is False, "FATAL: Tutte graph claimed non-Hamiltonian!"

    # sanity: the searcher does find Ham cycles when they exist
    for name, K in [("dodecahedron", nx.dodecahedral_graph()),
                    ("K4", nx.complete_graph(4)),
                    ("3-prism", nx.circular_ladder_graph(3))]:
        h, _ = is_hamiltonian(K)
        assert h is True, f"searcher failed to find Ham cycle in {name}"
    print("(B) sanity: searcher finds Hamiltonian cycles in dodecahedron/K4/prism: OK")
    # and correctly rejects a small non-Hamiltonian cubic graph: K_{3,3} minus a
    # perfect matching is a 6-cycle (Hamiltonian) -- use the Petersen graph
    # (non-Hamiltonian, cubic) instead.
    h, _ = is_hamiltonian(nx.petersen_graph())
    assert h is False, "searcher wrongly found Ham cycle in Petersen graph"
    print("(B) sanity: searcher rejects Petersen graph (non-Hamiltonian): OK")

    G, faces = build_dual(H, emb)
    nG, mG = G.number_of_nodes(), G.number_of_edges()
    print(f"(C) dual: {nG} vertices, {mG} edges")
    assert nG == 25 and mG == 69
    assert nx.check_planarity(G)[0]
    assert min(d for _, d in G.degree()) >= 3
    assert mG == 3 * nG - 6, "not a triangulation edge count"
    # faces of H have length = degree of the corresponding dual vertex (>=4 here);
    # the DUAL's faces are triangles because H is cubic.  A simple planar graph
    # with exactly 3n-6 edges is maximal planar, i.e. a triangulation:
    # verify triangular faces of G directly from an embedding of G.
    okG, embG = nx.check_planarity(G)
    assert okG
    seenG = set()
    for u in G:
        for v in embG.neighbors_cw_order(u):
            if (u, v) not in seenG:
                fc = embG.traverse_face(u, v, mark_half_edges=seenG)
                assert len(fc) == 3, f"non-triangular face {fc} in dual"
    degs = sorted(d for _, d in G.degree())
    print(f"(C) dual degree sequence: {degs}")
    Wtot = sum(d - 2 for _, d in G.degree())
    print(f"(C) sum of (d(v)-2) = {Wtot} (writeup says 88)")
    assert Wtot == 88

    print("(D) exhaustive max-weight induced forest, weights d(v)-2 ...")
    t = time.time()
    wdict = {v: G.degree(v) - 2 for v in G.nodes()}
    M, S, cnt = max_weight_induced_forest(G, wdict)
    assert check_forest(G, S)
    assert sum(wdict[v] for v in S) == M
    print(f"(D) M = max_F w(F) = {M}  (writeup needs <= 43; 2n-6 = 44) "
          f"[B&B nodes {cnt}, {time.time()-t:.1f}s]")
    print(f"(D) an optimal forest ({len(S)} vertices): {sorted(S)}")

    t = time.time()
    aG, Sa, cnta = max_weight_induced_forest(G, {v: 1 for v in G.nodes()})
    assert check_forest(G, Sa)
    print(f"(D) a(G) = max induced forest size = {aG}  "
          f"[B&B nodes {cnta}, {time.time()-t:.1f}s]  n/a(G) = {25/aG:.4f}")

    print("(E) exhaustive search for partition into two induced forests ...")
    t = time.time()
    part = two_forest_partition(G)
    print(f"(E) two-induced-forest partition exists: {part is not None} "
          f"({time.time()-t:.1f}s)")
    if part is not None:
        A, B = part
        print("    A =", sorted(A))
        print("    B =", sorted(B))
        assert check_forest(G, A) and check_forest(G, B)

    print("(F) LP column generation for va_f(G) ...")
    t = time.time()
    primal, dualbound, cols, iters = va_f_lp(G)
    print(f"(F) LP va_f(G): primal (upper bd) = {primal:.6f}, "
          f"verified dual (lower bd) = {dualbound}, "
          f"iters = {iters}, columns = {len(cols)} ({time.time()-t:.1f}s)")
    print(f"(F) writeup's claimed lower bound 88/43 = {88/43:.6f}")

    # explicit check of the writeup's dual certificate:
    ok_cert = (M <= 43)
    print(f"Writeup's certificate z_v=(d(v)-2)/43 feasible (i.e. M<=43): {ok_cert}")
    print(f"total time {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
