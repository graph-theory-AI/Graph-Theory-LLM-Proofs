#!/usr/bin/env python3
"""Independent verification for referee report on 1802.05582__00.

Checks:
  A. Lemma 2: components of G[H] (H = vertices of G-degree >= q) have weak
     diameter in G at most 5n/(q+1) + 4.
  B. Wrapper algorithm (Steps 1-2): on graphs of degeneracy <= q-1 with lists
     of size q, coloring H-components canonically then verifying the residual
     instance on G[L] satisfies |M(v)| >= deg_{G[L]}(v) + 1, and that greedy
     (any order) finishes: final coloring proper and from lists.
  C. Lemma 1 phase simulation: with an arbitrary network decomposition
     (same-color clusters non-adjacent), sequential phase processing with
     per-cluster central greedy succeeds whenever |M(v)| >= deg_F(v)+1.
  D. Balancing arithmetic: min(d^4 log^3 n, 5n/(d+1)+4) <= C n^{4/5} log^{3/5} n
     for all d, and the analogous d^3 S(n) computation.
"""
import itertools
import math
import random

import networkx as nx

random.seed(12345)

# ---------------------------------------------------------------- A: Lemma 2
def check_lemma2(G, qs):
    n = G.number_of_nodes()
    worst = []
    for q in qs:
        H = [v for v in G if G.degree(v) >= q]
        GH = G.subgraph(H)
        bound = 5 * n / (q + 1) + 4
        for comp in nx.connected_components(GH):
            comp = list(comp)
            # weak diameter of comp measured in G
            wd = 0
            for s in comp:
                dist = nx.single_source_shortest_path_length(G, s)
                for t in comp:
                    assert t in dist, "component of G[H] disconnected in G?!"
                    wd = max(wd, dist[t])
            assert wd <= bound, (
                f"LEMMA 2 VIOLATED: n={n} q={q} weak diam {wd} > {bound:.2f}")
            worst.append((wd, bound, q, len(comp)))
    return worst


