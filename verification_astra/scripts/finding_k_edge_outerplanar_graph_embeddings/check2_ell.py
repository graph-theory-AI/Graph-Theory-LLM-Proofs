"""Check 2 (Lemma 2): for a two-terminal component H with reference edge rho,
ell(H) = dist in (dual of H+rho minus rho*) between the two faces beside rho
is embedding-invariant, and equals the s-t min edge cut of H."""
import random
import networkx as nx
from collections import deque
from pl import Graph, embeddings

def ell_values(g, rho):
    """All values of dist(A,B) in D_H over genus-0 embeddings of Hhat=g."""
    vals = set()
    for emb in embeddings(g):
        A, B = emb.sides(rho)
        if A == B:           # rho a bridge: Hhat not biconnected, skip
            vals.add(None); continue
        # BFS in dual minus rho*
        adj = [[] for _ in range(emb.nf)]
        for e in range(g.m):
            if e == rho: continue
            a, b = emb.sides(e)
            if a != b:
                adj[a].append(b); adj[b].append(a)
        d = [None]*emb.nf; d[A]=0; dq=deque([A])
        while dq:
            x=dq.popleft()
            for y in adj[x]:
                if d[y] is None:
                    d[y]=d[x]+1; dq.append(y)
        vals.add(d[B])
    return vals

def mincut(g, rho):
    """min s-t edge cut of H = g minus edge rho, s,t = ends of rho."""
    s, t = g.edges[rho]
    N = nx.MultiGraph()
    N.add_nodes_from(range(g.n))
    for i,(u,v) in enumerate(g.edges):
        if i == rho: continue
        N.add_edge(u,v)
    D = nx.DiGraph()
    D.add_nodes_from(range(g.n))
    for u,v in N.edges():
        D.add_edge(u,v,capacity=D.get_edge_data(u,v,{}).get('capacity',0)+1)
        D.add_edge(v,u,capacity=D.get_edge_data(v,u,{}).get('capacity',0)+1)
    try:
        return nx.maximum_flow_value(D, s, t)
    except Exception:
        return None

def from_nx(G):
    vs = sorted(G.nodes()); idx={v:i for i,v in enumerate(vs)}
    return Graph(len(vs), [(idx[u],idx[v]) for u,v in G.edges()])

random.seed(7)
tested=0; bad=0
count=0
while count < 60:
    n = random.randint(4,7)
    G = nx.gnp_random_graph(n, random.uniform(0.4,0.85), seed=random.randint(0,10**9))
    if not nx.is_connected(G): continue
    ok,_ = nx.check_planarity(G)
    if not ok: continue
    if nx.node_connectivity(G) < 2: continue
    g = from_nx(G)
    if sum(max(len(g.inc[v])-1,0) for v in range(g.n)) > 13: continue
    count += 1
    for rho in range(g.m):
        vals = ell_values(g, rho)
        tested += 1
        mc = mincut(g, rho)
        if len(vals) != 1 or None in vals or list(vals)[0] != mc:
            bad += 1
            print("ELL MISMATCH", g.edges, rho, vals, mc)
print(f"ell-invariance: {tested} (biconnected graph, reference edge) pairs, mismatches = {bad}")
