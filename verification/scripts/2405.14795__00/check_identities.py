#!/usr/bin/env python3
"""Independent checks of the combinatorial identities used in the writeup for
2405.14795__00 (sharp threshold for rainbow stackings).

Pure-python (no external deps). Checks:

 A. Exact encoding: P(two fixed normalized stackings are both rainbow)
    == (# proper edge-colorings of the bipartite multigraph B) / r^{mN},
    by brute force for n=3, m=2 and m=3.
 B. e(L(B)) = 2N*C(m,2) - F2  and  t(L(B)) = 2N*C(m,3) - F3 (random instances).
 C. F2 = sum_{i<j} f(pi_i^{-1} pi_j)  (f = # unordered pairs fixed setwise).
 D. Chromatic polynomial coefficient: [q^{v-2}] P_G(q) = C(e,2) - t
    (random graphs on 7 vertices, exact interpolation).
 E. -log p_k(r) = C(k,2)/r + (C(k,2)/2 + C(k,3))/r^2 + O(r^-3), i.e.
    sum_{j<k} j^2/2 == C(k,2)/2 + C(k,3).
 F. h_k / C(k,2) nondecreasing in k (numeric, several r).
 G. Uniform spanning tree of K_m: each edge has probability 2/m (m=4,5).
 H. Factorial moments of #2-cycles: E(T)_j = 2^{-j} (n=8, full S_8).
 I. f(pi) = C(K,2) + T  (K = #fixed points, T = #2-cycles), full S_6.
 J. m=2 exact joint probability per component vs Lemma-2 error O(N/r^3).
"""
import itertools, math, random
from fractions import Fraction

random.seed(12345)

def pairs(n):
    return [frozenset(p) for p in itertools.combinations(range(n), 2)]

def act(perm, pair):
    a, b = tuple(pair)
    return frozenset((perm[a], perm[b]))

# ---------------------------------------------------------------- A
def check_A(n, m, r, trials=3):
    P = pairs(n)
    N = len(P)
    idx = {p: i for i, p in enumerate(P)}
    ok_all = True
    for t in range(trials):
        # normalized stackings sigma, tau (first coordinate = id)
        sigma = [tuple(range(n))] + [tuple(random.sample(range(n), n)) for _ in range(m - 1)]
        tau   = [tuple(range(n))] + [tuple(random.sample(range(n), n)) for _ in range(m - 1)]
        # joint rainbow count by brute force over all m-tuples of colorings
        cnt_joint = 0
        for chis in itertools.product(itertools.product(range(r), repeat=N), repeat=m):
            # chis[i][idx[g]] = color of edge g under chi_i
            ok = True
            for e in P:
                cols1 = set(); cols2 = set()
                for i in range(m):
                    inv_s = [0]*n; inv_t = [0]*n
                    for v in range(n):
                        inv_s[sigma[i][v]] = v
                        inv_t[tau[i][v]] = v
                    cols1.add(chis[i][idx[act(inv_s, e)]])
                    cols2.add(chis[i][idx[act(inv_t, e)]])
                if len(cols1) != m or len(cols2) != m:
                    ok = False; break
            if ok:
                cnt_joint += 1
        # bipartite multigraph B: edges (i, g) join left sigma_i(g), right tau_i(g)
        # proper edge-coloring count by brute force over colorings of B's mN edges
        Bedges = []
        for i in range(m):
            for g in P:
                Bedges.append((idx[act(sigma[i], g)], idx[act(tau[i], g)]))
        cnt_proper = 0
        for coloring in itertools.product(range(r), repeat=len(Bedges)):
            ok = True
            for L in range(N):
                seenl = set(); seenr = set()
                for eidx, (l, rr) in enumerate(Bedges):
                    if l == L:
                        if coloring[eidx] in seenl: ok = False; break
                        seenl.add(coloring[eidx])
                if not ok: break
            if ok:
                for R in range(N):
                    seenr = set()
                    for eidx, (l, rr) in enumerate(Bedges):
                        if rr == R:
                            if coloring[eidx] in seenr: ok = False; break
                            seenr.add(coloring[eidx])
                    if not ok: break
            if ok:
                cnt_proper += 1
        same = (cnt_joint == cnt_proper)
        ok_all &= same
        print(f"  A n={n} m={m} r={r} trial{t}: joint={cnt_joint} properB={cnt_proper} {'PASS' if same else 'FAIL'}")
    return ok_all

