"""Brute-force profiles F_H(d) for a two-terminal component, as defined in
sections 4.2 / 5 of the writeup."""
from collections import deque
from pl import Graph, embeddings

INF = float('inf')

def dual_dists_without_rho(emb, rho):
    """dist in D_H (dual of Hhat minus rho*) from each of the two rho-faces."""
    g = emb.g
    A, B = emb.sides(rho)
    adj = [[] for _ in range(emb.nf)]
    for e in range(g.m):
        if e == rho: continue
        a, b = emb.sides(e)
        if a != b:
            adj[a].append(b); adj[b].append(a)
    def bfs(src):
        d = [None]*emb.nf; d[src]=0; dq=deque([src])
        while dq:
            x=dq.popleft()
            for y in adj[x]:
                if d[y] is None:
                    d[y]=d[x]+1; dq.append(y)
        return d
    return A, B, bfs(A), bfs(B)

def cost(emb, rho, a, b, w=None):
    """max over real edges of H of 1+min delta, and over internal vertices
    v != s,t of w(v)+min_{f ni v} delta(f)."""
    g = emb.g
    s, t = g.edges[rho]
    A, B, dA, dB = dual_dists_without_rho(emb, rho)
    if A == B:
        return None
    delta = [min((a + dA[z]) if dA[z] is not None else INF,
                 (b + dB[z]) if dB[z] is not None else INF)
             for z in range(emb.nf)]
    best = 0
    for e in range(g.m):
        if e == rho: continue
        x, y = emb.sides(e)
        best = max(best, 1 + min(delta[x], delta[y]))
    if w:
        for v in range(g.n):
            if v in (s, t): continue
            if not g.inc[v]: continue
            best = max(best, w.get(v,0) + min(delta[f] for f in emb.faces_at_vertex(v)))
    return best

def ell_of(g, rho):
    for emb in embeddings(g):
        A, B, dA, dB = dual_dists_without_rho(emb, rho)
        if A == B: continue
        return dA[B]
    return None

def profile(g, rho, w=None, embs=None):
    """F_H(d) for d = 0..ell, brute force over ALL genus-0 embeddings."""
    if embs is None:
        embs = [e for e in embeddings(g)]
    L = ell_of(g, rho)
    F = {}
    for d in range(L+1):
        vals = [cost(e, rho, 0, d, w) for e in embs]
        vals = [v for v in vals if v is not None]
        F[d] = min(vals)
    return L, F

def profile_general(g, rho, a, b, w=None, embs=None):
    if embs is None:
        embs = [e for e in embeddings(g)]
    vals = [cost(e, rho, a, b, w) for e in embs]
    vals = [v for v in vals if v is not None]
    return min(vals)
