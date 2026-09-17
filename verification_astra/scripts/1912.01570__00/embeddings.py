"""Exhaustive computation of fp(G_1) over ALL planar embeddings.

An embedding of a connected graph in an orientable surface is a rotation system:
a cyclic order of the incident darts at every vertex.  Face tracing on darts gives
the number F of faces; the embedding is planar (genus 0) iff V - E + F = 2.
We enumerate every rotation system (fixing one rotation per vertex up to rotation of
the cyclic sequence), keep the planar ones, read off the facial walks that are simple
cycles, and take the maximum number of pairwise vertex-disjoint such cycles.
That maximum over all planar embeddings is exactly fp(G).
"""
import itertools
import sys

from build import build, max_disjoint


def rotation_choices(nbrs):
    """All cyclic orders of `nbrs`: fix the first element, permute the rest -> (d-1)! of them."""
    first, rest = nbrs[0], nbrs[1:]
    return [(first,) + p for p in itertools.permutations(rest)]


def faces_of(rot, edges):
    """Trace faces of the rotation system. rot[v] = tuple of neighbours in cyclic order."""
    nxt = {}
    for v, order in rot.items():
        d = len(order)
        pos = {u: i for i, u in enumerate(order)}
        for u in order:
            # dart (u -> v); next dart leaves v towards the neighbour after u in rot[v]
            nxt[(u, v)] = (v, order[(pos[u] + 1) % d])
    unvisited = set(nxt)
    faces = []
    while unvisited:
        start = next(iter(unvisited))
        walk = []
        d = start
        while d in unvisited:
            unvisited.discard(d)
            walk.append(d)
            d = nxt[d]
        faces.append(walk)
    return faces


def fp_exact(G, verbose=True):
    V = list(G.nodes())
    E = G.number_of_edges()
    n = len(V)
    per_vertex = [rotation_choices(sorted(G.neighbors(v))) for v in V]
    total = 1
    for c in per_vertex:
        total *= len(c)
    if verbose:
        print(f"n={n} m={E}; enumerating {total} rotation systems "
              f"(sizes {[len(c) for c in per_vertex]})")
    best = 0
    best_witness = None
    n_planar = 0
    facial_cycle_seen = set()
    for combo in itertools.product(*per_vertex):
        rot = dict(zip(V, combo))
        F = faces_of(rot, E)
        if n - E + len(F) != 2:
            continue           # not a sphere embedding
        n_planar += 1
        cyc = []
        for walk in F:
            vs = [d[0] for d in walk]
            if len(set(vs)) == len(vs) and len(vs) >= 3:
                cyc.append(frozenset(vs))
                facial_cycle_seen.add(frozenset(vs))
        k, wit = max_disjoint(cyc)
        if k > best:
            best, best_witness = k, (wit, rot)
    if verbose:
        print(f"planar rotation systems: {n_planar}")
        print(f"distinct cycles that are facial in SOME planar embedding: "
              f"{len(facial_cycle_seen)}")
    return best, best_witness, facial_cycle_seen


if __name__ == "__main__":
    t = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    G = build(t)
    best, wit, facial = fp_exact(G)
    print(f"\n*** fp(G_{t}) = {best}  (writeup claims {t+1}) ***")
    print("witnessing packing:", [sorted(c) for c in wit[0]])
    # is any C_i facial in some embedding?
    for i in range(1, t + 1):
        C = frozenset({f"a{i}", f"b{i}", f"c{i}", f"d{i}"})
        print(f"C_{i} facial in some planar embedding: {C in facial}")
    print("\nAll cycles facial in some embedding (sorted):")
    for c in sorted(facial, key=lambda s: (len(s), sorted(s))):
        print("   ", sorted(c))
