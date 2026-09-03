#!/usr/bin/env python3
"""
Cross-checks for attack 2009.12189__00 (supplement to verify.py).

  (G) Positive controls for the two-forest-partition backtracker:
      K4, octahedron, icosahedron (dual of the Hamiltonian dodecahedron)
      must all admit partitions into two induced forests (writeup's (3)/(4)
      predicts the icosahedron does, since the dodecahedron is Hamiltonian).
  (H) Independent recomputation of M = max induced-forest weight (weights
      d(v)-2) on the Tutte dual via scipy MILP (HiGHS) with lazily added
      cycle constraints: for each cycle C of G found in an incumbent,
      sum_{v in C} x_v <= |C|-1.  Must agree with verify.py's B&B (M=43).
  (I) Icosahedron spot checks used in the review: a(icosahedron) = 6 and
      it has a 2-forest partition, so va_f(icosahedron) = 2 exactly
      (vertex-transitive tight example, consistent with writeup Section 1).
"""

import time

import networkx as nx
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

from verify import (check_tutte_graph, build_dual, two_forest_partition,
                    max_weight_induced_forest, check_forest)


def milp_max_weight_forest(G, weight):
    nodes = sorted(G.nodes())
    n = len(nodes)
    vi = {v: i for i, v in enumerate(nodes)}
    w = np.array([float(weight[v]) for v in nodes])
    constraints = []
    # seed with all triangles
    for tri in nx.enumerate_all_cliques(G):
        if len(tri) == 3:
            row = np.zeros(n)
            for v in tri:
                row[vi[v]] = 1.0
            constraints.append((row, 2.0))
        if len(tri) > 3:
            break
    it = 0
    while True:
        it += 1
        A = np.array([r for r, _ in constraints])
        ub = np.array([b for _, b in constraints])
        lc = LinearConstraint(A, -np.inf, ub)
        res = milp(c=-w, integrality=np.ones(n), bounds=Bounds(0, 1),
                   constraints=[lc])
        assert res.status == 0, res.message
        x = np.round(res.x).astype(int)
        S = [nodes[i] for i in range(n) if x[i] == 1]
        sub = G.subgraph(S)
        try:
            cyc = nx.find_cycle(sub)
        except nx.NetworkXNoCycle:
            return -res.fun, S, it
        cyc_nodes = sorted({u for e in cyc for u in e[:2]})
        row = np.zeros(n)
        for v in cyc_nodes:
            row[vi[v]] = 1.0
        constraints.append((row, float(len(cyc_nodes) - 1)))


def main():
    print("(G) positive controls for two_forest_partition:")
    for name, K in [("K4", nx.complete_graph(4)),
                    ("octahedron", nx.octahedral_graph()),
                    ("icosahedron", nx.icosahedral_graph())]:
        part = two_forest_partition(K)
        assert part is not None, f"{name}: partition should exist!"
        A, B = part
        assert check_forest(K, A) and check_forest(K, B)
        assert set(A) | set(B) == set(K.nodes()) and not (set(A) & set(B))
        print(f"    {name}: partition found, |A|={len(A)}, |B|={len(B)}: OK")
    # negative control: K5 minus nothing is nonplanar; use wheel W6 (hub+C6)?
    # Wheel graphs are 2-arborable; a clean negative control is K5 itself:
    # any 2-partition has a class with >=3 mutually adjacent vertices -> cycle
    # only if class size >=3; K5: parts of sizes (3,2) or (4,1): the 3-part is
    # a triangle. So K5 has no 2-forest partition.
    assert two_forest_partition(nx.complete_graph(5)) is None
    print("    K5 (negative control): correctly no partition")

    H, emb = check_tutte_graph()
    G, _ = build_dual(H, emb)

    print("(H) MILP cross-check of M on the Tutte dual ...")
    t = time.time()
    wdict = {v: G.degree(v) - 2 for v in G.nodes()}
    M2, S2, iters = milp_max_weight_forest(G, wdict)
    assert check_forest(G, S2)
    print(f"(H) MILP: M = {M2:.0f} (lazy-cycle iterations: {iters}, "
          f"{time.time()-t:.1f}s)  [verify.py B&B gave 43]")
    assert abs(M2 - 43) < 1e-6

    a2, Sa2, _ = milp_max_weight_forest(G, {v: 1 for v in G.nodes()})
    print(f"(H) MILP: a(G) = {a2:.0f}  [verify.py B&B gave 15]")
    assert abs(a2 - 15) < 1e-6

    print("(I) icosahedron: a and va_f tightness check")
    ico = nx.icosahedral_graph()
    a_ico, S_ico, _ = max_weight_induced_forest(ico, {v: 1 for v in ico})
    print(f"(I) a(icosahedron) = {a_ico} (cut-counting bound predicts <= 6); "
          f"vertex-transitive => va_f = 12/6 = 2 exactly")
    assert a_ico == 6

    print("all cross-checks passed")


if __name__ == "__main__":
    main()
