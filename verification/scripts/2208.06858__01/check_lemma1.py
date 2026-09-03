"""Exhaustive check of Lemma 1 (balancing a monotone family) on {0,1}^4.

Lemma 1 claims: for any upward-closed F on {0,1}^n there is a balanced
upward-closed A with F <= A (if |F| <= 2^{n-1}) or A <= F (if |F| >= 2^{n-1}),
obtained greedily by adding inclusion-maximal elements of the complement /
removing inclusion-minimal elements of F, and mu(F symdiff A) = |mu(F)-1/2|.

We enumerate ALL upward-closed subsets of {0,1}^4 (there are Dedekind(4)=168)
and verify the greedy construction on each.
"""
import itertools

n = 4
PTS = list(range(1 << n))


def leq(x, y):
    """x <= y coordinatewise (as bitmasks)."""
    return (x & y) == x


def is_upclosed(S):
    return all((y in S) for x in S for y in PTS if leq(x, y))


# enumerate all upward-closed families (2^16 subsets, filter)
up_families = []
for mask in range(1 << (1 << n)):
    S = frozenset(i for i in PTS if (mask >> i) & 1)
    if is_upclosed(S):
        up_families.append(S)

print(f"n={n}: number of upward-closed families = {len(up_families)} (Dedekind(4)=168 expected)")
assert len(up_families) == 168

half = 1 << (n - 1)


def balance(F):
    """Greedy Lemma-1 balancing with a fixed tie-break (numeric order)."""
    A = set(F)
    while len(A) < half:
        # inclusion-maximal elements of the complement
        comp = [x for x in PTS if x not in A]
        maximal = [x for x in comp if not any(leq(x, y) and x != y for y in comp)]
        A.add(min(maximal))  # deterministic tie-break
    while len(A) > half:
        minimal = [x for x in A if not any(leq(y, x) and x != y for y in A)]
        A.remove(min(minimal))
    return frozenset(A)


bad = 0
for F in up_families:
    A = balance(F)
    ok_size = len(A) == half
    ok_mono = is_upclosed(A)
    ok_nested = (F <= A) if len(F) <= half else (A <= F)
    symdiff = len(F ^ A)
    ok_sym = symdiff == abs(len(F) - half)
    if not (ok_size and ok_mono and ok_nested and ok_sym):
        bad += 1
        print("FAIL", sorted(F))
print(f"checked {len(up_families)} monotone families: failures = {bad}")
assert bad == 0
print("Lemma 1 VERIFIED exhaustively on {0,1}^4.")
