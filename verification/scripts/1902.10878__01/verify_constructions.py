#!/usr/bin/env python3
"""Verification of the two explicit constructions in attacks/1902.10878__01/output.md.

Definitions (arXiv:1902.10878, v3):
  A tripartition (A,B,C): partition of V(G) into nonempty stable sets.
  (x,y)-constrained via (A,B,C):
    - every a in A has >= x|B| neighbours in B,
    - every b in B has >= y|C| neighbours in C,
    - no edges between A and C.
  (x,y)-biconstrained: additionally
    - every b in B has >= x|A| neighbours in A,
    - every c in C has >= y|B| neighbours in B.
  N^2_A(v) = vertices of A at distance exactly 2 from v.
  psi(x,y) = max z s.t. every (x,y)-biconstrained G has some v in C
             with |N^2_A(v)| >= z|A|.

Checks:
 1. For odd q in {7,9,11}: the section-3 construction is (2/q,(q-2)/q)-
    biconstrained and every c in C reaches exactly |A|-(q-2) vertices of A,
    giving psi(2/q,(q-2)/q) <= 1 - 2(q-2)/(q(q+1)); for q=7 this is 23/28.
 2. For odd q in {3,...,13}: the cyclic construction is ((q-2)/q,2/q)-
    biconstrained and every c reaches exactly q-1 vertices of A, giving
    psi((q-2)/q,2/q) <= 1-1/q  (upper bound of the writeup's lemma).
"""
from fractions import Fraction
from itertools import combinations


def check_biconstrained(x, y, A, B, C, adjAB, adjBC):
    """adjAB: dict a -> set of B-neighbours; adjBC: dict b -> set of C-neighbours.
    Returns list of violation strings (empty if biconstrained)."""
    bad = []
    nA, nB, nC = len(A), len(B), len(C)
    # a-side: >= x|B| neighbours in B
    for a in A:
        if Fraction(len(adjAB[a])) < x * nB:
            bad.append(f"A-vertex {a}: degB={len(adjAB[a])} < x|B|={x*nB}")
    # b-side towards A: >= x|A|
    for b in B:
        d = sum(1 for a in A if b in adjAB[a])
        if Fraction(d) < x * nA:
            bad.append(f"B-vertex {b}: degA={d} < x|A|={x*nA}")
    # b-side towards C: >= y|C|
    for b in B:
        if Fraction(len(adjBC[b])) < y * nC:
            bad.append(f"B-vertex {b}: degC={len(adjBC[b])} < y|C|={y*nC}")
    # c-side: >= y|B|
    for c in C:
        d = sum(1 for b in B if c in adjBC[b])
        if Fraction(d) < y * nB:
            bad.append(f"C-vertex {c}: degB={d} < y|B|={y*nB}")
    return bad


def second_neighbourhood_sizes(A, B, C, adjAB, adjBC):
    """|N^2_A(c)| for each c: a in A with a common B-neighbour with c.
    (No A-C edges and A,B,C stable, so distance exactly 2 <=> common B-neighbour.)"""
    NB_of_c = {c: {b for b in B if c in adjBC[b]} for c in C}
    out = {}
    for c in C:
        out[c] = sum(1 for a in A if adjAB[a] & NB_of_c[c])
    return out


def build_section3(q):
    """Asymmetric construction of section 3 for odd q >= 7."""
    h = (q - 3) // 2
    m = h + 3
    # B: pairs P_1..P_h are elements (i,0),(i,1); plus r12,r13,r23
    B = [("p", i, j) for i in range(1, h + 1) for j in (0, 1)] + [
        ("r", 12), ("r", 13), ("r", 23)]
    S = {}
    for i in range(1, h + 1):
        S[i] = {("p", i, 0), ("p", i, 1)}
    S[h + 1] = {("r", 12), ("r", 13)}
    S[h + 2] = {("r", 12), ("r", 23)}
    S[h + 3] = {("r", 13), ("r", 23)}
    assert len({frozenset(s) for s in S.values()}) == m  # all distinct
    # A: q-2 vertices of each type i (neighbourhood S_i), plus 3 universal
    A = [("a", i, t) for i in range(1, m + 1) for t in range(q - 2)] + [
        ("u", t) for t in range(3)]
    adjAB = {}
    for i in range(1, m + 1):
        for t in range(q - 2):
            adjAB[("a", i, t)] = set(S[i])
    for t in range(3):
        adjAB[("u", t)] = set(B)
    # C: two vertices of each type 1..h, one of each type h+1..h+3;
    # type-i vertex has N_B = B \ S_i
    C = [("c", i, t) for i in range(1, h + 1) for t in range(2)] + [
        ("c", i, 0) for i in range(h + 1, m + 1)]
    NB_c = {c: set(B) - S[c[1]] for c in C}
    adjBC = {b: {c for c in C if b in NB_c[c]} for b in B}
    return A, B, C, adjAB, adjBC


