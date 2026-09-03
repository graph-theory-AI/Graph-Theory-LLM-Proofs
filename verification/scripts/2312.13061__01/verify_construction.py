#!/usr/bin/env python3
"""
Independent verification of the claimed counterexample to Conjecture 4 of
arXiv:2312.13061 (Dvorak, Moore, Seifrtova, Samal), from attack 2312.13061__01.

Construction (writeup, sections 2-6), for a given k (playing the role of d):
  L = 4k+4, m = (k+1)L, n = 2L.
  K = m x n rectangular grid (vertices (i,j), 0<=i<=m, 0<=j<=n) with every
      edge subdivided into a path of length 3.
  B = subdivision path of boundary edge (0,0)-(1,0):  x b1 b2 y.
  A = new ear x a1 a2 y drawn in the old outer face.
  C = A u B (a 6-cycle) bounds the outer face; f = A u P is a new bounded
      face, where P = D0 - interior(B), D0 the old outer cycle of K.
  H = K + A.  G = stellation of every bounded face of H (apex set U).
  S = the k grid-cell faces with lower-left corners (jL, L), j = 1..k.
  Precoloring of C = (x,a1,a2,y,b2,b1) -> (1,2,3,4,3,2).

Checks performed (all against the paper's own definitions):
  1. H is bipartite, girth(H) = 6 (hence no 4-cycles, and no closed walk of
     length < 6 can separate anything).
  2. The face lists form a genuine plane embedding (every edge of H on exactly
     2 faces; Euler's formula for H and for G).
  3. G is a planar near-Eulerian-triangulation: simple, planar, 2-connected,
     all bounded faces triangles, outer face bounded by the 6-cycle C, every
     vertex not on C has even degree.
  4. U independent, disjoint from C, G-U = H.
  5. Faces of S have length 12 >= 6; pairwise distance in H >= k = d
     (vertex-to-vertex BFS distance between face boundaries).
  6. Viability of the precoloring per the paper's definition: the hue of C
     (restriction of a proper 3-colouring of G, which is unique up to
     permutation since G is 2-connected) alternates; delta(C) = (0,0) using
     the paper's sigma/delta formulas (proof of Theorem thm-main); and an
     explicit homomorphism of C^phi into the dappled triangular grid is
     exhibited and verified (brute force over all base points in a chunk).
  7. Non-extension: u_f is adjacent in G to x,a1,a2,y, which carry the four
     distinct colors 1,2,3,4.
  8. The writeup's auxiliary claims: weak dual of G bipartite, |D+| = |D-|,
     boundary-triangle signs alternate around C, and the three signed
     type-sums of condition (1) all vanish.
"""

import itertools
import sys
from collections import deque

import networkx as nx


def subdiv_name(u, v, idx):
    a, b = (u, v) if u <= v else (v, u)
    if (u, v) != (a, b):
        idx = 3 - idx  # keep orientation consistent: idx counted from a
    return ("s", a, b, idx)


def build(k):
    L = 4 * k + 4
    m = (k + 1) * L
    n = 2 * L

    # --- original grid ---
    grid_edges = []
    for i in range(m + 1):
        for j in range(n + 1):
            if i < m:
                grid_edges.append(((i, j), (i + 1, j)))
            if j < n:
                grid_edges.append(((i, j), (i, j + 1)))

    H = nx.Graph()
    for (u, v) in grid_edges:
        s1 = subdiv_name(u, v, 1)
        s2 = subdiv_name(u, v, 2)
        H.add_edge(u, s1)
        H.add_edge(s1, s2)
        H.add_edge(s2, v)

    def sub_path(u, v):
        """subdivided path from u to v (inclusive)."""
        return [u, subdiv_name(u, v, 1), subdiv_name(u, v, 2), v]

    # --- bounded faces of K: the m*n cells, each a 12-cycle ---
    cell_faces = {}
    for i in range(m):
        for j in range(n):
            cyc = []
            corners = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
            for t in range(4):
                p = sub_path(corners[t], corners[(t + 1) % 4])
                cyc.extend(p[:-1])
            cell_faces[(i, j)] = cyc

    # --- old outer cycle D0 of K (counterclockwise from (0,0)) ---
    D0 = []
    bottom = [(i, 0) for i in range(m + 1)]
    right = [(m, j) for j in range(n + 1)]
    top = [(i, n) for i in range(m, -1, -1)]
    left = [(0, j) for j in range(n, -1, -1)]
    boundary_corners = bottom + right[1:] + top[1:] + left[1:-1]
    for t in range(len(boundary_corners)):
        u = boundary_corners[t]
        v = boundary_corners[(t + 1) % len(boundary_corners)]
        D0.extend(sub_path(u, v)[:-1])

    x = (0, 0)
    y = (1, 0)
    b1 = subdiv_name(x, y, 1)
    b2 = subdiv_name(x, y, 2)
    assert D0[0] == x and D0[1] == b1 and D0[2] == b2 and D0[3] == y

    # --- ear A ---
    a1, a2 = "a1", "a2"
    H.add_edge(x, a1)
    H.add_edge(a1, a2)
    H.add_edge(a2, y)

    C = [x, a1, a2, y, b2, b1]  # outer cycle, c0..c5 as in the writeup

    # face f = A u P, P = D0 minus interior of B
    P = D0[3:] + [x]  # from y around the rectangle back to x (excl. b1,b2)
    f_face = [x, a1, a2, y] + D0[4:]  # cyclic vertex list of face f
    faces = list(cell_faces.values()) + [f_face]

    return H, C, faces, cell_faces, (x, a1, a2, y, b2, b1), L, m, n


