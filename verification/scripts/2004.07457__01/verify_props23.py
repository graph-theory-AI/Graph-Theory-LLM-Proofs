#!/usr/bin/env python3
"""Sanity checks for Propositions 2 and 3 of attacks/2004.07457__01/output.md.

Prop 2 claims: (k_A-1)/Delta_A + (k_B-1)/Delta_B >= 1 implies every bipartite
graph with the corresponding part-degree bounds is (k_A,k_B)-choosable, via
(a) a Hall-type orientation with d+(a) <= k_A-1, d+(b) <= k_B-1, and
(b) the kernel lemma on bipartite (odd-dicycle-free, hence kernel-perfect)
orientations.

Checks here:
A. Orientation existence: for every bipartite graph on parts of size <= 4
   and every (k_A,k_B,Delta_A,Delta_B) with the actual max part degrees and
   k_A-1 + (k_B-1)*Delta_A/Delta_B >= Delta_A (condition (1) scaled), verify
   by max-flow that an orientation with d+(a) <= k_A-1, d+(b) <= k_B-1 exists.
B. Choosability at the boundary k_A + k_B = Delta + 2, Delta = 2:
   exhaustively verify (2,2)-choosability of C_4, C_6, P_5 over all list
   assignments from universes of size up to 6.
C. Choosability at the boundary Delta = 3: verify (2,3)- and (3,2)-
   choosability of K_{3,3} over all list assignments from a universe of
   size 5, and random assignments from a universe of size 9.
D. Prop 3 numeric example: over a parameter grid, check that
   k_A >= (1+eta)Delta_B and k_B >= (1+log(Delta_B(Delta_A-1)+1))/log(1+eta)
   imply e(Delta_B(Delta_A-1)+1)(Delta_B/k_A)^{k_B} <= 1.
"""
import itertools
import math
import random


def is_L_colourable(edges, lists):
    verts = sorted(lists)
    def bt(i, col):
        if i == len(verts):
            return True
        v = verts[i]
        nbrs = [u for e in edges for u in e if v in e and u != v]
        for c in lists[v]:
            if all(col.get(u) != c for u in nbrs):
                col[v] = c
                if bt(i + 1, col):
                    return True
                del col[v]
        return False
    return bt(0, {})


# ---- A. orientation existence via max-flow ---------------------------------
def orientation_exists(edges, capA, capB):
    """Match each edge to one endpoint, vertex a used <= capA times, b <= capB
    times (bipartite matching edges -> capacity slots, augmenting paths)."""
    slots = []
    for a in {a for a, _ in edges}:
        slots += [("A", a, t) for t in range(capA)]
    for b in {_b for _, _b in edges}:
        slots += [("B", b, t) for t in range(capB)]
    adj = [[i for i, s in enumerate(slots)
            if (s[0] == "A" and s[1] == a) or (s[0] == "B" and s[1] == b)]
           for a, b in edges]
    match = [-1] * len(slots)  # slot -> edge index

    def augment(e, seen):
        for s in adj[e]:
            if s in seen:
                continue
            seen.add(s)
            if match[s] == -1 or augment(match[s], seen):
                match[s] = e
                return True
        return False

    return all(augment(e, set()) for e in range(len(edges)))


tested = 0
for nA, nB in [(2, 2), (3, 3), (4, 4), (4, 3)]:
    pairs = [(i, j) for i in range(nA) for j in range(nB)]
    for _ in range(300):
        m = random.randint(1, len(pairs))
        edges = random.sample(pairs, m)
        DA = max(sum(1 for a, _ in edges if a == i) for i in range(nA))
        DB = max(sum(1 for _, b in edges if b == j) for j in range(nB))
        if DA == 0 or DB == 0:
            continue
        for kA in range(1, DA + 2):
            for kB in range(1, DB + 2):
                if (kA - 1) / DA + (kB - 1) / DB >= 1:
                    assert orientation_exists(edges, kA - 1, kB - 1), (edges, kA, kB)
                    tested += 1
print(f"A. Orientation with d+(a)<=k_A-1, d+(b)<=k_B-1 exists in all {tested} "
      "random instances satisfying condition (1). OK")

# ---- B. exhaustive (2,2)-choosability, Delta = 2 ---------------------------
def check_choosable_exhaustive(edges, A, B, kA, kB, universe):
    for a_lists in itertools.product(itertools.combinations(universe, kA), repeat=len(A)):
        for b_lists in itertools.product(itertools.combinations(universe, kB), repeat=len(B)):
            lists = {a: set(L) for a, L in zip(A, a_lists)}
            lists.update({b: set(L) for b, L in zip(B, b_lists)})
            if not is_L_colourable(edges, lists):
                return lists
    return None


graphs = {
    "C_4": ([("a0", "b0"), ("b0", "a1"), ("a1", "b1"), ("b1", "a0")],
            ["a0", "a1"], ["b0", "b1"]),
    "P_5": ([("a0", "b0"), ("b0", "a1"), ("a1", "b1")],
            ["a0", "a1"], ["b0", "b1"]),
    "C_6": ([("a0", "b0"), ("b0", "a1"), ("a1", "b1"), ("b1", "a2"), ("a2", "b2"), ("b2", "a0")],
            ["a0", "a1", "a2"], ["b0", "b1", "b2"]),
}
for name, (edges, A, B) in graphs.items():
    for U in (4, 5, 6):
        bad = check_choosable_exhaustive(edges, A, B, 2, 2, list(range(U)))
        assert bad is None, (name, U, bad)
print("B. C_4, P_5, C_6 are (2,2)-choosable over all lists from universes of "
      "size 4-6 (boundary k_A+k_B = Delta+2 with Delta=2). OK")

# ---- C. K_{3,3}, Delta = 3, (2,3) and (3,2) --------------------------------
edges33 = [(f"a{i}", f"b{j}") for i in range(3) for j in range(3)]
A33 = [f"a{i}" for i in range(3)]
B33 = [f"b{j}" for j in range(3)]
for kA, kB in [(2, 3), (3, 2)]:
    bad = check_choosable_exhaustive(edges33, A33, B33, kA, kB, list(range(5)))
    assert bad is None, (kA, kB, bad)
    for _ in range(20000):
        lists = {a: set(random.sample(range(9), kA)) for a in A33}
        lists.update({b: set(random.sample(range(9), kB)) for b in B33})
        assert is_L_colourable(edges33, lists), lists
print("C. K_{3,3} is (2,3)- and (3,2)-list-colourable for all lists from a "
      "universe of size 5 and 20000 random 9-colour lists each. OK")

# ---- D. Prop 3 numeric example ---------------------------------------------
cnt = 0
for eta in (0.1, 0.5, 1.0, 3.0):
    for DB in (2, 5, 20, 100):
        for DA in (2, 5, 20, 100):
            kA = math.ceil((1 + eta) * DB)
            kB = math.ceil((1 + math.log(DB * (DA - 1) + 1)) / math.log(1 + eta))
            lhs = math.e * (DB * (DA - 1) + 1) * (DB / kA) ** kB
            assert lhs <= 1 + 1e-12, (eta, DB, DA, lhs)
            cnt += 1
print(f"D. Prop 3 example inequality verified on {cnt} parameter tuples. OK")
print("ALL CHECKS PASSED")
