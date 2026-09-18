"""
Brute-force test of inequality (3) of the writeup (the weighted perfect-matching
entropy bound), which is claimed EXACTLY (no error term):

    log Z <= (L/s) [ log Delta + int_0^1 log(u^{s-1} + eps) du ]

where
  K   : s-uniform hypergraph on L vertices with positive edge weights w
  Z   : sum over perfect matchings M of prod_{e in M} w(e)
  Delta: max over vertices v of sum_{e ni v} w(e)      (max weighted degree)
  eps : any number such that for EVERY perfect matching M and EVERY vertex v,
        sum_{e ni v, e bad rel. M} w(e) <= eps * Delta,
        where e is bad rel. M iff |e cap f| >= 2 for some f in M.
        (Note e in M is always bad, since |e cap e| = s >= 2.)
We compute the SMALLEST valid eps (max over M, v) and test the inequality.
"""
import itertools, math, random

def perfect_matchings(L, edges):
    """edges: list of frozensets of size s covering vertices 0..L-1."""
    full = frozenset(range(L))
    res = []
    def rec(remaining, chosen):
        if not remaining:
            res.append(tuple(chosen)); return
        v = min(remaining)
        for e in edges:
            if v in e and e <= remaining:
                rec(remaining - e, chosen + [e])
    rec(full, [])
    return res

def integral_log(s, eps, npts=400001):
    """int_0^1 log(u^{s-1}+eps) du by Simpson."""
    n = npts if npts % 2 == 1 else npts + 1
    h = 1.0 / (n - 1)
    tot = 0.0
    for i in range(n):
        u = i * h
        val = math.log(u**(s-1) + eps)
        wgt = 1 if i in (0, n-1) else (4 if i % 2 == 1 else 2)
        tot += wgt * val
    return tot * h / 3

def test(L, s, edges, w, name):
    PMs = perfect_matchings(L, edges)
    if not PMs:
        return None
    Z = sum(math_prod(w[e] for e in M) for M in PMs)
    Delta = max(sum(w[e] for e in edges if v in e) for v in range(L))
    eps = 0.0
    for M in PMs:
        Ms = list(M)
        for v in range(L):
            bad = 0.0
            for e in edges:
                if v not in e: continue
                if any(len(e & f) >= 2 for f in Ms):
                    bad += w[e]
            eps = max(eps, bad / Delta)
    rhs = (L / s) * (math.log(Delta) + integral_log(s, eps))
    lhs = math.log(Z)
    ok = lhs <= rhs + 1e-9
    print(f"{name:34s} L={L:3d} s={s} |E|={len(edges):4d} #PM={len(PMs):7d} "
          f"Delta={Delta:9.4f} eps={eps:8.5f} logZ={lhs:10.5f} bound={rhs:10.5f} "
          f"slack={rhs-lhs:9.5f} {'OK' if ok else '*** VIOLATED ***'}")
    return ok

def math_prod(it):
    p = 1.0
    for x in it: p *= x
    return p

if __name__ == "__main__":
    random.seed(20260917)
    allok = True

    # ---- structured unweighted cases ----
    # K_{D,D} (s=2): Z = D!
    for D in range(2, 7):
        L = 2*D
        edges = [frozenset((i, D+j)) for i in range(D) for j in range(D)]
        w = {e: 1.0 for e in edges}
        allok &= bool(test(L, 2, edges, w, f"K_{D},{D}"))
    # K_{2k} complete graph
    for k in range(2, 5):
        L = 2*k
        edges = [frozenset(p) for p in itertools.combinations(range(L), 2)]
        w = {e: 1.0 for e in edges}
        allok &= bool(test(L, 2, edges, w, f"K_{L}"))
    # AG(2,3): Steiner triple system on 9 points, 12 lines, D=4, linear
    pts = [(i, j) for i in range(3) for j in range(3)]
    idx = {p: i for i, p in enumerate(pts)}
    lines = set()
    for a in pts:
        for b in pts:
            if a == b: continue
            c = ((2*b[0]-a[0]) % 3, (2*b[1]-a[1]) % 3)
            lines.add(frozenset((idx[a], idx[b], idx[c])))
    lines = [l for l in lines if len(l) == 3]
    w = {e: 1.0 for e in lines}
    allok &= bool(test(9, 3, lines, w, "AG(2,3) Steiner triple system"))
    # complete 3-uniform on 6 and 9 points (NOT linear -> large eps)
    for L in (6, 9):
        edges = [frozenset(t) for t in itertools.combinations(range(L), 3)]
        w = {e: 1.0 for e in edges}
        allok &= bool(test(L, 3, edges, w, f"complete 3-uniform K_{L}^(3)"))
    # complete 4-uniform on 8
    edges = [frozenset(t) for t in itertools.combinations(range(8), 4)]
    allok &= bool(test(8, 4, edges, {e: 1.0 for e in edges}, "complete 4-uniform K_8^(4)"))

    # ---- random weighted cases (the regime the writeup actually uses:
    #      very unequal weights, non-linear, mixed) ----
    trials = 0
    for s, L in [(2, 8), (2, 10), (3, 9), (3, 12), (4, 8), (4, 12), (5, 10)]:
        for t in range(12):
            allE = [frozenset(c) for c in itertools.combinations(range(L), s)]
            keep = [e for e in allE if random.random() < 0.55]
            if not keep: continue
            # heavy-tailed weights, spanning several orders of magnitude
            w = {e: math.exp(random.uniform(-6, 2)) for e in keep}
            r = test(L, s, keep, w, f"random s={s} L={L} #{t}")
            if r is not None:
                trials += 1
                allok &= r
    print()
    print(f"random instances with >=1 perfect matching: {trials}")
    print("ALL INSTANCES SATISFY (3)" if allok else "SOME INSTANCE VIOLATES (3)")
