"""Cross-validate my attractor solver against the previous campaign's
independent dict-based fixed-point solver on random small graphs."""
import sys, random, itertools
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2008.03587__00')
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification/scripts/2008.03587__01')
from zgame import zombie_number as zn_mine
from zombie import zombie_number as zn_theirs, bfs_dist

random.seed(7)
bad = 0
for trial in range(120):
    n = random.randint(4, 9)
    while True:
        edges = [(i, j) for i in range(n) for j in range(i+1, n) if random.random() < 0.35]
        adj = {v: set() for v in range(n)}
        for u, v in edges:
            adj[u].add(v); adj[v].add(u)
        if len(bfs_dist(adj, 0)) == n:
            break
    mine = zn_mine([sorted(adj[v]) for v in range(n)], kmax=4)
    theirs = zn_theirs(adj, kmax=4)
    if mine != theirs:
        bad += 1
        print("MISMATCH", n, sorted(edges), mine, theirs)
print(f"cross-check on 120 random connected graphs: {bad} mismatches")