# ---------------------------------------------------------------- B, C
def build_B(n, m):
    P = pairs(n)
    N = len(P)
    perms = [tuple(range(n))] + [tuple(random.sample(range(n), n)) for _ in range(m - 1)]
    idx = {p: i for i, p in enumerate(P)}
    bundles = {}
    edges = []
    for i in range(m):
        for g in P:
            l, r_ = idx[g], idx[act(perms[i], g)]
            edges.append((i, l, r_))
            bundles[(l, r_)] = bundles.get((l, r_), 0) + 1
    return P, N, perms, edges, bundles, idx

def f_setwise(perm, P):
    return sum(1 for p in P if act(perm, p) == p)

def compose_inv(a, b):
    # a^{-1} b
    n = len(a)
    inv = [0]*n
    for v in range(n): inv[a[v]] = v
    return tuple(inv[b[v]] for v in range(n))

def check_BC(n, m, trials=4):
    ok_all = True
    for t in range(trials):
        P, N, perms, edges, bundles, idx = build_B(n, m)
        F2 = sum(math.comb(k, 2) for k in bundles.values())
        F3 = sum(math.comb(k, 3) for k in bundles.values())
        # line graph (simple): vertices = edges list; adjacency = share left or right
        ne = 0; tri = 0
        E = edges
        adj = [[False]*len(E) for _ in range(len(E))]
        for a in range(len(E)):
            for b in range(a+1, len(E)):
                if E[a][1] == E[b][1] or E[a][2] == E[b][2]:
                    adj[a][b] = adj[b][a] = True
                    ne += 1
        for a in range(len(E)):
            for b in range(a+1, len(E)):
                if not adj[a][b]: continue
                for c in range(b+1, len(E)):
                    if adj[a][c] and adj[b][c]:
                        tri += 1
        e_pred = 2*N*math.comb(m, 2) - F2
        t_pred = 2*N*math.comb(m, 3) - F3
        F_direct = sum(f_setwise(compose_inv(perms[i], perms[j]), P)
                       for i in range(m) for j in range(i+1, m))
        okB = (ne == e_pred and tri == t_pred)
        okC = (F2 == F_direct)
        ok_all &= okB and okC
        print(f"  B/C n={n} m={m} trial{t}: e={ne} (pred {e_pred}) t={tri} (pred {t_pred}) "
              f"F2={F2} sum_f={F_direct} {'PASS' if okB and okC else 'FAIL'}")
    return ok_all

# ---------------------------------------------------------------- D
def chrom_poly_coeffs(vlist, elist):
    v = len(vlist)
    # count proper colorings for q = 0..v, Lagrange-interpolate exact coefficients
    counts = []
    for q in range(v+1):
        c = 0
        for col in itertools.product(range(q), repeat=v):
            if all(col[a] != col[b] for (a, b) in elist):
                c += 1
        counts.append(Fraction(c))
    # interpolation (Newton)
    xs = [Fraction(q) for q in range(v+1)]
    coeffs = [Fraction(0)]*(v+1)
    # build polynomial via Lagrange, accumulate coefficients
    for i in range(v+1):
        # basis poly prod_{j!=i} (x - xj)/(xi - xj)
        num = [Fraction(1)]
        den = Fraction(1)
        for j in range(v+1):
            if j == i: continue
            num = polymul(num, [-xs[j], Fraction(1)])
            den *= (xs[i] - xs[j])
        for k in range(len(num)):
            coeffs[k] += counts[i]*num[k]/den
    return coeffs

