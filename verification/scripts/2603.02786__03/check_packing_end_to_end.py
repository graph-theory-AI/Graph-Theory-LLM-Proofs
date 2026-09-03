#!/usr/bin/env python3
"""End-to-end check of the writeup's counting machinery on real tight packings.

Build tight disjoint packings of B_d = {d,...,nd} (d = 1..k) by first-fit /
random-fit (numpy: compute the exact forbidden-shift set for each progression),
then verify on the actual object, with L = k^2:
  (a) Lemma 1: for every pair d != e with alpha_d == alpha_e mod gcd(d,e),
      cores are disjoint;
  (b) prime cores C_p pairwise disjoint;
  (c) Lemma 2: pointwise weighted multiplicity N(x) <= 1 (exact Fractions);
  (d) master inequality W >= |U| + T - int_U N.
k = 35 so all three families {2p, 3p, 5p} (p > 5) are nonempty:
  2p: p in {7,11,13,17}; 3p: p in {7,11}; 5p: p = 7.
Tight packings force many hull/core overlaps, exercising the lemmas.
"""
import numpy as np
from fractions import Fraction
from math import gcd

K = 35
N = 500           # (N-1)*7 = 3493 > 2*K^2 = 2450 so C_7 nonempty
L = K * K         # 1225

PRIMES = [p for p in range(2, K + 1) if all(p % q for q in range(2, p))]
FAMILIES = {a: [p for p in PRIMES if p > 5 and a * p <= K] for a in (2, 3, 5)}
LAM = {2: Fraction(1, 2), 3: Fraction(1, 3), 5: Fraction(1, 6)}

def build_packing(rng, mode, order):
    """Greedy packing. mode 'first' = smallest feasible shift; 'random' = random
    choice among the 2000 smallest feasible shifts."""
    CAP = 400000
    occ = np.zeros(0, dtype=np.int64)
    alpha = {}
    for d in order:
        pts = np.arange(1, N + 1, dtype=np.int64) * d
        if len(occ):
            diffs = (occ[:, None] - pts[None, :]).ravel()
            diffs = diffs[(diffs >= 0) & (diffs < CAP)]
            forb = np.zeros(CAP, dtype=bool)
            forb[diffs] = True
            free = np.nonzero(~forb)[0]
        else:
            free = np.arange(CAP)
        if mode == 'first':
            a = int(free[0])
        else:
            a = int(rng.choice(free[:2000]))
        alpha[d] = a          # alpha_d = position of first element (a + d ... use a as offset)
        occ = np.concatenate([occ, a + pts])
    # explicit disjointness verification
    assert len(np.unique(occ)) == len(occ), "PACKING NOT DISJOINT"
    W = int(occ.max() - occ.min() + 1)
    # alpha in writeup notation = first element of P_d
    first = {d: alpha[d] + d for d in order}
    return first, W

def core(d, a1):
    """Core interval given first element a1 of P_d."""
    lo, hi = a1 + L, a1 + (N - 1) * d - L
    return (lo, hi) if lo <= hi else None

def run_trial(t, first, W, label):
    ok = True
    # (a) Lemma 1 on the actual packing
    lemma1_pairs = 0
    for d in range(1, K + 1):
        for e in range(d + 1, K + 1):
            g = gcd(d, e)
            if (first[d] - first[e]) % g == 0:
                cd, ce = core(d, first[d]), core(e, first[e])
                if cd and ce and max(cd[0], ce[0]) <= min(cd[1], ce[1]):
                    print(f"  LEMMA 1 VIOLATED for d={d}, e={e}")
                    ok = False
                lemma1_pairs += 1
    # (b) prime cores pairwise disjoint
    pc = {p: core(p, first[p]) for p in PRIMES}
    plist = [p for p in PRIMES if pc[p]]
    for i, p in enumerate(plist):
        for q in plist[i + 1:]:
            if max(pc[p][0], pc[q][0]) <= min(pc[p][1], pc[q][1]):
                print(f"  PRIME CORES OVERLAP: p={p}, q={q}")
                ok = False
    # (c) N(x) <= 1 pointwise
    events = []
    n_core_overlaps = 0
    fam_cores = []
    for a, ps in FAMILIES.items():
        for p in ps:
            c = core(a * p, first[a * p])
            if c:
                fam_cores.append((a, p, c))
                events.append((c[0], LAM[a]))
                events.append((c[1] + 1, -LAM[a]))
    for i in range(len(fam_cores)):
        for j in range(i + 1, len(fam_cores)):
            c1, c2 = fam_cores[i][2], fam_cores[j][2]
            if max(c1[0], c2[0]) <= min(c1[1], c2[1]):
                n_core_overlaps += 1
    events.sort()
    cur = Fraction(0); maxN = Fraction(0)
    for _, delta in events:
        cur += delta
        maxN = max(maxN, cur)
    if maxN > 1:
        print(f"  LEMMA 2 VIOLATED, max N = {maxN}")
        ok = False
    # (d) master inequality (integer-point counting)
    U = np.zeros(0, dtype=np.int64)
    for p in plist:
        U = np.concatenate([U, np.arange(pc[p][0], pc[p][1] + 1)])
    Uset = set(U.tolist())
    T = Fraction(0); intUN = Fraction(0)
    for a, p, c in fam_cores:
        size = c[1] - c[0] + 1
        T += LAM[a] * size
        inter = sum(1 for x in range(c[0], c[1] + 1) if x in Uset)
        intUN += LAM[a] * inter
    rhs = len(Uset) + T - intUN
    if W < rhs:
        print(f"  MASTER INEQUALITY VIOLATED: W = {W} < {float(rhs):.1f}")
        ok = False
    print(f"trial {t} ({label}): W = {W}, congruent pairs checked = {lemma1_pairs}, "
          f"family-core overlapping pairs = {n_core_overlaps}, max N = {maxN}, "
          f"|U| = {len(Uset)}, T = {float(T):.1f}, int_U N = {float(intUN):.1f}, "
          f"W >= |U|+T-int_U N = {float(rhs):.1f}: {W >= rhs}  -> {'OK' if ok else 'FAIL'}")
    return ok

def main():
    rng = np.random.default_rng(2026)
    all_ok = True
    trials = []
    trials.append(('first-fit dec', 'first', sorted(range(1, K + 1), reverse=True)))
    trials.append(('first-fit inc', 'first', list(range(1, K + 1))))
    for i in range(4):
        order = list(range(1, K + 1))
        rng.shuffle(order)
        trials.append((f'random-fit #{i}', 'random', order))
    for t, (label, mode, order) in enumerate(trials):
        first, W = build_packing(rng, mode, order)
        all_ok &= run_trial(t, first, W, label)
    print("\nALL TRIALS PASSED" if all_ok else "\nFAILURE DETECTED")

if __name__ == "__main__":
    main()
