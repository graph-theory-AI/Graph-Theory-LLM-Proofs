"""Positive/negative controls validating the QF_LRA encoding of
 'exists l>0 such that every l-geodesic cycle is peripheral'."""
import itertools, sys, networkx as nx
from z3 import Real, Solver, Or, And, sat

def decide(G, name):
    V=sorted(G.nodes()); E=sorted(tuple(sorted(e)) for e in G.edges())
    L={e:Real("l_%s_%s"%e) for e in E}
    D={(x,y):Real(f"d_{x}_{y}") for x in V for y in V if x!=y}
    def le(u,v): return L[tuple(sorted((u,v)))]
    def w(es): return sum(le(*e) for e in es)
    s=Solver()
    for e in E: s.add(L[e]>0)
    for (x,y),d in D.items():
        s.add(d>0); s.add(d==D[(y,x)])
        for z in G[y]:
            s.add(d <= (le(z,y) if z==x else D[(x,z)]+le(z,y)))
        s.add(Or([d==(le(z,y) if z==x else D[(x,z)]+le(z,y)) for z in G[y]]))
    def induced(c): return G.subgraph(c).number_of_edges()==len(c)
    def per(c):
        if not induced(c): return False
        H=G.copy(); H.remove_nodes_from(c)
        return H.number_of_nodes()==0 or nx.is_connected(H)
    cyc=list(nx.simple_cycles(G)); nonper=[c for c in cyc if not per(c)]
    def eo(p): return [(p[i],p[i+1]) for i in range(len(p)-1)]
    for c in nonper:
        k=len(c); disj=[]
        for i,j in itertools.combinations(range(k),2):
            a1=eo(c[i:j+1]); rot=c[j:]+c[:i+1]
            disj.append(And(D[(c[i],c[j])]<w(a1), D[(c[i],c[j])]<w(eo(rot))))
        s.add(Or(disj))
    r=s.check()
    out=f"{name}: n={G.number_of_nodes()} m={G.number_of_edges()} cycles={len(cyc)} nonper={len(nonper)} -> {r}"
    if r==sat:
        m=s.model(); lv={e:float(m[L[e]].as_fraction()) for e in E}
        for e in E: G[e[0]][e[1]]['w']=lv[e]
        dd=dict(nx.all_pairs_dijkstra_path_length(G,weight='w'))
        def wt(es): return sum(lv[tuple(sorted(e))] for e in es)
        bad=[]
        for c in cyc:
            geo=True
            for i,j in itertools.combinations(range(len(c)),2):
                a1=eo(c[i:j+1]); rot=c[j:]+c[:i+1]
                if dd[c[i]][c[j]]<min(wt(a1),wt(eo(rot)))-1e-12: geo=False;break
            if geo and not per(c): bad.append(c)
        out+=f"  | model recheck: non-peripheral geodesic cycles = {len(bad)} {bad[:3]}"
        out+=f"  | lengths={ {f'{a}{b}':round(v,4) for (a,b),v in lv.items()} }"
    print(out); sys.stdout.flush()

decide(nx.complete_graph(4), "K4 (expect sat)")
decide(nx.complete_graph(5), "K5")
decide(nx.hypercube_graph(3), "Q3 cube")
decide(nx.circular_ladder_graph(3), "triangular prism")
decide(nx.octahedral_graph(), "octahedron")
decide(nx.wheel_graph(5), "W4 wheel")
