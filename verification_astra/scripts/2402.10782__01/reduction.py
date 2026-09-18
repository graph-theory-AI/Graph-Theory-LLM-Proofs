"""Independent implementation of the 3-SAT -> path-FAS reduction of
attacks_retry/2402.10782__01/output.md (Section 4), plus an exact solver for
  "does T have an ordering pi whose backward graph B_pi is a linear forest?"
which by Lemma 1 is equivalent to "T has a path-FAS".
"""
import sys, itertools, time
sys.setrecursionlimit(100000)

PAD = 12   # padding vertices between consecutive blocks, as in the writeup

# ---------------------------------------------------------------- construction
def build(formula, nvars, pad=PAD):
    """formula: list of clauses, each a list of (var, sign) with sign True=positive,
    three DISTINCT variables per clause.  Returns (n, arc, sigma_names, info)."""
    occs = {x: [] for x in range(nvars)}
    for ci, cl in enumerate(formula):
        assert len({v for v, s in cl}) == 3, "clause must have 3 distinct variables"
        for pi_, (v, s) in enumerate(cl):
            occs[v].append((ci, pi_, s))

    names = []           # sigma order, list of labels
    gadget = {}          # x -> list of global vertex ids (z_0..z_{m-1})
    port = {}            # (ci,pi) -> (a_id, b_id)
    buffers = []         # global ids of buffer vertices
    parity_of_pair = {}  # (ci,pi) -> j index inside gadget

    for x in range(nvars):
        seq = []                       # list of ('B',None) or ('A',o) / ('Bp',o)
        seq.append(('B', None))
        for (ci, pi_, s) in occs[x]:
            need = 0 if s else 1       # j even for positive, odd for negative
            if len(seq) % 2 != need:
                seq.append(('B', None))
            j = len(seq)
            parity_of_pair[(ci, pi_)] = j
            assert j % 2 == need
            seq.append(('A', (ci, pi_)))
            seq.append(('Bp', (ci, pi_)))
            seq.append(('B', None))
        while len(seq) < 5 or len(seq) % 2 == 0:
            seq.append(('B', None))
        ids = []
        for k, (kind, o) in enumerate(seq):
            vid = len(names)
            names.append(('gad', x, k, kind, o))
            ids.append(vid)
            if kind == 'B':
                buffers.append(vid)
        gadget[x] = ids
        for (ci, pi_) in [o for (k, o) in seq if k == 'A']:
            j = parity_of_pair[(ci, pi_)]
            port[(ci, pi_)] = (ids[j], ids[j+1])
        # padding after each gadget block
        for _ in range(pad):
            names.append(('pad',))
    # private block
    priv = {}
    for z in buffers:
        vid = len(names); names.append(('priv', z)); priv[z] = vid

    n = len(names)
    pos = {i: i for i in range(n)}   # sigma order is 0..n-1

    # wire matching W (undirected pairs)
    W = set()
    for ci, cl in enumerate(formula):
        o = [(ci, 0), (ci, 1), (ci, 2)]
        for t in range(3):
            b = port[o[t]][1]
            a = port[o[(t+1) % 3]][0]
            W.add(frozenset((b, a)))
    for z in buffers:
        W.add(frozenset((z, priv[z])))
    # W is a matching?
    cnt = {}
    for e in W:
        for v in e: cnt[v] = cnt.get(v, 0) + 1
    assert all(c == 1 for c in cnt.values()), "W is not a matching"

    arc = [[False]*n for _ in range(n)]
    # default: forward in sigma
    for i in range(n):
        for j in range(i+1, n):
            arc[i][j] = True
    # gadget internal: U_m
    for x in range(nvars):
        ids = gadget[x]; m = len(ids)
        assert m >= 5 and m % 2 == 1, (x, m)
        for i in range(m):
            for j in range(m):
                if i != j:
                    arc[ids[i]][ids[j]] = False
        for i in range(m-1):
            arc[ids[i+1]][ids[i]] = True
        for i in range(m):
            for j in range(i+2, m):
                arc[ids[i]][ids[j]] = True
    # wires: backward in sigma
    for e in W:
        u, v = sorted(e)
        assert not (names[u][0] == 'gad' and names[v][0] == 'gad' and names[u][1] == names[v][1]), \
            "wire inside a single gadget"
        arc[u][v] = False; arc[v][u] = True
    # tournament sanity
    for i in range(n):
        assert not arc[i][i]
        for j in range(i+1, n):
            assert arc[i][j] != arc[j][i], (i, j)
    info = dict(gadget=gadget, port=port, buffers=buffers, priv=priv, W=W,
                names=names, parity=parity_of_pair)
    return n, arc, info

def backward_graph(arc, n, order):
    pos = {v: i for i, v in enumerate(order)}
    E = set()
    for u in range(n):
        for v in range(n):
            if arc[u][v] and pos[u] > pos[v]:
                E.add(frozenset((u, v)))
    return E

def is_linear_forest(E, n):
    deg = {}
    for e in E:
        for v in e: deg[v] = deg.get(v, 0) + 1
    if deg and max(deg.values()) > 2: return False
    par = list(range(n))
    def f(a):
        while par[a] != a: par[a] = par[par[a]]; a = par[a]
        return a
    for e in E:
        u, v = tuple(e)
        ru, rv = f(u), f(v)
        if ru == rv: return False
        par[ru] = rv
    return True

