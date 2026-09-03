"""Check 4: end-to-end simulation of the writeup's algorithm (Sections 5-7).

Pipeline implemented exactly as in the writeup, with core radius rho:
  - candidate core C_x = {canonical low-degree vertex in B_rho(x)} if one
    exists, else the ball G[B_rho(x)] (then it must be non-Gallai: asserted);
  - X = maximal independent set of G^{2 rho + 1} (randomized greedy MIS);
  - S = union of selected cores; layers V_i by distance to S, colored in
    DECREASING distance order with the Lemma-1 randomized subroutine
    (entry condition |A(v)| >= d_{G[V_i]}(v) + 1 asserted for every vertex);
  - nonsingleton cores: assert residual lists |A_C(v)| >= d_C(v), assert the
    core is connected and not a Gallai tree, and color it by backtracking
    (must succeed, per the degree-choosability theorem);
  - singleton cores: assert a free color remains.

Two radius regimes per instance:
  (a) faithful R = 2 ceil(log2(n+1)) + 3 (at these n, cores are large);
  (b) tight rho = max_x (minimal radius where Lemma 2's disjunction holds),
      which exercises the separation / layering machinery nontrivially.
      This is sound because the disjunction is monotone in the radius
      (blocks are induced, so a non-Gallai ball stays non-Gallai).

Instances: random 3/4-regular graphs, G(n,p), torus, hypercubes, Petersen,
triangle trees, a disconnected instance; lists of size exactly Delta:
identical {0..Delta-1} (the hard case), or random from universes of size
Delta+1 and 2*Delta. Every run must end in a proper coloring from the lists.
"""
import math
import random
import sys

import networkx as nx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import is_gallai_tree, ball, list_colorable, random_regular_connected

rng = random.Random(31337)


def lemma1_color(G, layer, A, color):
    """Randomized slack coloring of G[layer] given current lists A (mutated).
    Asserts the entry condition. Returns rounds used."""
    layer = set(layer)
    for v in layer:
        d0 = sum(1 for u in G[v] if u in layer)
        assert len(A[v]) >= d0 + 1, "layer entry condition violated"
    uncolored = set(layer)
    rounds = 0
    while uncolored:
        rounds += 1
        active = {v for v in uncolored if rng.random() < 0.5}
        pick = {v: rng.choice(sorted(A[v])) for v in active}
        committed = [v for v in active
                     if all(pick.get(u) != pick[v]
                            for u in G[v] if u in active)]
        for v in committed:
            color[v] = pick[v]
            uncolored.discard(v)
        for v in committed:
            for u in G[v]:
                if u in A and u != v and color.get(u) is None:
                    A[u].discard(color[v])
        assert rounds < 10000
    return rounds


def run_algorithm(G, Delta, lists, rho):
    n = G.number_of_nodes()
    # candidate cores
    cores = {}
    for x in G:
        B = ball(G, x, rho)
        low = sorted(z for z in B if G.degree(z) < Delta)
        if low:
            cores[x] = {low[0]}
        else:
            H = G.subgraph(B)
            assert nx.is_connected(H)
            assert not is_gallai_tree(H), "Lemma 2 violated at core construction"
            cores[x] = set(B)
    # MIS of G^q, q = 2 rho + 1 (randomized greedy)
    q = 2 * rho + 1
    order = list(G.nodes())
    rng.shuffle(order)
    X = []
    for v in order:
        if all(nx.shortest_path_length(G, v, x) > q if nx.has_path(G, v, x)
               else True for x in X):
            X.append(v)
    # separation check
    for i, x in enumerate(X):
        for y in X[i + 1:]:
            if nx.has_path(G, x, y):
                dxy = nx.shortest_path_length(G, x, y)
                assert dxy >= q + 1
    S = set().union(*(cores[x] for x in X))
    # cores pairwise at distance >= 2
    for i, x in enumerate(X):
        for y in X[i + 1:]:
            for u in cores[x]:
                for w in cores[y]:
                    assert u != w and not G.has_edge(u, w)
    # layers
    dist = {}
    for v in G:
        dv = min((nx.shortest_path_length(G, v, s) for s in S
                  if nx.has_path(G, v, s)), default=None)
        assert dv is not None, "domination failed"
        dist[v] = dv
    D = max(dist.values())
    assert D <= q + rho, "domination bound violated"
    color = {v: None for v in G}
    A = {v: set(lists[v]) for v in G}
    total_rounds = 0
    for i in range(D, 0, -1):
        layer = [v for v in G if dist[v] == i and v not in S]
        if layer:
            total_rounds += lemma1_color(G, layer, A, color)
    # cores
    for x in X:
        C = cores[x]
        if len(C) == 1:
            (z,) = C
            avail = set(lists[z]) - {color[u] for u in G[z] if color[u] is not None}
            assert avail, "singleton core has no free color"
            color[z] = min(avail)
        else:
            H = G.subgraph(C)
            res = {}
            for v in C:
                res[v] = set(lists[v]) - {color[u] for u in G[v]
                                          if u not in C and color[u] is not None}
                assert len(res[v]) >= H.degree(v), "core residual list too small"
            sol = list_colorable(H, {v: sorted(res[v]) for v in C})
            assert sol is not None, "DEGREE-CHOOSABLE CORE NOT COLORABLE (fatal)"
            for v, c in sol.items():
                color[v] = c
    # final verification
    for v in G:
        assert color[v] is not None and color[v] in set(lists[v])
        for u in G[v]:
            assert color[u] != color[v]
    return total_rounds, len(X), D


