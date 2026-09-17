"""Check 9: hand-crafted hard instances (deep branches, nested blocks,
a_B(v)>0 attachments) for the block-cut / weighted machinery."""
import networkx as nx
from pl import Graph, min_edge_outerplanarity
from check8_cutvertex import algorithm, sub_graph

def mk(edges):
    G=nx.Graph(); G.add_edges_from(edges); return G

cases={
 "K4+pendant": [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(3,4)],
 "K4+P3 pendant": [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6)],
 "two K4 sharing a vertex": [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),
                             (3,4),(3,5),(3,6),(4,5),(4,6),(5,6)],
 "K4 + triangle at a vertex": [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(3,4),(4,5),(5,3)],
 "W4 + pendant": [(0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4),(4,1),(1,5)],
 "K4 with pendant on every vertex": [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),
                                     (0,4),(1,5),(2,6),(3,7)],
 "path of 3 triangles": [(0,1),(1,2),(2,0),(2,3),(3,4),(4,2),(4,5),(5,6),(6,4)],
 "K5-e + pendant": [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(4,5)],
 "star of triangles at one vertex": [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0),(0,5),(5,6),(6,0)],
 "tree": [(0,1),(1,2),(1,3),(3,4),(3,5),(0,6)],
 "K4 chain": [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(3,4),(4,5),(3,5),(5,6)],
}
bad=0
for name,E in cases.items():
    G=mk(E)
    assert nx.check_planarity(G)[0], name
    g,_=sub_graph(set(G.nodes()), list(G.edges()))
    size=1
    for v in range(g.n):
        import math
        size*= math.factorial(max(len(g.inc[v])-1,0))
    bf=min_edge_outerplanarity(g)
    alg=algorithm(G) if set(nx.articulation_points(G)) else None
    if alg is None:
        print(f"{name:35s} rot.systems={size:8d} brute={bf}  (2-connected, no cut vertex)")
        continue
    flag = "OK" if bf==alg else "*** MISMATCH ***"
    if bf!=alg: bad+=1
    print(f"{name:35s} rot.systems={size:8d} brute={bf} alg={alg}  {flag}")
print("mismatches:",bad)
