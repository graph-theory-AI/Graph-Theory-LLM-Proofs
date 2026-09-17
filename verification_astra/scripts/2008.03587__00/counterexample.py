"""Verify the writeup's 59-vertex cactus counterexample for arXiv:2008.03587 Q4.1.

G : path v0..v10, with a 25-cycle attached at v0, a 17-cycle at v2, a 9-cycle
    at v4 (each cycle *includes* its attachment vertex).  |V(G)| = 59.
H : G plus a pendant vertex v11 adjacent to v10.  |V(H)| = 60.

Claim under review: z(G) >= 3 and z(H) = 2.
"""
import sys, itertools
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2008.03587__00')
from zgame import solve, winning_placements, all_dist


def build(pendant=False):
    names = []
    idx = {}
    def add(name):
        idx[name] = len(names); names.append(name); return idx[name]
    npath = 12 if pendant else 11
    for i in range(npath):
        add(('v', i))
    edges = [(idx[('v', i)], idx[('v', i + 1)]) for i in range(npath - 1)]
    # cycles: (length, attachment path index, tag)
    for length, at, tag in [(25, 0, 'A'), (17, 2, 'B'), (9, 4, 'C')]:
        ring = [idx[('v', at)]] + [add((tag, j)) for j in range(1, length)]
        for j in range(length):
            edges.append((ring[j], ring[(j + 1) % length]))
    adj = [set() for _ in names]
    for u, v in edges:
        assert u != v and v not in adj[u], (u, v)
        adj[u].add(v); adj[v].add(u)
    return [sorted(a) for a in adj], names, idx


G, gn, gi = build(False)
H, hn, hi = build(True)
print("|V(G)| =", len(G), " |E(G)| =", sum(len(a) for a in G) // 2)
print("|V(H)| =", len(H), " |E(H)| =", sum(len(a) for a in H) // 2)
print("degree sequence G:", sorted({v: len(a) for v, a in enumerate(G)}.values(), reverse=True)[:6])
print("H = G + leaf v11 at v10 :", len(H) == len(G) + 1 and len(H[hi[('v', 11)]]) == 1
      and H[hi[('v', 11)]] == [hi[('v', 10)]])
# cactus check: every edge in at most one cycle <=> #edges = #vertices - 1 + #cycles
print("cactus (n-1+3 edges):", sum(len(a) for a in G) // 2 == len(G) - 1 + 3)

for name, adj in (("G", G), ("H", H)):
    for k in (1, 2):
        w = winning_placements(adj, k, limit=3)
        print(f"{name}: k={k} winning placements found: {len(w)}"
              + ("" if not w else "  e.g. " + str([tuple((gn if name=='G' else hn)[x] for x in p) for p in w])))

# the writeup's explicit strategy on H
Zwin, n, pw = solve(H, 2)
p = (hi[('v', 0)], hi[('v', 11)])
base = p[0] * pw[2] + p[1] * pw[1]
bad = [hn[s] for s in range(n) if not Zwin[base + s]]
print("H: placement (v0, v11) beats every survivor start:", not bad, "failures:", bad[:5])
