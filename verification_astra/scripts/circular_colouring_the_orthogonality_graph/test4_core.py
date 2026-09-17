"""Independent verification that a concrete finite subgraph of O has chi_c > 7/2.

Step 1: from the 49 lines with integer coordinates in [-2,2], shrink to a small vertex set
        that still admits no homomorphism to K_{7/2} (greedy deletion).
Step 2: re-verify that small core with a SECOND, deliberately naive solver (plain DFS over
        vertices in index order, no forward checking, no symmetry breaking beyond fixing
        one vertex, written independently of circ.py).
Step 3: also check the core against every K_{p/q} with p/q <= 7/2 and p <= |core|, and
        print the core's vectors so the result is human-checkable.
"""
import sys
from fractions import Fraction
from itertools import combinations
from math import gcd

from circ import hom_exists, to_nbrs, fractions_upto
from geom import primitive_lines, ortho_graph


def p(*a):
    print(*a)
    sys.stdout.flush()


# ---------- second, independent solver ----------
def naive_hom(adjlist, n, P, Q):
    """Plain DFS: is there f: V -> Z_P with Q <= (f(v)-f(u)) mod P <= P-Q on every edge?"""
    def compat(a, b):
        d = (b - a) % P
        return Q <= d <= P - Q

    col = [-1] * n

    def rec(v):
        if v == n:
            return True
        lo = 1 if v > 0 else 1   # placeholder
        for c in range(P):
            if v == 0 and c != 0:
                break  # translation automorphism x -> x+1 of K_{P/Q}
            ok = True
            for u in adjlist[v]:
                if u < v and not compat(col[u], c):
                    ok = False
                    break
            if ok:
                col[v] = c
                if rec(v + 1):
                    return True
                col[v] = -1
        return False

    return rec(0)


LINES = primitive_lines(2)
U, E = ortho_graph(LINES)
n0 = len(LINES)
p(f"start: {n0} lines (integer coords in [-2,2]), {len(E)} orthogonal pairs")

keep = list(range(n0))


def sub(keepset):
    idx = {v: i for i, v in enumerate(keepset)}
    edges = [(idx[a], idx[b]) for a, b in E if a in idx and b in idx]
    return len(keepset), edges


def colourable_72(keepset):
    m, edges = sub(keepset)
    return hom_exists(to_nbrs(m, edges), m, 7, 2)


p(f"full set K_{{7/2}}-colourable? {colourable_72(keep)}")

changed = True
while changed:
    changed = False
    for v in list(keep):
        trial = [w for w in keep if w != v]
        if not colourable_72(trial):
            keep = trial
            changed = True
p(f"core after greedy deletion: {len(keep)} vertices")

m, edges = sub(keep)
p(f"core: n={m}, edges={len(edges)}")
p("core lines (primitive integer direction vectors):")
for i, v in enumerate(keep):
    p(f"   {i}: {tuple(int(round(x)) for x in LINES[v])}")
p(f"core edges: {sorted(edges)}")

adjlist = [[] for _ in range(m)]
for a, b in edges:
    adjlist[a].append(b)
    adjlist[b].append(a)

p("\nindependent naive solver:")
p(f"   core -> K_{{7/2}} : {naive_hom(adjlist, m, 7, 2)}")
p(f"   core -> K_{{4/1}} : {naive_hom(adjlist, m, 4, 1)}")
p(f"   core -> K_{{11/3}}: {naive_hom(adjlist, m, 11, 3)}")
p(f"   core -> K_{{15/4}}: {naive_hom(adjlist, m, 15, 4)}")
p("   (sanity: C5 -> K_{5/2} should be True, C5 -> K_{7/3} should be False)")
c5 = [[1, 4], [0, 2], [1, 3], [2, 4], [3, 0]]
p(f"   C5  -> K_{{5/2}} : {naive_hom(c5, 5, 5, 2)}")
p(f"   C5  -> K_{{7/3}} : {naive_hom(c5, 5, 7, 3)}")

p("\nexact chi_c of the core, both solvers:")
cands = [f for f in fractions_upto(m) if f <= Fraction(7, 2)]
nb = to_nbrs(m, edges)
for f in cands:
    a = hom_exists(nb, m, f.numerator, f.denominator)
    b = naive_hom(adjlist, m, f.numerator, f.denominator)
    if a != b:
        p(f"   SOLVER DISAGREEMENT at {f}: {a} vs {b}")
p(f"   no ratio <= 7/2 works: {not any(hom_exists(nb, m, f.numerator, f.denominator) for f in cands)}")
# now find the exact value
val = None
for f in fractions_upto(m):
    if hom_exists(nb, m, f.numerator, f.denominator):
        val = f
        break
p(f"   chi_c(core) = {val} = {float(val):.6f}")
