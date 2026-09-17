"""Sanity test of the independent min_cover solver in verify_rat.py.

Known value (Proposition: convex position => pi(A) = ceil(n/2), attained by the
standard 'zig-zag' plane Hamilton path decomposition).  If the solver returns
something else on convex point sets, the solver -- not the writeup -- is wrong.
"""
import itertools, math
from fractions import Fraction as F
from verify_rat import crossmatrix, min_cover, proper_cross

def convex(n, N=10**7):
    return [(F(round(N*math.cos(2*math.pi*j/n)), N), F(round(N*math.sin(2*math.pi*j/n)), N))
            for j in range(n)]

def pi_of(P):
    n = len(P)
    edges, eidx, X = crossmatrix(P, n)
    masks = set(); seq=[]
    def dfs(last, visited, blocked, mask):
        if mask: masks.add(mask)
        for nxt in range(n):
            if visited>>nxt & 1: continue
            k = eidx[frozenset((last,nxt))]
            if blocked>>k & 1: continue
            dfs(nxt, visited|(1<<nxt), blocked|X[k], mask|(1<<k))
    for st in range(n): dfs(st, 1<<st, 0, 0)
    return min_cover(masks, len(edges))[0]

for n in range(4, 9):
    got = pi_of(convex(n)); want = -(-n//2)
    print("convex n=%d : pi = %d, expected ceil(n/2) = %d  %s"
          % (n, got, want, "OK" if got == want else "SOLVER BUG"))
