#!/usr/bin/env python3
"""
Referee verification for attack 2512.17342__00.

Claim under review: the writeup constructs a 38-vertex cubic bridgeless planar
graph G (dual of two colored icosahedra glued along a facial triangle) whose
integer nowhere-zero-5-flow reconfiguration graph F(G,5) is disconnected,
via a Z5-flow phi_c that is an isolated vertex of F(G, Z5).

We verify, fully independently:
  A. H0 (claimed icosahedron) is the icosahedral graph; c0 is a proper Z5-coloring.
  B. The writeup's D_1(c0) / D_2(c0) tables and SCC structure.
  C. The glued triangulation H: 21 vertices, 57 edges, simple, planar,
     all 38 faces triangles; induced coloring c proper.
  D. D_a(c) strongly connected for a = 1,2,3,4 (Lemma 2 hypothesis).
  E. Dual graph G: 38 vertices, 57 edges, cubic, simple, planar, 2-edge-connected.
  F. phi_c (dual of the tension of c) is a valid nowhere-zero Z5-flow.
  G. MAIN CHECK (independent of Lemma 2): phi_c is an isolated vertex of
     F(G, Z5): for EVERY simple cycle C of G (enumerated exhaustively) and
     every a in {1,2,3,4}, the flow phi_c + a*chi_C has a zero edge.
  H. The integer lifts f (from representatives of c) and g (from representatives
     of 2c) are valid integer nowhere-zero 5-flows with reductions phi_c and
     2*phi_c respectively, and 2*phi_c != phi_c on every edge.
"""

import itertools
import sys
import networkx as nx

ok = True
def check(name, cond, extra=""):
    global ok
    status = "PASS" if cond else "FAIL"
    if not cond:
        ok = False
    print(f"[{status}] {name} {extra}")

# ---------------------------------------------------------------- A. icosahedron
def icosa():
    V = ["t", "b"] + [f"u{i}" for i in range(5)] + [f"v{i}" for i in range(5)]
    E = []
    for i in range(5):
        E.append(("t", f"u{i}"))
        E.append(("b", f"v{i}"))
        E.append((f"u{i}", f"u{(i+1)%5}"))
        E.append((f"v{i}", f"v{(i+1)%5}"))
        E.append((f"u{i}", f"v{i}"))
        E.append((f"u{i}", f"v{(i-1)%5}"))
    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_edges_from(E)
    return G

H0 = icosa()
check("H0 has 12 vertices, 30 edges", H0.number_of_nodes() == 12 and H0.number_of_edges() == 30)
check("H0 is 5-regular", all(d == 5 for _, d in H0.degree()))
check("H0 is planar", nx.check_planarity(H0)[0])
check("H0 isomorphic to icosahedral graph", nx.is_isomorphic(H0, nx.icosahedral_graph()))

c0 = {"t": 0, "b": 0}
for i, val in enumerate([1, 2, 1, 3, 4]):
    c0[f"u{i}"] = val
for i, val in enumerate([3, 4, 2, 1, 2]):
    c0[f"v{i}"] = val

def is_proper(G, col):
    return all((col[x] - col[y]) % 5 != 0 for x, y in G.edges())

check("c0 is a proper Z5-coloring of H0", is_proper(H0, c0))
check("distinguished triangle t,u0,u1 exists with colors 0,1,2",
      H0.has_edge("t", "u0") and H0.has_edge("t", "u1") and H0.has_edge("u0", "u1")
      and (c0["t"], c0["u0"], c0["u1"]) == (0, 1, 2))

# ------------------------------------------------- B. D_a(c0) tables and SCCs
def D_a(G, col, a):
    D = nx.DiGraph()
    D.add_nodes_from(G.nodes())
    for x, y in G.edges():
        if (col[y] - col[x]) % 5 == a % 5:
            D.add_edge(x, y)
        if (col[x] - col[y]) % 5 == a % 5:
            D.add_edge(y, x)
    return D

D1 = D_a(H0, c0, 1)
D2 = D_a(H0, c0, 2)

# writeup's table of out-neighborhoods
table = {
    "t":  ({"u0", "u2"}, {"u1"}),
    "b":  ({"v3"}, {"v2", "v4"}),
    "u0": ({"u1", "v4"}, {"v0"}),
    "u1": ({"v0"}, {"v1"}),
    "u2": ({"u1", "v2"}, {"u3"}),
    "u3": ({"u4"}, {"t"}),
    "u4": ({"t"}, {"u0", "v3"}),
    "v0": ({"v1"}, {"b"}),
    "v1": ({"b"}, {"u2"}),
    "v2": ({"u3"}, {"v1"}),
    "v3": ({"v2", "v4"}, {"u3"}),
    "v4": ({"v0"}, {"u4"}),
}
tab_ok = all(set(D1.successors(x)) == t1 and set(D2.successors(x)) == t2
             for x, (t1, t2) in table.items())
