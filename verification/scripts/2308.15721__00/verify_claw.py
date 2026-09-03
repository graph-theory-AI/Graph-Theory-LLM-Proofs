"""Independent verification for referee report 2308.15721__00.

Checks, by brute force:
  A. connected tree-depth (vertex-height convention of the paper) of K_{1,3} is 2.
  B. On all graphs with <= 6 vertices: G has an odd K_{1,3}-minor  <=>  Delta(G) >= 3.
     (Generic odd-minor checker following the paper's definition: an odd H-model is a
      collection of pairwise disjoint subtrees T_x plus a 2-colouring c of G<H> such
      that each T_x is properly 2-coloured by c and for each edge xy of H there is a
      monochromatic edge of G between T_x and T_y.)
  C. Every connected graph with Delta <= 2 (paths P_n, cycles C_n, n <= 12) admits a
     2-colouring with every monochromatic component of order <= 2; and the 1-colouring
     of P_n has a monochromatic component of order n (so clustering is unbounded with
     one colour).
"""
import itertools
import networkx as nx

# ---------- A. connected tree-depth of K_{1,3} ----------
def vertex_height(T, root):
    # max number of vertices on a root-to-leaf path
    depths = nx.single_source_shortest_path_length(T, root)
    return 1 + max(depths.values())

def closure_contains(T, root, G):
    # closure: uv edge iff u is a descendant of v or vice versa (u on root-path of v)
    paths = nx.single_source_shortest_path(T, root)
    anc = {v: set(paths[v]) for v in T}
    for u, v in G.edges():
        if v not in anc[u] and u not in anc[v]:
            return False
    return True

def connected_treedepth(G):
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    best = n
    # enumerate labelled trees on V(G) via Pruefer sequences, plus all roots
    if n == 1:
        return 1
    if n == 2:
        seqs = [()]
    else:
        seqs = itertools.product(nodes, repeat=n - 2)
    for seq in seqs:
        T = nx.from_prufer_sequence(list(seq)) if n > 2 else nx.path_graph(2)
        if n > 2:
            T = nx.relabel_nodes(T, dict(enumerate(nodes)))
        for root in nodes:
            if closure_contains(T, root, G):
                best = min(best, vertex_height(T, root))
    return best

claw = nx.star_graph(3)  # K_{1,3}: center 0, leaves 1,2,3
td_claw = connected_treedepth(claw)
print("A. connected tree-depth of K_{1,3} (vertex-height convention):", td_claw)
assert td_claw == 2

# ---------- B. odd K_{1,3}-minor <=> max degree >= 3, all graphs n <= 6 ----------
def connected_subsets(G, verts):
    n = len(verts)
    for r in range(1, n + 1):
        for S in itertools.combinations(verts, r):
            if nx.is_connected(G.subgraph(S)):
                yield frozenset(S)

def has_odd_claw_model(G):
    """Generic check for an odd K_{1,3}-model in G (H = claw, center h0, leaves h1..h3)."""
    V = list(G.nodes())
    subs = list(connected_subsets(G, V))
    for Sc in subs:  # branch set of the center
        rest = [S for S in subs if not (S & Sc)]
        for S1, S2, S3 in itertools.combinations(rest, 3):
            if S1 & S2 or S1 & S3 or S2 & S3:
                continue
            sets = [Sc, S1, S2, S3]
            # model needs an edge between Sc and each leaf set
            if not all(any(G.has_edge(u, v) for u in Sc for v in Si)
                       for Si in (S1, S2, S3)):
                continue
            # choose spanning trees and a 2-colouring of the model's vertices
            model_vertices = sorted(set().union(*sets))
            trees = []
            ok_trees = True
            for S in sets:
                sub = G.subgraph(S)
                trees.append(list(nx.minimum_spanning_edges(sub, data=False))
                             if len(S) > 1 else [])
            # enumerate 2-colourings of model vertices (fix nothing; 2^{|V|} small)
            for bits in itertools.product((0, 1), repeat=len(model_vertices)):
                col = dict(zip(model_vertices, bits))
                # each spanning tree properly 2-coloured?
                # NOTE: properness must hold on SOME subtree; a spanning tree of S is
                # one candidate. To be exhaustive we require properness on all edges of
                # a chosen spanning tree only. For a fully general check we would try
                # all spanning trees; for the claw with small sets, if any proper
                # 2-colouring of some spanning tree works it works for a BFS tree of a
                # bipartition, so we instead test: colouring restricted to S is a
                # proper 2-colouring of SOME spanning tree of G[S]. That holds iff the
                # two colour classes partition S with the bipartite "cross" edges of
                # G[S] connecting S (i.e., the cross-edge subgraph of G[S] is
                # connected and spans S).
                good = True
                for S in sets:
                    if len(S) == 1:
                        continue
                    cross = nx.Graph()
                    cross.add_nodes_from(S)
                    for u, v in G.subgraph(S).edges():
                        if col[u] != col[v]:
                            cross.add_edge(u, v)
                    if not nx.is_connected(cross):
                        good = False
                        break
                if not good:
                    continue
                # monochromatic edge between Sc and each leaf set?
                if all(any(G.has_edge(u, v) and col[u] == col[v]
                           for u in Sc for v in Si) for Si in (S1, S2, S3)):
                    return True
    return False

import networkx.generators.atlas as atlas_mod
count = mismatches = 0
for G in nx.graph_atlas_g()[1:]:  # all graphs up to 7 vertices; keep n<=6 for speed
    if G.number_of_nodes() > 6:
        break
    if G.number_of_nodes() == 0:
        continue
    count += 1
    deg3 = max((d for _, d in G.degree()), default=0) >= 3
    odd = has_odd_claw_model(G)
    if deg3 != odd:
        mismatches += 1
        print("MISMATCH:", G.number_of_nodes(), sorted(G.edges()), "deg>=3:", deg3, "oddclaw:", odd)
print(f"B. checked {count} graphs (n<=6): odd K_1,3-minor <=> Delta>=3 ; mismatches = {mismatches}")
assert mismatches == 0

# ---------- C. clustering for Delta<=2 graphs ----------
def min_clustering_with_k_colours(G, k):
    best = None
    V = list(G.nodes())
    for colouring in itertools.product(range(k), repeat=len(V)):
        col = dict(zip(V, colouring))
        worst = 0
        for c in range(k):
            sub = G.subgraph([v for v in V if col[v] == c])
            if sub.number_of_nodes():
                worst = max(worst, max(len(cc) for cc in nx.connected_components(sub)))
        best = worst if best is None else min(best, worst)
    return best

for n in range(2, 13):
    P = nx.path_graph(n)
    C = nx.cycle_graph(n) if n >= 3 else None
    p2 = min_clustering_with_k_colours(P, 2)
    p1 = min_clustering_with_k_colours(P, 1)
    line = f"C. n={n}: P_n 1-col clustering={p1}, 2-col clustering={p2}"
    assert p1 == n and p2 <= 2
    if C is not None:
        c2 = min_clustering_with_k_colours(C, 2)
        line += f"; C_n 2-col clustering={c2}"
        assert c2 <= 2
    print(line)

print("All checks passed.")
