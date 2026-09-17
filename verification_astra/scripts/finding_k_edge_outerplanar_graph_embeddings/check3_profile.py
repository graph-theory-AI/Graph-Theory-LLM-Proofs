"""Check 3: the profile abstraction (eq. 6-7):
  min_emb cost(a,b) == min(a,b) + F_H(|a-b|),  and F_H(0,d) == F_H(d,0)."""
import random
import networkx as nx
from pl import Graph, embeddings
from prof import profile, profile_general, ell_of

def from_nx(G):
    vs=sorted(G.nodes()); idx={v:i for i,v in enumerate(vs)}
    return Graph(len(vs), [(idx[u],idx[v]) for u,v in G.edges()])

random.seed(3)
cnt=0; tested=0; bad=0; badsym=0
while cnt < 40:
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
    for rho in range(g.m):
        w={v: random.randint(0,4) for v in range(g.n)}
        L, F = profile(g, rho, w, embs)
        for a in range(0, 7):
            for b in range(0, 7):
                if abs(a-b) > L: continue
                tested+=1
                lhs = profile_general(g, rho, a, b, w, embs)
                rhs = min(a,b) + F[abs(a-b)]
                if lhs != rhs:
                    bad+=1
                    print("PROFILE MISMATCH", g.edges, rho, a, b, lhs, rhs)
        # reflection symmetry
        for d in range(L+1):
            v1 = profile_general(g, rho, 0, d, w, embs)
            v2 = profile_general(g, rho, d, 0, w, embs)
            if v1 != v2:
                badsym+=1
                print("ASYM", g.edges, rho, d, v1, v2)
print(f"profile shift identity: {tested} (component,rho,a,b) cases, mismatches={bad}; reflection asymmetries={badsym}")
