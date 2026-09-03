"""Referee check for 1802.03727__00, Lemma 3 (dense induced bipartite core).

Lemma 3 claims: if G has minimum degree d > 0 and chromatic number r, then G has an
induced bipartite subgraph B with delta(B) >= d / (2(r-1)).

(This matches Theorem 1.7 of the source paper arXiv:1802.03727, with denominator
2(r-1) instead of the paper's 2r -- the writeup's version is slightly sharper.)

We implement exactly the writeup's proof: take a proper coloring with r classes
(r = exact chromatic number, computed by SAT-style brute force for small n), pick
the pair (i,j) maximizing e_ij/(n_i+n_j), peel vertices of degree < a/2 where
a = 2 e_ij/(n_i+n_j), and verify:
  - the peeled graph B is nonempty, bipartite, induced in G;
  - a >= d/(r-1)  (the averaging step);
  - delta(B) >= a/2 >= d/(2(r-1)).
Tested on many random graphs G(n, p) (restricted to those with min degree > 0).
"""
import itertools
import random

def chromatic_number(n, adj):
    for r in range(1, n + 1):
        col = [-1] * n
        def rec(v):
            if v == n:
                return True
            used = {col[w] for w in adj[v] if col[w] >= 0}
            for c in range(min(r, v + 1)):  # symmetry break: vertex v uses color <= v
                if c not in used:
                    col[v] = c
                    if rec(v + 1):
                        return True
                    col[v] = -1
            return False
        if rec(0):
            return r, col
    raise AssertionError

def peel(vertices, edges_set, threshold):
    """Repeatedly delete vertices of current degree < threshold. Return survivors."""
    V = set(vertices)
    changed = True
    while changed:
        changed = False
        for v in list(V):
            deg = sum(1 for u in V if u != v and (min(u, v), max(u, v)) in edges_set)
            if deg < threshold:
                V.discard(v)
                changed = True
    return V

def run_one(n, p, rng):
    edges = set()
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < p:
                edges.add((u, v))
                adj[u].add(v)
                adj[v].add(u)
    d = min(len(a) for a in adj)
    if d == 0:
        return None
    r, col = chromatic_number(n, adj)
    if r < 2:
        return None
    classes = [[v for v in range(n) if col[v] == i] for i in range(r)]
    best = None
    for i, j in itertools.combinations(range(r), 2):
        eij = sum(1 for (u, v) in edges if col[u] in (i, j) and col[v] in (i, j))
        nij = len(classes[i]) + len(classes[j])
        if best is None or eij / nij > best[0]:
            best = (eij / nij, i, j, eij, nij)
    ratio, i, j, eij, nij = best
    m = len(edges)
    # averaging step: e_ij/(n_i+n_j) >= m/((r-1) n)
    assert ratio >= m / ((r - 1) * n) - 1e-12, (ratio, m, r, n)
    a = 2 * eij / nij
    assert a >= d / (r - 1) - 1e-12, (a, d, r)
    Vij = [v for v in range(n) if col[v] in (i, j)]
    eset = {(u, v) for (u, v) in edges if col[u] in (i, j) and col[v] in (i, j)}
    B = peel(Vij, eset, a / 2)
    assert B, "peeling emptied the graph -- contradicts Lemma 3 proof"
    # bipartite by construction (two color classes); check min degree
    degB = {v: sum(1 for u in B if u != v and (min(u, v), max(u, v)) in eset) for v in B}
    dB = min(degB.values())
    assert dB >= a / 2 - 1e-12, (dB, a)
    assert dB >= d / (2 * (r - 1)) - 1e-12, (dB, d, r)
    return (n, d, r, dB, d / (2 * (r - 1)))

def main():
    rng = random.Random(20260902)
    tested = 0
    for trial in range(4000):
        n = rng.randint(5, 13)
        p = rng.uniform(0.15, 0.95)
        res = run_one(n, p, rng)
        if res:
            tested += 1
    print(f"Lemma 3 verified on {tested} random graphs (n<=13, exact chi): "
          f"peeled induced bipartite subgraph always nonempty with "
          f"delta(B) >= d/(2(r-1)). PASS")

main()
