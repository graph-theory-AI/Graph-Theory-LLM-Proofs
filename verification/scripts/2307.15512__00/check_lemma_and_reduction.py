#!/usr/bin/env python3
"""Verification for 2307.15512__00 (part 1): game mechanics.

Checks, by exact game solving on small instances:
  (A) The hypergraph Cops-and-Robber game (pieces move along hyperedges,
      capture = same vertex) has the same cop number as the 2-section graph.
  (B) The writeup's "safe-neighbor lemma": if for every u in R and every
      C subseteq V\{u} with |C| <= q there is v in N(u) cap R with
      v notin N[C], then c(G) > q.  We brute-force (*) for q = 1, 2 on random
      graphs and compare against the exact cop number.
"""
import itertools
import random
from functools import lru_cache


def cop_number_from_closed_nbhd(closed, max_cops=4):
    """Exact cop number of a reflexive move structure.

    closed[v] = frozenset of vertices reachable in one move from v (incl. v).
    Standard alternating game: cops place, robber places, cops move first.
    """
    n = len(closed)
    for q in range(1, max_cops + 1):
        if cops_win(closed, n, q):
            return q
    return None  # > max_cops


def cops_win(closed, n, q):
    cop_tuples = list(itertools.combinations_with_replacement(range(n), q))
    # state: (cop_tuple_sorted, robber, turn) turn 0 = cops to move
    # cop-win set computed as least fixed point.
    win = set()
    # capture states: robber on a cop vertex (any turn)
    for ct in cop_tuples:
        s = set(ct)
        for r in range(n):
            if r in s:
                win.add((ct, r, 0))
                win.add((ct, r, 1))
    changed = True
    # Precompute cop move options per tuple (cartesian product of closed nbhds)
    moves = {}
    for ct in cop_tuples:
        opts = set()
        for combo in itertools.product(*[closed[c] for c in ct]):
            opts.add(tuple(sorted(combo)))
        moves[ct] = opts
    while changed:
        changed = False
        for ct in cop_tuples:
            for r in range(n):
                if (ct, r, 0) not in win:
                    # cops to move: exists a move leading to win (robber turn)
                    for nt in moves[ct]:
                        if r in nt or (nt, r, 1) in win:
                            win.add((ct, r, 0))
                            changed = True
                            break
                if (ct, r, 1) not in win and (ct, r, 0) in win.union():
                    pass
        for ct in cop_tuples:
            s = set(ct)
            for r in range(n):
                if (ct, r, 1) in win or r in s:
                    continue
                # robber to move: all robber moves lead to cop-win states
                if all((ct, r2, 0) in win or r2 in s for r2 in closed[r]):
                    win.add((ct, r, 1))
                    changed = True
    # cops win overall: exists initial placement s.t. for all robber choices,
    # state (ct, r, 0) is cop-win (cops move first after placement).
    for ct in cop_tuples:
        if all((ct, r, 0) in win for r in range(n)):
            return True
    return False


def two_section_closed(n, hyperedges):
    closed = [set([v]) for v in range(n)]
    for e in hyperedges:
        for v in e:
            closed[v] |= set(e)
    return [frozenset(s) for s in closed]


def graph_closed(n, edges):
    closed = [set([v]) for v in range(n)]
    for (a, b) in edges:
        closed[a].add(b)
        closed[b].add(a)
    return [frozenset(s) for s in closed]