check("writeup's D_1/D_2 out-neighbor table is exactly correct", tab_ok)
if not tab_ok:
    for x, (t1, t2) in table.items():
        a1, a2 = set(D1.successors(x)), set(D2.successors(x))
        if a1 != t1: print(f"   D1 mismatch at {x}: actual {sorted(a1)} vs table {sorted(t1)}")
        if a2 != t2: print(f"   D2 mismatch at {x}: actual {sorted(a2)} vs table {sorted(t2)}")

check("D_1(c0) strongly connected", nx.is_strongly_connected(D1))
sccs2 = [frozenset(s) for s in nx.strongly_connected_components(D2)]
P = frozenset({"b", "v4", "u4", "u0", "v0"})
Q = frozenset({"t", "u1", "v1", "u2", "u3"})
check("D_2(c0) SCCs are P, Q, {v2}, {v3} as claimed",
      set(sccs2) == {P, Q, frozenset({"v2"}), frozenset({"v3"})})
cond = nx.condensation(D2)
# identify condensation nodes
lab = {}
for n, data in cond.nodes(data=True):
    lab[frozenset(data["members"])] = n
check("condensation arcs: P->{v2}->Q and P->{v3}->Q (P source, Q sink)",
      set(cond.edges()) >= {(lab[P], lab[frozenset({'v2'})]), (lab[frozenset({'v2'})], lab[Q]),
                            (lab[P], lab[frozenset({'v3'})]), (lab[frozenset({'v3'})], lab[Q])}
      and cond.in_degree(lab[P]) == 0 and cond.out_degree(lab[Q]) == 0)

# ---------------------------------------------------------------- C. gluing
# copy +: vertices "x+", coloring c0; copy -: vertices "x-", coloring 2 - c0.
# identify t+ = u1-, u0+ = u0-, u1+ = t-.
ident = {"u1-": "t+", "u0-": "u0+", "t-": "u1+"}
def pv(x): return x + "+"
def nv(x):
    y = x + "-"
    return ident.get(y, y)

H = nx.Graph()
cH = {}
for x in H0.nodes():
    cH[pv(x)] = c0[x]
for x, y in H0.edges():
    H.add_edge(pv(x), pv(y))
for x in H0.nodes():
    xx = nv(x)
    col = (2 - c0[x]) % 5
    if xx in cH:
        check(f"gluing color consistency at {xx}", cH[xx] == col, f"({cH[xx]} vs {col})")
    cH[xx] = col
for x, y in H0.edges():
    H.add_edge(nv(x), nv(y))

check("H has 21 vertices, 57 edges (simple graph, so no multi-edges arose)",
      H.number_of_nodes() == 21 and H.number_of_edges() == 57)
check("induced coloring c on H is proper", is_proper(H, cH))
planar, emb = nx.check_planarity(H)
check("H is planar", planar)

# faces = all triangles of H except the shared (removed) one
tris = [frozenset(t) for t in
        (set(itertools.combinations(sorted(H.nodes()), 3)))
        if H.has_edge(t[0], t[1]) and H.has_edge(t[1], t[2]) and H.has_edge(t[0], t[2])]
shared = frozenset({"t+", "u0+", "u1+"})
check("H has exactly 39 triangles, incl. the shared separating one", len(tris) == 39 and shared in tris)
faces = [t for t in tris if t != shared]
check("38 candidate faces; Euler: 21 - 57 + 38 = 2", len(faces) == 38 and 21 - 57 + 38 == 2)

edge_faces = {}
for fidx, t in enumerate(faces):
    for e in itertools.combinations(sorted(t), 2):
        edge_faces.setdefault(frozenset(e), []).append(fidx)
check("every edge of H lies in exactly 2 faces",
      set(map(frozenset, (frozenset(e) for e in H.edges()))) == set(edge_faces) and
      all(len(v) == 2 for v in edge_faces.values()))

# orient the faces coherently: BFS over dual, adjacent faces must traverse the
# shared edge in opposite directions.  Success <=> these faces give a genus-0
# (orientable, Euler 2) embedding.
orient = {}          # fidx -> tuple(x,y,z) cyclic order
def directed_edges(tri_cycle):
    x, y, z = tri_cycle
    return [(x, y), (y, z), (z, x)]

f0 = 0
orient[f0] = tuple(sorted(faces[f0]))
stack = [f0]
coherent = True
while stack:
    f = stack.pop()
    for (x, y) in directed_edges(orient[f]):
        e = frozenset((x, y))
        g = [w for w in edge_faces[e] if w != f][0]
        # g must traverse (y, x)
        gs = sorted(faces[g])
        want = None
        for perm in [(gs[0], gs[1], gs[2]), (gs[0], gs[2], gs[1])]:
            if (y, x) in directed_edges(perm):
                want = perm
        assert want is not None
        if g in orient:
            if orient[g] != want:
                coherent = False
        else:
            orient[g] = want
            stack.append(g)
check("faces admit a coherent orientation (valid spherical embedding)",
      coherent and len(orient) == 38)

# ------------------------------------------------- D. D_a(c) strong connectivity
for a in (1, 2, 3, 4):
    check(f"D_{a}(c) on glued H is strongly connected",
          nx.is_strongly_connected(D_a(H, cH, a)))

