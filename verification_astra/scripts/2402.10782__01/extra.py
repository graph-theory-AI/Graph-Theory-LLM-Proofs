"""Extra adversarial checks.

(i)   Lemma 2 for the ACTUAL gadget sizes used by the reduction (m up to 41):
      exhaustively enumerate every ordering of U_m with Delta(B_pi) <= 1 and
      collect the distinct backward graphs.  This is exactly what step 4.4 of
      the writeup needs ("the restriction of B_pi to the gadget is M_0 or M_1").
      Full enumeration of all matchings of K_m is infeasible for m=33, so we
      enumerate orderings instead, via the (exact) d=1 position windows.
(ii)  every wire of the reduction is FORCED backward: the d=2 windows of its two
      endpoints are disjoint and in the sigma order (a numerical strengthening
      of step (8)).
(iii) exhaustive path-FAS test on genuinely UNSAT formulas.
"""
import itertools, random, time
from struct_check import (build, backward_graph, is_linear_forest, sat,
                          solve_linear_forest, PAD)


def build_U(m):
    arc = [[False] * m for _ in range(m)]
    for i in range(m - 1):
        arc[i + 1][i] = True
    for i in range(m):
        for j in range(i + 2, m):
            arc[i][j] = True
    for i in range(m):
        assert not arc[i][i]
        for j in range(i + 1, m):
            assert arc[i][j] != arc[j][i]
    return arc


def all_degree_d_backward_graphs(arc, n, d):
    """Every B_pi over orderings pi with Delta(B_pi) <= d, exhaustively."""
    outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
    a = [n - outdeg[v] for v in range(n)]
    lo = [max(1, a[v] - d) for v in range(n)]
    hi = [min(n, a[v] + d) for v in range(n)]
    res = set()
    placed = [False] * n
    edges = []

    def rec(i):
        if i == n:
            res.add(frozenset(edges)); return
        for v in range(n):
            if placed[v] or not (lo[v] <= i + 1 <= hi[v]):
                continue
            beta = 0
            for u in range(n):
                if u == v: continue
                if placed[u]:
                    if arc[v][u]: beta += 1
                else:
                    if arc[u][v]: beta += 1
            if beta > d: continue
            new = [frozenset((v, u)) for u in range(n) if placed[u] and arc[v][u]]
            placed[v] = True; edges.extend(new)
            rec(i + 1)
            del edges[len(edges) - len(new):]; placed[v] = False
    rec(0)
    return res


def part_i(ms):
    ok = True
    for m in ms:
        arc = build_U(m)
        t0 = time.time()
        gs = all_degree_d_backward_graphs(arc, m, 1)
        M0 = frozenset(frozenset((i, i + 1)) for i in range(0, m - 2, 2))
        M1 = frozenset(frozenset((i, i + 1)) for i in range(1, m - 1, 2))
        good = gs == {M0, M1}
        ok &= good
        print("   m=%-3d  #distinct B_pi with Delta<=1 : %d   == {M_0,M_1}: %s  "
              "(%.1fs)" % (m, len(gs), good, time.time() - t0))
    print("(i) Lemma 2 (in the form used in 4.4) verified:", ok)
    return ok


def part_ii(formulas):
    ok = True
    for label, formula, nvars in formulas:
        n, arc, info = build(formula, nvars)
        outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
        a = [n - outdeg[v] for v in range(n)]
        lo = [max(1, a[v] - 2) for v in range(n)]
        hi = [min(n, a[v] + 2) for v in range(n)]
        forced = all(hi[min(e)] < lo[max(e)] for e in info['W'])
        span = min(max(e) - min(e) for e in info['W'])
        deg = {}
        for e in backward_graph(arc, n, list(range(n))):
            for v in e: deg[v] = deg.get(v, 0) + 1
        print("   %-34s n=%-4d |W|=%-4d min wire span=%-3d Delta(B_sigma)=%d  "
              "all wires forced backward: %s" %
              (label, n, len(info['W']), span, max(deg.values()), forced))
        ok &= forced
    print("(ii) every wire forced backward by disjoint d=2 windows:", ok)
    return ok


def part_iii():
    all8 = [[(0, s0), (1, s1), (2, s2)] for s0 in (True, False)
            for s1 in (True, False) for s2 in (True, False)]
    rng = random.Random(77)
    uns = [("all 8 clauses on x,y,z", all8, 3)]
    tries = 0
    while len(uns) < 6 and tries < 20000:
        tries += 1
        nv = 4
        f = [[(v, rng.random() < .5) for v in rng.sample(range(nv), 3)]
             for _ in range(rng.randint(9, 14))]
        if sat(f, nv) is None:
            uns.append(("random UNSAT #%d (%d clauses)" % (len(uns), len(f)), f, nv))
    ok = True
    for label, f, nv in uns:
        n, arc, info = build(f, nv)
        t0 = time.time()
        res = solve_linear_forest(arc, n, time_limit=900)
        print("   %-34s n=%-4d satisfiable=%s  linear-forest ordering exists=%s"
              "  (%.1fs)" % (label, n, sat(f, nv) is not None,
                             res if res in (None, 'TIMEOUT') else True,
                             time.time() - t0))
        ok &= (res is None)
    print("(iii) every UNSAT instance exhaustively has NO path-FAS:", ok)
    return ok, uns


if __name__ == '__main__':
    ok1 = part_i([5, 7, 9, 11, 15, 21, 23, 27, 29, 31, 33, 41])
    ok3, uns = part_iii()
    all8 = [[(0, s0), (1, s1), (2, s2)] for s0 in (True, False)
            for s1 in (True, False) for s2 in (True, False)]
    sats = [("SAT 7 of 8", all8[1:], 3), ("SAT 1 clause",
             [[(0, True), (1, True), (2, True)]], 3)]
    ok2 = part_ii(sats + uns)
    print("\nOVERALL:", "ALL PASS" if (ok1 and ok2 and ok3) else "FAILURE")