def connected(n, closed):
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in closed[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


def test_reduction(trials=30, seed=1):
    rng = random.Random(seed)
    ok = 0
    for t in range(trials):
        n = rng.randint(6, 9)
        k = rng.randint(3, 4)
        m = rng.randint(n // 2, n + 2)
        hyperedges = set()
        while len(hyperedges) < m:
            hyperedges.add(tuple(sorted(rng.sample(range(n), k))))
        closed_h = two_section_closed(n, hyperedges)
        if not connected(n, closed_h):
            continue
        # hypergraph game move structure IS closed_h by definition;
        # build 2-section as a graph explicitly and compare
        edges = set()
        for e in hyperedges:
            for a, b in itertools.combinations(e, 2):
                edges.add((min(a, b), max(a, b)))
        closed_g = graph_closed(n, edges)
        assert closed_h == closed_g, "move structures differ!"
        ch = cop_number_from_closed_nbhd(closed_h, max_cops=3)
        cg = cop_number_from_closed_nbhd(closed_g, max_cops=3)
        assert ch == cg, (ch, cg)
        ok += 1
    print(f"(A) reduction check: {ok} connected random hypergraphs, "
          f"c(H) == c(2-section) in all cases")


def star_condition(n, closed, R, q):
    """Brute-force the writeup's condition (*) for parameter q."""
    V = range(n)
    for u in R:
        Nu = closed[u] - {u}
        for j in range(q + 1):
            for C in itertools.combinations([x for x in V if x != u], j):
                NC = set(C)
                for c in C:
                    NC |= closed[c]
                if not any(v in R and v not in NC for v in Nu):
                    return False
    return True


def test_solver_sanity():
    # known cop numbers
    def cycle(n):
        return graph_closed(n, [(i, (i + 1) % n) for i in range(n)])
    assert cop_number_from_closed_nbhd(cycle(3)) == 1
    assert cop_number_from_closed_nbhd(cycle(4)) == 2
    assert cop_number_from_closed_nbhd(cycle(5)) == 2
    assert cop_number_from_closed_nbhd(cycle(6)) == 2
    # path -> 1
    assert cop_number_from_closed_nbhd(
        graph_closed(6, [(i, i + 1) for i in range(5)])) == 1
    # complete graph -> 1
    assert cop_number_from_closed_nbhd(
        graph_closed(6, list(itertools.combinations(range(6), 2)))) == 1
    # Petersen graph -> 3
    pet = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
           (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
           (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    assert cop_number_from_closed_nbhd(graph_closed(10, pet)) == 3
    print("solver sanity: C3=1 C4=C5=C6=2 P6=1 K6=1 Petersen=3, all correct")


def test_safe_neighbor(trials=400, seed=2):
    rng = random.Random(seed)
    tested = {1: 0, 2: 0}
    holds = {1: 0, 2: 0}
    for t in range(trials):
        n = rng.randint(8, 11)
        p = rng.uniform(0.3, 0.85)
        edges = [(a, b) for a in range(n) for b in range(a + 1, n)
                 if rng.random() < p]
        closed = graph_closed(n, edges)
        if not connected(n, closed):
            continue
        R = set(range(n))  # take R = V as in the lemma with R = R-part
        for q in (1, 2):
            tested[q] += 1
            if star_condition(n, closed, R, q):
                holds[q] += 1
                c = cop_number_from_closed_nbhd(closed, max_cops=q + 1)
                # lemma asserts c(G) > q, i.e. solver must not find <= q cops
                assert c is None or c > q, (
                    f"LEMMA VIOLATED: n={n} q={q} c={c} edges={edges}")
    print(f"(B) safe-neighbor lemma: graphs tested q=1:{tested[1]} q=2:{tested[2]}; "
          f"(*) held in q=1:{holds[1]} q=2:{holds[2]} cases; "
          f"cop number exceeded q in every case where (*) held")


def test_safe_neighbor_positive():
    """Positive instances: graphs where (*) provably holds, check c(G) > q."""
    pet = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
           (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
           (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    closed = graph_closed(10, pet)
    R = set(range(10))
    for q in (1, 2):
        assert star_condition(10, closed, R, q), f"(*) fails on Petersen q={q}"
        c = cop_number_from_closed_nbhd(closed, max_cops=q + 1)
        assert c is None or c > q
    print("(B+) Petersen: (*) holds for q=1,2 and c=3 > 2, lemma consistent")
    # random larger sparse graphs, q=1
    rng = random.Random(7)
    found = 0
    for t in range(300):
        n = rng.randint(12, 16)
        p = rng.uniform(0.18, 0.4)
        edges = [(a, b) for a in range(n) for b in range(a + 1, n)
                 if rng.random() < p]
        closed = graph_closed(n, edges)
        if not connected(n, closed):
            continue
        if star_condition(n, closed, set(range(n)), 1):
            found += 1
            c = cop_number_from_closed_nbhd(closed, max_cops=2)
            assert c is None or c > 1, f"LEMMA VIOLATED n={n} edges={edges}"
    print(f"(B+) random sparse graphs: (*) held with q=1 in {found} instances; "
          f"cop number > 1 in every one")


if __name__ == "__main__":
    test_solver_sanity()
    test_reduction()
    test_safe_neighbor()
    test_safe_neighbor_positive()
    print("part 1: all checks passed")
