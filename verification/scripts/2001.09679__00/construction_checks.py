#!/usr/bin/env python3
"""Referee checks for the construction X(g,L) in the writeup for 2001.09679__00.

Builds X(g,L) exactly as described: g blocks, each a (40L+1)x(40L+1) grid,
with a length-L port centred on each of the 4 sides, ports paired along the
edges of a 4-regular graph H, joined by order-preserving perfect matchings.

Checks:
  A. bounded degree (max degree 5);
  B. in-block distance between distinct ports >= 30L (writeup's dist claim);
  C. Lemma 1(3): L pairwise-disjoint crosscuts per port, each separating its
     port from the other three ports of the block; the 4 collar systems of a
     block are pairwise disjoint;
  D. Lemma 6 locality: for every vertex, the distance to the second-nearest
     other block (=> any ball of radius r < that meets <= 2 blocks), and the
     nearest other block is always adjacent in H; distance to nearest
     NON-adjacent block;
  E. explicit balanced separator of size 4gL = O(gL) (remove all ports);
  F. Lemma 5 pipeline: for F = X and F = random induced subgraph, delete the
     per-port crosscuts minimising |F \\cap C|, check |Z| <= 4n/L, and check
     every component of F - Z is planar and meets at most 2 blocks (adjacent
     in H if 2).
"""
import random
from collections import deque

import networkx as nx

random.seed(7)

L = 3
S = 40 * L + 1          # grid side
G_EXP = 6               # number of expander vertices (structure check only)


def build():
    H = nx.random_regular_graph(4, G_EXP, seed=1)
    assert nx.is_connected(H)
    x0 = (S - L) // 2    # port offset

    def port_vertices(side):
        # side 0=bottom(y=0),1=right(x=S-1),2=top(y=S-1),3=left(x=0)
        if side == 0:
            return [(x0 + i, 0) for i in range(L)]
        if side == 1:
            return [(S - 1, x0 + i) for i in range(L)]
        if side == 2:
            return [(x0 + i, S - 1) for i in range(L)]
        return [(0, x0 + i) for i in range(L)]

    # assign each incident edge of each H-vertex to a distinct side
    side_of = {}
    for v in H.nodes():
        for k, e in enumerate(sorted((tuple(sorted((v, w))) for w in H[v]))):
            side_of[(v, e)] = k

    X = nx.Graph()
    for b in H.nodes():
        for x in range(S):
            for y in range(S):
                if x + 1 < S:
                    X.add_edge((b, x, y), (b, x + 1, y))
                if y + 1 < S:
                    X.add_edge((b, x, y), (b, x, y + 1))
    for e in H.edges():
        e = tuple(sorted(e))
        u, v = e
        pu = port_vertices(side_of[(u, e)])
        pv = port_vertices(side_of[(v, e)])
        for i in range(L):
            X.add_edge((u,) + pu[i], (v,) + pv[i])
    return H, X, port_vertices, side_of, x0


def crosscut(side, k, x0):
    """Depth-k U-shaped crosscut for the given side, in block coordinates."""
    pts = set()
    lo, hi = x0 - k, x0 + L - 1 + k
    if side == 0:
        pts |= {(x, k) for x in range(lo, hi + 1)}
        pts |= {(lo, y) for y in range(k)} | {(hi, y) for y in range(k)}
    elif side == 1:
        pts |= {(S - 1 - k, y) for y in range(lo, hi + 1)}
        pts |= {(x, lo) for x in range(S - k, S)} | {(x, hi) for x in range(S - k, S)}
    elif side == 2:
        pts |= {(x, S - 1 - k) for x in range(lo, hi + 1)}
        pts |= {(lo, y) for y in range(S - k, S)} | {(hi, y) for y in range(S - k, S)}
    else:
        pts |= {(k, y) for y in range(lo, hi + 1)}
        pts |= {(x, lo) for x in range(k)} | {(x, hi) for x in range(k)}
    return pts


def grid_graph():
    Q = nx.Graph()
    for x in range(S):
        for y in range(S):
            if x + 1 < S:
                Q.add_edge((x, y), (x + 1, y))
            if y + 1 < S:
                Q.add_edge((x, y), (x, y + 1))
    return Q


def multi_source_dist(adj, sources, nodes):
    dist = {u: -1 for u in nodes}
    dq = deque()
    for s in sources:
        dist[s] = 0
        dq.append(s)
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if dist[w] < 0:
                dist[w] = dist[u] + 1
                dq.append(w)
    return dist


