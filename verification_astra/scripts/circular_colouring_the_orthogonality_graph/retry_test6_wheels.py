"""Cross-check of Section 3 from the other side: the lemma 'K_{p/q} is locally bipartite
for p<4q' is exactly equivalent to 'every odd wheel has circular chromatic number 4'.
Compute chi_c of odd wheels by brute force and confirm."""
import itertools, networkx as nx
from fractions import Fraction
from math import gcd

def Kpq(p, q):
    G = nx.Graph(); G.add_nodes_from(range(p))
    for a in range(p):
        for b in range(a+1, p):
            d = (b-a) % p
            if q <= d <= p-q: G.add_edge(a, b)
    return G

def hom_exists(G, H):
    Gv = sorted(G, key=lambda v: -G.degree(v)); Hv = list(H)
    Hadj = {u: set(H.neighbors(u)) for u in Hv}
    assign = {}
    def bt(i):
        if i == len(Gv): return True
        v = Gv[i]
        for c in Hv:
            if all(assign[u] in Hadj[c] for u in G.neighbors(v) if u in assign):
                assign[v] = c
                if bt(i+1): return True
                del assign[v]
        return False
    return bt(0)

def chi_c(G):
    n = G.number_of_nodes()
    if G.number_of_edges() == 0: return Fraction(1)
    best = None
    for p in range(2, n+1):
        for q in range(1, p//2+1):
            if gcd(p, q) != 1: continue
            r = Fraction(p, q)
            if best is not None and r >= best: continue
            if hom_exists(G, Kpq(p, q)): best = r
    return best

for n in (3, 5, 7, 9):
    W = nx.Graph()
    W.add_edges_from([(i, (i+1) % n) for i in range(n)])
    W.add_edges_from([('h', i) for i in range(n)])
    c = chi_c(W)
    hubnb = W.subgraph([i for i in range(n)])
    print(f"W_{n} (hub + C_{n}): chi = {max(nx.coloring.greedy_color(W, strategy='DSATUR').values())+1}, "
          f"hub neighbourhood bipartite = {nx.is_bipartite(hubnb)}, chi_c = {c}")
# calibration
print("calibration: chi_c(C5) =", chi_c(nx.cycle_graph(5)), " chi_c(K4) =", chi_c(nx.complete_graph(4)),
      " chi_c(Petersen) =", chi_c(nx.petersen_graph()), " chi_c(K_{7/2}) =", chi_c(Kpq(7,2)),
      " chi_c(K_{11/3}) =", chi_c(Kpq(11,3)))