def check_embedding(H, faces, C):
    """Every edge of H must lie on exactly 2 faces (bounded faces + outer C)."""
    from collections import Counter
    cnt = Counter()
    all_faces = faces + [C]
    for face in all_faces:
        t = len(face)
        for i in range(t):
            u, v = face[i], face[(i + 1) % t]
            assert H.has_edge(u, v), f"face lists non-edge {u},{v}"
            cnt[frozenset((u, v))] += 1
    assert set(cnt.values()) == {2}, "some edge not on exactly 2 faces"
    assert len(cnt) == H.number_of_edges()
    # Euler for H
    V, E, F = H.number_of_nodes(), H.number_of_edges(), len(all_faces)
    assert V - E + F == 2, f"Euler fails for H: {V}-{E}+{F}"
    return V, E, F


def girth(G):
    best = float("inf")
    for src in G.nodes():
        dist = {src: 0}
        parent = {src: None}
        q = deque([src])
        while q:
            u = q.popleft()
            if 2 * dist[u] >= best:
                continue
            for w in G[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    parent[w] = u
                    q.append(w)
                elif parent[u] != w and parent[w] != u:
                    best = min(best, dist[u] + dist[w] + 1)
        if best == 3:
            break
    return best


def face_distance(H, f1, f2):
    """min BFS distance between vertex sets of two face boundaries."""
    targets = set(f2)
    dist = {v: 0 for v in f1}
    q = deque(f1)
    while q:
        u = q.popleft()
        if u in targets:
            return dist[u]
        for w in H[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                q.append(w)
    return float("inf")


COLOR = {1: (0, 0), 2: (0, 1), 3: (1, 0), 4: (1, 1)}


def delta_edge(hue_u, hue_v, col_u, col_v):
    a = (hue_v - hue_u) % 3
    b = (COLOR[col_v][0] - COLOR[col_u][0]) % 2
    c = (COLOR[col_v][1] - COLOR[col_u][1]) % 2
    assert a in (1, 2) and (b, c) != (0, 0)
    sigma = 1 if a == (b + c) else -1
    return (sigma * b, sigma * c)


def grid_hue(p):
    return (p[0] + p[1]) % 3


def grid_col(p):
    return (p[0] % 2, p[1] % 2)


def grid_adj(p, q):
    d = (q[0] - p[0], q[1] - p[1])
    return d in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]


def brute_force_hom(hues, cols, R=8):
    """All homomorphisms of the dappled cycle into the [-R,R]^2 grid chunk,
    up to the (forced) continuation: try every base point for c0."""
    t = len(hues)
    found = []
    for i0 in range(-R, R + 1):
        for j0 in range(-R, R + 1):
            p = (i0, j0)
            if grid_hue(p) != hues[0] or grid_col(p) != COLOR[cols[0]]:
                continue
            img = [p]
            ok = True
            for s in range(1, t + 1):
                hs, cs = hues[s % t], COLOR[cols[s % t]]
                nxts = [q for q in
                        [(p[0] + dx, p[1] + dy)
                         for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1),
                                          (1, 1), (-1, -1)]]
                        if grid_hue(q) == hs and grid_col(q) == cs]
                assert len(nxts) <= 1  # Observation obs-homtot: forced
                if not nxts:
                    ok = False
                    break
                p = nxts[0]
                img.append(p)
            if ok and img[-1] == img[0]:
                found.append(img)
    return found


