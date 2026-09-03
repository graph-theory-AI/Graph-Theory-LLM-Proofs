#!/usr/bin/env python3
"""Independent verification of the claimed counterexample to Conjecture 6 (v1)
of arXiv:2512.17232 (Hickingbotham-Joret, "An Induced A-Path Theorem").

Conjecture 6 (v1): for every k, every G and X,Y subseteq V(G):
  (i) G contains k pairwise anti-complete (X,Y)-paths, or
  (ii) there is Z with |Z| <= k-1 such that G - N[Z] has no (X,Y)-path.

Paper's definition: an (X,Y)-path is a path v_1..v_m with V(P) cap X = {v_1}
and V(P) cap Y = {v_m}. Two paths are anti-complete if vertex-disjoint with
no edge between them.

Writeup's claims (k=2), 16-vertex graph:
  C1: max anti-complete packing of (X,Y)-paths = 1 (no two anti-complete),
      and in fact no two X->Y paths of any kind are anti-complete;
  C2: for every single vertex z, G - N[z] still has an (X,Y)-path
      (and Z = empty set fails too), so no Z with |Z| <= 1 works;
  C3: Z = {a0, b0} works, so min separator = 2;
  C4: (scaling) disjoint union of r copies: packing = r, min separator = 2r.
      Checked here for r = 2 (32 vertices, all Z of size <= 3 fail).
"""
import itertools
import networkx as nx


def build_gadget(tag=""):
    G = nx.Graph()
    x = [f"x{i}{tag}" for i in range(4)]
    a = [f"a{i}{tag}" for i in range(4)]
    b = [f"b{i}{tag}" for i in range(4)]
    y = [f"y{i}{tag}" for i in range(4)]
    for i in range(4):
        G.add_edge(x[i], a[i])
        G.add_edge(a[i], b[i])
        G.add_edge(b[i], y[i])
    for i in range(4):
        G.add_edge(a[i], a[(i + 1) % 4])          # 4-cycle on the a_i
    G.add_edge(b[0], b[2])                        # opposite-pair edges
    G.add_edge(b[1], b[3])
    return G, set(x), set(y)


def xy_paths(G, X, Y):
    """All (X,Y)-paths under the paper's definition:
    V(P) cap X = {first vertex}, V(P) cap Y = {last vertex}."""
    H = G.copy()
    paths = []
    inner_ok = set(G.nodes) - X - Y
    for s in sorted(X):
        for t in sorted(Y):
            # simple paths from s to t whose internal vertices avoid X u Y
            K = G.subgraph(inner_ok | {s, t})
            for p in nx.all_simple_paths(K, s, t):
                paths.append(tuple(p))
    return paths


def all_x_to_y_paths(G, X, Y):
    """All simple paths with first vertex in X and last in Y (no restriction
    on internal vertices) -- used for the stronger form of claim C1."""
    paths = []
    for s in sorted(X):
        for t in sorted(Y):
            for p in nx.all_simple_paths(G, s, t):
                paths.append(tuple(p))
    return paths


def anti_complete(G, p, q):
    sp, sq = set(p), set(q)
    if sp & sq:
        return False
    return not any(G.has_edge(u, v) for u in sp for v in sq)


def has_xy_path(G, X, Y):
    """Does G contain an (X,Y)-path?  Equivalent to: some vertex of X reaches
    some vertex of Y (a minimal X-Y connection is an (X,Y)-path)."""
    Xp = X & set(G.nodes)
    Yp = Y & set(G.nodes)
    if not Xp or not Yp:
        return False
    for comp in nx.connected_components(G):
        if comp & Xp and comp & Yp:
            return True
    return False


def closed_nbhd(G, Z):
    N = set(Z)
    for z in Z:
        N |= set(G.neighbors(z))
    return N


def min_separator_leq(G, X, Y, size):
    """Return a Z with |Z| <= size s.t. G - N[Z] has no (X,Y)-path, or None."""
    nodes = sorted(G.nodes)
    for s in range(0, size + 1):
        for Z in itertools.combinations(nodes, s):
            if not has_xy_path(G.subgraph(set(G.nodes) - closed_nbhd(G, Z)), X, Y):
                return Z
    return None


def max_anti_complete_packing(G, X, Y, paths, cap):
    """Max size (up to cap) of a pairwise anti-complete family among `paths`,
    via greedy exhaustive search on the compatibility graph."""
    n = len(paths)
    compat = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            compat[i][j] = compat[j][i] = anti_complete(G, paths[i], paths[j])
    best = 1 if n else 0

    def extend(chosen, cand):
        nonlocal best
        best = max(best, len(chosen))
        if best >= cap:
            return
        for i in list(cand):
            extend(chosen + [i], [j for j in cand if j > i and compat[i][j]])
            if best >= cap:
                return
    extend([], list(range(n)))
    return best


