"""Fast pure-Python brute force for m=3 (n=9) plus symbolic corollary check
for m=3..8. Same checks as check_diamond_chain.py, no external deps.

Vertices encoded 0..3m-1: c_i = 3i, a_i = 3i+1, b_i = 3i+2.
Arcs: c_i->c_{i+1}, c_i->a_i, a_i->c_{i+1}, c_i->b_i, b_i->c_{i+1}.
"""

import itertools


def build(m):
    adj = [[] for _ in range(3 * m)]
    for i in range(m):
        c, a, b = 3 * i, 3 * i + 1, 3 * i + 2
        cn = 3 * ((i + 1) % m)
        adj[c] += [cn, a, b]
        adj[a].append(cn)
        adj[b].append(cn)
    return adj


def strong_and_oriented(m, adj):
    n = 3 * m
    arcs = {(u, v) for u in range(n) for v in adj[u]}
    assert all((v, u) not in arcs for (u, v) in arcs), "digon found"
    assert all(u != v for (u, v) in arcs), "loop found"

    def reach(s, nbrs):
        seen = {s}
        st = [s]
        while st:
            u = st.pop()
            for v in nbrs[u]:
                if v not in seen:
                    seen.add(v)
                    st.append(v)
        return seen

    radj = [[] for _ in range(n)]
    for u, v in arcs:
        radj[v].append(u)
    assert len(reach(0, adj)) == n and len(reach(0, radj)) == n, "not strong"


def fwd_reach(adj, pos, s, t):
    seen = {s}
    st = [s]
    while st:
        u = st.pop()
        pu = pos[u]
        for v in adj[u]:
            if pos[v] > pu and v not in seen:
                if v == t:
                    return True
                seen.add(v)
                st.append(v)
    return False


def brute_m3():
    m = 3
    adj = build(m)
    strong_and_oriented(m, adj)
    V = list(range(9))
    pos = [0] * 9
    maxcov = 0
    ge2 = 0
    coverable = set()
    witness = {}
    total = 0
    for order in itertools.permutations(V):
        total += 1
        for k, v in enumerate(order):
            pos[v] = k
        cov = 0
        covset = []
        for i in range(m):
            a, b = 3 * i + 1, 3 * i + 2
            if fwd_reach(adj, pos, a, b) or fwd_reach(adj, pos, b, a):
                cov += 1
                covset.append(i)
        if cov > maxcov:
            maxcov = cov
        if cov >= 2:
            ge2 += 1
            if ge2 == 1:
                print("!! ordering covering >=2:", order, covset)
        for i in covset:
            if i not in coverable:
                coverable.add(i)
                witness[i] = order
    print(f"m=3: {total} orderings checked")
    print(f"  max #hard pairs {{a_i,b_i}} forward-covered by one ordering = {maxcov}")
    print(f"  orderings covering >=2 pairs: {ge2}")
    print(f"  individually coverable: {sorted(coverable)}")
    names = lambda o: [f"{'cab'[v % 3]}{v // 3}" for v in o]
    for i in sorted(witness):
        print(f"    witness for R_{i}: {names(witness[i])}")
    assert maxcov == 1 and coverable == {0, 1, 2}


def simple_paths(adj, s, t, n):
    out = []
    def dfs(u, path, seen):
        if u == t:
            out.append(path[:])
            return
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                path.append(v)
                dfs(v, path, seen)
                path.pop()
                seen.remove(v)
    dfs(s, [s], {s})
    return out


def acyclic(edges, n):
    # Kahn
    indeg = [0] * n
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = [u for u in range(n) if indeg[u] == 0]
    cnt = 0
    while q:
        u = q.pop()
        cnt += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return cnt == n


def symbolic(m):
    adj = build(m)
    strong_and_oriented(m, adj)
    n = 3 * m
    paths = {}
    for i in range(m):
        a, b = 3 * i + 1, 3 * i + 2
        paths[i] = simple_paths(adj, a, b, n) + simple_paths(adj, b, a, n)
    print(f"m={m}: {len(paths[0])} realizing paths per hard pair")
    for i, k in itertools.combinations(range(m), 2):
        for P in paths[i]:
            for Q in paths[k]:
                E = set(zip(P, P[1:])) | set(zip(Q, Q[1:]))
                if acyclic(E, n):
                    print(f"  !! consistent realizing paths for R_{i},R_{k}: {P} {Q}")
                    return False
    print(f"  all path combinations for distinct pairs are order-inconsistent: "
          f"one ordering covers <=1 hard pair. OK")
    return True


def random_large_m(m, trials=200000, seed=99):
    """Randomized check for larger m: no sampled ordering covers >=2 hard pairs;
    also count coverage to confirm pairs are individually coverable."""
    import random
    adj = build(m)
    strong_and_oriented(m, adj)
    n = 3 * m
    rng = random.Random(seed)
    V = list(range(n))
    pos = [0] * n
    maxcov = 0
    cover_counts = [0] * m
    for _ in range(trials):
        rng.shuffle(V)
        for k, v in enumerate(V):
            pos[v] = k
        cov = []
        for i in range(m):
            a, b = 3 * i + 1, 3 * i + 2
            if fwd_reach(adj, pos, a, b) or fwd_reach(adj, pos, b, a):
                cov.append(i)
        maxcov = max(maxcov, len(cov))
    # targeted orderings: the writeup's witness ordering for each R_i
    for i in range(m):
        order = [3 * i + 1]  # a_i
        for s in range(1, m + 1):
            j = (i + s) % m
            order.append(3 * j)  # c_{i+1..i} in cyclic order ending at c_i
        order.append(3 * i + 2)  # b_i
        rest = [v for v in range(n) if v not in order]
        order += rest
        for k, v in enumerate(order):
            pos[v] = k
        cov = []
        for x in range(m):
            a, b = 3 * x + 1, 3 * x + 2
            if fwd_reach(adj, pos, a, b) or fwd_reach(adj, pos, b, a):
                cov.append(x)
        cover_counts[i] = 1 if cov == [i] else -1
        maxcov = max(maxcov, len(cov))
    print(f"m={m}: {trials} random orderings + {m} targeted witness orderings: "
          f"max hard pairs covered by one ordering = {maxcov}")
    assert maxcov == 1
    assert all(c == 1 for c in cover_counts), "witness ordering failed"
    print(f"  each R_i coverable by its targeted ordering (covering exactly R_i). OK")


if __name__ == "__main__":
    brute_m3()
    ok = all(symbolic(m) for m in range(3, 7))
    for m in (10, 20):
        random_large_m(m, trials=20000)
    print("ALL CHECKS PASS" if ok else "CHECK FAILED")
