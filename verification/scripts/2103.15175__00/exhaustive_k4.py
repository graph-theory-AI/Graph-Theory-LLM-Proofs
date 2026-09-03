#!/usr/bin/env python3
"""Exhaustive verification of the lower-bound claim for s=2, k=2, n=4 = s^k.

Claim (writeup, Lower bound section): for EVERY 2-list assignment L on E(K_4),
there is an L-coloring in which every color class is 2-colorable (bipartite).
This shows R_ell(H_2, 2) > 4 = s^k.

We enumerate ALL list assignments up to color isomorphism using a
restricted-growth canonical form (colors are named 0,1,2,... in order of
first appearance), and for each we brute-force over all 2^6 = 64 L-colorings,
checking every color class for bipartiteness via a precomputed table over the
2^6 edge subsets of K_4.  This check is fully independent of the writeup's
greedy method.
"""
import itertools, sys

EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
NE = len(EDGES)

def is_bipartite(mask):
    adj = [[] for _ in range(4)]
    for idx,(u,v) in enumerate(EDGES):
        if mask >> idx & 1:
            adj[u].append(v); adj[v].append(u)
    color = [-1]*4
    for s in range(4):
        if color[s] != -1: continue
        color[s] = 0; stack=[s]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if color[y] == -1:
                    color[y] = 1-color[x]; stack.append(y)
                elif color[y] == color[x]:
                    return False
    return True

BIP = [is_bipartite(m) for m in range(1<<NE)]

def good_coloring_exists(lists):
    for choice in itertools.product(range(2), repeat=NE):
        classes = {}
        for e,ch in enumerate(choice):
            c = lists[e][ch]
            classes[c] = classes.get(c,0) | (1<<e)
        if all(BIP[m] for m in classes.values()):
            return True
    return False

def canonical_assignments():
    """Yield all 6-tuples of 2-element color lists (a,b), a<b, in
    restricted-growth canonical form.  With `used` colors seen so far,
    an edge's list is one of:
      - {a,b} with a<b<used            (both colors old)
      - {a,used} with a<used           (one new color)
      - {used, used+1}                 (two new colors)
    Every list assignment is color-isomorphic to a canonical one."""
    def rec(e, used, acc):
        if e == NE:
            yield tuple(acc); return
        for a in range(used):
            for b in range(a+1, used):
                acc.append((a,b)); yield from rec(e+1, used, acc); acc.pop()
        for a in range(used):
            acc.append((a,used)); yield from rec(e+1, used+1, acc); acc.pop()
        acc.append((used, used+1)); yield from rec(e+1, used+2, acc); acc.pop()
    yield from rec(0, 0, [])

def main():
    total = 0; failures = 0
    for lists in canonical_assignments():
        total += 1
        if not good_coloring_exists(lists):
            failures += 1
            print("FAILURE (forcing assignment found):", lists)
    print(f"canonical 2-list assignments on E(K_4) checked: {total}")
    print(f"assignments with NO good coloring (would refute claim): {failures}")
    if failures == 0:
        print("VERIFIED: every 2-list assignment on K_4 admits an L-coloring "
              "with all color classes bipartite => R_ell(H_2,2) > 4")
    else:
        print("CLAIM REFUTED"); sys.exit(1)

if __name__ == "__main__":
    main()
