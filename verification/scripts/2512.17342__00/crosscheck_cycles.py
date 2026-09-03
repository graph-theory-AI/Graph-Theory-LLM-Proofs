#!/usr/bin/env python3
"""
Independent cross-check for the crucial isolation claim of attack 2512.17342__00.

Rebuilds G and phi_c exactly as in verify.py, then enumerates the ENTIRE
cycle space of G (2^20 - 1 nonzero even subgraphs, via fundamental-cycle
XOR over a spanning tree), filters to circuits (connected, 2-regular),
and for each circuit and each a in {1,2,3,4} checks that phi_c + a*chi_C
has a zero edge.  Also reports the circuit count for comparison with the
networkx simple_cycles enumeration in verify.py (235856).
"""

import itertools, sys
import networkx as nx

# ---- rebuild H, c, faces, dual arcs (same code path as verify.py) ----
def icosa():
    E = []
    for i in range(5):
        E += [("t", f"u{i}"), ("b", f"v{i}"),
              (f"u{i}", f"u{(i+1)%5}"), (f"v{i}", f"v{(i+1)%5}"),
              (f"u{i}", f"v{i}"), (f"u{i}", f"v{(i-1)%5}")]
    G = nx.Graph(); G.add_edges_from(E); return G

H0 = icosa()
c0 = {"t": 0, "b": 0}
for i, val in enumerate([1, 2, 1, 3, 4]): c0[f"u{i}"] = val
for i, val in enumerate([3, 4, 2, 1, 2]): c0[f"v{i}"] = val
ident = {"u1-": "t+", "u0-": "u0+", "t-": "u1+"}
pv = lambda x: x + "+"
nv = lambda x: ident.get(x + "-", x + "-")
H = nx.Graph(); cH = {}
for x in H0.nodes(): cH[pv(x)] = c0[x]
for x, y in H0.edges(): H.add_edge(pv(x), pv(y))
for x in H0.nodes(): cH[nv(x)] = (2 - c0[x]) % 5
for x, y in H0.edges(): H.add_edge(nv(x), nv(y))

tris = [frozenset(t) for t in itertools.combinations(sorted(H.nodes()), 3)
        if H.has_edge(t[0], t[1]) and H.has_edge(t[1], t[2]) and H.has_edge(t[0], t[2])]
faces = [t for t in tris if t != frozenset({"t+", "u0+", "u1+"})]
assert len(faces) == 38
edge_faces = {}
for fi, t in enumerate(faces):
    for e in itertools.combinations(sorted(t), 2):
        edge_faces.setdefault(frozenset(e), []).append(fi)

def dedges(tri):
    x, y, z = tri; return [(x, y), (y, z), (z, x)]
orient = {0: tuple(sorted(faces[0]))}
stack = [0]
while stack:
    f = stack.pop()
    for (x, y) in dedges(orient[f]):
        g = [w for w in edge_faces[frozenset((x, y))] if w != f][0]
        gs = sorted(faces[g]); want = None
        for perm in [(gs[0], gs[1], gs[2]), (gs[0], gs[2], gs[1])]:
            if (y, x) in dedges(perm): want = perm
        if g in orient: assert orient[g] == want
        else: orient[g] = want; stack.append(g)

arcs = []          # (tail, head, phi value mod 5)
for e, (f1, f2) in edge_faces.items():
    x, y = tuple(e)
    if (x, y) in dedges(orient[f1]): xx, yy = x, y
    else:
        assert (y, x) in dedges(orient[f1]); xx, yy = y, x
    assert (yy, xx) in dedges(orient[f2])
    arcs.append((f1, f2, (cH[yy] - cH[xx]) % 5))

m = len(arcs); assert m == 57
phi = [a[2] for a in arcs]

# ---- spanning tree, fundamental cycles as edge bitmasks with signs ----
Gd = nx.Graph((a[0], a[1], {"i": i}) for i, a in enumerate(arcs))
assert Gd.number_of_edges() == 57 and Gd.number_of_nodes() == 38
T = nx.bfs_tree(Gd, 0)
tree_edges = set(frozenset(e) for e in T.edges())
tree_idx = [i for i, a in enumerate(arcs) if frozenset((a[0], a[1])) in tree_edges]
non_tree = [i for i in range(m) if i not in tree_idx]
assert len(non_tree) == 20

