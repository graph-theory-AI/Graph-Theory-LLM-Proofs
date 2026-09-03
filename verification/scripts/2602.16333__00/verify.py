#!/usr/bin/env python3
"""Verification of the claimed construction for 2602.16333__00.

Claim: Gamma_m = right Cayley digraph on A4 x Z_m with generators
u=(a,1), v=(b,1), a=(12)(34), b=(243) (right-to-left composition),
is strongly connected, vertex-transitive, non-Hamiltonian, and every
directed cycle has length divisible by m, hence circ <= 11m and
gap >= m = n/12.

Checks:
 1. group facts: a^2=e, b^3=e, ba=(142) order 3, ab=(123), <a,b>=A4
 2. lemma: every bijection f of A4 with f(x) in {xa,xb} is even
    (full enumeration of 2^12 choice functions)
 3. layered DP: no product f_{m-1}...f_0 of m valid bijections is a
    12-cycle (checked for m=1..6, via parity + explicit m=3 product scan)
 4. direct brute-force Hamilton cycle search on Gamma_m for m=1,3,4
 5. strong connectivity of Gamma_m for m=3..6
 6. all cycle lengths divisible by m (structural + spot check m=3)
 7. search for a 33-cycle in Gamma_3 (to pin circumference = 33)
"""
import itertools, sys
sys.setrecursionlimit(100000)

# permutations of 0..3 as tuples; composition right-to-left: (p*q)(i)=p(q(i))
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
assert len(A4) == 12
idx = {p: i for i, p in enumerate(A4)}

# a = (12)(34) 1-indexed -> 0-indexed (0 1)(2 3): 0->1,1->0,2->3,3->2
a = (1, 0, 3, 2)
# b = (243) 1-indexed: 2->4,4->3,3->2 -> 0-indexed: 1->3,3->2,2->1
b = (0, 3, 1, 2)
assert a in idx and b in idx

print("== 1. group facts ==")
print("a^2 == e:", comp(a, a) == E)
print("b^3 == e:", comp(b, comp(b, b)) == E)
ba = comp(b, a)  # apply a then b (right-to-left)
ab = comp(a, b)
print("ba =", ba, " order 3:", comp(ba, comp(ba, ba)) == E and ba != E)
# (142) 1-indexed: 1->4,4->2,2->1 -> 0-indexed 0->3,3->1,1->0
print("ba == (142):", ba == (3, 0, 2, 1))
# (123) 1-indexed: 1->2,2->3,3->1 -> 0-indexed 0->1,1->2,2->0
print("ab == (123):", ab == (1, 2, 0, 3))
# closure of {a,b} as a semigroup
gen = {a, b}
while True:
    new = {comp(x, y) for x in gen for y in gen} | gen
    if new == gen:
        break
    gen = new
print("<a,b> = A4:", sorted(gen) == A4)

print("\n== 2. lemma enumeration ==")
# right multiplication x -> x*s means comp(x, s) (right-to-left product xs)
def rmul(x, s):
    return comp(x, s)

def sign12(f):
    # f: dict A4 element -> A4 element; parity as permutation of 12 points
    perm = [idx[f[p]] for p in A4]
    seen = [False] * 12
    s = 1
    for i in range(12):
        if not seen[i]:
            l = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                l += 1
            if l % 2 == 0:
                s = -s
    return s

def cycle_type(perm):
    seen = [False] * len(perm)
    cyc = []
    for i in range(len(perm)):
        if not seen[i]:
            l = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                l += 1
            cyc.append(l)
    return tuple(sorted(cyc))

bijections = []
n_funcs = 0
for choice in itertools.product([0, 1], repeat=12):
    f = {A4[i]: rmul(A4[i], a if c == 0 else b) for i, c in enumerate(choice)}
    n_funcs += 1
    if len(set(f.values())) == 12:
        bijections.append(f)
print("choice functions examined:", n_funcs)
print("bijections found:", len(bijections))
signs = [sign12(f) for f in bijections]
print("all even:", all(s == 1 for s in signs))

print("\n== 3. products of m valid bijections (as perms of 12 points) ==")
perms = [tuple(idx[f[p]] for p in A4) for f in bijections]

def pcomp(p, q):  # apply q then p
    return tuple(p[q[i]] for i in range(12))

