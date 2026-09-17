"""Exact verification of the 'odd polygon + central cluster' construction
claimed in attacks_retry/2507.10840__01/output.md.

All geometric predicates are decided with sympy exact algebraic arithmetic:
a high-precision numeric evaluation decides the sign when it is clearly
nonzero, and any value that is numerically tiny is settled by an exact
symbolic zero test.  Every triple of points is additionally submitted to an
exact collinearity (=0) test, so degeneracies cannot be missed.
"""
import sys, itertools, math
from fractions import Fraction
import sympy as sp

CACHE = {}

def sgn(expr):
    """Exact sign of a sympy expression (algebraic number)."""
    key = sp.srepr(expr)
    if key in CACHE:
        return CACHE[key]
    v = sp.N(expr, 60)
    if abs(v) > sp.Float("1e-40"):
        s = 1 if v > 0 else -1
    else:
        e = sp.simplify(sp.expand_trig(sp.expand(expr)))
        e = sp.nsimplify(e)
        if sp.simplify(e) == 0:
            s = 0
        else:
            v2 = sp.N(e, 200)
            if abs(v2) < sp.Float("1e-120"):
                raise RuntimeError("cannot decide sign of %s" % expr)
            s = 1 if v2 > 0 else -1
    CACHE[key] = s
    return s

def orient(P, a, b, c):
    ax, ay = P[a]; bx, by = P[b]; cx, cy = P[c]
    return sgn((bx-ax)*(cy-ay) - (by-ay)*(cx-ax))

def proper_cross(P, a, b, c, d):
    """segments ab and cd cross in their relative interiors"""
    if len({a,b,c,d}) < 4:
        return False
    o1 = orient(P,a,b,c); o2 = orient(P,a,b,d)
    o3 = orient(P,c,d,a); o4 = orient(P,c,d,b)
    return o1*o2 < 0 and o3*o4 < 0

def build(h, cluster):
    """polygon vertices 0..h-1 (exact), then cluster points (rational)."""
    P = []
    for j in range(h):
        ang = sp.Rational(2*j, h)*sp.pi
        P.append((sp.cos(ang), sp.sin(ang)))
    for (x, y) in cluster:
        P.append((sp.Rational(x), sp.Rational(y)))
    return P

