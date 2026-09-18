"""Enumerate connected (0,2)-graphs on n vertices via nauty geng, and for each one
report: order, degree, bipartite?, chromatic number, and whether the Lemma of the
writeup holds (quadrangles span the cycle space over R).

A (0,2)-graph: every pair of DISTINCT vertices has 0 or exactly 2 common neighbours.
"""
import subprocess, sys, itertools
import numpy as np
import networkx as nx

GENG = "/usr/bin/geng"


def g6_stream(n, k):
    """connected k-regular graphs on n vertices in graph6"""
    cmd = [GENG, "-q", "-c", f"-d{k}", f"-D{k}", str(n)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    for line in p.stdout.splitlines():
        line = line.strip()
        if line:
            yield line


def is_02(G):
    nodes = list(G.nodes())
    adj = {v: set(G[v]) for v in nodes}
    for u, v in itertools.combinations(nodes, 2):
        c = len(adj[u] & adj[v])
        if c not in (0, 2):
            return False
    return True


def chromatic_number(G, cap=8):
    n = G.number_of_nodes()
    if G.number_of_edges() == 0:
        return 1
    if nx.is_bipartite(G):
        return 2
    for k in range(3, cap + 1):
        if k_colorable(G, k):
            return k
    return None


def k_colorable(G, k):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    idx = {v: i for i, v in enumerate(nodes)}
    adj = [[idx[w] for w in G[v]] for v in nodes]
    n = len(nodes)
    color = [-1] * n

    def bt(i, used):
        if i == n:
            return True
        forb = set(color[j] for j in adj[i] if color[j] >= 0)
        for c in range(min(used + 1, k)):
            if c in forb:
                continue
            color[i] = c
            if bt(i + 1, max(used, c + 1)):
                return True
            color[i] = -1
        return False

    return bt(0, 0)


def squares_span_cycle_space(G):
    """Return (dim cycle space, rank of span of quadrangle vectors over R)."""
    edges = list(G.edges())
    eidx = {}
    for i, (x, y) in enumerate(edges):
        eidx[(x, y)] = (i, 1)
        eidx[(y, x)] = (i, -1)
    m = len(edges)
    n = G.number_of_nodes()
    c = nx.number_connected_components(G)
    cyc_dim = m - n + c
    rows = []
    # all 4-cycles (as vertex sets traversals), enumerated as closed walks u-v-b-a-u
    seen = set()
    nodes = list(G.nodes())
    for u in nodes:
        for v in G[u]:
            for b in G[v]:
                if b == u:
                    continue
                for a in G[b]:
                    if a == v or a == u:
                        continue
                    if not G.has_edge(a, u):
                        continue
                    key = frozenset([(u, v), (v, b), (b, a), (a, u)])
                    key = frozenset(frozenset(e) for e in [(u, v), (v, b), (b, a), (a, u)])
                    ck = (key, )
                    if ck in seen:
                        continue
                    seen.add(ck)
                    row = np.zeros(m)
                    for (x, y) in [(u, v), (v, b), (b, a), (a, u)]:
                        i, s = eidx[(x, y)]
                        row[i] += s
                    rows.append(row)
    if not rows:
        return cyc_dim, 0
    A = np.array(rows)
    return cyc_dim, int(np.linalg.matrix_rank(A, tol=1e-8))


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    nmin = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    total = 0
    for n in range(nmin, nmax + 1):
        for k in range(1, n):
            if (n * k) % 2:
                continue
            for g6 in g6_stream(n, k):
                G = nx.from_graph6_bytes(g6.encode())
                if not is_02(G):
                    continue
                total += 1
                bip = nx.is_bipartite(G)
                chi = chromatic_number(G)
                cd, rk = squares_span_cycle_space(G)
                flag = "LEMMA-FAILS" if rk != cd else "lemma-ok"
                mark = ""
                if chi == 3:
                    mark = "  <<<< CHI=3 !!!!"
                print(f"n={n:3d} k={k:3d} g6={g6:20s} bipartite={bip!s:5s} chi={chi} "
                      f"cycdim={cd} squarerank={rk} {flag}{mark}", flush=True)
    print(f"# total connected (0,2)-graphs found for n<={nmax}: {total}")


if __name__ == "__main__":
    main()
