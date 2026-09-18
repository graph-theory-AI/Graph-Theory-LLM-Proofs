"""Core utilities: build direct products of complete multipartite graphs,
compute alpha and IR (upper irredundance) by exhaustive search."""
import itertools
from functools import lru_cache

def build(factors):
    """factors: list of lists of part sizes. Returns (vertices, N, Nclosed, labels)
    vertex = tuple of (part_index, index_within_part) per coordinate; adjacency iff
    part indices differ in EVERY coordinate."""
    coords = []
    for f in factors:
        cs = []
        for a, s in enumerate(f):
            for k in range(s):
                cs.append((a, k))
        coords.append(cs)
    verts = list(itertools.product(*coords))
    n = len(verts)
    idx = {v: i for i, v in enumerate(verts)}
    N = [0]*n
    for i, u in enumerate(verts):
        for j, v in enumerate(verts):
            if i == j:
                continue
            if all(u[c][0] != v[c][0] for c in range(len(factors))):
                N[i] |= (1 << j)
    Nc = [N[i] | (1 << i) for i in range(n)]
    return verts, N, Nc

def is_irredundant(S, Nc, n):
    """S: bitmask."""
    members = [v for v in range(n) if S >> v & 1]
    for v in members:
        ok = False
        for p in range(n):
            if Nc[p] & S == (1 << v):
                ok = True
                break
        if not ok:
            return False
    return True

def IR(Nc, n, verbose=False):
    """Exhaustive DFS over irredundant sets (irredundance is hereditary)."""
    best = 0
    bestset = 0
    count = 0
    # precompute closed neighborhoods
    def rec(start, S, size):
        nonlocal best, bestset, count
        count += 1
        if size > best:
            best, bestset = size, S
        for v in range(start, n):
            S2 = S | (1 << v)
            if is_irredundant(S2, Nc, n):
                rec(v+1, S2, size+1)
    rec(0, 0, 0)
    if verbose:
        print("  irredundant sets visited:", count)
    return best, bestset

def alpha(factors):
    """max weight independent family in the quotient, brute force over quotient."""
    qs = [len(f) for f in factors]
    Om = list(itertools.product(*[range(q) for q in qs]))
    def w(x):
        p = 1
        for i, a in enumerate(x):
            p *= factors[i][a]
        return p
    # max weight independent set in quotient graph via DP over subsets is too big;
    # use networkx max weight clique on the complement
    import networkx as nx
    Gc = nx.Graph()
    for x in Om:
        Gc.add_node(x, weight=w(x))
    for x, y in itertools.combinations(Om, 2):
        if any(x[i] == y[i] for i in range(len(qs))):   # non-adjacent in Q
            Gc.add_edge(x, y)
    cl, wt = nx.max_weight_clique(Gc, weight='weight')
    return wt, cl