def run(h, cluster, enumerate_paths=True, exact_cover=False, verbose=True):
    m = (h-1)//2
    r = len(cluster)
    P = build(h, cluster)
    n = len(P)
    tag = "h=%d (m=%d), r=%d, n=%d" % (h, m, r, n)
    print("="*70); print(tag); print("="*70)

    # ---- 1. general position: EXACT check that no 3 points are collinear
    bad = [t for t in itertools.combinations(range(n),3) if orient(P,*t)==0]
    print("[general position] collinear triples:", len(bad), "->",
          "OK" if not bad else "FAIL %s" % bad[:5])

    D = [(i, (i+m) % h) for i in range(h)]
    Dset = set(frozenset(e) for e in D)
    assert len(Dset) == h
    S = [(v, h+t) for v in range(h) for t in range(r)]
    Sset = set(frozenset(e) for e in S)
    assert len(Sset) == h*r
    assert not (Dset & Sset)

    # ---- 2. Property 1: vertex-disjoint edges of D cross
    ok, fails = True, []
    for e, f in itertools.combinations(D, 2):
        if set(e) & set(f):
            if proper_cross(P, e[0], e[1], f[0], f[1]):
                ok = False; fails.append(("adjacent pair crosses?!", e, f))
        else:
            if not proper_cross(P, e[0], e[1], f[0], f[1]):
                ok = False; fails.append(("disjoint pair does NOT cross", e, f))
    print("[Property 1] every vertex-disjoint pair in D crosses:",
          "OK" if ok else "FAIL %s" % fails[:5])

    # ---- 3. Property 2
    # 3a: each cluster point lies strictly inside every triangle T_i
    inside_ok = True
    for t in range(r):
        x = h+t
        for i in range(h):
            a = (i+m) % h; b = (i+m+1) % h
            s1 = orient(P, i, a, x); s2 = orient(P, a, b, x); s3 = orient(P, b, i, x)
            if not (s1 == s2 == s3 and s1 != 0):
                inside_ok = False
                print("   cluster pt", t, "not strictly inside T_%d" % i)
    print("[Property 2a] every cluster point strictly inside every T_i:",
          "OK" if inside_ok else "FAIL")
    # 3b: for x in cluster, z outside {v_i,a,b}: xz properly crosses v_i a or v_i b
    p2_ok = True; p2_fail = []
    for t in range(r):
        x = h+t
        for i in range(h):
            a = (i+m) % h; b = (i+m+1) % h
            for z in range(h):
                if z in (i, a, b): continue
                c1 = proper_cross(P, x, z, i, a)
                c2 = proper_cross(P, x, z, i, b)
                if not (c1 or c2):
                    p2_ok = False; p2_fail.append((t, i, z))
    print("[Property 2b] xz crosses v_i a or v_i b for all x,i,z:",
          "OK" if p2_ok else "FAIL %s" % p2_fail[:5])

    if not enumerate_paths:
        return

    # ---- 4. crossing matrix on all edges, then enumerate crossing-free paths
    edges = list(itertools.combinations(range(n), 2))
    eidx = {frozenset(e): k for k, e in enumerate(edges)}
    ne = len(edges)
    X = [[False]*ne for _ in range(ne)]
    for k1, k2 in itertools.combinations(range(ne), 2):
        a, b = edges[k1]; c, d = edges[k2]
        if proper_cross(P, a, b, c, d):
            X[k1][k2] = X[k2][k1] = True

    wD = 2*r-2
    def ew(e):
        fe = frozenset(e)
        if fe in Dset: return (wD, 1, 0)   # (weight, is_D, is_S)
        if fe in Sset: return (1, 0, 1)
        return (0, 0, 0)
    EW = [ew(e) for e in edges]

    best_ds = 0; best_w = 0; best_ds_path = None; best_w_path = None
    profile = {}
    npaths = 0
    maxlist = []
    # DFS over simple paths (each undirected path enumerated twice; fine)
    seq = []
    used_edges = []
    def dfs(last, visited, w, d, s):
        nonlocal best_ds, best_w, npaths, best_ds_path, best_w_path
        npaths += 1
        if d + s > best_ds:
            best_ds = d + s; best_ds_path = list(seq)
        if w > best_w:
            best_w = w; best_w_path = list(seq)
        if s > profile.get(d, -1): profile[d] = s
        for nxt in range(n):
            if visited >> nxt & 1: continue
            k = eidx[frozenset((last, nxt))]
            if any(X[k][k2] for k2 in used_edges): continue
            wt, isD, isS = EW[k]
            used_edges.append(k); seq.append(nxt)
            dfs(nxt, visited | (1 << nxt), w+wt, d+isD, s+isS)
            used_edges.pop(); seq.pop()
    for start in range(n):
        seq = [start]; used_edges = []
        dfs(start, 1 << start, 0, 0, 0)
    print("[paths] crossing-free simple paths enumerated (each twice, incl. trivial): %d" % npaths)
    print("[paths] max |E(P) cap (D u S)| over crossing-free paths = %d   (writeup claims <= 3 for r=1)" % best_ds)
    print("        witness vertex sequence:", best_ds_path)
    print("[paths] max weight (2r-2)d(P)+s(P) = %d   (writeup claims <= 4r-2 = %d)" % (best_w, 4*r-2))
    print("        witness vertex sequence:", best_w_path)
    tot_w = wD*h + h*r
    print("[profile] max s(P) for each value of d(P):",
          {d: profile[d] for d in sorted(profile)},
          " (writeup: d<=2 always; s<=2r=%d; and d=2 => s<=2)" % (2*r))
    print("[bound] total weight = (2r-2)h + hr = %d ; lower bound ceil(W/maxw) = %d ; n/2 = %.1f"
          % (tot_w, -(-tot_w // max(best_w,1)), n/2))
    print("[bound] writeup formula ceil((3r-2)h/(4r-2)) = %d" % (-(-( (3*r-2)*h ) // (4*r-2))))

    if exact_cover:
        exact_min_cover(P, n, edges, eidx, X)

def exact_min_cover(P, n, edges, eidx, X):
    """Exact minimum number of crossing-free paths covering all edges (ILP)."""
    import numpy as np
    from scipy.optimize import milp, LinearConstraint, Bounds
    ne = len(edges)
    # enumerate maximal-ish: collect all crossing-free path edge sets (as bitmask)
    masks = set()
    used_edges = []
    def dfs(last, visited, mask):
        if mask: masks.add(mask)
        for nxt in range(n):
            if visited >> nxt & 1: continue
            k = eidx[frozenset((last, nxt))]
            if any(X[k][k2] for k2 in used_edges): continue
            used_edges.append(k)
            dfs(nxt, visited | (1 << nxt), mask | (1 << k))
            used_edges.pop()
    for start in range(n):
        used_edges = []
        dfs(start, 1 << start, 0)
    # keep only maximal masks (subsets never help)
    ms = sorted(masks, key=lambda z: -bin(z).count("1"))
    keep = []
    for mm in ms:
        if not any((mm | k) == k for k in keep):
            keep.append(mm)
    A = np.zeros((ne, len(keep)))
    for j, mm in enumerate(keep):
        for k in range(ne):
            if mm >> k & 1: A[k, j] = 1
    res = milp(c=np.ones(len(keep)),
               constraints=LinearConstraint(A, lb=np.ones(ne), ub=np.full(ne, np.inf)),
               integrality=np.ones(len(keep)),
               bounds=Bounds(0, 1))
    print("[ILP] maximal crossing-free paths: %d ; EXACT pi(A) = %s  (trivial bound ceil(C(n,2)/(n-1)) = %d)"
          % (len(keep), round(res.fun) if res.success else "FAILED",
             -(-(n*(n-1)//2) // (n-1))))

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "h5r1"):
        run(5, [(0, 0)], exact_cover=True)
    if which in ("all", "h7r1"):
        run(7, [(0, 0)], exact_cover=True)
    if which in ("all", "h5r2"):
        run(5, [(Fraction(1,10), Fraction(1,17)), (Fraction(-1,13), Fraction(1,23))])
    if which in ("all", "h7r2"):
        run(7, [(Fraction(1,20), Fraction(1,31)), (Fraction(-1,27), Fraction(1,43))])
    if which == "h9r1":
        run(9, [(0, 0)])
    if which == "h9r3":
        run(9, [(Fraction(1,50), Fraction(1,71)), (Fraction(-1,61), Fraction(1,83)),
                (Fraction(1,97), Fraction(-1,59))])
    if which == "h11r1":
        run(11, [(0, 0)])
