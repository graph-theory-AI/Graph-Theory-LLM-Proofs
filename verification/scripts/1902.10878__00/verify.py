#!/usr/bin/env python3
"""Referee verification for attack 1902.10878__00.

Claim under review: phi(2/5, 1/4) = 2/5 via an explicit 5-5-4 tripartite graph,
and 2/5 != F_k(2/5,1/4) = (ceil(2k/5)+ceil(k/4)-1)/k for every integer k >= 1.

Also verifies the SOURCE PAPER's own counterexample (intro of arXiv:1902.10878v3,
figure "fig:exactcount"): an 81-vertex graph with psi(13/27,1/9) = 13/27,
which already refutes the same 'wild conjecture' for phi (since
max(x,y) <= phi <= psi and 13/27 is not of the ceiling form).
"""

from fractions import Fraction
from math import ceil
from itertools import count

def check_constrained(A, B, C, edges, x, y):
    """Check (x,y)-constrained via tripartition (A,B,C):
    - A,B,C stable, no A-C edges (we only pass A-B and B-C edges, so automatic;
      but verify no edge endpoints violate this),
    - every a in A has >= x|B| neighbours in B,
    - every b in B has >= y|C| neighbours in C.
    Returns (ok, details)."""
    adj = {v: set() for v in A | B | C}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    # tripartition sanity: stability and no A-C edges
    for u, v in edges:
        sides = []
        for w in (u, v):
            sides.append('A' if w in A else 'B' if w in B else 'C')
        assert set(sides) in ({'A', 'B'}, {'B', 'C'}), f"illegal edge {u}-{v} ({sides})"
    degAB = {a: len(adj[a] & B) for a in A}
    degBC = {b: len(adj[b] & C) for b in B}
    okA = all(Fraction(d) >= x * len(B) for d in degAB.values())
    okB = all(Fraction(d) >= y * len(C) for d in degBC.values())
    # |N^2_A(c)| for each c in C: vertices of A at distance exactly 2
    # (equivalently, sharing a common neighbour; A-C non-adjacent by construction)
    n2 = {}
    for c in C:
        reach = set()
        for b in adj[c] & B:
            reach |= adj[b] & A
        n2[c] = len(reach)
    return okA, okB, degAB, degBC, n2

def F(k, x, y):
    return Fraction(ceil(k * x) + ceil(k * y) - 1, k)

# ---------------------------------------------------------------- writeup graph
x, y = Fraction(2, 5), Fraction(1, 4)
A = {'a1', 'a2', 'a23', 'a24', 'a34'}
B = {'b1', 'bp1', 'b2', 'b3', 'b4'}
C = {'c1', 'c2', 'c3', 'c4'}
edges = [
    ('b1', 'a1'), ('b1', 'a2'), ('bp1', 'a1'), ('bp1', 'a2'),
    ('b2', 'a23'), ('b2', 'a24'),
    ('b3', 'a23'), ('b3', 'a34'),
    ('b4', 'a24'), ('b4', 'a34'),
    ('b1', 'c1'), ('bp1', 'c1'), ('b2', 'c2'), ('b3', 'c3'), ('b4', 'c4'),
]
okA, okB, degAB, degBC, n2 = check_constrained(A, B, C, edges, x, y)
print("=== Writeup construction (|A|,|B|,|C|) =", (len(A), len(B), len(C)))
print("x|B| =", x * len(B), " y|C| =", y * len(C))
print("A-side degree condition holds:", okA, " degrees:", sorted(degAB.values()))
print("B-side degree condition holds:", okB, " degrees:", sorted(degBC.values()))
print("|N^2_A(c)| per c:", {c: n2[c] for c in sorted(C)})
mx = max(n2.values())
print(f"max_c |N^2_A(c)| = {mx}  =>  phi(2/5,1/4) <= {Fraction(mx, len(A))}")
assert okA and okB and Fraction(mx, len(A)) == Fraction(2, 5)

