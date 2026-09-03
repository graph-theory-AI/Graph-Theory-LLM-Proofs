#!/usr/bin/env python3
"""Exhaustive check of Lemma 1 (equality case for cross-intersecting families).

Claim: for r,s < n/2, cross-intersecting A subset of C([n],r), B subset of C([n],s)
with |A||B| = C(n-1,r-1)C(n-1,s-1) implies A,B are the full stars through a common
point.

Method: enumerate every family A (bitmask over C(n,r)).  For fixed A, the largest
compatible B is Bmax(A) = {B : B meets every member of A}.  An equality pair with
this A exists iff |A| divides the bound and bound/|A| <= |Bmax(A)|.  If such a pair
exists and is NOT forced to be (full r-star, full s-star through the same point),
Lemma 1 is refuted.  We flag every A admitting an equality pair and check it is a
full star with Bmax exactly the co-star and bound/|A| == |Bmax| (so B is forced).
"""
import itertools, math, sys

def check(n, r, s):
    R = list(itertools.combinations(range(n), r))
    S = list(itertools.combinations(range(n), s))
    bound = math.comb(n-1, r-1) * math.comb(n-1, s-1)
    # disj[bi] = bitmask over R of A-sets disjoint from S[bi]
    disj = []
    for B in S:
        m = 0
        Bset = set(B)
        for ai, A in enumerate(R):
            if Bset.isdisjoint(A):
                m |= 1 << ai
        disj.append(m)
    stars_r = []  # bitmask of full star through c, for each c
    for c in range(n):
        m = 0
        for ai, A in enumerate(R):
            if c in A:
                m |= 1 << ai
        stars_r.append(m)
    star_s_size = math.comb(n-1, s-1)
    nR = len(R)
    maxprod = 0
    bad = []
    n_equality_A = 0
    for Amask in range(1, 1 << nR):
        acount = bin(Amask).count('1')
        bmax = [bi for bi in range(len(S)) if disj[bi] & Amask == 0]
        m = len(bmax)
        if acount * m > maxprod:
            maxprod = acount * m
        if m == 0:
            continue
        if bound % acount == 0 and bound // acount <= m:
            # an equality pair (A, B) exists with |B| = bound//acount
            n_equality_A += 1
            ok = False
            if Amask in stars_r:
                c = stars_r.index(Amask)
                # B must be forced: bound//acount == m and Bmax == s-star at c
                want = set(bi for bi in range(len(S)) if c in S[bi])
                if bound // acount == m and set(bmax) == want and m == star_s_size:
                    ok = True
            if not ok:
                bad.append((Amask, acount, m))
    print(f"n={n} r={r} s={s}: bound={bound}, max |A|*|Bmax|={maxprod}, "
          f"A-masks admitting equality pair={n_equality_A}, violations={len(bad)}")
    if maxprod != bound:
        print("  *** MAX PRODUCT != BOUND ***")
    for Amask, ac, m in bad[:5]:
        print("  BAD A:", [R[i] for i in range(nR) if Amask >> i & 1], ac, m)
    return maxprod == bound and not bad

if __name__ == "__main__":
    allok = True
    cases = [(5,2,2), (6,2,2), (7,2,2), (5,1,2), (7,1,3), (7,2,3)]
    for (n, r, s) in cases:
        assert r < n/2 and s < n/2
        allok &= check(n, r, s)
    print("ALL OK" if allok else "FAILURES FOUND")