def polymul(a, b):
    out = [Fraction(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def check_D(trials=4):
    ok_all = True
    v = 7
    for t in range(trials):
        elist = [e for e in itertools.combinations(range(v), 2) if random.random() < 0.45]
        e = len(elist)
        tri = sum(1 for (a, b, c) in itertools.combinations(range(v), 3)
                  if (a, b) in elist and (b, c) in elist and (a, c) in elist)
        coeffs = chrom_poly_coeffs(list(range(v)), elist)
        # P_G(q) = q^v - e q^{v-1} + (C(e,2)-t) q^{v-2} + ...
        c2 = coeffs[v-2]
        pred = Fraction(math.comb(e, 2) - tri)
        ok = (coeffs[v] == 1 and coeffs[v-1] == -e and c2 == pred)
        ok_all &= ok
        print(f"  D trial{t}: v=7 e={e} tri={tri} [q^5]={c2} pred={pred} "
              f"[q^6]={coeffs[v-1]} {'PASS' if ok else 'FAIL'}")
    return ok_all

# ---------------------------------------------------------------- E
def check_E():
    ok_all = True
    for k in range(2, 12):
        lhs = Fraction(sum(j*j for j in range(1, k)), 2)
        rhs = Fraction(math.comb(k, 2), 2) + math.comb(k, 3)
        ok = lhs == rhs
        ok_all &= ok
        print(f"  E k={k}: sum j^2/2={lhs} C(k,2)/2+C(k,3)={rhs} {'PASS' if ok else 'FAIL'}")
    # also (k-1)k(2k-1)/12 form used in Section 7 (m(m-1)(2m-1)/12)
    for m in range(2, 10):
        ok = Fraction((m-1)*m*(2*m-1), 12) == Fraction(math.comb(m, 2), 2) + math.comb(m, 3)
        ok_all &= ok
    print(f"  E closed form m(m-1)(2m-1)/12: {'PASS' if ok_all else 'FAIL'}")
    return ok_all

# ---------------------------------------------------------------- F
def check_F():
    ok_all = True
    for r in (10, 50, 1000):
        for m in (3, 5, 8):
            hs = []
            for k in range(2, m+1):
                h = -sum(math.log(1 - j/r) for j in range(1, k))
                hs.append(h/math.comb(k, 2))
            ok = all(hs[i] <= hs[i+1] + 1e-15 for i in range(len(hs)-1))
            ok_all &= ok
            print(f"  F r={r} m={m}: ratios h_k/C(k,2) = {[f'{x:.6g}' for x in hs]} {'PASS' if ok else 'FAIL'}")
    return ok_all

# ---------------------------------------------------------------- G
def check_G():
    ok_all = True
    for m in (4, 5):
        edges_all = list(itertools.combinations(range(m), 2))
        trees = []
        for es in itertools.combinations(edges_all, m-1):
            # spanning tree test: connected on m vertices with m-1 edges
            parent = list(range(m))
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]; x = parent[x]
                return x
            ok = True
            for (a, b) in es:
                ra, rb = find(a), find(b)
                if ra == rb: ok = False; break
                parent[ra] = rb
            if ok:
                trees.append(es)
        assert len(trees) == m**(m-2)
        for e0 in edges_all:
            freq = Fraction(sum(1 for tr in trees if e0 in tr), len(trees))
            ok = freq == Fraction(2, m)
            ok_all &= ok
        print(f"  G m={m}: #trees={len(trees)} each edge freq=2/{m} {'PASS' if ok_all else 'FAIL'}")
    return ok_all

# ---------------------------------------------------------------- H, I
def cycle_stats(perm):
    n = len(perm)
    seen = [False]*n
    K = T = 0
    for v in range(n):
        if seen[v]: continue
        l = 0; u = v
        while not seen[u]:
            seen[u] = True; u = perm[u]; l += 1
        if l == 1: K += 1
        if l == 2: T += 1
    return K, T

def check_H(n=8):
    perms = list(itertools.permutations(range(n)))
    ok_all = True
    for j in range(1, 5):
        s = Fraction(0)
        for p in perms:
            K, T = cycle_stats(p)
            fm = 1
            for i in range(j): fm *= (T - i)
            s += fm
        val = s / len(perms)
        ok = val == Fraction(1, 2**j)
        ok_all &= ok
        print(f"  H n={n} j={j}: E(T)_j = {val} (pred {Fraction(1,2**j)}) {'PASS' if ok else 'FAIL'}")
    return ok_all

def check_I(n=6):
    P = pairs(n)
    ok_all = True
    bad = 0
    for p in itertools.permutations(range(n)):
        K, T = cycle_stats(p)
        f = f_setwise(p, P)
        if f != math.comb(K, 2) + T:
            bad += 1; ok_all = False
    print(f"  I n={n}: f(pi)=C(K,2)+T for all {math.factorial(n)} perms, "
          f"violations={bad} {'PASS' if ok_all else 'FAIL'}")
    return ok_all

# ---------------------------------------------------------------- J
def check_J(n=8):
    # m=2: exact joint prob per component vs Lemma 2 formula p^{2N} W e^{O(N/r^3)}
    P = pairs(n); N = len(P)
    perm = tuple(random.sample(range(n), n))
    # orbits of induced action on pairs
    seen = set(); orbits = []
    for p in P:
        if p in seen: continue
        l = 0; u = p
        while u not in seen:
            seen.add(u); u = act(perm, u); l += 1
        orbits.append(l)
    fhat = sum(1 for l in orbits if l == 1)
    print(f"  J n={n} perm orbits on pairs: {sorted(orbits)}, fixed pairs={fhat}")
    ok_all = True
    prev = None
    for r in (50, 100, 200, 400, 800):
        logjoint = sum(math.log(((r-1)**(2*l) + (r-1))) - 2*l*math.log(r) for l in orbits)
        logp2N = 2*N*math.log((r-1)/r)
        logW = -fhat*math.log((r-1)/r)
        delta = logjoint - logp2N - logW
        scaled = delta * r**3 / N
        print(f"    r={r}: delta={delta:.3e}, delta*r^3/N={scaled:.4f}")
        if prev is not None:
            # delta should shrink roughly by 8x when r doubles
            ok_all &= abs(prev/delta) > 4 if delta != 0 else True
        prev = delta
    print(f"  J scaling consistent with O(N/r^3): {'PASS' if ok_all else 'FAIL'}")
    return ok_all

if __name__ == "__main__":
    results = {}
    print("Check A (exact B-encoding of joint rainbow probability):")
    results['A1'] = check_A(3, 2, 3, trials=2)
    results['A2'] = check_A(3, 3, 4, trials=1)
    print("Check B/C (line graph edge/triangle counts, F identity):")
    results['BC1'] = check_BC(7, 3)
    results['BC2'] = check_BC(6, 4)
    print("Check D (chromatic polynomial [q^{v-2}] coefficient):")
    results['D'] = check_D()
    print("Check E (second-order coefficient of -log p_k):")
    results['E'] = check_E()
    print("Check F (h_k/C(k,2) monotone):")
    results['F'] = check_F()
    print("Check G (uniform spanning tree edge prob 2/m):")
    results['G'] = check_G()
    print("Check H (factorial moments of #2-cycles):")
    results['H'] = check_H()
    print("Check I (f = C(K,2)+T):")
    results['I'] = check_I()
    print("Check J (m=2 exact vs Lemma 2, error O(N/r^3)):")
    results['J'] = check_J()
    print()
    print("SUMMARY:", {k: ('PASS' if v else 'FAIL') for k, v in results.items()})
    print("ALL PASS" if all(results.values()) else "SOME FAILED")
