#!/usr/bin/env python3
"""Verification for 2307.15048__00.

The writeup's counterexample rests on a single finite claim:
    chi_DP(E_n) = 1 for every nonempty edgeless graph E_n,
i.e. every 1-fold correspondence (DP) cover of an edgeless graph admits an
independent transversal.

We verify this by brute force with a fully generic DP-colorability checker:
G is ell-DP-colorable iff for EVERY correspondence assignment (L, M) -- each
edge uv carrying an arbitrary (not necessarily perfect) matching between
{u} x [ell] and {v} x [ell] -- there exists phi with phi(v) in [ell] such that
no edge uv has (u, phi(u)) matched to (v, phi(v)).

Sanity checks on known values (kept small so full enumeration is feasible):
    chi_DP(K_n) = n for n = 1, 2, 3
    chi_DP(C_4) = 3  (even cycles have DP-chromatic number 3, unlike the
                      list chromatic number, which is 2)
    C_5 and C_6 are NOT 2-DP-colorable (bad-assignment search only)
We then confirm chi_DP(E_n) = 1 for n = 1..8 and print the ratio
chi_DP(E_n) / (n / log n) -> 0.
"""

import itertools
import math


def all_partial_matchings(ell):
    """All partial matchings between [ell] and [ell], as frozensets of pairs."""
    result = []

    def rec(i, used_right, current):
        if i == ell:
            result.append(frozenset(current))
            return
        rec(i + 1, used_right, current)  # left vertex i unmatched
        for r in range(ell):
            if r not in used_right:
                rec(i + 1, used_right | {r}, current + [(i, r)])

    rec(0, set(), [])
    return result


def dp_colorable(n, edges, ell):
    """Is the graph ([n], edges) ell-DP-colorable (for every assignment)?"""
    matchings = all_partial_matchings(ell)
    colorings = list(itertools.product(range(ell), repeat=n))
    for assignment in itertools.product(matchings, repeat=len(edges)):
        if not any(
            all((phi[u], phi[v]) not in m
                for (u, v), m in zip(edges, assignment))
            for phi in colorings
        ):
            return False
    return True


def dp_chromatic_number(n, edges, max_ell=6):
    for ell in range(1, max_ell + 1):
        if dp_colorable(n, edges, ell):
            return ell
    return None


def cycle_edges(k):
    return [(i, (i + 1) % k) for i in range(k)]


def complete_edges(k):
    return list(itertools.combinations(range(k), 2))


def main():
    print("Sanity checks (known DP-chromatic numbers):")
    for k in range(1, 4):
        v = dp_chromatic_number(k, complete_edges(k))
        print(f"  chi_DP(K_{k}) = {v}   (expected {k})")
        assert v == k, f"sanity check failed for K_{k}"
    v = dp_chromatic_number(4, cycle_edges(4), max_ell=3)
    print(f"  chi_DP(C_4) = {v}   (expected 3; list chromatic number is 2)")
    assert v == 3
    for k in (5, 6):
        bad = not dp_colorable(k, cycle_edges(k), 2)
        print(f"  C_{k} 2-DP-colorable: {not bad}   (expected False)")
        assert bad

    print("\nMain check: edgeless graphs E_n.")
    print("(E_n has no edges, hence exactly one correspondence assignment for"
          " each ell: the empty one; the checker verifies this generically.)")
    for n in range(1, 9):
        v = dp_chromatic_number(n, [])
        assert v == 1, f"E_{n} not 1-DP-colorable?!"
        if n > 1:
            print(f"  chi_DP(E_{n}) = {v}   chi_DP / (n/log n) = "
                  f"{v / (n / math.log(n)):.4f}")
        else:
            print(f"  chi_DP(E_1) = {v}")

    print("\nAsymptotics of the ratio 1 / (n/log n) = log(n)/n:")
    for n in (10, 100, 10**4, 10**8):
        print(f"  n = {n:>10}: log(n)/n = {math.log(n)/n:.3e}")

    print("\nAll checks passed: chi_DP(edgeless graph) = 1, so chi_DP(G(n,0))"
          " is NOT Theta(n/log n).")


if __name__ == "__main__":
    main()
