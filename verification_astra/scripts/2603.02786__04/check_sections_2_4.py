"""
(A) Verify the regularization construction of Section 2 of the writeup:
    given r-uniform H with max degree Delta, build H' on V(H) x {0..r-1} x F_p
    (p prime > max(r,Delta)) with the copied edges plus, for each v, a set
    S_v subset F_p with |S_v| = Delta - deg_H(v), the edges
        {(v,i,b+i*s) : 0<=i<r},  s in S_v, b in F_p.
    Claims to check: H' is r-uniform, simple, EXACTLY Delta-regular,
    Delta_2(H') <= max(Delta_2(H),1), and H contains a copy of H'.

(B) Verify the greedy bound (17): M_s(n) <= (n^2+n-1)s, by actually running the
    greedy in an interval of that length, and also compute true M_s(n) by brute
    force for small s,n to compare with n*s.
"""
import random, itertools, sys
from collections import defaultdict
from sympy import nextprime

def regularize(H_edges, V, r, Delta):
    p = int(nextprime(max(r, Delta)))
    deg = defaultdict(int)
    for e in H_edges:
        for v in e:
            deg[v] += 1
    edges = []
    # copies of H
    for i in range(r):
        for b in range(p):
            for e in H_edges:
                edges.append(frozenset((v, i, b) for v in e))
    # added edges
    for v in V:
        need = Delta - deg[v]
        assert 0 <= need <= p, (need, p)
        S_v = list(range(need))          # any subset of F_p of that size
        for s in S_v:
            for b in range(p):
                edges.append(frozenset((v, i, (b + i*s) % p) for i in range(r)))
    return edges, p

def stats(edges):
    deg = defaultdict(int); codeg = defaultdict(int); uniform = set()
    seen = set(); dup = 0
    for e in edges:
        uniform.add(len(e))
        if e in seen: dup += 1
        seen.add(e)
        for v in e: deg[v] += 1
        for u, v in itertools.combinations(sorted(e, key=str), 2):
            codeg[(u, v)] += 1
    return deg, codeg, uniform, dup

def testA():
    random.seed(1)
    ok = True
    for trial in range(6):
        r = random.choice([2, 3, 4])
        nv = random.randint(5, 8)
        V = list(range(nv))
        allE = list(itertools.combinations(V, r))
        H = [frozenset(e) for e in random.sample(allE, min(len(allE), random.randint(2, 6)))]
        degH, codegH, _, _ = stats(H)
        Delta = max([degH[v] for v in V] + [0])
        if Delta == 0: continue
        D2H = max([c for c in codegH.values()] + [0])
        E2, p = regularize(H, V, r, Delta)
        deg2, codeg2, uni, dup = stats(E2)
        reg = set(deg2.values())
        D22 = max(codeg2.values())
        cond = (uni == {r}) and (reg == {Delta}) and (D22 <= max(D2H, 1)) and dup == 0
        print(f"trial {trial}: r={r} |V|={nv} |E|={len(H)} Delta={Delta} Delta2(H)={D2H} p={p} "
              f"-> uniform={uni} degrees={sorted(reg)} Delta2(H')={D22} dup_edges={dup} "
              f"{'OK' if cond else 'FAIL'}")
        ok = ok and cond
    print("Section 2 regularization:", "ALL OK" if ok else "FAILURE")
    return ok

def greedy_pack(n, ds, m):
    """greedy: place differences in the given order in [1..m]; return placement or None"""
    used = set(); place = {}
    for d in ds:
        L = m - (n-1)*d
        done = False
        for a in range(1, L+1):
            P = [a + j*d for j in range(n)]
            if all(x not in used for x in P):
                used.update(P); place[d] = a; done = True; break
        if not done: return None
    return place

def exact_M(n, k, cap=200):
    """smallest m admitting a packing of differences 1..k (exhaustive DFS)."""
    for m in range(n*k, cap+1):
        used = [False]*(m+2)
        order = sorted(range(1, k+1), key=lambda d: -(d))   # hardest first
        def dfs(i):
            if i == len(order): return True
            d = order[i]; L = m - (n-1)*d
            for a in range(1, L+1):
                P = [a + j*d for j in range(n)]
                if all(not used[x] for x in P):
                    for x in P: used[x] = True
                    if dfs(i+1): return True
                    for x in P: used[x] = False
            return False
        if dfs(0): return m
    return None

def testB():
    ok = True
    for n in range(2, 6):
        for s in range(1, 9):
            m = (n*n + n - 1)*s
            r = greedy_pack(n, list(range(1, s+1)), m)
            good = r is not None
            ok = ok and good
            if not good: print(f"(17) FAIL n={n} s={s} m={m}")
    print("Section 4 bound (17) M_s(n)<=(n^2+n-1)s, greedy in increasing order:", "ALL OK" if ok else "FAILURE")
    print()
    print("Exact M_k(n) (brute force) vs trivial lower bound nk:")
    for n in [2, 3, 4]:
        row = []
        for k in range(1, 9):
            v = exact_M(n, k, cap=6*n*k+10)
            row.append((k, v, n*k, None if v is None else v - n*k))
        print(f"  n={n}: " + "  ".join(f"k={k}: M={v} (nk={t}, excess={e})" for k, v, t, e in row))
    return ok

if __name__ == "__main__":
    a = testA(); print()
    b = testB()
    print()
    print("OVERALL:", "OK" if (a and b) else "SOME FAILURE")
