"""Check 8 (Lemma 3 + section 8.2): block-cut-tree DP with the weighted
objective Psi, versus brute force over ALL embeddings of the whole graph."""
import random, itertools
import networkx as nx
from pl import Graph, embeddings, min_edge_outerplanarity

def sub_graph(nodes, edges):
    idx={v:i for i,v in enumerate(sorted(nodes))}
    return Graph(len(idx), [(idx[u],idx[v]) for u,v in edges]), idx

def brute_psi(g, w, require_vertex=None):
    best=None
    for emb in embeddings(g):
        for r in range(emb.nf):
            if require_vertex is not None and r not in emb.faces_at_vertex(require_vertex): continue
            d=emb.dual_dist(r)
            val=emb.K(r)
            for v in range(g.n):
                if not g.inc[v]: continue
                a=min(d[f] for f in emb.faces_at_vertex(v))
                val=max(val, w.get(v,0)+a)
            if best is None or val<best: best=val
    return best

def algorithm(G):
    """block-cut-tree DP of section 8.2, using brute-forced block values."""
    blocks=[frozenset(b) for b in nx.biconnected_components(G)]
    block_edges={}
    for b in blocks:
        block_edges[b]=[(u,v) for u,v in G.edges() if u in b and v in b and
                        (len(b)>2 or True)]
    # fix: an edge belongs to the unique block containing both ends AND being 2-conn
    be={b:[] for b in blocks}
    for u,v in G.edges():
        cands=[b for b in blocks if u in b and v in b]
        # a bridge uv gives block {u,v}; pick the smallest matching block
        cands.sort(key=len)
        be[cands[0]].append((u,v))
    cuts=set(nx.articulation_points(G))
    # block-cut tree
    BC=nx.Graph()
    for b in blocks: BC.add_node(('B',b))
    for c in cuts: BC.add_node(('C',c))
    for b in blocks:
        for c in cuts:
            if c in b: BC.add_edge(('B',b),('C',c))
    best=None
    for root in blocks:
        # bottom-up
        order=list(nx.dfs_postorder_nodes(BC, ('B',root)))
        msg={}   # block -> value of its branch, with parent cutvertex on outer face
        parentc={}
        # determine parent cut vertex of each block via BFS from root
        par=nx.predecessor(BC, ('B',root))
        for node in order:
            if node[0]!='B': continue
            b=node[1]
            p=par[node][0] if par[node] else None
            c = p[1] if p is not None else None
            w={}
            for v in b:
                if v==c: continue
                if v in cuts:
                    ch=[bb for bb in blocks if bb!=b and v in bb and
                        par[('B',bb)] and par[('B',bb)][0]==('C',v)]
                    if ch: w[v]=max(msg[bb] for bb in ch)
            g,idx=sub_graph(b, be[b])
            ww={idx[v]:x for v,x in w.items()}
            if c is None:
                val=brute_psi(g,ww)
            else:
                val=brute_psi(g,ww,require_vertex=idx[c])
            msg[b]=val
        v=msg[root]
        if best is None or v<best: best=v
    return best

random.seed(31)
tested=0; bad=0
cnt=0
while cnt<40:
    n=random.randint(4,8)
    G=nx.gnp_random_graph(n, random.uniform(0.2,0.45), seed=random.randint(0,10**9))
    if not nx.is_connected(G) or G.number_of_edges()==0: continue
    if not nx.check_planarity(G)[0]: continue
    if not set(nx.articulation_points(G)): continue   # want cut vertices
    gg,_=sub_graph(set(G.nodes()), list(G.edges()))
    if sum(max(len(gg.inc[v])-1,0) for v in range(gg.n))>13: continue
    cnt+=1
    bf=min_edge_outerplanarity(gg)
    alg=algorithm(G)
    tested+=1
    if bf!=alg:
        bad+=1
        print("CUTVERTEX MISMATCH", sorted(G.edges()), "brute=",bf, "alg=",alg)
print(f"block-cut DP: {tested} connected graphs with cut vertices, mismatches={bad}")
