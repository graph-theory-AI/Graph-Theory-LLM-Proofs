"""Robustness: is the mechanism generic?  Scale the construction down."""
import sys, itertools
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2008.03587__00')
from zgame import winning_placements

def build(L, roots, pendant):
    """path v0..vL (+ pendant v_{L+1}); at each root r a cycle of length 2*(L+1-2r)+3."""
    n = L + 1 + (1 if pendant else 0)
    adj = [set() for _ in range(n)]
    def add(u, v):
        while max(u, v) >= len(adj): adj.append(set())
        adj[u].add(v); adj[v].add(u)
    for i in range(n - 1): add(i, i + 1)
    for r in roots:
        length = 2 * (L + 1 - 2 * r) + 3
        ring = [r] + [len(adj) + j for j in range(length - 1)]
        for j in range(length - 1): adj.append(set())
        for j in range(length): add(ring[j], ring[(j + 1) % length])
    return [sorted(a) for a in adj]

for L in (6, 8, 10):
    roots = [r for r in (0, 2, 4) if 2 * (L + 1 - 2 * r) + 3 >= 3]
    G = build(L, roots, False); H = build(L, roots, True)
    lens = [2 * (L + 1 - 2 * r) + 3 for r in roots]
    g2 = len(winning_placements(G, 2, limit=1)); h2 = len(winning_placements(H, 2, limit=1))
    h1 = len(winning_placements(H, 1, limit=1))
    print(f"L={L} cycles={lens} |V(G)|={len(G)} : 2 zombies win on G? {bool(g2)}"
          f" | 1 wins on H? {bool(h1)} | 2 win on H? {bool(h2)}"
          f" -> counterexample: {bool(h2) and not bool(g2)}")

# variant: drop one of the three cycles from the 59-vertex graph
for keep in ([0,2],[0,4],[2,4],[0],[2],[4]):
    G = build(10, keep, False); H = build(10, keep, True)
    g2 = bool(winning_placements(G, 2, limit=1)); h2 = bool(winning_placements(H, 2, limit=1))
    print(f"roots kept {keep}: 2 win on G? {g2} | 2 win on H? {h2} -> counterexample: {h2 and not g2}")
