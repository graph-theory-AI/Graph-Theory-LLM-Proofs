#!/usr/bin/env python3
"""Verify the upper-bound claim for s=2, k=2: on K_5 = K_{s^k+1} with the
constant list assignment L(e) = {1,2}, EVERY L-coloring (i.e. every 2-coloring
of E(K_5)) has a color class with chromatic number > 2 (i.e. non-bipartite),
hence contains a monochromatic member of H_2 (odd cycle).
Also verify the classical fact on K_4 there IS a 2-coloring with both classes
bipartite (so s^k+1 is the right threshold).
"""
import itertools

def is_bipartite(n, edges):
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    color=[-1]*n
    for s in range(n):
        if color[s]!=-1: continue
        color[s]=0; st=[s]
        while st:
            x=st.pop()
            for y in adj[x]:
                if color[y]==-1: color[y]=1-color[x]; st.append(y)
                elif color[y]==color[x]: return False
    return True

def check(n):
    E = list(itertools.combinations(range(n),2))
    bad = 0
    for mask in range(1<<len(E)):
        c0 = [E[i] for i in range(len(E)) if not(mask>>i&1)]
        c1 = [E[i] for i in range(len(E)) if mask>>i&1]
        if is_bipartite(n,c0) and is_bipartite(n,c1):
            bad += 1
    return bad

good_k5 = check(5)
print(f"K_5: 2-colorings with both classes bipartite: {good_k5} out of {1<<10}")
assert good_k5 == 0, "upper bound claim fails"
print("VERIFIED: every 2-coloring of E(K_5) has a non-bipartite class "
      "=> R_ell(H_2,2) <= R(H_2,2) <= 5")

good_k4 = check(4)
print(f"K_4: 2-colorings with both classes bipartite: {good_k4} out of {1<<6}")
assert good_k4 > 0
print("Sanity: K_4 admits such colorings (constant-list case of the lemma).")
