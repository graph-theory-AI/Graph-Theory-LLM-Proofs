"""
Verification of the writeup's counterexample D_d for target 2510.11311__04.

Builds D_d = B -> A_1 -(Q)-> A_2 -(Q)-> ... -(Q)-> A_L -> B  with
  |B| = d, M = C(d,2), L = M+1, Q a d-regular bipartite graph of girth > 2M.
Checks: oriented (no digon), Eulerian (d^+ = d^-), delta^+ = d, strongly connected.
Then decides EXACTLY whether D_d has a NONEMPTY subdigraph H with
delta^+(H) >= 2 that is K_{2,2}-free (no two distinct vertices with two
common out-neighbours).

Exact reduction used (equivalence proved in the report):
  such an H exists  <=>  there is a nonempty S subset V and an injective
  assignment v -> P_v, P_v a 2-subset of N^+(v) cap S  (a system of distinct
  representatives).  Reason: delete arcs so every out-degree is exactly 2;
  K_{2,2}-freeness of a 2-out digraph is exactly "all P_v pairwise distinct".

Two independent decision procedures:
  (A) exhaustive enumeration of all vertex subsets + bipartite matching (small d=2)
  (B) MILP feasibility (HiGHS via scipy) on the arc/vertex indicator formulation
"""
import itertools, sys
import networkx as nx
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


# ---------- building blocks ----------------------------------------------

def cycle_bipartite(n):
    """2-regular bipartite graph: the 2n-cycle, parts X=0..n-1, Y=0..n-1."""
    adj = {i: sorted({i, (i - 1) % n}) for i in range(n)}   # X_i ~ Y_i , Y_{i-1}
    return n, adj


def tutte_coxeter():
    """3-regular bipartite graph of girth 8 (Tutte-Coxeter / Levi graph of GQ(2,2))."""
    G = nx.LCF_graph(30, [-13, -9, 7, -7, 9, 13], 5)
    assert nx.is_bipartite(G)
    assert all(deg == 3 for _, deg in G.degree())
    assert nx.girth(G) == 8, nx.girth(G)
    X, Y = nx.bipartite.sets(G)
    X, Y = sorted(X), sorted(Y)
    xi = {v: i for i, v in enumerate(X)}
    yi = {v: i for i, v in enumerate(Y)}
    adj = {i: sorted(yi[w] for w in G[v]) for v, i in xi.items()}
    return len(X), adj


def heawood():
    """3-regular bipartite graph of girth 6 (Heawood graph) -- girth TOO SMALL for d=3."""
    G = nx.heawood_graph()
    X, Y = nx.bipartite.sets(G)
    X, Y = sorted(X), sorted(Y)
    xi = {v: i for i, v in enumerate(X)}
    yi = {v: i for i, v in enumerate(Y)}
    adj = {i: sorted(yi[w] for w in G[v]) for v, i in xi.items()}
    return len(X), adj


def bipartite_girth(nX, adj):
    G = nx.Graph()
    G.add_nodes_from(("X", i) for i in range(nX))
    for i, nb in adj.items():
        for j in nb:
            G.add_edge(("X", i), ("Y", j))
    return nx.girth(G)


def build_D(d, L, nQ, adjQ, nB=None):
    """Return a networkx DiGraph for the layered construction."""
    nB = d if nB is None else nB
    D = nx.DiGraph()
    B = [("B", i) for i in range(nB)]
    A = [[("A", i, j) for j in range(nQ)] for i in range(1, L + 1)]
    D.add_nodes_from(B)
    for layer in A:
        D.add_nodes_from(layer)
    for b in B:                       # all arcs B -> A_1
        for a in A[0]:
            D.add_edge(b, a)
    for i in range(L - 1):            # copy of Q from A_i to A_{i+1}
        for x, nb in adjQ.items():
            for y in nb:
                D.add_edge(A[i][x], A[i + 1][y])
    for a in A[L - 1]:                # all arcs A_L -> B
        for b in B:
            D.add_edge(a, b)
    return D, B, A


def structural_report(D, d, name):
    digons = [(u, v) for u, v in D.edges() if D.has_edge(v, u)]
    outs = [D.out_degree(v) for v in D]
    ins = [D.in_degree(v) for v in D]
    eul = all(D.out_degree(v) == D.in_degree(v) for v in D)
    sc = nx.is_strongly_connected(D)
    print(f"  [{name}] |V|={D.number_of_nodes()} |A|={D.number_of_edges()} "
          f"digons={len(digons)} Eulerian={eul} strongly_connected={sc} "
          f"delta^+={min(outs)} Delta^+={max(outs)} (target delta^+={d})")
    return dict(eulerian=eul, oriented=not digons, strongly_connected=sc,
                delta_out=min(outs), delta_in=min(ins))


# ---------- decision procedure (A): exhaustive over vertex subsets --------

