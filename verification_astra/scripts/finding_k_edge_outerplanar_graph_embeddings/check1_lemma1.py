"""Check 1: sanity of the machinery + Lemma 1 (layer(e) = 1 + min dual dist)."""
import itertools, random
import networkx as nx
from pl import Graph, embeddings, min_edge_outerplanarity

def from_nx(G):
    vs = sorted(G.nodes()); idx = {v: i for i, v in enumerate(vs)}
    return Graph(len(vs), [(idx[u], idx[v]) for u, v in G.edges()])

# --- sanity: triangle has 2 faces, K4 has 4
tri = Graph(3, [(0,1),(1,2),(2,0)])
embs = list(embeddings(tri))
print("triangle: #genus0 rotation systems =", len(embs), " faces:", [e.nf for e in embs])
print("triangle min edge-outerplanarity:", min_edge_outerplanarity(tri))

k4 = from_nx(nx.complete_graph(4))
print("K4: min edge-outerplanarity =", min_edge_outerplanarity(k4))
k5m = nx.complete_graph(5); k5m.remove_edge(3,4)
print("K5-e: min edge-outerplanarity =", min_edge_outerplanarity(from_nx(k5m)))

# --- Lemma 1 on many random connected planar graphs, ALL embeddings, ALL outer faces
random.seed(11)
tested = 0; bad = 0
graphs = []
while len(graphs) < 40:
    n = random.randint(3, 7)
    p = random.uniform(0.35, 0.8)
    G = nx.gnp_random_graph(n, p, seed=random.randint(0, 10**9))
    if not nx.is_connected(G) or G.number_of_edges() == 0:
        continue
    ok, _ = nx.check_planarity(G)
    if not ok:
        continue
    g = from_nx(G)
    if sum(max(len(g.inc[v])-1,0) for v in range(g.n)) > 14:
        continue
    graphs.append(g)

for g in graphs:
    for emb in embeddings(g):
        for r in range(emb.nf):
            tested += 1
            if emb.K(r) != emb.peel_rounds(r):
                bad += 1
                print("MISMATCH", g.edges, r, emb.K(r), emb.peel_rounds(r))
print(f"Lemma 1: {tested} (embedding,outer face) pairs tested over {len(graphs)} graphs, mismatches = {bad}")

# multigraph + bridge case
mg = Graph(4, [(0,1),(0,1),(1,2),(2,3)])
for emb in embeddings(mg):
    for r in range(emb.nf):
        assert emb.K(r) == emb.peel_rounds(r)
print("multigraph/bridge case OK; min =", min_edge_outerplanarity(mg))
