"""Check the writeup's Section 2 construction on the chain S_2 < S_3 < S_4.

Construction: having ordered G_m, partition G_{m+1} into right cosets G_m t,
put G_m first, order other cosets arbitrarily, transport the order on G_m to
G_m t via x -> x t.  Claims verified here on G = S_4 (chain {e} < S_2 < S_3 < S_4):

  (a) every right coset G_m x is convex in the final order;
  (b) for g in G_m, all order-inversions of L_g (x < y but gx > gy) happen
      inside a single right G_m-coset;
  (c) for g in G_m, the permutation matrix of L_g (rows/cols in the built
      order) contains no (|G_m|+1)-grid, where a k-grid is k consecutive
      row intervals and k consecutive column intervals with every cell
      containing a 1 (paper's k-grid from a k x k-division).
      Checked by exhaustive search over row-cut positions with an exact
      greedy feasibility test for column cuts.
"""
import itertools

n = 4
elements_all = list(itertools.permutations(range(n)))

def compose(p, q):  # (p*q)(x) = p(q(x))
    return tuple(p[q[x]] for x in range(len(q)))

def embed(p, n):  # embed a permutation of range(k) into range(n)
    return tuple(list(p) + list(range(len(p), n)))

# chain G_0={e} < G_1=S_2 < G_2=S_3 < G_3=S_4, all as permutations of range(4)
chain = []
for k in range(1, n + 1):
    Gk = [embed(p, n) for p in itertools.permutations(range(k))]
    chain.append(set(Gk))

# ---- build the order recursively ----
order = [embed(tuple(range(1)), n)]  # trivial group: [identity]
for m in range(len(chain) - 1):
    Gm, Gnext = chain[m], chain[m + 1]
    assert set(order) == Gm
    # right cosets of Gm in Gnext
    seen = set()
    cosets = []
    for t in sorted(Gnext):  # deterministic "arbitrary" order of cosets
        if t in seen:
            continue
        coset = frozenset(compose(x, t) for x in Gm)
        seen |= coset
        cosets.append((t, coset))
    new_order = list(order)  # Gm first (it is the coset of identity)
    for t, coset in cosets:
        if t in Gm:
            continue
        new_order.extend(compose(x, t) for x in order)  # transported order
    order = new_order
assert len(order) == 24 and set(order) == chain[-1]
pos = {p: i for i, p in enumerate(order)}
print("order built on S_4:", [''.join(map(str, p)) for p in order])

# ---- (a) convexity of right cosets G_m x ----
for m, Gm in enumerate(chain):
    for x in chain[-1]:
        coset = sorted(pos[compose(g, x)] for g in Gm)
        assert coset == list(range(coset[0], coset[0] + len(coset))), (m, x)
print("(a) all right cosets G_m x are convex: OK")

# ---- (b) inversions of L_g stay within one right G_m-coset ----
N = 24
for m, Gm in enumerate(chain):
    for g in Gm:
        for xi in range(N):
            for yi in range(xi + 1, N):
                x, y = order[xi], order[yi]
                if pos[compose(g, y)] < pos[compose(g, x)]:
                    # must be same right G_m-coset: x y^{-1} in Gm ... right coset Gm x = Gm y
                    yinv = tuple(sorted(range(n), key=lambda i: y[i]))
                    assert compose(x, yinv) in Gm, (m, g, x, y)
print("(b) all inversions of L_g (g in G_m) are within a single G_m-coset: OK")

# ---- (c) no (|G_m|+1)-grid in L_g ----
def perm_of_Lg(g):
    return [pos[compose(g, order[i])] for i in range(N)]  # column of the 1 in row i

def has_k_grid(perm, k, N):
    """Exact test: exists k x k division (k row intervals, k column intervals,
    consecutive, covering [0,N)) with every cell nonempty.
    Exhaust row cuts; greedy minimal column cuts is exact for fixed rows."""
    if k == 1:
        return True
    for rowcuts in itertools.combinations(range(1, N), k - 1):
        bounds = [0] + list(rowcuts) + [N]
        colsets = []
        for i in range(k):
            s = sorted(perm[r] for r in range(bounds[i], bounds[i + 1]))
            colsets.append(s)
        # greedy: process column intervals left to right with minimal cuts
        import bisect
        ptr = [0] * k  # pointer into each sorted colset
        start = 0
        ok = True
        for j in range(k):
            # minimal end position e such that every colset has an element in [start, e)
            need = 0
            for i in range(k):
                t = bisect.bisect_left(colsets[i], start)
                if t >= len(colsets[i]):
                    ok = False
                    break
                need = max(need, colsets[i][t])
            if not ok:
                break
            start = need + 1  # cut just after the last mandatory element
        if ok:
            return True
    return False

sizes = [len(G) for G in chain]  # 1, 2, 6, 24
for m, Gm in enumerate(chain[:-1]):  # for G_3 = S_4 bound 24 is vacuous
    s = sizes[m]
    for g in sorted(Gm):
        perm = perm_of_Lg(g)
        if s + 1 <= N:
            assert not has_k_grid(perm, s + 1, N), (m, g)
        # also report the largest grid found (search upward from 1)
        k = 1
        while k + 1 <= min(s, N) and has_k_grid(perm, k + 1, N):
            k += 1
        print(f"  g={''.join(map(str,g))} in G_{m} (|G_{m}|={s}): max grid = {k} <= {s}")
print("(c) no (|G_m|+1)-grid for any g in G_m: OK")
print("ALL COSET-ORDER CHECKS PASSED")
