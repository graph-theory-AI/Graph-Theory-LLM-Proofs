"""(a) Sanity-check the rotation-system enumerator on graphs with known embeddings.
(b) A rigorous UPPER bound on fp(G_t) for larger t.

For (b): if cycle C bounds a face in some embedding of G, then we may place a new
apex vertex inside that face and join it to every vertex of C, keeping the graph
planar.  Hence
      C facial in some embedding  ==>  G + apex(V(C)) is planar.
So  fp(G) <= max number of pairwise vertex-disjoint cycles C with G+apex(V(C)) planar.
This is a valid upper bound (the converse direction is not needed).
"""
import itertools
import networkx as nx

from build import build, all_cycles, max_disjoint
from embeddings import fp_exact


def count_planar_rotations(G):
    V = list(G.nodes())
    E = G.number_of_edges()
    from embeddings import rotation_choices, faces_of
    per = [rotation_choices(sorted(G.neighbors(v))) for v in V]
    c = 0
    for combo in itertools.product(*per):
        rot = dict(zip(V, combo))
        if len(V) - E + len(faces_of(rot, E)) == 2:
            c += 1
    return c


def apex_facial_candidates(G):
    """Cycles C such that G + (apex joined to all of V(C)) is planar."""
    out = []
    for C in set(all_cycles(G)):
        H = G.copy()
        H.add_node("APEX")
        for v in C:
            H.add_edge("APEX", v)
        if nx.check_planarity(H)[0]:
            out.append(C)
    return out


if __name__ == "__main__":
    print("--- (a) enumerator sanity checks (expected: 2 planar rotation systems "
          "for a 3-connected planar graph, by Whitney) ---")
    tests = [("K4", nx.complete_graph(4)),
             ("cube Q3", nx.hypercube_graph(3)),
             ("octahedron", nx.octahedral_graph()),
             ("K5 (non-planar)", nx.complete_graph(5)),
             ("K3,3 (non-planar)", nx.complete_bipartite_graph(3, 3)),
             ("C5 (cycle)", nx.cycle_graph(5))]
    for name, H in tests:
        H = nx.convert_node_labels_to_integers(H)
        print(f"   {name:18s} planar rotation systems = {count_planar_rotations(H)} "
              f"(nx planar: {nx.check_planarity(H)[0]})")

    print("\n--- (b) apex criterion validated against exhaustive ground truth, t=1 ---")
    G1 = build(1)
    _, _, facial_exact = fp_exact(G1, verbose=False)
    cand1 = set(apex_facial_candidates(G1))
    print("   exhaustively facial:", len(facial_exact),
          "| apex-candidates:", len(cand1))
    print("   facial set subset of apex-candidates:", facial_exact <= cand1)
    print("   the two sets are equal:", facial_exact == cand1)

    print("\n--- (b) upper bound on fp(G_t) via the apex criterion ---")
    for t in (1, 2, 3):
        G = build(t)
        cand = apex_facial_candidates(G)
        ub, wit = max_disjoint(cand)
        Ci_facial = [i for i in range(1, t + 1)
                     if frozenset({f"a{i}", f"b{i}", f"c{i}", f"d{i}"}) in set(cand)]
        print(f"   t={t}: apex-candidate cycles = {len(cand)}, "
              f"fp <= {ub} (claim t+1 = {t+1}); "
              f"C_i passing apex test: {Ci_facial or 'none'}")
        print(f"          upper-bound witness: {[sorted(c) for c in wit]}")

    print("\n--- (c) the writeup's explicit packing {p_j q_j s_j} realised in one embedding ---")
    for t in (1, 2, 3):
        G = build(t)
        H = G.copy()
        for j in range(t + 1):
            H.add_node(f"AP{j}")
            for v in (f"p{j}", f"q{j}", f"s{j}"):
                H.add_edge(f"AP{j}", v)
        print(f"   t={t}: G + apexes over all t+1 triangles p_j q_j s_j is planar: "
              f"{nx.check_planarity(H)[0]}  =>  fp(G_{t}) >= {t+1}")

    print("\n--- (d) the K_4-subdivision witness making C_i non-facial ---")
    for t in (1, 2, 3):
        G = build(t)
        for i in range(1, t + 1):
            a, b, c, d = f"a{i}", f"b{i}", f"c{i}", f"d{i}"
            Q = {f"p{i}", f"q{i}", f"r{i}", f"s{i}"}
            # P_i : a_i -> c_i through Q_i ; R_i : b_i -> d_i avoiding C_i and Q_i
            H1 = G.subgraph([v for v in G if v in Q or v in (a, c)])
            P = nx.shortest_path(H1, a, c)
            H2 = G.copy()
            H2.remove_nodes_from(Q | {a, c})
            R = nx.shortest_path(H2, b, d)
            internally_disjoint = not (set(P[1:-1]) & set(R[1:-1]))
            avoids_C = not (set(R[1:-1]) & {a, b, c, d}) and not (set(P[1:-1]) & {a, b, c, d})
            print(f"   t={t} C_{i}: P={P} R={R} | internally disjoint: "
                  f"{internally_disjoint} | avoid C_i internally: {avoids_C}")
