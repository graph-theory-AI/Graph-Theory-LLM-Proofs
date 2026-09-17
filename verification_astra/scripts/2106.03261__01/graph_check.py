"""Independent verification of the construction in attacks_retry/2106.03261__01/output.md.

G_q: vertices F_q^2 = {(x,y)}.  Classes V_r = T_r x F_q, r in V(Petersen),
T_r = {x in {0..q-1} : x mod 10 == index(r)}.
Edge between (x,y) in V_r and (x',y') in V_s iff rs in E(P) and y+y'+x x' = c_rs,
with c_rs = 1 for rs = ij and 0 otherwise.

Checks:
  - simple graph, no loops
  - every pair of distinct vertices has codegree <= 1  (C4-freeness)
  - triangle-free
  - degrees equal sum_{s in N(r)} |T_s|, and Delta < sqrt(N)
  - each required pair has density exactly 1/q
  - e(G) = q * sum_{rs in E(P)} |T_r||T_s|
  - exhaustive search for canonical Petersen copies (should be 0),
    together with a count of "Petersen minus ij" canonical configurations
    and the value of <I,J> = y_I+y_J+x_I x_J on each of them.
  - control: the same graph with ALL c_rs = 0 (pure polarity model) is also
    C4-free and DOES contain canonical Petersen copies, one for each
    Petersen-minus-ij configuration.
"""
import sys, itertools
from collections import defaultdict
import numpy as np

LAB = "abcdefghij"
# Kneser labelling from the writeup
KN = {'a': (1,2), 'b': (1,3), 'c': (1,4), 'd': (4,5), 'e': (3,5),
      'f': (2,5), 'g': (2,3), 'h': (2,4), 'i': (3,4), 'j': (1,5)}
EDGES = [(u, v) for u, v in itertools.combinations(LAB, 2)
         if not (set(KN[u]) & set(KN[v]))]
ADJ = {r: sorted(s for s in LAB if (min(r,s),max(r,s)) in
                 [(min(u,v),max(u,v)) for u,v in EDGES]) for r in LAB}

def cconst(r, s, twisted=True):
    return 1 if (twisted and {r, s} == {'i', 'j'}) else 0

def build(q, twisted=True):
    idx = {r: k for k, r in enumerate(LAB)}
    T = {r: [x for x in range(q) if x % 10 == idx[r]] for r in LAB}
    cls = {}
    for r in LAB:
        for x in T[r]:
            cls[x] = r
    V = [(x, y) for x in range(q) for y in range(q)]
    adj = defaultdict(set)
    for (x, y) in V:
        r = cls[x]
        for s in ADJ[r]:
            c = cconst(r, s, twisted)
            for xp in T[s]:
                yp = (c - y - x * xp) % q
                adj[(x, y)].add((xp, yp))
    return T, cls, adj, V

def checks(q, twisted=True, verbose=True):
    T, cls, adj, V = build(q, twisted)
    N = q * q
    # symmetry / no loops
    for u in V:
        assert u not in adj[u], "loop!"
        for v in adj[u]:
            assert u in adj[v], "asymmetric!"
    # degrees
    degs = {}
    for r in LAB:
        degs[r] = sum(len(T[s]) for s in ADJ[r])
    for (x, y) in V:
        assert len(adj[(x, y)]) == degs[cls[x]], "degree mismatch"
    Delta = max(degs.values())
    # codegree <= 1  (C4-freeness)
    codeg = defaultdict(int)
    for w in V:
        nb = sorted(adj[w])
        for a, b in itertools.combinations(nb, 2):
            codeg[(a, b)] += 1
    maxcodeg = max(codeg.values()) if codeg else 0
    # triangles
    tri = 0
    for u in V:
        for v in adj[u]:
            if v > u:
                tri += len(adj[u] & adj[v])
    # edges and pair densities
    m = sum(len(adj[u]) for u in V) // 2
    dens = set()
    for (r, s) in EDGES:
        cnt = sum(1 for x in T[r] for y in range(q) for (xp, yp) in adj[(x, y)] if cls[xp] == s)
        dens.add((cnt, len(T[r]) * q * len(T[s]) * q))
    densvals = sorted({(a, b) for a, b in dens})
    ok_dens = all(abs(a / b - 1.0 / q) < 1e-12 for a, b in densvals)
    m_formula = q * sum(len(T[r]) * len(T[s]) for r, s in EDGES)
    if verbose:
        print(f"  q={q} N={N} twisted={twisted}")
        print(f"    max degree = {Delta}  (sqrt(N) = {q}), degrees by class = "
              f"{ {r: degs[r] for r in LAB} }")
        print(f"    max codegree over all vertex pairs = {maxcodeg}  -> C4-free: {maxcodeg <= 1}")
        print(f"    triangles = {tri}")
        print(f"    e(G) = {m}, formula q*sum|T_r||T_s| = {m_formula}, "
              f"e/N^1.5 = {m / N**1.5:.6f}  (claim 3/20 = 0.15)")
        print(f"    all required-pair densities == 1/q exactly: {ok_dens}")
    return dict(N=N, Delta=Delta, maxcodeg=maxcodeg, tri=tri, m=m,
                m_formula=m_formula, ok_dens=ok_dens, T=T, cls=cls)

