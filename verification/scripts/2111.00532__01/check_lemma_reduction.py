#!/usr/bin/env python3
"""Referee checks for attack 2111.00532__01.

The writeup claims: for every ordered graph H on k>=2 vertices, if a blockade
(B_1,...,B_k) of width W in G has no ordered B-transversal copy of H (v_i in B_i,
adjacency pattern equal to H), then some pair of blocks contains a pure pair
X,Y with |X|,|Y| >= t where t = floor((W/(k-1))^(1/(k-1))) >= W^(1/(k-1)) / (2 (k-1)^(1/(k-1))).

Proof structure verified here:
  1. Multipartite clique lemma (constructive implementation follows the proof
     verbatim; every internal counting claim of the proof is asserted).
  2. XOR reduction G,H -> F (transversal clique in F <=> ordered copy of H in G),
     checked exhaustively on random instances.
  3. End-to-end: run reduction + lemma on random blockades and independently
     verify the returned object in G (ordered H-copy, or pure pair of size >= t).
  4. Numeric inequality floor((W/(k-1))^(1/(k-1))) >= W^(1/(k-1))/(2(k-1)^(1/(k-1)))
     for all W >= k-1 over a large range, plus the W < k-1 remark.
  5. Exhaustive tiny-case check of the lemma (k=3, t=1, parts of size 2:
     all 2^12 cross-adjacency patterns).
"""

import itertools
import random
from collections import Counter


# ---------------------------------------------------------------- lemma

def lemma(parts, edge, t, depth=0):
    """Constructive version of the writeup's multipartite clique lemma.

    parts: list of k disjoint vertex lists, |parts[i]| >= (k-1)*t^(k-1).
    edge(u,v): symmetric adjacency predicate (cross-part edges of F).
    Returns ('clique', [v_1..v_k]) or ('anti', i, j, X, Y) with i<j,
    X subset of parts[i], Y subset of parts[j], |X|=|Y|=t, no edges X-Y.
    Asserts every counting step used in the proof.
    """
    k = len(parts)
    assert k >= 2
    for i, P in enumerate(parts):
        assert len(P) >= (k - 1) * t ** (k - 1), (k, t, i, len(P))
    if k == 2:
        for u in parts[0]:
            for v in parts[1]:
                if edge(u, v):
                    return ('clique', [u, v])
        return ('anti', 0, 1, parts[0][:t], parts[1][:t])
    need = (k - 2) * t ** (k - 2)
    assign = {}
    for v in parts[-1]:
        nbrs = [[u for u in parts[i] if edge(u, v)] for i in range(k - 1)]
        if all(len(N) >= need for N in nbrs):
            us = [N[:need] for N in nbrs]
            res = lemma(us, edge, t, depth + 1)
            if res[0] == 'clique':
                return ('clique', res[1] + [v])
            # anticomplete pair found inside U_i x U_j subset V_i x V_j
            _, i, j, X, Y = res
            return ('anti', i, j, X, Y)
        assign[v] = next(i for i, N in enumerate(nbrs) if len(N) < need)
    # every v in parts[-1] has a deficient index: pigeonhole
    cnt = Counter(assign.values())
    i, m = cnt.most_common(1)[0]
    # proof claims |Y_0| >= |V_k|/(k-1) >= t^(k-1) >= t
    assert m * (k - 1) >= len(parts[-1])
    assert m >= t ** (k - 1) >= t, (m, t, k)
    Y = [v for v in parts[-1] if assign[v] == i][:t]
    X = [u for u in parts[i] if all(not edge(u, v) for v in Y)]
    # proof claims >= t^(k-1) >= t non-neighbours remain in V_i
    assert len(X) >= t ** (k - 1) >= t, (len(X), t, k)
    return ('anti', i, k - 1, X[:t], Y)


def verify_certificate(parts, edge, t, res):
    """Independently verify a lemma certificate."""
    if res[0] == 'clique':
        vs = res[1]
        assert len(vs) == len(parts)
        for i, v in enumerate(vs):
            assert v in parts[i]
        for u, v in itertools.combinations(vs, 2):
            assert edge(u, v), 'claimed clique has a non-edge'
    else:
        _, i, j, X, Y = res
        assert i < j
        assert len(X) >= t and len(Y) >= t
        assert set(X) <= set(parts[i]) and set(Y) <= set(parts[j])
        for u in X:
            for v in Y:
                assert not edge(u, v), 'claimed anticomplete pair has an edge'


def random_lemma_trials():
    random.seed(20260902)
    configs = [(2, 4, 300), (3, 2, 800), (3, 3, 300), (4, 2, 200), (5, 2, 30)]
    total = Counter()
    for k, t, trials in configs:
        size = (k - 1) * t ** (k - 1)
        for tr in range(trials):
            # vary density; include extreme and near-critical densities
            p = random.choice([0.02, 0.1, 0.3, 0.5, 0.7, 0.9, 0.98,
                               random.random()])
            parts = [list(range(i * size, (i + 1) * size)) for i in range(k)]
            E = set()
            for a, b in itertools.combinations(range(k), 2):
                for u in parts[a]:
                    for v in parts[b]:
                        if random.random() < p:
                            E.add((u, v))
            edge = lambda u, v: (min(u, v), max(u, v)) in E or (u, v) in E or (v, u) in E
            res = lemma(parts, edge, t)
            verify_certificate(parts, edge, t, res)
            total[(k, t, res[0])] += 1
    print('lemma random trials passed:', dict(total))


