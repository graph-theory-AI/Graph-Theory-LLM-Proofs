#!/usr/bin/env python3
"""Referee verification for attack 1902.06473__00.

Checks, for ALL posets on up to N_EXHAUSTIVE elements (up to isomorphism, via
naturally-labeled representatives) and random larger posets:

  (A) Main claim (17):  ln e(P) <= F(P) <= ln e(P) / ln 2,
      where F(P) = E_{sigma in L(P)} sum_v H_{r_sigma(v)}  (writeup's QLB formula,
      identical to eq. (qlb) of arXiv:1902.06473).
  (B) Lemma 4: for every maximal v,
      ln(e(P)/e(P-v)) <= c_v <= (1/ln2) ln(e(P)/e(P-v)),
      and log-concavity + monotonicity of the tail sequence a_k = Pr(L_v >= k)
      (equivalently of the fixed-element rank counts N_j -- Stanley's theorem).
  (C) Recursion (14): F(P) = sum_{v maximal} q_v (F(P-v) + c_v), exactly in
      rational arithmetic.
  (D) Insertion identity: e(P) = e(P-v) * E[L_v + 1].
"""
import itertools, math, random
from fractions import Fraction

# ---------- harmonic numbers ----------
HMAX = 40
H = [Fraction(0)]
for k in range(1, HMAX):
    H.append(H[-1] + Fraction(1, k))

# ---------- poset utilities ----------
# poset on elements 0..n-1 given as frozenset of pairs (i,j) meaning i <_P j,
# always with i < j (natural labeling; every iso class has such a representative).

def is_transitive(rel, n):
    s = set(rel)
    for (i, j) in rel:
        for (j2, k) in rel:
            if j2 == j and (i, k) not in s:
                return False
    return True

def all_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for bits in range(1 << len(pairs)):
        rel = [pairs[t] for t in range(len(pairs)) if bits >> t & 1]
        if is_transitive(rel, n):
            yield frozenset(rel)

def random_poset(n, p, rng):
    """random naturally-labeled poset: keep each pair (i<j) w.p. p, transitive closure."""
    rel = set()
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                rel.add((i, j))
    # transitive closure (Warshall)
    changed = True
    while changed:
        changed = False
        for (i, j) in list(rel):
            for (j2, k) in list(rel):
                if j2 == j and (i, k) not in rel:
                    rel.add((i, k)); changed = True
    return frozenset(rel)

def linear_extensions(rel, elems):
    """yield tuples listing elements in order (position 0 first)."""
    preds = {v: set() for v in elems}
    for (i, j) in rel:
        if i in preds and j in preds:
            preds[j].add(i)
    n = len(elems)
    out = []
    ext = []
    remaining = set(elems)
    def rec():
        if not remaining:
            out.append(tuple(ext)); return
        for v in sorted(remaining):
            if preds[v] <= set(ext):
                ext.append(v); remaining.remove(v)
                rec()
                ext.pop(); remaining.add(v)
    rec()
    return out

def F_and_exts(rel, elems):
    """exact F(P) as Fraction, and number of linear extensions."""
    preds = {v: set() for v in elems}
    for (i, j) in rel:
        if i in preds and j in preds:
            preds[j].add(i)
    exts = linear_extensions(rel, elems)
    tot = Fraction(0)
    for ext in exts:
        pos = {v: t + 1 for t, v in enumerate(ext)}   # 1-based positions
        s = Fraction(0)
        for v in elems:
            p = max([pos[u] for u in preds[v]] + [0])
            r = pos[v] - p - 1
            s += H[r]
        tot += s
    return tot / len(exts), len(exts)

def maximal_elements(rel, elems):
    non_max = {i for (i, j) in rel if i in elems and j in elems}
    return [v for v in elems if v not in non_max]

