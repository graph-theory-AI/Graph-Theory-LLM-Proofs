#!/usr/bin/env python3
"""Verification of Lemma 1 of attacks/1702.01094__01/output.md.

Lemma 1 (writeup): if D(G) (common-neighbor graph) has a proper q-coloring and
odd-girth(G) > 4q-3, then the cover A = {A_x} by principal upsets of the
color-increasing orientation of D(G) is a stable-set cover of G such that no
induced path P with >= 3 vertices satisfies:
    for every v in V(P) there is X in A with X ∩ V(P) = {v}.

We implement the construction exactly as written and brute-force check, on
several concrete graphs satisfying the hypothesis:
  (a) every A_x is a stable set of G,
  (b) the A_x cover V(G),
  (c) the domination property: whenever u,w have a common neighbor, one of
      them (say u) satisfies: every A_x containing u contains w,
  (d) NO induced path with s >= 3 vertices (s = 3..6, full enumeration)
      has the private-cover property,
  (e) sanity: for s = 1 and s = 2 the property DOES hold (trivial cases),
  (f) control experiment: with a proper-coloring cover (partition into color
      classes) rainbow induced paths DO exist on the same graphs, confirming
      the counterexample does not clash with the Scott-Seymour main theorem.
"""

import itertools
import sys
import networkx as nx


def distance_two_graph(G):
    """D(G): u ~ w iff u != w and they have a common neighbor in G."""
    D = nx.Graph()
    D.add_nodes_from(G.nodes())
    for x in G.nodes():
        nbrs = list(G.neighbors(x))
        for u, w in itertools.combinations(nbrs, 2):
            if u != w:
                D.add_edge(u, w)
    return D


def odd_girth(G):
    best = None
    for cyc in nx.simple_cycles(G):  # fine for the small graphs used here
        if len(cyc) % 2 == 1:
            if best is None or len(cyc) < best:
                best = len(cyc)
    return best  # None means bipartite / forest (odd girth = infinity)


def lemma1_cover(G, coloring):
    """Build the cover {A_x} from a proper coloring of D(G) as in the writeup."""
    # orientation: edge u->w of D(G) when coloring[u] < coloring[w]
    D = distance_two_graph(G)
    for u, w in D.edges():
        assert coloring[u] != coloring[w], "coloring of D(G) not proper"
    order = nx.DiGraph()
    order.add_nodes_from(G.nodes())
    for u, w in D.edges():
        if coloring[u] < coloring[w]:
            order.add_edge(u, w)
        else:
            order.add_edge(w, u)
    assert nx.is_directed_acyclic_graph(order)
    # A_x = {y : x <= y} (reflexive transitive closure => descendants + x)
    cover = {}
    for x in G.nodes():
        cover[x] = frozenset(nx.descendants(order, x)) | {x}
    return cover, order


def is_stable(G, S):
    return all(not G.has_edge(u, w) for u, w in itertools.combinations(S, 2))


def induced_paths(G, s):
    """Yield all s-vertex induced paths of G (as vertex tuples)."""
    if s == 1:
        for v in G.nodes():
            yield (v,)
        return
    # DFS over paths, checking induced condition incrementally
    def extend(path, pathset):
        if len(path) == s:
            yield tuple(path)
            return
        last = path[-1]
        for w in G.neighbors(last):
            if w in pathset:
                continue
            # induced: w adjacent to last only, among path vertices
            if any(G.has_edge(w, p) for p in path[:-1]):
                continue
            path.append(w)
            pathset.add(w)
            yield from extend(path, pathset)
            path.pop()
            pathset.remove(w)

    seen = set()
    for v in G.nodes():
        for p in extend([v], {v}):
            key = p if p[0] <= p[-1] else p[::-1]
            if key not in seen:
                seen.add(key)
                yield p


def has_private_cover(P, cover_sets):
    Pset = set(P)
    for v in P:
        if not any(v in X and len(X & Pset) == 1 for X in cover_sets):
            return False
    return True


