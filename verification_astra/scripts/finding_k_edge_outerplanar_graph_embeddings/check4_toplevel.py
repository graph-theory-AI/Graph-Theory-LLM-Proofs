"""Check 4: the top-level reduction for a biconnected block, eqs (23)-(25):
   Opt(B,w;e) = max{1, F_{B-e}(1), w(s), w(t)}
   Opt(B,w)   = min_e Opt(B,w;e)           (and the c-constrained version)
against brute force over all embeddings/outer faces of
   Psi(B,w) = max{K(B,r), max_v (w(v)+a_B(v))}."""
import random
import networkx as nx
from pl import Graph, embeddings
from prof import profile

def from_nx(G):
    vs=sorted(G.nodes()); idx={v:i for i,v in enumerate(vs)}
    return Graph(len(vs), [(idx[u],idx[v]) for u,v in G.edges()])

def brute_psi(g, w, embs, require_vertex=None, require_edge=None):
    best=None
    for emb in embs:
        for r in range(emb.nf):
            if require_vertex is not None and r not in emb.faces_at_vertex(require_vertex): continue
            if require_edge is not None and r not in emb.sides(require_edge): continue
            d = emb.dual_dist(r)
            val = emb.K(r)
            for v in range(g.n):
                if not g.inc[v]: continue
                a = min(d[f] for f in emb.faces_at_vertex(v))
                val = max(val, w.get(v,0)+a)
            if best is None or val<best: best=val
    return best

random.seed(5)
cnt=0; tested=0; bad=0; badc=0; bade=0
while cnt<40:
    n=random.randint(4,7)
    G=nx.gnp_random_graph(n, random.uniform(0.4,0.9), seed=random.randint(0,10**9))
    if not nx.is_connected(G): continue
    ok,_=nx.check_planarity(G)
    if not ok: continue
    if nx.node_connectivity(G)<2: continue
    g=from_nx(G)
    if sum(max(len(g.inc[v])-1,0) for v in range(g.n))>12: continue
    cnt+=1
    embs=list(embeddings(g))
    for trial in range(3):
        w={v: random.choice([0,0,1,2,3,5]) for v in range(g.n)}
        # algorithm value
        opt_e={}
        for e in range(g.m):
            sub=Graph(g.n, [x for i,x in enumerate(g.edges) if i!=e])
            # Hhat = g with rho = e ; profile of H = g-e with reference edge e
            L,F = profile(g, e, w, embs)
            s,t = g.edges[e]
            opt_e[e]=max(1, F[1] if 1<=L else F[L], w.get(s,0), w.get(t,0))
            assert L>=1
        alg = min(opt_e.values())
        bf  = brute_psi(g,w,embs)
        tested+=1
        if alg!=bf:
            bad+=1; print("TOPLEVEL MISMATCH", g.edges, w, alg, bf)
        # per-edge version
        for e in range(g.m):
            bfe = brute_psi(g,w,embs,require_edge=e)
            if opt_e[e]!=bfe:
                bade+=1; print("PER-EDGE MISMATCH", g.edges, w, e, opt_e[e], bfe)
        # constrained at a vertex
        for c in range(g.n):
            algc = min(opt_e[e] for e in range(g.m) if c in g.edges[e])
            bfc = brute_psi(g,w,embs,require_vertex=c)
            if algc!=bfc:
                badc+=1; print("CONSTRAINED MISMATCH", g.edges, w, c, algc, bfc)
print(f"top-level: {tested} (block,weights) cases; unconstrained mismatches={bad}, per-edge={bade}, vertex-constrained={badc}")
