#!/usr/bin/env python3
"""Remaining checks for 1907.06019__01:

1. Section 4 sign identity: the coefficient of the e-containing component of
   (e^x + A(x)) ^ (e^y + B(y)) equals e ^ (x^B(y) + (-1)^{p+1} A(x)^y),
   i.e. annihilation forces A(x)^y = (-1)^p x^B(y)   [eq. (10) vs (5)].
   Checked symbolically-by-monomials for random integer A, B, x, y.

2. Converse: U = v^Wedge^{r-1}V and W = v^Wedge^{s-1}V are mutually
   annihilating with dims C(n-1,r-1), C(n-1,s-1) (random v, small n).

3. Connectivity of the bipartite disjointness graph between C([N],p') and
   C([N],q') when p'+q' <= N-1 (used when undoing compressions), and of the
   Johnson graph of p-subsets of an (m-1)-set (used in Lemma 3).

4. The r=1 numeric inequality: for n > 2s and 2 <= a <= s,
   prod_{j=1}^{a-1} (n-a+j)/(s-a+j) > 2^{a-1} >= a.
"""
import itertools, math
from fractions import Fraction
import random

random.seed(12345)

# ---------- exterior algebra over Q with dict {tuple(sorted): coeff} ----------
def inversions(A, B):
    return sum(1 for a in A for b in B if a > b)

def wedge(u, w):
    out = {}
    for K, cK in u.items():
        for L, cL in w.items():
            if set(K) & set(L):
                continue
            sg = (-1) ** inversions(K, L)
            T = tuple(sorted(K + L))
            out[T] = out.get(T, 0) + sg * cK * cL
    return {k: v for k, v in out.items() if v != 0}

def add(u, w, c=1):
    out = dict(u)
    for k, v in w.items():
        out[k] = out.get(k, 0) + c * v
        if out[k] == 0:
            del out[k]
    return out

def rand_form(ground, k, coef=5):
    return {I: random.randint(-coef, coef) for I in itertools.combinations(ground, k)}

# ---------- 1. sign identity ----------
def check_sign_identity(n, r, s, trials=20):
    # e = index 0; H = indices 1..n-1
    p, q = r - 1, s - 1
    H = tuple(range(1, n))
    ok = True
    for _ in range(trials):
        x = rand_form(H, p); y = rand_form(H, q)
        Ax = rand_form(H, p + 1); By = rand_form(H, q + 1)  # arbitrary values of A(x), B(y)
        e = {(0,): 1}
        u = add(wedge(e, x), Ax)
        w = add(wedge(e, y), By)
        prod = wedge(u, w)
        e_part = {K: v for K, v in prod.items() if 0 in K}
        claimed = wedge(e, add(wedge(x, By), wedge(Ax, y), c=(-1) ** (p + 1)))
        if e_part != claimed:
            ok = False
    print(f"sign identity n={n} r={r} s={s}: {'OK' if ok else 'FAIL'}")
    return ok

# ---------- 2. converse ----------
def check_converse(n, r, s):
    V = tuple(range(n))
    v = {(i,): random.randint(1, 9) for i in V}
    # basis of v ^ Wedge^{r-1} V : v ^ e_I over (r-1)-subsets; compute rank
    def star_vectors(k):
        vecs = []
        mons = list(itertools.combinations(V, k))
        idx = {m: i for i, m in enumerate(mons)}
        for I in itertools.combinations(V, k - 1):
            w = wedge(v, {I: 1})
            row = [Fraction(0)] * len(mons)
            for K, c in w.items():
                row[idx[K]] = Fraction(c)
            vecs.append(row)
        return vecs
    def rank(rows):
        rows = [r[:] for r in rows]; rk = 0; col = 0; ncol = len(rows[0])
        for col in range(ncol):
            piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
            if piv is None:
                continue
            rows[rk], rows[piv] = rows[piv], rows[rk]
            pr = rows[rk]
            for i in range(len(rows)):
                if i != rk and rows[i][col] != 0:
                    f = rows[i][col] / pr[col]
                    rows[i] = [a - f * b for a, b in zip(rows[i], pr)]
            rk += 1
        return rk
    dU, dW = rank(star_vectors(r)), rank(star_vectors(s))
    # annihilation: (v^z)^(v^z') = 0 for all basis z, z'
    ann = True
    for I in itertools.combinations(V, r - 1):
        for J in itertools.combinations(V, s - 1):
            if wedge(wedge(v, {I: 1}), wedge(v, {J: 1})):
                ann = False
    expU, expW = math.comb(n-1, r-1), math.comb(n-1, s-1)
    ok = (dU == expU and dW == expW and ann)
    print(f"converse n={n} r={r} s={s}: dimU={dU} (exp {expU}), dimW={dW} (exp {expW}), annihilating={ann} -> {'OK' if ok else 'FAIL'}")
    return ok

# ---------- 3. connectivity ----------
def bip_connected(N, pp, qq):
    left = list(itertools.combinations(range(N), pp))
    right = list(itertools.combinations(range(N), qq))
    if not left or not right:
        return True
    seen = {('L', left[0])}
    stack = [('L', left[0])]
    while stack:
        side, X = stack.pop()
        others = right if side == 'L' else left
        oside = 'R' if side == 'L' else 'L'
        for Y in others:
            if set(X).isdisjoint(Y) and (oside, Y) not in seen:
                seen.add((oside, Y)); stack.append((oside, Y))
    return len(seen) == len(left) + len(right)

def johnson_connected(M, p):
    verts = list(itertools.combinations(range(M), p))
    if len(verts) <= 1:
        return True
    seen = {verts[0]}; stack = [verts[0]]
    while stack:
        X = stack.pop()
        for Y in verts:
            if len(set(X) & set(Y)) == p - 1 and Y not in seen:
                seen.add(Y); stack.append(Y)
    return len(seen) == len(verts)

def check_connectivity():
    ok = True
    for N in range(2, 11):
        for pp in range(1, N):
            for qq in range(1, N - pp):   # pp+qq <= N-1
                if not bip_connected(N, pp, qq):
                    print(f"  bipartite disjointness graph DISCONNECTED: N={N} p'={pp} q'={qq}")
                    ok = False
    for M in range(2, 10):
        for p in range(1, M):
            if not johnson_connected(M, p) and p <= M - 1:
                # note: p == M gives single vertex; p<=M-1 needed
                print(f"  Johnson graph DISCONNECTED: M={M} p={p}")
                ok = False
    print(f"connectivity checks: {'OK' if ok else 'FAIL'}")
    return ok

# ---------- 4. r=1 inequality ----------
def check_r1():
    ok = True
    for s in range(2, 21):
        for n in range(2 * s + 1, 2 * s + 30):
            for a in range(2, s + 1):
                ratio = Fraction(math.comb(n - 1, s - 1), math.comb(n - a, s - a))
                if not (ratio > 2 ** (a - 1) >= a):
                    print(f"  r=1 inequality FAILS at n={n} s={s} a={a}: ratio={ratio}")
                    ok = False
    print(f"r=1 inequality (ratio > 2^(a-1) >= a) for s<=20, n<=2s+29: {'OK' if ok else 'FAIL'}")
    return ok

if __name__ == "__main__":
    ok = True
    for (n, r, s) in [(6,2,2), (7,2,3), (8,3,3), (7,1,2)]:
        ok &= check_sign_identity(n, r, s)
    for (n, r, s) in [(5,2,2), (6,2,2), (7,2,3), (7,3,3)]:
        ok &= check_converse(n, r, s)
    ok &= check_connectivity()
    ok &= check_r1()
    print("ALL OK" if ok else "FAILURES FOUND")
