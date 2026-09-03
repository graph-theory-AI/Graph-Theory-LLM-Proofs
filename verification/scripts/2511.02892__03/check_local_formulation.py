"""Verification of the writeup's secondary claims for 2511.02892__03:

  A. In T(G), the six "local" edges at each replacement triangle (3 internal +
     3 external) are pairwise conflicting (so any strong coloring is locally rainbow),
     and 6 is a lower bound for chi'_s(T(G)).
  B. The only strong conflicts NOT inside a single local six-edge configuration are
     the cross-triangle pairs {xy,xz} x {x'y',x'z'} across each external edge xx'
     (this is what makes condition (1) of the writeup necessary and sufficient).
  C. The locally-bijective-homomorphism-to-K4 construction yields a valid strong
     6-edge-coloring of T(G); tested on G = K4. Hence chi'_s(T(K4)) = 6.
"""
import itertools
import networkx as nx


def truncation(G):
    """T(G): replace each vertex by a triangle, one incidence vertex per incident edge."""
    T = nx.Graph()
    for v in G.nodes():
        edges_v = [tuple(sorted(e)) for e in G.edges(v)]
        for e, f in itertools.combinations(edges_v, 2):
            T.add_edge((v, e), (v, f))          # internal triangle edges
    for e in G.edges():
        e = tuple(sorted(e))
        u, v = e
        T.add_edge((u, e), (v, e))              # external edge
    return T


def conflict_pairs(T):
    """All unordered pairs of distinct edges that must get distinct colors."""
    E = [frozenset(e) for e in T.edges()]
    conf = set()
    for e, f in itertools.combinations(E, 2):
        if e & f or any(T.has_edge(x, y) for x in e for y in f):
            conf.add(frozenset((e, f)))
    return conf


def local_config(G, v):
    """The six local edges at the replacement triangle of v, as frozensets."""
    edges_v = [tuple(sorted(e)) for e in G.edges(v)]
    s = set()
    for e, f in itertools.combinations(edges_v, 2):
        s.add(frozenset(((v, e), (v, f))))
    for e in edges_v:
        u = e[0] if e[1] == v else e[1]
        s.add(frozenset(((v, e), (u, e))))
    return s


# ---------- claims A and B on simple cubic G (K4 and the 3-cube) ----------
for name, G in [("K4", nx.complete_graph(4)), ("Q3", nx.hypercube_graph(3))]:
    T = truncation(G)
    assert all(d == 3 for _, d in T.degree())
    conf = conflict_pairs(T)
    configs = {v: local_config(G, v) for v in G.nodes()}

    ok_A = all(frozenset((a, b)) in conf
               for v in G.nodes()
               for a, b in itertools.combinations(configs[v], 2))
    print(name, "claim A (each local six-edge set pairwise conflicting):", ok_A)

    ok_B, n_cross = True, 0
    for pair in conf:
        e, f = tuple(pair)
        if any(e in c and f in c for c in configs.values()):
            continue
        # must be cross-triangle: e internal at v containing incidence vertex (v,g),
        # f internal at u containing (u,g), for some edge g = uv of G
        def owner(edge):  # vertex of G whose triangle contains this internal edge
            vs = {p[0] for p in edge}
            return vs.pop() if len(vs) == 1 else None
        v, u = owner(e), owner(f)
        good = False
        if v is not None and u is not None and G.has_edge(u, v):
            g = tuple(sorted((u, v)))
            good = ((v, g) in e) and ((u, g) in f)
        ok_B &= good
        n_cross += 1
    print(name, "claim B (all non-local conflicts are cross-triangle pairs):",
          ok_B, "| cross pairs found:", n_cross,
          "| expected 4 per edge of G =", 4 * G.number_of_edges())

# ---------- claim C: the K4-labeling construction on G = K4 ----------
G = nx.complete_graph(4)
lam = {v: v + 1 for v in G.nodes()}  # identity labeling: v and its 3 neighbors all distinct
assert all(len({lam[v]} | {lam[u] for u in G[v]}) == 4 for v in G.nodes())

T = truncation(G)
coloring = {}
for e in G.edges():
    e = tuple(sorted(e))
    u, v = e
    coloring[frozenset(((u, e), (v, e)))] = frozenset((lam[u], lam[v]))
for v in G.nodes():
    edges_v = [tuple(sorted(e)) for e in G.edges(v)]
    for e, f in itertools.combinations(edges_v, 2):
        ju = e[0] if e[1] == v else e[1]
        jk = f[0] if f[1] == v else f[1]
        coloring[frozenset(((v, e), (v, f)))] = frozenset((lam[ju], lam[jk]))

assert len(coloring) == T.number_of_edges()
ncolors = len(set(coloring.values()))
conf = conflict_pairs(T)
ok = all(coloring[e] != coloring[f] for pair in conf for e, f in [tuple(pair)])
print("K4 construction: colors used =", ncolors,
      "| coloring is strong:", ok, "| with claim A lower bound, chi'_s(T(K4)) = 6")
