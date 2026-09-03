#!/usr/bin/env python3
"""Positive control for the long-pyramid finder in verify_candidate.py:
build a graph that IS a long pyramid (apex + base triangle + three paths,
two of length ell) and check the finder detects it; also a negative control
where one long path is shortened."""
import verify_candidate as vc

def pyramid_graph(l1, l2, l3):
    # apex 0; path i goes 0 - internal... - base_i; base vertices form triangle
    V = [0]
    adj = {0: set()}
    def add(u, v):
        adj.setdefault(u, set()); adj.setdefault(v, set())
        adj[u].add(v); adj[v].add(u)
    bases = []
    nxt = 1
    for L in (l1, l2, l3):
        prev = 0
        for k in range(L):
            w = nxt; nxt += 1
            add(prev, w)
            prev = w
        bases.append(prev)
    add(bases[0], bases[1]); add(bases[1], bases[2]); add(bases[0], bases[2])
    V = sorted(adj)
    return V, adj

for lens, expect in [((7, 7, 3), True), ((7, 4, 3), False), ((7, 7, 7), True)]:
    V, adj = pyramid_graph(*lens)
    res = vc.find_long_pyramids(V, adj, ell=7, verbose=False)
    print(f"path lengths {lens}: pyramid found = {bool(res)} (expected {expect})")
    assert bool(res) == expect
print("pyramid finder controls passed")
