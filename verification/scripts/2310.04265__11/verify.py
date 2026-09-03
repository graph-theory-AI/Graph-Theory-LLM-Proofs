#!/usr/bin/env python3
"""Independent verification of the counterexample in attacks/2310.04265__11/output.md.

Conventions (from arXiv:2310.04265):
  - digraphs: no loops, no digons.
  - backedge graph D^prec: edge uv if u prec v and vu in A(D).
  - dic(D) = dichromatic number = min #parts in partition into acyclic sets
           = min over orderings of chi(D^prec).
  - diomega(D) = min over orderings of omega(D^prec).

Writeup's construction:
  - S(H): for ordered graph H on x_1..x_m, add a_{ij} per edge x_i x_j (i<j)
    with arcs x_i->a_{ij}, a_{ij}->x_j, x_j->x_i.
  - F_H(G): substitute a copy of G for each a_{ij}.
  - H_n = mu^{n+1}(K_2) (iterated Mycielskian), G_0 = S(K_2) (directed triangle),
    G_{n+1} = F_{H_n}(G_n).
Claims verified here:
  A. dic identity sanity check on random small digraphs.
  B. Mycielski: mu(K2)=C5 and mu^2(K2)=Grotzsch are triangle-free with chi 3, 4.
  C. S(H) for H in {K2, C5, Grotzsch}: dic = 2, and diomega = 2
     (<=2 via an explicit ordering; >=2 since not acyclic); hereditary bound on
     random induced subdigraphs.
  D. F_H(G) equals iterated paper-style substitution (checked on a small case).
  E. G_1 = F_{C5}(triangle): dic(G_1) = 3 by exhaustive search (no 2-dicoloring),
     diomega(G_1) = 2 (Lemma-2 ordering gives triangle-free backedge graph).
  F. Lemma-2 ordering for G_2 = F_{Grotzsch}(G_1) (411 vertices): backedge graph
     has clique number 2, so diomega(G_2) = 2.
  G. Lemma 1 premise ingredients for G_2: every 3-coloring of Grotzsch has a
     monochromatic edge (chi=4), and dic(G_1)=3 (from E); the gluing argument
     then forces dic(G_2) >= 4. Upper bound dic(G_2) <= 4 exhibited explicitly.
"""
import itertools, random
import networkx as nx

random.seed(12)

# ---------- basic parameters ----------

def is_acyclic(D, S):
    return nx.is_directed_acyclic_graph(D.subgraph(S))

def dic_brute(D, kmax=6):
    """dichromatic number by exhaustive search over colorings (small D only)."""
    nodes = list(D.nodes())
    n = len(nodes)
    if n == 0:
        return 0
    for k in range(1, kmax + 1):
        # backtracking
        color = {}
        def ok(v, c):
            color[v] = c
            cls = [u for u in color if color[u] == c]
            good = is_acyclic(D, cls)
            del color[v]
            return good
        def bt(i, used):
            if i == n:
                return True
            v = nodes[i]
            for c in range(min(used + 1, k)):
                if ok(v, c):
                    color[v] = c
                    if bt(i + 1, max(used, c + 1)):
                        return True
                    del color[v]
            return False
        if bt(0, 0):
            return k
    return None

def has_2_dicoloring_exhaustive(D):
    """check all bipartitions (feasible up to ~22 vertices)."""
    nodes = list(D.nodes())
    n = len(nodes)
    for mask in range(2 ** (n - 1)):  # fix nodes[0] in part 0
        A = [nodes[0]] + [nodes[i] for i in range(1, n) if (mask >> (i - 1)) & 1]
        B = [v for v in nodes if v not in set(A)]
        if is_acyclic(D, A) and is_acyclic(D, B):
            return True, (A, B)
    return False, None

def backedge_graph(D, order):
    pos = {v: i for i, v in enumerate(order)}
    G = nx.Graph()
    G.add_nodes_from(D.nodes())
    for (u, v) in D.edges():  # arc u->v ; backedge iff v prec u
        if pos[v] < pos[u]:
            G.add_edge(v, u)
    return G

