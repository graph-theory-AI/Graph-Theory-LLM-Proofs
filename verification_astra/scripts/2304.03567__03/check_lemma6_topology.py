"""Lemma 6, structural claim: replacing every core of F_h by the full tree Q
(a-x, b-x, x-y, y-l, y-r), then contracting the central edges x_w y_w, yields exactly
the 1-subdivision of B_h plus two pendant edges at the top.  Also checks that every
central edge really IS a bridge of the ambient graph."""
import itertools, networkx as nx
from construction import build_B, DSU

def ambient(h):
    """undirected ambient graph of F_h with full Q at every core; returns (G, central_edges)"""
    G=nx.Graph(); dsu=DSU(); central=[]
    def A_(w): return ('A',w)
    def B_(w): return ('B',w)
    def rec(w,d):
        if d==0:
            z=('Z',w); G.add_edge(A_(w),z); G.add_edge(z,B_(w))
        else:
            rec(w+'0',d-1); rec(w+'1',d-1)
            dsu.union(B_(w+'0'),A_(w+'1'))
            x=('x',w); y=('y',w)
            G.add_edge(A_(w),x); G.add_edge(B_(w),x); G.add_edge(x,y)
            G.add_edge(y,A_(w+'0')); G.add_edge(y,B_(w+'1'))
            central.append((x,y))
    rec('',h)
    f=dsu.find
    H=nx.Graph()
    for u,v in G.edges(): H.add_edge(f(u),f(v))
    return H,[(f(x),f(y)) for x,y in central]

def target(h):
    """1-subdivision of B_h, plus two pendants at the root"""
    V,E,M=build_B(h)
    T=nx.Graph()
    for i,(u,v) in enumerate(E):
        s=('sub',u,v); T.add_edge(('m',u),s); T.add_edge(s,('m',v))
    T.add_edge(('m',''),('pend',0)); T.add_edge(('m',''),('pend',1))
    return T

for h in range(1,6):
    H,central=ambient(h)
    # bridge check
    bridges=set(map(frozenset,nx.bridges(H)))
    allbr=all(frozenset(e) in bridges for e in central)
    C=H.copy()
    for x,y in central:
        C=nx.contracted_edge(C,(x,y),self_loops=False)
    T=target(h)
    iso=nx.is_isomorphic(C,T)
    print(f"h={h}: ambient |V|={H.number_of_nodes()} |E|={H.number_of_edges()}; "
          f"{len(central)} central edges, all bridges: {allbr}; "
          f"after contraction |V|={C.number_of_nodes()} |E|={C.number_of_edges()} vs "
          f"target |V|={T.number_of_nodes()} |E|={T.number_of_edges()}; isomorphic: {iso}")
    assert allbr and iso
print("Lemma 6 structural claim verified for h=1..5.")
