"""Shared helpers: the tournament T* = C3[TT2,TT2,1] and basic tournament utilities.

A tournament on n vertices is encoded as a dict/matrix: adj[i][j] = True iff i->j.
"""
from itertools import combinations, permutations, product

def tstar():
    """T* = C3[TT2,TT2,1]: A={a0,a1}, B={b0,b1}, {c}; a0->a1, b0->b1, A->B->c->A."""
    V = ['a0','a1','b0','b1','c']
    idx = {v:i for i,v in enumerate(V)}
    n = 5
    adj = [[False]*n for _ in range(n)]
    def arc(u,v): adj[idx[u]][idx[v]] = True
    arc('a0','a1'); arc('b0','b1')
    for a in ('a0','a1'):
        for b in ('b0','b1'):
            arc(a,b)
    for b in ('b0','b1'): arc(b,'c')
    for a in ('a0','a1'): arc('c',a)
    return adj, V

def is_tournament(adj):
    n = len(adj)
    for i in range(n):
        if adj[i][i]: return False
        for j in range(i+1,n):
            if adj[i][j] == adj[j][i]: return False
    return True

def induced(adj, S):
    return [[adj[i][j] for j in S] for i in S]

def iso(a, b):
    """isomorphism test for small tournaments"""
    n = len(a)
    if n != len(b): return False
    # prune by outdegree multiset
    da = sorted(sum(r) for r in a); db = sorted(sum(r) for r in b)
    if da != db: return False
    for p in permutations(range(n)):
        ok = True
        for i in range(n):
            for j in range(n):
                if i != j and a[i][j] != b[p[i]][p[j]]:
                    ok = False; break
            if not ok: break
        if ok: return True
    return False

TSTAR, TSTAR_V = tstar()

def contains_tstar(adj):
    n = len(adj)
    if n < 5: return False
    for S in combinations(range(n), 5):
        if iso(induced(adj,S), TSTAR): return True
    return False

def directed_triangles(adj):
    n = len(adj); out = []
    for i,j,k in combinations(range(n),3):
        for (a,b,c) in ((i,j,k),(i,k,j)):
            if adj[a][b] and adj[b][c] and adj[c][a]:
                out.append((a,b,c))
    return out

def is_transitive(adj):
    n = len(adj)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and j!=k and i!=k and adj[i][j] and adj[j][k] and not adj[i][k]:
                    return False
    return True

def Z(adj,x,y):   # {z : y->z->x}
    return [z for z in range(len(adj)) if z!=x and z!=y and adj[y][z] and adj[z][x]]

def P(adj,x,y):   # {p : x->p->y}
    return [p for p in range(len(adj)) if p!=x and p!=y and adj[x][p] and adj[p][y]]

def transitive_tournament(n):
    return [[i<j for j in range(n)] for i in range(n)]

def reverse_arc(adj,u,v):
    import copy
    b = [row[:] for row in adj]
    b[u][v], b[v][u] = b[v][u], b[u][v]
    return b