# ---------------------------------------------------------------- E. dual graph G
# dual vertex = face index; for each H-edge {x,y}: the face traversing (x,y)
# is the tail, the face traversing (y,x) is the head; flow value across the
# dual arc = c(y) - c(x)  (tension of the head-side traversal), giving the
# standard tension->flow planar duality.  Conservation then telescopes.
Gd = nx.MultiGraph()
Gd.add_nodes_from(range(38))
arcs = []            # (tail_face, head_face, mod_value, int_value_c, int_value_2c)
for e, (f1, f2) in edge_faces.items():
    x, y = tuple(e)
    if (x, y) in directed_edges(orient[f1]):
        tail, head, (xx, yy) = f1, f2, (x, y)
    else:
        assert (y, x) in directed_edges(orient[f1])
        tail, head, (xx, yy) = f1, f2, (y, x)
    # sanity: the head face must traverse the edge in the opposite direction
    assert (yy, xx) in directed_edges(orient[head])
    mod = (cH[yy] - cH[xx]) % 5
    f_int = cH[yy] - cH[xx]                       # representatives 0..4
    g_int = (2 * cH[yy]) % 5 - (2 * cH[xx]) % 5   # representatives of 2c
    arcs.append((tail, head, mod, f_int, g_int))
    Gd.add_edge(tail, head)

G_simple = nx.Graph(Gd)
check("G has 38 vertices, 57 edges", Gd.number_of_nodes() == 38 and Gd.number_of_edges() == 57)
check("G is simple (no parallel dual edges)", G_simple.number_of_edges() == 57)
check("G is cubic", all(d == 3 for _, d in Gd.degree()))
check("G is planar", nx.check_planarity(G_simple)[0])
check("G is connected", nx.is_connected(G_simple))
check("G is 2-edge-connected (bridgeless)",
      nx.edge_connectivity(G_simple) >= 2)
print(f"       edge connectivity of G = {nx.edge_connectivity(G_simple)}, "
      f"vertex connectivity = {nx.node_connectivity(G_simple)}")

# ------------------------------------------- F. phi_c and the integer lifts f, g
def conserved(values):
    net = {v: 0 for v in range(38)}
    for (t_, h_, *_), val in zip(arcs, values):
        net[t_] += val
        net[h_] -= val
    return net

phi = [a[2] for a in arcs]
f_int = [a[3] for a in arcs]
g_int = [a[4] for a in arcs]

check("phi_c is nowhere-zero mod 5", all(v % 5 != 0 for v in phi))
check("phi_c conservation (mod 5) at every dual vertex",
      all(v % 5 == 0 for v in conserved(phi).values()))
check("integer flow f: values in {-4..-1,1..4}",
      all(v != 0 and -4 <= v <= 4 for v in f_int))
check("integer flow f: exact integer conservation at every vertex",
      all(v == 0 for v in conserved(f_int).values()))
check("integer flow g: values in {-4..-1,1..4}",
      all(v != 0 and -4 <= v <= 4 for v in g_int))
check("integer flow g: exact integer conservation at every vertex",
      all(v == 0 for v in conserved(g_int).values()))
check("f reduces to phi_c mod 5", all((a - b) % 5 == 0 for a, b in zip(f_int, phi)))
check("g reduces to 2*phi_c mod 5", all((a - 2 * b) % 5 == 0 for a, b in zip(g_int, phi)))
check("2*phi_c differs from phi_c on EVERY edge (so f,g reduce differently)",
      all((2 * v - v) % 5 != 0 for v in phi))
check("f != g as integer flows", f_int != g_int)

# ------------------------------------------- G. MAIN: phi_c isolated in F(G,Z5)
# Exhaustively enumerate ALL simple cycles (circuits) of G and check every
# move  phi_c + a*chi_C  (a = 1,2,3,4; one fixed orientation of C suffices
# since the reverse orientation with a is the same as a -> 5-a).
edge_index = {}
for i, (t_, h_, *_ ) in enumerate(arcs):
    edge_index[frozenset((t_, h_))] = i   # G is simple: unique edge per pair

adj = {v: [] for v in range(38)}
for i, (t_, h_, *_ ) in enumerate(arcs):
    adj[t_].append((h_, i, +1))   # traversing tail->head: chi = +1
    adj[h_].append((t_, i, -1))   # traversing head->tail: chi = -1

n_cycles = 0
bad_moves = []
for cyc in nx.simple_cycles(G_simple):
    n_cycles += 1
    k = len(cyc)
    signs = []
    okcyc = True
    for j in range(k):
        u, v = cyc[j], cyc[(j + 1) % k]
        i = edge_index[frozenset((u, v))]
        t_, h_ = arcs[i][0], arcs[i][1]
        s = +1 if (t_, h_) == (u, v) else -1
        signs.append((i, s))
    for a in (1, 2, 3, 4):
        if all((phi[i] + a * s) % 5 != 0 for i, s in signs):
            bad_moves.append((cyc, a))
check(f"isolation of phi_c: NO valid Z5 cycle move exists "
      f"(checked {n_cycles} simple cycles x 4 values of a)", not bad_moves)
if bad_moves:
    print("   counter-moves found:", bad_moves[:5])

print()
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
