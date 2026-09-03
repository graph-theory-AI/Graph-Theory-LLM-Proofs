#!/usr/bin/env python3
"""Referee verification for attack 2310.04265__09.

Claim: for n >= 3, the circulant tournament T_n on Z_q, q = 2n+1, with
out-neighbour difference set S_n = {1,...,n-1, n+1}, satisfies
  (a) T_n is a tournament (S_n and -S_n partition Z_q \ {0});
  (b) every vertex dominates a directed triangle  =>  omega->(T_n) >= 3;
  (c) the natural order 0<1<...<2n gives a backedge graph whose unique
      triangle is {0, n, 2n} and whose clique number is 3  =>  omega-> <= 3;
  (d) deleting any vertex leaves omega-> <= 2 (exhibited ordering for T_n - 0,
      vertex-transitivity for the rest);
  (e) brute force / pruned exhaustive search over ALL orderings confirms
      omega->(T_n) = 3 and omega->(T_n - v) = 2 for small n.

Convention (paper 2310.04265, Sec. 1): backedge graph D^< has edge uv iff
u < v and arc (v,u) in A(D); omega->(D) = min over orderings of omega(D^<).
"""

import itertools
import sys

def make_T(n):
    q = 2 * n + 1
    S = set(range(1, n)) | {n + 1}
    # arcs x -> y iff (y - x) mod q in S
    return q, S

def check_tournament(n):
    q, S = make_T(n)
    negS = {(-s) % q for s in S}
    ok = (S & negS == set()) and (S | negS == set(range(1, q)))
    return ok

def dominated_triangle(n):
    """Check every vertex x dominates the directed triangle x+1,x+2,x+n+1."""
    q, S = make_T(n)
    def arc(x, y):
        return (y - x) % q in S
    for x in range(q):
        a, b, c = (x + 1) % q, (x + 2) % q, (x + n + 1) % q
        if not (arc(x, a) and arc(x, b) and arc(x, c)):
            return False
        if not (arc(a, b) and arc(b, c) and arc(c, a)):
            return False
    return True

def backedge_graph(order, q, S):
    """order: tuple of vertices, positions define <. Edge (u,v) iff u before v
    and arc v->u, i.e. (u - v) mod q in S."""
    pos = {v: i for i, v in enumerate(order)}
    edges = set()
    for u in order:
        for v in order:
            if pos[u] < pos[v] and (u - v) % q in S:
                edges.add((u, v))
    return edges

def triangles_of(edges, verts):
    adj = {v: set() for v in verts}
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    tris = []
    vl = sorted(verts)
    for i, a in enumerate(vl):
        for b in vl[i+1:]:
            if b in adj[a]:
                for c in vl:
                    if c > b and c in adj[a] and c in adj[b]:
                        tris.append((a, b, c))
    return tris, adj

def natural_order_check(n):
    q, S = make_T(n)
    order = tuple(range(q))
    edges = backedge_graph(order, q, S)
    # claimed: edge ij (i<j) iff j-i in D_n = {n} cup {n+2,...,2n}
    D = {n} | set(range(n + 2, 2 * n + 1))
    claimed = {(i, j) for i in range(q) for j in range(i + 1, q) if (j - i) in D}
    tris, adj = triangles_of(edges, range(q))
    # K4 check (clique number exactly 3): any K4 contains >= 4 triangles
    has_k4 = False
    for (a, b, c) in tris:
        for d in range(q):
            if d in (a, b, c):
                continue
            if d in adj[a] and d in adj[b] and d in adj[c]:
                has_k4 = True
    return edges == claimed, tris, has_k4

def deletion_order_check(n):
    """Backedge graph of T_n - 0 under order 1<2<...<2n is triangle-free."""
    q, S = make_T(n)
    order = tuple(range(1, q))
    edges = backedge_graph(order, q, S)
    tris, _ = triangles_of(edges, range(1, q))
    return len(tris) == 0