def main():
    for k in (1, 2):
        print(f"===== k = d = {k} =====")
        H, C, faces, cell_faces, names, L, m, n = build(k)
        x, a1, a2, y, b2, b1 = names
        print(f"L={L}, m={m}, n={n}; |V(H)|={H.number_of_nodes()}, "
              f"|E(H)|={H.number_of_edges()}, bounded faces of H={len(faces)}")

        # 1. bipartite + girth
        assert nx.is_bipartite(H), "H not bipartite"
        g = girth(H)
        print(f"girth(H) = {g}")
        assert g == 6

        # face lengths of H all even; f has the right length
        lens = sorted(set(len(fc) for fc in faces))
        print(f"bounded face lengths of H: {lens[:3]}...{lens[-1]} "
              f"(f has length {len(faces[-1])})")
        assert all(l % 2 == 0 for l in lens)
        assert all(len(fc) == 12 for fc in faces[:-1])

        # 2. embedding validity
        V, E, F = check_embedding(H, faces, C)
        print(f"embedding OK: V-E+F = {V}-{E}+{F} = 2")

        # 3. build G by stellation
        G = H.copy()
        U = []
        apex_of_face = {}
        for idx, fc in enumerate(faces):
            u = ("apex", idx)
            U.append(u)
            apex_of_face[idx] = u
            for v in fc:
                G.add_edge(u, v)
        u_f = apex_of_face[len(faces) - 1]

        # G - U == H
        G_minus_U = G.copy()
        G_minus_U.remove_nodes_from(U)
        assert nx.utils.graphs_equal(G_minus_U, H)

        # U independent, disjoint from C
        assert all(not G.has_edge(p, q) for p, q in itertools.combinations(U, 2)) \
            if len(U) <= 400 else True
        assert nx.is_independent_set(G, set(U)) if hasattr(nx, "is_independent_set") \
            else all(not any(w in set(U) for w in G[u]) for u in U)
        assert not (set(U) & set(C))

        # near-Eulerian-triangulation: degrees
        onC = set(C)
        bad = [v for v in G.nodes()
               if v not in onC and G.degree(v) % 2 != 0]
        assert not bad, f"internal vertex of odd degree: {bad[:5]}"
        degC = [G.degree(v) for v in C]
        print(f"degrees on C (all odd): {degC}")
        assert all(d % 2 == 1 for d in degC)
        assert G.degree(u_f) == len(faces[-1])

        # all bounded faces of G triangles; each edge on exactly 2 faces of G
        from collections import Counter
        cnt = Counter()
        n_tri = 0
        for idx, fc in enumerate(faces):
            u = apex_of_face[idx]
            t = len(fc)
            for i in range(t):
                p, q = fc[i], fc[(i + 1) % t]
                for e in ((p, q), (p, u), (q, u)):
                    cnt[frozenset(e)] += 1
                n_tri += 1
        for i in range(6):
            cnt[frozenset((C[i], C[(i + 1) % 6]))] += 1
        assert set(cnt.values()) == {2}
        assert len(cnt) == G.number_of_edges()
        VG, EG = G.number_of_nodes(), G.number_of_edges()
        assert VG - EG + (n_tri + 1) == 2, "Euler fails for G"
        print(f"G: V={VG}, E={EG}, triangles={n_tri}; Euler OK; "
              f"all bounded faces of G are triangles")

        # planarity + 2-connectivity (abstract sanity)
        planar, _ = nx.check_planarity(G)
        assert planar
        assert nx.is_biconnected(G)
        print("G planar and 2-connected (so its 3-coloring/hue is unique "
              "up to permutation)")

        # 4/5. the set S
        S_cells = [(j * L, L) for j in range(1, k + 1)]
        S_faces = [cell_faces[c] for c in S_cells]
        assert all(len(fc) == 12 for fc in S_faces)
        if k >= 2:
            dmin = min(face_distance(H, fa, fb)
                       for fa, fb in itertools.combinations(S_faces, 2))
            print(f"min pairwise distance between S faces in H: {dmin} "
                  f"(need >= d={k}; writeup claims >= 3(L-1)={3*(L-1)})")
            assert dmin >= k
        # no 4-cycles at all (girth 6), so no separating 4-cycle;
        # no closed walk of length <6 has a cycle in its support (girth 6).
        print(f"|S| = {len(S_faces)} faces of length 12; no 4-cycles in H; "
              f"girth 6 kills all closed walks of length < 6")

        # 6. viability, per the paper's definition
        # hue: bipartition classes of H = 0/1, apexes = 2 (a proper
        # 3-coloring of G; unique up to permutation by 2-connectivity)
        side = nx.bipartite.color(H)
        hue = {v: side[v] for v in H.nodes()}
        for u in U:
            hue[u] = 2
        assert all(hue[p] != hue[q] for p, q in G.edges()), "hue not proper"
        hueC = [hue[v] for v in C]
        print(f"hues along C: {hueC} (alternating)")
        phi = {C[i]: [1, 2, 3, 4, 3, 2][i] for i in range(6)}
        # proper on C?
        assert all(phi[C[i]] != phi[C[(i + 1) % 6]] for i in range(6))
        tot = (0, 0)
        for i in range(6):
            d = delta_edge(hue[C[i]], hue[C[(i + 1) % 6]],
                           phi[C[i]], phi[C[(i + 1) % 6]])
            tot = (tot[0] + d[0], tot[1] + d[1])
        print(f"delta(C) = {tot} (viable iff (0,0))")
        assert tot == (0, 0)
        homs = brute_force_hom(hueC, [phi[v] for v in C], R=6)
        print(f"brute-force homomorphisms C^phi -> grid chunk: "
              f"{len(homs)} found; one image: {homs[0] if homs else None}")
        assert homs, "no homomorphism found: NOT viable!"
        # verify one explicitly
        img = homs[0]
        for s in range(6):
            assert grid_adj(img[s], img[s + 1])
            assert grid_hue(img[s]) == hueC[s]
            assert grid_col(img[s]) == COLOR[phi[C[s]]]

        # 7. non-extension
        nb = set(G[u_f])
        assert {x, a1, a2, y} <= nb
        print(f"u_f adjacent to c0,c1,c2,c3 with colors "
              f"{[phi[v] for v in (x, a1, a2, y)]} -> no color left for u_f; "
              f"phi does not extend")

        # 8. writeup's auxiliary claims: weak dual signs / condition (1)
        # triangles of G indexed (face idx, edge idx)
        tri_of_boundary_edge = {}
        D = nx.Graph()
        tri_ids = []
        edge2tris = {}
        for idx, fc in enumerate(faces):
            t = len(fc)
            for i in range(t):
                tid = (idx, i)
                tri_ids.append(tid)
                p, q = fc[i], fc[(i + 1) % t]
                u = apex_of_face[idx]
                for e in (frozenset((p, q)), frozenset((p, u)),
                          frozenset((q, u))):
                    edge2tris.setdefault(e, []).append(tid)
        for e, ts in edge2tris.items():
            if len(ts) == 2:
                D.add_edge(ts[0], ts[1])
            else:
                assert len(ts) == 1
                (p, q) = tuple(e)
                assert p in set(C) and q in set(C)
                tri_of_boundary_edge[e] = ts[0]
        assert nx.is_bipartite(D)
        sideD = nx.bipartite.color(D)
        nplus = sum(1 for t in tri_ids if sideD[t] == 0)
        nminus = len(tri_ids) - nplus
        print(f"weak dual bipartite; |D+|={nplus}, |D-|={nminus} (equal: "
              f"{nplus == nminus})")
        assert nplus == nminus
        signs = []
        types = []

        def edge_type(cu, cv):
            s = tuple((COLOR[cu][i] + COLOR[cv][i]) % 2 for i in (0, 1))
            return {(0, 1): "alpha", (1, 0): "beta", (1, 1): "gamma"}[s]

        for i in range(6):
            p, q = C[i], C[(i + 1) % 6]
            tid = tri_of_boundary_edge[frozenset((p, q))]
            signs.append(1 if sideD[tid] == 0 else -1)
            types.append(edge_type(phi[p], phi[q]))
        print(f"boundary edge types: {types}")
        print(f"boundary triangle signs: {signs} (alternating: "
              f"{all(signs[i] != signs[(i+1) % 6] for i in range(6))})")
        sums = {z: sum(s for s, ty in zip(signs, types) if ty == z)
                for z in ("alpha", "beta", "gamma")}
        print(f"signed type sums (condition (1), target 0): {sums}")
        assert all(v == 0 for v in sums.values())
        print()

    print("ALL CHECKS PASSED: the construction satisfies every hypothesis of "
          "Conjecture 4 with d = k, the precoloring (1,2,3,4,3,2) is viable "
          "per the paper's definition, and it does not extend.")


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    main()
