"""Section 3 lemma: K_{p/q} is locally bipartite whenever p < 4q (and NOT when p >= 4q).
Also verifies the stated A/B bipartition, and the Section 2 pigeonhole/Vandermonde claim."""
import itertools, networkx as nx
from fractions import Fraction

def Kpq(p, q):
    G = nx.Graph(); G.add_nodes_from(range(p))
    for a in range(p):
        for b in range(a+1, p):
            d = (b-a) % p
            if q <= d <= p-q: G.add_edge(a, b)
    return G

def locally_bipartite(G):
    return all(nx.is_bipartite(G.subgraph(list(G.neighbors(v)))) for v in G)

bad = []
for q in range(1, 13):
    for p in range(2*q, 6*q+1):
        G = Kpq(p, q)
        lb = locally_bipartite(G)
        pred = (p < 4*q)
        if lb != pred: bad.append((p, q, lb, pred))
        if p < 4*q:   # check the writeup's explicit A,B bipartition of N(0)
            N0 = set(range(q, p-q+1))
            A = N0 & set(range(q, 2*q)); B = N0 & set(range(2*q, 3*q))
            assert A | B == N0, (p, q, "A,B do not cover N(0)")
            for S in (A, B):
                for x, y in itertools.combinations(sorted(S), 2):
                    d = (y-x) % p
                    assert not (q <= d <= p-q), (p, q, "block not independent")
print("K_{p/q} locally-bipartite <=> p<4q, tested q=1..12, p=2q..6q :",
      "ALL MATCH" if not bad else bad)

# smallest p<4q ratios and their local bipartiteness, plus the >=4q boundary
for (p, q) in [(7,2),(11,3),(15,4),(19,5),(23,6),(4,1),(8,2),(12,3),(9,2)]:
    G = Kpq(p, q)
    print(f"  K_{{{p}/{q}}} = {Fraction(p,q)}  locally bipartite: {locally_bipartite(G)}  (p<4q: {p<4*q})")

# Section 2 pigeonhole: any 3 of [(1,j,j^2)] are independent
import numpy as np
from sympy import Matrix
ok = all(Matrix([[1,i,i*i],[1,j,j*j],[1,k,k*k]]).det() == (j-i)*(k-i)*(k-j) != 0
         for i,j,k in itertools.combinations(range(1, 26), 3))
print("moment-curve lines: every triple linearly independent, det formula exact:", ok)
m = 7
print(f"  with m={m} vertices in H and 2m+1={2*m+1} lines, some fibre has >= ceil((2m+1)/m) = {-(-(2*m+1)//m)} lines")
