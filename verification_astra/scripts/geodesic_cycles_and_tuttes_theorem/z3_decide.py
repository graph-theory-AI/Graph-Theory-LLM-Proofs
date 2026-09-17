"""NOTE: superseded by z3_decide_lean.py -- this path-enumeration encoding is
correct but blows up (>25 min, ~1 GB) and was aborted; z3_decide_lean.py decides
the same question in seconds via distance variables.

Exact decision: does there exist l: E(G)->R_{>0} such that EVERY l-geodesic
cycle of G is peripheral?  Encoded as a QF_LRA formula and handed to z3.

A cycle C is l-geodesic iff for all x,y in V(C) there is no x-y path in G
strictly shorter than BOTH x-y arcs of C.  So "C is NOT geodesic" is
  OR over pairs x,y in C, over simple x-y paths P:  l(P)<arc1 and l(P)<arc2.
We require this for every non-peripheral cycle C.
"""
import itertools, networkx as nx
from z3 import Real, Solver, Or, And, sat, unsat

B = [f"b{i}" for i in range(1, 5)]
S = [f"s{i}" for i in range(1, 5)]
G = nx.Graph()
G.add_edges_from(itertools.combinations(B, 2))
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            G.add_edge(f"s{i}", f"b{j}")

E = sorted(tuple(sorted(e)) for e in G.edges())
L = {e: Real("l_%s_%s" % e) for e in E}
def w(edgeset):
    return sum(L[tuple(sorted(e))] for e in edgeset)

def edges_of_path(p):
    return [tuple(sorted((p[i], p[i+1]))) for i in range(len(p)-1)]

paths = {}
for x, y in itertools.combinations(G.nodes(), 2):
    ps = list(nx.all_simple_paths(G, x, y))
    paths[(x, y)] = [edges_of_path(p) for p in ps]
    paths[(y, x)] = paths[(x, y)]
print("simple paths per pair:", {k: len(v) for k, v in sorted(paths.items()) if k[0] < k[1]})

def induced(c):
    return G.subgraph(c).number_of_edges() == len(c)
def peripheral(c):
    if not induced(c): return False
    H = G.copy(); H.remove_nodes_from(c); return nx.is_connected(H)

cycles = list(nx.simple_cycles(G))
nonper = [c for c in cycles if not peripheral(c)]
print("cycles:", len(cycles), " non-peripheral:", len(nonper))

s = Solver()
for e in E:
    s.add(L[e] > 0)
nclause = 0
for c in nonper:
    k = len(c)
    disj = []
    for i, j in itertools.combinations(range(k), 2):
        x, y = c[i], c[j]
        arc1 = edges_of_path(c[i:j+1])
        arc2 = edges_of_path(c[j:] + c[:i+1])
        a1, a2 = w(arc1), w(arc2)
        for P in paths[(x, y)]:
            if set(P) == set(arc1) or set(P) == set(arc2):
                continue
            disj.append(And(w(P) < a1, w(P) < a2))
    s.add(Or(disj)); nclause += len(disj)
print("total witness literals:", nclause)
res = s.check()
print("z3 says:", res)
if res == sat:
    m = s.model()
    print("MODEL:", {f"{e[0]}-{e[1]}": str(m[L[e]]) for e in E})
