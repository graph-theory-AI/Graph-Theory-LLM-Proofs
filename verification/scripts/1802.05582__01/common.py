"""Shared helpers for refereeing 1802.05582__01 (randomized Delta-list-coloring).

Gallai tree test, list-coloring by backtracking, ball extraction.
"""
import itertools
import random
import networkx as nx


def is_gallai_tree(H):
    """H connected. True iff every block (biconnected component) is a
    complete graph or an odd cycle. Bridges are K_2 blocks (complete)."""
    assert nx.is_connected(H)
    for block in nx.biconnected_components(H):
        B = H.subgraph(block)
        b = len(block)
        m = B.number_of_edges()
        if m == b * (b - 1) // 2:
            continue  # complete (includes K_2 bridges)
        # odd cycle: b == m, all degrees 2, b odd
        if b >= 3 and b % 2 == 1 and m == b and all(d == 2 for _, d in B.degree()):
            continue
        return False
    return True


def list_colorable(H, lists):
    """Backtracking: is H properly colorable with color of v drawn from lists[v]?
    Returns a coloring dict or None."""
    nodes = sorted(H.nodes(), key=lambda v: len(lists[v]))
    color = {}

    def bt(i):
        if i == len(nodes):
            return True
        v = nodes[i]
        for c in lists[v]:
            if all(color.get(u) != c for u in H[v]):
                color[v] = c
                if bt(i + 1):
                    return True
                del color[v]
        return False

    return dict(color) if bt(0) else None


def ball(G, x, r):
    """Set of vertices at distance <= r from x."""
    return set(nx.single_source_shortest_path_length(G, x, cutoff=r).keys())


def random_regular_connected(n, d, rng, avoid_complete=True, tries=200):
    for _ in range(tries):
        try:
            G = nx.random_regular_graph(d, n, seed=rng.randrange(10**9))
        except nx.NetworkXError:
            return None
        if nx.is_connected(G):
            if avoid_complete and n == d + 1:
                return None
            return G
    return None
