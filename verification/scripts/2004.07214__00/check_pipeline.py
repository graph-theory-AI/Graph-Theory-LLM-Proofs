"""Referee check for 2004.07214__00, Lemma 3 + Section 4 (full pipeline).

1. Lemma 3 sanity: for all graphs sampled, D is a minimal dominating set
   iff there exists W such that conditions (1) hold (checked by brute force
   over W).
2. Full enumeration pipeline: random posets P, G = Inc(P), vertex order =
   a linear extension; binary flashlight search using the DP extension oracle
   from check_dp_oracle; compare the enumerated family with the brute-force
   list of minimal dominating sets of G.

Also reports the max prefix-cut mim of the linear extension against the
largest standard example S_m contained in P (Lemma 1 inequality, again).
"""

import itertools
import random

from check_dp_oracle import dp_feasible, brute_force_exists, random_graph

random.seed(424242)


def closed(v, adj):
    return {v} | adj[v]


def is_min_domset(D, n, adj):
    V = range(n)
    if any(not (closed(v, adj) & D) for v in V):
        return False
    for d in D:
        if not any(len(closed(p, adj) & D) == 1 and d in closed(p, adj)
                   for p in closed(d, adj)):
            return False
    return True


def brute_min_domsets(n, adj):
    out = []
    for bits in itertools.product([0, 1], repeat=n):
        D = {v for v in range(n) if bits[v]}
        if is_min_domset(D, n, adj):
            out.append(frozenset(D))
    return set(out)


def lemma3_check(n, adj):
    """D minimal dominating iff exists W with (1)."""
    for bits in itertools.product([0, 1], repeat=n):
        D = {v for v in range(n) if bits[v]}
        exists_w = False
        for wbits in itertools.product([0, 1], repeat=n):
            W = {v for v in range(n) if wbits[v]}
            ok = True
            for v in range(n):
                cD = min(2, len(closed(v, adj) & D))
                cW = min(2, len(closed(v, adj) & W))
                if cD < 1:
                    ok = False
                    break
                if v in W and cD != 1:
                    ok = False
                    break
                if v in D and cW < 1:
                    ok = False
                    break
            if ok:
                exists_w = True
                break
        if exists_w != is_min_domset(D, n, adj):
            return (D,)
    return None


def random_poset(n):
    perm = list(range(n))
    random.shuffle(perm)
    rel = set()
    p = random.random() * 0.7 + 0.1
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                rel.add((perm[i], perm[j]))
    changed = True
    while changed:
        changed = False
        for (a, b) in list(rel):
            for c in range(n):
                if (b, c) in rel and (a, c) not in rel:
                    rel.add((a, c))
                    changed = True
    return rel


def linear_extension(rel, n):
    preds = {v: {a for (a, b) in rel if b == v} for v in range(n)}
    out = []
    remaining = set(range(n))
    while remaining:
        for v in sorted(remaining):
            if preds[v] <= set(out):
                out.append(v)
                remaining.discard(v)
                break
    return out


def inc_graph(rel, n):
    adj = {v: set() for v in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in rel and (j, i) not in rel:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def max_cut_mim(adj, order, n):
    best = 0
    E = {(a, b) for a in adj for b in adj[a]}
    for k in range(1, n):
        A, B = order[:k], order[k:]
        cross = [(a, b) for a in A for b in B if (a, b) in E]
        for m in range(best + 1, min(len(A), len(B)) + 1):
            found = False
            for combo in itertools.combinations(cross, m):
                As = [e[0] for e in combo]
                Bs = [e[1] for e in combo]
                if len(set(As)) < m or len(set(Bs)) < m:
                    continue
                if all((As[i], Bs[j]) not in E
                       for i in range(m) for j in range(m) if i != j):
                    found = True
                    break
            if found:
                best = m
            else:
                break
    return best


def max_standard_example(rel, n):
    """Largest m with S_m as induced suborder (brute force, small n)."""
    best = 0
    for m in range(1, n // 2 + 1):
        found = False
        for As in itertools.permutations(range(n), m):
            if As[0] != min(As):  # cut symmetry a bit
                continue
            rest = set(range(n)) - set(As)
            for Bs in itertools.permutations(sorted(rest), m):
                ok = True
                for i in range(m):
                    for j in range(m):
                        if i != j:
                            if (As[i], Bs[j]) not in rel:
                                ok = False
                                break
                            if (As[i], As[j]) in rel or (Bs[i], Bs[j]) in rel:
                                ok = False
                                break
                    if not ok:
                        break
                    if (As[i], Bs[i]) in rel or (Bs[i], As[i]) in rel:
                        ok = False
                        break
                if ok:
                    found = True
                    break
            if found:
                break
        if found:
            best = m
        else:
            break
    return best


def flashlight_enumerate(n, adj, order):
    """Binary flashlight search with the DP extension oracle (Section 4)."""
    out = []
    oracle_calls = [0]

    def oracle(I, O):
        oracle_calls[0] += 1
        return dp_feasible(n, adj, order, I, O)

    def rec(i, I, O):
        if i == n:
            out.append(frozenset(I))
            return
        v = order[i]
        if oracle(I | {v}, O):
            rec(i + 1, I | {v}, O)
        if oracle(I, O | {v}):
            rec(i + 1, I, O | {v})

    if oracle(set(), set()):
        rec(0, set(), set())
    return set(out), oracle_calls[0]


def main():
    # 1. Lemma 3 characterization, exhaustive over W, random graphs n<=6
    bad = 0
    for n in range(1, 7):
        for _ in range(25):
            adj = random_graph(n, random.random())
            if lemma3_check(n, adj):
                bad += 1
                print("LEMMA3 VIOLATION", n, adj)
    print(f"Lemma 3 (minimal domset <-> exists witness set W): "
          f"150 random graphs n=1..6: {bad} violations")

    # 2. full pipeline on random posets
    mismatches = 0
    trials = 0
    for n in range(2, 9):
        reps = {2: 10, 3: 20, 4: 30, 5: 30, 6: 25, 7: 12, 8: 6}[n]
        for _ in range(reps):
            rel = random_poset(n)
            adj = inc_graph(rel, n)
            order = linear_extension(rel, n)
            enum, calls = flashlight_enumerate(n, adj, order)
            brute = brute_min_domsets(n, adj)
            trials += 1
            if enum != brute:
                mismatches += 1
                print("PIPELINE MISMATCH", n, sorted(rel),
                      sorted(map(sorted, enum)), sorted(map(sorted, brute)))
            # Lemma 1 inequality check on this instance
            mim = max_cut_mim(adj, order, n)
            se = max_standard_example(rel, n)
            if mim > max(se, 1) or (se >= 1 and mim > se):
                print("LEMMA1 INEQ VIOLATION", n, sorted(rel), order, mim, se)
    print(f"flashlight+DP enumeration vs brute force on Inc(P): "
          f"{trials} random posets (n=2..8): {mismatches} mismatches")


if __name__ == "__main__":
    main()
