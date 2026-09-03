"""Referee check for 2004.07214__00, Lemma 1:

Claim: if v_1..v_n is a linear extension of a poset P and (A_k, B_k) is a prefix
cut, then any induced matching of size m in the bipartite cut graph of the
incomparability graph Inc(P) has its 2m matched vertices inducing the standard
example S_m in P.  Consequently max cut mim <= t-1 whenever P is S_t-free.

We verify the strong form (the matched vertices induce S_m, with the matching
pairing) exhaustively for all posets on n <= 5 elements and all their linear
extensions and all induced matchings of every cut, and on random posets for
n = 6..11 (sampled linear extensions).
"""

import itertools
import random

random.seed(12345)


def is_transitive(rel, n):
    for a in range(n):
        for b in range(n):
            if (a, b) in rel:
                for c in range(n):
                    if (b, c) in rel and (a, c) not in rel:
                        return False
    return True


def all_posets(n):
    """All strict partial orders on [n] (as sets of ordered pairs)."""
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    count = 0
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        rel = {p for p, b in zip(pairs, bits) if b}
        # antisymmetry
        if any((b, a) in rel for (a, b) in rel):
            continue
        if not is_transitive(rel, n):
            continue
        count += 1
        yield rel
    # count printed by caller


def random_poset(n):
    """Random strict partial order: transitive closure of a random DAG on a
    random permutation."""
    perm = list(range(n))
    random.shuffle(perm)
    rel = set()
    p = random.random() * 0.7 + 0.1
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                rel.add((perm[i], perm[j]))
    # transitive closure
    changed = True
    while changed:
        changed = False
        for (a, b) in list(rel):
            for c in range(n):
                if (b, c) in rel and (a, c) not in rel:
                    rel.add((a, c))
                    changed = True
    return rel


def linear_extensions(rel, n, limit=None):
    """All (or up to limit) linear extensions of the poset."""
    preds = {v: {a for (a, b) in rel if b == v} for v in range(n)}
    out = []

    def rec(prefix, remaining):
        if limit is not None and len(out) >= limit:
            return
        if not remaining:
            out.append(list(prefix))
            return
        for v in sorted(remaining):
            if preds[v] <= set(prefix):
                prefix.append(v)
                rec(prefix, remaining - {v})
                prefix.pop()

    rec([], set(range(n)))
    return out


def incomparability_edges(rel, n):
    E = set()
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in rel and (j, i) not in rel:
                E.add((i, j))
                E.add((j, i))
    return E


def check_poset(rel, n, exts):
    """Return list of violations of the strong Lemma-1 claim."""
    E = incomparability_edges(rel, n)
    violations = []
    for order in exts:
        for k in range(1, n):
            A = set(order[:k])
            B = set(order[k:])
            cross = [(a, b) for a in A for b in B if (a, b) in E]
            # enumerate all induced matchings among cross edges (brute force)
            for m in range(1, min(len(A), len(B)) + 1):
                for combo in itertools.combinations(cross, m):
                    As = [e[0] for e in combo]
                    Bs = [e[1] for e in combo]
                    if len(set(As)) < m or len(set(Bs)) < m:
                        continue
                    # induced in the bipartite cut graph:
                    induced = all(
                        (As[i], Bs[j]) not in E
                        for i in range(m) for j in range(m) if i != j)
                    if not induced:
                        continue
                    # Lemma 1 proof claims: {As} u {Bs} induce S_m in P
                    # i.e. As antichain, Bs antichain, As[i] < Bs[j] iff i != j,
                    # As[i] incomparable Bs[i].
                    ok = True
                    for i in range(m):
                        for j in range(m):
                            if i != j:
                                if (As[i], Bs[j]) not in rel:
                                    ok = False
                                if (As[i], As[j]) in rel or (Bs[i], Bs[j]) in rel:
                                    ok = False
                        if (As[i], Bs[i]) in rel or (Bs[i], As[i]) in rel:
                            ok = False
                    if not ok:
                        violations.append((sorted(rel), order, k, combo))
    return violations


def main():
    # exhaustive for n <= 5
    for n in range(2, 6):
        cnt = 0
        bad = 0
        for rel in all_posets(n):
            cnt += 1
            exts = linear_extensions(rel, n)
            v = check_poset(rel, n, exts)
            if v:
                bad += 1
                print("VIOLATION", n, v[0])
        print(f"n={n}: exhaustively checked {cnt} posets, "
              f"all linear extensions, all cuts, all induced matchings: "
              f"{bad} violations")

    # random for n = 6..11
    for n in range(6, 12):
        bad = 0
        trials = {6: 400, 7: 250, 8: 120, 9: 60, 10: 30, 11: 15}[n]
        for _ in range(trials):
            rel = random_poset(n)
            exts = linear_extensions(rel, n, limit=20)
            v = check_poset(rel, n, exts)
            if v:
                bad += 1
                print("VIOLATION", n, v[0])
        print(f"n={n}: {trials} random posets (<=20 linear extensions each): "
              f"{bad} violations")


if __name__ == "__main__":
    main()
