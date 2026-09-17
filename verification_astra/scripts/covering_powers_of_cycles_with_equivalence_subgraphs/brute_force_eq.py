#!/usr/bin/env python3
"""Exact equivalence covering number eq(C_n^k) by brute force.

An equivalence subgraph of G is a spanning subgraph whose components are cliques,
i.e. a partition of V(G) into cliques of G.  eq(G) is the least number of such
partitions whose edge sets cover E(G).

Method: enumerate every partition of V into cliques, keep the inclusion-maximal
edge sets, then solve the minimum set cover exactly by iterative deepening with
the "branch on a least-coverable uncovered edge" rule.
"""
import itertools
import sys
from functools import lru_cache


def cyc_dist(a, b, n):
    d = (a - b) % n
    return min(d, n - d)


def build(n, k):
    adj = [0] * n
    E = []
    for u in range(n):
        for v in range(n):
            if u != v and cyc_dist(u, v, n) <= k:
                adj[u] |= 1 << v
    for u in range(n):
        for v in range(u + 1, n):
            if adj[u] >> v & 1:
                E.append((u, v))
    return adj, E


def clique_partitions(n, adj):
    """Yield every partition of [n] into cliques, as a list of vertex bitmasks."""
    parts = []
    out = []

    def rec(assigned):
        if assigned == (1 << n) - 1:
            out.append(tuple(parts))
            return
        v = (~assigned & ((1 << n) - 1)).bit_length() - 1
        # lowest unassigned vertex
        v = 0
        while assigned >> v & 1:
            v += 1
        # option: join an existing part (only parts whose members are all adjacent to v)
        for i, p in enumerate(parts):
            if p & ~adj[v] == 0:
                parts[i] = p | (1 << v)
                rec(assigned | (1 << v))
                parts[i] = p
        # option: start a new part
        parts.append(1 << v)
        rec(assigned | (1 << v))
        parts.pop()

    rec(0)
    return out


def edgeset_mask(parts, eidx):
    m = 0
    for p in parts:
        vs = [i for i in range(p.bit_length()) if p >> i & 1]
        for a, b in itertools.combinations(vs, 2):
            m |= 1 << eidx[(a, b)]
    return m


def min_cover(universe, sets, limit=8):
    sets = sorted(set(sets), key=lambda m: -bin(m).count("1"))
    # drop non-maximal sets
    maximal = []
    for i, s in enumerate(sets):
        if not any(s != t and s & ~t == 0 for t in sets):
            maximal.append(s)
    sets = maximal
    ne = universe.bit_length()
    by_edge = [[] for _ in range(ne)]
    for s in sets:
        for e in range(ne):
            if s >> e & 1:
                by_edge[e].append(s)

    best = None

    def rec(uncov, depth, budget):
        nonlocal best
        if uncov == 0:
            return depth
        if budget == 0:
            return None
        # branch on the uncovered edge with fewest covering sets
        beste, bestlist = None, None
        for e in range(ne):
            if uncov >> e & 1:
                lst = by_edge[e]
                if bestlist is None or len(lst) < len(bestlist):
                    beste, bestlist = e, lst
                if len(lst) <= 1:
                    break
        for s in bestlist:
            got = rec(uncov & ~s, depth + 1, budget - 1)
            if got is not None:
                return got
        return None

    for t in range(1, limit + 1):
        if rec(universe, 0, t) is not None:
            return t, len(sets)
    return None, len(sets)


def eq_value(n, k, limit=8, verbose=False):
    adj, E = build(n, k)
    eidx = {e: i for i, e in enumerate(E)}
    universe = (1 << len(E)) - 1
    parts_list = clique_partitions(n, adj)
    masks = {edgeset_mask(p, eidx) for p in parts_list}
    t, nsets = min_cover(universe, masks)
    return t, len(E), len(parts_list), nsets


def main():
    print("n, k, eq(C_n^k) exact, |E|, #clique-partitions, #maximal layers, "
          "r=ceil(log2(k+1)), lower bd r+1, upper bd 2r+1, S2 bound r+1 if (k+1)|n")
    rows = []
    cases = []
    for n in range(4, 14):
        for k in range(1, n):
            if n <= 2 * k + 1:
                continue  # complete graph, eq = 1
            cases.append((n, k))
    for (n, k) in cases:
        s = k + 1
        r = max(1, (s - 1).bit_length())
        t, ne, npart, nsets = eq_value(n, k)
        div = (n % s == 0)
        flag = ""
        if t is None:
            flag = "  UNRESOLVED(limit)"
        else:
            if t < r + 1:
                flag += "  *** BELOW CLAIMED LOWER BOUND r+1 ***"
            if t > 2 * r + 1:
                flag += "  *** ABOVE CLAIMED UPPER BOUND 2r+1 ***"
            if div and t != r + 1:
                flag += "  *** EXACT FORMULA r+1 VIOLATED ***"
        print(f"n={n:3d} k={k:3d} eq={t}  |E|={ne:3d} parts={npart:7d} maxlayers={nsets:5d} "
              f"r={r} [{r+1},{2*r+1}] div={int(div)}{flag}")
        sys.stdout.flush()
        rows.append((n, k, t, r, div))
    print()
    bad = [row for row in rows if row[2] is None or row[2] < row[3] + 1 or row[2] > 2 * row[3] + 1
           or (row[4] and row[2] != row[3] + 1)]
    print("violations:", bad if bad else "NONE")


if __name__ == "__main__":
    main()