# lower bound phi >= x is the paper's Theorem 1.2 (trivial averaging); so phi = 2/5.
target = Fraction(2, 5)
print("\n=== F_k(2/5,1/4) for k = 1..12:", [str(F(k, x, y)) for k in range(1, 13)])
KMAX = 10**6
mn = min(F(k, x, y) for k in range(1, KMAX + 1))
print(f"min over k=1..{KMAX} of F_k =", mn)
assert mn == Fraction(1, 2)
# rigorous tail: F_k >= x + y - 1/k > 2/5 for all k > 1/(x+y-2/5) = 4
assert all(F(k, x, y) != target for k in range(1, KMAX + 1))
print("F_k == 2/5 for some k <= 10^6:", any(F(k, x, y) == target for k in range(1, KMAX + 1)))
print("Tail bound: for k >= 5, F_k >= x+y-1/k =", x + y - Fraction(1, 5), "> 2/5:",
      x + y - Fraction(1, 5) > target)

# ------------------------------------------- source paper's own counterexample
# Figure fig:exactcount of arXiv:1902.10878v3: blow-up multiplicities
# A row: a1..a3 -> 3, a4,a5 -> 5, a6,a7 -> 4  (total 27)
# B row: b1..b3 -> 3, b4,b5 -> 5, b6,b7 -> 4  (total 27)
# C row: c1..c3 -> 3, c4,c5 -> 5, c6,c7 -> 4  (total 27)
mult = {**{f'a{i}': 3 for i in (1, 2, 3)}, 'a4': 5, 'a5': 5, 'a6': 4, 'a7': 4,
        **{f'b{i}': 3 for i in (1, 2, 3)}, 'b4': 5, 'b5': 5, 'b6': 4, 'b7': 4,
        **{f'c{i}': 3 for i in (1, 2, 3)}, 'c4': 5, 'c5': 5, 'c6': 4, 'c7': 4}
fig_edges = [('a1','b1'),('a2','b2'),('a3','b3'),('a4','b1'),('a4','b2'),('a4','b3'),
             ('a5','b1'),('a5','b2'),('a5','b3'),('a1','b4'),('a2','b4'),('a3','b4'),
             ('a1','b5'),('a2','b5'),('a3','b5'),('a4','b6'),('a5','b7'),('a6','b4'),
             ('a7','b5'),('a6','b6'),('a6','b7'),('a7','b6'),('a7','b7'),
             ('b1','c1'),('b2','c2'),('b3','c3'),('b4','c4'),('b5','c5'),('b6','c6'),('b7','c7')]
def blow(v):
    return {(v, i) for i in range(mult[v])}
A2 = set().union(*[blow(f'a{i}') for i in range(1, 8)])
B2 = set().union(*[blow(f'b{i}') for i in range(1, 8)])
C2 = set().union(*[blow(f'c{i}') for i in range(1, 8)])
edges2 = [(u2, v2) for (u, v) in fig_edges for u2 in blow(u) for v2 in blow(v)]
x2, y2 = Fraction(13, 27), Fraction(1, 9)
okA, okB, degAB, degBC, n2 = check_constrained(A2, B2, C2, edges2, x2, y2)
print("\n=== Source paper's figure example (blow-up): sizes", (len(A2), len(B2), len(C2)))
print("x|B| =", x2 * 27, " y|C| =", y2 * 27)
print("A-side condition holds:", okA, " A->B degrees:", sorted(set(degAB.values())))
print("B-side condition holds:", okB, " B->C degrees:", sorted(set(degBC.values())))
print("|N^2_A(v)| values over C:", sorted(set(n2.values())))
assert okA and okB and set(n2.values()) == {13}
# biconstrained part (paper claims biconstrained):
adj = {v: set() for v in A2 | B2 | C2}
for u, v in edges2:
    adj[u].add(v); adj[v].add(u)
okBA = all(Fraction(len(adj[b] & A2)) >= x2 * 27 for b in B2)
okCB = all(Fraction(len(adj[c] & B2)) >= y2 * 27 for c in C2)
print("biconstrained extra conditions (B->A >= 13, C->B >= 3):", okBA, okCB)
print("=> psi(13/27,1/9) <= 13/27, hence phi(13/27,1/9) = 13/27 (paper Thm 1.2).")
mn2 = min(F(k, x2, y2) for k in range(1, KMAX + 1))
print(f"min over k=1..{KMAX} of F_k(13/27,1/9) =", mn2, " equals 13/27 anywhere:",
      any(F(k, x2, y2) == Fraction(13, 27) for k in range(1, KMAX + 1)))
print("\nAll assertions passed.")
