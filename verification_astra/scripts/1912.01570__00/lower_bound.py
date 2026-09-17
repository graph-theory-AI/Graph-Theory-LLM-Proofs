"""Airtight lower bound fp(G_t) >= t+1: exhibit a concrete planar embedding and read
off t+1 pairwise vertex-disjoint facial triangles from its actual face list."""
import networkx as nx
from build import build, max_disjoint


def faces_of_embedding(emb):
    seen = set()
    faces = []
    for u in emb:
        for v in emb[u]:
            if (u, v) in seen:
                continue
            face = emb.traverse_face(u, v, mark_half_edges=seen)
            faces.append(face)
    return faces


for t in range(1, 7):
    G = build(t)
    ok, emb = nx.check_planarity(G)
    assert ok
    faces = faces_of_embedding(emb)
    V, E = G.number_of_nodes(), G.number_of_edges()
    euler = V - E + len(faces)
    cyc = [frozenset(f) for f in faces if len(set(f)) == len(f) and len(f) >= 3]
    k, wit = max_disjoint(cyc)
    print(f"t={t}: V={V} E={E} F={len(faces)} Euler V-E+F={euler} "
          f"| disjoint facial cycles in THIS embedding: {k} (need >= {t+1})")
    print(f"      witness: {[sorted(c) for c in wit]}")
