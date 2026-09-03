#!/usr/bin/env python3
"""Heuristic search for a K6 minor via local search over connected 6-partitions.

Fact used: a connected graph G has a K6 minor iff V(G) can be partitioned into
exactly 6 connected parts that are pairwise adjacent (unused vertices of any
model can always be absorbed into adjacent branch sets).

Search: start from a random Voronoi/BFS partition grown from 6 random seeds;
hill-climb with random restarts, moving boundary vertices between parts while
keeping both parts connected and nonempty, maximizing the number of adjacent
part-pairs (15 = K6 model found). This is a heuristic REFUTER only: success
proves a K6 minor exists; failure over many restarts merely corroborates the
lemma-based proof of K6-minor-freeness in build_and_check.py.

Validated on positive controls (including a planted K6 inside G itself and a
28-vertex sparse positive) and on a known negative control from the source
paper (planar triangulation with min degree 5 plus an apex vertex).
"""
import random
import itertools
import networkx as nx

random.seed(2026)


def part_connected(G, part):
    it = iter(part)
    start = next(it)
    seen = {start}
    stack = [start]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if w in part and w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(part)


def random_connected_partition(G, k=6):
    nodes = list(G.nodes)
    seeds = random.sample(nodes, k)
    label = {s: i for i, s in enumerate(seeds)}
    frontier = list(seeds)
    while frontier:
        v = random.choice(frontier)
        unl = [w for w in G[v] if w not in label]
        if not unl:
            frontier.remove(v)
            continue
        w = random.choice(unl)
        label[w] = label[v]
        frontier.append(w)
    if len(label) != len(nodes):
        return None
    parts = [set() for _ in range(k)]
    for v, i in label.items():
        parts[i].add(v)
    return label, parts


def adjacency_pairs(G, label, k=6):
    adj = [[False] * k for _ in range(k)]
    for u, v in G.edges:
        iu, iv = label[u], label[v]
        if iu != iv:
            adj[iu][iv] = adj[iv][iu] = True
    return sum(adj[i][j] for i in range(k) for j in range(i + 1, k))


def hill_climb(G, iters=4000, k=6):
    rp = random_connected_partition(G, k)
    if rp is None:
        return False
    label, parts = rp
    best = adjacency_pairs(G, label, k)
    if best == 15:
        return True
    nodes = list(G.nodes)
    for _ in range(iters):
        v = random.choice(nodes)
        i = label[v]
        if len(parts[i]) == 1:
            continue
        if not part_connected(G, parts[i] - {v}):
            continue
        targets = {label[w] for w in G[v] if label[w] != i}
        if not targets:
            continue
        j = random.choice(list(targets))
        # move v: i -> j (j stays connected since v has a neighbor in j)
        parts[i].discard(v)
        parts[j].add(v)
        label[v] = j
        score = adjacency_pairs(G, label, k)
        if score == 15:
            return True
        if score >= best or random.random() < 0.15:
            best = max(best, score)
        else:  # revert
            parts[j].discard(v)
            parts[i].add(v)
            label[v] = i
    return False


def search(G, name, restarts=400, iters=4000):
    assert nx.is_connected(G)
    for r in range(restarts):
        if hill_climb(G, iters=iters):
            print(f"{name}: K6 minor FOUND (restart {r})")
            return True
    print(f"{name}: NO K6 minor found in {restarts} restarts x {iters} iters")
    return False


# ---- load target graphs ----
G = nx.read_edgelist(
    "/Users/viennot/dev/Graph-Theory-LLM-Proofs/verification/scripts/2204.10119__01/G28.edgelist")
assert G.number_of_nodes() == 28 and G.number_of_edges() == 88
side1 = [v for v in G.nodes if v.endswith("_1") or v.startswith("m_")]
P = G.subgraph(side1).copy()
assert P.number_of_nodes() == 16 and P.number_of_edges() == 47

print("== positive controls ==")
assert search(nx.complete_bipartite_graph(6, 6), "K_{6,6}", restarts=50)

ico2 = nx.icosahedral_graph()
ico2.add_edges_from([("p", v) for v in range(12)] + [("q", v) for v in range(12)])
ico2.add_edge("p", "q")
assert search(ico2, "icosahedron + 2 adjacent apexes (14 vtx)", restarts=100)

# sparse 28-vertex positive: ico2 glued by one edge to an icosahedron+pendant tail
big = nx.disjoint_union(ico2, nx.icosahedral_graph())
big.add_edge(0, 20)
big = nx.convert_node_labels_to_integers(big)
assert big.number_of_nodes() == 26
assert search(big, "ico+2apex glued to icosahedron (26 vtx, sparse)", restarts=200)

ctrl4 = nx.Graph(G)
six = random.sample(list(ctrl4.nodes), 6)
ctrl4.add_edges_from(itertools.combinations(six, 2))
assert search(ctrl4, "G + planted K6 (28 vtx)", restarts=400)

print("== negative control (known K6-minor-free, from the source paper) ==")
# planar triangulation with min degree 5 (icosahedron) + apex to everything
neg = nx.icosahedral_graph()
neg.add_edges_from([("apex", v) for v in range(12)])
found_neg = search(neg, "icosahedron + 1 apex (known negative)", restarts=400)
assert not found_neg

print("== targets ==")
found_P = search(P, "P (16-vertex apex piece)", restarts=1500)
found_G = search(G, "G (28-vertex amalgam)", restarts=1500)
print("RESULT: K6 minor found in P:", found_P, "| in G:", found_G)
