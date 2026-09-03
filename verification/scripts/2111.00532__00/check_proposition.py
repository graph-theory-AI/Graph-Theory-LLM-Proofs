#!/usr/bin/env python3
"""
Verification script for attack 2111.00532__00.

The writeup claims (Proposition): for any blockade (B1,B2,B3) of width W with no
transversal triangle, some two distinct blocks contain an anticomplete pair X,Y
with |X| = |Y| = floor(sqrt(W)).

Only edges BETWEEN distinct blocks matter (a transversal triangle uses one
inter-block edge per pair of blocks; an anticomplete pair between two blocks
depends only on the bipartite graph between them), so we model an instance as
three bipartite graphs E12, E13, E23.

Checks performed:
  1. Exhaustive: |B1|=|B2|=|B3|=2 (W=2, m=1): all 2^12 = 4096 edge patterns.
     For every pattern with no transversal triangle, verify an anticomplete
     singleton pair exists between some two blocks.
  2. Exhaustive: blocks of size 3 restricted... too large exhaustively (2^27),
     so: full exhaustive n=2, and randomized for n in {4,...,60}: sample random
     instances, discard those with a transversal triangle (or delete a vertex
     from triangles until none remain, keeping width >= floor stated), then
     (a) run the writeup's constructive procedure and confirm it returns an
         anticomplete pair of size m = floor(sqrt(W)) between two blocks,
     (b) independently verify that pair is anticomplete.
  3. Adversarial randomized search for a counterexample to the Proposition for
     small n (n<=5) by exact max-anticomplete-pair computation (brute force over
     subsets) on triangle-transversal-free random instances.
"""

import itertools, math, random

random.seed(12345)


def has_transversal_triangle(n1, n2, n3, E12, E13, E23):
    # E12: set of (a,b) a in B1, b in B2, etc.
    for a in range(n1):
        for b in range(n2):
            if (a, b) not in E12:
                continue
            for c in range(n3):
                if (a, c) in E13 and (b, c) in E23:
                    return True
    return False


def anticomplete_singleton_exists(n1, n2, n3, E12, E13, E23):
    # m=1 case: some non-edge between some pair of distinct blocks
    return (len(E12) < n1 * n2) or (len(E13) < n1 * n3) or (len(E23) < n2 * n3)


def exhaustive_n2():
    n = 2
    slots12 = [(a, b) for a in range(n) for b in range(n)]
    slots13 = list(slots12)
    slots23 = list(slots12)
    total = 0
    fails = 0
    for mask in range(1 << 12):
        E12 = {slots12[i] for i in range(4) if (mask >> i) & 1}
        E13 = {slots13[i] for i in range(4) if (mask >> (4 + i)) & 1}
        E23 = {slots23[i] for i in range(4) if (mask >> (8 + i)) & 1}
        if has_transversal_triangle(n, n, n, E12, E13, E23):
            continue
        total += 1
        if not anticomplete_singleton_exists(n, n, n, E12, E13, E23):
            fails += 1
            print("COUNTEREXAMPLE (n=2):", E12, E13, E23)
    print(f"[exhaustive n=2] triangle-free instances: {total}, failures: {fails}")
    return fails == 0


def writeup_procedure(n1, n2, n3, E12, E13, E23):
    """Implement the writeup's proof verbatim; return ((i,X),(j,Y)) blocks 1-indexed."""
    W = min(n1, n2, n3)
    m = math.isqrt(W)
    # neighbourhoods of B2 vertices in B1 and B3
    N1 = {v: {a for a in range(n1) if (a, v) in E12} for v in range(n2)}
    N3 = {v: {c for c in range(n3) if (v, c) in E23} for v in range(n2)}
    for v in range(n2):
        if len(N1[v]) >= m and len(N3[v]) >= m:
            X = sorted(N1[v])[:m]
            Y = sorted(N3[v])[:m]
            return (1, X), (3, Y), m
    L1 = [v for v in range(n2) if len(N1[v]) < m]
    L3 = [v for v in range(n2) if len(N3[v]) < m]
    assert len(L1) + len(L3) >= n2
    if len(L1) >= m:
        Yv = L1[:m]
        covered = set().union(*(N1[y] for y in Yv)) if Yv else set()
        X = [a for a in range(n1) if a not in covered][:m]
        assert len(X) >= m, "proof's counting bound failed"
        return (1, X), (2, Yv), m
    else:
        assert len(L3) >= m
        Yv = L3[:m]
        covered = set().union(*(N3[y] for y in Yv)) if Yv else set()
        X = [c for c in range(n3) if c not in covered][:m]
        assert len(X) >= m, "proof's counting bound failed"
        return (3, X), (2, Yv), m


