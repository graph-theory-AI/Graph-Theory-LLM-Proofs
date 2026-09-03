"""Check 4: numeric ingredients of the union bound, plus exact small values.

  (a) 2e^3 < 49;
  (b) C(N,s) <= (eN/s)^s for many (N,s);
  (c) d! >= (d/e)^d for d=0..40;
  (d) algebra: (eN/s)*(2e^2 n/s) = 2e^3 n^3/s^2 when N=n^2;
  (e) exact a(D_4) over all 2^16 subsets, and exact dichromatic number of D_4;
  (f) randomized-greedy lower bounds on a(D_n) for n=30, 49 vs 7 n^{3/2}
      (sanity that acyclic sets found are far below n^2).
"""
import math, itertools, random
from check1_construction import build_Dn

# (a)
print(f"2e^3 = {2*math.e**3:.6f} < 49 : {2*math.e**3 < 49}")
assert 2 * math.e**3 < 49

# (b)
for N, s in [(100, 7), (10000, 700), (2500, 350), (49**2, int(7*49**1.5)+1)]:
    lhs = math.log(math.comb(N, min(s, N)))
    rhs = s * math.log(math.e * N / s)
    assert lhs <= rhs, (N, s)
print("C(N,s) <= (eN/s)^s : OK on samples")

# (c)
for d in range(0, 41):
    assert math.factorial(d) >= (d / math.e) ** d if d > 0 else True
print("d! >= (d/e)^d : OK for d<=40")

# (d)
n, s = 64.0, 7 * 64.0**1.5
val1 = (math.e * n**2 / s) * (2 * math.e**2 * n / s)
val2 = 2 * math.e**3 * n**3 / s**2
assert abs(val1 - val2) / val2 < 1e-12
print(f"algebraic combination OK; base at s=7n^1.5: {val2:.6f} (= 2e^3/49 = {2*math.e**3/49:.6f})")

# (e) exact a(D_4) and dichromatic number of D_4
def is_acyclic(sub, out):
    indeg = {v: 0 for v in sub}
    for u in sub:
        for w in out[u]:
            if w in indeg: indeg[w] += 1
    q = [v for v in sub if indeg[v] == 0]
    seen = 0
    while q:
        x = q.pop(); seen += 1
        for y in out[x]:
            if y in indeg:
                indeg[y] -= 1
                if indeg[y] == 0: q.append(y)
    return seen == len(sub)

V, arcs = build_Dn(4, 7)
out = {v: [] for v in V}
for u, w in arcs: out[u].append(w)
idx = {i: v for i, v in enumerate(V)}
best = 0
for mask in range(1 << 16):
    sub = {idx[i] for i in range(16) if (mask >> i) & 1}
    if len(sub) > best and is_acyclic(sub, out):
        best = len(sub)
print(f"n=4: exact a(D_4) = {best} (|V|=16, lower bd chi_vec >= {16/best:.2f})")

# 2-colorability: is chi_vec(D_4) <= 2?
two = False
for mask in range(1 << 15):  # fix vertex 0 in part A by symmetry
    A = {idx[i] for i in range(16) if (mask >> i) & 1} | {idx[15]}
    B = set(V) - A
    if is_acyclic(A, out) and is_acyclic(B, out):
        two = True; break
print(f"chi_vec(D_4) <= 2 ? {two}  => chi_vec(D_4) = {2 if two else '>2'}")

# (f) randomized greedy acyclic sets in D_n for larger n
for n, seed in [(30, 11), (49, 12)]:
    V, arcs = build_Dn(n, seed)
    out = {v: [] for v in V}
    for u, w in arcs: out[u].append(w)
    best = 0
    rng = random.Random(seed)
    for trial in range(3):
        orderv = V[:]; rng.shuffle(orderv)
        S = set()
        for v in orderv:
            S.add(v)
            if not is_acyclic(S, out):
                S.discard(v)
        best = max(best, len(S))
    print(f"n={n}: greedy acyclic set found {best}; n = {n}, 7 n^1.5 = {7*n**1.5:.0f}, n^2 = {n*n}")
print("CHECK4 DONE")
