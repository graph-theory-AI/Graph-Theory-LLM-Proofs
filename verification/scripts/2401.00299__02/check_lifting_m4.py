"""Supplementary check: lifting construction for m=4 -> Q_6.

Takes the best singleton set L for Q_4 (L = empty set, a_L = 30), builds all
30^4 = 810000 lifted candidate partitions of Q_6, and verifies each is a valid
partition of Q_6 into coordinate 2-faces, and that the map is injective.
(The exhaustive f_2(6) census is not attempted.)
"""
from itertools import combinations, product
from collections import defaultdict

def squares(d):
    out = []
    for i, j in combinations(range(d), 2):
        bi, bj = 1 << i, 1 << j
        for base in range(1 << d):
            if base & bi or base & bj:
                continue
            out.append(frozenset({base, base | bi, base | bj, base | bi | bj}))
    return out

def partitions_02(m):
    sqs = squares(m)
    nverts = 1 << m
    results = []
    def rec(start, used, chosen):
        results.append((frozenset(chosen),
                        frozenset(v for v in range(nverts) if v not in used)))
        for k in range(start, len(sqs)):
            s = sqs[k]
            if used & s:
                continue
            rec(k + 1, used | s, chosen + [s])
    rec(0, frozenset(), [])
    return results

m = 4
parts = partitions_02(m)
byL = defaultdict(list)
for sq, L in parts:
    byL[L].append(sq)
aL, Lstar = max((len(v), k) for k, v in byL.items())
pool = byL[Lstar]
print(f"m={m}: f_02={len(parts)}, best L has |L|={len(Lstar)}, a_L={aL}")
assert Lstar == frozenset() and aL == 30

SQ6 = set(squares(m + 2))
nv6 = 1 << (m + 2)
images = set()
count = 0
for t in product(range(aL), repeat=4):
    parts6 = []
    for zi in range(4):
        for C in pool[t[zi]]:
            parts6.append(frozenset(x + (zi << m) for x in C))
    for x in Lstar:
        parts6.append(frozenset(x + (z << m) for z in range(4)))
    P = frozenset(parts6)
    # validity
    allv = set()
    for part in P:
        assert part in SQ6, "part is not a coordinate 2-face of Q_6"
        assert not (allv & part), "overlapping parts"
        allv |= part
    assert len(allv) == nv6, "does not cover Q_6"
    images.add(P)
    count += 1
print(f"built {count} tuples -> {len(images)} distinct valid square partitions of Q_6")
assert len(images) == aL ** 4, "INJECTIVITY FAILS"
print(f"injectivity holds: f_2(6) >= {aL**4}")
