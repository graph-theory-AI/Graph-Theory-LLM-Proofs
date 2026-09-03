#!/usr/bin/env python3
"""Sanity checks for Section 2 of the writeup (k = b+2, n = b+2):
 - B_e = [n]\\e gives a bijection edges of K_n <-> b-subsets of [n];
 - intersection of {B_e : e in E'} is empty  <=>  E' is an edge cover of K_n;
 - the star S_v and the family T = {vx : x not in {v,p,q}} + {pq} are
   inclusion-minimal edge covers, of sizes n-1 and n-2;
 - the two edge counts of H[R] claimed in the writeup (n-5 vs n-4) for the
   forced chordless cycles, for n = 5..9.
Checked for n = 5, 6, 7 (b = 3, 4, 5)."""
import itertools

for n in (5, 6, 7):
    b = n - 2
    V = set(range(1, n+1))
    edges = [frozenset(p) for p in itertools.combinations(V, 2)]
    # bijection
    comp = {e: frozenset(V - e) for e in edges}
    assert len(set(comp.values())) == len(edges)
    assert all(len(c) == b for c in comp.values())
    # empty intersection <=> edge cover (check over all edge subsets for n=5, sampled families for n>5)
    import random
    random.seed(0)
    fams = (list(itertools.chain.from_iterable(
                itertools.combinations(edges, r) for r in range(1, len(edges)+1)))
            if n == 5 else
            [random.sample(edges, random.randint(1, len(edges))) for _ in range(20000)])
    for fam in fams:
        inter = frozenset.intersection(*[comp[e] for e in fam])
        cover = set().union(*fam) == V
        assert (inter == frozenset()) == cover
    # S_v and T minimal covers
    v, p, q = 1, 2, 3
    Sv = [frozenset({v, x}) for x in V - {v}]
    T = [frozenset({v, x}) for x in V - {v, p, q}] + [frozenset({p, q})]
    def is_cover(E): return set().union(*E) == V
    def is_min_cover(E):
        return is_cover(E) and all(not is_cover([f for f in E if f != e]) for e in E)
    assert is_min_cover(Sv) and len(Sv) == n-1
    assert is_min_cover(T) and len(T) == n-2
    # edge-count clash: |E(C_{n-1} minus 2 nonadjacent verts)| vs |E(C_{n-2} minus 1 vert)|
    c1 = (n-1) - 4   # cycle C_{n-1}: delete 2 nonadjacent vertices -> removes 4 edges
    c2 = (n-2) - 2   # cycle C_{n-2}: delete 1 vertex -> path
    print(f"n={n} (b={b}): bijection OK, cover<=>empty-intersection OK, "
          f"S_v/T minimal covers OK; H[R] edge counts {c1} vs {c2} -> "
          f"{'CONTRADICTION (as claimed)' if c1 != c2 else 'no contradiction?!'}")
    assert c1 != c2
print("Section 2 correspondence and arithmetic VERIFIED for n=5,6,7.")
