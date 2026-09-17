"""Machine check of the finite combinatorial lemmas used by the writeup."""
import itertools, networkx as nx
B=[f"b{i}" for i in range(1,5)]
G=nx.Graph(); G.add_edges_from(itertools.combinations(B,2))
for i in range(1,5):
    for j in range(1,5):
        if i!=j: G.add_edge(f"s{i}",f"b{j}")
core=[tuple(sorted(e)) for e in itertools.combinations(B,2)]
def induced(c): return G.subgraph(c).number_of_edges()==len(c)
def peripheral(c):
    if not induced(c): return False
    H=G.copy(); H.remove_nodes_from(c); return nx.is_connected(H)
cyc=list(nx.simple_cycles(G))
per=[c for c in cyc if peripheral(c)]
def eset(c): return {tuple(sorted((a,b))) for a,b in zip(c,c[1:]+c[:1])}
print("每 peripheral triangle: #core edges it contains ->",
      sorted({len(eset(c)&set(core)) for c in per}))
inc={e: [c for c in per if e in eset(c)] for e in core}
print("core edge -> number of peripheral triangles containing it:",
      {f"{a}{b}": len(v) for (a,b),v in inc.items()})
spokes=[tuple(sorted(e)) for e in G.edges() if not (e[0][0]=='b' and e[1][0]=='b')]
print("spoke edge -> number of peripheral triangles containing it:",
      {f"{a}{b}": sum(1 for c in per if (a,b) in eset(c)) for a,b in spokes})
coreT=[tuple(sorted(t)) for t in itertools.combinations(B,3)]
print("core triangles:",coreT,"each is induced&non-peripheral:",
      [(induced(list(t)), peripheral(list(t))) for t in coreT])
# minimum number of core edges meeting every core triangle
best=min(k for k in range(7) if any(all(len({tuple(sorted(e)) for e in itertools.combinations(t,2)} & set(S))>0
        for t in coreT) for S in itertools.combinations(core,k)))
print("minimum edge set of K4 hitting all 4 triangles:",best,
      "=> with <=1 non-tight core edge some core triangle is all-tight:", best>1)
