"""End-to-end test of the writeup's machinery.

Builds Q_{k,q}(G) using ONLY difference-constraint feasibility (Bellman-Ford),
exactly as Sections 3-4 prescribe, and compares "Q nonempty and connected"
against brute-force "(k,q)-mixing" (reconfiguration graph nonempty+connected).
By Lemma 2 these must agree whenever k/q is not in E_n.
"""
from fractions import Fraction
from itertools import product
import sys

def E(N):
    return {Fraction(a, b) for a in range(2, N+1) for b in range(1, a//2+1)}

def feasible(nv, arcs, k):
    """arcs: list (i,j,c) meaning x_j - x_i <= c ; plus box 0<=x_i<=k-1 via node nv (=*)
    Returns True iff the integer system is feasible (no negative cycle)."""
    N = nv + 1
    star = nv
    A = list(arcs)
    for i in range(nv):
        A.append((star, i, k-1))
        A.append((i, star, 0))
    d = [0]*N
    for _ in range(N):
        changed = False
        for (i, j, c) in A:
            if d[i] + c < d[j]:
                d[j] = d[i] + c
                changed = True
        if not changed:
            return True
    return False

def class_arcs(edges, D, q, k):
    """D: dict edge-index -> 0/1 (1 means u->v, 0 means v->u). Returns arcs."""
    arcs = []
    for e, (u, v) in enumerate(edges):
        a, b = (u, v) if D[e] == 1 else (v, u)   # a -> b, i.e. x_a < x_b
        arcs.append((b, a, -q))    # x_a - x_b <= -q
        arcs.append((a, b, k-q))   # x_b - x_a <= k-q
    return arcs

def Q_graph(n, edges, k, q):
    orients = list(product([0, 1], repeat=len(edges)))
    nodes = [D for D in orients if feasible(n, class_arcs(edges, D, q, k), k)]
    nodeset = set(nodes)
    adj = {D: set() for D in nodes}
    for D in nodes:
        for D2 in nodes:
            if D2 <= D:   # tuple order, do each unordered pair once
                continue
            diff = [e for e in range(len(edges)) if D[e] != D2[e]]
            # all differing edges must share a common vertex v
            cand = set(range(n))
            for e in diff:
                cand &= set(edges[e])
            for v in cand:
                # twin graph: v0 = v, v1 = new vertex n
                arcs = []
                for e, (x, y) in enumerate(edges):
                    if v in (x, y):
                        # copy for v0 (orientation D) and v1 (orientation D2)
                        for (Dc, vid) in ((D, v), (D2, n)):
                            xx = vid if x == v else x
                            yy = vid if y == v else y
                            a, b = (xx, yy) if Dc[e] == 1 else (yy, xx)
                            arcs.append((b, a, -q)); arcs.append((a, b, k-q))
                    else:
                        a, b = (x, y) if D[e] == 1 else (y, x)
                        arcs.append((b, a, -q)); arcs.append((a, b, k-q))
                if feasible(n+1, arcs, k):
                    adj[D].add(D2); adj[D2].add(D)
                    break
    if not nodes:
        return False
    seen = {nodes[0]}; st = [nodes[0]]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); st.append(y)
    return len(seen) == len(nodes)

def brute_mixing(n, edges, k, q):
    C = [f for f in product(range(k), repeat=n)
         if all(q <= abs(f[u]-f[v]) <= k-q for (u, v) in edges)]
    if not C:
        return False
    S = set(C)
    seen = {C[0]}; st = [C[0]]
    while st:
        x = st.pop()
        for v in range(n):
            for c in range(k):
                if c == x[v]: continue
                y = list(x); y[v] = c; y = tuple(y)
                if y in S and y not in seen:
                    seen.add(y); st.append(y)
    return len(seen) == len(C)

GRAPHS = {
    "K2":(2,[(0,1)]), "P3":(3,[(0,1),(1,2)]), "K3":(3,[(0,1),(1,2),(0,2)]),
    "P4":(4,[(0,1),(1,2),(2,3)]), "C4":(4,[(0,1),(1,2),(2,3),(3,0)]),
    "paw":(4,[(0,1),(1,2),(2,0),(0,3)]), "K4":(4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
    "diamond":(4,[(0,1),(0,2),(0,3),(1,2),(1,3)]),
    "C5":(5,[(0,1),(1,2),(2,3),(3,4),(4,0)]),
    "bull":(5,[(0,1),(1,2),(2,0),(0,3),(1,4)]),
    "house":(5,[(0,1),(1,2),(2,3),(3,4),(4,0),(1,4)]),
    "K23":(5,[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]),
}

def _main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    tot = mism = 0
    for name in (sys.argv[2:] or list(GRAPHS)):
        n, edges = GRAPHS[name]
        En = E(n)
        bad = []
        for k in range(2, KMAX+1):
            for q in range(1, k//2+1):
                r = Fraction(k, q)
                b = brute_mixing(n, edges, k, q)
                Qc = Q_graph(n, edges, k, q)
                tot += 1
                if b != Qc:
                    bad.append((k, q, str(r), r in En, b, Qc))
                    if r not in En: mism += 1
        off = [x for x in bad if not x[3]]
        on  = [x for x in bad if x[3]]
        print(f"{name}: mismatches OFF E_n (must be empty): {off}")
        print(f"        mismatches AT E_n (allowed): {len(on)} e.g. {on[:3]}")
    print(f"TOTAL pairs tested {tot}; fatal mismatches off E_n: {mism}")

if __name__ == "__main__":
    _main()