def min_disjunction_radius(G, x, Delta, rmax):
    for r in range(rmax + 1):
        B = ball(G, x, r)
        if any(G.degree(z) < Delta for z in B):
            return r
        if not is_gallai_tree(G.subgraph(B)):
            return r
    raise AssertionError("Lemma 2 violated")


def make_lists(G, Delta, mode):
    if mode == "identical":
        return {v: list(range(Delta)) for v in G}
    U = list(range(Delta + 1 if mode == "small" else 2 * Delta))
    return {v: rng.sample(U, Delta) for v in G}


def instances():
    for Delta, ns in ((3, (10, 16, 24, 32)), (4, (10, 15, 25, 35))):
        for n in ns:
            if (n * Delta) % 2:
                continue
            for _ in range(6):
                G = random_regular_connected(n, Delta, rng)
                if G is not None:
                    yield f"{Delta}-regular n={n}", G, Delta
    for _ in range(10):
        n = rng.randrange(15, 40)
        G = nx.gnp_random_graph(n, 3.0 / n, seed=rng.randrange(10**9))
        G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
        G = nx.convert_node_labels_to_integers(G)
        Delta = max(d for _, d in G.degree())
        if Delta >= 3 and not (G.number_of_nodes() == Delta + 1
                               and G.number_of_edges() == Delta * (Delta + 1) // 2):
            yield f"gnp n={G.number_of_nodes()} Delta={Delta}", G, Delta
    yield "torus 4x4", nx.convert_node_labels_to_integers(
        nx.grid_2d_graph(4, 4, periodic=True)), 4
    yield "Q3", nx.convert_node_labels_to_integers(nx.hypercube_graph(3)), 3
    yield "Q4", nx.convert_node_labels_to_integers(nx.hypercube_graph(4)), 4
    yield "Petersen", nx.petersen_graph(), 3
    # disconnected: two 3-regular components
    G1 = random_regular_connected(10, 3, rng)
    G2 = random_regular_connected(14, 3, rng)
    if G1 and G2:
        yield "disconnected 3-reg", nx.disjoint_union(G1, G2), 3
    # triangle tree fragment (many low-degree vertices)
    from check3_lemma2 import triangle_tree
    yield "triangle-tree d=3", triangle_tree(3), 3


def main():
    count = 0
    for name, G, Delta in instances():
        n = G.number_of_nodes()
        R = 2 * math.ceil(math.log2(n + 1)) + 3
        rho_tight = max(min_disjunction_radius(G, x, Delta, R) for x in G)
        for mode in ("identical", "small", "wide"):
            lists = make_lists(G, Delta, mode)
            for rho in {R, rho_tight}:
                rounds, nx_cores, D = run_algorithm(G, Delta, lists, rho)
                count += 1
    print(f"CHECK 4 PASSED: {count} full-pipeline runs, "
          f"every run produced a proper coloring from the Delta-lists")


if __name__ == "__main__":
    main()