def clique_number(G):
    return max((len(c) for c in nx.find_cliques(G)), default=1) if G.number_of_nodes() else 0

def diomega_brute(D):
    nodes = list(D.nodes())
    best = None
    for perm in itertools.permutations(nodes):
        w = clique_number(backedge_graph(D, perm))
        best = w if best is None else min(best, w)
        if best == 1:
            break
    return best

def dic_via_orderings(D):
    nodes = list(D.nodes())
    best = None
    for perm in itertools.permutations(nodes):
        c = nx.algorithms.coloring.greedy_color(backedge_graph(D, perm))  # upper bound
        chi = chi_brute(backedge_graph(D, perm))
        best = chi if best is None else min(best, chi)
    return best

def chi_brute(G, kmax=8):
    nodes = list(G.nodes())
    for k in range(1, kmax + 1):
        color = {}
        def bt(i, used):
            if i == len(nodes):
                return True
            v = nodes[i]
            for c in range(min(used + 1, k)):
                if all(color.get(u) != c for u in G.neighbors(v)):
                    color[v] = c
                    if bt(i + 1, max(used, c + 1)):
                        return True
                    del color[v]
            return False
        if bt(0, 0):
            return k
    return None

# ---------- constructions ----------

def mycielski(G):
    M = nx.Graph()
    M.add_nodes_from([("v", x) for x in G.nodes()])
    M.add_nodes_from([("u", x) for x in G.nodes()])
    M.add_node("w")
    for (a, b) in G.edges():
        M.add_edge(("v", a), ("v", b))
        M.add_edge(("u", a), ("v", b))
        M.add_edge(("u", b), ("v", a))
    for x in G.nodes():
        M.add_edge("w", ("u", x))
    mapping = {v: i for i, v in enumerate(sorted(M.nodes(), key=str))}
    return nx.relabel_nodes(M, mapping)

def S_of(H):
    """H: graph with integer nodes 0..m-1 (the ordering is by integer)."""
    D = nx.DiGraph()
    D.add_nodes_from(("x", i) for i in H.nodes())
    for (a, b) in H.edges():
        i, j = min(a, b), max(a, b)
        D.add_node(("a", i, j))
        D.add_edge(("x", i), ("a", i, j))
        D.add_edge(("a", i, j), ("x", j))
        D.add_edge(("x", j), ("x", i))
    return D

def F(H, G):
    """substitute a fresh copy of G for each a_{ij} in S(H)."""
    D = nx.DiGraph()
    D.add_nodes_from(("x", i) for i in H.nodes())
    for (a, b) in H.edges():
        i, j = min(a, b), max(a, b)
        copy = {g: ("g", i, j, g) for g in G.nodes()}
        D.add_nodes_from(copy.values())
        for (u, v) in G.edges():
            D.add_edge(copy[u], copy[v])
        D.add_edge(("x", j), ("x", i))
        for g in copy.values():
            D.add_edge(("x", i), g)
            D.add_edge(g, ("x", j))
    return D

def substitute(D1, u, D2):
    """paper's substitution of D2 for u in D1 (fresh labels for D2)."""
    D = nx.DiGraph()
    lab = {t: ("sub", u, t) for t in D2.nodes()}
    D.add_nodes_from(v for v in D1.nodes() if v != u)
    D.add_nodes_from(lab.values())
    for (a, b) in D1.edges():
        if u not in (a, b):
            D.add_edge(a, b)
    for (a, b) in D2.edges():
        D.add_edge(lab[a], lab[b])
    for v in D1.nodes():
        if v == u:
            continue
        if D1.has_edge(v, u):
            for t in lab.values():
                D.add_edge(v, t)
        if D1.has_edge(u, v):
            for t in lab.values():
                D.add_edge(t, v)
    return D

