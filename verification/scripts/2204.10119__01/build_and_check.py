#!/usr/bin/env python3
"""Independent verification of the construction in attacks/2204.10119__01/output.md.

Builds the claimed 28-vertex graph G (4-clique amalgam of two apex graphs P1, P2)
and checks every claimed property:
  - icosahedron model is correct (12 vertices, 30 edges, 5-regular, planar);
  - abc and abd are faces / triangles as used;
  - T (after the two insertions, the flip, and inserting x) is planar and simple;
  - {x,u,v,a} induces a K4 in T;
  - degree table of P = T + apex z over W;
  - P - z is planar (hypothesis of Lemma 1);
  - the amalgam G: vertex/edge counts, degree sequence, min/max degree,
    connectivity, simplicity;
  - Lemma 2 hypotheses on G: V(P1) cap V(P2) = S, |S| = 4, S is a clique,
    no edges between V(P1)\\S and V(P2)\\S.
"""
import itertools
import networkx as nx

# ---------- icosahedron, standard model from the writeup ----------
I = nx.Graph()
A = [f"A{i}" for i in range(5)]
B = [f"B{i}" for i in range(5)]
I.add_nodes_from(["N", "S"] + A + B)
for i in range(5):
    j = (i + 1) % 5
    I.add_edge("N", A[i])
    I.add_edge("S", B[i])
    I.add_edge(A[i], A[j])
    I.add_edge(B[i], B[j])
    I.add_edge(A[i], B[i])
    I.add_edge(A[j], B[i])

assert I.number_of_nodes() == 12 and I.number_of_edges() == 30
assert all(d == 5 for _, d in I.degree())
planar, _ = nx.check_planarity(I)
assert planar
# sanity: it really is the icosahedral graph
assert nx.is_isomorphic(I, nx.icosahedral_graph())
print("icosahedron model OK (12 vertices, 30 edges, 5-regular, planar, isomorphic)")

a, b, c, d = "A0", "A1", "N", "B0"
# abc and abd are triangles
for tri in [(a, b, c), (a, b, d)]:
    for x_, y_ in itertools.combinations(tri, 2):
        assert I.has_edge(x_, y_), (tri, x_, y_)
W = sorted(set(I.nodes) - {a, b, c, d})
assert len(W) == 8
print("triangles abc, abd OK; |W| =", len(W), W)

# ---------- build T ----------
T = I.copy()
T.add_edges_from([("u", a), ("u", b), ("u", c)])   # insert u in face abc
T.add_edges_from([("v", a), ("v", b), ("v", d)])   # insert v in face abd
T.remove_edge(a, b)                                # flip ab -> uv
T.add_edge("u", "v")
T.add_edges_from([("x", a), ("x", "u"), ("x", "v")])  # insert x in face auv

planarT, embT = nx.check_planarity(T)
assert planarT, "T is NOT planar -- fatal"
assert T.number_of_nodes() == 15
print("T planar OK; |V(T)| =", T.number_of_nodes(), " |E(T)| =", T.number_of_edges())

S0 = ["x", "u", "v", a]
for x_, y_ in itertools.combinations(S0, 2):
    assert T.has_edge(x_, y_), ("missing K4 edge", x_, y_)
print("S0 =", S0, "induces K4 in T: OK")

# claimed degrees in T
claimed_T = {"x": 3, "u": 5, "v": 5, a: 7, b: 6, c: 6, d: 6}
for w in W:
    claimed_T[w] = 5
for vtx, deg in claimed_T.items():
    assert T.degree(vtx) == deg, (vtx, T.degree(vtx), deg)
print("degree table of T matches the writeup")

# ---------- build P = T + apex z over W ----------
P = T.copy()
P.add_edges_from([("z", w) for w in W])
Pm = P.copy(); Pm.remove_node("z")
planarPz, _ = nx.check_planarity(Pm)
assert planarPz, "P - z not planar -- fatal"
claimed_P = dict(claimed_T)
for w in W:
    claimed_P[w] = 6
claimed_P["z"] = 8
for vtx, deg in claimed_P.items():
    assert P.degree(vtx) == deg, (vtx, P.degree(vtx), deg)
assert P.number_of_nodes() == 16 and P.number_of_edges() == 47
print("P built: 16 vertices, 47 edges; P - z planar; degrees match "
      "(W:6, b,c,d:6, z:8, x:3, u,v:5, a:7)")

# ---------- amalgam G of two copies of P over the K4 ----------
# identification: x1=a2, a1=x2, u1=u2, v1=v2
def rename(g, tag):
    return nx.relabel_nodes(g, {v: (v, tag) for v in g.nodes})

P1 = rename(P, 1)
P2 = rename(P, 2)
ident = {  # P2 vertex -> merged name
    ("x", 2): ("x", 1) if False else "m_x1a2",
    (a, 2): "m_a1x2",
    ("u", 2): "m_u",
    ("v", 2): "m_v",
}
merge1 = {("x", 1): "m_x1a2", (a, 1): "m_a1x2", ("u", 1): "m_u", ("v", 1): "m_v"}
P1r = nx.relabel_nodes(P1, merge1)
P2r = nx.relabel_nodes(P2, {("x", 2): "m_a1x2", (a, 2): "m_x1a2",
                            ("u", 2): "m_u", ("v", 2): "m_v"})
G = nx.compose(P1r, P2r)

S = ["m_x1a2", "m_a1x2", "m_u", "m_v"]
# Lemma 2 hypotheses
assert set(P1r.nodes) & set(P2r.nodes) == set(S)
for x_, y_ in itertools.combinations(S, 2):
    assert G.has_edge(x_, y_)
side1 = set(P1r.nodes) - set(S)
side2 = set(P2r.nodes) - set(S)
cross = [(p, q) for p, q in G.edges if (p in side1 and q in side2) or (p in side2 and q in side1)]
assert not cross, cross
print("amalgam hypotheses OK: V(P1) cap V(P2) = S (K4), no cross edges")

# claimed global stats
assert G.number_of_nodes() == 28, G.number_of_nodes()
assert G.number_of_edges() == 88, G.number_of_edges()
degs = sorted(dd for _, dd in G.degree())
from collections import Counter
cnt = Counter(degs)
print("G: n=28? ", G.number_of_nodes() == 28, " m=88? ", G.number_of_edges() == 88)
print("degree distribution:", dict(cnt))
assert cnt == Counter({6: 22, 7: 4, 8: 2}), cnt
assert min(degs) == 6 and max(degs) == 8
assert nx.is_connected(G)
assert all(not G.has_edge(vv, vv) for vv in G.nodes)  # simple (nx.Graph is simple anyway)
print("G connected, simple, degree sequence 6^22 7^4 8^2 : OK")

# identified-vertex degrees
for s in S:
    print("  merged vertex", s, "degree", G.degree(s))

# both sides K6-minor-free by Lemma 1 (apex over planar) -- planarity re-checked per side:
for tag, Pr in [(1, P1r), (2, P2r)]:
    z = ("z", tag)
    Q = Pr.copy(); Q.remove_node(z)
    pl, _ = nx.check_planarity(Q)
    assert pl
print("each side minus its apex vertex is planar: OK (Lemma 1 applies to both)")

G2 = nx.relabel_nodes(G, {v: (v if isinstance(v, str) else f"{v[0]}_{v[1]}") for v in G.nodes})
nx.write_edgelist(G2, "/Users/viennot/dev/Graph-Theory-LLM-Proofs/verification/scripts/2204.10119__01/G28.edgelist", data=False)
print("ALL DETERMINISTIC CHECKS PASSED; G written to G28.edgelist")
