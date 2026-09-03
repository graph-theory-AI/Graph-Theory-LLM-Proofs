"""Small pure-Python graph utilities for the referee check of 2408.02400__00.
Graphs are (n, adjset) with adjset a list of Python sets of neighbors.
"""
import itertools, sys

def from_edges(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    return n, adj

def complement(g):
    n, adj = g
    cadj = [set(range(n)) - adj[v] - {v} for v in range(n)]
    return n, cadj

def mycielski(g):
    """Vertices: 0..n-1 old copies v^0, n..2n-1 first-layer copies v^1, 2n root."""
    n, adj = g
    N = 2 * n + 1
    madj = [set() for _ in range(N)]
    for u in range(n):
        for v in adj[u]:
            madj[u].add(v)
            madj[u].add(v + n); madj[v + n].add(u)
    for v in range(n):
        madj[2 * n].add(v + n); madj[v + n].add(2 * n)
    return N, madj

def bron_kerbosch(g):
    """All maximal cliques (as frozensets)."""
    n, adj = g
    out = []
    def bk(R, P, X):
        if not P and not X:
            out.append(frozenset(R)); return
        pivot = max(P | X, key=lambda u: len(adj[u] & P))
        for v in list(P - adj[pivot]):
            bk(R | {v}, P & adj[v], X & adj[v])
            P.remove(v); X.add(v)
    bk(set(), set(range(n)), set())
    return out

def maximal_homogeneous(g):
    """Maximal cliques of g plus maximal independent sets of g (= maximal
    cliques of complement); a set that is both is included once."""
    return list(set(bron_kerbosch(g)) | set(bron_kerbosch(complement(g))))

def zeta(g, ub=None):
    """Exact cochromatic number: minimum cover of V by maximal homogeneous sets
    (any cover of size t refines to a partition into <= t homogeneous parts,
    and any partition extends to such a cover), via branch and bound."""
    n, adj = g
    sets = maximal_homogeneous(g)
    full = frozenset(range(n))
    best = [n + 1 if ub is None else ub + 1]
    # order sets by size descending for better pruning
    bymember = {v: sorted([s for s in sets if v in s], key=len, reverse=True)
                for v in range(n)}
    maxsize = max(len(s) for s in sets)
    def bb(uncovered, used):
        if used + (len(uncovered) + maxsize - 1) // maxsize >= best[0]:
            return
        if not uncovered:
            best[0] = used
            return
        v = min(uncovered)
        for s in bymember[v]:
            bb(uncovered - s, used + 1)
    bb(full, 0)
    return best[0]

def has_independent_part_optimal(g):
    """Does g admit a minimum cochromatic partition with >=1 independent part?
    Brute force: try covers of size zeta(g) that include >=1 maximal independent
    set covering some vertex not covered by cliques... simpler: search covers of
    size z where at least one chosen set is independent, then refine to a
    partition keeping the independent part nonempty."""
    n, adj = g
    z = zeta(g)
    sets = maximal_homogeneous(g)
    def is_indep(s):
        return all(v not in adj[u] for u in s for v in s if v > u)
    full = frozenset(range(n))
    found = [False]
    def bb(uncovered, chosen):
        if found[0]:
            return
        if not uncovered:
            # refine to partition: assign each vertex to first chosen set
            # need one part independent and nonempty
            partition = []
            assigned = set()
            for s in chosen:
                part = set(s) - assigned
                assigned |= set(s)
                partition.append((part, is_indep(s)))
            if any(indep and part for part, indep in partition):
                found[0] = True
            return
        if len(chosen) == z:
            return
        v = min(uncovered)
        for s in sets:
            if v in s:
                bb(uncovered - s, chosen + [s])
    # try independent-first orderings by forcing: just do plain search but check
    bb(full, [])
    return found[0]

def chromatic_number(g, ub=None):
    n, adj = g
    order = sorted(range(n), key=lambda v: -len(adj[v]))
    def color_with(k):
        colors = {}
        def bt(i):
            if i == n:
                return True
            v = order[i]
            used = {colors[u] for u in adj[v] if u in colors}
            maxc = max(colors.values(), default=-1)
            for c in range(min(maxc + 1, k - 1) + 1):
                if c not in used:
                    colors[v] = c
                    if bt(i + 1):
                        return True
                    del colors[v]
            return False
        return bt(0)
    k = max((len(c) for c in bron_kerbosch(g)), default=1)  # start at omega
    while not color_with(k):
        k += 1
    return k

def clique_number(g):
    return max(len(c) for c in bron_kerbosch(g))

def independence_number(g):
    return clique_number(complement(g))
