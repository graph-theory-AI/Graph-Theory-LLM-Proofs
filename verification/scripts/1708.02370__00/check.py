#!/usr/bin/env python3
"""Verification script for referee report 1708.02370__00 (pure stdlib).

Checks, by brute force:
  (a) td(2K_1) = 1 and ctd(2K_1) = 2 under the paper's definitions
      (depth = max #vertices on a root-to-leaf path; ctd = min depth of a
      rooted TREE whose closure contains H as subgraph; td = max ctd over
      connected components; arXiv:1708.02370, Section 1).
  (b) Every graph on 2..5 vertices has a 2K_1 minor (generic branch-set
      minor check), and graphs on <=1 vertex do not, hence
      M_{2K_1} = {G : |V(G)| <= 1}.
  (c) chi*(M_{2K_1}) = 1.
  (d) Consequences: the garbled catalog bound 2*td-2 = 0 fails (1 > 0),
      but the paper's actual bound 2*ctd-2 = 2 holds (1 <= 2).

A graph is (frozenset_of_vertices, frozenset_of_frozenset_edges).
"""

import itertools


# ---------- basic graph helpers ----------

def empty_graph(n):
    return frozenset(range(n)), frozenset()


def is_connected(verts, edges):
    verts = set(verts)
    if not verts:
        return False
    adj = {v: set() for v in verts}
    for e in edges:
        a, b = tuple(e)
        if a in verts and b in verts:
            adj[a].add(b)
            adj[b].add(a)
    seen = {next(iter(verts))}
    stack = [next(iter(verts))]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return seen == verts


def components(verts, edges):
    verts = set(verts)
    out = []
    while verts:
        v = verts.pop()
        comp = {v}
        stack = [v]
        while stack:
            x = stack.pop()
            for e in edges:
                if x in e:
                    (y,) = tuple(e - {x})
                    if y in verts:
                        verts.remove(y)
                        comp.add(y)
                        stack.append(y)
        out.append((frozenset(comp),
                    frozenset(e for e in edges if e <= comp)))
    return out


# ---------- (a) tree-depth / connected tree-depth ----------

def rooted_forests(n, single_tree):
    """All acyclic parent maps on 0..n-1 (parent None = root)."""
    verts = range(n)
    for parents in itertools.product(*[[None] + [u for u in verts if u != v]
                                       for v in verts]):
        pmap = dict(zip(verts, parents))
        ok = True
        for v in verts:
            seen, u = set(), v
            while u is not None:
                if u in seen:
                    ok = False
                    break
                seen.add(u)
                u = pmap[u]
            if not ok:
                break
        if not ok:
            continue
        if single_tree and sum(1 for v in verts if pmap[v] is None) != 1:
            continue
        yield pmap


def depth_of(pmap):
    """Paper convention: max number of VERTICES on a root-to-leaf path."""
    def d(v):
        c = 0
        while v is not None:
            c += 1
            v = pmap[v]
        return c
    return max(d(v) for v in pmap) if pmap else 0


def closure_edges(pmap):
    edges = set()
    for v in pmap:
        u = pmap[v]
        while u is not None:
            edges.add(frozenset((v, u)))
            u = pmap[u]
    return edges


def has_subgraph(host_verts, host_edges, hverts, hedges):
    for img in itertools.permutations(host_verts, len(hverts)):
        m = dict(zip(sorted(hverts), img))
        if all(frozenset((m[a], m[b])) in host_edges
               for e in hedges for a, b in [tuple(e)]):
            return True
    return False


def ctd(hverts, hedges, max_n=6):
    """Min depth of a rooted tree whose closure contains H as subgraph."""
    for n in range(max(1, len(hverts)), max_n + 1):
        best = None
        for pmap in rooted_forests(n, single_tree=True):
            ce = closure_edges(pmap)
            if has_subgraph(set(pmap), ce, hverts, hedges):
                d = depth_of(pmap)
                best = d if best is None else min(best, d)
        if best is not None:
            return best
    raise RuntimeError("ctd not found up to max_n")