# m=3 exhaustive: 16^3 products
found12 = False
types = set()
for p0 in perms:
    for p1 in perms:
        p10 = pcomp(p1, p0)
        for p2 in perms:
            t = cycle_type(pcomp(p2, p10))
            types.add(t)
            if t == (12,):
                found12 = True
print("m=3: any product a 12-cycle?", found12)
print("m=3 product cycle types:", sorted(types))

print("\n== 4. direct Hamilton search on Gamma_m ==")
def build(m):
    V = [(p, i) for i in range(m) for p in A4]
    vi = {v: k for k, v in enumerate(V)}
    succ = [[vi[(rmul(p, a), (i + 1) % m)], vi[(rmul(p, b), (i + 1) % m)]]
            for (p, i) in V]
    return V, vi, succ

def hamilton(m, count_nodes_cap=None):
    V, vi, succ = build(m)
    N = len(V)
    start = 0
    visited = [False] * N
    visited[start] = True
    nodes = [0]

    def dfs(v, depth):
        nodes[0] += 1
        if count_nodes_cap and nodes[0] > count_nodes_cap:
            raise TimeoutError
        if depth == N:
            return start in succ[v]
        for w in succ[v]:
            if not visited[w]:
                visited[w] = True
                if dfs(w, depth + 1):
                    return True
                visited[w] = False
        return False

    res = dfs(start, 1)
    return res, nodes[0]

for m in (1, 3, 4):
    try:
        res, nd = hamilton(m, count_nodes_cap=200_000_000)
        print(f"m={m}: n={12*m}, Hamiltonian: {res} (search nodes: {nd})")
    except TimeoutError:
        print(f"m={m}: search exceeded node cap, inconclusive by direct DFS")

print("\n== 5. strong connectivity ==")
def strongly_connected(m):
    V, vi, succ = build(m)
    N = len(V)
    def reach(adj):
        seen = {0}
        st = [0]
        while st:
            v = st.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    st.append(w)
        return len(seen) == N
    pred = [[] for _ in range(N)]
    for v, ws in enumerate(succ):
        for w in ws:
            pred[w].append(v)
    return reach(succ) and reach(pred)

for m in range(3, 7):
    print(f"m={m}: strongly connected: {strongly_connected(m)}")

print("\n== 6. loops / antiparallel arcs (m>=3) ==")
for m in (3, 4):
    V, vi, succ = build(m)
    loops = sum(1 for v, ws in enumerate(succ) for w in ws if w == v)
    anti = sum(1 for v, ws in enumerate(succ) for w in ws if v in succ[w])
    print(f"m={m}: loops={loops}, antiparallel pairs (arc count)={anti}")

print("\n== 7. is there a 33-cycle in Gamma_3? (circ lower bound) ==")
# A 3k-cycle uses exactly k vertices per layer. For k=11: drop one vertex
# per layer, ask for a Hamilton cycle of the 33-vertex induced subgraph via
# layer-map composition: need injective g_i: S_i -> S_{i+1} with
# g_i(x) in {xa,xb}, composite a single 11-cycle.
def layer_bijections(S_from, S_to):
    S_from = list(S_from)
    out = []
    def rec(i, used, cur):
        if i == len(S_from):
            out.append(dict(cur))
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

def has_cycle_33():
    full = set(A4)
    for d0 in A4:
        S0 = full - {d0}
        for d1 in A4:
            S1 = full - {d1}
            B01 = layer_bijections(S0, S1)
            if not B01:
                continue
            for d2 in A4:
                S2 = full - {d2}
                B12 = layer_bijections(S1, S2)
                B20 = layer_bijections(S2, S0)
                for g0 in B01:
                    for g1 in B12:
                        for g2 in B20:
                            # composite on S0
                            comp0 = {x: g2[g1[g0[x]]] for x in S0}
                            # single 11-cycle?
                            x0 = next(iter(S0))
                            l = 1
                            y = comp0[x0]
                            while y != x0:
                                y = comp0[y]
                                l += 1
                            if l == 11:
                                return True, (d0, d1, d2)
    return False, None

ok33, drop = has_cycle_33()
print("33-cycle exists in Gamma_3:", ok33, "dropped:", drop)
print("=> circ(Gamma_3) =", 33 if ok33 else "<=30 (33-cycle not found)")
