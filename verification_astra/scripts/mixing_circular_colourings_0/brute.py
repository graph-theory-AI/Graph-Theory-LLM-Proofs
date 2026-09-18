"""Brute-force (k,q)-mixing for small graphs.

Convention (as in the writeup): G is (k,q)-mixing iff the reconfiguration graph
R_{k,q}(G) (vertices = (k,q)-colourings, edges = differ in exactly one vertex)
is NONEMPTY and CONNECTED.
"""
from fractions import Fraction
from itertools import product, combinations
import sys

def colourings(n, edges, k, q):
    out = []
    for f in product(range(k), repeat=n):
        ok = True
        for (u, v) in edges:
            d = abs(f[u] - f[v])
            if not (q <= d <= k - q):
                ok = False
                break
        if ok:
            out.append(f)
    return out

def mixing(n, edges, k, q, want_components=False):
    C = colourings(n, edges, k, q)
    if not C:
        return (False, 0, 0) if want_components else False
    idx = {f: i for i, f in enumerate(C)}
    parent = list(range(len(C)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    for f in C:
        i = idx[f]
        for v in range(n):
            for c in range(k):
                if c == f[v]:
                    continue
                g = list(f); g[v] = c; g = tuple(g)
                j = idx.get(g)
                if j is not None:
                    union(i, j)
    ncomp = len({find(i) for i in range(len(C))})
    if want_components:
        return (ncomp == 1, len(C), ncomp)
    return ncomp == 1

def E(N):
    """{a/b : a,b>0, 2b <= a <= N}"""
    s = set()
    for a in range(2, N + 1):
        for b in range(1, a // 2 + 1):
            s.add(Fraction(a, b))
    return sorted(s)

GRAPHS = {
    "K2":   (2, [(0,1)]),
    "P3":   (3, [(0,1),(1,2)]),
    "K3":   (3, [(0,1),(1,2),(0,2)]),
    "P4":   (4, [(0,1),(1,2),(2,3)]),
    "C4":   (4, [(0,1),(1,2),(2,3),(3,0)]),
    "K4":   (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
    "star3":(4, [(0,1),(0,2),(0,3)]),
    "C5":   (5, [(0,1),(1,2),(2,3),(3,4),(4,0)]),
    "K23":  (5, [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]),
    "bull": (5, [(0,1),(1,2),(2,0),(0,3),(1,4)]),
    "C6":   (6, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]),  # = L_3 = K33 minus PM
}

def main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 13
    names = sys.argv[2:] if len(sys.argv) > 2 else list(GRAPHS)
    for name in names:
        n, edges = GRAPHS[name]
        En1 = E(n + 1)
        print(f"=== {name}: n={n}, |E|={len(edges)};  E_(n+1) = {[str(x) for x in En1]}")
        results = {}   # Fraction -> dict (k,q)->bool
        for k in range(2, KMAX + 1):
            for q in range(1, k // 2 + 1):
                r = Fraction(k, q)
                m = mixing(n, edges, k, q)
                results.setdefault(r, {})[(k, q)] = m
        # (a) representation dependence
        repdep = [(r, d) for r, d in results.items() if len(set(d.values())) > 1]
        # (b) bad ratios
        bad = sorted(r for r, d in results.items() if not all(d.values()))
        good = sorted(r for r, d in results.items() if all(d.values()))
        supbad = max(bad) if bad else None
        print(f"    bad ratios (some rep not mixing): {[str(x) for x in bad]}")
        print(f"    sup(bad) = {supbad}   in E_(n+1)? {supbad in En1 if supbad is not None else 'n/a'}")
        if repdep:
            print(f"    REPRESENTATION-DEPENDENT ratios: "
                  f"{[(str(r), d) for r, d in repdep]}")
            for r, d in repdep:
                print(f"        {r} in E_(n+1)? {r in En1}")
        else:
            print("    no representation-dependent ratio found in range")
        # (c) Prop 4: constancy on component intervals of (2,inf) \ E_{n+1}
        pts = [x for x in En1 if x > 2]
        viol = []
        for r, d in results.items():
            if r <= 2:
                continue
            for r2, d2 in results.items():
                if r2 <= 2 or r2 <= r:
                    continue
                # same component interval iff no point of E_{n+1} in [r, r2]
                if any(r <= p <= r2 for p in pts):
                    continue
                if all(d.values()) != all(d2.values()):
                    viol.append((str(r), str(r2)))
        print(f"    Prop.4 violations (same open interval, different mixing): {viol[:10]}"
              f"{' ...' if len(viol) > 10 else ''}  count={len(viol)}")
        # (d) Section 5: k/q >= n+1 => mixing
        s5 = [(k, q) for k in range(2, KMAX + 1) for q in range(1, k // 2 + 1)
              if Fraction(k, q) >= n + 1 and not mixing(n, edges, k, q)]
        print(f"    Sec.5 counterexamples (k/q>=n+1 but not mixing): {s5}")
        print()

main()
