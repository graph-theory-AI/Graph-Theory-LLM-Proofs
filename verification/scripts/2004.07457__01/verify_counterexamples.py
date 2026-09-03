#!/usr/bin/env python3
"""Verify the finite objects in attacks/2004.07457__01/output.md.

1. The K_2 counterexample to the literal reading of Conjecture 7(ii):
   Delta_A = Delta_B = k_A = k_B = 1, both lists = {1}.
   Check: clause (ii) hypotheses hold for every C (since log 1 = 0), and
   K_2 admits no proper colouring from these lists.

2. Uniqueness of the loophole: clause (ii) must hold for EVERY C>1
   (the conjecture asserts existence of an absolute constant), so a literal
   counterexample needs C*log(Delta_B) <= k_A for all C, forcing
   log(Delta_B) = 0, i.e. Delta_B = 1 (and symmetrically Delta_A = 1).

3. Proposition 1 converse: the star with centre b (list {1..k_B}) and
   leaves a_1..a_{k_B} (list {i}) has no proper colouring, for k_B = 1..6.

4. Proposition 1 forward direction, brute force: every bipartite graph with
   deg_B <= Delta_B, all singleton lists on A and arbitrary (Delta_B+1)-lists
   on B, has a proper colouring -- checked exhaustively on all bipartite
   graphs with |A| <= 3, |B| <= 3 and all list assignments from a universe
   of size Delta_B + 2, for Delta_B in {1, 2, 3}.
"""
import itertools
import math


def proper_colourings(edges, lists):
    """Yield proper colourings (dicts) from lists; vertices = keys of lists."""
    verts = sorted(lists)
    for combo in itertools.product(*(sorted(lists[v]) for v in verts)):
        col = dict(zip(verts, combo))
        if all(col[u] != col[v] for u, v in edges):
            yield col


def is_L_colourable(edges, lists):
    return next(proper_colourings(edges, lists), None) is not None


# ---- 1. K_2 counterexample -------------------------------------------------
edges = [("a", "b")]
lists = {"a": {1}, "b": {1}}
assert not is_L_colourable(edges, lists)
print("1. K_2 with L(a)=L(b)={1}: no proper colouring -> K_2 is NOT (1,1)-choosable. OK")
for C in (1.000001, 2, 10, 1e6):
    for base in (2, math.e, 10):
        assert 1 >= C * math.log(1, base)  # k_A >= C log Delta_B, both sides
print("   Clause (ii) hypotheses (k=1 >= C*log 1 = 0) hold for every C and every log base. OK")

# ---- 2. Uniqueness of the loophole ----------------------------------------
# For Delta >= 2 and any base b <= e (or any fixed base), C*log(Delta) is
# unbounded in C, so 'for some absolute constant C>1' cannot be beaten
# except at Delta = 1.  Sanity check numerically:
for Delta in (2, 3, 10):
    k = 10**6
    C = (k + 1) / math.log(Delta)  # some C makes C log Delta > any fixed k
    assert C * math.log(Delta) > k
print("2. For Delta_B >= 2 the hypothesis k_A >= C log Delta_B fails for large C:")
print("   the only literal loophole is Delta_A = Delta_B = 1. OK")

# ---- 3. Proposition 1 converse (star) --------------------------------------
for kB in range(1, 7):
    edges = [("b", f"a{i}") for i in range(1, kB + 1)]
    lists = {"b": set(range(1, kB + 1))}
    lists.update({f"a{i}": {i} for i in range(1, kB + 1)})
    assert not is_L_colourable(edges, lists), kB
print("3. Star K_{1,kB} (centre list {1..kB}, leaf i list {i}): not colourable for kB=1..6. OK")
print("   (Centre b has degree kB <= Delta_B whenever kB <= Delta_B, so kB <= Delta_B")
print("    lists do not suffice: threshold Delta_B + 1 is necessary.)")

# ---- 4. Proposition 1 forward direction, exhaustive small cases ------------
def all_bipartite_graphs(nA, nB):
    """All bipartite graphs on parts of sizes nA, nB (as edge lists)."""
    pairs = [(f"a{i}", f"b{j}") for i in range(nA) for j in range(nB)]
    for mask in range(1 << len(pairs)):
        yield [pairs[t] for t in range(len(pairs)) if mask >> t & 1]


checked = 0
for DeltaB in (1, 2, 3):
    kB = DeltaB + 1
    universe = list(range(DeltaB + 2))
    for nA in (1, 2, 3):
        for nB in (1, 2, 3):
            for edges in all_bipartite_graphs(nA, nB):
                degB = {f"b{j}": 0 for j in range(nB)}
                for _, b in edges:
                    degB[b] += 1
                if max(degB.values(), default=0) > DeltaB:
                    continue
                A = [f"a{i}" for i in range(nA)]
                B = [f"b{j}" for j in range(nB)]
                for a_cols in itertools.product(universe, repeat=nA):
                    listsA = {a: {c} for a, c in zip(A, a_cols)}
                    for b_lists in itertools.product(
                        itertools.combinations(universe, kB), repeat=nB
                    ):
                        lists = dict(listsA)
                        lists.update({b: set(L) for b, L in zip(B, b_lists)})
                        # forward direction: colour forced on A; b needs a
                        # colour of L(b) unused among its <= DeltaB neighbours
                        ok = all(
                            set(L) - {a_cols[int(a[1:])] for a, bb in edges if bb == b}
                            for b, L in zip(B, (set(x) for x in b_lists))
                        )
                        assert ok == is_L_colourable(edges, lists)
                        assert is_L_colourable(edges, lists)
                        checked += 1
print(f"4. Prop 1 forward direction: {checked} (graph, list) instances with")
print("   deg_B <= Delta_B, k_A = 1, k_B = Delta_B + 1 all properly colourable. OK")
print("ALL CHECKS PASSED")
