"""Check 3: Lemma 2 — for a set S of edges of K_{n,n},
Pr(D_n[S] acyclic) = A(L(G_S)) / prod_z d_z!   (exact, by enumerating all local orders),
and this is <= prod_{uv in S}(d_u+d_v-1)/prod_z d_z!  <= (2 e^2 n / s)^s.

Also checks the identity prod_z d_z^{d_z} = prod_{uv in S} d_u d_v used in the proof.

Exhaustive enumeration for random small S (prod d_z! <= 2*10^5).
"""
import itertools, math, random

def line_graph(S):
    """S: list of edges (('x',i),('y',j)). Vertices of L: edges of S; adjacency: share endpoint."""
    L_edges = []
    for a, b in itertools.combinations(range(len(S)), 2):
        if set(S[a]) & set(S[b]):
            L_edges.append((a, b))
    return L_edges

def count_acyclic_orientations(nv, edges):
    cnt = 0
    m = len(edges)
    for mask in range(1 << m):
        arcs = [(u, v) if (mask >> i) & 1 else (v, u) for i, (u, v) in enumerate(edges)]
        indeg = [0] * nv
        out = [[] for _ in range(nv)]
        for u, v in arcs:
            indeg[v] += 1; out[u].append(v)
        q = [x for x in range(nv) if indeg[x] == 0]
        seen = 0
        indeg2 = indeg[:]
        while q:
            x = q.pop(); seen += 1
            for y in out[x]:
                indeg2[y] -= 1
                if indeg2[y] == 0: q.append(y)
        if seen == nv:
            cnt += 1
    return cnt

def exact_probability(S):
    """Enumerate all systems of local orders; count those making D[S] acyclic."""
    verts = sorted(set(v for e in S for v in e))
    inc = {z: [i for i, e in enumerate(S) if z in e] for z in verts}
    perms_per_vertex = [list(itertools.permutations(inc[z])) for z in verts]
    total = 1
    for p in perms_per_vertex: total *= len(p)
    fav = 0
    Ledges = line_graph(S)
    # which endpoint does each L-edge share?
    share = []
    for a, b in Ledges:
        z = (set(S[a]) & set(S[b])).pop()
        share.append(z)
    for system in itertools.product(*perms_per_vertex):
        rank = {}
        for z, perm in zip(verts, system):
            for pos, eidx in enumerate(perm):
                rank[(z, eidx)] = pos
        # build orientation of L
        nv = len(S)
        indeg = [0] * nv
        out = [[] for _ in range(nv)]
        for (a, b), z in zip(Ledges, share):
            if rank[(z, a)] < rank[(z, b)]:
                out[a].append(b); indeg[b] += 1
            else:
                out[b].append(a); indeg[a] += 1
        q = [x for x in range(nv) if indeg[x] == 0]
        seen = 0
        while q:
            x = q.pop(); seen += 1
            for y in out[x]:
                indeg[y] -= 1
                if indeg[y] == 0: q.append(y)
        if seen == nv:
            fav += 1
    return fav, total

if __name__ == "__main__":
    rng = random.Random(999)
    tested = 0
    while tested < 12:
        n = rng.randint(3, 5)
        pool = [(('x', i), ('y', j)) for i in range(n) for j in range(n)]
        s = rng.randint(3, 7)
        S = rng.sample(pool, s)
        verts = sorted(set(v for e in S for v in e))
        deg = {z: sum(1 for e in S if z in e) for z in verts}
        total_orders = 1
        for z in verts: total_orders *= math.factorial(deg[z])
        if total_orders > 200000:
            continue
        tested += 1
        fav, total = exact_probability(S)
        assert total == total_orders
        A = count_acyclic_orientations(len(S), line_graph(S))
        p_exact = fav / total
        # identity: prod d_z^{d_z} == prod_{uv} d_u d_v
        lhs = 1
        for z in verts: lhs *= deg[z] ** deg[z]
        rhs = 1
        for u, v in S: rhs *= deg[u] * deg[v]
        assert lhs == rhs, "product identity fails"
        bound1 = 1
        for u, v in S: bound1 *= deg[u] + deg[v] - 1
        bound1 /= total
        bound2 = (2 * math.e**2 * n / s) ** s
        assert fav == A, f"favorable ({fav}) != acyclic orientations of L(G_S) ({A})"
        assert p_exact <= bound1 + 1e-12, "Lemma 1 bound violated"
        assert bound1 <= bound2 + 1e-9, f"final Lemma 2 bound violated: {bound1} > {bound2}"
        print(f"n={n} s={s} degs={sorted(deg.values())}: Pr={p_exact:.4f} "
              f"= A(L)/prod d! ; bound prod(d_u+d_v-1)/prod d! = {bound1:.4f} ; (2e^2 n/s)^s = {bound2:.3g}")
    print("ALL CHECK3 PASSED (favorable outcomes == acyclic orientations of L(G_S); bounds hold)")
