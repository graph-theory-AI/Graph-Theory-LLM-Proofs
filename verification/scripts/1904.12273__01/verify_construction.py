#!/usr/bin/env python3
"""Independent verification of the counterexample in attacks/1904.12273__01/output.md.

Construction: C = cycle of length 3q (q odd) made of arcs A1,A2,A3 of q edges
with corners a1,a2,a3.  y_i adjacent to all of V(A_i); y1,y2,y3 a triangle;
x complete to V(C), anticomplete to {y1,y2,y3}.  M = {x,y1,y2,y3}.

Checks:
 1. C is an induced (chordless) cycle of odd length 3q.
 2. All of M are C-major (no 3-vertex subpath of C contains all C-neighbours);
    x is nonadjacent to y1,y2,y3.
 3. Full chordless-cycle (hole) census of G, classified by length; verify that
    the only odd holes are C and 5-holes, so C is the unique odd hole of
    length >= 6, hence the shortest long odd hole for any threshold ell with
    6 <= ell <= 3q.
 4. Minimum length of a subpath Q of C such that every vertex of M has a
    neighbour in V(Q) (writeup's catching notion), and also under the paper's
    notion (neighbour in the interior of Q, vertex not on Q).  Expect ~q, i.e.
    unbounded as q grows.
 5. Longest induced path through x (sanity for jewel/pyramid analysis).
"""
import itertools, sys
from collections import defaultdict

def build(q):
    assert q % 2 == 1 and q >= 3
    n = 3 * q
    C = list(range(n))                       # cycle vertices 0..3q-1
    a1, a2, a3 = 0, q, 2 * q                 # corners
    A1 = list(range(0, q + 1))               # a1..a2 inclusive
    A2 = list(range(q, 2 * q + 1))           # a2..a3 inclusive
    A3 = list(range(2 * q, 3 * q)) + [0]     # a3..a1 inclusive
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
    for c in C:
        add(x, c)
    return V, adj, C, (A1, A2, A3), (a1, a2, a3), (y1, y2, y3), x

def is_chordless_cycle(vs, adj):
    k = len(vs)
    for i in range(k):
        for j in range(i + 1, k):
            expect = (j == i + 1) or (i == 0 and j == k - 1)
            if (vs[j] in adj[vs[i]]) != expect:
                return False
    return True

def enumerate_holes(V, adj):
    """All chordless cycles of length >= 4, as frozensets (with a witness order)."""
    holes = {}
    Vs = sorted(V)
    for s in Vs:
        # paths starting at s, all other vertices > s
        # path invariant: induced path; extend at the end.
        stack = [[s, w] for w in sorted(adj[s]) if w > s]
        while stack:
            path = stack.pop()
            last = path[-1]
            for w in adj[last]:
                if w <= s or w in path:
                    continue
                # w must be nonadjacent to all of path except last (and possibly s)
                mid_ok = all(w not in adj[u] for u in path[1:-1])
                if not mid_ok:
                    continue
                if s in adj[w]:
                    if len(path) >= 3:
                        cyc = path + [w]
                        holes.setdefault(frozenset(cyc), tuple(cyc))
                    # w adjacent to s cannot be an internal vertex (chord to s)
                    continue
                stack.append(path + [w])
    return holes

def main(q):
    V, adj, C, arcs, corners, ys, x = build(q)
    A1, A2, A3 = arcs
    y1, y2, y3 = ys
    n = 3 * q
    M = [x, y1, y2, y3]
    print(f"=== q = {q}  (|V(C)| = {n}, |V(G)| = {n+4}) ===")

    # 1. C chordless odd cycle
    ok = is_chordless_cycle(C, adj)
    print(f"C is a chordless cycle: {ok}; length {n} odd: {n % 2 == 1}")
    assert ok and n % 2 == 1

    # 2. C-major checks
    triples = [set(((i) % n, (i + 1) % n, (i + 2) % n)) for i in range(n)]
    for v in M:
        NC = set(adj[v]) & set(C)
        major = not any(NC <= t for t in triples)
        print(f"vertex {'x' if v==x else 'y'+str(v-n+1)}: |N_C| = {len(NC)}, C-major: {major}")
        assert major
    assert all(v not in adj[x] for v in (y1, y2, y3)), "x must be anticomplete to ys"
    assert all(u in adj[v] for u, v in itertools.combinations((y1, y2, y3), 2))
    print("x anticomplete to {y1,y2,y3}: True; y's form a triangle: True")

    # 3. hole census
    holes = enumerate_holes(V, adj)
    by_len = defaultdict(int)
    odd_holes = []
    for fs, wit in holes.items():
        L = len(fs)
        by_len[L] += 1
        if L % 2 == 1:
            odd_holes.append((L, fs))
    print("hole census (length: count):", dict(sorted(by_len.items())))
    odd_lens = sorted(set(L for L, _ in odd_holes))
    print("odd hole lengths present:", odd_lens)
    long_odd = [fs for L, fs in odd_holes if L >= 6]
    print(f"odd holes of length >= 6: {len(long_odd)}")
    assert len(long_odd) == 1 and long_odd[0] == frozenset(C), \
        "C should be the unique odd hole of length >= 6"
    print("unique odd hole of length >= 6 is C itself: True")

    # 4. minimum catching path along C
    def subpath(i, L):        # L edges, starting at vertex i
        return [C[(i + k) % n] for k in range(L + 1)]
    best_nbr = None
    best_paper = None
    for L in range(0, n):
        found_nbr = found_paper = False
        for i in range(n):
            P = subpath(i, L)
            Pset = set(P)
            interior = set(P[1:-1])
            if best_nbr is None and all(adj[m] & Pset for m in M):
                found_nbr = True
            if best_paper is None and all((m not in Pset) and (adj[m] & interior) for m in M):
                found_paper = True
        if best_nbr is None and found_nbr:
            best_nbr = L
        if best_paper is None and found_paper:
            best_paper = L
        if best_nbr is not None and best_paper is not None:
            break
    print(f"min edges of a subpath of C with a neighbour of every m in M: {best_nbr} (q = {q})")
    print(f"min edges under paper's catch (interior neighbour, m not on path): {best_paper}")
    assert best_nbr == q

    # 5. longest induced path through x
    longest = 0
    stack = [[x]]
    # grow induced paths in both directions is equivalent to: enumerate induced
    # paths starting anywhere and containing x; cheaper: paths starting at x,
    # then max over concatenations. Simpler: DFS over induced paths containing x
    # by growing from x on both sides via paths starting at x (two-sided join).
    one_sided = []
    st = [[x]]
    while st:
        p = st.pop()
        one_sided.append(p)
        last = p[-1]
        for w in adj[last]:
            if w in p:
                continue
            if all(w not in adj[u] for u in p[:-1]):
                st.append(p + [w])
    # join two one-sided paths at x
    for p in one_sided:
        for r in one_sided:
            if set(p) & set(r) != {x}:
                continue
            # check cross-induced: no edges between p[1:] and r[1:] except none
            okj = all(b not in adj[a] for a in p[1:] for b in r[1:])
            if okj:
                longest = max(longest, len(p) - 1 + len(r) - 1)
    print(f"longest induced path containing x: {longest} edges")
    print()

if __name__ == "__main__":
    for q in (3, 5, 7):
        main(q)