def lemma2_order(H, G, Gorder):
    """x_1, blocks G_{1j}, x_2, blocks G_{2j}, ..., x_m (paper indices = ints)."""
    order = []
    m = sorted(H.nodes())
    for i in m:
        order.append(("x", i))
        for j in sorted(H.nodes()):
            if j > i and H.has_edge(i, j):
                order.extend(("g", i, j, g) for g in Gorder)
    return order

# ---------- checks ----------

print("== A. sanity: dic = min_orderings chi(backedge) on random digraphs ==")
for t in range(30):
    n = random.randint(3, 6)
    D = nx.DiGraph()
    D.add_nodes_from(range(n))
    for a in range(n):
        for b in range(a + 1, n):
            r = random.random()
            if r < 0.35:
                D.add_edge(a, b)
            elif r < 0.7:
                D.add_edge(b, a)
    d1 = dic_brute(D)
    d2 = dic_via_orderings(D)
    assert d1 == d2, (t, d1, d2)
print("   OK: 30 random digraphs, dic_brute == min over orderings of chi(backedge)")

print("== B. Mycielski graphs ==")
K2 = nx.Graph([(0, 1)])
H0 = mycielski(K2)              # should be C5
H1 = mycielski(H0)              # Grotzsch
assert nx.is_isomorphic(H0, nx.cycle_graph(5))
for name, Hh, expchi in [("H0=mu(K2)", H0, 3), ("H1=mu^2(K2)", H1, 4)]:
    tri = any(True for _ in nx.enumerate_all_cliques(Hh) if False)  # placeholder
    tri_free = clique_number(Hh) <= 2
    ch = chi_brute(Hh)
    print(f"   {name}: n={Hh.number_of_nodes()}, triangle-free={tri_free}, chi={ch}")
    assert tri_free and ch == expchi

print("== C. S(H) for H in {K2, C5, Grotzsch} ==")
for name, Hh in [("K2", K2), ("C5", H0), ("Grotzsch", H1)]:
    S = S_of(Hh)
    # explicit 2-dicoloring: X acyclic, A independent
    X = [v for v in S.nodes() if v[0] == "x"]
    A = [v for v in S.nodes() if v[0] == "a"]
    assert is_acyclic(S, X) and is_acyclic(S, A)
    assert not nx.is_directed_acyclic_graph(S)   # has a directed triangle -> dic=2
    # diomega <= 2 via ordering x_1 < a_{1j} < x_2 < ... (Lemma-2 order with 1-vertex G)
    dummy = nx.DiGraph(); dummy.add_node(0)
    order = lemma2_order(Hh, dummy, [0])
    order = [(("a", v[1], v[2]) if v[0] == "g" else v) for v in order]
    B = backedge_graph(S, order)
    w = clique_number(B)
    print(f"   S({name}): n={S.number_of_nodes()}, dic=2 (explicit), backedge clique via order = {w}")
    assert w == 2
    # hereditary: random induced subdigraphs are 2-dicolorable
    nodes = list(S.nodes())
    for _ in range(50):
        sub = S.subgraph(random.sample(nodes, random.randint(1, len(nodes))))
        Xs = [v for v in sub.nodes() if v[0] == "x"]; As = [v for v in sub.nodes() if v[0] == "a"]
        assert is_acyclic(sub, Xs) and is_acyclic(sub, As)
print("   OK (hereditary 2-dicolorability spot-checked, 50 samples each)")

print("== C'. exact diomega of S(K2) (directed triangle) by all orderings ==")
print("   diomega(S(K2)) =", diomega_brute(S_of(K2)))

print("== D. F_H(G) == iterated paper substitution (small case) ==")
G0 = S_of(K2)  # directed triangle
P2 = nx.Graph([(0, 1), (1, 2)])  # path, 2 edges
direct = F(P2, G0)
step = S_of(P2)
for v in [v for v in step.nodes() if v[0] == "a"]:
    step = substitute(step, v, G0)