def lemma2_suite():
    print("== A. Lemma 2 (weak diameter of high-degree components) ==")
    worst_ratio = 0.0
    cases = 0
    graphs = []
    for n, p in [(30, 0.1), (30, 0.3), (60, 0.05), (60, 0.15), (60, 0.4),
                 (100, 0.03), (100, 0.08), (120, 0.02)]:
        for _ in range(5):
            graphs.append(nx.gnp_random_graph(n, p, seed=random.randrange(10**9)))
    # structured adversarial graphs: cliques joined by long paths (high-degree
    # blobs far apart but connected through low-degree threads do NOT form one
    # component of G[H]; also barbell where the path is short)
    graphs.append(nx.barbell_graph(10, 3))
    graphs.append(nx.barbell_graph(8, 0))
    # chain of cliques sharing single vertices: one big H-component
    for k, m in [(5, 8), (10, 5), (4, 20)]:
        Gc = nx.Graph()
        offset = 0
        prev = None
        for _ in range(k):
            nodes = list(range(offset, offset + m))
            Gc.add_edges_from(itertools.combinations(nodes, 2))
            if prev is not None:
                Gc.add_edge(prev, nodes[0])
            prev = nodes[-1]
            offset += m
        graphs.append(Gc)
    # long cycle with hubs
    Gc = nx.cycle_graph(80)
    for h in range(0, 80, 10):
        for j in range(1, 6):
            Gc.add_edge(h, (h + j) % 80)
    graphs.append(Gc)
    # random regular graphs
    for n, d in [(50, 6), (60, 10), (40, 20)]:
        graphs.append(nx.random_regular_graph(d, n, seed=random.randrange(10**9)))
    for G in graphs:
        n = G.number_of_nodes()
        qs = sorted(set([1, 2, 3, 4, 5, 8, max(2, n // 10), max(2, n // 4),
                         max(2, n // 2)]))
        for wd, bound, q, csize in check_lemma2(G, qs):
            cases += 1
            worst_ratio = max(worst_ratio, wd / bound)
    print(f"   checked {len(graphs)} graphs, {cases} (component,q) cases: "
          f"all weak diameters <= 5n/(q+1)+4; worst ratio wd/bound = "
          f"{worst_ratio:.3f}")


# ------------------------------------------------- B: wrapper simulation
def random_degenerate_graph(n, degmax_back):
    """Random graph built by inserting vertices with <= degmax_back back-edges
    => degeneracy <= degmax_back."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for v in range(1, n):
        k = random.randint(0, min(degmax_back, v))
        for u in random.sample(range(v), k):
            G.add_edge(u, v)
    return G


def canonical_component_coloring(G, comp, lists):
    """Central canonical list-coloring of a (q-1)-degenerate component via
    repeated deletion of the min-degree vertex (ties by id), coloring back
    greedily with the smallest available color."""
    sub = G.subgraph(comp).copy()
    order = []
    while sub.number_of_nodes():
        v = min(sub.nodes, key=lambda x: (sub.degree(x), x))
        order.append(v)
        sub.remove_node(v)
    col = {}
    for v in reversed(order):
        used = {col[u] for u in G.neighbors(v) if u in col}
        avail = [c for c in sorted(lists[v]) if c not in used]
        assert avail, "greedy failed on component (degeneracy argument broken)"
        col[v] = avail[0]
    return col


def wrapper_trial(n, q, palette_size):
    G = random_degenerate_graph(n, q - 1)     # degeneracy <= q-1 => mad < 2(q-1)+? ; guarantees greedy q-list-colorability
    lists = {v: set(random.sample(range(palette_size), q)) for v in G}
    H = {v for v in G if G.degree(v) >= q}
    L = set(G) - H
    color = {}
    # Step 1: color components of G[H] centrally & canonically
    for comp in nx.connected_components(G.subgraph(H)):
        color.update(canonical_component_coloring(G, comp, lists))
    # check no conflict inside H (components should be G-nonadjacent)
    for u, v in G.edges():
        if u in H and v in H:
            assert color[u] != color[v], "conflict inside H"
    # Step 2: residual lists on L, check the deg+1 inequality, greedy any order
    GL = G.subgraph(L)
    M = {}
    for v in L:
        used = {color[u] for u in G.neighbors(v) if u in H}
        M[v] = set(lists[v]) - used
        need = GL.degree(v) + 1
        assert len(M[v]) >= q - sum(1 for u in G.neighbors(v) if u in H)
        assert len(M[v]) >= need, (
            f"STEP 2 INEQUALITY VIOLATED: |M(v)|={len(M[v])} < deg+1={need}")
    for v in sorted(L, key=lambda x: random.random()):   # arbitrary order
        used = {color[u] for u in GL.neighbors(v) if u in color}
        avail = sorted(M[v] - used)
        assert avail, "greedy on L failed despite deg+1 lists"
        color[v] = avail[0]
    # final verification
    for v in G:
        assert color[v] in lists[v], "color not from list"
    for u, v in G.edges():
        assert color[u] != color[v], "improper edge"
    return True


def wrapper_suite():
    print("== B. Wrapper algorithm simulation (Steps 1-2) ==")
    trials = 0
    for n, q, pal in [(40, 3, 8), (40, 4, 6), (60, 5, 10), (80, 6, 9),
                      (100, 4, 12), (50, 10, 15), (70, 3, 5), (30, 8, 8)]:
        for _ in range(30):
            wrapper_trial(n, q, pal)
            trials += 1
    print(f"   {trials} random trials: Step-2 inequality always held; final "
          f"coloring always proper and from lists")


# ------------------------------------------------- C: Lemma 1 phase simulation
def lemma1_trial(n, p, extra):
    F = nx.gnp_random_graph(n, p, seed=random.randrange(10**9))
    pal = max(dict(F.degree()).values(), default=0) + 1 + extra + 3
    lists = {v: set(random.sample(range(pal), F.degree(v) + 1 + random.randint(0, extra)))
             for v in F}
    # arbitrary decomposition into connected clusters: BFS-carving
    unassigned = set(F)
    clusters = []
    while unassigned:
        seed_v = min(unassigned)
        size = random.randint(1, 6)
        comp_nodes = []
        frontier = [seed_v]
        seen = {seed_v}
        while frontier and len(comp_nodes) < size:
            v = frontier.pop(0)
            if v in unassigned:
                comp_nodes.append(v)
            for u in F.neighbors(v):
                if u in unassigned and u not in seen:
                    seen.add(u)
                    frontier.append(u)
        clusters.append(comp_nodes)
        unassigned -= set(comp_nodes)
    # cluster graph, properly color it => same-color clusters non-adjacent
    CG = nx.Graph()
    CG.add_nodes_from(range(len(clusters)))
    where = {}
    for i, cl in enumerate(clusters):
        for v in cl:
            where[v] = i
    for u, v in F.edges():
        if where[u] != where[v]:
            CG.add_edge(where[u], where[v])
    ccol = nx.greedy_color(CG)
    ncolors = max(ccol.values(), default=0) + 1
    # phase processing exactly as in Lemma 1's proof
    color = {}
    for phase in range(ncolors):
        for i, cl in enumerate(clusters):
            if ccol[i] != phase:
                continue
            # current lists
            M = {}
            for v in cl:
                used = {color[u] for u in F.neighbors(v) if u in color}
                M[v] = set(lists[v]) - used
                indeg = sum(1 for u in F.neighbors(v) if u in cl)
                assert len(M[v]) >= indeg + 1, (
                    "LEMMA 1 INVARIANT VIOLATED inside cluster")
            # central greedy inside cluster (min-degree-last order)
            sub = F.subgraph(cl).copy()
            order = []
            while sub.number_of_nodes():
                v = min(sub.nodes, key=lambda x: (sub.degree(x), x))
                order.append(v)
                sub.remove_node(v)
            for v in reversed(order):
                used = {color[u] for u in F.neighbors(v) if u in color}
                avail = sorted(set(M[v]) - used)
                assert avail, "cluster greedy failed"
                color[v] = avail[0]
    for v in F:
        assert color[v] in lists[v]
    for u, v in F.edges():
        assert color[u] != color[v]


def lemma1_suite():
    print("== C. Lemma 1 phase-processing simulation ==")
    trials = 0
    for n, p, extra in [(40, 0.1, 0), (40, 0.2, 0), (60, 0.08, 2),
                        (60, 0.15, 0), (80, 0.05, 1)]:
        for _ in range(20):
            lemma1_trial(n, p, extra)
            trials += 1
    print(f"   {trials} trials: invariant |M(v)| >= deg_in_cluster+1 always "
          f"held; phase-greedy always produced a proper list coloring")


# ------------------------------------------------- D: balancing arithmetic
def balancing_suite():
    print("== D. Balancing arithmetic ==")
    bad = 0
    worst = 0.0
    for n in [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**12]:
        ln = math.log(n)
        target = n ** 0.8 * ln ** 0.6
        for d in itertools.chain(range(1, 1000),
                                 (int(n ** (i / 40.0)) for i in range(1, 41))):
            d = max(1, min(d, n))
            best = min(d ** 4 * ln ** 3, 5 * n / (d + 1) + 4 + ln ** 3)
            worst = max(worst, best / target)
            if best > 10 * target:
                bad += 1
        # crossover value D
        D = (n / ln ** 3) ** 0.2
        v1 = D ** 4 * ln ** 3
        assert abs(v1 - target) / target < 1e-9
        assert abs((n / D) - target) / target < 1e-9
    assert bad == 0
    print(f"   min(d^4 log^3 n, 5n/(d+1)+O(polylog)) <= C n^0.8 log^0.6 n for "
          f"all tested (n,d); max ratio to n^0.8 log^0.6 n = {worst:.3f}")
    # alternative d^3 S(n) balancing
    for n in [10**4, 10**6, 10**9]:
        ln = math.log(n)
        S = 2 ** (2 * math.sqrt(math.log2(n)))
        D = (n / S) ** 0.25
        assert abs(D ** 3 * S - n ** 0.75 * S ** 0.25) / (n ** 0.75 * S ** 0.25) < 1e-9
        assert abs(n / D - n ** 0.75 * S ** 0.25) / (n ** 0.75 * S ** 0.25) < 1e-9
    print("   alternative balancing d^3 S(n) vs n/d at D=(n/S)^{1/4}: exponents check out")


if __name__ == "__main__":
    lemma2_suite()
    wrapper_suite()
    lemma1_suite()
    balancing_suite()
    print("ALL CHECKS PASSED")
