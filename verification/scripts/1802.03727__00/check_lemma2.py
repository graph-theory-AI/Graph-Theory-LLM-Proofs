"""Referee check for 1802.03727__00, Lemma 2 (affine-function separated list assignment).

Lemma 2 claims: if chi(G) > 4k^2 then G has a separated k-list assignment with no
proper list coloring (hence ch_sep(G) > k).

Construction: r = chi(G); q = least power of 2 with q >= sqrt(r); X subset of F_q,
|X| = k; palette P = X x F_q; class V_i gets list S_{a_i,b_i} = {(x, a_i x + b_i) : x in X}
for distinct pairs (a_i,b_i) in F_q^2.

We verify, for two concrete graphs with chi = 17 and k = 2 (4k^2 = 16 < 17):
  (a) every list has size exactly k;
  (b) the assignment is separated: |L(u) cap L(v)| <= 1 for every edge uv;
  (c) |P| = kq < r;
  (d) EXHAUSTIVE search over all k^n list colorings finds no proper one.

Test graphs:
  1. K_17 (clique, chi = omega = 17)
  2. C_5 join K_14 (chi = 17 > omega = 16 -- tests that chromatic number, not
     clique number, drives the construction)

Also: integer sanity sweep that for all k in 1..300 and representative r > 4k^2,
the least power of two q >= sqrt(r) satisfies k <= q, q^2 >= r and kq < r.
"""
import itertools
import math

# ---------- GF(2^m) arithmetic ----------
IRRED = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011}

def gf_mul(a, b, m):
    """Multiply in GF(2^m) with the fixed irreducible polynomial."""
    p = IRRED[m]
    res = 0
    while b:
        if b & 1:
            res ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= p
    return res

def gf_check(m):
    """Sanity: GF(2^m) multiplication makes nonzero elements a group of order 2^m-1."""
    q = 1 << m
    for a in range(1, q):
        seen = {gf_mul(a, b, m) for b in range(1, q)}
        assert seen == set(range(1, q)), f"GF(2^{m}) mult table broken at {a}"

# ---------- construction ----------
def least_pow2_geq(x):
    q = 1
    while q < x:
        q *= 2
    return q

def build_assignment(classes, k):
    """classes: list of lists of vertices (a proper coloring). Returns lists dict, palette."""
    r = len(classes)
    q = least_pow2_geq(math.isqrt(r - 1) + 1)  # least power of 2 >= ceil(sqrt(r)) >= sqrt(r)
    # careful: we need q >= sqrt(r); isqrt(r-1)+1 = ceil(sqrt(r)) for r >= 1
    m = q.bit_length() - 1
    assert q == 1 << m
    assert q * q >= r, (q, r)
    assert q >= k
    X = list(range(k))  # k distinct field elements
    pairs = list(itertools.product(range(q), range(q)))[:r]
    lists = {}
    for (a, b), cls in zip(pairs, classes):
        S = frozenset((x, gf_mul(a, x, m) ^ b) for x in X)
        assert len(S) == k
        for v in cls:
            lists[v] = S
    palette = set().union(*lists.values())
    return lists, palette, q

def check_graph(name, n, edges, classes, k):
    print(f"=== {name}: n={n}, |E|={len(edges)}, r={len(classes)} classes, k={k} ===")
    r = len(classes)
    # verify proper coloring
    cls_of = {}
    for i, cls in enumerate(classes):
        for v in cls:
            cls_of[v] = i
    assert sorted(cls_of) == list(range(n)), "classes must partition V"
    for u, v in edges:
        assert cls_of[u] != cls_of[v], "coloring not proper"
    lists, palette, q = build_assignment(classes, k)
    # (a) list sizes
    assert all(len(L) == k for L in lists.values())
    # (b) separation
    max_shared = max(len(lists[u] & lists[v]) for u, v in edges)
    print(f"  q={q}, |P|={len(palette)} (= kq = {k*q}), r={r}; palette < r: {len(palette) < r}")
    print(f"  max |L(u) cap L(v)| over edges: {max_shared}  (need <= 1)")
    assert max_shared <= 1
    assert len(palette) == k * q < r
    # (d) exhaustive uncolorability
    Ls = [sorted(lists[v]) for v in range(n)]
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    # backtracking exhaustive search (equivalent to trying all k^n assignments)
    tried = 0
    def extend(v, col):
        nonlocal tried
        if v == n:
            return True
        for c in Ls[v]:
            if all(col.get(w) != c for w in adj[v]):
                col[v] = c
                if extend(v + 1, col):
                    return True
                del col[v]
        tried += 1
        return False
    ok = extend(0, {})
    print(f"  proper list coloring exists: {ok}  (need False)")
    assert not ok
    print("  PASS: separated k-assignment with no proper list coloring -> ch_sep > k\n")

def main():
    for m in range(1, 7):
        gf_check(m)
    print("GF(2^m) arithmetic verified for m=1..6\n")

    k = 2
    # Test 1: K_17
    n = 17
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    classes = [[v] for v in range(n)]
    check_graph("K_17", n, edges, classes, k)

    # Test 2: C_5 join K_14  (chi = 3 + 14 = 17, omega = 2 + 14 = 16)
    n = 19  # vertices 0..4 = C_5, 5..18 = K_14
    edges = [(i, (i + 1) % 5) for i in range(5)]
    edges = [tuple(sorted(e)) for e in edges]
    edges += [(u, v) for u in range(5, n) for v in range(u + 1, n)]  # K_14
    edges += [(c, u) for c in range(5) for u in range(5, n)]          # join
    # chi check by brute force lower bound: try to 16-color? Instead: verify no proper
    # 16-coloring exists via clique 16 + C5 not 2-colorable argument; do a direct search
    # that chi > 16: any proper coloring must give the 14 clique vertices 14 distinct
    # colors, all distinct from every C5 vertex color; C5 needs 3 colors. So chi = 17.
    classes = [[0, 2], [1, 3], [4]] + [[u] for u in range(5, n)]
    check_graph("C_5 join K_14 (chi=17 > omega=16)", n, edges, classes, k)

    # Integer sanity sweep for the general inequalities in Lemma 2
    bad = 0
    for kk in range(1, 301):
        for r in [4 * kk * kk + 1, 4 * kk * kk + 2, 5 * kk * kk + 3, 8 * kk * kk, 100 * kk * kk + 17]:
            q = least_pow2_geq(math.isqrt(r - 1) + 1)
            if not (q >= kk and q * q >= r and kk * q < r):
                bad += 1
                print("FAIL", kk, r, q)
    print(f"inequality sweep k=1..300: {'PASS' if bad == 0 else 'FAIL'} ({bad} failures)")

main()
