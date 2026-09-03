#!/usr/bin/env python3
"""Compare the writeup's Cayley digraph on A4 x Z_m with the Li-Methuku
(arXiv:2607.05807) layered digraph on X x Z_m, X = ordered pairs of
distinct elements of [4], arcs (a,b,t)->(b,c,t+1), c not in {a,b}.
Check digraph isomorphism for m=3, and non-Hamiltonicity of Li-Methuku's
digraph for m=3 by brute force.
"""
import itertools
import networkx as nx

def comp(p, q):
    return tuple(p[q[i]] for i in range(4))

def sign4(p):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    return s

A4 = sorted(p for p in itertools.permutations(range(4)) if sign4(p) == 1)
a = (1, 0, 3, 2)
b = (0, 3, 1, 2)

def gamma(m):
    G = nx.DiGraph()
    for p in A4:
        for i in range(m):
            for s in (a, b):
                G.add_edge((p, i), (comp(p, s), (i + 1) % m))
    return G

def limethuku(m):
    X = [(x, y) for x in range(4) for y in range(4) if x != y]
    G = nx.DiGraph()
    for (x, y) in X:
        for i in range(m):
            for z in range(4):
                if z != x and z != y:
                    G.add_edge((x, y, i), (y, z, (i + 1) % m))
    return G

m = 3
G1 = gamma(m)
G2 = limethuku(m)
print("orders:", G1.number_of_nodes(), G2.number_of_nodes(),
      "sizes:", G1.number_of_edges(), G2.number_of_edges())
print("isomorphic (m=3):", nx.is_isomorphic(G1, G2))

# brute force Hamiltonicity of Li-Methuku digraph, m=3
V = list(G2.nodes())
vi = {v: k for k, v in enumerate(V)}
succ = [[vi[w] for w in G2.successors(v)] for v in V]
N = len(V)
visited = [False] * N
visited[0] = True
def dfs(v, depth):
    if depth == N:
        return 0 in succ[v]
    for w in succ[v]:
        if not visited[w]:
            visited[w] = True
            if dfs(w, depth + 1):
                return True
            visited[w] = False
    return False
import sys
sys.setrecursionlimit(10000)
print("Li-Methuku digraph (m=3) Hamiltonian:", dfs(0, 1))
print("Li-Methuku digraph (m=3) strongly connected:",
      nx.is_strongly_connected(G2))
