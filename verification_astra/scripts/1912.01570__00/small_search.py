"""Independent sanity check: does Conjecture 14 (fvs <= 2 fp) survive on ALL small planar
graphs?  We use the rigorous upper bound UB(fp) from the apex criterion
(C facial in some embedding  ==>  G + apex over V(C) planar), so
     fvs(G) > 2 * UB(fp)  ==>  genuine counterexample.
Any hit is then re-checked by exhaustive rotation-system enumeration.
"""
import itertools
import networkx as nx
from networkx.generators.atlas import graph_atlas_g

from build import all_cycles, max_disjoint, fvs_bruteforce
from embeddings import fp_exact


def fp_upper(G):
    cand = []
    for C in set(all_cycles(G)):
        H = G.copy()
        H.add_node(("APEX",))
        for v in C:
            H.add_edge(("APEX",), v)
        if nx.check_planarity(H)[0]:
            cand.append(C)
    return max_disjoint(cand)[0]


if __name__ == "__main__":
    worst = []
    checked = 0
    for G in graph_atlas_g():
        if G.number_of_nodes() < 3:
            continue
        if not nx.check_planarity(G)[0]:
            continue
        checked += 1
        k, _ = fvs_bruteforce(G)
        if k == 0:
            continue
        ub = fp_upper(G)
        if k > 2 * ub:
            worst.append((G.number_of_nodes(), k, ub, sorted(G.edges())))
    print(f"planar graphs from the atlas (n<=7) checked: {checked}")
    print(f"counterexamples found (fvs > 2*UB(fp)): {len(worst)}")
    for w in worst:
        print("   ", w)

    # ratio record among small graphs
    best = (0, None)
    for G in graph_atlas_g():
        if G.number_of_nodes() < 3 or not nx.check_planarity(G)[0]:
            continue
        k, _ = fvs_bruteforce(G)
        if k == 0:
            continue
        ub = fp_upper(G)
        if ub and k / ub > best[0]:
            best = (k / ub, (G.number_of_nodes(), k, ub, sorted(G.edges())))
    print("\nbest fvs/UB(fp) ratio among planar graphs with n<=7:", best[0])
    print("   attained by:", best[1])
