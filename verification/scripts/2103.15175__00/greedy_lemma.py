#!/usr/bin/env python3
"""Independent implementation of the writeup's separation lemma greedy, tested
on many random and adversarial k-list assignments on K_n with n = s^k, for
several (s,k).  For each instance we:
  1. run the greedy exactly as in the writeup (choose x_j in [s]^C avoiding
     the bad sets B_i);  FAILURE of the greedy would falsify the union-bound
     argument;
  2. independently verify the produced maps f_c separate every edge in some
     listed color;
  3. build the coloring phi and verify, edge by edge, that f_c is a proper
     s-coloring of each color class G_c (hence chi(G_c) <= s, so no
     monochromatic member of H_s).
Only the coordinates relevant to earlier neighbours are searched (the rest are
set arbitrarily), which is an equivalent but feasible version of scanning
[s]^C.
"""
import itertools, random, sys

def greedy_separation(n, s, lists):
    """lists: dict edge (i,j) i<j -> tuple of k distinct colors.
    Returns f: dict color -> list of vertex labels in [s], or None if the
    greedy gets stuck (should never happen when n <= s^k)."""
    colors = sorted({c for L in lists.values() for c in L})
    f = {c: [None]*n for c in colors}
    for j in range(n):
        # coordinates relevant to edges (i,j), i<j
        rel = sorted({c for i in range(j) for c in lists[(i,j)]})
        def bad(x):
            return any(all(x[c] == f[c][i] for c in lists[(i,j)])
                       for i in range(j))
        found = None
        # the union bound guarantees the good fraction is >= 1 - (n-1)/s^k
        # > 0, so random sampling finds a good vector fast; fall back to an
        # exhaustive scan when the relevant coordinate set is small.
        for _ in range(20000):
            x = dict(zip(rel, (random.randrange(s) for _ in rel)))
            if not bad(x):
                found = x; break
        if found is None and s**len(rel) <= 2_000_000:
            for combo in itertools.product(range(s), repeat=len(rel)):
                x = dict(zip(rel, combo))
                if not bad(x):
                    found = x; break
        if found is None:
            return None
        for c in colors:
            f[c][j] = found.get(c, 0)   # irrelevant coordinates: arbitrary
    return f

def verify_instance(n, s, k, lists):
    f = greedy_separation(n, s, lists)
    if f is None:
        return "GREEDY_STUCK"
    # check separation + build coloring
    phi = {}
    for (i,j),L in lists.items():
        sep = [c for c in L if f[c][i] != f[c][j]]
        if not sep:
            return "NOT_SEPARATED"
        phi[(i,j)] = sep[0]
    # verify each color class properly s-colored by f_c
    for (i,j),c in phi.items():
        if f[c][i] == f[c][j]:
            return "IMPROPER"
    return "OK"

def random_lists(n, k, palette):
    return {(i,j): tuple(random.sample(palette, k))
            for i in range(n) for j in range(i+1,n)}

def run(s, k, trials, seed=0):
    random.seed(seed)
    n = s**k
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    fails = 0
    # adversarial: constant lists (extremal case: exactly one free vector at
    # the last vertex)
    const = {e: tuple(range(k)) for e in edges}
    r = verify_instance(n, s, k, const)
    print(f"s={s} k={k} n={n}: constant lists -> {r}")
    if r != "OK": fails += 1
    for t in range(trials):
        psize = random.choice([k, k+1, 2*k, 3*k, k*len(edges)])
        palette = list(range(psize))
        L = random_lists(n, k, palette)
        r = verify_instance(n, s, k, L)
        if r != "OK":
            fails += 1
            print(f"s={s} k={k} trial {t} palette {psize}: {r}")
    print(f"s={s} k={k} n={n}: {trials} random trials, failures: {fails}")
    return fails

total = 0
total += run(2, 2, 2000, seed=1)
total += run(2, 3, 500, seed=2)
total += run(3, 2, 500, seed=3)
total += run(2, 4, 100, seed=4)   # n=16
total += run(3, 3, 50, seed=5)    # n=27
total += run(5, 2, 50, seed=6)    # n=25
if total == 0:
    print("ALL GREEDY/SEPARATION/PROPERNESS CHECKS PASSED")
else:
    print("FAILURES FOUND"); sys.exit(1)
