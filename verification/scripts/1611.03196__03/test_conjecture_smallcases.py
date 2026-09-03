"""Small-case sanity check of Conjecture 1.15 (arXiv:1611.03196) as proved in
attacks/1611.03196__03/output.md.

For random small bipartite graphs G and random edge-set families E_1..E_m,
compute by branch-and-bound the maximum size of a matching S obeying
|S cap E_i| <= ceil(|E_i|/Delta(G)) for all i, and record the deficit
|E(G)|/Delta(G) - max|S|.  The writeup claims deficit <= 32(m+1)^3; the
authors of the source paper suggest m/2 may suffice.  We report the maximum
deficit observed.
"""
import math
import random
from fractions import Fraction

random.seed(2026)


def max_matching_capped(edges, Esets, caps):
    n = len(edges)
    membership = [tuple(i for i, E in enumerate(Esets) if e in E)
                  for e in edges]
    best = 0

    def rec(idx, used, counts, size):
        nonlocal best
        if size + (n - idx) <= best:
            return
        if idx == n:
            best = max(best, size)
            return
        u, v = edges[idx]
        if u not in used and v not in used:
            ok = True
            for t in membership[idx]:
                if counts[t] + 1 > caps[t]:
                    ok = False
                    break
            if ok:
                for t in membership[idx]:
                    counts[t] += 1
                used.add(u)
                used.add(v)
                rec(idx + 1, used, counts, size + 1)
                used.discard(u)
                used.discard(v)
                for t in membership[idx]:
                    counts[t] -= 1
        rec(idx + 1, used, counts, size)
        best = max(best, size)

    rec(0, set(), [0] * len(Esets), 0)
    return best


def degree_max(edges):
    deg = {}
    for (u, v) in edges:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    return max(deg.values())


def random_instance():
    p = random.randint(2, 6)
    q = random.randint(2, 6)
    prob = random.choice([0.3, 0.5, 0.7, 1.0])
    edges = [((("L", u)), (("R", v))) for u in range(p) for v in range(q)
             if random.random() < prob]
    if len(edges) > 22:
        random.shuffle(edges)
        edges = edges[:22]
    if not edges:
        return None
    m = random.randint(1, 3)
    style = random.choice(["subsets", "partition", "overlap"])
    if style == "partition":
        Esets = [set() for _ in range(m)]
        for e in edges:
            Esets[random.randrange(m)].add(e)
    else:
        pr = 0.5 if style == "subsets" else 0.8
        Esets = [{e for e in edges if random.random() < pr} for _ in range(m)]
    return edges, Esets, m


def main():
    worst = Fraction(-10)
    worst_info = None
    tested = 0
    for _ in range(600):
        inst = random_instance()
        if inst is None:
            continue
        edges, Esets, m = inst
        D = degree_max(edges)
        caps = [math.ceil(len(E) / D) for E in Esets]
        best = max_matching_capped(edges, Esets, caps)
        deficit = Fraction(len(edges), D) - best
        tested += 1
        if deficit > worst:
            worst = deficit
            worst_info = (len(edges), D, m, [len(E) for E in Esets],
                          caps, best)
    print(f"tested {tested} random instances (|E|<=22, m<=3)")
    print(f"max deficit |E|/Delta - max|S| observed: {worst} "
          f"= {float(worst):.3f}")
    print(f"worst instance: |E|={worst_info[0]}, Delta={worst_info[1]}, "
          f"m={worst_info[2]}, |E_i|={worst_info[3]}, caps={worst_info[4]}, "
          f"best={worst_info[5]}")
    print("bound claimed by writeup for m=3: 32*(3+1)^3 =", 32 * 4 ** 3)
    print("bound suggested by authors for m=3: m/2 = 1.5")


if __name__ == "__main__":
    main()
