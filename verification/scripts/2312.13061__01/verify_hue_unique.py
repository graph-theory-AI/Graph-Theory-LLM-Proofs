#!/usr/bin/env python3
"""
Verify that the 3-coloring (hue) of the constructed near-Eulerian-triangulation
G is unique up to permutation of the three hues, by propagation across
triangles: in a triangulation, once one triangle's hues are fixed, every
adjacent triangle's third vertex is forced. If the weak dual is connected and
propagation is globally consistent, the 3-coloring is unique up to permutation
(3! = 6 choices on the starting triangle).

Consequence: the hues along the outer 6-cycle C necessarily alternate between
two values (as in verify_construction.py), so the viability computation there
covers every admissible hue of G.
"""
import sys
from collections import deque

sys.path.insert(0, ".")
from verify_construction import build  # noqa: E402

import networkx as nx  # noqa: E402


def main():
    k = 1
    H, C, faces, cell_faces, names, L, m, n = build(k)
    G = H.copy()
    apex_of_face = {}
    for idx, fc in enumerate(faces):
        u = ("apex", idx)
        apex_of_face[idx] = u
        for v in fc:
            G.add_edge(u, v)

    # triangles of G and weak dual
    triangles = []
    edge2tris = {}
    for idx, fc in enumerate(faces):
        u = apex_of_face[idx]
        t = len(fc)
        for i in range(t):
            p, q = fc[i], fc[(i + 1) % t]
            tid = len(triangles)
            triangles.append((u, p, q))
            for e in (frozenset((p, q)), frozenset((p, u)), frozenset((q, u))):
                edge2tris.setdefault(e, []).append(tid)

    D = nx.Graph()
    D.add_nodes_from(range(len(triangles)))
    for e, ts in edge2tris.items():
        if len(ts) == 2:
            D.add_edge(ts[0], ts[1], shared=e)
    assert nx.is_connected(D), "weak dual not connected"

    # propagate a 3-coloring from triangle 0
    col = {}
    t0 = triangles[0]
    for i, v in enumerate(t0):
        col[v] = i
    q = deque([0])
    seen = {0}
    while q:
        t = q.popleft()
        for t2 in D[t]:
            tri2 = triangles[t2]
            known = [v for v in tri2 if v in col]
            unknown = [v for v in tri2 if v not in col]
            assert len(known) >= 2
            if unknown:
                forced = ({0, 1, 2} - {col[v] for v in known})
                assert len(forced) == 1, "inconsistent propagation"
                col[unknown[0]] = forced.pop()
            else:
                assert len({col[v] for v in tri2}) == 3, \
                    "propagation inconsistent on closed triangle"
            if t2 not in seen:
                seen.add(t2)
                q.append(t2)
    assert seen == set(D.nodes())
    assert len(col) == G.number_of_nodes()
    # proper?
    assert all(col[a] != col[b] for a, b in G.edges())
    hueC = [col[v] for v in C]
    print("propagated (unique up to permutation) hue along C:", hueC)
    vals = set(hueC)
    assert len(vals) == 2, "hue on C does not alternate between two values!"
    assert all(hueC[i] != hueC[(i + 1) % 6] for i in range(6))
    print("OK: G's 3-coloring is unique up to permutation of hues, and the")
    print("hue along C alternates between two values, as assumed in the")
    print("viability computation.")


if __name__ == "__main__":
    main()
