"""Verification for 2511.02892__03 (strong edge coloring of diamond-free claw-free cubic graphs).

Checks the writeup's claims about the triangular prism P:
  1. P is cubic, claw-free, diamond-free (both induced- and subgraph-sense).
  2. L(P)^2 = K_9, hence chi'_s(P) = 9 (also confirmed by direct exact computation).
  3. T(G0) for the 3-dipole multigraph (two vertices, three parallel edges) is isomorphic to P.
"""
import itertools
import networkx as nx

# --- Triangular prism ---
P = nx.Graph()
for i in (1, 2, 3):
    j = i % 3 + 1
    P.add_edge(f"a{i}", f"a{j}")
    P.add_edge(f"b{i}", f"b{j}")
    P.add_edge(f"a{i}", f"b{i}")

assert P.number_of_nodes() == 6 and P.number_of_edges() == 9
print("cubic:", all(d == 3 for _, d in P.degree()))

# claw-free: no induced K_{1,3}
def has_induced(G, H):
    return any(nx.is_isomorphic(G.subgraph(S), H)
               for S in itertools.combinations(G.nodes(), H.number_of_nodes()))

claw = nx.star_graph(3)
diamond = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])
print("claw-free (induced):", not has_induced(P, claw))
print("diamond-free (induced):", not has_induced(P, diamond))

# diamond-free even as a (not nec. induced) subgraph: no two triangles share an edge
tris = [set(t) for t in itertools.combinations(P.nodes(), 3)
        if all(P.has_edge(x, y) for x, y in itertools.combinations(t, 2))]
print("triangles of P:", tris)
share = any(len(t1 & t2) >= 2 for t1, t2 in itertools.combinations(tris, 2))
print("diamond-free (subgraph sense, no two triangles share an edge):", not share)

# --- L(P)^2 = K_9 ---
L = nx.line_graph(P)
L2 = nx.power(L, 2)
print("L(P)^2 is K_9:", L2.number_of_nodes() == 9 and
      L2.number_of_edges() == 36)

# direct check: every pair of distinct edges of P "conflicts"
# (shares an endpoint or some edge of P joins their endpoints)
def conflict(e, f):
    e, f = set(e), set(f)
    if e & f:
        return True
    return any(P.has_edge(x, y) for x in e for y in f)

pairs = list(itertools.combinations(P.edges(), 2))
print("all", len(pairs), "edge pairs conflict:", all(conflict(e, f) for e, f in pairs))

# exact strong chromatic index by brute force (greedy over color counts)
def strong_chromatic_index(G):
    E = list(G.edges())
    m = len(E)
    conf = [[False] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i != j:
                e, f = set(E[i]), set(E[j])
                conf[i][j] = bool(e & f) or any(G.has_edge(x, y) for x in e for y in f)
    for k in range(1, m + 1):
        col = [None] * m

        def bt(i):
            if i == m:
                return True
            used = {col[j] for j in range(m) if conf[i][j] and col[j] is not None}
            for c in range(k):
                if c not in used:
                    col[i] = c
                    if bt(i + 1):
                        return True
                    col[i] = None
                if c > max((x for x in col[:i] if x is not None), default=-1):
                    break  # symmetry: first unused color only once
            return False

        if bt(0):
            return k
    return None

print("chi'_s(P) =", strong_chromatic_index(P))

# --- T(G0) for G0 = two vertices joined by three parallel edges ---
# Truncation: replace each vertex by a triangle, one triangle vertex per incident
# edge; join the two incidence vertices of each original edge.
TG0 = nx.Graph()
# vertex u -> triangle u0,u1,u2 (incidence vertices for parallel edges 0,1,2); same for v
for x in ("u", "v"):
    for i, j in itertools.combinations(range(3), 2):
        TG0.add_edge(f"{x}{i}", f"{x}{j}")
for i in range(3):
    TG0.add_edge(f"u{i}", f"v{i}")
print("T(G0) isomorphic to prism:", nx.is_isomorphic(TG0, P))
