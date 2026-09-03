#!/usr/bin/env python3
"""Positive certificate of planarity for T (and both amalgam sides minus apex).

Rather than trusting the planarity tester's boolean, extract the combinatorial
embedding it returns and independently verify Euler's formula V - E + F = 2 by
traversing all faces of the embedding. A rotation system whose face count
satisfies Euler's formula on a connected graph is a genus-0 (planar) embedding.
"""
import networkx as nx

def count_faces(emb):
    """Traverse all faces of a PlanarEmbedding via next_face_half_edge."""
    visited = set()
    faces = 0
    for u, v in emb.edges():  # directed half-edges
        if (u, v) in visited:
            continue
        faces += 1
        w, x = u, v
        while True:
            visited.add((w, x))
            w, x = emb.next_face_half_edge(w, x)
            if (w, x) == (u, v):
                break
    return faces

def certify(G, name):
    assert nx.is_connected(G)
    ok, emb = nx.check_planarity(G)
    assert ok, f"{name}: planarity tester says non-planar"
    emb.check_structure()          # validates the rotation system
    V = G.number_of_nodes()
    E = G.number_of_edges()
    F = count_faces(emb)
    print(f"{name}: V={V} E={E} F={F}  V-E+F={V - E + F}")
    assert V - E + F == 2, f"{name}: Euler formula fails -- embedding not planar"

# rebuild T exactly as in build_and_check.py
I = nx.Graph()
A = [f"A{i}" for i in range(5)]; B = [f"B{i}" for i in range(5)]
for i in range(5):
    j = (i + 1) % 5
    I.add_edge("N", A[i]); I.add_edge("S", B[i])
    I.add_edge(A[i], A[j]); I.add_edge(B[i], B[j])
    I.add_edge(A[i], B[i]); I.add_edge(A[j], B[i])
a, b, c, d = "A0", "A1", "N", "B0"
T = I.copy()
T.add_edges_from([("u", a), ("u", b), ("u", c)])
T.add_edges_from([("v", a), ("v", b), ("v", d)])
T.remove_edge(a, b); T.add_edge("u", "v")
T.add_edges_from([("x", a), ("x", "u"), ("x", "v")])

certify(I, "icosahedron I")
certify(T, "T (15 vertices)")
print("Planarity of T certified via explicit embedding + Euler's formula.")
print("Hence (Wagner): T has no K5 minor; so P = T + apex(z) has no K6 minor.")