def exists_trianglefree_ordering(verts, q, S, fix_first=None):
    """Pruned exhaustive search: is there an ordering of verts whose backedge
    graph is triangle-free?  Build order left to right; placing v after prefix
    adds edges {u, v} for placed u with (u - v) mod q in S (arc v->u).  Edges
    among placed vertices are final, so prune on any triangle."""
    verts = list(verts)
    n_v = len(verts)
    sys.setrecursionlimit(10000)

    def rec(placed, adj):
        if len(placed) == n_v:
            return placed[:]
        cands = [v for v in verts if v not in adj]
        if fix_first is not None and not placed:
            cands = [fix_first]
        for v in cands:
            nbrs = {u for u in placed if (u - v) % q in S}
            ok = True
            for a in nbrs:
                if nbrs & adj[a]:
                    ok = False
                    break
            if ok:
                adj[v] = nbrs
                for u in nbrs:
                    adj[u].add(v)
                placed.append(v)
                r = rec(placed, adj)
                if r:
                    return r
                placed.pop()
                for u in nbrs:
                    adj[u].discard(v)
                del adj[v]
        return None

    return rec([], {})

def exists_edgefree_ordering(verts, q, S):
    """omega-> <= 1 iff transitive: check whether some ordering has NO backedge.
    Equivalent to acyclicity; we just check for a directed triangle instead."""
    for a, b, c in itertools.combinations(verts, 3):
        for x, y, z in itertools.permutations((a, b, c)):
            if (y - x) % q in S and (z - y) % q in S and (x - z) % q in S:
                return False  # directed triangle -> not transitive
    return True

def brute_omega_values(n, do_full=True):
    """Return (omega(T_n), omega(T_n - 0)) determined exhaustively."""
    q, S = make_T(n)
    # omega->(T_n): >= 3 iff no triangle-free ordering exists.
    # By vertex-transitivity we may fix the first vertex to be 0.
    tf_full = exists_trianglefree_ordering(range(q), q, S, fix_first=0)
    # omega->(T_n - 0)
    tf_del = exists_trianglefree_ordering(range(1, q), q, S)
    trans_del = exists_edgefree_ordering(range(1, q), q, S)
    om_full = 2 if tf_full else 3   # (<=3 from natural order check)
    om_del = (1 if trans_del else 2) if tf_del else 3
    return om_full, om_del, tf_full

def main():
    print("=== structural checks, n = 3..60 ===")
    for n in range(3, 61):
        ok_t = check_tournament(n)
        ok_dom = dominated_triangle(n)
        ok_nat, tris, has_k4 = natural_order_check(n)
        ok_del = deletion_order_check(n)
        assert ok_t, f"n={n}: not a tournament!"
        assert ok_dom, f"n={n}: dominated-triangle claim fails!"
        assert ok_nat, f"n={n}: natural backedge graph differs from claim!"
        assert tris == [(0, n, 2 * n)], f"n={n}: triangles = {tris}"
        assert not has_k4, f"n={n}: K4 present!"
        assert ok_del, f"n={n}: deletion ordering not triangle-free!"
    print("all pass: tournament property, dominated directed triangle at every"
          " vertex,\n unique natural-order triangle {0,n,2n}, no K4,"
          " triangle-free ordering of T_n - 0.")

    print("\n=== exhaustive omega-> computation (all orderings, pruned) ===")
    for n in range(3, 8):
        om_full, om_del, witness = brute_omega_values(n)
        q = 2 * n + 1
        print(f"n={n} (q={q}): omega->(T_n) = {om_full},"
              f" omega->(T_n - 0) = {om_del}"
              + (f"  [triangle-free ordering found: {witness}]" if witness else ""))
        assert om_full == 3 and om_del == 2, f"n={n}: CLAIM FAILS"
    print("claim verified exhaustively for n = 3..7 "
          "(tournaments on 7, 9, 11, 13, 15 vertices).")

if __name__ == "__main__":
    main()