def is_anticomplete(blkX, X, blkY, Y, E12, E13, E23):
    E = {frozenset((1, 2)): E12, frozenset((1, 3)): E13, frozenset((2, 3)): E23}
    edges = E[frozenset((blkX, blkY))]
    lo, hi = min(blkX, blkY), max(blkX, blkY)
    A = X if blkX == lo else Y
    B = Y if blkY == hi else X
    return all((a, b) not in edges for a in A for b in B)


def random_instance(n, p):
    E12 = {(a, b) for a in range(n) for b in range(n) if random.random() < p}
    E13 = {(a, c) for a in range(n) for c in range(n) if random.random() < p}
    E23 = {(b, c) for b in range(n) for c in range(n) if random.random() < p}
    # destroy transversal triangles by deleting E23 edges
    changed = True
    while changed:
        changed = False
        for a in range(n):
            for b in range(n):
                if (a, b) in E12:
                    for c in range(n):
                        if (a, c) in E13 and (b, c) in E23:
                            E23.discard((b, c))
                            changed = True
    return E12, E13, E23


def randomized_check():
    trials = 0
    for n in [4, 6, 9, 16, 25, 36, 49, 60]:
        for p in [0.02, 0.1, 0.3, 0.6, 0.9]:
            for _ in range(40):
                E12, E13, E23 = random_instance(n, p)
                assert not has_transversal_triangle(n, n, n, E12, E13, E23)
                (bi, X), (bj, Y), m = writeup_procedure(n, n, n, E12, E13, E23)
                assert len(X) >= m and len(Y) >= m, (n, p, m, len(X), len(Y))
                assert bi != bj
                assert is_anticomplete(bi, X, bj, Y, E12, E13, E23), (n, p, bi, bj)
                assert m == math.isqrt(n)
                trials += 1
    print(f"[randomized] {trials} instances: writeup's construction always produced "
          f"a valid anticomplete pair of size m=floor(sqrt(W)) between distinct blocks")


def max_anticomplete_pair(nA, nB, edges, m):
    """Is there an anticomplete pair of size m between two blocks (brute force)?"""
    for X in itertools.combinations(range(nA), m):
        # Y must avoid all neighbours of X
        forb = {b for a in X for b in range(nB) if (a, b) in edges}
        if nB - len(forb) >= m:
            return True
    return False


def adversarial_small():
    checked = 0
    for n in [4, 5]:
        m = math.isqrt(n)
        for _ in range(3000):
            p = random.random()
            E12, E13, E23 = random_instance(n, p)
            if has_transversal_triangle(n, n, n, E12, E13, E23):
                continue
            ok = (max_anticomplete_pair(n, n, E12, m)
                  or max_anticomplete_pair(n, n, E13, m)
                  or max_anticomplete_pair(n, n, E23, m))
            checked += 1
            if not ok:
                print("COUNTEREXAMPLE:", n, E12, E13, E23)
                return False
    print(f"[adversarial small] {checked} triangle-free instances (n=4,5): proposition "
          f"held in every one (exact subset search)")
    return True


if __name__ == "__main__":
    ok1 = exhaustive_n2()
    randomized_check()
    ok3 = adversarial_small()
    print("ALL CHECKS PASSED" if (ok1 and ok3) else "SOME CHECK FAILED")
