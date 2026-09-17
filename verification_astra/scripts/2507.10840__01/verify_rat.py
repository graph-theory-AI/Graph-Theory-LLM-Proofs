"""INDEPENDENT re-verification of attacks_retry/2507.10840__01/output.md.

Deliberately implemented differently from verify.py:
  * the polygon vertices are RATIONAL approximations of the regular h-gon
    (denominator N), so every geometric predicate is an exact Fraction
    determinant -- no algebraic-number sign heuristics anywhere;
  * all of Property 1 / Property 2 are open conditions, so a rational
    perturbation that passes the tests is itself a legitimate witness point
    set (this strengthens the claim: rational coordinates suffice);
  * an independent set-cover solver (own branch and bound + greedy/LP upper
    bounds), not scipy's milp, computes the exact pi(A).
"""
import sys, itertools, math, random
from fractions import Fraction as F

# ---------------------------------------------------------------- geometry
def orient(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

def sgn(x): return (x > 0) - (x < 0)

def proper_cross(P, a, b, c, d):
    if len({a,b,c,d}) < 4: return False
    o1 = sgn(orient(P[a],P[b],P[c])); o2 = sgn(orient(P[a],P[b],P[d]))
    o3 = sgn(orient(P[c],P[d],P[a])); o4 = sgn(orient(P[c],P[d],P[b]))
    return o1*o2 < 0 and o3*o4 < 0

def build(h, r, N=10**7, seed=0):
    """rational near-regular h-gon + r rational cluster points near origin."""
    rng = random.Random(seed)
    P = []
    for j in range(h):
        ang = 2*math.pi*j/h
        P.append((F(round(N*math.cos(ang)), N), F(round(N*math.sin(ang)), N)))
    # cluster: inside the disc of radius sin(pi/(2h)) about the origin,
    # which is contained in every T_i (distance from origin to a long chord).
    rad = math.sin(math.pi/(2*h)) * 0.5
    M = 10**9
    for t in range(r):
        while True:
            x = F(rng.randrange(-int(rad*M), int(rad*M)+1), M)
            y = F(rng.randrange(-int(rad*M), int(rad*M)+1), M)
            if x*x + y*y < F(int(rad*M)**2, M*M) and (x, y) not in P:
                P.append((x, y)); break
    return P

# ---------------------------------------------------------------- checks
def checks(h, r, P, verbose=True):
    m = (h-1)//2
    n = h + r
    ok = True
    bad = [t for t in itertools.combinations(range(n),3) if orient(P[t[0]],P[t[1]],P[t[2]]) == 0]
    ok &= not bad
    print("[gen.pos] collinear triples: %d %s" % (len(bad), "OK" if not bad else "FAIL"))
    # convex position of the polygon part, in cyclic order
    conv = all(orient(P[i], P[(i+1)%h], P[(i+2)%h]) > 0 for i in range(h))
    ok &= conv
    print("[convex ] polygon vertices in convex position, ccw order:", "OK" if conv else "FAIL")

    D = [(i, (i+m) % h) for i in range(h)]
    S = [(v, h+t) for v in range(h) for t in range(r)]
    Dset = {frozenset(e) for e in D}; Sset = {frozenset(e) for e in S}
    assert len(Dset) == h and len(Sset) == h*r and not (Dset & Sset)

    f1 = [(e,f) for e,f in itertools.combinations(D,2)
          if (not set(e)&set(f)) != proper_cross(P,e[0],e[1],f[0],f[1])]
    ok &= not f1
    print("[Prop 1 ] D-edges: disjoint <=> cross :", "OK" if not f1 else "FAIL %s" % f1[:3])

    f2a = []
    for t in range(r):
        x = h+t
        for i in range(h):
            a,b = (i+m)%h, (i+m+1)%h
            s = [sgn(orient(P[i],P[a],P[x])), sgn(orient(P[a],P[b],P[x])), sgn(orient(P[b],P[i],P[x]))]
            if not (s[0]==s[1]==s[2] and s[0]!=0): f2a.append((t,i))
    ok &= not f2a
    print("[Prop 2a] cluster pts strictly inside every T_i:", "OK" if not f2a else "FAIL %s" % f2a[:3])

    f2b = []
    for t in range(r):
        x = h+t
        for i in range(h):
            a,b = (i+m)%h, (i+m+1)%h
            for z in range(h):
                if z in (i,a,b): continue
                if not (proper_cross(P,x,z,i,a) or proper_cross(P,x,z,i,b)):
                    f2b.append((t,i,z))
    ok &= not f2b
    print("[Prop 2b] x z crosses v_i a or v_i b:", "OK" if not f2b else "FAIL %s" % f2b[:3])
    return ok, Dset, Sset

# ------------------------------------------------- crossing-free path search
def crossmatrix(P, n):
    edges = list(itertools.combinations(range(n),2))
    eidx = {frozenset(e):k for k,e in enumerate(edges)}
    ne = len(edges)
    X = [0]*ne                      # bitmask of edges crossing edge k
    for k1,k2 in itertools.combinations(range(ne),2):
        a,b = edges[k1]; c,d = edges[k2]
        if proper_cross(P,a,b,c,d):
            X[k1] |= 1<<k2; X[k2] |= 1<<k1
    return edges, eidx, X

def path_stats(P, n, Dset, Sset, edges, eidx, X, collect_masks=False):
    """DFS over all crossing-free simple paths. Returns (profile, maxDS, maxw, masks)."""
    isD = [1 if frozenset(e) in Dset else 0 for e in edges]
    isS = [1 if frozenset(e) in Sset else 0 for e in edges]
    profile = {}          # d -> max s
    maxDS = [0, None]
    masks = set()
    seq = []
    def dfs(last, visited, blocked, mask, d, s):
        if collect_masks and mask: masks.add(mask)
        if s > profile.get(d,-1): profile[d] = s
        if d+s > maxDS[0]: maxDS[0] = d+s; maxDS[1] = list(seq)
        for nxt in range(n):
            if visited>>nxt & 1: continue
            k = eidx[frozenset((last,nxt))]
            if blocked>>k & 1: continue
            seq.append(nxt)
            dfs(nxt, visited|(1<<nxt), blocked|X[k], mask|(1<<k), d+isD[k], s+isS[k])
            seq.pop()
    for st in range(n):
        seq=[st]; dfs(st, 1<<st, 0, 0, 0, 0)
    return profile, maxDS, masks

# ------------------------------------------------- exact minimum path cover
def min_cover(masks, ne, ub_hint=None):
    """Exact minimum number of masks whose union is all ne edges (own B&B)."""
    full = (1<<ne) - 1
    ms = sorted(masks, key=lambda z: -bin(z).count("1"))
    maximal = []
    for mm in ms:
        if not any((mm | k) == k for k in maximal): maximal.append(mm)
    maximal.sort(key=lambda z: -bin(z).count("1"))
    # greedy upper bound
    cov, ub = 0, 0
    while cov != full:
        best = max(maximal, key=lambda mm: bin(mm & ~cov).count("1"))
        cov |= best; ub += 1
    best = [ub]
    # cover-by-hardest-edge branch and bound
    cnt = [0]*ne
    for mm in maximal:
        for k in range(ne):
            if mm>>k & 1: cnt[k]+=1
    order = sorted(range(ne), key=lambda k: cnt[k])
    cands = {k: [mm for mm in maximal if mm>>k & 1] for k in range(ne)}
    maxsize = max(bin(mm).count("1") for mm in maximal)
    def bb(cov, used):
        if cov == full:
            if used < best[0]: best[0] = used
            return
        rem = bin(full & ~cov).count("1")
        if used + -(-rem//maxsize) >= best[0]: return
        k = next(k for k in order if not (cov>>k & 1))
        for mm in cands[k]:
            bb(cov|mm, used+1)
    bb(0, 0)
    return best[0], len(maximal), ub

def run(h, r, do_cover=False, N=10**7, seed=0, props_only=False):
    n = h+r
    print("="*70); print("h=%d (m=%d) r=%d n=%d  [rational coords, denom %d]" % (h,(h-1)//2,r,n,N)); print("="*70)
    P = build(h, r, N=N, seed=seed)
    ok, Dset, Sset = checks(h, r, P)
    if props_only:
        print("[props  ] structural checks only (path enumeration skipped)")
        return ok
    edges, eidx, X = crossmatrix(P, n)
    profile, maxDS, masks = path_stats(P,n,Dset,Sset,edges,eidx,X,collect_masks=do_cover)
    wD = 2*r-2
    maxw = max(wD*d + s for d,s in profile.items())
    print("[paths  ] max d(P) = %d (claim <=2); profile d -> max s: %s" % (max(profile), {d:profile[d] for d in sorted(profile)}))
    print("          claims: s<=2r=%d for all d; d=2 => s<=2" % (2*r))
    print("          => s<=2r holds: %s ; d=2 => s<=2 holds: %s"
          % (all(s<=2*r for s in profile.values()), profile.get(2,0)<=2))
    print("[paths  ] max |E(P) cap (D u S)| = %d  (r=1 claim: <=3) witness %s" % (maxDS[0], maxDS[1]))
    print("[weights] max (2r-2)d+s over plane paths = %d ; writeup bound 4r-2 = %d -> %s"
          % (maxw, 4*r-2, "OK" if maxw <= 4*r-2 else "VIOLATED"))
    W = wD*h + h*r
    print("[bound  ] total weight %d ; ceil(W/maxw)=%d ; writeup ceil((3r-2)h/(4r-2))=%d ; n/2=%.1f ; 2n/3=%.2f"
          % (W, -(-W//max(maxw,1)), -(-((3*r-2)*h)//(4*r-2)), n/2, 2*n/3))
    if r == 1:
        print("[bound  ] section-2 bound ceil(2h/3) = %d" % (-(-2*h//3)))
    if do_cover:
        val, nmax, ub = min_cover(masks, len(edges))
        print("[COVER  ] EXACT pi(A) = %d   (maximal plane paths %d, greedy UB %d, trivial LB %d, n/2=%.1f)"
              % (val, nmax, ub, -(-(n*(n-1)//2)//(n-1)), n/2))
    return ok

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        h, r, c = arg.split(",")
        run(int(h), int(r), do_cover=(c=="1"), props_only=(c=="p"))
