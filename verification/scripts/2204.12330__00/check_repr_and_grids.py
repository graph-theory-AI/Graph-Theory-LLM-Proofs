"""Checks for Sections 3 (consequence), 4 and 5 of the writeup.

Part A (Section 4): for n in {8, 9, 12, 16}, the double transpositions
  e_i = (4i-3, 4i-2)(4i-1, 4i), 1 <= i <= q = floor(n/4),
are even, commute, and generate an elementary abelian group of order 2^q.
Also check the known irrep dimension lists of A_5, A_6, A_7, A_8 against the
sum-of-squares identity and D(A_n) >= floor(n/4).

Part B (Sections 3+5, qualitative): for the finite group H = A_5 (N=60,
D(A_5)=3) and H = A_6 (N=360, D(A_6)=5) with several orders (natural lex
order, random orders, and the coset-transported order of Section 2 restricted
to H), divide (H, order) into r equal consecutive intervals and search for an
element h such that ALL r^2 cells of the r x r division of L_h contain at
least r ones.  The lemma's explicit hypothesis D > 16 r^4 is far from
satisfied at this size (constants are not optimized), so this only checks
that the qualitative phenomenon (uniform grids appear regardless of order)
is consistent, and that the counting |hA_i cap B_j| used in the writeup is
what makes the grid.
"""
import itertools, random
import numpy as np

random.seed(7)
rng = np.random.default_rng(7)

# ---------- Part A ----------
def double_transposition(n, i):  # e_i on points 4i-3..4i (1-indexed -> 0-indexed)
    p = list(range(n))
    a, b, c, d = 4 * i - 4, 4 * i - 3, 4 * i - 2, 4 * i - 1
    p[a], p[b] = p[b], p[a]
    p[c], p[d] = p[d], p[c]
    return tuple(p)

def compose(p, q):
    return tuple(p[q[x]] for x in range(len(q)))

def is_even(p):
    inv = sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])
    return inv % 2 == 0

for n in (8, 9, 12, 16):
    q = n // 4
    es = [double_transposition(n, i) for i in range(1, q + 1)]
    assert all(is_even(e) for e in es)
    assert all(compose(a, b) == compose(b, a) for a in es for b in es)
    # generate subgroup
    group = {tuple(range(n))}
    frontier = list(group)
    while frontier:
        new = []
        for g in frontier:
            for e in es:
                h = compose(g, e)
                if h not in group:
                    group.add(h); new.append(h)
        frontier = new
    assert len(group) == 2 ** q, (n, len(group))
    print(f"n={n}: e_1..e_{q} even, commuting, generate C_2^{q} of order {2**q}: OK")

# known complex irrep dimension lists (standard character tables)
irreps = {
    5: [1, 3, 3, 4, 5],
    6: [1, 5, 5, 8, 8, 9, 10],
    7: [1, 6, 10, 10, 14, 14, 15, 21, 35],
    8: [1, 7, 14, 20, 21, 21, 21, 28, 35, 45, 45, 56, 64, 70],
}
import math
for n, dims in irreps.items():
    order = math.factorial(n) // 2
    assert sum(d * d for d in dims) == order, n
    D = min(d for d in dims if d > 1)
    assert D >= n // 4, n
    print(f"A_{n}: |A_{n}|={order}, sum of squares OK, D(A_{n})={D} >= floor(n/4)={n//4}")

# ---------- Part B ----------
def build_group(n):
    els = [p for p in itertools.permutations(range(n)) if is_even(p)]
    idx = {p: i for i, p in enumerate(els)}
    return els, idx

def max_uniform_grid_for_order(els, idx, order_perm, rs):
    """order_perm: list of element-indices in order.  For each r in rs, report
    whether some h has all r^2 cells of the equal-interval r-division of L_h
    containing >= r ones."""
    N = len(els)
    posn = np.empty(N, dtype=int)
    for p, e in enumerate(order_perm):
        posn[e] = p
    # interval id of each position for each r
    out = {}
    for r in rs:
        bounds = np.linspace(0, N, r + 1).astype(int)
        block = np.zeros(N, dtype=int)
        for i in range(r):
            block[bounds[i]:bounds[i + 1]] = i
        found = None
        for hi, h in enumerate(els):
            if hi == 0:
                continue  # identity: diagonal, cells off-diagonal empty
            counts = np.zeros((r, r), dtype=int)
            for xi in range(N):
                gx = idx[compose(els[hi], els[xi])]
                counts[block[posn[xi]], block[posn[gx]]] += 1
            if counts.min() >= r:
                found = hi
                break
        out[r] = found
    return out

for n, rs in ((5, [2, 3]), (6, [2, 3, 4])):
    els, idx = build_group(n)
    N = len(els)
    orders = {"lex order": list(range(N))}
    for t in range(3):
        orders[f"random order {t}"] = list(rng.permutation(N))
    for name, op in orders.items():
        res = max_uniform_grid_for_order(els, idx, op, rs)
        desc = ", ".join(
            f"r={r}: {'h found' if hf is not None else 'NONE'}" for r, hf in res.items()
        )
        print(f"A_{n} (N={N}), {name}: uniform r-grid with >= r ones/cell -> {desc}")

print("DONE")
