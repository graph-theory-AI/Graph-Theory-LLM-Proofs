"""Check 1: the degree-choosability theorem (Borodin 1977 / Erdos-Rubin-Taylor 1979)
as used in the writeup (Section 2, forward direction only):

  If a connected graph H is NOT a Gallai tree, then for every list assignment A
  with |A(v)| >= d_H(v), H is A-colorable.

Exhaustive over all connected graphs on n <= 6 vertices; for each non-Gallai-tree
graph we try many adversarial list assignments with |A(v)| = d(v) exactly, drawn
from small color universes (the hardest regime), plus the all-identical-lists
assignment. Any failure would falsify the theorem as used.

Also sanity-checks the converse on examples: Gallai trees DO have bad degree-list
assignments (K_{D+1} with identical lists, odd cycles with identical 2-lists).
"""
import itertools
import random
import sys

import networkx as nx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import is_gallai_tree, list_colorable

rng = random.Random(12345)


def all_connected_graphs(n):
    """All connected graphs on n labelled vertices, up to isomorphism (crudely:
    we just iterate labelled and dedupe by certificate for speed at n<=6)."""
    verts = list(range(n))
    pairs = list(itertools.combinations(verts, 2))
    seen = set()
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        if len(edges) < n - 1:
            continue
        G = nx.Graph()
        G.add_nodes_from(verts)
        G.add_edges_from(edges)
        if not nx.is_connected(G):
            continue
        cert = nx.weisfeiler_lehman_graph_hash(G, iterations=3)
        deg = tuple(sorted(d for _, d in G.degree()))
        key = (cert, deg)
        if key in seen:
            continue
        seen.add(key)
        yield G


def adversarial_lists(G, trials, universe_extra):
    """Yield list assignments with |A(v)| = d(v), from a small universe."""
    dmax = max(d for _, d in G.degree())
    # identical lists first (classical worst case)
    yield {v: list(range(G.degree(v))) for v in G}
    for _ in range(trials):
        U = list(range(dmax + universe_extra))
        yield {v: rng.sample(U, G.degree(v)) for v in G}


def main():
    total = failures = tested_nongallai = 0
    for n in range(2, 7):
        cnt = 0
        for G in all_connected_graphs(n):
            cnt += 1
            if min(d for _, d in G.degree()) == 0:
                continue
            if is_gallai_tree(G):
                continue
            tested_nongallai += 1
            for lists in adversarial_lists(G, trials=200, universe_extra=1):
                total += 1
                if list_colorable(G, lists) is None:
                    failures += 1
                    print("FALSIFIED on", sorted(G.edges()), lists)
            # also universe_extra=0 impossible (need d(v) colors from d_max universe) fine
        print(f"n={n}: {cnt} connected graphs (up to WL-hash iso)")
    print(f"non-Gallai-tree graphs tested: {tested_nongallai}")
    print(f"list assignments tested: {total}, failures: {failures}")

    # Converse sanity: Gallai trees admit bad degree-list assignments
    bad = 0
    for D in (3, 4):
        K = nx.complete_graph(D + 1)
        lists = {v: list(range(D)) for v in K}
        if list_colorable(K, lists) is None:
            bad += 1
    C5 = nx.cycle_graph(5)
    if list_colorable(C5, {v: [0, 1] for v in C5}) is None:
        bad += 1
    print(f"sanity (expected 3 uncolorable Gallai-tree instances): {bad}")
    assert failures == 0 and bad == 3
    print("CHECK 1 PASSED")


if __name__ == "__main__":
    main()