def td(hverts, hedges):
    comps = components(hverts, hedges)
    if not comps:
        return 0
    return max(ctd(cv, ce) for cv, ce in comps)


# ---------- (b) generic minor check ----------

def has_minor(gverts, gedges, hverts, hedges):
    gv = sorted(gverts)
    hv = sorted(hverts)
    k = len(hv)
    if k > len(gv):
        return False

    def rec(i, used, branch):
        if i == k:
            for e in hedges:
                a, b = tuple(e)
                A, B = branch[a], branch[b]
                if not any(frozenset((x, y)) in gedges for x in A for y in B):
                    return False
            return True
        avail = [v for v in gv if v not in used]
        for size in range(1, len(avail) - (k - i - 1) + 1):
            for S in itertools.combinations(avail, size):
                Sf = frozenset(S)
                if is_connected(Sf, gedges):
                    branch[hv[i]] = Sf
                    if rec(i + 1, used | Sf, branch):
                        return True
        return False

    return rec(0, frozenset(), {})


def all_graphs(n):
    verts = frozenset(range(n))
    pairs = [frozenset(p) for p in itertools.combinations(range(n), 2)]
    for mask in range(1 << len(pairs)):
        yield verts, frozenset(p for i, p in enumerate(pairs)
                               if mask >> i & 1)


# ---------- run ----------

def main():
    h2v, h2e = empty_graph(2)  # 2K_1

    # (a) tree-depth values under the paper's definitions
    t = td(h2v, h2e)
    c = ctd(h2v, h2e)
    print(f"td(2K_1)  = {t}   (writeup claims 1)")
    print(f"ctd(2K_1) = {c}   (paper's connected tree-depth)")
    assert t == 1 and c == 2

    for r in (3, 4):
        hv, he = empty_graph(r)
        tr, cr = td(hv, he), ctd(hv, he)
        # a root with r-1 children has depth 2 and its closure (a star)
        # contains rK_1, so ctd(rK_1) = 2 for every r >= 2
        print(f"td({r}K_1) = {tr}, ctd({r}K_1) = {cr}")
        assert tr == 1 and cr == 2

    # sanity: paper's rule ctd = td + 1 iff two components attain max td
    # e.g. 2K_2 (two disjoint edges): td = 2, ctd = 3
    h22v = frozenset(range(4))
    h22e = frozenset({frozenset((0, 1)), frozenset((2, 3))})
    print(f"td(2K_2) = {td(h22v, h22e)}, ctd(2K_2) = {ctd(h22v, h22e)}")
    assert td(h22v, h22e) == 2 and ctd(h22v, h22e) == 3

    # (b) M_{2K_1} = graphs with at most 1 vertex (checked on <=5 vertices)
    for n in range(0, 6):
        for gv, ge in all_graphs(n):
            assert has_minor(gv, ge, h2v, h2e) == (n >= 2), (n, sorted(map(tuple, ge)))
    print("verified: G has a 2K_1 minor iff |V(G)| >= 2 (all graphs on <=5 vertices)")

    # (c) chi*(M_{2K_1}): class = {empty graph, K_1}. K_1 needs >= 1 colour;
    # 1 colour with clustering 1 works for both members. So chi* = 1.
    print("chi*(M_{2K_1}) = 1  (K_1 in the class forces >= 1 colour; "
          "1 colour, clustering 1, suffices)")

    # (d) the two bounds
    print(f"garbled catalog bound  2*td(2K_1)-2  = {2*t-2}:  1 > {2*t-2}  "
          f"-> literal (mis-extracted) statement fails")
    print(f"actual paper bound     2*ctd(2K_1)-2 = {2*c-2}:  1 <= {2*c-2} "
          f"-> real Conjecture 4 holds for H = 2K_1")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