# path in tree between two vertices
parent = {0: None}
for u, v in T.edges():
    parent[v] = u
def tree_path(u):
    p = []
    while parent[u] is not None:
        p.append(u); u = parent[u]
    p.append(0); return p

eidx = {}
for i, a in enumerate(arcs): eidx[frozenset((a[0], a[1]))] = i

fund = []
for i in non_tree:
    t_, h_ = arcs[i][0], arcs[i][1]
    pu, pv_ = tree_path(t_), tree_path(h_)
    su, sv = set(pu), set(pv_)
    # lowest common ancestor: first vertex of pu in sv
    lca = next(v for v in pu if v in sv)
    cyc_vertices = pu[:pu.index(lca) + 1] + list(reversed(pv_[:pv_.index(lca)]))
    mask = 0
    for j in range(len(cyc_vertices)):
        u, v = cyc_vertices[j], cyc_vertices[(j + 1) % len(cyc_vertices)]
        mask |= 1 << eidx[frozenset((u, v))]
    fund.append(mask)

inc = [0] * 38
for i, a in enumerate(arcs):
    inc[a[0]] |= 1 << i
    inc[a[1]] |= 1 << i
endpoints = [(a[0], a[1]) for a in arcs]

# ---- enumerate cycle space by Gray code, filter circuits, test moves ----
n_even = 0
n_circuits = 0
bad = []
mask = 0
gray_prev = 0
for g in range(1, 1 << 20):
    gray = g ^ (g >> 1)
    mask ^= fund[(gray ^ gray_prev).bit_length() - 1]
    gray_prev = gray
    # 2-regularity: every vertex covered has exactly 2 incident mask edges
    okdeg = True
    verts = []
    mm = mask
    # quick vertex set from edges
    seen = 0
    m2 = mask
    while m2:
        i = (m2 & -m2).bit_length() - 1
        m2 &= m2 - 1
        u, v = endpoints[i]
        seen |= (1 << u) | (1 << v)
    s2 = seen
    while s2:
        vtx = (s2 & -s2).bit_length() - 1
        s2 &= s2 - 1
        if (mask & inc[vtx]).bit_count() != 2:
            okdeg = False
            break
    if not okdeg:
        continue
    n_even += 1
    # connectivity of support: walk from one edge
    i0 = (mask & -mask).bit_length() - 1
    u0 = endpoints[i0][0]
    comp = 0
    frontier = [u0]
    comp |= 1 << u0
    used = 0
    while frontier:
        u = frontier.pop()
        mu = mask & inc[u]
        while mu:
            i = (mu & -mu).bit_length() - 1
            mu &= mu - 1
            a_, b_ = endpoints[i]
            w = b_ if a_ == u else a_
            if not (comp >> w) & 1:
                comp |= 1 << w
                frontier.append(w)
    if comp != seen:
        continue
    n_circuits += 1
    # orient the circuit and test the 4 moves
    # walk: start at u0, follow mask edges
    order = [u0]
    prev_edge = -1
    cur = u0
    while True:
        mu = mask & inc[cur]
        nxt = None
        while mu:
            i = (mu & -mu).bit_length() - 1
            mu &= mu - 1
            if i == prev_edge:
                continue
            a_, b_ = endpoints[i]
            w = b_ if a_ == cur else a_
            nxt = (w, i)
            break
        w, i = nxt
        sgn = +1 if endpoints[i][0] == cur else -1
        order.append((i, sgn))
        prev_edge = i
        cur = w
        if cur == u0:
            break
    signs = order[1:]
    for a in (1, 2, 3, 4):
        if all((phi[i] + a * s) % 5 != 0 for i, s in signs):
            bad.append((mask, a))

print(f"cycle-space elements scanned : {(1 << 20) - 1}")
print(f"2-regular even subgraphs     : {n_even}")
print(f"circuits (simple cycles)     : {n_circuits}   (verify.py/networkx found 235856)")
print(f"valid Z5 moves from phi_c    : {len(bad)}")
print("MATCH" if n_circuits == 235856 else "MISMATCH", "on circuit count;",
      "ISOLATED confirmed" if not bad else f"NOT ISOLATED: {bad[:3]}")
sys.exit(0 if (n_circuits == 235856 and not bad) else 1)
