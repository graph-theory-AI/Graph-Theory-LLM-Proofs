"""Test Lemma 1 of the writeup on many small graphs:
  (a) zeta(mu(H)) >= zeta(H) + 1 for every graph H;
  (b) if H has a minimum cochromatic partition with an independent part,
      then zeta(mu(H)) = zeta(H) + 1 and mu(H) again has such a partition.
Exhaustive on all graphs with n <= 5 vertices, random on n = 6, 7.
"""
import itertools, random
from graphlib import (from_edges, mycielski, zeta, has_independent_part_optimal)

random.seed(12345)

def all_graphs(n):
    pairs = list(itertools.combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        yield from_edges(n, edges)

def random_graph(n, p):
    edges = [e for e in itertools.combinations(range(n), 2) if random.random() < p]
    return from_edges(n, edges)

def check(g, tag):
    zH = zeta(g)
    m = mycielski(g)
    zM = zeta(m, ub=zH + 2)
    assert zM >= zH + 1, f"LOWER BOUND FAILS on {tag}: zeta(H)={zH}, zeta(mu(H))={zM}"
    ind = has_independent_part_optimal(g)
    if ind:
        assert zM == zH + 1, f"EQUALITY FAILS on {tag}: zeta(H)={zH}, zeta(mu(H))={zM}"
        assert has_independent_part_optimal(m), f"PERSISTENCE FAILS on {tag}"
    return zH, zM, ind

count = 0
for n in range(1, 6):
    for g in all_graphs(n):
        check(g, f"n={n} graph#{count}")
        count += 1
print(f"exhaustive check passed on all graphs with 1..5 vertices ({count} graphs)")

for n, trials in ((6, 60), (7, 25), (8, 10)):
    for trial in range(trials):
        p = random.choice([0.2, 0.35, 0.5, 0.65, 0.8])
        g = random_graph(n, p)
        check(g, f"random n={n} trial={trial} p={p}")
    print(f"random check passed on n={n}")

print("LEMMA CHECK COMPLETE: no counterexample found")
