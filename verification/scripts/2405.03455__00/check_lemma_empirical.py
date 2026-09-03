#!/usr/bin/env python3
"""Empirical stress-test of the alteration Lemma in the writeup for 2405.03455__00.

Lemma: if an N-point planar set P has fewer than l points on every line, then for
every k >= 3 it contains a subset Q with no k collinear points and
    |Q| >= (1/4) * (N/l)^((k-2)/(k-1)).

For a battery of concrete integer point sets (grids, unions of few lines,
random sets) and several k, we:
  1. compute the maximum number of collinear points (to get the true l = max+1),
  2. verify the edge bound e = sum_L C(s_L,k) <= l^(k-2) * C(N,2)  [ineq (1)],
  3. exhibit a subset with no k collinear of size >= bound via greedy deletion
     (delete a point of max hyperedge-degree until no line has k chosen points),
     which certifies the existential claim on that instance.
"""
import itertools, math, random
from collections import defaultdict
from fractions import Fraction

random.seed(12345)

def lines_of(points):
    """Group points by the line through them. Returns dict line -> set(indices)."""
    n = len(points)
    lines = {}
    for i, j in itertools.combinations(range(n), 2):
        (x1, y1), (x2, y2) = points[i], points[j]
        a, b = y2 - y1, x1 - x2
        c = -(a * x1 + b * y1)
        g = math.gcd(math.gcd(abs(a), abs(b)), abs(c)) or 1
        a, b, c = a // g, b // g, c // g
        if (a, b, c) < (0, 0, 0) or (a < 0) or (a == 0 and b < 0):
            a, b, c = -a, -b, -c
        lines.setdefault((a, b, c), set()).update((i, j))
    return lines

def greedy_no_k_collinear(points, k):
    """Greedy: repeatedly delete a point lying on a 'rich' line (>= k chosen pts)."""
    lines = lines_of(points)
    chosen = set(range(len(points)))
    while True:
        rich = [(len(S & chosen), L) for L, S in lines.items() if len(S & chosen) >= k]
        if not rich:
            break
        # delete the point covering the most rich lines (break ties arbitrarily)
        cnt = defaultdict(int)
        for _, L in rich:
            for p in lines[L] & chosen:
                cnt[p] += 1
        victim = max(cnt, key=lambda p: cnt[p])
        chosen.discard(victim)
    return chosen

def check_instance(name, points, ks):
    N = len(points)
    lines = lines_of(points)
    maxcol = max((len(S) for S in lines.values()), default=2)
    l = maxcol + 1  # fewer than l points on every line
    all_ok = True
    for k in ks:
        if k < 3:
            continue
        e = sum(math.comb(len(S), k) for S in lines.values())
        bound_e = l ** (k - 2) * math.comb(N, 2)
        ok_e = e <= bound_e
        target = 0.25 * (N / l) ** ((k - 2) / (k - 1))
        Q = greedy_no_k_collinear(points, k)
        ok_q = len(Q) >= target
        status = "PASS" if (ok_e and ok_q) else "FAIL"
        if not (ok_e and ok_q):
            all_ok = False
        print(f"[{status}] {name}: N={N} l={l} k={k}  e={e} <= {bound_e}: {ok_e}"
              f"  |Q|={len(Q)} >= {target:.2f}: {ok_q}")
    return all_ok

ok = True

# 1. grids (many collinear points)
for g in [5, 8, 12]:
    pts = [(x, y) for x in range(g) for y in range(g)]
    ok &= check_instance(f"{g}x{g} grid", pts, [3, 4, 5, g])

# 2. union of few long lines (extremal for the lemma: N/l points suffice-ish)
for nl, ppl in [(4, 20), (10, 15), (3, 40)]:
    pts = []
    for i in range(nl):
        # line y = i*x + 7i with ppl integer points, plus slight variety
        pts += [(t, i * t + 7 * i) for t in range(ppl)]
    pts = list(dict.fromkeys(pts))
    ok &= check_instance(f"{nl} lines x {ppl} pts", pts, [3, 4, 5])

# 3. random integer points (mostly general position)
for N in [30, 80]:
    pts = list({(random.randrange(1000), random.randrange(1000)) for _ in range(N)})
    ok &= check_instance(f"random N={len(pts)}", pts, [3, 4])

# 4. clustered construction mimicking the paper's lower bound: collinear
#    clusters of size l-1 placed at general-position locations
base = [(random.randrange(10**6), random.randrange(10**6)) for _ in range(12)]
lm1 = 6
pts = []
for (x, y) in base:
    for t in range(lm1):
        pts.append((x * 100 + t, y * 100 + 2 * t))  # small collinear cluster
pts = list(dict.fromkeys(pts))
ok &= check_instance("12 clusters of 6 collinear", pts, [3, 4, 5, 6, 7])

print()
print("ALL EMPIRICAL CHECKS PASSED" if ok else "SOME EMPIRICAL CHECKS FAILED")
