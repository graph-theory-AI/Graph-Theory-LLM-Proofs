"""Consistency check against the literature record for the WEAKER problem.

Obenaus-Orthaber / Dumitrescu-Toth: the best known lower bound for partitioning
K_n[A] into PLANE SUBGRAPHS is n/2+1.  Is pi(A) >= 3n/4 consistent with that?

Yes, and the direction matters: k plane paths covering E(K_n[A]) yield, after
assigning each edge to one path containing it, a partition into <= k plane
subgraphs.  So  chi_cross(A) <= pi(A), never the reverse.  A big pi(A) implies
nothing about chi_cross(A).  We verify this numerically on the construction.

chi_cross(A) = chromatic number of the crossing graph on the edge set
(a plane subgraph = an independent set of the crossing graph).
"""
import itertools, math
from fractions import Fraction as F
from verify_rat import build, crossmatrix, min_cover, proper_cross

def chi_cross(P):
    n = len(P)
    edges = list(itertools.combinations(range(n),2))
    ne = len(edges)
    adj = [set() for _ in range(ne)]
    for k1,k2 in itertools.combinations(range(ne),2):
        a,b = edges[k1]; c,d = edges[k2]
        if proper_cross(P,a,b,c,d): adj[k1].add(k2); adj[k2].add(k1)
    # exact chromatic number by increasing k, DSATUR-style backtracking
    order = sorted(range(ne), key=lambda k: -len(adj[k]))
    for K in range(1, ne+1):
        col = {}
        def bt(idx):
            if idx == ne: return True
            v = order[idx]
            used = {col[u] for u in adj[v] if u in col}
            top = min(K, (max(col.values())+2) if col else 1)
            for c in range(top):
                if c in used: continue
                col[v] = c
                if bt(idx+1): return True
                del col[v]
            return False
        if bt(0): return K
    return None

for h in (5, 7):
    P = build(h, 1, seed=0)
    n = h+1
    edges, eidx, X = crossmatrix(P, n)
    masks=set()
    def dfs(last, visited, blocked, mask):
        if mask: masks.add(mask)
        for nxt in range(n):
            if visited>>nxt & 1: continue
            k = eidx[frozenset((last,nxt))]
            if blocked>>k & 1: continue
            dfs(nxt, visited|(1<<nxt), blocked|X[k], mask|(1<<k))
    for st in range(n): dfs(st, 1<<st, 0, 0)
    pi = min_cover(masks, len(edges))[0]
    ch = chi_cross(P)
    print("h=%d n=%d : pi(A)=%d (plane PATHS)  chi_cross(A)=%d (plane SUBGRAPHS)  n/2=%.1f  n/2+1=%.1f"
          % (h, n, pi, ch, n/2, n/2+1))
    print("          chi_cross <= pi : %s   (so a 3n/4 path bound does NOT contradict the n/2+1 subgraph record)"
          % (ch <= pi))
