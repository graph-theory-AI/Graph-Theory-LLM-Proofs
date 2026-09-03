"""Exact search: does G_4 (writeup's construction, k=4) admit a modular
4-edge-colouring with m colours?  Writeup's lemma predicts NO for m = 4
(bound: chi'_4 >= ceil(28/6) = 5).  We decide m=4 exactly with a generic
backtracking solver that does NOT use the lemma's reasoning, then look for
a valid colouring at m=5,6,7 to confirm the encoding is satisfiable at all.

Generic pruning: for each vertex, given current per-colour counts and the
number r of its not-yet-coloured edges, check by DP whether finals
f_c in {0} u {1+jk} with f_c >= current count (and f_c = count required if
colour c already closed... we don't track closure, so just f_c >= count,
f_c <= count + r) can sum to d(v). Sound relaxation; exact at r = 0.
"""
import sys
from functools import lru_cache

k = 4


def build(k):
    X = [("x", i) for i in range(2 * k)]
    H = [("h", i) for i in range(k // 2)]
    L = [("l", i) for i in range(k)]
    S = set(range(k // 2))
    edges = []
    for h in H:
        for x in X:
            edges.append((h, x))
    for x in X:
        for l in L:
            if (l[1] - (x[1] % k)) % k in S:
                edges.append((x, l))
    return X + H + L, edges


V, edges = build(k)
deg = {v: 0 for v in V}
for a, b in edges:
    deg[a] += 1
    deg[b] += 1
vid = {v: i for i, v in enumerate(V)}
E = [(vid[a], vid[b]) for a, b in edges]
D = [deg[v] for v in V]
NV, NE = len(V), len(E)
print(f"k={k}: {NV} vertices, {NE} edges, degrees {sorted(set(D))}")

# order edges to finish vertices quickly: sort by vertex blocks
order = sorted(range(NE), key=lambda i: (min(E[i]), max(E[i])))
E = [E[i] for i in order]


def solve(m):
    # counts[v][c]; rem[v] = uncoloured edges at v
    counts = [[0] * m for _ in range(NV)]
    rem = list(D)

    @lru_cache(maxsize=None)
    def feasible_key(cnts, r, d):
        # cnts: sorted tuple of per-colour counts; can finals sum to d?
        # DP over colours: possible total "extra" amounts
        target = d - sum(cnts)
        if target != r:  # extras must total exactly r
            # note sum(finals) = d and finals = cnts + extras => extras sum to d - sum(cnts) = r always
            return False
        poss = {0}
        for c in cnts:
            opts = set()
            for f in range(c, c + r + 1):
                if f == 0 or f % k == 1 % k:
                    opts.add(f - c)
            if not opts:
                return False
            poss = {p + o for p in poss for o in opts if p + o <= r}
            if not poss:
                return False
        return r in poss

    def vfeas(v):
        return feasible_key(tuple(sorted(counts[v])), rem[v], D[v])

    sys.setrecursionlimit(10000)
    nodes = 0

    def dfs(i, maxc):
        nonlocal nodes
        nodes += 1
        if i == NE:
            return True
        a, b = E[i]
        for c in range(min(maxc + 1, m)):
            counts[a][c] += 1
            counts[b][c] += 1
            rem[a] -= 1
            rem[b] -= 1
            if vfeas(a) and vfeas(b) and dfs(i + 1, max(maxc, c + 1)):
                return True
            counts[a][c] -= 1
            counts[b][c] -= 1
            rem[a] += 1
            rem[b] += 1
        return False

    ok = dfs(0, 0)
    return ok, nodes


for m in [4, 5, 6]:
    ok, nodes = solve(m)
    print(f"m={m}: {'COLOURING FOUND' if ok else 'NO valid colouring'}  ({nodes} search nodes)")
    if m == 4:
        assert not ok, "FATAL: lemma predicted no 4-colouring but one exists!"