def main():
    G, X, Y = build_gadget()
    assert G.number_of_nodes() == 16
    print(f"Gadget: n={G.number_of_nodes()}, m={G.number_of_edges()}")
    print(f"X stable: {not any(G.has_edge(u,v) for u in X for v in X if u<v)}, "
          f"Y stable: {not any(G.has_edge(u,v) for u in Y for v in Y if u<v)}, "
          f"X,Y disjoint: {not (X & Y)}")

    # Writeup's stated closed neighbourhoods
    assert set(closed_nbhd(G, ["x0"])) == {"x0", "a0"}
    assert set(closed_nbhd(G, ["y0"])) == {"y0", "b0"}
    assert set(closed_nbhd(G, ["a0"])) == {"a0", "x0", "b0", "a1", "a3"}
    assert set(closed_nbhd(G, ["b0"])) == {"b0", "a0", "y0", "b2"}
    print("Stated closed neighbourhoods N[x0],N[y0],N[a0],N[b0]: all match.")

    # C1: no two anti-complete (X,Y)-paths -- strict definition
    P = xy_paths(G, X, Y)
    print(f"\n(X,Y)-paths (strict definition): {len(P)}")
    pairs = sum(1 for p, q in itertools.combinations(P, 2) if anti_complete(G, p, q))
    print(f"anti-complete pairs among them: {pairs}")
    assert pairs == 0

    # C1 strong form: among ALL simple X->Y paths (endpoints in X and Y,
    # internal vertices unrestricted)
    PA = all_x_to_y_paths(G, X, Y)
    print(f"all simple X->Y paths: {len(PA)}")
    pairs_all = sum(1 for p, q in itertools.combinations(PA, 2)
                    if anti_complete(G, p, q))
    print(f"anti-complete pairs among all X->Y paths: {pairs_all}")
    assert pairs_all == 0
    print("C1 verified: max anti-complete packing = 1 (a single (X,Y)-path exists).")
    assert len(P) >= 1

    # C2 + C3: minimum closed-neighbourhood separator
    z0 = min_separator_leq(G, X, Y, 0)
    z1 = min_separator_leq(G, X, Y, 1)
    print(f"\nZ of size 0 destroying all (X,Y)-paths: {z0}")
    print(f"Z of size <=1 destroying all (X,Y)-paths: {z1}")
    assert z0 is None and z1 is None
    # the writeup's Z = {a0,b0}
    rem = set(G.nodes) - closed_nbhd(G, ["a0", "b0"])
    ok = not has_xy_path(G.subgraph(rem), X, Y)
    print(f"Z = {{a0,b0}} destroys all (X,Y)-paths: {ok}")
    assert ok
    print("C2/C3 verified: min separator = 2 > k-1 = 1  (k=2).")

    # C4: disjoint union of 2 copies -> k=3: packing 2, min separator 4
    G1, X1, Y1 = build_gadget("_c1")
    G2, X2, Y2 = build_gadget("_c2")
    H = nx.union(G1, G2)
    XX, YY = X1 | X2, Y1 | Y2
    PH = xy_paths(H, XX, YY)
    print(f"\nDisjoint union (n=32): (X,Y)-paths: {len(PH)}")
    pack = max_anti_complete_packing(H, XX, YY, PH, cap=3)
    print(f"max anti-complete packing (capped at 3): {pack}")
    assert pack == 2
    z3 = min_separator_leq(H, XX, YY, 3)
    print(f"Z of size <=3 destroying all (X,Y)-paths: {z3}")
    assert z3 is None
    rem = set(H.nodes) - closed_nbhd(H, ["a0_c1", "b0_c1", "a0_c2", "b0_c2"])
    ok4 = not has_xy_path(H.subgraph(rem), XX, YY)
    print(f"Z = {{a0,b0}} in each copy (size 4) works: {ok4}")
    assert ok4
    print("C4 verified for r=2 (k=3): packing 2 < 3, min separator 4 > 3.")
    print("Note: this also violates the REVISED v2 conjecture bound |Z| <= k for k=3.")

    print("\nALL CHECKS PASSED: the construction refutes Conjecture 6 (v1, |Z|<=k-1).")


if __name__ == "__main__":
    main()
