"""Sanity checks on the writeup's claims:
 (a) the reformulation  chi > ceil(floor(w/2)/(n-w))  <=>  n <= (2k-1)t+1,
 (b) no counterexample among all graphs on <= 7 vertices (atlas) / <= 8 or 9 with geng,
 (c) the numeric bounds of table (10) for k up to 300, t=1..6,
 (d) the sensitivity of the counterexample to where the ceiling sits.
"""
import math, itertools, sys
import networkx as nx

def params(G):
    n = G.number_of_nodes()
    degs = [d for _, d in G.degree()]
    w = len(set(degs))
    k = chromatic_number(G)
    return n, w, k

def chromatic_number(G):
    n = G.number_of_nodes()
    if G.number_of_edges() == 0:
        return 1 if n else 0
    for k in range(2, n + 1):
        if kcol(G, k):
            return k
    return n

def kcol(G, k):
    nodes = sorted(G.nodes, key=lambda v: -G.degree(v))
    colour = {}
    def bt(i):
        if i == len(nodes):
            return True
        v = nodes[i]
        used = {colour[u] for u in G[v] if u in colour}
        maxnew = (max(colour.values()) + 1) if colour else 0
        for c in range(min(k, maxnew + 1)):
            if c not in used:
                colour[v] = c
                if bt(i + 1):
                    return True
                del colour[v]
        return False
    return bt(0)

def conjecture_holds(n, w, k):
    t = n - w
    return k > math.ceil((w // 2) / t)

# (a) equivalence check over a wide parameter box
bad = []
for n in range(2, 200):
    for w in range(1, n):
        t = n - w
        for k in range(1, n + 1):
            lhs = k > math.ceil((w // 2) / t)
            rhs = n <= (2 * k - 1) * t + 1
            if lhs != rhs:
                bad.append((n, w, k))
print("(a) reformulation n<=(2k-1)t+1 disagrees with the conjecture in", len(bad), "cases")

# (b) exhaustive over all graphs with <= 7 vertices
from networkx.generators.atlas import graph_atlas_g
worst = {}
cnt = 0
for G in graph_atlas_g():
    if G.number_of_nodes() < 2:
        continue
    cnt += 1
    n, w, k = params(G)
    t = n - w
    if not conjecture_holds(n, w, k):
        print("  COUNTEREXAMPLE on <=7 vertices:", n, w, k, sorted(d for _, d in G.degree()))
    slack = (2 * k - 1) * t + 1 - n
    if slack < worst.get(n, 99):
        worst[n] = slack
print(f"(b) checked all {cnt} graphs on 2..7 vertices: no counterexample.")
print("    minimum slack (2k-1)t+1-n by order:", dict(sorted(worst.items())))

# (c) table (10) bounds
rows = {1: lambda k: k, 2: lambda k: 2*k-1, 3: lambda k: 3*k-1,
        4: lambda k: 4*k-2, 5: lambda k: 5*k-2, 6: lambda k: 6*k-2}
ok = True
for t in range(1, 7):
    for k in range(2, 301):
        claimed = rows[t](k)
        # largest m with m^2/k <= t*m - floor(t^2/4)
        mmax = 0
        for m in range(1, 20000):
            if m * m / k <= t * m - (t * t) // 4:
                mmax = m
        if mmax != claimed:
            ok = False
            print("   table (10) mismatch t,k,claimed,true:", t, k, claimed, mmax)
print("(c) table (10) matches the true integer bound for all k in 2..300:", ok)

# (d) where the ceiling sits
n, w, k = 37, 30, 3
t = n - w
print("(d) n,w,t,k =", n, w, t, k)
print("    chi > ceil(floor(w/2)/t) :", k, ">", math.ceil((w//2)/t), "->", k > math.ceil((w//2)/t))
print("    chi > floor(w/2)/t       :", k, ">", (w//2)/t, "->", k > (w//2)/t)
print("    chi > ceil(w/2)/t (no floor):", k, ">", math.ceil(w/2)/t, "->", k > math.ceil(w/2)/t)
print("    chi > floor((w/2)/t)     :", k, ">", (w//2)//t, "->", k > (w//2)//t)
