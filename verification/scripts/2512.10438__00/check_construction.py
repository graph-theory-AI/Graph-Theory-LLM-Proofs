#!/usr/bin/env python3
"""Verify the writeup's non-transitive 6-colored 9-vertex tournament T:
   - it is a tournament (every pair gets exactly one directed edge),
   - it is non-transitive,
   - all 6 colors occur,
   - the longest color-avoiding directed path (edges using <= 5 of the 6 colors)
     has exactly 7 vertices (claim: p(T) = 7).

Encoding follows attacks/2512.10438__00/output.md section 2 exactly.
Vertices: l1 l2 l3 (L), x0 x1 x2 (C), r1 r2 r3 (R).
Orientation: L transitive l1->l2->l3; R transitive r1->r2->r3;
C directed triangle x0->x1->x2->x0; all edges L->C, C->R, L->R.
Colors: d0,d1,d2 = 2,5,6 with indices mod 3.
  l1l2:1; l2l3,l1l3:3; r1r2,r1r3:4; r2r3:1;
  x_i x_{i+1}: d_i; l3 x_i: d_{i-1}; x_i r1: d_i; l2 x_i: 3; x_i r2: 4;
  every remaining edge: 1.
"""
import itertools, sys

L = ["l1", "l2", "l3"]
C = ["x0", "x1", "x2"]
R = ["r1", "r2", "r3"]
V = L + C + R
d = {0: 2, 1: 5, 2: 6}

color = {}  # (u,v) -> color, edge directed u->v

# within L (transitive)
color[("l1", "l2")] = 1
color[("l2", "l3")] = 3
color[("l1", "l3")] = 3
# within R (transitive)
color[("r1", "r2")] = 4
color[("r1", "r3")] = 4
color[("r2", "r3")] = 1
# triangle C: x_i -> x_{i+1}, color d_i
for i in range(3):
    color[(f"x{i}", f"x{(i+1)%3}")] = d[i]
# l3 -> x_i : d_{i-1}
for i in range(3):
    color[("l3", f"x{i}")] = d[(i - 1) % 3]
# x_i -> r1 : d_i
for i in range(3):
    color[(f"x{i}", "r1")] = d[i]
# l2 -> x_i : 3
for i in range(3):
    color[("l2", f"x{i}")] = 3
# x_i -> r2 : 4
for i in range(3):
    color[(f"x{i}", "r2")] = 4
# remaining edges (L->C, C->R, L->R not listed above): color 1
for u in L:
    for v in C:
        color.setdefault((u, v), 1)
for u in C:
    for v in R:
        color.setdefault((u, v), 1)
for u in L:
    for v in R:
        color.setdefault((u, v), 1)

# --- tournament sanity check ---
assert len(color) == 36, len(color)
for a, b in itertools.combinations(V, 2):
    fwd, bwd = (a, b) in color, (b, a) in color
    assert fwd != bwd, (a, b)
print("tournament OK: 36 edges, one direction per pair")

colors_used = sorted(set(color.values()))
print("colors used:", colors_used)
assert colors_used == [1, 2, 3, 4, 5, 6]

# non-transitive: directed triangle exists?
has_cycle = any(
    (a, b) in color and (b, c) in color and (c, a) in color
    for a, b, c in itertools.permutations(V, 3)
)
print("contains directed triangle (non-transitive):", has_cycle)
assert has_cycle

# --- longest color-avoiding path, exhaustive DFS over all directed paths ---
adj = {v: [] for v in V}
for (u, v) in color:
    adj[u].append(v)

best = 0
best_path = None
ALL = frozenset([1, 2, 3, 4, 5, 6])

def dfs(path, used_colors):
    global best, best_path
    if used_colors != ALL and len(path) > best:  # avoids at least one color
        best = len(path)
        best_path = (list(path), set(used_colors))
    last = path[-1]
    for w in adj[last]:
        if w not in path:
            path.append(w)
            dfs(path, used_colors | {color[(path[-2], w)]})
            path.pop()

for v in V:
    dfs([v], frozenset())

print("longest color-avoiding path (vertices):", best)
print("witness path:", best_path[0], "colors used:", sorted(best_path[1]))
assert best == 7, best

# also verify the writeup's explicit witness path and its colors
wit = ["l1", "l2", "l3", "x0", "x1", "x2", "r1"]
wcols = [color[(wit[i], wit[i + 1])] for i in range(len(wit) - 1)]
print("writeup witness path colors:", wcols)
assert wcols == [1, 3, 6, 2, 5, 6], wcols

# count: verify every 8-vertex directed path uses all 6 colors (direct check)
n_eight = 0
def dfs8(path, used_colors):
    global n_eight
    if len(path) == 8:
        n_eight += 1
        assert used_colors == ALL, (path, used_colors)
        return
    for w in adj[path[-1]]:
        if w not in path:
            path.append(w)
            dfs8(path, used_colors | {color[(path[-2], w)]})
            path.pop()

for v in V:
    dfs8([v], frozenset())
print("number of 8-vertex directed paths:", n_eight, "- all use all 6 colors")

print("CONSTRUCTION CHECK PASSED: p(T) = 7, tournament non-transitive, 6 colors")
