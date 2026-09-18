"""
Independent check of the writeup's Lemma 2 (Section 4 of output.md):
explicit d-regular bipartite graph of girth > g from involutions on the set W
of words of length <= g over [d] with consecutive letters distinct.

(a) sigma_j is a well-defined involution of W.
(b) empty . sigma_{j1}...sigma_{jl} = j1...jl  for every reduced word of length l <= g
    (this is eq. (4.1), the whole engine of the girth bound).
(c) build the bipartite Cayley graph on the GENERATED subgroup <sigma_1,..,sigma_d>
    (a union of components of the graph on Sym(W), hence an equally valid witness)
    and measure d-regularity, simplicity and girth for the small feasible cases.
"""
import itertools
import networkx as nx


def words(d, g):
    W = [()]
    cur = [()]
    for _ in range(g):
        nxt = []
        for w in cur:
            for j in range(1, d + 1):
                if not w or w[-1] != j:
                    nxt.append(w + (j,))
        W += nxt
        cur = nxt
    return W


def sigma(d, g, W, j):
    idx = {w: i for i, w in enumerate(W)}
    perm = []
    for w in W:
        if w and w[-1] == j:
            img = w[:-1]
        elif len(w) < g:
            img = w + (j,)
        else:
            img = w
        perm.append(idx[img])
    return tuple(perm)


def compose(p, q):          # right action: first p then q  (x -> q[p[x]])
    return tuple(q[x] for x in p)


def check(d, g, build_graph=False):
    W = words(d, g)
    n = len(W)
    S = {j: sigma(d, g, W, j) for j in range(1, d + 1)}
    # (a) permutations and involutions
    for j, p in S.items():
        assert sorted(p) == list(range(n)), f"sigma_{j} not a permutation"
        assert compose(p, p) == tuple(range(n)), f"sigma_{j} not an involution"
    assert len(set(S.values())) == d, "generators not distinct"
    # (b) eq. (4.1)
    ident = tuple(range(n))
    empty = W.index(())
    nred = 0
    for l in range(1, g + 1):
        for seq in itertools.product(range(1, d + 1), repeat=l):
            if any(seq[i] == seq[i + 1] for i in range(l - 1)):
                continue
            nred += 1
            cur = ident
            for j in seq:
                cur = compose(cur, S[j])
            assert cur[empty] == W.index(seq), "(4.1) fails: image is not the word"
            assert cur != ident, "(4.1) fails: product is the identity"
    info = f"d={d} g={g}: |W|={n}, reduced words tested={nred}, (a) and (4.1) OK"
    if build_graph:
        # generated subgroup
        G, frontier = {ident}, [ident]
        while frontier:
            new = []
            for p in frontier:
                for j in S:
                    q = compose(p, S[j])
                    if q not in G:
                        G.add(q); new.append(q)
            frontier = new
        G = sorted(G)
        gi = {p: i for i, p in enumerate(G)}
        Q = nx.Graph()
        Q.add_nodes_from((0, i) for i in range(len(G)))
        Q.add_nodes_from((1, i) for i in range(len(G)))
        for p in G:
            for j in S:
                Q.add_edge((0, gi[p]), (1, gi[compose(p, S[j])]))
        degs = {deg for _, deg in Q.degree()}
        gir = nx.girth(Q)
        assert degs == {d}, f"not {d}-regular: {degs}"
        assert nx.is_bipartite(Q)
        assert gir > g, f"girth {gir} not > g={g}"
        info += f" | |<sigma>|={len(G)}, graph {Q.number_of_nodes()}v/{Q.number_of_edges()}e, {d}-regular, girth={gir} > g={g} OK"
    print(info)


if __name__ == "__main__":
    for d, g in [(2, 2), (2, 3), (2, 4), (2, 6), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (5, 2)]:
        check(d, g)
    print("--- full graph realisation (small cases) ---")
    # For d >= 3 the subgroup <sigma_1,...,sigma_d> <= Sym(W) is far too large to
    # enumerate, so the graph is realised in full only for d = 2 (where the group is
    # dihedral).  For d >= 3 only the algebraic core (a) + (4.1) is machine-checked --
    # which is the entire content of the girth bound.
    for d, g in [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]:
        check(d, g, build_graph=True)
