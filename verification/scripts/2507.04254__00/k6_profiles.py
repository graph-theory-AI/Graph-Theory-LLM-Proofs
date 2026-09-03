"""Exact impossibility proof, verified by enumeration, that G_6 (writeup's
construction, k=6) has no modular 6-edge-colouring with m <= 6 colours,
hence chi'_6(G_6) >= 7 = ceil(7k/6) -- as the writeup's lemma predicts.

Argument verified here (independent of the writeup's summation argument):
 1. For any m, a vertex of degree d must split d into at most m nonzero parts,
    each == 1 (mod 6).  We enumerate ALL such partitions by brute force.
 2. For m <= 5: degree-6 vertices admit no partition with <= 5 parts -> no colouring.
 3. For m = 6: the only profiles are:  deg 6 -> (1,1,1,1,1,1);  deg 12 -> (7,1,1,1,1,1).
    So every X-vertex and L-vertex has exactly one edge of each colour, and each
    of the 3 H-vertices has degree 1 or 7 in each colour.
    Colour class c edge count from the X side: e_c = |X| * 1 = 12.
    From the Y side: e_c = |L|*1 + sum over 3 H-vertices of (1 or 7)
                        = 6 + {3, 9, 15, 21}  = {9, 15, 21, 27}.
    12 is not attainable -> no 6-colouring.  We enumerate all 2^3 H-choices.
"""
import itertools

k = 6
nX, nH, nL = 2 * k, k // 2, k          # 12, 3, 6

def partitions_into_parts_1modk(d, max_parts):
    """All multisets of positive integers ==1 (mod k) summing to d, size <= max_parts."""
    parts_pool = [p for p in range(1, d + 1) if p % k == 1 % k]
    out = []
    def rec(remaining, minpart_idx, cur):
        if remaining == 0:
            out.append(tuple(cur))
            return
        if len(cur) == max_parts:
            return
        for i in range(minpart_idx, len(parts_pool)):
            p = parts_pool[i]
            if p > remaining:
                break
            cur.append(p)
            rec(remaining - p, i, cur)
            cur.pop()
    rec(d, 0, [])
    return out

# Step 2: m <= 5 impossible
for m in range(1, 6):
    assert partitions_into_parts_1modk(6, m) == [], m
print("m <= 5: degree-6 vertices have no admissible colour-degree profile -> impossible. OK")

# Step 3: m = 6
p6 = partitions_into_parts_1modk(6, 6)
p12 = partitions_into_parts_1modk(12, 6)
print("deg-6 profiles (m=6):", p6)
print("deg-12 profiles (m=6):", p12)
assert p6 == [(1, 1, 1, 1, 1, 1)]
assert p12 == [(1, 1, 1, 1, 1, 7)]
# every vertex uses all 6 colours; per colour, X contributes exactly 12 edges,
# L contributes 6 vertex-degrees of 1, each H vertex contributes 1 or 7.
attainable_Y = sorted({nL * 1 + sum(ch) for ch in itertools.product([1, 7], repeat=nH)})
print("attainable per-colour edge counts from Y side:", attainable_Y)
assert nX * 1 == 12 and 12 not in attainable_Y
print("X side forces e_c = 12 for every colour, unattainable from Y side -> no 6-colouring. OK")
print("=> chi'_6(G_6) >= 7 = ceil(7*6/6), independently confirming the lemma at k=6")
