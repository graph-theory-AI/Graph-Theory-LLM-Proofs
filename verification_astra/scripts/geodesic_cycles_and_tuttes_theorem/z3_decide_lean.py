"""Lean exact decision (QF_LRA): is there l: E -> R_{>0} on G such that every
l-geodesic cycle is peripheral?

Distances are modelled by variables d[x][y] with the standard Bellman
characterisation (d <= every relaxation, and equality attained at some
predecessor), which for positive lengths forces d to be the true distance.
Then for every NON-peripheral cycle C we assert that C is not geodesic:
  OR over x,y in V(C):  d[x][y] < arc1(x,y)  and  d[x][y] < arc2(x,y).
UNSAT  => no length assignment works  => the writeup's theorem holds.
SAT    => the model is a length assignment refuting the writeup.
"""
import itertools, sys, networkx as nx
from z3 import Real, Solver, Or, And, sat, unsat

B = [f"b{i}" for i in range(1,5)]
G = nx.Graph(); G.add_edges_from(itertools.combinations(B,2))
for i in range(1,5):
    for j in range(1,5):
        if i != j: G.add_edge(f"s{i}", f"b{j}")
V = sorted(G.nodes()); E = sorted(tuple(sorted(e)) for e in G.edges())
L = {e: Real("l_%s_%s" % e) for e in E}
D = {(x,y): Real(f"d_{x}_{y}") for x in V for y in V if x != y}
def le(u,v): return L[tuple(sorted((u,v)))]
def w(es): return sum(le(*e) for e in es)

s = Solver()
for e in E: s.add(L[e] > 0)
for (x,y),d in D.items():
    s.add(d > 0)
    s.add(d == D[(y,x)])
    for z in G[y]:
        s.add(d <= (le(z,y) if z == x else D[(x,z)] + le(z,y)))
    s.add(Or([d == (le(z,y) if z == x else D[(x,z)] + le(z,y)) for z in G[y]]))

def induced(c): return G.subgraph(c).number_of_edges() == len(c)
def peripheral(c):
    if not induced(c): return False
    H = G.copy(); H.remove_nodes_from(c); return nx.is_connected(H)
cycles = list(nx.simple_cycles(G))
nonper = [c for c in cycles if not peripheral(c)]
print("cycles", len(cycles), "non-peripheral", len(nonper)); sys.stdout.flush()

def eo(p): return [(p[i],p[i+1]) for i in range(len(p)-1)]
for c in nonper:
    k = len(c); disj = []
    for i,j in itertools.combinations(range(k),2):
        a1 = eo(c[i:j+1]); rot = c[j:]+c[:i+1]; a2 = eo(rot)
        disj.append(And(D[(c[i],c[j])] < w(a1), D[(c[i],c[j])] < w(a2)))
    s.add(Or(disj))
print("solving..."); sys.stdout.flush()
r = s.check()
print("z3 result:", r); sys.stdout.flush()
if r == sat:
    m = s.model()
    lv = {e: float(m[L[e]].as_fraction()) for e in E}
    print("MODEL lengths:", {f"{a}-{b}": v for (a,b),v in lv.items()})
    # independent re-check with Dijkstra
    for e in E: G[e[0]][e[1]]['w'] = lv[e]
    dd = dict(nx.all_pairs_dijkstra_path_length(G, weight='w'))
    def wt(es): return sum(lv[tuple(sorted(e))] for e in es)
    bad = []
    for c in cycles:
        k = len(c); geo = True
        for i,j in itertools.combinations(range(k),2):
            a1 = eo(c[i:j+1]); rot = c[j:]+c[:i+1]
            if dd[c[i]][c[j]] < min(wt(a1), wt(eo(rot))) - 1e-12: geo = False; break
        if geo and not peripheral(c): bad.append(c)
    print("INDEPENDENT RECHECK: non-peripheral geodesic cycles under the model:", bad)
