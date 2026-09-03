"""Check 2: Lemma 1 — acyclic orientations of a graph Q are determined by their
indegree sequence, and hence A(Q) <= prod_v (d_Q(v)+1).

Exhaustive over: all graphs on <=5 vertices (via edge subsets of K_5), plus
200 random graphs on 6-7 vertices with <=13 edges.
"""
import itertools, random

def acyclic_orientations(V, edges):
    """Enumerate all acyclic orientations; return list of (orientation, indegree tuple)."""
    res = []
    m = len(edges)
    for mask in range(1 << m):
        arcs = []
        for i, (u, v) in enumerate(edges):
            arcs.append((u, v) if (mask >> i) & 1 else (v, u))
        # acyclicity via repeated source removal
        indeg = {x: 0 for x in V}
        out = {x: [] for x in V}
        for u, v in arcs:
            indeg[v] += 1; out[u].append(v)
        order = [x for x in V if indeg[x] == 0]
        seen = 0
        q = list(order)
        indeg2 = dict(indeg)
        while q:
            x = q.pop(); seen += 1
            for y in out[x]:
                indeg2[y] -= 1
                if indeg2[y] == 0: q.append(y)
        if seen == len(V):
            res.append((mask, tuple(indeg[x] for x in V)))
    return res

def check(V, edges):
    aos = acyclic_orientations(V, edges)
    A = len(aos)
    seqs = set(t for _, t in aos)
    assert len(seqs) == A, f"two acyclic orientations share an indegree sequence: {V} {edges}"
    deg = {x: 0 for x in V}
    for u, v in edges: deg[u] += 1; deg[v] += 1
    bound = 1
    for x in V: bound *= deg[x] + 1
    assert A <= bound, f"A(Q)={A} > prod(d+1)={bound} for {edges}"
    return A, bound

if __name__ == "__main__":
    # all graphs on 5 vertices
    V = list(range(5))
    all_edges = list(itertools.combinations(V, 2))
    worst = 0.0
    cnt = 0
    for mask in range(1 << len(all_edges)):
        edges = [e for i, e in enumerate(all_edges) if (mask >> i) & 1]
        A, bound = check(V, edges)
        worst = max(worst, A / bound)
        cnt += 1
    print(f"all {cnt} graphs on 5 vertices: indegree-injectivity OK, A<=prod(d+1) OK, max ratio {worst:.3f}")

    rng = random.Random(12345)
    for t in range(200):
        nV = rng.choice([6, 7])
        V = list(range(nV))
        pool = list(itertools.combinations(V, 2))
        m = rng.randint(1, min(13, len(pool)))
        edges = rng.sample(pool, m)
        check(V, edges)
    print("200 random graphs on 6-7 vertices: OK")
    print("ALL CHECK2 PASSED")
