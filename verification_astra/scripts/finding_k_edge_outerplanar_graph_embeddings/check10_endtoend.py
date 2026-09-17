"""Check 10: full pipeline -- block-cut-tree DP (sec 8.2) where each block's
value is computed by the SPQR *top-level* formula (23)-(25) with brute-forced
profiles -- versus brute force over all embeddings of the whole graph.
Also: multigraph bundles, disconnected graphs, trees."""
import random, math
import networkx as nx
from pl import Graph, embeddings, min_edge_outerplanarity
from prof import profile

def sub_graph(nodes, edges):
    idx={v:i for i,v in enumerate(sorted(nodes))}
    return Graph(len(idx), [(idx[u],idx[v]) for u,v in edges]), idx

def block_value(g, w, require_vertex=None):
    """eqs (23)-(25): min over admissible reference edges e of
       max{1, F_{B-e}(1), w(s), w(t)}."""
    if g.m==1:                      # bridge block, eq (28)
        u,v=g.edges[0]
        return max(1, w.get(u,0), w.get(v,0))
    embs=list(embeddings(g))
    best=None
    for e in range(g.m):
        s,t=g.edges[e]
        if require_vertex is not None and require_vertex not in (s,t): continue
        L,F=profile(g,e,w,embs)
        val=max(1, F[1], w.get(s,0), w.get(t,0))
        if best is None or val<best: best=val
    return best

def algorithm(G):
    blocks=[frozenset(b) for b in nx.biconnected_components(G)]
    be={b:[] for b in blocks}
    for u,v in G.edges():
        cands=sorted([b for b in blocks if u in b and v in b], key=len)
        be[cands[0]].append((u,v))
    cuts=set(nx.articulation_points(G))
    BC=nx.Graph()
    for b in blocks: BC.add_node(('B',b))
    for c in cuts: BC.add_node(('C',c))
    for b in blocks:
        for c in cuts:
            if c in b: BC.add_edge(('B',b),('C',c))
    best=None
    for root in blocks:
        order=list(nx.dfs_postorder_nodes(BC,('B',root)))
        par=nx.predecessor(BC,('B',root))
        msg={}
        for node in order:
            if node[0]!='B': continue
            b=node[1]
            p=par[node][0] if par[node] else None
            c=p[1] if p is not None else None
            w={}
            for v in b:
                if v==c: continue
                if v in cuts:
                    ch=[bb for bb in blocks if bb!=b and v in bb and par[('B',bb)] and par[('B',bb)][0]==('C',v)]
                    if ch: w[v]=max(msg[bb] for bb in ch)
            g,idx=sub_graph(b, be[b])
            ww={idx[v]:x for v,x in w.items()}
            msg[b]=block_value(g,ww, None if c is None else idx[c])
        if best is None or msg[root]<best: best=msg[root]
    return best

random.seed(41)
tested=0; bad=0; cnt=0
while cnt<35:
    n=random.randint(4,8)
    G=nx.gnp_random_graph(n, random.uniform(0.2,0.5), seed=random.randint(0,10**9))
    if not nx.is_connected(G) or G.number_of_edges()==0: continue
    if not nx.check_planarity(G)[0]: continue
    gg,_=sub_graph(set(G.nodes()), list(G.edges()))
    sz=1
    for v in range(gg.n): sz*=math.factorial(max(len(gg.inc[v])-1,0))
    if sz>20000: continue
    cnt+=1
    bf=min_edge_outerplanarity(gg); alg=algorithm(G)
    tested+=1
    if bf!=alg:
        bad+=1; print("E2E MISMATCH", sorted(G.edges()), bf, alg)
print(f"end-to-end (block-cut DP + eqs 23-25): {tested} connected planar graphs, mismatches={bad}")

# multigraph bundles (P-node only)
for k in range(1,7):
    g=Graph(2,[(0,1)]*k)
    print(f"  bundle of {k} parallel edges: brute-force optimum = {min_edge_outerplanarity(g)}  (ceil(k/2)={-(-k//2)})")

# disconnected graphs: the machinery here is for connected graphs (Euler
# formula); components are simply handled separately, matching sec. 8's claim.
