#!/usr/bin/env python3
"""Check whether the counterexample graph G(q) is a *candidate* in the sense of
Chudnovsky-Scott-Seymour, "Detecting a long odd hole" (arXiv:1904.12273v2):

  G is a candidate if it contains no long pyramid, no long jewel of order at
  most ell+2, and no long odd hole of length at most 2*ell+2,
  where "long" means length >= ell (ell >= 5 fixed).

Definitions (verbatim from the paper):
 * long jewel: u,v in V(G); Q1,Q2 induced u-v paths of different parity;
   P an induced u-v path of length >= ell such that no vertex of P* (interior)
   equals or is adjacent to any vertex of Q1*, Q2*.  Order =
   max(|V(Q1)|,|V(Q2)|).
 * long pyramid: apex v0, base triangle {v1,v2,v3}, induced paths P_i from v0
   to v_i, pairwise vertex-disjoint except v0, at least two of length >= ell,
   and for i<j the only edge between V(P_i)\{v0} and V(P_j)\{v0} is v_i v_j.

This matters because the intended setting of the "heavy path" extension is a
candidate graph (the heavy-edge theorem 7.4 of arXiv:1903.00208 likewise
assumes no jewel, no pyramid, no 5-hole).
"""
import itertools, sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def build(q):
    n = 3 * q
    a1, a2, a3 = 0, q, 2 * q
    A1 = list(range(0, q + 1))
    A2 = list(range(q, 2 * q + 1))
    A3 = list(range(2 * q, 3 * q)) + [0]
    y1, y2, y3, x = n, n + 1, n + 2, n + 3
    V = list(range(n + 4))
    adj = {v: set() for v in V}
    def add(u, v):
        adj[u].add(v); adj[v].add(u)
    for i in range(n):
        add(i, (i + 1) % n)
    for y, A in ((y1, A1), (y2, A2), (y3, A3)):
        for c in A:
            add(y, c)
    add(y1, y2); add(y1, y3); add(y2, y3)
    for c in range(n):
        add(x, c)
    return V, adj, n, (y1, y2, y3), x

def induced_paths(u, v, adj, allowed, max_vertices=None, stop_at_len=None,
                  collect=True):
    """Enumerate induced u-v paths with all vertices in `allowed` (u,v must be
    in allowed).  If stop_at_len is set, return True as soon as a path with
    length (edges) >= stop_at_len is found (existence mode)."""
    out = []
    stack = [[u]]
    while stack:
        p = stack.pop()
        last = p[-1]
        for w in adj[last]:
            if w not in allowed or w in p:
                continue
            # induced path condition: w adjacent only to `last` among p,
            # except: if w == v we close the path (v must be nonadjacent to
            # p[:-1] as well for the path to be induced).
            if any(w in adj[t] for t in p[:-1]):
                continue
            newp = p + [w]
            if w == v:
                if stop_at_len is not None and len(newp) - 1 >= stop_at_len:
                    return True
                if collect:
                    out.append(newp)
                continue
            if max_vertices is not None and len(newp) >= max_vertices:
                continue
            stack.append(newp)
    if stop_at_len is not None:
        return False
    return out

def find_long_jewels(V, adj, ell, max_order, verbose=True):
    """Search for a long jewel of order <= max_order. Returns first found or None."""
    Vset = set(V)
    found = []
    for u, v in itertools.combinations(V, 2):
        if v in adj[u]:
            continue  # adjacent u,v cannot both carry two induced paths of
                      # different parity AND a long induced path (any induced
                      # u-v path then has length 1)
        Qs = induced_paths(u, v, adj, Vset, max_vertices=max_order)
        if not Qs:
            continue
        # group by parity of length
        even = [Q for Q in Qs if (len(Q) - 1) % 2 == 0]
        odd = [Q for Q in Qs if (len(Q) - 1) % 2 == 1]
        if not even or not odd:
            continue
        seen_interiors = set()
        for Q1 in even:
            for Q2 in odd:
                bad = set(Q1[1:-1]) | set(Q2[1:-1])
                key = frozenset(bad)
                if key in seen_interiors:
                    continue
                seen_interiors.add(key)
                forb = set(bad)
                for b in bad:
                    forb |= adj[b]
                allowed = (Vset - forb) | {u, v}
                if u not in allowed or v not in allowed:
                    continue  # u or v adjacent to interiors is fine; they are
                              # re-added; interiors themselves excluded
                exists = induced_paths(u, v, adj, allowed, stop_at_len=ell,
                                       collect=False)
                if exists:
                    found.append((u, v, Q1, Q2))
                    if verbose:
                        print(f"  LONG JEWEL: u={u} v={v} Q1={Q1} Q2={Q2} "
                              f"(order {max(len(Q1),len(Q2))})")
                    return found
    return found

