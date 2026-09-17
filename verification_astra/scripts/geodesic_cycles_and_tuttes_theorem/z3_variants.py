"""Robustness of the UNSAT verdict for G under weaker readings of 'peripheral'."""
import itertools, sys, networkx as nx
from z3 import Real, Solver, Or, And, sat
B=[f"b{i}" for i in range(1,5)]
G=nx.Graph(); G.add_edges_from(itertools.combinations(B,2))
for i in range(1,5):
    for j in range(1,5):
        if i!=j: G.add_edge(f"s{i}",f"b{j}")
V=sorted(G.nodes()); E=sorted(tuple(sorted(e)) for e in G.edges())
cyc=list(nx.simple_cycles(G))
def induced(c): return G.subgraph(c).number_of_edges()==len(c)
def nonsep(c):
    H=G.copy(); H.remove_nodes_from(c); return H.number_of_nodes()==0 or nx.is_connected(H)
defs={"standard (induced & non-separating)": lambda c: induced(c) and nonsep(c),
      "non-separating only": nonsep,
      "induced only": induced}
def decide(pred,name):
    L={e:Real("l_%s_%s"%e) for e in E}
    D={(x,y):Real(f"d_{x}_{y}") for x in V for y in V if x!=y}
    def le(u,v): return L[tuple(sorted((u,v)))]
    def w(es): return sum(le(*e) for e in es)
    s=Solver()
    for e in E: s.add(L[e]>0)
    for (x,y),d in D.items():
        s.add(d>0); s.add(d==D[(y,x)])
        for z in G[y]: s.add(d <= (le(z,y) if z==x else D[(x,z)]+le(z,y)))
        s.add(Or([d==(le(z,y) if z==x else D[(x,z)]+le(z,y)) for z in G[y]]))
    def eo(p): return [(p[i],p[i+1]) for i in range(len(p)-1)]
    nonper=[c for c in cyc if not pred(c)]
    for c in nonper:
        disj=[]
        for i,j in itertools.combinations(range(len(c)),2):
            a1=eo(c[i:j+1]); rot=c[j:]+c[:i+1]
            disj.append(And(D[(c[i],c[j])]<w(a1), D[(c[i],c[j])]<w(eo(rot))))
        s.add(Or(disj))
    r=s.check(); print(f"{name}: #'peripheral' cycles={len(cyc)-len(nonper)} -> {r}"); sys.stdout.flush()
    return r,s,L
for n,p in defs.items():
    r,s,L=decide(p,n)
    if r==sat:
        m=s.model(); print("   model:",{f"{a}{b}":str(m[L[(a,b)]]) for (a,b) in E})
