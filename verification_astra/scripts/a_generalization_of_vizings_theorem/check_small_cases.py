"""
Sanity checks on the CONJECTURE itself (not the writeup), to make sure the
referee's reading is the intended one and that the conjecture is not trivially
false at small parameters:

 (a) complete d-uniform hypergraph on d+k vertices: codegree r = k+1, and the
     facet-conflict graph is the Johnson graph J(d+k,k). Compute chi exactly for
     small cases and compare with the conjectured bound r+d-1 = d+k.
 (b) random / exhaustive small d-uniform hypergraphs (d=3,4): compute r and the
     exact chromatic number of the facet-conflict graph, test chi <= r+d-1.
"""
import itertools, random

def facet_conflict_graph(edges, d):
    """edges: list of frozensets of size d. Returns adjacency (share d-1 vertices) and r."""
    from collections import defaultdict
    facets = defaultdict(list)
    for i, e in enumerate(edges):
        for f in itertools.combinations(sorted(e), d-1):
            facets[f].append(i)
    r = max((len(v) for v in facets.values()), default=0)
    adj = {i: set() for i in range(len(edges))}
    for f, lst in facets.items():
        for a, b in itertools.combinations(lst, 2):
            adj[a].add(b); adj[b].add(a)
    return adj, r

def chromatic_number(adj, ub):
    """exact chromatic number by DSATUR-style branch and bound (small graphs)."""
    n = len(adj)
    if n == 0: return 0
    order = sorted(range(n), key=lambda v: -len(adj[v]))
    best = [ub]
    color = {}
    def rec(i, used):
        if used >= best[0]: return
        if i == n:
            best[0] = used; return
        # pick uncolored vertex with max saturation
        cand = max((v for v in order if v not in color),
                   key=lambda v: (len({color[u] for u in adj[v] if u in color}), len(adj[v])))
        forbidden = {color[u] for u in adj[cand] if u in color}
        for c in range(min(used+1, best[0]-1) + 1):
            if c in forbidden: continue
            color[cand] = c
            rec(i+1, max(used, c+1))
            del color[cand]
            if c == used: break   # symmetry: only one fresh color
    rec(0, 0)
    return best[0]

print("(a) complete d-uniform hypergraph on d+k vertices (r = k+1, bound = d+k):")
for d in range(2, 8):
    for k in range(1, 4):
        n = d + k
        edges = [frozenset(c) for c in itertools.combinations(range(n), d)]
        if len(edges) > 21: continue
        adj, r = facet_conflict_graph(edges, d)
        chi = chromatic_number(adj, len(edges)+1)
        bound = r + d - 1
        print(f"   d={d} n={n}: |E|={len(edges):4d} r={r} chi={chi:3d} bound r+d-1={bound:3d}"
              f"  {'TIGHT' if chi==bound else ('ok' if chi<=bound else '*** COUNTEREXAMPLE ***')}")

print("\n(b) random small hypergraphs are tested separately in check_small_random.py")