def find_long_pyramids(V, adj, ell, verbose=True):
    """Exhaustive long-pyramid search."""
    Vset = set(V)
    # enumerate triangles
    tris = [t for t in itertools.combinations(V, 3)
            if t[1] in adj[t[0]] and t[2] in adj[t[0]] and t[2] in adj[t[1]]]
    npaths_stats = 0
    for tri in tris:
        for v0 in V:
            if v0 in tri:
                continue
            # candidate paths P_i: induced v0-v_i paths whose vertices other
            # than v0 and v_i are nonadjacent to the other two base vertices,
            # and v_i's only base-adjacencies are the triangle edges (auto).
            plists = []
            ok = True
            for idx in range(3):
                vi = tri[idx]
                others = [tri[j] for j in range(3) if j != idx]
                allowed = set()
                for w in Vset:
                    if w == v0 or w == vi:
                        allowed.add(w)
                        continue
                    if w in tri:
                        continue
                    if any(w in adj[o] for o in others):
                        continue
                    allowed.add(w)
                ps = induced_paths(v0, vi, adj, allowed)
                if not ps:
                    ok = False
                    break
                plists.append(ps)
            if not ok:
                continue
            npaths_stats = max(npaths_stats,
                               max(len(p) for p in plists))
            # need at least two paths of length >= ell overall; prune triples
            L = [sorted(ps, key=len, reverse=True) for ps in plists]
            for P1 in L[0]:
                for P2 in L[1]:
                    l1, l2 = len(P1) - 1, len(P2) - 1
                    s1, s2 = set(P1) - {v0}, set(P2) - {v0}
                    if s1 & s2:
                        continue
                    # cross edges P1/P2: only tri[0]-tri[1]
                    if any(b in adj[a] for a in s1 for b in s2
                           if not (a == tri[0] and b == tri[1])
                           and not (a == tri[1] and b == tri[0])):
                        continue
                    for P3 in L[2]:
                        l3 = len(P3) - 1
                        if sorted((l1, l2, l3))[1] < ell:
                            continue  # fewer than two long paths
                        s3 = set(P3) - {v0}
                        if s3 & (s1 | s2):
                            continue
                        bad = False
                        for a in s3:
                            for b in s1:
                                if b in adj[a] and not ({a, b} == {tri[2], tri[0]}):
                                    bad = True; break
                            if bad: break
                            for b in s2:
                                if b in adj[a] and not ({a, b} == {tri[2], tri[1]}):
                                    bad = True; break
                            if bad: break
                        if bad:
                            continue
                        if verbose:
                            print(f"  LONG PYRAMID: apex {v0}, base {tri}, "
                                  f"paths {P1} {P2} {P3}")
                        return [(v0, tri, P1, P2, P3)]
    return []

def main():
    for q, ell in [(7, 7), (9, 7), (11, 7), (9, 6), (13, 7)]:
        V, adj, n, ys, x = build(q)
        print(f"=== q={q}, ell={ell}, |V(G)|={n+4} ===")
        print(f"  candidate needs: no long odd hole of length <= {2*ell+2} "
              f"(C has length {3*q}; other odd holes have length 5 < {ell}), ")
        jew = find_long_jewels(V, adj, ell, max_order=ell + 2)
        print(f"  long jewels of order <= {ell+2}: "
              f"{'FOUND' if jew else 'none'}")
        pyr = find_long_pyramids(V, adj, ell)
        print(f"  long pyramids: {'FOUND' if pyr else 'none'}")
        short_long_odd = (3 * q <= 2 * ell + 2)
        cand = (not jew) and (not pyr) and (not short_long_odd) and (5 < ell)
        print(f"  ==> G(q={q}) is a candidate for ell={ell}: {cand}")
        print()

if __name__ == "__main__":
    main()
