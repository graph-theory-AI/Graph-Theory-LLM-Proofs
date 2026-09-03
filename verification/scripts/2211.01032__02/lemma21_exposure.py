"""Check Lemma 2.1: for a uniform random d-cycle pi, condition on k exposed
arcs (extendible to a d-cycle); then for x with unexposed image, pi(x) is
uniform over the d-k-1 admissible points (initial points of other path
components). Full enumeration for d=6, several exposure patterns.
"""
import itertools
from collections import Counter

d = 6
pts = list(range(d))
cycles = []
for perm in itertools.permutations(pts[1:]):
    order = [0] + list(perm)
    cycles.append({order[i]: order[(i + 1) % d] for i in range(d)})
print(f"d={d}, number of d-cycles: {len(cycles)}")

# exposure patterns: list of (input, output) arcs
patterns = [
    [(0, 1)],                       # k=1
    [(0, 1), (1, 2)],               # k=2, one path 0->1->2
    [(0, 1), (3, 4)],               # k=2, two paths
    [(0, 1), (1, 2), (4, 5)],       # k=3
    [(0, 1), (2, 3), (4, 5)],       # k=3, three paths
]
for arcs in patterns:
    matching = [c for c in cycles if all(c[x] == y for (x, y) in arcs)]
    k = len(arcs)
    exposed_inputs = {x for x, _ in arcs}
    # pick a query point x: terminal of some component with unexposed image
    heads = {y for _, y in arcs}
    tails = {x for x, _ in arcs}
    # terminals: exposed heads not in tails, plus isolated points
    candidates = [p for p in pts if p not in tails]
    x = candidates[0]
    dist = Counter(c[x] for c in matching)
    vals = sorted(dist.values())
    uniform = len(set(vals)) == 1
    print(f"arcs={arcs} |cond|={len(matching)} query x={x} -> image dist "
          f"{dict(dist)}  #admissible={len(dist)} expected {d-k-1}: "
          f"{'OK' if uniform and len(dist) == d - k - 1 else 'CHECK'}")
