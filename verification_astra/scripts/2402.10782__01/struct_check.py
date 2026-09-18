"""Independent re-implementation of the Section-4 reduction of
attacks_retry/2402.10782__01/output.md, plus a STRUCTURED EXHAUSTIVE decision
procedure for

    "does T have an ordering pi whose backward graph B_pi is a linear forest?"
    (= "does T have a path-FAS", by Lemma 1 of the writeup)

Naive brute force over all n! orderings is hopeless (n ~ 60..200) and even a
plain DFS blows up because the padding / private vertices permute freely.  The
search below quotients that symmetry out:

 * Score localisation (an exact identity, |pos(v) - a(v)| <= deg_{B_pi}(v),
   re-derived and unit-tested in check_localization()) confines every vertex of
   a Delta<=2 ordering to the window [a(v)-2, a(v)+2].
 * When v is placed, ALL of its backward edges are determined by the prefix SET
   S alone (edges to u in S with v->u, and edges to w outside S with w->v).
   Hence the whole graph B_pi is built incrementally and the only history that
   can still matter for the future is (i) the prefix set S and (ii) which
   still-extendable vertices currently lie in a common component.
 * We therefore memoise on (S, partition-of-still-extendable-vertices).  A
   placed vertex u is still extendable iff some unplaced w has w->u, which is a
   function of S alone.  This collapses the padding permutations.

The search is sound and COMPLETE: every ordering with B_pi a linear forest has
Delta(B_pi) <= 2, hence respects the windows and every prefix-set transition.
"""
import itertools, sys, time
sys.setrecursionlimit(100000)

PAD = 12


# ------------------------------------------------------------------ build T
def build(formula, nvars, pad=PAD):
    """formula: list of clauses, each a list of (var, sign); 3 distinct vars."""
    occs = {x: [] for x in range(nvars)}
    for ci, cl in enumerate(formula):
        assert len({v for v, s in cl}) == 3
        for k, (v, s) in enumerate(cl):
            occs[v].append((ci, k, s))

    names, gadget, port, buffers, pair_index = [], {}, {}, [], {}
    for x in range(nvars):
        seq = [('B', None)]                      # start with a buffer
        for (ci, k, s) in occs[x]:
            need = 0 if s else 1                 # j even for x, odd for ~x
            if len(seq) % 2 != need:
                seq.append(('B', None))
            j = len(seq)
            assert j % 2 == need
            pair_index[(ci, k)] = j
            seq.append(('A', (ci, k)))
            seq.append(('Bp', (ci, k)))
            seq.append(('B', None))              # buffer after the pair
        while len(seq) < 5 or len(seq) % 2 == 0:
            seq.append(('B', None))              # odd length >= 5
        ids = []
        for t, (kind, o) in enumerate(seq):
            vid = len(names)
            names.append(('gad', x, t, kind, o))
            ids.append(vid)
            if kind == 'B':
                buffers.append(vid)
        gadget[x] = ids
        for (kind, o) in seq:
            if kind == 'A':
                j = pair_index[o]
                port[o] = (ids[j], ids[j + 1])
        for _ in range(pad):
            names.append(('pad', x))
    priv = {}
    for z in buffers:
        priv[z] = len(names)
        names.append(('priv', z))
    n = len(names)

    W = set()
    for ci, cl in enumerate(formula):
        o = [(ci, 0), (ci, 1), (ci, 2)]
        for t in range(3):
            W.add(frozenset((port[o[t]][1], port[o[(t + 1) % 3]][0])))
    for z in buffers:
        W.add(frozenset((z, priv[z])))
    cnt = {}
    for e in W:
        assert len(e) == 2
        for v in e:
            cnt[v] = cnt.get(v, 0) + 1
    assert all(c == 1 for c in cnt.values()), "W not a matching"

    arc = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            arc[i][j] = True                     # forward in sigma = 0..n-1
    for x in range(nvars):
        ids = gadget[x]; m = len(ids)
        assert m >= 5 and m % 2 == 1
        for i in range(m):
            for j in range(m):
                if i != j:
                    arc[ids[i]][ids[j]] = False
        for i in range(m - 1):
            arc[ids[i + 1]][ids[i]] = True
        for i in range(m):
            for j in range(i + 2, m):
                arc[ids[i]][ids[j]] = True
    for e in W:
        u, v = sorted(e)
        assert not (names[u][0] == 'gad' and names[v][0] == 'gad'
                    and names[u][1] == names[v][1]), "wire inside one gadget"
        arc[u][v] = False; arc[v][u] = True
    for i in range(n):
        assert not arc[i][i]
        for j in range(i + 1, n):
            assert arc[i][j] != arc[j][i]
    info = dict(gadget=gadget, port=port, buffers=buffers, priv=priv, W=W,
                names=names, pair_index=pair_index)
    return n, arc, info