def build_cyclic(q):
    """Cyclic construction of section 2 (lemma upper bound) for odd q >= 3."""
    B = list(range(q))
    S = {i: {i % q, (i + 1) % q} for i in range(q)}
    A = [("a", i) for i in range(q)]
    adjAB = {("a", i): set(B) - S[i] for i in range(q)}
    C = [("c", i) for i in range(q)]
    NB_c = {("c", i): set(S[i]) for i in range(q)}
    adjBC = {b: {c for c in C if b in NB_c[c]} for b in B}
    return A, B, C, adjAB, adjBC


def main():
    ok = True
    print("=== Section 3 construction: psi(2/q,(q-2)/q) <= 1 - 2(q-2)/(q(q+1)) ===")
    for q in (7, 9, 11):
        x, y = Fraction(2, q), Fraction(q - 2, q)
        A, B, C, adjAB, adjBC = build_section3(q)
        assert len(B) == q and len(C) == q and len(A) == q * (q + 1) // 2, \
            (len(A), len(B), len(C))
        bad = check_biconstrained(x, y, A, B, C, adjAB, adjBC)
        n2 = second_neighbourhood_sizes(A, B, C, adjAB, adjBC)
        mx = max(n2.values())
        target = len(A) - (q - 2)
        claimed = 1 - Fraction(2 * (q - 2), q * (q + 1))
        print(f"q={q}: |A|={len(A)} |B|={len(B)} |C|={len(C)} "
              f"biconstrained={'YES' if not bad else 'NO'} "
              f"|N2_A(c)| values={sorted(set(n2.values()))} "
              f"max={mx} (expected {target}) "
              f"max/|A|={Fraction(mx, len(A))} (claimed {claimed})")
        if bad:
            ok = False
            for msg in bad:
                print("  VIOLATION:", msg)
        if mx != target or Fraction(mx, len(A)) != claimed:
            ok = False
            print("  MISMATCH in second neighbourhood sizes")

    print()
    print("=== Cyclic construction: psi((q-2)/q,2/q) <= 1 - 1/q ===")
    for q in (3, 5, 7, 9, 11, 13):
        x, y = Fraction(q - 2, q), Fraction(2, q)
        A, B, C, adjAB, adjBC = build_cyclic(q)
        bad = check_biconstrained(x, y, A, B, C, adjAB, adjBC)
        n2 = second_neighbourhood_sizes(A, B, C, adjAB, adjBC)
        vals = sorted(set(n2.values()))
        print(f"q={q}: biconstrained={'YES' if not bad else 'NO'} "
              f"|N2_A(c)| values={vals} (expected [q-1]={q-1}) "
              f"max/|A|={Fraction(max(n2.values()), len(A))} (claimed {Fraction(q-1,q)})")
        if bad:
            ok = False
            for msg in bad:
                print("  VIOLATION:", msg)
        if vals != [q - 1]:
            ok = False
            print("  MISMATCH")

    print()
    print("=== q=7 headline numbers ===")
    A, B, C, adjAB, adjBC = build_section3(7)
    n2 = second_neighbourhood_sizes(A, B, C, adjAB, adjBC)
    print(f"|A|=28, every c reaches {sorted(set(n2.values()))} vertices of A "
          f"-> psi(2/7,5/7) <= 23/28 = {Fraction(23,28)} < 6/7 = {Fraction(6,7)}")
    print()
    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")


if __name__ == "__main__":
    main()
