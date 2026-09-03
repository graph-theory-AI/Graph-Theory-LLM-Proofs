#!/usr/bin/env python3
"""Independent verification of the counterexample in attacks/2503.23191__00/output.md.

Claim under review: the balanced blow-up G_m of the directed triangle
(parts A0,A1,A2 of size m, all arcs A0->A1->A2->A0) has minimum semidegree
m = k/2 (k = 2m) but contains no copy of the non-antidirected k-edge path P_m
defined by:
    v0 -> v1 <- v2, and for 2 <= j <= m:  v_{2j-1} -> v_{2j-2},  v_{2j-1} -> v_{2j}.

Also cross-checks against the v2 revision of the source paper (arXiv:2503.23191v2,
Section 5): the blow-up should exclude PRECISELY the "bouncing" orientations
(height function h with h_i in {-1,0,1} and h_j = 0 for every even index j).
"""

from itertools import permutations, product


def blowup(m):
    """Vertices 0..3m-1; part(v) = v // m; arcs part i -> part i+1 mod 3."""
    n = 3 * m
    arcs = set()
    for u in range(n):
        for v in range(n):
            if (u // m + 1) % 3 == v // m:
                arcs.add((u, v))
    return n, arcs


def semidegrees(n, arcs):
    outd = [0] * n
    ind = [0] * n
    for (u, v) in arcs:
        outd[u] += 1
        ind[v] += 1
    return min(outd), min(ind)


def path_arcs_from_signs(signs):
    """signs[i] = +1 means v_i -> v_{i+1}, -1 means v_{i+1} -> v_i."""
    arcs = []
    for i, s in enumerate(signs):
        arcs.append((i, i + 1) if s == 1 else (i + 1, i))
    return arcs


def writeup_path_signs(m):
    """Orientation of P_m from the writeup, as a sign vector of length k=2m."""
    k = 2 * m
    signs = [0] * k
    signs[0] = +1          # v0 -> v1
    signs[1] = -1          # v2 -> v1
    for j in range(2, m + 1):
        signs[2 * j - 2] = -1   # v_{2j-1} -> v_{2j-2}
        signs[2 * j - 1] = +1   # v_{2j-1} -> v_{2j}
    return tuple(signs)


def is_antidirected(signs):
    """Antidirected = arc directions strictly alternate along the path."""
    return all(signs[i] != signs[i + 1] for i in range(len(signs) - 1))


def is_bouncing(signs):
    """Heights h_0=0, h_{i+1}=h_i+signs[i]; bouncing iff all h in {-1,0,1}
    and h_j = 0 for every even j (paper v2, Section 5)."""
    h = 0
    for i, s in enumerate(signs):
        h += s
        if h not in (-1, 0, 1):
            return False
        if (i + 1) % 2 == 0 and h != 0:
            return False
    return True


def embeds(n, arcs, path_arcs, num_path_vertices):
    """Brute force: does the oriented path embed injectively into (n, arcs)?"""
    verts = range(n)
    for f in permutations(verts, num_path_vertices):
        if all((f[a], f[b]) in arcs for (a, b) in path_arcs):
            return True
    return False


def embeds_pruned(n, arcs, path_arcs, num_path_vertices):
    """Backtracking embedding along the path order (faster for k=6,8)."""
    # constraints between consecutive path vertices
    succ = {}
    for (a, b) in path_arcs:
        succ.setdefault(min(a, b), (a, b))

    def rec(i, mapping, used):
        if i == num_path_vertices:
            return True
        for v in range(n):
            if v in used:
                continue
            ok = True
            for (a, b) in path_arcs:
                if max(a, b) == i and min(a, b) < i:
                    fa = mapping[a] if a < i else v
                    fb = mapping[b] if b < i else v
                    if (fa, fb) not in arcs:
                        ok = False
                        break
            if ok:
                mapping.append(v)
                used.add(v)
                if rec(i + 1, mapping, used):
                    return True
                mapping.pop()
                used.remove(v)
        return False

    return rec(0, [], set())


def main():
    print("=== 1. Smallest counterexample: k=4, m=2 (n=6) ===")
    m = 2
    n, arcs = blowup(m)
    dp, dm = semidegrees(n, arcs)
    print(f"blow-up G_2: n={n}, delta^+={dp}, delta^-={dm}, delta^0={min(dp, dm)} (claimed {m})")
    assert min(dp, dm) == m

    signs = writeup_path_signs(m)
    print(f"P signs (k=4): {signs}  (expected (+1,-1,-1,+1): v0->v1<-v2<-v3->v4)")
    assert signs == (1, -1, -1, 1)
    print(f"P antidirected? {is_antidirected(signs)} (claimed False)")
    print(f"P bouncing (v2 class)? {is_bouncing(signs)} (v2 predicts True)")
    p_arcs = path_arcs_from_signs(signs)
    found = embeds(n, arcs, p_arcs, 5)
    print(f"P embeds in G_2? {found} (claimed False)")
    assert not found

    # sanity: directed 4-edge path DOES embed (so the graph is not trivially path-free)
    dir_arcs = path_arcs_from_signs((1, 1, 1, 1))
    print(f"directed P4 embeds in G_2? {embeds(n, arcs, dir_arcs, 5)} (should be True)")

    print()
    print("=== 2. Exhaustive: which of the 16 orientations of the 4-edge path embed in G_2? ===")
    for signs4 in product((1, -1), repeat=4):
        e = embeds(n, arcs, path_arcs_from_signs(signs4), 5)
        b = is_bouncing(signs4)
        a = is_antidirected(signs4)
        tag = "antidirected" if a else ("bouncing(non-anti)" if b else "")
        print(f"  signs={signs4}  embeds={e}  bouncing={b}  {tag}")
        # v2 Section 5 claim: excluded <=> bouncing
        assert e == (not b), f"mismatch for {signs4}"
    print("  Verified: an orientation of the 4-edge path embeds in G_2 iff it is NOT bouncing.")

    print()
    print("=== 3. Infinite family check: k=6, m=3 (n=9) ===")
    m = 3
    n, arcs = blowup(m)
    dp, dm = semidegrees(n, arcs)
    print(f"blow-up G_3: n={n}, delta^0={min(dp, dm)} (claimed {m})")
    assert min(dp, dm) == m
    signs = writeup_path_signs(m)
    print(f"P_3 signs (k=6): {signs}")
    print(f"P_3 antidirected? {is_antidirected(signs)} (claimed False)")
    print(f"P_3 bouncing? {is_bouncing(signs)} (v2 predicts True)")
    assert not is_antidirected(signs) and is_bouncing(signs)
    found = embeds_pruned(n, arcs, path_arcs_from_signs(signs), 7)
    print(f"P_3 embeds in G_3? {found} (claimed False)")
    assert not found

    print()
    print("=== 4. Exhaustive: 64 orientations of the 6-edge path vs G_3 ===")
    mismatches = 0
    excluded = []
    for signs6 in product((1, -1), repeat=6):
        e = embeds_pruned(n, arcs, path_arcs_from_signs(signs6), 7)
        b = is_bouncing(signs6)
        if e == b:
            mismatches += 1
            print(f"  MISMATCH signs={signs6} embeds={e} bouncing={b}")
        if not e:
            excluded.append((signs6, is_antidirected(signs6)))
    print(f"  excluded orientations: {len(excluded)}")
    for s, a in excluded:
        print(f"    {s}  antidirected={a}")
    assert mismatches == 0
    print("  Verified: an orientation of the 6-edge path embeds in G_3 iff it is NOT bouncing.")

    print()
    print("=== 5. k=8, m=4 (n=12): writeup path P_4 only ===")
    m = 4
    n, arcs = blowup(m)
    assert semidegrees(n, arcs) == (m, m)
    signs = writeup_path_signs(m)
    assert not is_antidirected(signs) and is_bouncing(signs)
    found = embeds_pruned(n, arcs, path_arcs_from_signs(signs), 9)
    print(f"P_4 signs: {signs}; antidirected=False, bouncing=True, embeds in G_4? {found} (claimed False)")
    assert not found

    print()
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
