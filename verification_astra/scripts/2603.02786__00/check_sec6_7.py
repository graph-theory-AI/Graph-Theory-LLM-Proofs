"""Checks for Corollary 2.2, Lemma 6.1 (folding), Lemma 6.2 (large-prime greedy)
and the Section 7 covering claim."""
import math, random
from sympy import primerange, primefactors

# ---------- Corollary 2.2 : pack a bundle B_q(n) ----------
def colour(N):
    root = math.isqrt(N)
    divs = [[] for _ in range(N+1)]
    for d in range(1, N+1):
        for m in range(d, N+1, d): divs[m].append(d)
    col = {a: a-1 for a in range(1, root+1)}
    big = list(range(root+1, N+1)); adj = {a: set() for a in big}
    for a in big:
        for k in range(1, N//a+1):
            for b in divs[k*a]:
                if b > root and b != a and (a*b)//math.gcd(a,b) <= N: adj[a].add(b)
    for a in sorted(big, key=lambda t: -len(adj[t])):
        used = {col[b] for b in adj[a] if b in col}
        c = root
        while c in used: c += 1
        col[a] = c
    return col

def test_cor22(n, q):
    N = n//q; col = colour(N); cols = sorted(set(col.values())); R = len(cols)
    batches = math.ceil(R/q); occ = {}
    for bi in range(batches):
        base = bi*(n+q)
        for ci, c in enumerate(cols[bi*q:(bi+1)*q]):
            r = ci
            for a in range(1, N+1):
                if col[a] != c: continue
                d = q*a
                for m in range(d, n+1, d):
                    z = base + m + r
                    assert z not in occ, f"collision {z}"
                    occ[z] = (a, c)
    span = max(occ)-min(occ)+1
    bound = (n+q)*math.ceil(R/q)
    print(f"Cor 2.2: n={n} q={q} N={N} R(N)={R} batches={batches} span={span} <= bound={bound}: {span<=bound}")

# ---------- Lemma 6.1 : folding ----------
def test_fold(trials=200):
    rnd = random.Random(2)
    for _ in range(trials):
        Nd = rnd.randint(5, 40); a = rnd.randint(2, 9); M = rnd.randint(Nd+1, 120)
        # random packed family inside [0,M-1], diameters <= Nd
        sets = []; used = set()
        for _ in range(rnd.randint(2, 8)):
            for _try in range(200):
                s = sorted(rnd.sample(range(0, M), rnd.randint(1, 4)))
                if s[-1]-s[0] <= Nd and not (set(s) & used):
                    used |= set(s); sets.append(set(s)); break
        H = math.ceil(M/a); out = []
        for B in sets:
            j = min(B)//H
            out.append({a*(b-j*H)+j for b in B})
        for i in range(len(out)):
            for j in range(i+1, len(out)):
                assert not (out[i] & out[j]), "folding collision"
        lo = min(min(s) for s in out); hi = max(max(s) for s in out)
        assert hi-lo+1 <= M + a*Nd + a, (hi-lo+1, M+a*Nd+a)
    print(f"Lemma 6.1: {trials} random folding instances: disjointness + length bound OK")

# ---------- Lemma 6.2 : greedy for large prime differences ----------
def test_lem62(N, P):
    assert P >= 2*math.isqrt(N)
    total = 0; Q = P
    while Q <= N:
        prs = [p for p in primerange(Q+1, min(2*Q, N)+1)]
        K = (Q*Q)//(2*N)
        assert K >= Q*Q/(4*N) - 1e-9, "(6.4) fails"
        for gstart in range(0, len(prs), max(K,1)):
            grp = prs[gstart:gstart+max(K,1)]
            occ = set()
            for p in grp:
                placed = False
                for r in range(p):
                    S = set(range(r+p, N+1, p))
                    if S and max(S) <= 2*N and not (S & occ):
                        occ |= S; placed = True; break
                assert placed, f"no free residue for p={p} in bin ({Q},{2*Q}]"
            total += 2*N
        Q *= 2
    bound_ok = total
    print(f"Lemma 6.2: N={N} P={P}: greedy always found a free residue; total length used={total}")

if __name__ == "__main__":
    test_cor22(20000, 37)
    test_cor22(20000, 211)
    test_fold()
    test_lem62(5000, 200)
    test_lem62(20000, 400)
    # ---------- Section 7 cover ----------
    for n in [10**4, 10**5, 10**6]:
        x = math.isqrt(n); Y = math.ceil(n**0.2); eps, C = 0.3, 3.0
        miss = []
        for d in range(1, n+1):
            pf = primefactors(d)
            if any(eps*x <= p <= C*x for p in pf): continue           # type 1
            if any(Y <= p < eps*x for p in pf): continue              # type 2 (prime q)
            s = d
            big = [p for p in pf if p > C*x]
            assert len(big) <= 1
            for p in big: s //= p**1
            if s >= Y:                                                # type 2 (q in [Y,Y^2])
                q = 1
                for p in sorted(primefactors(s)):
                    e = 0; t = s
                    while t % p == 0: t //= p; e += 1
                    for _ in range(e):
                        q *= p
                        if q >= Y: break
                    if q >= Y: break
                if Y <= q <= Y*Y and d % q == 0: continue
                miss.append(('q-fail', d, q)); continue
            if d < Y: continue                                        # type 3
            if big and s < Y: continue                                # type 4
            miss.append(('uncovered', d))
        print(f"Section 7 cover: n={n} Y={Y} uncovered indices: {len(miss)} {miss[:5]}")
