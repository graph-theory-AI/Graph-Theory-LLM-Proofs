"""Structural checks on the claimed 8-vertex counterexample G.

G: B = {b1..b4} induces K4; S = {s1..s4} independent; s_i ~ B \ {b_i}.
"""
import itertools, networkx as nx, numpy as np

B = [f"b{i}" for i in range(1, 5)]
S = [f"s{i}" for i in range(1, 5)]
G = nx.Graph()
G.add_nodes_from(B + S)
G.add_edges_from(itertools.combinations(B, 2))
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            G.add_edge(f"s{i}", f"b{j}")

print("n =", G.number_of_nodes(), " m =", G.number_of_edges())
print("degrees:", dict(G.degree()))
print("cycle space dim =", G.number_of_edges() - G.number_of_nodes() + nx.number_connected_components(G))
print("connectivity =", nx.node_connectivity(G))
print("planar =", nx.check_planarity(G)[0])
print("iso to triakis-tetrahedron-ish? complement:", nx.to_dict_of_lists(nx.complement(G)))

cycles = [c for c in nx.simple_cycles(G)]   # vertex lists
print("total simple cycles:", len(cycles))
from collections import Counter
print("cycle length distribution:", Counter(len(c) for c in cycles))

def induced(c):
    return G.subgraph(c).number_of_edges() == len(c)

def peripheral(c):
    if not induced(c):
        return False
    H = G.copy(); H.remove_nodes_from(c)
    return H.number_of_nodes() > 0 and nx.is_connected(H)

ind = [c for c in cycles if induced(c)]
per = [c for c in cycles if peripheral(c)]
print("induced cycles:", len(ind), "lengths:", Counter(len(c) for c in ind))
print("peripheral cycles:", len(per))
for c in sorted(per, key=str):
    print("   peripheral:", sorted(c))
nonper_induced = [c for c in ind if not peripheral(c)]
print("induced but NOT peripheral:", [sorted(c) for c in nonper_induced])

# rank of peripheral cycles in GF(2) cycle space
edges = sorted(tuple(sorted(e)) for e in G.edges())
eidx = {e: k for k, e in enumerate(edges)}
def vec(c):
    v = np.zeros(len(edges), dtype=np.int8)
    for a, b in zip(c, c[1:] + c[:1]):
        v[eidx[tuple(sorted((a, b)))]] ^= 1
    return v
def gf2_rank(M):
    M = M.copy() % 2; r = 0
    for col in range(M.shape[1]):
        piv = None
        for i in range(r, M.shape[0]):
            if M[i, col]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(M.shape[0]):
            if i != r and M[i, col]: M[i] ^= M[r]
        r += 1
    return r
P = np.array([vec(c) for c in per])
print("GF(2) rank of the peripheral cycles:", gf2_rank(P), "of", len(edges) - G.number_of_nodes() + 1)
# rank after deleting any two peripheral cycles
worst = max(gf2_rank(np.delete(P, [i, j], axis=0)) for i, j in itertools.combinations(range(len(per)), 2))
print("max rank of any 10 of the 12 peripheral cycles:", worst)