def exhaustive_tiny_lemma():
    """k=3, t=1, parts of size 2 = (k-1)t^(k-1): all 2^12 cross patterns."""
    parts = [[0, 1], [2, 3], [4, 5]]
    cross = [(u, v) for a, b in itertools.combinations(range(3), 2)
             for u in parts[a] for v in parts[b]]
    assert len(cross) == 12
    count = Counter()
    for mask in range(1 << 12):
        E = {cross[i] for i in range(12) if mask >> i & 1}
        edge = lambda u, v: (u, v) in E or (v, u) in E
        res = lemma(parts, edge, 1)
        verify_certificate(parts, edge, 1, res)
        count[res[0]] += 1
        # independent brute-force cross-check of the disjunction
        has_clique = any(edge(a, b) and edge(a, c) and edge(b, c)
                         for a in parts[0] for b in parts[1] for c in parts[2])
        has_anti = any(not edge(u, v) for (u, v) in cross)
        assert has_clique or has_anti  # lemma disjunction, brute force
    print('exhaustive tiny lemma (4096 graphs) passed:', dict(count))

# ------------------------------------------------------- reduction check

def build_F(k, H_edges, blocks, G_edge):
    """F-edge between x in B_i, y in B_j (i<j): G-adjacency agrees with H."""
    def F_edge(u, v):
        bu, bv = block_of[u], block_of[v]
        if bu == bv:
            return False
        i, j = min(bu, bv), max(bu, bv)
        return G_edge(u, v) == ((i, j) in H_edges)
    block_of = {u: i for i, B in enumerate(blocks) for u in B}
    return F_edge


def reduction_equivalence_trials():
    """Exhaustively check: transversal clique in F <=> ordered copy of H in G."""
    random.seed(7)
    for trial in range(200):
        k = random.choice([2, 3, 4])
        bs = 4  # block size; k*4^k transversals is small
        blocks = [list(range(i * bs, (i + 1) * bs)) for i in range(k)]
        H_edges = {(i, j) for i, j in itertools.combinations(range(k), 2)
                   if random.random() < 0.5}
        E = set()
        p = random.random()
        for a, b in itertools.combinations(range(k), 2):
            for u in blocks[a]:
                for v in blocks[b]:
                    if random.random() < p:
                        E.add((u, v))
        G_edge = lambda u, v: (u, v) in E or (v, u) in E
        F_edge = build_F(k, H_edges, blocks, G_edge)
        for tv in itertools.product(*blocks):
            is_clique = all(F_edge(u, v) for u, v in itertools.combinations(tv, 2))
            is_copy = all(G_edge(tv[i], tv[j]) == ((i, j) in H_edges)
                          for i, j in itertools.combinations(range(k), 2))
            assert is_clique == is_copy
    print('reduction equivalence: 200 random (G,H) instances,'
          ' all transversals agree')

# ------------------------------------------------------- end-to-end check

def end_to_end_trials():
    random.seed(99)
    stats = Counter()
    for trial in range(120):
        k = random.choice([2, 3, 4])
        W = {2: 60, 3: 100, 4: 90}[k]
        # t = floor((W/(k-1))^(1/(k-1))), computed robustly in integers
        t = 1
        while (k - 1) * (t + 1) ** (k - 1) <= W:
            t += 1
        assert (k - 1) * t ** (k - 1) <= W
        blocks = [list(range(i * W, (i + 1) * W)) for i in range(k)]
        H_edges = {(i, j) for i, j in itertools.combinations(range(k), 2)
                   if random.random() < 0.5}
        p = random.choice([0.05, 0.3, 0.5, 0.7, 0.95, random.random()])
        E = set()
        for a, b in itertools.combinations(range(k), 2):
            for u in blocks[a]:
                for v in blocks[b]:
                    if random.random() < p:
                        E.add((u, v))
        G_edge = lambda u, v: (u, v) in E or (v, u) in E
        F_edge = build_F(k, H_edges, blocks, G_edge)
        parts = [B[: (k - 1) * t ** (k - 1)] for B in blocks]
        res = lemma(parts, F_edge, t)
        if res[0] == 'clique':
            tv = res[1]
            # verify: this is an ordered B-transversal copy of H in G
            for i, j in itertools.combinations(range(k), 2):
                assert G_edge(tv[i], tv[j]) == ((i, j) in H_edges)
            stats['ordered H copy found'] += 1
        else:
            _, i, j, X, Y = res
            assert len(X) >= t and len(Y) >= t
            if (i, j) in H_edges:
                for u in X:
                    for v in Y:
                        assert not G_edge(u, v)
                stats['anticomplete pure pair'] += 1
            else:
                for u in X:
                    for v in Y:
                        assert G_edge(u, v)
                stats['complete pure pair'] += 1
            # claimed uniform bound
            assert t >= W ** (1.0 / (k - 1)) / (2 * (k - 1) ** (1.0 / (k - 1))) - 1e-9
    print('end-to-end trials passed:', dict(stats))

# ------------------------------------------------------- numeric bound

def numeric_bound_check():
    bad = []
    for k in range(2, 12):
        for W in range(k - 1, 5000):
            t = 1
            while (k - 1) * (t + 1) ** (k - 1) <= W:
                t += 1
            # t = floor((W/(k-1))^(1/(k-1)))
            lower = W ** (1.0 / (k - 1)) / (2 * (k - 1) ** (1.0 / (k - 1)))
            if t < lower - 1e-9:
                bad.append((k, W, t, lower))
        # W < k-1: claimed bound is < 1 (a singleton pure pair suffices)
        for W in range(1, k - 1):
            lower = W ** (1.0 / (k - 1)) / (2 * (k - 1) ** (1.0 / (k - 1)))
            assert lower < 1
    print('numeric bound check: OK' if not bad else f'FAILURES: {bad[:5]}')


if __name__ == '__main__':
    exhaustive_tiny_lemma()
    random_lemma_trials()
    reduction_equivalence_trials()
    end_to_end_trials()
    numeric_bound_check()
    print('ALL CHECKS PASSED')
