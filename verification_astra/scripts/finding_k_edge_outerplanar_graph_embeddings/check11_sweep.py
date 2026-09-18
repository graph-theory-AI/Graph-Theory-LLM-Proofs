"""Check 11: a larger randomized sweep of the full pipeline, different seed,
including 2-connected graphs and graphs of optimum >= 3."""
import random, math, collections
import networkx as nx
from pl import Graph, min_edge_outerplanarity
from check10_endtoend import algorithm, sub_graph

random.seed(97)
tested=0; bad=0; dist=collections.Counter()
cnt=0
while cnt<60:
    n=random.randint(4,9)
    G=nx.gnp_random_graph(n, random.uniform(0.25,0.6), seed=random.randint(0,10**9))
    if not nx.is_connected(G) or G.number_of_edges()==0: continue
    if not nx.check_planarity(G)[0]: continue
    gg,_=sub_graph(set(G.nodes()), list(G.edges()))
    sz=1
    for v in range(gg.n): sz*=math.factorial(max(len(gg.inc[v])-1,0))
    if sz>30000: continue
    cnt+=1
    bf=min_edge_outerplanarity(gg); alg=algorithm(G)
    tested+=1; dist[bf]+=1
    if bf!=alg:
        bad+=1; print("MISMATCH", sorted(G.edges()), bf, alg)
print(f"sweep: {tested} graphs, mismatches={bad}, optimum distribution={dict(sorted(dist.items()))}")