assert nx.is_isomorphic(direct, step)
print("   OK: F_{P3}(triangle) isomorphic to substituting the triangle for each a_ij in S(P3)")

print("== E. G_1 = F_{C5}(G_0): dic and diomega ==")
G1 = F(H0, G0)
print("   |V(G_1)| =", G1.number_of_nodes(), " |A(G_1)| =", G1.number_of_edges())
ok2, _ = has_2_dicoloring_exhaustive(G1)
print("   2-dicoloring exists:", ok2)
assert not ok2
# explicit 3-dicoloring per Lemma 1: each copy 2-dicolored with the same palette,
# X gets one additional color.  2-dicoloring of the triangle G_0: {x0, a01} | {x1}.
tri_class0 = {("x", 0), ("a", 0, 1)}
c0 = [v for v in G1.nodes() if v[0] == "g" and v[3] in tri_class0]
c1 = [v for v in G1.nodes() if v[0] == "g" and v[3] not in tri_class0]
c2 = [v for v in G1.nodes() if v[0] == "x"]
assert is_acyclic(G1, c0) and is_acyclic(G1, c1) and is_acyclic(G1, c2)
assert len(c0) + len(c1) + len(c2) == G1.number_of_nodes()
print("   dic(G_1) = 3  (no 2-dicoloring among all 2^19 bipartitions; explicit 3-dicoloring)")
# diomega(G_1): Lemma-2 ordering; internal order of the triangle: x1 < a12 < x2 gives backedge K?
# choose triangle ordering with backedge clique 2: any ordering of a 3-cycle gives one backedge.
Gorder = [("x", 0), ("a", 0, 1), ("x", 1)]
order1 = lemma2_order(H0, G0, Gorder)
B1 = backedge_graph(G1, order1)
w1 = clique_number(B1)
print("   backedge clique number of G_1 under Lemma-2 ordering:", w1)
assert w1 == 2
assert not nx.is_directed_acyclic_graph(G1)
print("   => diomega(G_1) = 2")

print("== F. G_2 = F_{Grotzsch}(G_1): diomega ==")
G2 = F(H1, G1)
print("   |V(G_2)| =", G2.number_of_nodes(), " |A(G_2)| =", G2.number_of_edges())
order2 = lemma2_order(H1, G1, order1)
assert len(order2) == G2.number_of_nodes()
B2 = backedge_graph(G2, order2)
w2 = clique_number(B2)
print("   backedge clique number of G_2 under Lemma-2 ordering:", w2)
assert w2 == 2
assert not nx.is_directed_acyclic_graph(G2)
print("   => diomega(G_2) = 2")

print("== G. Lemma 1 ingredients for dic(G_2) = 4 ==")
# every 3-coloring of Grotzsch has a monochromatic edge (chi=4 established in B)
# upper bound: explicit 4-dicoloring of G_2
c0, c1 = set(c0), set(c1)
cls = [[], [], [], []]
for v in G2.nodes():
    if v[0] == "x":
        cls[3].append(v)
    else:
        # v = ('g', i, j, g1vertex) with g1vertex a G_1 vertex
        g1v = v[3]
        if g1v in c0:
            cls[0].append(v)
        elif g1v in c1:
            cls[1].append(v)
        else:
            cls[2].append(v)
assert all(is_acyclic(G2, c) for c in cls)
assert sum(len(c) for c in cls) == G2.number_of_nodes()
print("   explicit 4-dicoloring of G_2 verified; dic(G_1)=3 and chi(Grotzsch)=4 give dic(G_2)>=4")
print("   (Lemma 1 gluing: any 3-dicoloring restricted to a copy of G_1 uses all 3 colors,")
print("    and the 11 x-vertices 3-colored must leave some Grotzsch edge monochromatic ->")
print("    monochromatic directed triangle x_i -> y -> x_j -> x_i.)")

print()
print("ALL CHECKS PASSED")