def check_poset(rel, n, stats):
    elems = list(range(n))
    F, e = F_and_exts(rel, elems)
    lnE = math.log(e)
    Ff = float(F)
    slack_lo = Ff - lnE
    slack_hi = lnE / math.log(2) - Ff
    stats['min_slack_lo'] = min(stats['min_slack_lo'], slack_lo)
    stats['min_slack_hi'] = min(stats['min_slack_hi'], slack_hi)
    if slack_lo < -1e-9 or slack_hi < -1e-9:
        stats['violations'].append((rel, Ff, lnE))

    # Lemma 4 + recursion + insertion identity + log-concavity
    preds = {v: set() for v in elems}
    for (i, j) in rel:
        preds[j].add(i)
    rec_sum = Fraction(0)
    for v in maximal_elements(rel, elems):
        sub_elems = [u for u in elems if u != v]
        sub_rel = frozenset((i, j) for (i, j) in rel if i != v and j != v)
        Fv, ev = F_and_exts(sub_rel, sub_elems)
        exts_v = linear_extensions(sub_rel, sub_elems)
        m = n - 1
        counts = [0] * (m + 1)          # counts[k] = #{tau : L_v(tau) = k}
        cv = Fraction(0)
        for tau in exts_v:
            pos = {u: t + 1 for t, u in enumerate(tau)}
            p = max([pos[u] for u in preds[v]] + [0])
            L = m - p
            counts[L] += 1
            cv += H[L]
        cv /= ev
        # tail sequence a_k * ev = # extensions of P with exactly k elements after v
        tails = [sum(counts[k:]) for k in range(m + 1)]  # integer = ev * a_k
        assert tails[0] == ev
        # monotone (trivially true) and log-concave
        for k in range(1, m):
            if tails[k] ** 2 < tails[k - 1] * tails[k + 1]:
                stats['logcc_violations'].append((rel, v, tails))
        # insertion identity e(P) = sum over tau of (L+1)
        assert sum(tails) == e, (rel, v)
        # Lemma 4 bounds
        ratio = math.log(e / ev)
        lo = float(cv) - ratio
        hi = ratio / math.log(2) - float(cv)
        stats['min_cv_lo'] = min(stats['min_cv_lo'], lo)
        stats['min_cv_hi'] = min(stats['min_cv_hi'], hi)
        if lo < -1e-9 or hi < -1e-9:
            stats['lemma4_violations'].append((rel, v, float(cv), ratio))
        rec_sum += Fraction(ev, e) * (Fv + cv)
    # recursion (14), exact
    assert rec_sum == F, ('recursion failed', rel, rec_sum, F)
    stats['count'] += 1

def run():
    for n in range(1, 7):
        stats = dict(count=0, min_slack_lo=float('inf'), min_slack_hi=float('inf'),
                     min_cv_lo=float('inf'), min_cv_hi=float('inf'),
                     violations=[], lemma4_violations=[], logcc_violations=[])
        for rel in all_posets(n):
            check_poset(rel, n, stats)
        print(f"n={n}: {stats['count']} naturally-labeled posets checked (exhaustive)")
        print(f"   (17) min slack: F-ln e = {stats['min_slack_lo']:.6f}, "
              f"ln e/ln2 - F = {stats['min_slack_hi']:.6f}")
        print(f"   Lemma4 min slack: c_v-ln ratio = {stats['min_cv_lo']:.6f}, "
              f"ratio/ln2 - c_v = {stats['min_cv_hi']:.6f}")
        print(f"   violations: main={len(stats['violations'])} "
              f"lemma4={len(stats['lemma4_violations'])} "
              f"logconcavity={len(stats['logcc_violations'])}")
        assert not stats['violations'] and not stats['lemma4_violations'] \
            and not stats['logcc_violations']

    # random posets n=7,8
    rng = random.Random(12345)
    for n, trials in [(7, 400), (8, 150)]:
        stats = dict(count=0, min_slack_lo=float('inf'), min_slack_hi=float('inf'),
                     min_cv_lo=float('inf'), min_cv_hi=float('inf'),
                     violations=[], lemma4_violations=[], logcc_violations=[])
        for _ in range(trials):
            p = rng.choice([0.1, 0.2, 0.3, 0.5, 0.7])
            rel = random_poset(n, p, rng)
            check_poset(rel, n, stats)
        print(f"n={n}: {stats['count']} random posets checked")
        print(f"   (17) min slack: F-ln e = {stats['min_slack_lo']:.6f}, "
              f"ln e/ln2 - F = {stats['min_slack_hi']:.6f}")
        print(f"   violations: main={len(stats['violations'])} "
              f"lemma4={len(stats['lemma4_violations'])} "
              f"logconcavity={len(stats['logcc_violations'])}")
        assert not stats['violations'] and not stats['lemma4_violations'] \
            and not stats['logcc_violations']
    print("ALL CHECKS PASSED")

if __name__ == '__main__':
    run()
