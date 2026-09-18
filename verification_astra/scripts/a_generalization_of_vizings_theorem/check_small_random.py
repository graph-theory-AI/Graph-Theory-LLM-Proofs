"""Random SMALL d-uniform hypergraphs: test the conjecture chi_facet <= r+d-1 directly."""
import itertools, random
from collections import defaultdict

def facet_conflict_graph(edges, d):
    facets = defaultdict(list)
    for i, e in enumerate(edges):
        for f in itertools.combinations(sorted(e), d-1):
            facets[f].append(i)
    r = max((len(v) for v in facets.values()), default=0)
    n = len(edges); adj = [set() for _ in range(n)]
    for lst in facets.values():
        for a, b in itertools.combinations(lst, 2):
            adj[a].add(b); adj[b].add(a)
    return adj, r

def exact_chi(adj):
    n = len(adj)
    if n == 0: return 0
    best = [n]
    color = [-1]*n
    def rec(k, used):
        if used >= best[0]: return
        if k == n:
            best[0] = used; return
        v = max((v for v in range(n) if color[v] < 0),
                key=lambda v: (len({color[u] for u in adj[v] if color[u] >= 0}), len(adj[v])))
        forb = {color[u] for u in adj[v] if color[u] >= 0}
        for c in range(used):
            if c in forb: continue
            color[v] = c; rec(k+1, used); color[v] = -1
        if used < best[0]-1:
            color[v] = used; rec(k+1, used+1); color[v] = -1
    rec(0, 0)
    return best[0]

random.seed(11)
worst = {}; tested = 0; viol = 0
for d in (3, 4, 5):
    for n in range(d+1, d+5):
        allE = [frozenset(c) for c in itertools.combinations(range(n), d)]
        for _ in range(300):
            p = random.uniform(0.2, 1.0)
            edges = [e for e in allE if random.random() < p]
            if len(edges) < 2 or len(edges) > 22: continue
            adj, r = facet_conflict_graph(edges, d)
            chi = exact_chi(adj); tested += 1
            slack = (r + d - 1) - chi
            if slack < 0: viol += 1
            key = (d, n)
            if key not in worst or slack < worst[key][0]:
                worst[key] = (slack, r, chi, len(edges))
for k in sorted(worst):
    s_, r, chi, m = worst[k]
    print(f"  d={k[0]} n={k[1]}: min slack (r+d-1)-chi = {s_:2d}  (r={r}, chi={chi}, |E|={m})"
          f"  {'*** VIOLATION ***' if s_ < 0 else ''}")
print(f"instances tested: {tested}, violations: {viol}")