def canonical_search(q, twisted=True, verbose=True):
    """Exhaustive: for every (A,B,C) in V_a x V_b x V_c, close up D..J using the
    common-neighbour maps of the graph; count configurations where all 7 closures
    land in the right classes (Petersen minus ij), and among those how many also
    satisfy the ij edge equation (= canonical Petersen copies)."""
    idx = {r: k for k, r in enumerate(LAB)}
    T = {r: np.array([x for x in range(q) if x % 10 == idx[r]], dtype=np.int64) for r in LAB}
    inclass = {r: np.zeros(q, dtype=bool) for r in LAB}
    for r in LAB:
        inclass[r][T[r]] = True
    parents = [('d', 'a', 'b'), ('e', 'a', 'c'), ('f', 'b', 'c'),
               ('g', 'c', 'd'), ('h', 'b', 'e'), ('i', 'a', 'f'), ('j', 'g', 'h')]
    inv = np.array([0] + [pow(t, q - 2, q) for t in range(1, q)], dtype=np.int64)

    def closure(xu, yu, xv, yv, cu, cv):
        """common neighbour (z,t) of (xu,yu) [const cu] and (xv,yv) [const cv]:
           t + yu + xu z = cu ,  t + yv + xv z = cv
           => (xu-xv) z = (cu-cv) - (yu-yv) ; t = cu - yu - xu z."""
        d = (xu - xv) % q
        rhs = ((cu - cv) - (yu - yv)) % q
        bad = (d == 0)
        z = (rhs * inv[d % q]) % q
        t = (cu - yu - xu * z) % q
        return z, t, bad

    cst = lambda r, s: cconst(r, s, twisted)
    # seeds
    Xa, Xb, Xc = T['a'], T['b'], T['c']
    total_minus_ij = 0
    total_full = 0
    ij_values = defaultdict(int)
    ys = np.arange(q, dtype=np.int64)
    for xa in Xa:
        for ya in ys:
            for xb in Xb:
                for yb in ys:
                    # vectorise over C
                    XC = np.repeat(Xc, q)
                    YC = np.tile(ys, len(Xc))
                    P = {}
                    P['a'] = (np.full(XC.shape, xa), np.full(XC.shape, ya))
                    P['b'] = (np.full(XC.shape, xb), np.full(XC.shape, yb))
                    P['c'] = (XC, YC)
                    ok = np.ones(XC.shape, dtype=bool)
                    for (new, p1, p2) in parents:
                        x1, y1 = P[p1]; x2, y2 = P[p2]
                        z, t, bad = closure(x1, y1, x2, y2, cst(p1, new), cst(p2, new))
                        ok &= ~bad
                        ok &= inclass[new][z % q]
                        P[new] = (z, t)
                        if not ok.any():
                            break
                    if not ok.any():
                        continue
                    xi, yi = P['i']; xj, yj = P['j']
                    val = (yi + yj + xi * xj) % q
                    sel = ok
                    total_minus_ij += int(sel.sum())
                    for v in np.unique(val[sel]):
                        ij_values[int(v)] += int((val[sel] == v).sum())
                    total_full += int((sel & (val == cst('i', 'j'))).sum())
    if verbose:
        print(f"    seeds |V_a|*|V_b|*|V_c| = {(len(Xa)*q)*(len(Xb)*q)*(len(Xc)*q)}")
        print(f"    canonical 'Petersen minus ij' configurations = {total_minus_ij}")
        print(f"    distribution of <I,J> = y_I+y_J+x_I x_J over them: {dict(sorted(ij_values.items()))}")
        print(f"    canonical PETERSEN copies (needs <I,J> = {cst('i','j')}) = {total_full}")
    return total_minus_ij, total_full, dict(ij_values)

if __name__ == "__main__":
    qs = [int(a) for a in sys.argv[1:]] or [23, 31, 41]
    for q in qs:
        print(f"=== q = {q} (TWISTED, c_ij = 1) ===")
        checks(q, True)
        canonical_search(q, True)
        print(f"=== q = {q} (CONTROL: all c = 0, plain polarity model) ===")
        checks(q, False)
        canonical_search(q, False)
        print()