# ---------------------------------------------------- exact linear-forest solver
def solve(arc, n, verbose=False, node_cap=None):
    """Return an ordering pi with B_pi a linear forest, or None. Exhaustive."""
    outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
    a = [n - outdeg[v] for v in range(n)]
    d = 2
    lo = [max(1, a[v]-d) for v in range(n)]
    hi = [min(n, a[v]+d) for v in range(n)]
    for i in range(1, n):
        X = [v for v in range(n) if lo[v] <= i < hi[v]]
        if len(X) > 4*d:
            if verbose: print("   rejected by boundary rule at i=%d (|X|=%d)" % (i, len(X)))
            return None
    inarc = [[u for u in range(n) if arc[u][v]] for v in range(n)]
    placed = [False]*n
    par = list(range(n))
    order = []
    nodes = [0]
    def find(x):
        while par[x] != x: x = par[x]
        return x
    def rec(i, nplaced_mask_count):
        nodes[0] += 1
        if node_cap and nodes[0] > node_cap: raise TimeoutError
        if i == n: return True
        cands = [v for v in range(n) if not placed[v] and lo[v] <= i+1 <= hi[v]]
        # forced vertices must be placed now
        forced = [v for v in cands if hi[v] == i+1]
        if len(forced) > 1: return False
        if forced: cands = forced
        for v in cands:
            beta = 0
            for u in range(n):
                if u == v: continue
                if placed[u]:
                    if arc[v][u]: beta += 1
                else:
                    if arc[u][v]: beta += 1
            if beta > 2: continue
            newe = [u for u in range(n) if placed[u] and arc[v][u]]
            roots = []
            ok = True
            undo = []
            for u in newe:
                rv, ru = find(v), find(u)
                if rv == ru: ok = False; break
                par[rv] = ru; undo.append(rv)
            if ok:
                placed[v] = True; order.append(v)
                if rec(i+1, 0): return True
                placed[v] = False; order.pop()
            for r in reversed(undo): par[r] = r
        return False
    try:
        ok = rec(0, 0)
    except TimeoutError:
        return 'TIMEOUT'
    if verbose: print("   search nodes:", nodes[0])
    return list(order) if ok else None

# -------------------------------------------------------------- sat brute force
def sat(formula, nvars):
    for bits in itertools.product([False, True], repeat=nvars):
        if all(any(bits[v] == s for v, s in cl) for cl in formula):
            return bits
    return None

# ------------------------------------------------ explicit ordering from assignment
def ordering_from_assignment(n, arc, info, assign):
    """Section 4.5 construction."""
    order = list(range(n))   # sigma
    for x, ids in info['gadget'].items():
        m = len(ids)
        t = 1 if assign[x] else 0
        Mother = [(i, i+1) for i in range(1-t, m-1, 2)]   # M_{1-t}
        for (i, j) in Mother:
            pi_, pj = order.index(ids[i]), order.index(ids[j])
            order[pi_], order[pj] = order[pj], order[pi_]
    return order

def main():
    tests = []
    tests.append(("SAT: (x|y|z)", [[(0, True), (1, True), (2, True)]], 3))
    tests.append(("SAT: (x|y|z)&(~x|~y|~z)",
                  [[(0, True), (1, True), (2, True)],
                   [(0, False), (1, False), (2, False)]], 3))
    all8 = [[(0, s0), (1, s1), (2, s2)] for s0 in (True, False)
            for s1 in (True, False) for s2 in (True, False)]
    tests.append(("UNSAT: all 8 clauses on x,y,z", all8, 3))
    tests.append(("SAT (unique): 7 of the 8 clauses", all8[1:], 3))
    tests.append(("UNSAT: 4 vars, all 8 on x,y,z plus (x|y|w)", all8 + [[(0, True), (1, True), (3, True)]], 4))

    for label, formula, nvars in tests:
        t0 = time.time()
        n, arc, info = build(formula, nvars)
        s = sat(formula, nvars)
        # structural checks on sigma
        sigma = list(range(n))
        Bs = backward_graph(arc, n, sigma)
        deg = {}
        for e in Bs:
            for v in e: deg[v] = deg.get(v, 0)+1
        maxdeg_sigma = max(deg.values()) if deg else 0
        Wmin = min(abs(max(e)-min(e)) for e in info['W'])
        # forced-backward check via d=2 score intervals
        outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
        aa = [n-outdeg[v] for v in range(n)]
        lo = [max(1, aa[v]-2) for v in range(n)]
        hi = [min(n, aa[v]+2) for v in range(n)]
        forced_ok = all(hi[min(e)] < lo[max(e)] for e in info['W'])
        res = solve(arc, n, verbose=True)
        found = res is not None and res != 'TIMEOUT'
        print(f"[{label}]")
        print(f"   n={n}, |W|={len(info['W'])}, Delta(B_sigma)={maxdeg_sigma}, "
              f"min sigma-gap of a wire={Wmin}, all wires forced backward by d=2 intervals: {forced_ok}")
        print(f"   3-SAT satisfiable: {s is not None}   linear-forest ordering exists: "
              f"{found if res!='TIMEOUT' else 'TIMEOUT'}")
        if found:
            assert is_linear_forest(backward_graph(arc, n, res), n), "solver returned junk"
        if s is not None:
            o = ordering_from_assignment(n, arc, info, s)
            B = backward_graph(arc, n, o)
            print(f"   explicit ordering from the satisfying assignment: "
                  f"B_pi linear forest = {is_linear_forest(B, n)}, |B_pi|={len(B)}, "
                  f"W subset of B_pi = {info['W'] <= B}")
        agree = (s is not None) == found
        print(f"   EQUIVALENCE HOLDS: {agree}    [{time.time()-t0:.1f}s]")
        if not agree: print("   *** MISMATCH ***")
        print()

main()
