#!/usr/bin/env python3
"""Independent verification that no digraph K(5,3) with the Problem 5.40 property exists.

Convention (matching the source paper arXiv:1812.02420): digraphs are loopless,
antiparallel arcs (digons) are allowed, and a digon IS a directed cycle.

Required property of a solution D on vertex set C([5],3):
    for every family F of 3-subsets, D[F] is acyclic  <=>  intersection(F) != empty.

Proof strategy verified here (independent of the writeup's lemma):
  Let V_x = [5]\\{1,x} for x in {2,3,4,5}  (the four 3-sets avoiding 1),
      S1  = {V_2,V_3,V_4,V_5},
      U_xy = {1,x,y} for pairs {x,y} in {2,3,4,5}.

  Facts checked by code below:
  (F0) every pair of distinct 3-subsets of [5] intersects  => every 2-subfamily
       must be ACYCLIC => no digon anywhere in a solution.
  (F1) every triple of S1 has nonempty intersection (=> acyclic constraint),
       while S1 itself has empty intersection (=> cyclic constraint).
  (F2) the family {V_x, V_y, U_xy} has empty intersection (=> cyclic constraint),
       and its three pairwise intersections are nonempty (=> no digons inside).

  Stage A: enumerate ALL 2^12 digraphs on 4 labelled vertices; keep those with
       no digon, all triples acyclic, whole 4-set cyclic.  Verify every survivor
       has at least one pair with NO arc between them (in fact survivors are
       exactly the 6 directed Hamilton 4-cycles, each with 2 arcless pairs).

  Stage B: for 3 vertices {V_x, V_y, U} with both V_x<->V_y arcs ABSENT (from the
       survivor) and digons with U forbidden (by F2 pairwise intersections),
       enumerate all 2^4 configurations of the remaining arcs and verify NONE
       contains a directed cycle.  Hence {V_x,V_y,U_xy} would be acyclic despite
       empty intersection: contradiction.  Therefore no solution exists.

  Sanity: also enumerate all inclusion-minimal empty-intersection families of
       3-subsets of [5] and report their count/sizes (writeup implies 30 of size
       3 and 5 of size 4, matching minimal edge covers of K5).
"""
import itertools

def has_dicycle(n, arcs):
    """arcs: set of (i,j). True iff digraph on vertices 0..n-1 has a directed cycle
    (a digon (i,j),(j,i) counts)."""
    adj = {i: [] for i in range(n)}
    for (i, j) in arcs:
        adj[i].append(j)
    color = [0]*n  # 0 white 1 grey 2 black
    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and dfs(v):
                return True
        color[u] = 2
        return False
    return any(color[i] == 0 and dfs(i) for i in range(n))

# ---------- set-level facts ----------
ground = frozenset(range(1, 6))
threesets = [frozenset(c) for c in itertools.combinations(range(1, 6), 3)]
assert len(threesets) == 10

# F0: all pairs of distinct 3-subsets of [5] intersect
f0 = all(A & B for A, B in itertools.combinations(threesets, 2))
print("F0 (all pairs of 3-subsets of [5] intersect => no digon allowed):", f0)
assert f0

V = {x: ground - {1, x} for x in (2, 3, 4, 5)}
S1 = [V[2], V[3], V[4], V[5]]
U = {frozenset(p): frozenset({1, *p}) for p in itertools.combinations((2, 3, 4, 5), 2)}

# F1
f1a = all(frozenset.intersection(*t) for t in itertools.combinations(S1, 3))
f1b = (frozenset.intersection(*S1) == frozenset())
print("F1 (every triple of S1 intersects, S1 itself doesn't):", f1a, f1b)
assert f1a and f1b

# F2
f2 = True
for p, Up in U.items():
    x, y = sorted(p)
    fam = [V[x], V[y], Up]
    f2 &= (frozenset.intersection(*fam) == frozenset())
    f2 &= all(A & B for A, B in itertools.combinations(fam, 2))
print("F2 ({V_x,V_y,U_xy}: empty triple intersection, nonempty pairwise):", f2)
assert f2

# ---------- Stage A ----------
pairs4 = list(itertools.permutations(range(4), 2))  # 12 possible arcs
survivors = []
for mask in range(1 << 12):
    arcs = {pairs4[i] for i in range(12) if mask >> i & 1}
    # no digon on any pair (F0: every 2-subfamily must be acyclic)
    if any((i, j) in arcs and (j, i) in arcs for i in range(4) for j in range(i+1, 4)):
        continue
    # every triple acyclic (F1)
    if any(has_dicycle(4, {(i, j) for (i, j) in arcs if i in t and j in t})
           for t in itertools.combinations(range(4), 3)):
        continue
    # whole 4-set cyclic (F1)
    if not has_dicycle(4, arcs):
        continue
    survivors.append(arcs)

print(f"Stage A: {len(survivors)} digraphs on S1 satisfy the subfamily constraints")
ham4 = set()
for perm in itertools.permutations(range(1, 4)):
    seq = (0,) + perm
    ham4.add(frozenset((seq[i], seq[(i+1) % 4]) for i in range(4)))
all_are_C4 = all(frozenset(s) in ham4 for s in survivors)
print("Stage A: every survivor is exactly a directed Hamilton 4-cycle:", all_are_C4)
every_has_arcless_pair = all(
    any((i, j) not in s and (j, i) not in s
        for i in range(4) for j in range(i+1, 4))
    for s in survivors)
print("Stage A: every survivor has an arcless (nonadjacent) pair:", every_has_arcless_pair)
assert survivors and every_has_arcless_pair

# ---------- Stage B ----------
# vertices 0=V_x, 1=V_y, 2=U ; arcs between 0 and 1 fixed ABSENT;
# digons {0,2} and {1,2} forbidden; enumerate the 4 candidate arcs 0<->2, 1<->2.
cand = [(0, 2), (2, 0), (1, 2), (2, 1)]
bad = 0
for mask in range(1 << 4):
    arcs = {cand[i] for i in range(4) if mask >> i & 1}
    if ((0, 2) in arcs and (2, 0) in arcs) or ((1, 2) in arcs and (2, 1) in arcs):
        continue  # digon forbidden: those pairs intersect (F2)
    if has_dicycle(3, arcs):
        bad += 1
print("Stage B: configurations making {V_x,V_y,U_xy} cyclic (must be 0):", bad)
assert bad == 0

print()
print("CONCLUSION: a solution D would induce on S1 one of the Stage-A survivors,")
print("hence have an arcless pair {V_x,V_y}; but then (Stage B) the empty-")
print("intersection family {V_x,V_y,U_xy} induces an ACYCLIC digraph.")
print("=> NO digraph K(5,3) with the Problem 5.40 property exists.  VERIFIED")

# ---------- sanity: minimal empty-intersection families of C([5],3) ----------
from collections import Counter
minimal = []
for r in range(2, 11):
    for fam in itertools.combinations(threesets, r):
        if frozenset.intersection(*fam):
            continue
        if all(frozenset.intersection(*sub)
               for sub in itertools.combinations(fam, r-1)):
            minimal.append(fam)
print("\nSanity: inclusion-minimal empty-intersection families, sizes:",
      dict(Counter(len(f) for f in minimal)))
