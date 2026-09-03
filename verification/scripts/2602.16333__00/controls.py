#!/usr/bin/env python3
"""Positive/negative controls for the Hamilton search used in verify.py,
plus the opposite multiplication convention, plus exact circumference of
Gamma_m for m=3,4 via layered analysis, plus Held-Karp check for m=1."""
import itertools, sys
sys.setrecursionlimit(100000)

def comp(p, q):
    return tuple(p[q[i]] for i in range(4))

E = (0, 1, 2, 3)

def sign4(p):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    return s

A4 = sorted(p for p in itertools.permutations(range(4)) if sign4(p) == 1)
a = (1, 0, 3, 2)   # (12)(34)
b = (0, 3, 1, 2)   # (243)

def hamilton_generic(N, succ, start=0):
    visited = [False] * N
    visited[start] = True
    nodes = [0]
    def dfs(v, depth):
        nodes[0] += 1
        if depth == N:
            return start in succ[v]
        for w in succ[v]:
            if not visited[w]:
                visited[w] = True
                if dfs(w, depth + 1):
                    return True
                visited[w] = False
        return False
    return dfs(start, 1), nodes[0]

def build_group_layered(elems, gens, m, mul):
    V = [(p, i) for i in range(m) for p in elems]
    vi = {v: k for k, v in enumerate(V)}
    succ = [[vi[(mul(p, g), (i + 1) % m)] for g in gens] for (p, i) in V]
    return V, succ

print("== control 1: directed cycle C_12 (Hamiltonian, unique) ==")
N = 12
succ = [[(i + 1) % N] for i in range(N)]
print(hamilton_generic(N, succ))

print("== control 2: Cay(Z12 x Z_3, {(1,1),(2,1)}) ==")
Z12 = list(range(12))
V, succ = build_group_layered(Z12, [1, 2], 3, lambda p, g: (p + g) % 12)
res, nd = hamilton_generic(len(V), succ)
print("Hamiltonian:", res, "nodes:", nd)

print("== control 3: Cay(A4 x Z_3, {((123),1), ((124),1)}) ==")
c1 = (1, 2, 0, 3)  # (123): 0->1,1->2,2->0
c2 = (1, 3, 2, 0)  # (124) 1-indexed: 1->2,2->4,4->1 -> 0-indexed 0->1,1->3,3->0
assert sign4(c1) == 1 and sign4(c2) == 1
V, succ = build_group_layered(A4, [c1, c2], 3, comp)
res, nd = hamilton_generic(len(V), succ)
print("Hamiltonian:", res, "nodes:", nd)

print("== control 4: left-multiplication convention, Cay with x -> sx ==")
for m in (1, 3):
    V, succ = build_group_layered(A4, [a, b], m, lambda p, g: comp(g, p))
    res, nd = hamilton_generic(len(V), succ)
    print(f"m={m}: Hamiltonian (arcs x->ax, x->bx):", res, "nodes:", nd)

print("== control 5: Held-Karp style exact check m=1 (independent) ==")
idx = {p: i for i, p in enumerate(A4)}
succ1 = [[idx[comp(p, a)], idx[comp(p, b)]] for p in A4]
# DP over subsets from vertex 0
import functools
N = 12
full = (1 << N) - 1
reach = {(1, 0)}  # (mask, v) reachable path states starting at 0
frontier = {(1, 0)}
ham = False
seen = set(frontier)
while frontier:
    nf = set()
    for mask, v in frontier:
        for w in succ1[v]:
            if mask == full and w == 0:
                ham = True
            if not (mask >> w) & 1:
                st = (mask | (1 << w), w)
                if st not in seen:
                    seen.add(st)
                    nf.add(st)
    frontier = nf
print("Cay(A4,{a,b}) Hamiltonian (BFS over subset-states):", ham,
      "states:", len(seen))

print("== exact circumference of Gamma_3 and Gamma_4 ==")
# cycle of length k*m uses exactly k vertices per layer; search over k
def rmul(x, s):
    return comp(x, s)

def layer_maps(S_from, S_to):
    S_from = list(S_from)
    out = []
    def rec(i, used, cur):
        if i == len(S_from):
            out.append(tuple(cur))
            return
        x = S_from[i]
        for s in (a, b):
            y = rmul(x, s)
            if y in S_to and y not in used:
                used.add(y)
                cur.append((x, y))
                rec(i + 1, used, cur)
                cur.pop()
                used.remove(y)
    rec(0, set(), [])
    return out

def exists_cycle(k, m):
    # choose k-subsets S_0,...,S_{m-1} of A4 and bijections g_i:S_i->S_{i+1}
    # with composite a single k-cycle.  DFS over layers keeping the set of
    # achievable maps S_0 -> S_i.
    from itertools import combinations
    subsets = list(combinations(A4, k))
    # to keep this tractable only for m<=4, k close to 12
    def rec(i, S0, Si, maps):
        # maps: set of tuples of (x in S0 -> current image) as tuple ordered by S0
        if i == m:
            if Si != S0:
                return False
            for mp in maps:
                # mp is tuple of images of S0 in order; check single k-cycle
                pos = {x: j for j, x in enumerate(S0)}
                perm = [pos[y] for y in mp]
                l, j = 0, 0
                seenl = [False] * k
                while not seenl[j]:
                    seenl[j] = True
                    j = perm[j]
                    l += 1
                if l == k:
                    return True
            return False
        for Snext in subsets:
            for g in layer_maps(Si, set(Snext)):
                gd = dict(g)
                nmaps = {tuple(gd[y] for y in mp) for mp in maps}
                if rec(i + 1, S0, Snext, nmaps):
                    return True
        return False
    for S0 in subsets:
        if rec(1, S0, S0, {S0})if False else None:
            pass
    # simpler correct driver:
    for S0 in subsets:
        if rec_driver(S0, k, m):
            return True
    return False

def rec_driver(S0, k, m):
    from functools import lru_cache
    def rec(i, Si, maps):
        if i == m:
            if Si != S0:
                return False
            pos = {x: j for j, x in enumerate(S0)}
            for mp in maps:
                perm = [pos[y] for y in mp]
                l, j = 0, 0
                seenl = [False] * k
                while not seenl[j]:
                    seenl[j] = True
                    j = perm[j]
                    l += 1
                if l == k:
                    return True
            return False
        from itertools import combinations
        for Snext in combinations(A4, k):
            gs = layer_maps(Si, set(Snext))
            if not gs:
                continue
            for g in gs:
                gd = dict(g)
                nmaps = {tuple(gd[y] for y in mp) for mp in maps}
                if rec(i + 1, Snext, nmaps):
                    return True
        return False
    return rec(1, S0, {S0})

for m in (3,):
    best = 0
    for k in range(11, 0, -1):
        if exists_cycle(k, m):
            best = k * m
            break
    print(f"m={m}: circumference = {best} (n={12*m}, gap={12*m-best})")
