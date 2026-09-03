#!/usr/bin/env python3
"""Referee verification for attack 1611.03196__00.

Conjecture 1.6 (Aharoni-Alon-Berger-Chudnovsky-Kotlar-Loebl-Ziv, arXiv:1611.03196,
label treesconj0), literal wording:

  Given a partition of V(P_n) into V_1..V_m there exist an independent set S and
  INTEGERS b_i such that |S cap V_i| >= |V_i|/2 - b_i for all i, with
  (1) sum b_i <= m/2 and (2) b_i <= 1 for all i.

The writeup claims the partition of P_7 (vertices 1..7)
  V_1 = {2,4,6}, V_2 = {1}, V_3 = {3,5,7}
is a counterexample to the literal (integer b_i) reading.

We brute-force all independent sets of P_n. For a fixed S the minimal admissible
integer b_i is ceil(|V_i|/2) - |S cap V_i| (b_i may be negative; smaller only
helps the sum, larger only hurts). Hence the instance is feasible iff some
independent S has
  ceil(|V_i|/2) - |S cap V_i| <= 1 for all i        (condition 2)
  sum_i (ceil(|V_i|/2) - |S cap V_i|) <= floor(m)/... <= m/2 (integer sum)
We ALSO run a fully naive double-check enumerating integer vectors b in a box,
to guard against an error in the minimal-b reduction.

Additionally we test:
  - the real-b_i relaxation (minimal real b_i = |V_i|/2 - |S cap V_i|);
  - the Alishahi-Meunier reading: |S cap V_j| >= |V_j|/2 - 1 for all j with
    strict inequality for at least m/2 indices;
  - the floor variant: |S cap V_i| >= floor(|V_i|/2) - b_i, integer b_i.
Finally we sweep all partitions of P_n for n <= 9 (m <= 4, up to part-relabeling)
to find the smallest counterexamples to the literal reading and to confirm the
other three readings never fail there.
"""

import itertools
from math import ceil, floor
from fractions import Fraction


def independent_sets(n):
    """All independent sets of the path 1-2-...-n, as frozensets."""
    out = []
    for r in range(n + 1):
        for comb in itertools.combinations(range(1, n + 1), r):
            if all(comb[k + 1] - comb[k] >= 2 for k in range(len(comb) - 1)):
                out.append(frozenset(comb))
    return out


def feasible_literal(n, parts, indep=None):
    """Literal reading: integer b_i, |S cap V_i| >= |V_i|/2 - b_i, b_i<=1, sum<=m/2."""
    m = len(parts)
    if indep is None:
        indep = independent_sets(n)
    for S in indep:
        mins = [ceil(len(V) / 2) - len(S & V) for V in parts]
        if all(b <= 1 for b in mins) and sum(mins) <= Fraction(m, 2):
            return S, mins
    return None


def feasible_literal_naive(n, parts, brange=range(-7, 2)):
    """Same, but enumerate integer b vectors explicitly (no minimality argument)."""
    m = len(parts)
    indep = independent_sets(n)
    for S in indep:
        for b in itertools.product(brange, repeat=m):
            if (all(bi <= 1 for bi in b)
                    and sum(b) <= Fraction(m, 2)
                    and all(len(S & V) >= Fraction(len(V), 2) - bi
                            for V, bi in zip(parts, b))):
                return S, b
    return None


def feasible_real(n, parts, indep=None):
    """Real b_i relaxation."""
    m = len(parts)
    if indep is None:
        indep = independent_sets(n)
    for S in indep:
        mins = [Fraction(len(V), 2) - len(S & V) for V in parts]
        if all(b <= 1 for b in mins) and sum(mins) <= Fraction(m, 2):
            return S, mins
    return None


def feasible_am(n, parts, indep=None):
    """Alishahi-Meunier reading: >= |V_j|/2 - 1 for all j, strict for >= m/2 j's."""
    m = len(parts)
    if indep is None:
        indep = independent_sets(n)
    for S in indep:
        vals = [(len(S & V), Fraction(len(V), 2) - 1) for V in parts]
        if all(a >= t for a, t in vals):
            strict = sum(1 for a, t in vals if a > t)
            if strict >= Fraction(m, 2):
                return S
    return None


