"""Referee check for 1802.03727__00, Lemma 1 (induced-subgraph monotonicity).

Lemma 1: if H is induced in G and H has an uncolorable separated k-list assignment,
extending it by pairwise-disjoint fresh k-lists outside H gives an uncolorable
separated k-list assignment of G.

End-to-end test: H = K_17 with the Lemma 2 bad separated 2-assignment (verified
uncolorable in check_lemma2.py); G = K_17 plus 4 extra vertices with assorted
edges to the clique and among themselves (H stays induced). Fresh disjoint pairs
of colors outside. Verify: extended assignment separated on G, and exhaustive
search finds no proper list coloring of G.
"""
import itertools, math

IRRED = {3: 0b1011}
def gf_mul(a, b, m=3):
    p = IRRED[m]; res = 0
    while b:
        if b & 1: res ^= a
        b >>= 1; a <<= 1
        if a & (1 << m): a ^= p
    return res

def main():
    k, r, q, m = 2, 17, 8, 3
    X = [0, 1]
    pairs = list(itertools.product(range(q), range(q)))[:r]
    lists = {v: frozenset((x, gf_mul(a, x) ^ b) for x in X) for v, (a, b) in enumerate(pairs)}
    n_clique = 17
    extras = [17, 18, 19, 20]
    edges = [(u, v) for u in range(n_clique) for v in range(u + 1, n_clique)]
    edges += [(0, 17), (1, 17), (5, 18), (6, 18), (7, 18), (17, 18), (2, 19), (19, 20), (10, 20)]
    # fresh pairwise-disjoint lists (colors disjoint from P = X x F_q; use tag 'f')
    for idx, v in enumerate(extras):
        lists[v] = frozenset(("f", idx, t) for t in range(k))
    n = 21
    for u, v in edges:
        shared = len(lists[u] & lists[v])
        assert shared <= 1, (u, v, shared)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    Ls = [sorted(lists[v], key=str) for v in range(n)]
    def extend(v, col):
        if v == n: return True
        for c in Ls[v]:
            if all(col.get(w) != c for w in adj[v]):
                col[v] = c
                if extend(v + 1, col): return True
                del col[v]
        return False
    ok = extend(0, {})
    print(f"extended assignment separated: True; proper list coloring exists: {ok} (need False)")
    assert not ok
    print("PASS: Lemma 1 extension preserves separation and uncolorability")

main()
