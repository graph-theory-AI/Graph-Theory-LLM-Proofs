"""Check 3: Lemma 2 of the writeup.

Lemma 2: with k = ceil(log2(n+1)), R = 2k+3, for every x whose component is not
K_{Delta+1}: either (1) B_R(x) contains a vertex of G-degree < Delta, or
(2) G[B_R(x)] is not a Gallai tree.

We verify this on:
  - random Delta-regular connected graphs (Delta = 3,4,5), where case (1) can
    only fail, so G[B_R(x)] must not be a Gallai tree;
  - structured graphs: hypercube Q3, Petersen, toroidal grids, circulants;
  - 'triangle-tree' Gallai graphs (cubic in the interior), the natural
    near-worst-case: balls around deep interior vertices ARE Gallai trees,
    so case (1) must hold within radius R -- we check it does, and we measure
    the minimal radius r* at which the disjunction first holds, comparing
    against R.
"""
import math
import random
import sys

import networkx as nx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import is_gallai_tree, ball, random_regular_connected

rng = random.Random(777)


def R_of(n):
    k = math.ceil(math.log2(n + 1))
    return 2 * k + 3, k


def disjunction_holds(G, x, r, Delta):
    B = ball(G, x, r)
    if any(G.degree(z) < Delta for z in B):
        return True, "low-degree"
    H = G.subgraph(B)
    if not is_gallai_tree(H):
        return True, "non-gallai"
    return False, None


def min_radius(G, x, Delta, rmax):
    for r in range(0, rmax + 1):
        ok, why = disjunction_holds(G, x, r, Delta)
        if ok:
            return r, why
    return None, None


def triangle_tree(depth):
    """Gallai tree, cubic in the interior: rooted tree of triangles joined by
    bridges; every triangle vertex gets a bridge to the apex of a child
    triangle, up to given depth. Interior vertices have degree 3."""
    G = nx.Graph()
    counter = [0]

    def new_triangle():
        a, b, c = counter[0], counter[0] + 1, counter[0] + 2
        counter[0] += 3
        G.add_edges_from([(a, b), (b, c), (a, c)])
        return [a, b, c]

    root = new_triangle()
    frontier = [(v, 1) for v in root]
    while frontier:
        v, d = frontier.pop()
        if d >= depth:
            continue
        child = new_triangle()
        G.add_edge(v, child[0])  # bridge; apex child[0] reaches degree 3 (2+1)
        for w in child[1:]:      # apex spawns no further child (keeps deg 3)
            frontier.append((w, d + 1))
    assert max(d for _, d in G.degree()) == 3
    return G


def main():
    worst_ratio = 0.0
    # --- random regular graphs ---
    for Delta in (3, 4, 5):
        for n in (10, 14, 20, 30, 40, 60):
            if n <= Delta or (n * Delta) % 2:
                continue
            for it in range(15):
                G = random_regular_connected(n, Delta, rng)
                if G is None:
                    continue
                R, k = R_of(n)
                for x in G:
                    ok, why = disjunction_holds(G, x, R, Delta)
                    assert ok, f"LEMMA 2 FALSIFIED: Delta={Delta} n={n} x={x}"
                    r, _ = min_radius(G, x, Delta, R)
                    worst_ratio = max(worst_ratio, r / R)
    print("random regular graphs: Lemma 2 disjunction held for every vertex")

    # --- structured graphs ---
    tests = [
        ("Q3 hypercube", nx.hypercube_graph(3), 3),
        ("Q4 hypercube", nx.hypercube_graph(4), 4),
        ("Petersen", nx.petersen_graph(), 3),
        ("torus 4x4", nx.grid_2d_graph(4, 4, periodic=True), 4),
        ("torus 6x6", nx.grid_2d_graph(6, 6, periodic=True), 4),
        ("circulant C20(1,2)", nx.circulant_graph(20, [1, 2]), 4),
        ("K4 minus edge", nx.Graph([(0,1),(0,2),(0,3),(1,2),(1,3)]), 3),
        ("K_{3,3}", nx.complete_bipartite_graph(3, 3), 3),
    ]
    for name, G, Delta in tests:
        n = G.number_of_nodes()
        R, k = R_of(n)
        for x in G:
            ok, why = disjunction_holds(G, x, R, Delta)
            assert ok, f"LEMMA 2 FALSIFIED on {name} at {x}"
        print(f"{name}: disjunction held at all {n} vertices (R={R})")

    # --- triangle trees (Gallai, cubic interior): near-worst-case radius ---
    print()
    print("triangle-tree Gallai graphs (interior degree 3, Delta=3):")
    print("depth      n      R   max over x of minimal r*   r*/R")
    for depth in (3, 4, 5, 6, 7):
        G = triangle_tree(depth)
        n = G.number_of_nodes()
        Delta = 3
        R, k = R_of(n)
        worst = 0
        for x in G:
            ok, why = disjunction_holds(G, x, R, Delta)
            assert ok, f"LEMMA 2 FALSIFIED on triangle_tree({depth}) at {x}"
            r, _ = min_radius(G, x, Delta, R)
            worst = max(worst, r)
        worst_ratio = max(worst_ratio, worst / R)
        print(f"{depth:5d}  {n:5d}  {R:5d}  {worst:10d}              {worst/R:.2f}")

    print()
    print(f"largest observed (minimal r*)/R over all tests: {worst_ratio:.2f}")
    print("CHECK 3 PASSED (no counterexample to Lemma 2 found)")


if __name__ == "__main__":
    main()
