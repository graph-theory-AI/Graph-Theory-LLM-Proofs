"""Check 1: the construction D_n (random locally-transitive orientation of L(K_{n,n})).

Verifies, for sampled random orders (several seeds) and n up to 8:
  (a) the underlying graph of D_n is the rook graph = L(K_{n,n});
  (b) the underlying graph is claw-free (no induced K_{1,3}), hence K_{1,4}-free;
  (c) D_n has no directed triangle;
  (d) every row/column clique is transitively oriented;
  (e) D_n has no induced copy of Delta(1,m,m') for small m,m' (direct check, n=5);
  (f) Delta(1,m,m') contains a directed triangle for all 1<=m,m'<=4.
"""
import itertools, random

def build_Dn(n, seed):
    rng = random.Random(seed)
    # vertices of D_n: edges (x,y) of K_{n,n}, x row in range(n), y col in range(n)
    V = [(x, y) for x in range(n) for y in range(n)]
    # random linear order at each row x and each column y: rank of edge
    row_rank = []
    for x in range(n):
        perm = list(range(n)); rng.shuffle(perm)
        row_rank.append({y: perm[y] for y in range(n)})  # rank of edge (x,y) in order <_x
    col_rank = []
    for y in range(n):
        perm = list(range(n)); rng.shuffle(perm)
        col_rank.append({x: perm[x] for x in range(n)})
    arcs = set()
    for e, f in itertools.combinations(V, 2):
        (x1, y1), (x2, y2) = e, f
        if x1 == x2:  # share row endpoint
            if row_rank[x1][y1] < row_rank[x1][y2]: arcs.add((e, f))
            else: arcs.add((f, e))
        elif y1 == y2:  # share column endpoint
            if col_rank[y1][x1] < col_rank[y1][x2]: arcs.add((e, f))
            else: arcs.add((f, e))
    return V, arcs

def underlying(arcs):
    return set(frozenset(a) for a in arcs)

def is_rook_graph_edges(V, und, n):
    expected = set()
    for e, f in itertools.combinations(V, 2):
        if e[0] == f[0] or e[1] == f[1]:
            expected.add(frozenset((e, f)))
    return und == expected

def clawfree(V, und):
    adj = {v: set() for v in V}
    for ed in und:
        a, b = tuple(ed); adj[a].add(b); adj[b].add(a)
    for c in V:
        nb = sorted(adj[c])
        for trio in itertools.combinations(nb, 3):
            if all(frozenset((p, q)) not in und for p, q in itertools.combinations(trio, 2)):
                return False, (c, trio)
    return True, None

def directed_triangles(V, arcs):
    A = {v: set() for v in V}
    for u, w in arcs: A[u].add(w)
    count = 0
    for u in V:
        for v in A[u]:
            for w in A[v]:
                if u in A[w]:
                    count += 1
    return count  # counts each directed triangle 3 times

def check_local_transitive(V, arcs, n):
    A = set(arcs)
    ok = True
    for x in range(n):
        clique = [(x, y) for y in range(n)]
        for a, b, c in itertools.permutations(clique, 3):
            if (a, b) in A and (b, c) in A and (a, c) not in A:
                ok = False
    for y in range(n):
        clique = [(x, y) for x in range(n)]
        for a, b, c in itertools.permutations(clique, 3):
            if (a, b) in A and (b, c) in A and (a, c) not in A:
                ok = False
    return ok

def delta(m1, m2, m3):
    """Delta(m1,m2,m3): cyclic join of transitive tournaments TT_m1, TT_m2, TT_m3."""
    V = [(i, j) for i, blk in enumerate((m1, m2, m3)) for j in range(blk)]
    arcs = set()
    for (i, j), (i2, j2) in itertools.permutations(V, 2):
        if i == i2:
            if j < j2: arcs.add(((i, j), (i2, j2)))
        elif (i, i2) in {(0, 1), (1, 2), (2, 0)}:
            arcs.add(((i, j), (i2, j2)))
    return V, arcs

def has_directed_triangle(V, arcs):
    return directed_triangles(V, arcs) > 0

def contains_induced(DV, Darcs, HV, Harcs):
    """Does digraph D contain an induced copy of H? Brute force over injections."""
    DA = set(Darcs)
    k = len(HV)
    for combo in itertools.combinations(DV, k):
        for perm in itertools.permutations(combo):
            m = dict(zip(HV, perm))
            good = True
            for u, v in itertools.permutations(HV, 2):
                inH = (u, v) in Harcs
                inD = (m[u], m[v]) in DA
                if inH != inD:
                    good = False; break
            if good:
                return True
    return False

if __name__ == "__main__":
    for n, seed in [(5, 1), (6, 2), (8, 3)]:
        V, arcs = build_Dn(n, seed)
        und = underlying(arcs)
        assert len(arcs) == len(und), "digon or duplicate found"
        assert is_rook_graph_edges(V, und, n), "underlying graph is not the rook graph"
        cf, wit = clawfree(V, und)
        assert cf, f"claw found: {wit}"
        t = directed_triangles(V, arcs)
        assert t == 0, f"directed triangle count {t}"
        assert check_local_transitive(V, arcs, n)
        print(f"n={n} seed={seed}: |V|={len(V)}, arcs={len(arcs)}, rook graph OK, "
              f"claw-free OK, directed triangles = {t}, local cliques transitive OK")

    # (f) Delta(1,m,m') contains a directed triangle
    for m in range(1, 5):
        for mp in range(1, 5):
            DV, DA = delta(1, m, mp)
            assert has_directed_triangle(DV, DA), (m, mp)
    print("Delta(1,m,m') contains a directed triangle for all 1<=m,m'<=4: OK")

    # (e) direct induced-subdigraph check on n=5 for the smallest Deltas
    V, arcs = build_Dn(5, 1)
    for (m, mp) in [(1, 1), (1, 2), (2, 1)]:
        HV, HA = delta(1, m, mp)
        found = contains_induced(V, arcs, HV, HA)
        print(f"induced Delta(1,{m},{mp}) in D_5? {found}")
        assert not found
    print("ALL CHECK1 PASSED")