def exists_core_exhaustive(D):
    V = list(D.nodes())
    idx = {v: i for i, v in enumerate(V)}
    n = len(V)
    assert n <= 22, "too big for exhaustive enumeration"
    for mask in range(1, 1 << n):
        S = [V[i] for i in range(n) if mask >> i & 1]
        Sset = set(S)
        ok = True
        Gm = nx.Graph()
        for v in S:
            nb = [w for w in D.successors(v) if w in Sset]
            if len(nb) < 2:
                ok = False
                break
            Gm.add_node(("v", v), bipartite=0)
            for p in itertools.combinations(sorted(nb, key=lambda z: idx[z]), 2):
                Gm.add_edge(("v", v), ("p", p))
        if not ok:
            continue
        m = nx.algorithms.bipartite.maximum_matching(
            Gm, top_nodes=[("v", v) for v in S])
        if sum(1 for k in m if k[0] == "v") == len(S):
            return S, m
    return None, None


# ---------- decision procedure (B): MILP feasibility ---------------------

def exists_core_milp(D, kmin=2):
    V = list(D.nodes())
    arcs = list(D.edges())
    vi = {v: i for i, v in enumerate(V)}
    ai = {a: len(V) + i for i, a in enumerate(arcs)}
    N = len(V) + len(arcs)
    rows, lo, hi = [], [], []

    def add(coeffs, l, h):
        r = np.zeros(N)
        for j, c in coeffs:
            r[j] += c
        rows.append(r); lo.append(l); hi.append(h)

    for (u, v) in arcs:                       # x_uv <= y_u , x_uv <= y_v
        add([(ai[(u, v)], 1), (vi[u], -1)], -np.inf, 0)
        add([(ai[(u, v)], 1), (vi[v], -1)], -np.inf, 0)
    for v in V:                               # sum_out x >= kmin * y_v
        add([(ai[(v, w)], 1) for w in D.successors(v)] + [(vi[v], -kmin)], 0, np.inf)
    add([(vi[v], 1) for v in V], 1, np.inf)   # nonempty
    ncons_ff = 0
    for u, v in itertools.combinations(V, 2): # K_{2,2}-freeness
        common = sorted(set(D.successors(u)) & set(D.successors(v)), key=lambda z: vi[z])
        if len(common) < 2:
            continue
        for a, b in itertools.combinations(common, 2):
            add([(ai[(u, a)], 1), (ai[(u, b)], 1), (ai[(v, a)], 1), (ai[(v, b)], 1)],
                -np.inf, 3)
            ncons_ff += 1
    A = np.array(rows)
    res = milp(c=np.zeros(N), constraints=LinearConstraint(A, lo, hi),
               integrality=np.ones(N), bounds=Bounds(0, 1))
    return res, ncons_ff


# ---------- experiments ---------------------------------------------------

def run(name, d, L, nQ, adjQ, exhaustive=False, nB=None, expect=None):
    print(f"\n=== {name} ===")
    print(f"  Q: {len(adjQ)}+{nQ} vertices, girth={bipartite_girth(nQ, adjQ)}, "
          f"d={d}, M=C(d,2)={d*(d-1)//2}, L={L}")
    D, B, A = build_D(d, L, nQ, adjQ, nB=nB)
    structural_report(D, d, name)
    res, nff = exists_core_milp(D)
    feas = (res.status == 0)
    print(f"  MILP: status={res.status} ({res.message.strip()[:60]}) "
          f"F-free constraints={nff}  ->  core exists: {feas}")
    if exhaustive:
        S, m = exists_core_exhaustive(D)
        print(f"  exhaustive over 2^{D.number_of_nodes()} subsets -> core exists: {S is not None}")
        assert (S is not None) == feas, "MILP and exhaustive disagree!"
    if expect is not None:
        assert feas == expect, f"expected core-exists={expect}, got {feas}"
    return feas


if __name__ == "__main__":
    # ---- d = 2 : M = 1, L = 2, Q must have girth > 2 (any simple bipartite) ----
    for n in (4, 5, 6, 7):
        nQ, adjQ = cycle_bipartite(n)
        run(f"D_2 with Q = C_{2*n}", d=2, L=2, nQ=nQ, adjQ=adjQ,
            exhaustive=(n <= 7), expect=False)

    # ---- d = 3 : M = 3, L = 4, Q needs girth > 6, i.e. >= 8 : Tutte-Coxeter ----
    nQ, adjQ = tutte_coxeter()
    run("D_3 with Q = Tutte-Coxeter (girth 8)", d=3, L=4, nQ=nQ, adjQ=adjQ, expect=False)

    # ---- controls: the hypotheses must be needed ----
    print("\n### CONTROLS (encoding sanity: solver must FIND cores when they exist) ###")
    # (C1) too few layers: L = 2 instead of 4 for d = 3
    run("CONTROL D_3 with only L=2 layers (proof needs L=M+1=4)", d=3, L=2,
        nQ=nQ, adjQ=adjQ)
    run("CONTROL D_3 with only L=3 layers", d=3, L=3, nQ=nQ, adjQ=adjQ)
    # (C2) large B: the pair-count bound C(|B|,2) no longer bites at M=3
    run("CONTROL D_3 but |B|=8 (breaks the small-bottleneck bound)", d=3, L=4,
        nQ=nQ, adjQ=adjQ, nB=8)
    # (C3) girth too small for d=3 (Heawood, girth 6, needs > 6)
    nH, adjH = heawood()
    run("CONTROL D_3 with Q = Heawood (girth 6 -- violates girth>2M=6)", d=3, L=4,
        nQ=nH, adjQ=adjH)