def main():
    H, X, port_vertices, side_of, x0 = build()
    N = X.number_of_nodes()
    print(f"Built X(g={G_EXP}, L={L}): N={N} vertices, {X.number_of_edges()} edges "
          f"(expected N={G_EXP * S * S})")
    assert N == G_EXP * S * S

    # A. degree bound
    dmax = max(d for _, d in X.degree())
    print(f"A. max degree = {dmax} (claim: bounded, <=5): {'OK' if dmax <= 5 else 'FAIL'}")

    # B. in-block port distances
    Q = grid_graph()
    adjQ = {u: list(Q[u]) for u in Q.nodes()}
    dists = []
    for s1 in range(4):
        d = multi_source_dist(adjQ, port_vertices(s1), Q.nodes())
        for s2 in range(4):
            if s2 != s1:
                dists.append(min(d[p] for p in port_vertices(s2)))
    print(f"B. min in-block distance between distinct ports = {min(dists)} "
          f"(claim >= 30L = {30 * L}): {'OK' if min(dists) >= 30 * L else 'FAIL'}")

    # C. crosscuts: disjoint, in-collar-disjoint across ports, separating
    all_cuts = {}
    union_check = set()
    disjoint = True
    for side in range(4):
        for k in range(1, L + 1):
            c = crosscut(side, k, x0)
            if union_check & c:
                disjoint = False
            union_check |= c
            all_cuts[(side, k)] = c
    sep_ok = True
    for side in range(4):
        for k in range(1, L + 1):
            c = all_cuts[(side, k)]
            Qc = Q.copy()
            Qc.remove_nodes_from(c)
            comp = None
            reach = set()
            for p in port_vertices(side):
                if p in Qc:
                    if comp is None or p not in reach:
                        # BFS from p
                        seen = {p}
                        dq = deque([p])
                        while dq:
                            u = dq.popleft()
                            for w in Qc[u]:
                                if w not in seen:
                                    seen.add(w)
                                    dq.append(w)
                        reach |= seen
            others = set()
            for s2 in range(4):
                if s2 != side:
                    others |= set(port_vertices(s2))
            if reach & others:
                sep_ok = False
    print(f"C. {4 * L} crosscuts pairwise disjoint: {'OK' if disjoint else 'FAIL'}; "
          f"each separates its port from other ports: {'OK' if sep_ok else 'FAIL'}")

    # D. Lemma 6 locality
    adjX = {u: list(X[u]) for u in X.nodes()}
    nodes = list(X.nodes())
    dist_to_block = {}
    for b in H.nodes():
        srcs = [u for u in nodes if u[0] == b]
        dist_to_block[b] = multi_source_dist(adjX, srcs, nodes)
    min_d2 = 10 ** 9
    nearest_adj_ok = True
    min_nonadj = 10 ** 9
    for u in nodes:
        b0 = u[0]
        ds = sorted((dist_to_block[b][u], b) for b in H.nodes() if b != b0)
        d1, b1 = ds[0]
        d2, _ = ds[1]
        min_d2 = min(min_d2, d2)
        if d1 <= 2 * L + 1 and not H.has_edge(b0, b1):
            nearest_adj_ok = False
        for d, b in ds:
            if not H.has_edge(b0, b):
                min_nonadj = min(min_nonadj, d)
                break
    print(f"D. min over vertices of distance to 2nd-nearest other block = {min_d2} "
          f"(so every ball of radius r <= {min_d2 - 1} meets <= 2 blocks; "
          f"{min_d2 - 1}/L = {(min_d2 - 1) / L:.1f})")
    print(f"   nearest other block within 2r+1 is H-adjacent: "
          f"{'OK' if nearest_adj_ok else 'FAIL'}; "
          f"min distance to a NON-adjacent block = {min_nonadj} "
          f"({min_nonadj / L:.1f} L)")

    # E. explicit balanced separator: all ports
    Z = set()
    for e in H.edges():
        e = tuple(sorted(e))
        u, v = e
        Z |= {(u,) + p for p in port_vertices(side_of[(u, e)])}
        Z |= {(v,) + p for p in port_vertices(side_of[(v, e)])}
    Xz = X.copy()
    Xz.remove_nodes_from(Z)
    mx = max(len(c) for c in nx.connected_components(Xz))
    print(f"E. |Z|={len(Z)} = 4gL = {4 * G_EXP * L}; max component after removal = {mx} "
          f"<= 2N/3 = {2 * N // 3}: {'OK' if mx <= 2 * N / 3 else 'FAIL'} "
          f"=> sep(X) <= {len(Z)} = O(gL)")

    # F. Lemma 5 pipeline
    for label, F in (("F = X", X),
                     ("F = random induced subgraph (p=0.6)",
                      X.subgraph([u for u in X.nodes() if random.random() < 0.6]).copy())):
        n = F.number_of_nodes()
        Z5 = set()
        for b in H.nodes():
            for side in range(4):
                best = None
                for k in range(1, L + 1):
                    cnt = {(b,) + p for p in all_cuts[(side, k)]} & set(F.nodes())
                    if best is None or len(cnt) < len(best):
                        best = cnt
                Z5 |= best
        ok_size = len(Z5) <= 4 * n / L
        Fz = F.copy()
        Fz.remove_nodes_from(Z5)
        comps = list(nx.connected_components(Fz))
        all_planar = True
        blocks_ok = True
        maxblocks = 0
        for c in comps:
            bl = {u[0] for u in c}
            maxblocks = max(maxblocks, len(bl))
            if len(bl) > 2 or (len(bl) == 2 and not H.has_edge(*bl)):
                blocks_ok = False
            planar, _ = nx.check_planarity(F.subgraph(c), counterexample=False)
            if not planar:
                all_planar = False
        print(f"F. [{label}] n={n}, |Z|={len(Z5)} <= 4n/L={4 * n / L:.0f}: "
              f"{'OK' if ok_size else 'FAIL'}; {len(comps)} components, "
              f"max blocks/component={maxblocks} (<=2, adjacent): "
              f"{'OK' if blocks_ok else 'FAIL'}; all components planar: "
              f"{'OK' if all_planar else 'FAIL'}; "
              f"max component size={max(len(c) for c in comps)} (n*2/3={2 * n / 3:.0f})")


if __name__ == "__main__":
    main()
