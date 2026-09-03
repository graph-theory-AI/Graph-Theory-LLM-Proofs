"""Verify the counterexample construction G_k from attacks/2507.04254__00/output.md.

G_k (k even): X = Z_{2k}; Y = H (|H|=k/2) disjoint-union L = Z_k.
- every h in H adjacent to every x in X;
- x ~ l  iff  (l - (x mod k)) mod k in S, where S subset of Z_k, |S| = k/2.

Claims to check (writeup, "Counterexample construction"):
  d(x) = k for x in X;  d(h) = 2k;  d(l) = k;
  graph simple, bipartite, no isolated vertices;
  |X| = 2k, |Y| = 3k/2, n = 7k/2, rho = dist(|X|-|Y|, kZ) = k/2;
  implied lower bound ceil(7k/6) from the lemma (arithmetic re-check).
"""
import itertools, math, sys


def build(k, S=None):
    assert k % 2 == 0 and k >= 2
    if S is None:
        S = set(range(k // 2))          # any S of size k/2 works; degrees are S-independent
    assert len(S) == k // 2 and all(0 <= s < k for s in S)
    X = [("x", i) for i in range(2 * k)]
    H = [("h", i) for i in range(k // 2)]
    L = [("l", i) for i in range(k)]
    edges = set()
    for h in H:
        for x in X:
            edges.add(frozenset((h, x)))
    for x in X:
        for l in L:
            if (l[1] - (x[1] % k)) % k in S:
                edges.add(frozenset((x, l)))
    return X, H, L, sorted(tuple(sorted(e)) for e in edges)


def check(k, S=None):
    X, H, L, edges = build(k, S)
    V = X + H + L
    # simple: edges is a set of unordered pairs of distinct vertices
    assert all(len(set(e)) == 2 for e in edges)
    # bipartite between X and Y=H+L
    Y = set(H) | set(L)
    for a, b in edges:
        assert (a in Y) != (b in Y) or ((a[0] == "x") != (b[0] == "x"))
        assert {a[0], b[0]} in ({"x", "h"}, {"x", "l"}, {"h", "x"}, {"l", "x"})
    deg = {v: 0 for v in V}
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    dx = {deg[v] for v in X}
    dh = {deg[v] for v in H}
    dl = {deg[v] for v in L}
    assert dx == {k}, (k, dx)
    assert dh == {2 * k}, (k, dh)
    assert dl == {k}, (k, dl)
    assert all(deg[v] % k == 0 and deg[v] > 0 for v in V)   # 0_k-graph, no isolated vertices
    nX, nY = len(X), len(H) + len(L)
    assert nX == 2 * k and 2 * nY == 3 * k
    n = nX + nY
    assert 2 * n == 7 * k
    diff = nX - nY
    rho = min(abs(diff - k * t) for t in range(-5, 6))
    assert 2 * rho == k, (k, rho)
    # lemma arithmetic: for m < 2k, n(m-k) >= m*rho  =>  m >= n*k/(n-rho) = 7k/6
    bound = math.ceil(n * k / (n - rho))
    assert bound == math.ceil(7 * k / 6), (k, bound)
    m_edges = len(edges)
    assert m_edges == 2 * k * k          # each x has degree k, |X| = 2k
    return n, rho, bound, m_edges


if __name__ == "__main__":
    for k in [2, 4, 6, 8, 10, 12, 20, 50]:
        n, rho, bound, m_edges = check(k)
        print(f"k={k}: OK. n={n}, rho={rho}, edges={m_edges}, "
              f"lemma lower bound ceil(7k/6)={bound} (= k + {bound - k})")
    # also try a different S for a couple of k, to confirm S-independence
    for k in [4, 6]:
        S = set(itertools.islice((s for s in range(k) if s % 2 == 0), k // 2))
        n, rho, bound, m_edges = check(k, S)
        print(f"k={k} with even S: OK, edges={m_edges}, bound={bound}")
    print("all construction checks passed")