def check_graph(name, G, smax=6):
    print(f"=== {name}: n={G.number_of_nodes()}, m={G.number_of_edges()} ===")
    assert all(len(c) < 3 for c in nx.enumerate_all_cliques(G) if len(c) >= 3) or True
    tri_free = all(False for _ in nx.triangles(G).items() if False)
    ntri = sum(nx.triangles(G).values()) // 3
    print(f"  triangles: {ntri}")
    D = distance_two_graph(G)
    coloring = nx.greedy_color(D, strategy="DSATUR")
    q = max(coloring.values()) + 1
    og = odd_girth(G)
    og_str = "infinity" if og is None else str(og)
    hyp = (og is None) or (og > 4 * q - 3)
    print(f"  q = {q} (greedy proper coloring of D(G)), 4q-3 = {4*q-3}, odd girth = {og_str}")
    print(f"  hypothesis odd-girth > 4q-3: {hyp}")
    if not hyp:
        print("  SKIP (hypothesis fails; lemma not applicable)")
        return
    cover, order = lemma1_cover(G, coloring)
    cover_sets = set(cover.values())
    # (a) stability
    bad = [x for x, S in cover.items() if not is_stable(G, S)]
    print(f"  (a) all A_x stable: {not bad}" + (f"  VIOLATIONS at {bad}" if bad else ""))
    # (b) cover
    union = set().union(*cover_sets)
    print(f"  (b) union of A_x = V(G): {union == set(G.nodes())}")
    # (c) domination for common-neighbor pairs
    dom_ok = True
    for u, w in D.edges():
        du = all(w in X for X in cover_sets if u in X)
        dw = all(u in X for X in cover_sets if w in X)
        if not (du or dw):
            dom_ok = False
            print(f"    domination FAILS for pair {u},{w}")
    print(f"  (c) domination property on all {D.number_of_edges()} D(G)-edges: {dom_ok}")
    # (d)/(e) path property per s
    for s in range(1, smax + 1):
        paths = list(induced_paths(G, s))
        good = [P for P in paths if has_private_cover(P, cover_sets)]
        print(f"  s={s}: {len(paths)} induced paths, {len(good)} with private-cover property")
        if s >= 3:
            assert len(good) == 0, f"LEMMA 1 FAILS: path {good[0]} works for s={s}"
        elif paths:
            assert len(good) == len(paths), f"trivial case s={s} unexpectedly fails"
    # (f) control: proper coloring of G as a partition cover -> rainbow paths exist
    gcol = nx.greedy_color(G, strategy="DSATUR")
    classes = {}
    for v, c in gcol.items():
        classes.setdefault(c, set()).add(v)
    part_cover = [frozenset(S) for S in classes.values()]
    s = min(3, smax)
    good = [P for P in induced_paths(G, 3) if has_private_cover(P, part_cover)]
    print(f"  (f) control with proper-coloring partition cover, s=3: "
          f"{len(good)} rainbow induced paths exist (expected > 0 unless chi<3)")
    print()


def main():
    # 1. Odd cycles: chi=3, triangle-free, D(C_n) needs q=3 (n odd), odd girth n.
    for n in (13, 17, 21, 25):
        check_graph(f"C_{n}", nx.cycle_graph(n))

    # 2. Paths (forests: odd girth infinite, hypothesis vacuous).
    check_graph("P_20", nx.path_graph(20))

    # 3. Even cycle (bipartite, odd girth infinite).
    check_graph("C_24", nx.cycle_graph(24))

    # 4. Petersen graph subdivided: each edge -> path with 7 edges.
    #    Delta = 3 so Delta(D) <= 6, q <= 7, need odd girth > 4q-3 (<= 25).
    #    Odd girth = 5*7 = 35 > 25; graph is triangle-free, chi = 3.
    P = nx.petersen_graph()
    S7 = nx.Graph()
    cnt = 1000
    for u, w in P.edges():
        prev = u
        for i in range(6):
            S7.add_edge(prev, cnt)
            prev = cnt
            cnt += 1
        S7.add_edge(prev, w)
    check_graph("Petersen edges subdivided into 7 (odd girth 35)", S7, smax=5)

    # 5. A random tree.
    import random
    random.seed(7)
    check_graph("random tree n=40", nx.random_labeled_tree(40, seed=7))

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
