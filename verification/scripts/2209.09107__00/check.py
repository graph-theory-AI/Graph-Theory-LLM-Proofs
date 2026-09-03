"""Verification script for 2209.09107__00 (referee check).

Writeup claim: Question 6.1 of arXiv:2209.09107 is false as stated; the triangle
C_3 (and every odd cycle / Eulerian graph with an odd number of edges) is a
counterexample, because the forced orientation is Eulerian with an odd number of
edges and such an orientation is never Alon-Tarsi (EE(D) = EO(D)).

Checks performed here:
 1. AT test: for a digraph D, count even/odd Eulerian sub-digraphs (empty
    subgraph included, as in the standard definition and in the paper's
    EE(D)/EO(D)); D is AT iff EE != EO.
 2. Exhaustive check of Question 6.1 for G = C_3 and G = C_5: enumerate every
    spanning subgraph H and every orientation D of H, keep those with
    deg+_D(v) >= (deg_G(v)-1)/2 for all v, and test whether any is AT.
 3. Lemma check: for every connected even-degree graph on <= 6 vertices with an
    odd number of edges, and every Eulerian orientation of it, verify EE == EO.
 4. Sanity control: even cycle C_4 (even |E|) DOES admit such an AT orientation,
    confirming the AT test is not degenerate.
"""

import itertools
from math import ceil


def eulerian_counts(arcs):
    """Return (EE, EO): number of even/odd subsets of arcs that are Eulerian
    (in-degree == out-degree at every vertex). Empty subset included."""
    arcs = list(arcs)
    EE = EO = 0
    for r in range(len(arcs) + 1):
        for sub in itertools.combinations(arcs, r):
            bal = {}
            for (u, v) in sub:
                bal[u] = bal.get(u, 0) + 1
                bal[v] = bal.get(v, 0) - 1
            if all(x == 0 for x in bal.values()):
                if r % 2 == 0:
                    EE += 1
                else:
                    EO += 1
    return EE, EO


def is_AT(arcs):
    EE, EO = eulerian_counts(arcs)
    return EE != EO


def outdegs(arcs, verts):
    d = {v: 0 for v in verts}
    for (u, v) in arcs:
        d[u] += 1
    return d


def question61_witness(edges, verts):
    """Search all spanning subgraphs H of G=(verts,edges) and all orientations D
    of H with deg+_D(v) >= (deg_G(v)-1)/2 for all v; return an AT witness or None,
    plus the number of orientations meeting the degree bound."""
    degG = {v: 0 for v in verts}
    for (u, v) in edges:
        degG[u] += 1
        degG[v] += 1
    # integer threshold: deg+ >= (degG-1)/2  <=>  deg+ >= ceil((degG-1)/2)
    thr = {v: ceil((degG[v] - 1) / 2) for v in verts}
    n_ok = 0
    for r in range(len(edges) + 1):
        for H in itertools.combinations(edges, r):
            for orient in itertools.product([0, 1], repeat=r):
                arcs = [(e[0], e[1]) if o == 0 else (e[1], e[0])
                        for e, o in zip(H, orient)]
                dplus = outdegs(arcs, verts)
                if all(dplus[v] >= thr[v] for v in verts):
                    n_ok += 1
                    if is_AT(arcs):
                        return arcs, n_ok
    return None, n_ok


def cycle_edges(k):
    return [(i, (i + 1) % k) for i in range(k)], list(range(k))


def all_connected_even_odd_graphs(nmax):
    """Yield (edges, verts) for every connected graph on <= nmax vertices
    (up to labeled generation; no isomorphism reduction needed for a lemma check)
    in which every vertex has even degree and |E| is odd."""
    for n in range(3, nmax + 1):
        verts = list(range(n))
        pairs = list(itertools.combinations(verts, 2))
        for mask in range(1, 1 << len(pairs)):
            edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
            if len(edges) % 2 == 0:
                continue
            deg = {v: 0 for v in verts}
            adj = {v: [] for v in verts}
            for (u, v) in edges:
                deg[u] += 1
                deg[v] += 1
                adj[u].append(v)
                adj[v].append(u)
            if any(d % 2 != 0 or d == 0 for d in deg.values()):
                continue
            # connectivity over all n vertices
            seen = {0}
            stack = [0]
            while stack:
                x = stack.pop()
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
            if len(seen) != n:
                continue
            yield edges, verts


def eulerian_orientations(edges, verts):
    for orient in itertools.product([0, 1], repeat=len(edges)):
        arcs = [(e[0], e[1]) if o == 0 else (e[1], e[0])
                for e, o in zip(edges, orient)]
        d = {v: 0 for v in verts}
        for (u, v) in arcs:
            d[u] += 1
            d[v] -= 1
        if all(x == 0 for x in d.values()):
            yield arcs


def main():
    # --- Check 1+2: Question 6.1 exhaustively on C_3 and C_5 ---
    for k in (3, 5):
        edges, verts = cycle_edges(k)
        witness, n_ok = question61_witness(edges, verts)
        print(f"C_{k}: orientations meeting the degree bound: {n_ok}; "
              f"AT witness: {witness}")
        assert witness is None, f"Q6.1 witness found for C_{k}: {witness}"

    # Detail for C_3: show EE/EO of the directed triangle
    tri = [(0, 1), (1, 2), (2, 0)]
    print("directed triangle EE,EO =", eulerian_counts(tri))
    assert eulerian_counts(tri) == (1, 1)

    # --- Check 3: parity lemma on all small even-degree odd-size graphs ---
    n_graphs = 0
    n_orients = 0
    for edges, verts in all_connected_even_odd_graphs(6):
        n_graphs += 1
        for arcs in eulerian_orientations(edges, verts):
            n_orients += 1
            EE, EO = eulerian_counts(arcs)
            assert EE == EO, (edges, arcs, EE, EO)
    print(f"lemma verified: {n_graphs} labeled connected even-degree graphs "
          f"with odd |E| on <=6 vertices, {n_orients} Eulerian orientations, "
          f"all have EE == EO (not Alon-Tarsi)")

    # --- Check 4: control, C_4 should succeed ---
    edges, verts = cycle_edges(4)
    witness, n_ok = question61_witness(edges, verts)
    print(f"C_4 control: AT witness meeting bound: {witness}")
    assert witness is not None

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
