"""Brute-force check of Lemma 2 of attacks_retry/2402.10782__01/output.md.

U_m (m odd >= 5): vertices z_0..z_{m-1};
  arcs  z_{i+1} -> z_i   for 0 <= i < m-1
        z_i -> z_j       whenever j >= i+2.
Claim: the ONLY feedback arc sets of U_m whose underlying graph is a matching
(max degree <= 1) are M_0 = {z0z1, z2z3, ...} and M_1 = {z1z2, z3z4, ...}.
Also: each M_t is realized as the backward graph of an explicit ordering.
"""
import itertools, sys

def build_U(m):
    arc = [[False]*m for _ in range(m)]
    for i in range(m-1):
        arc[i+1][i] = True          # z_{i+1} -> z_i
    for i in range(m):
        for j in range(i+2, m):
            arc[i][j] = True        # z_i -> z_j
    # sanity: tournament
    for i in range(m):
        for j in range(m):
            if i != j:
                assert arc[i][j] != arc[j][i], (i, j)
        assert not arc[i][i]
    return arc

def is_acyclic(arc, n, removed):
    """Kahn on the digraph arc minus removed (set of (u,v))."""
    indeg = [0]*n
    out = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if arc[u][v] and (u, v) not in removed:
                out[u].append(v); indeg[v] += 1
    stack = [v for v in range(n) if indeg[v] == 0]
    seen = 0
    while stack:
        u = stack.pop(); seen += 1
        for v in out[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)
    return seen == n

def matchings(n):
    """all matchings (sets of unordered pairs, pairwise disjoint) on n vertices"""
    res = []
    def rec(v, used, cur):
        if v == n:
            res.append(list(cur)); return
        if v in used:
            rec(v+1, used, cur); return
        rec(v+1, used, cur)                     # v unmatched
        for w in range(v+1, n):
            if w not in used:
                cur.append((v, w)); used.add(v); used.add(w)
                rec(v+1, used, cur)
                used.discard(v); used.discard(w); cur.pop()
    rec(0, set(), [])
    return res

def backward_graph(arc, n, order):
    pos = {v: i for i, v in enumerate(order)}
    return {frozenset((u, v)) for u in range(n) for v in range(n)
            if arc[u][v] and pos[u] > pos[v]}

def main():
    for m in [5, 7, 9, 11]:
        arc = build_U(m)
        M0 = {frozenset((i, i+1)) for i in range(0, m-2, 2)}
        M1 = {frozenset((i, i+1)) for i in range(1, m-1, 2)}
        good = []
        for M in matchings(m):
            removed = set()
            for (a, b) in M:
                removed.add((a, b) if arc[a][b] else (b, a))
            if is_acyclic(arc, m, removed):
                good.append({frozenset(e) for e in M})
        print(f"m={m}: #matching FAS = {len(good)}")
        assert len(good) == 2, good
        assert M0 in good and M1 in good, (M0, M1, good)
        # realizability as backward graphs
        for t, Mt, Mother in [(0, M0, M1), (1, M1, M0)]:
            order = list(range(m))
            for e in Mother:
                i, j = sorted(e)
                order[i], order[j] = order[j], order[i]
            B = backward_graph(arc, m, order)
            assert B == Mt, (m, t, sorted(map(sorted, B)), sorted(map(sorted, Mt)))
        print(f"   only M0,M1; both realized as backward graphs. OK")
    print("Lemma 2: VERIFIED for m in {5,7,9,11}")

main()