def backward_graph(arc, n, order):
    pos = {v: i for i, v in enumerate(order)}
    return {frozenset((u, v)) for u in range(n) for v in range(n)
            if arc[u][v] and pos[u] > pos[v]}


def is_linear_forest(E, n):
    deg = {}
    for e in E:
        for v in e:
            deg[v] = deg.get(v, 0) + 1
    if deg and max(deg.values()) > 2:
        return False
    par = list(range(n))
    def f(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for e in E:
        u, v = tuple(e)
        ru, rv = f(u), f(v)
        if ru == rv:
            return False
        par[ru] = rv
    return True


def sat(formula, nvars):
    for bits in itertools.product([False, True], repeat=nvars):
        if all(any(bits[v] == s for v, s in cl) for cl in formula):
            return bits
    return None


def ordering_from_assignment(n, info, assign):
    """Section 4.5: inside each gadget swap the adjacent pairs of M_{1-t}."""
    order = list(range(n))
    posn = {v: i for i, v in enumerate(order)}
    for x, ids in info['gadget'].items():
        m = len(ids)
        t = 1 if assign[x] else 0
        for i in range(1 - t, m - 1, 2):         # M_{1-t} = {e_i : i = 1-t mod 2}
            a, b = ids[i], ids[i + 1]
            pa, pb = posn[a], posn[b]
            order[pa], order[pb] = order[pb], order[pa]
            posn[a], posn[b] = pb, pa
    return order


# ------------------------------------------------- structured exhaustive search
def solve_linear_forest(arc, n, d=2, time_limit=None, report=None):
    """Exhaustive: return an ordering with B_pi a linear forest, or None."""
    outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
    a = [n - outdeg[v] for v in range(n)]
    lo = [max(1, a[v] - d) for v in range(n)]
    hi = [min(n, a[v] + d) for v in range(n)]
    for i in range(1, n):
        if len([v for v in range(n) if lo[v] <= i < hi[v]]) > 4 * d:
            if report: report("boundary rule (13) rejects at i=%d" % i)
            return None

    inarc = [[u for u in range(n) if arc[u][v]] for v in range(n)]
    outarc = [[v for v in range(n) if arc[u][v]] for u in range(n)]

    placed = [False] * n
    par = list(range(n))
    order = []
    seen = set()
    stats = [0, 0]                                # nodes, memo hits
    t0 = time.time()

    def find(x):
        while par[x] != x:
            x = par[x]
        return x

    def key(i):
        # still-extendable vertices: unplaced ones, and placed u with some
        # unplaced w s.t. w->u.  Both determined by the prefix SET.
        act = []
        for v in range(n):
            if not placed[v]:
                act.append(v)
            else:
                for w in inarc[v]:
                    if not placed[w]:
                        act.append(v); break
        comp = {}
        for v in act:
            comp.setdefault(find(v), []).append(v)
        parts = frozenset(frozenset(p) for p in comp.values() if len(p) > 1)
        return (frozenset(v for v in range(n) if placed[v]), parts)

    class TO(Exception):
        pass

    def rec(i):
        stats[0] += 1
        if time_limit and stats[0] % 4096 == 0 and time.time() - t0 > time_limit:
            raise TO
        if i == n:
            return True
        k = key(i)
        if k in seen:
            stats[1] += 1
            return False
        # any vertex whose window already closed but is unplaced => dead
        cands = []
        forced = []
        for v in range(n):
            if placed[v]:
                continue
            if hi[v] < i + 1:
                seen.add(k); return False
            if lo[v] <= i + 1 <= hi[v]:
                cands.append(v)
                if hi[v] == i + 1:
                    forced.append(v)
        if len(forced) > 1:
            seen.add(k); return False
        if forced:
            cands = forced
        for v in cands:
            beta = 0
            for u in range(n):
                if u == v:
                    continue
                if placed[u]:
                    if arc[v][u]: beta += 1
                else:
                    if arc[u][v]: beta += 1
            if beta > d:
                continue
            newe = [u for u in outarc[v] if placed[u]]
            undo = []
            ok = True
            for u in newe:
                rv, ru = find(v), find(u)
                if rv == ru:
                    ok = False; break
                par[rv] = ru; undo.append(rv)
            if ok:
                placed[v] = True; order.append(v)
                if rec(i + 1):
                    return True
                placed[v] = False; order.pop()
            for r in reversed(undo):
                par[r] = r
        seen.add(k)
        return False

    try:
        ok = rec(0)
    except TO:
        if report: report("TIMEOUT after %d nodes" % stats[0])
        return 'TIMEOUT'
    if report:
        report("search nodes=%d memo-hits=%d states=%d time=%.1fs"
               % (stats[0], stats[1], len(seen), time.time() - t0))
    return list(order) if ok else None


# ---------------------------------------------------------- sanity unit tests
def check_localization(trials=4000, seed=1):
    """|pos(v) - (n - outdeg(v))| <= deg_{B_pi}(v) on random tournaments."""
    import random
    rng = random.Random(seed)
    worst = 0
    for _ in range(trials):
        n = rng.randint(2, 9)
        arc = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < .5: arc[i][j] = True
                else: arc[j][i] = True
        order = list(range(n)); rng.shuffle(order)
        pos = {v: k + 1 for k, v in enumerate(order)}
        deg = [0] * n
        for u in range(n):
            for v in range(n):
                if arc[u][v] and pos[u] > pos[v]:
                    deg[u] += 1; deg[v] += 1
        for v in range(n):
            av = n - sum(1 for w in range(n) if arc[v][w])
            assert abs(pos[v] - av) <= deg[v], (n, v, pos[v], av, deg[v])
            worst = max(worst, deg[v] - abs(pos[v] - av))
    return True


def main():
    print("score-localization identity (2) on random tournaments:",
          check_localization())
    all8 = [[(0, s0), (1, s1), (2, s2)] for s0 in (True, False)
            for s1 in (True, False) for s2 in (True, False)]
    tests = [
        ("SAT  1 clause (x|y|z)", [[(0, True), (1, True), (2, True)]], 3),
        ("SAT  2 clauses", [[(0, True), (1, True), (2, True)],
                            [(0, False), (1, False), (2, False)]], 3),
        ("UNSAT 3 clauses (x|y|z),(~x|y|z) ... forced", None, None),
        ("SAT  7 of the 8 clauses (unique model)", all8[1:], 3),
        ("UNSAT all 8 clauses on x,y,z", all8, 3),
    ]
    tests = [t for t in tests if t[1] is not None]
    for label, formula, nvars in tests:
        n, arc, info = build(formula, nvars)
        s = sat(formula, nvars)
        sigma = list(range(n))
        Bs = backward_graph(arc, n, sigma)
        deg = {}
        for e in Bs:
            for v in e: deg[v] = deg.get(v, 0) + 1
        paths = {frozenset((ids[i], ids[i + 1]))
                 for ids in info['gadget'].values() for i in range(len(ids) - 1)}
        print("\n[%s]  n=%d  gadget sizes=%s  |W|=%d  satisfiable=%s"
              % (label, n, sorted(len(v) for v in info['gadget'].values()),
                 len(info['W']), s is not None))
        print("   Delta(B_sigma)=%d ; B_sigma == W u gadget-paths: %s ; "
              "min sigma-span of a wire=%d"
              % (max(deg.values()), Bs == (set(info['W']) | paths),
                 min(max(e) - min(e) for e in info['W'])))
        if s is not None:
            o = ordering_from_assignment(n, info, s)
            B = backward_graph(arc, n, o)
            print("   Sec 4.5 ordering from the model: B_pi == W u matchings: %s ;"
                  " linear forest: %s" %
                  (B == set(info['W']) | {frozenset((info['gadget'][x][i],
                                                     info['gadget'][x][i + 1]))
                                          for x in range(nvars)
                                          for i in range(1 if s[x] else 0,
                                                         len(info['gadget'][x]) - 1, 2)},
                   is_linear_forest(B, n)))
        t0 = time.time()
        res = solve_linear_forest(arc, n, time_limit=1500,
                                  report=lambda m: print("   [search]", m))
        found = res not in (None, 'TIMEOUT')
        if found:
            assert is_linear_forest(backward_graph(arc, n, res), n)
        print("   EXHAUSTIVE: linear-forest ordering exists = %s  (%.1fs)"
              % (res if res in (None, 'TIMEOUT') else True, time.time() - t0))
        if res != 'TIMEOUT':
            print("   EQUIVALENCE (10) holds: %s" % ((s is not None) == found))


if __name__ == '__main__':
    main()
