#!/usr/bin/env python3
"""Monte Carlo check of the writeup's Lemma 1 (= Theorem 3 of arXiv:1902.06473):

    QLB(P) := n(H_n - QH(P)) equals F(P) = E_{sigma} sum_v H_{r_sigma(v)},

where QH(P) = E[-(1/n) sum ln z_i] for z UNIFORM (Lebesgue) on the chain
polytope C(P).  We sample z uniformly on C(P) by rejection from [0,1]^n
(the chain-polytope constraints are checked on all maximal chains) --
completely independent of the transfer-map argument being verified.
"""
import math, random
from verify_main import F_and_exts, linear_extensions

def maximal_chains(rel, n):
    succ = {v: [] for v in range(n)}
    pred = {v: set() for v in range(n)}
    for (i, j) in rel:
        succ[i].append(j); pred[j].add(i)
    # covers not needed: any chain constraint follows from maximal chains;
    # enumerate maximal chains in the DAG of relations
    chains = []
    def rec(chain, last):
        ext = [j for j in succ[last]]
        # keep only immediate extensions (any successor works; maximality handled below)
        extended = False
        for j in ext:
            rec(chain + [j], j); extended = True
        if not extended:
            chains.append(chain)
    for v in range(n):
        if not pred[v]:
            rec([v], v)
    return chains

def mc_qlb(rel, n, samples, rng):
    chains = maximal_chains(rel, n)
    tot = 0.0; tot2 = 0.0; acc = 0
    while acc < samples:
        z = [rng.random() for _ in range(n)]
        ok = all(sum(z[v] for v in ch) <= 1.0 for ch in chains)
        if not ok:
            continue
        acc += 1
        s = -sum(math.log(zi) for zi in z)   # = n*h(z)
        tot += s; tot2 += s * s
    mean = tot / samples                     # = n * QH estimate
    var = tot2 / samples - mean * mean
    Hn = sum(1.0 / k for k in range(1, n + 1))
    return n * Hn - mean, math.sqrt(var / samples)

def main():
    rng = random.Random(2026)
    tests = {
        'antichain3': (frozenset(), 3),
        'paper_example_b<a_plus_c': (frozenset({(1, 0)}), 3),  # b<=a, c isolated (relabeled 1<0)
        'N_poset': (frozenset({(0, 1), (2, 1), (2, 3)}), 4),   # a<b, c<b, c<d
        '2+2': (frozenset({(0, 1), (2, 3)}), 4),
        'diamond5': (frozenset({(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4),
                                (0, 4)}), 5),
        'random6': (frozenset({(0, 3), (1, 3), (1, 4), (2, 5), (0, 5)}), 6),
    }
    for name, (rel0, n) in tests.items():
        # normalize pairs so representation matches verify_main (i <_P j stored as-is)
        rel = frozenset(rel0)
        F, e = F_and_exts(rel, list(range(n)))
        est, se = mc_qlb(rel, n, 400000, rng)
        z = (est - float(F)) / se if se > 0 else 0.0
        print(f"{name:28s} n={n} e(P)={e:4d}  F(P)={float(F):.6f}  "
              f"MC QLB={est:.6f} +- {se:.6f}  (z={z:+.2f})")

if __name__ == '__main__':
    main()