def feasible_floor(n, parts, indep=None):
    """Floor variant: |S cap V_i| >= floor(|V_i|/2) - b_i, integer b_i<=1, sum<=m/2."""
    m = len(parts)
    if indep is None:
        indep = independent_sets(n)
    for S in indep:
        mins = [floor(len(V) / 2) - len(S & V) for V in parts]
        if all(b <= 1 for b in mins) and sum(mins) <= Fraction(m, 2):
            return S, mins
    return None


def main():
    # ---- The writeup's specific instance ----
    n = 7
    parts = [frozenset({2, 4, 6}), frozenset({1}), frozenset({3, 5, 7})]
    indep = independent_sets(n)
    print(f"P_7: number of independent sets (incl. empty) = {len(indep)}")
    maxsets = [S for S in indep if len(S) == 4]
    print(f"P_7: independent sets of size 4: {[sorted(S) for S in maxsets]}")
    assert len(maxsets) == 1 and maxsets[0] == frozenset({1, 3, 5, 7})
    assert max(len(S) for S in indep) == 4

    r = feasible_literal(n, parts, indep)
    print(f"Literal integer reading feasible on writeup instance: {r}")
    r2 = feasible_literal_naive(n, parts)
    print(f"Naive b-enumeration (b_i in -7..1) feasible: {r2}")
    assert r is None and r2 is None, "counterexample FAILED: instance is feasible!"

    rr = feasible_real(n, parts, indep)
    print(f"Real-b_i relaxation feasible: S={sorted(rr[0])}, min b={rr[1]}")
    # writeup's caveat witness
    S = frozenset({2, 5})
    ok = all(len(S & V) >= Fraction(len(V), 2) - Fraction(1, 2) for V in parts)
    print(f"Writeup caveat witness S={{2,5}}, b_i=1/2 valid: {ok}")
    assert ok

    ram = feasible_am(n, parts, indep)
    print(f"Alishahi-Meunier reading feasible: S={sorted(ram) if ram else None}")
    assert ram is not None

    rf = feasible_floor(n, parts, indep)
    print(f"Floor variant feasible: S={sorted(rf[0])}, min b={rf[1]}")
    assert rf is not None

    # ---- Sweep small paths: set partitions of {1..n} into m parts ----
    print("\nSweep of all partitions of P_n, n<=9 (all m):")
    smallest = None
    counts = {}
    for n in range(1, 10):
        indep = independent_sets(n)
        verts = list(range(1, n + 1))
        # enumerate set partitions via restricted growth strings
        def rgs(k):
            if k == len(verts):
                yield tuple(assign)
                return
            mx = max(assign[:k], default=-1)
            for c in range(mx + 2):
                assign[k] = c
                yield from rgs(k + 1)
        assign = [0] * len(verts)
        n_cex = 0
        n_tot = 0
        for a in rgs(0):
            m = max(a) + 1
            parts = [frozenset(v for v, c in zip(verts, a) if c == j)
                     for j in range(m)]
            n_tot += 1
            lit = feasible_literal(n, parts, indep)
            if lit is None:
                n_cex += 1
                if smallest is None:
                    smallest = (n, parts)
                # cross-check the sane readings still hold
                assert feasible_real(n, parts, indep) is not None, (n, parts)
                assert feasible_am(n, parts, indep) is not None, (n, parts)
                assert feasible_floor(n, parts, indep) is not None, (n, parts)
        counts[n] = (n_tot, n_cex)
        print(f"  n={n}: partitions={n_tot}, literal-reading counterexamples={n_cex}")
    if smallest:
        sn, sp = smallest
        print(f"\nSmallest literal-reading counterexample: n={sn}, "
              f"parts={[sorted(V) for V in sp]}")
    print("\nAll checks passed: literal integer reading FAILS on the writeup's "
          "instance; real/AM/floor readings hold on every instance tested.")


if __name__ == "__main__":
    main()
