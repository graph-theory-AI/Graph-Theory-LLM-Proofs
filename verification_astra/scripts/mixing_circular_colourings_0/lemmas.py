"""Direct tests of Lemma 1/2 (orientation classes connected off E_n),
Lemma 3 (feasibility of X_D depends only on k/q, constant on intervals of
(2,inf)\E_s), and the quotient criterion of Section 4."""
from fractions import Fraction
from itertools import product
import sys

def E(N):
    s = set()
    for a in range(2, N + 1):
        for b in range(1, a // 2 + 1):
            s.add(Fraction(a, b))
    return s

def colourings(n, edges, k, q):
    out = []
    for f in product(range(k), repeat=n):
        if all(q <= abs(f[u]-f[v]) <= k-q for (u, v) in edges):
            out.append(f)
    return out

def orient(f, edges):
    return tuple(1 if f[u] < f[v] else 0 for (u, v) in edges)

def comps(nodes, nbr):
    seen, c = set(), 0
    for s in nodes:
        if s in seen: continue
        c += 1; stack=[s]; seen.add(s)
        while stack:
            x = stack.pop()
            for y in nbr(x):
                if y not in seen:
                    seen.add(y); stack.append(y)
        return_c = c
    return c

def analyse(n, edges, k, q):
    C = colourings(n, edges, k, q)
    S = set(C)
    classes = {}
    for f in C:
        classes.setdefault(orient(f, edges), []).append(f)
    # per-class connectivity under UNIT moves
    unit_bad, any_bad = [], []
    for D, L in classes.items():
        LS = set(L)
        def nbr_unit(x):
            for v in range(n):
                for d in (-1, 1):
                    y = list(x); y[v] += d; y = tuple(y)
                    if y in LS: yield y
        def nbr_any(x):
            for v in range(n):
                for c in range(k):
                    if c == x[v]: continue
                    y = list(x); y[v] = c; y = tuple(y)
                    if y in LS: yield y
        if comps(L, nbr_unit) != 1: unit_bad.append(D)
        if comps(L, nbr_any) != 1: any_bad.append(D)
    # quotient graph Q
    qadj = {}
    for f in C:
        Df = orient(f, edges)
        for v in range(n):
            for c in range(k):
                if c == f[v]: continue
                g = list(f); g[v] = c; g = tuple(g)
                if g in S:
                    Dg = orient(g, edges)
                    if Dg != Df:
                        qadj.setdefault(Df, set()).add(Dg)
                        qadj.setdefault(Dg, set()).add(Df)
    Qnodes = list(classes)
    Qconn = (len(Qnodes) > 0 and
             comps(Qnodes, lambda x: qadj.get(x, ())) == 1)
    # full reconfiguration connectivity
    def nbrR(x):
        for v in range(n):
            for c in range(k):
                if c == x[v]: continue
                y = list(x); y[v] = c; y = tuple(y)
                if y in S: yield y
    Rconn = (len(C) > 0 and comps(C, nbrR) == 1)
    return dict(ncol=len(C), nclasses=len(classes), unit_bad=unit_bad,
                any_bad=any_bad, Qconn=Qconn, Rconn=Rconn,
                feas=frozenset(classes))

GRAPHS = {
    "K2":   (2, [(0,1)]),
    "P3":   (3, [(0,1),(1,2)]),
    "K3":   (3, [(0,1),(1,2),(0,2)]),
    "P4":   (4, [(0,1),(1,2),(2,3)]),
    "C4":   (4, [(0,1),(1,2),(2,3),(3,0)]),
    "K4":   (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
    "paw":  (4, [(0,1),(1,2),(2,0),(0,3)]),
    "C5":   (5, [(0,1),(1,2),(2,3),(3,4),(4,0)]),
    "bull": (5, [(0,1),(1,2),(2,0),(0,3),(1,4)]),
}

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
for name in (sys.argv[2:] or list(GRAPHS)):
    n, edges = GRAPHS[name]
    En, En1 = E(n), E(n+1)
    print(f"=== {name} n={n}")
    L2fail_off, L2fail_on = [], []
    Qfail = []
    feas_by_ratio = {}
    for k in range(2, KMAX+1):
        for q in range(1, k//2+1):
            r = Fraction(k, q)
            a = analyse(n, edges, k, q)
            if a["unit_bad"] or a["any_bad"]:
                (L2fail_on if r in En else L2fail_off).append(
                    (k, q, len(a["unit_bad"]), len(a["any_bad"])))
            if r not in En and a["Rconn"] != a["Qconn"]:
                Qfail.append((k, q, a["Rconn"], a["Qconn"]))
            feas_by_ratio.setdefault(r, {})[(k, q)] = a["feas"]
    print(f"  Lemma 2 FAILURES at k/q NOT in E_n  (should be empty): {L2fail_off}")
    print(f"  Lemma 2 failures at k/q in E_n (expected/allowed): {len(L2fail_on)} cases"
          f" e.g. {L2fail_on[:4]}")
    print(f"  Quotient-criterion failures off E_n (should be empty): {Qfail}")
    # Lemma 3 part 1: feasible orientation set depends only on ratio
    bad1 = [(str(r), len({v for v in d.values()})) for r, d in feas_by_ratio.items()
            if len(set(d.values())) > 1]
    print(f"  Lemma 3(1) representation-dependence of feasible-class set"
          f" (should be empty): {bad1}")
    # Lemma 3 part 2: constant on component intervals of (2,inf)\E_{n+1}
    pts = sorted(x for x in En1 if x > 2)
    rs = sorted(feas_by_ratio)
    bad2 = []
    for i in range(len(rs)):
        for j in range(i+1, len(rs)):
            r1, r2 = rs[i], rs[j]
            if r1 <= 2: continue
            if any(r1 <= p <= r2 for p in pts): continue
            f1 = next(iter(feas_by_ratio[r1].values()))
            f2 = next(iter(feas_by_ratio[r2].values()))
            if f1 != f2: bad2.append((str(r1), str(r2)))
    print(f"  Lemma 3(2) non-constancy on an interval (should be empty): {bad2[:6]}"
          f" count={len(bad2)}")
