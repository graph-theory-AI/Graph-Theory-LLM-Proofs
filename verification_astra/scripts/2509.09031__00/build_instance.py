"""Build small instances of the writeup's construction and verify its claims.

H  : 4-regular, high girth, edges partitioned into red/blue 2-factors
H+ : subdivision of K_{V(H)}; H-edges -> path of length S, non-edges -> length M
G  : split each v into v_R,v_B joined by a switch edge (length 1);
     red corridors at R-vertices, blue at B-vertices, long corridors at R-vertices.
p  : G -> H+ collapsing switch edges.
"""
import itertools
import networkx as nx


def circulant(n, k):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    red, blue = set(), set()
    for v in range(n):
        e = (min(v, (v + 1) % n), max(v, (v + 1) % n))
        G.add_edge(*e); red.add(e)
        e = (min(v, (v + k) % n), max(v, (v + k) % n))
        G.add_edge(*e); blue.add(e)
    return G, red, blue


def girth(G):
    best = float('inf')
    for u in G:
        # BFS tree, find shortest cycle through u
        dist = {u: 0}
        par = {u: None}
        q = [u]
        while q:
            nq = []
            for x in q:
                for y in G[x]:
                    if y not in dist:
                        dist[y] = dist[x] + 1
                        par[y] = x
                        nq.append(y)
                    elif y != par[x]:
                        best = min(best, dist[x] + dist[y] + 1)
            q = nq
    return best


def mono_cycle_lengths(G, colset):
    S = nx.Graph(); S.add_nodes_from(G); S.add_edges_from(colset)
    return sorted(len(c) for c in nx.connected_components(S))


def build_Hplus(H, S, M):
    Hp = nx.Graph()
    V = list(H.nodes())
    for u, v in itertools.combinations(V, 2):
        L = S if H.has_edge(u, v) else M
        prev = ('B', u)
        for i in range(L - 1):
            cur = ('I', u, v, i)
            Hp.add_edge(prev, cur); prev = cur
        Hp.add_edge(prev, ('B', v))
    return Hp


def build_G(H, red, blue, S, M):
    G = nx.Graph()
    V = list(H.nodes())
    for v in V:
        G.add_edge(('B', v, 'R'), ('B', v, 'B'))          # switch edge
    def corridor(a, b, L, tag):
        prev = a
        for i in range(L - 1):
            cur = ('I', tag, i)
            G.add_edge(prev, cur); prev = cur
        G.add_edge(prev, b)
    for u, v in itertools.combinations(V, 2):
        e = (min(u, v), max(u, v))
        tag = (u, v)
        if e in red:
            corridor(('B', u, 'R'), ('B', v, 'R'), S, tag)
        elif e in blue:
            corridor(('B', u, 'B'), ('B', v, 'B'), S, tag)
        else:
            corridor(('B', u, 'R'), ('B', v, 'R'), M, tag)
    return G


def proj(x):
    """p : V(G) -> V(H+)"""
    if x[0] == 'B':
        return ('B', x[1])
    return ('I',) + x[1] + (x[2],) if False else ('I', x[1][0], x[1][1], x[2])
