"""Independent check of the writeup on larger (0,2)-graphs.

Family used: cube-like (0,2)-graphs.  Cay(Z_2^m, S) has, for x != y with d = x+y,
exactly #{(s,t) in SxS : s+t = d} common neighbours.  That count is 0 or 2 for every
d != 0 iff S is a Sidon set (all pairwise sums of distinct elements are distinct).
So Sidon sets in Z_2^m give (0,2)-graphs on 2^m vertices.  These include the
hypercubes (S = standard basis) and Payan's chi = 4 / chi = 5 examples.

For each graph we check
  (a) the (0,2) property, by brute force over all vertex pairs;
  (b) the matching property (1) of the writeup: for every edge uv the map
      a |-> (second common neighbour of v,a) is a bijection N(u)\\{v} -> N(v)\\{u}
      with a*phi(a) an edge;
  (c) the Lemma: the quadrangles span the cycle space over R, equivalently every
      square-closed antisymmetric edge function is a potential difference;
  (d) the chromatic number (exactly, via SAT-free backtracking, capped).
"""
import itertools, sys, os
import numpy as np, networkx as nx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enumerate_02 import is_02, chromatic_number, squares_span_cycle_space, k_colorable


def sidon_sets(m, size, limit=200):
    """Sidon subsets of Z_2^m \\ {0} of given size (as tuples of ints), up to `limit`."""
    elems = list(range(1, 1 << m))
    out = []
    def rec(start, cur):
        if len(out) >= limit:
            return
        if len(cur) == size:
            out.append(tuple(cur))
            return
        for e in range(start, 1 << m):
            ok = True
            # Sidon in Z_2^m: all pairwise XORs of distinct elements are distinct
            sums = set(a ^ b for a, b in itertools.combinations(cur, 2))
            for c in cur:
                s = c ^ e
                if s in sums or s == 0:
                    ok = False
                    break
                sums.add(s)
            if ok:
                rec(e + 1, cur + [e])
    rec(1, [])
    return out


def cayley(m, S):
    G = nx.Graph()
    G.add_nodes_from(range(1 << m))
    for x in range(1 << m):
        for s in S:
            G.add_edge(x, x ^ s)
    return G


def matching_property(G):
    """Verify property (1) of the writeup for every edge."""
    adj = {v: set(G[v]) for v in G}
    for u, v in G.edges():
        for (x, y) in ((u, v), (v, u)):
            A = adj[x] - {y}
            B = adj[y] - {x}
            img = set()
            for a in A:
                common = adj[y] & adj[a]
                if len(common) != 2 or x not in common:
                    return False, f"pair ({y},{a}) has common nbrs {common}"
                b = (common - {x}).pop()
                if b not in B or not G.has_edge(a, b) or b == a:
                    return False, f"phi({a}) = {b} bad"
                img.add(b)
            if img != B:
                return False, f"phi not onto for edge {x}{y}"
    return True, "ok"


def report(name, G):
    n, mm = G.number_of_nodes(), G.number_of_edges()
    ok02 = is_02(G)
    okm, msg = matching_property(G) if ok02 else (None, "n/a")
    cd, rk = squares_span_cycle_space(G)
    chi = chromatic_number(G, cap=10)
    print(f"{name:34s} n={n:3d} m={mm:4d} (0,2)={ok02} matching={okm} "
          f"cycdim={cd:4d} squarerank={rk:4d} lemma={'OK' if rk == cd else 'FAILS'} "
          f"bip={nx.is_bipartite(G)} chi={chi}"
          + ("   <<<< CHI=3 !!!!" if chi == 3 else ""), flush=True)
    return chi


if __name__ == "__main__":
    # hypercubes
    for m in range(1, 7):
        S = [1 << i for i in range(m)]
        report(f"Q_{m} (hypercube)", cayley(m, S))
    # K_4 and the two sporadic small non-bipartite ones found by enumeration
    report("K_4", nx.complete_graph(4))
    report("n=8 k=4 (0,2)-graph", nx.from_graph6_bytes(b"GQzTrg"))
    report("n=12 k=5 (0,2)-graph", nx.from_graph6_bytes(b"KCpdQiqZeqEk"))
    report("n=14 k=4 (0,2)-graph", nx.from_graph6_bytes(b"M???FbKickF_U_X_?"))
    # all cube-like (0,2)-graphs from Sidon sets in Z_2^m, m <= 5, plus m=6 samples
    chis = {}
    for m in range(2, 6):
        for size in range(2, (1 << m)):
            sets = sidon_sets(m, size, limit=40)
            if not sets:
                continue
            for S in sets:
                G = cayley(m, list(S))
                if G.number_of_edges() == 0:
                    continue
                c = report(f"Cay(Z_2^{m}, {S})", G)
                chis.setdefault(c, 0)
                chis[c] += 1
    print("chromatic numbers seen among cube-like (0,2)-graphs:", chis)
