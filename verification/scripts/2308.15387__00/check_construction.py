#!/usr/bin/env python3
"""Verify the binary vector-space colouring used in attacks/2308.15387__00/output.md.

Lemma claimed: for r = 2^d - 1, n = t*2^d, colour K_n with vertex classes V_x
(x in F_2^d, each of size t); edge between V_x, V_y (x != y) gets colour x^y
(nonzero vector); edges inside every class get a fixed colour v0.
Claim: for every colour set C with |C| <= s, every component of the graph G_C
of edges coloured in C has at most 2^s * t vertices (in fact at most
|span(C)| * t).

Also checks:
  * surjectivity (all r colours occur),
  * the exact max component size over all C of size exactly s,
  * the writeup's "general r" variant (unused labels + colour-class splitting),
  * the elementary edge-count lower bound M >= 1 + s(n-1)/r on this colouring.
"""
import itertools
import sys
from collections import defaultdict


def components(n, adj):
    seen = [False] * n
    sizes = []
    for v0 in range(n):
        if seen[v0]:
            continue
        stack = [v0]
        seen[v0] = True
        c = 0
        while stack:
            v = stack.pop()
            c += 1
            for w in adj[v]:
                if not seen[w]:
                    seen[w] = True
                    stack.append(w)
        sizes.append(c)
    return sizes


def build_colouring(d, t, v0=1):
    """Return (n, r, edgecol) for the F_2^d construction; colours are 1..2^d-1."""
    m = 1 << d
    n = t * m
    cls = lambda v: v // t  # vertex -> class index in [0, 2^d)
    edgecol = {}
    for u in range(n):
        for w in range(u + 1, n):
            x, y = cls(u), cls(w)
            edgecol[(u, w)] = (x ^ y) if x != y else v0
    return n, m - 1, edgecol


def span_size(vecs):
    basis = []
    for v in vecs:
        w = v
        for b in basis:
            w = min(w, w ^ b)
        if w:
            basis.append(w)
    return 1 << len(basis)


def max_comp_for_C(n, edgecol, C):
    Cset = set(C)
    adj = defaultdict(list)
    for (u, w), c in edgecol.items():
        if c in Cset:
            adj[u].append(w)
            adj[w].append(u)
    return max(components(n, adj))


def check_lemma(d, t):
    n, r, edgecol = build_colouring(d, t)
    colours_used = set(edgecol.values())
    assert colours_used == set(range(1, r + 1)), "surjectivity fails"
    print(f"d={d} r={r} t={t} n={n}: all {r} colours occur -> surjective OK")
    ok = True
    for s in range(1, d + 1):
        worst = 0
        bound = (1 << s) * t
        for C in itertools.combinations(range(1, r + 1), s):
            mc = max_comp_for_C(n, edgecol, C)
            worst = max(worst, mc)
            # sharper claim: component <= |span(C)| * t
            if mc > span_size(C) * t:
                print(f"  FAIL span bound: C={C} maxcomp={mc} span={span_size(C)}")
                ok = False
        edge_lb = 1 + s * (n - 1) / r
        status = "OK" if worst <= bound else "FAIL"
        if worst > bound:
            ok = False
        print(f"  s={s}: max over C of largest comp = {worst}  "
              f"(claimed <= 2^s*t = {bound}) {status}; "
              f"edge-count lower bound 1+s(n-1)/r = {edge_lb:.2f} "
              f"{'OK' if worst >= edge_lb else 'FAIL(lb)'}")
        if worst < edge_lb:
            ok = False
    return ok


def check_general_r(r, n, s_max):
    """Writeup's general variant: m = 2^floor(log2(r+1)), use the F_2^log2(m)
    construction on m classes, then split colour classes to use all r labels."""
    import math
    d = int(math.floor(math.log2(r + 1)))
    m = 1 << d
    base = m // 2  # class sizes: split n into m parts as equally as possible
    sizes = [n // m + (1 if i < n % m else 0) for i in range(m)]
    starts = [0]
    for sz in sizes:
        starts.append(starts[-1] + sz)
    cls_of = []
    for i in range(m):
        cls_of += [i] * sizes[i]
    v0 = 1
    edgecol = {}
    for u in range(n):
        for w in range(u + 1, n):
            x, y = cls_of[u], cls_of[w]
            edgecol[(u, w)] = (x ^ y) if x != y else v0
    # split: refine colours m..? we need r colours total; original m-1 colours.
    # Split colour 1's edge set into (r - (m-1) + 1) parts round-robin.
    extra = r - (m - 1)
    if extra > 0:
        c1_edges = [e for e, c in edgecol.items() if c == 1]
        for i, e in enumerate(c1_edges):
            edgecol[e] = 1 if i % (extra + 1) == 0 else (m - 1 + (i % (extra + 1)))
    used = set(edgecol.values())
    print(f"general r={r}: m={m}, colours used = {len(used)} (want {r}): "
          f"{'OK' if len(used) == r else 'note: some split part empty'}")
    parent = {c: (1 if c >= m else c) for c in range(1, r + 1)}
    import itertools as it
    ok = True
    ceil_nm = -(-n // m)
    for s in range(1, s_max + 1):
        worst = 0
        bound = min(1 << s, m) * ceil_nm
        for C in it.combinations(sorted(used), s):
            mc = max_comp_for_C(n, edgecol, C)
            worst = max(worst, mc)
            # refined colours map into <= s original classes
            origs = {parent[c] for c in C}
            assert len(origs) <= s
        status = "OK" if worst <= bound else "FAIL"
        if worst > bound:
            ok = False
        print(f"  s={s}: max largest comp = {worst} (claimed <= min(2^s,m)*ceil(n/m) = {bound}) {status}")
    return ok


if __name__ == "__main__":
    ok = True
    ok &= check_lemma(d=3, t=2)   # r=7,  n=16
    ok &= check_lemma(d=3, t=3)   # r=7,  n=24
    ok &= check_lemma(d=4, t=2)   # r=15, n=32 (s up to 4; C(15,4)=1365 subsets)
    ok &= check_general_r(r=10, n=26, s_max=3)  # m=8, non-power-of-two r
    print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
    sys.exit(0 if ok else 1)
