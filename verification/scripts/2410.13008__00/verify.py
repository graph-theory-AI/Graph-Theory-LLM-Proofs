#!/usr/bin/env python3
"""
Referee verification for attack 2410.13008__00.

Writeup claims: the digraph D on Z_12 with arcs i->i+1, i->i+2 (all i mod 12)
plus exceptional arcs 4->0 and 10->6 is a counterexample to Seymour's
Conjecture 1.2 (arXiv:2410.13008): D is strongly 2-connected, admits a drawing
(with crossings) in the annulus with every directed cycle of winding number +1,
but admits no crossing-free drawing in the annulus with every directed cycle of
winding number +1.

Checks performed here:
  A. every simple directed cycle of D has total "advance" exactly 12
     (advance of arc u->v is (v-u) mod 12), hence the universal-cover drawing
     gives every directed cycle winding number exactly +1;
  B. D is strongly 2-connected (D and every D-z strongly connected);
  C. the underlying undirected graph U is simple, planar and 3-connected;
  D. {0,2,4} and {6,8,10} are faces of the (unique) sphere embedding, and the
     directed triangles 0->2->4->0 and 6->8->10->6 bound them with the SAME
     rotational orientation;
  E. EXHAUSTIVE obstruction check: for every choice of ordered pair of faces
     (f_p, f_q) of the sphere embedding (the two faces in which the annulus
     boundary disks are placed), compute the winding number of every simple
     directed cycle and test whether all windings can be +1 simultaneously
     (also testing the reflected embedding via global sign flip).  Since U is
     3-connected, its sphere embedding is unique up to reflection (Whitney),
     so this enumerates ALL crossing-free annular drawings of D.
     Also reports whether some choice makes all windings +-1 (the "unsigned"
     reading of the conjecture).
"""
import math
import itertools
import networkx as nx

N = 12

# ---------------------------------------------------------------- build D
D = nx.DiGraph()
D.add_nodes_from(range(N))
for i in range(N):
    D.add_edge(i, (i + 1) % N)
    D.add_edge(i, (i + 2) % N)
D.add_edge(4, 0)
D.add_edge(10, 6)
assert D.number_of_edges() == 26, D.number_of_edges()

def advance(u, v):
    return (v - u) % N

# check the advance table matches the writeup: base arcs 1 or 2, exceptional 8
assert advance(4, 0) == 8 and advance(10, 6) == 8

# ---------------------------------------------------------------- A. cycles
cycles = [c for c in nx.simple_cycles(D)]
adv_hist = {}
per_exceptional = {"none": 0, "(4,0)": 0, "(10,6)": 0, "both": 0}
bad = []
for c in cycles:
    arcs = list(zip(c, c[1:] + c[:1]))
    a = sum(advance(u, v) for u, v in arcs)
    adv_hist[a] = adv_hist.get(a, 0) + 1
    e1 = (4, 0) in arcs
    e2 = (10, 6) in arcs
    key = "both" if (e1 and e2) else "(4,0)" if e1 else "(10,6)" if e2 else "none"
    per_exceptional[key] += 1
    if a != N:
        bad.append((c, a))
print(f"[A] simple directed cycles: {len(cycles)}")
print(f"[A] advance histogram: {adv_hist}")
print(f"[A] cycles by exceptional arcs used: {per_exceptional}")
print(f"[A] cycles with advance != 12: {len(bad)}")
assert not bad, bad[:5]

# extra sub-claim check: no simple 0->4 path on base arcs with advance 16
B = nx.DiGraph((u, v) for u, v in D.edges if (u, v) not in [(4, 0), (10, 6)])
cnt16 = cnt4 = 0
for path in nx.all_simple_paths(B, 0, 4):
    a = sum(advance(u, v) for u, v in zip(path, path[1:]))
    if a == 16:
        cnt16 += 1
    elif a == 4:
        cnt4 += 1
    else:
        assert False, (path, a)
print(f"[A] base-arc simple 0->4 paths: advance 4: {cnt4}, advance 16: {cnt16}")
assert cnt16 == 0

# ---------------------------------------------------------------- B. strong 2-conn
assert nx.is_strongly_connected(D)
for z in range(N):
    Dz = D.copy()
    Dz.remove_node(z)
    assert nx.is_strongly_connected(Dz), f"D-{z} not strongly connected"
print("[B] D and every D-z are strongly connected  =>  strongly 2-connected")

# no digons (paper's digraphs may allow digons, but D has none):
digons = [(u, v) for u, v in D.edges if D.has_edge(v, u)]
print(f"[B] digons in D: {digons}")

# ---------------------------------------------------------------- C. U planar 3-conn
U = nx.Graph()
U.add_nodes_from(range(N))
mult = {}
for u, v in D.edges:
    key = frozenset((u, v))
    mult[key] = mult.get(key, 0) + 1
assert all(m == 1 for m in mult.values()), "parallel arcs would merge in U"
U.add_edges_from(D.edges)
assert U.number_of_edges() == 26
planar, emb = nx.check_planarity(U)
assert planar, "U not planar!"
conn = nx.node_connectivity(U)
print(f"[C] U planar: {planar}, node connectivity: {conn}")
assert conn >= 3

# ---------------------------------------------------------------- D. faces
def faces_of(embedding):
    seen = set()
    faces = []
    for u, v in embedding.edges:
        if (u, v) not in seen:
            walk = embedding.traverse_face(u, v, mark_half_edges=seen)
            faces.append(walk)
    return faces

faces = faces_of(emb)
E_count = U.number_of_edges()
assert len(faces) == 2 - N + E_count, (len(faces), 2 - N + E_count)  # Euler
print(f"[D] number of faces: {len(faces)} (Euler check ok)")

def find_face(faces, vset):
    return [w for w in faces if set(w) == set(vset) and len(w) == len(vset)]

f1 = find_face(faces, {0, 2, 4})
f2 = find_face(faces, {6, 8, 10})
print(f"[D] face with vertex set {{0,2,4}}: {f1}")
print(f"[D] face with vertex set {{6,8,10}}: {f2}")
assert len(f1) == 1 and len(f2) == 1

def cyclic_sense(walk, directed_triple):
    """+1 if directed_triple read cyclically equals walk's cyclic order, -1 if reversed."""
    a, b, c = directed_triple
    w = list(walk)
    i = w.index(a)
    w = w[i:] + w[:i]
    if w == [a, b, c]:
        return +1
    if w == [a, c, b]:
        return -1
    raise ValueError

s1 = cyclic_sense(f1[0], (0, 2, 4))
s2 = cyclic_sense(f2[0], (6, 8, 10))
print(f"[D] facial-walk sense of 0->2->4->0: {s1:+d}; of 6->8->10->6: {s2:+d}; "
      f"same orientation: {s1 == s2}")

# ---------------------------------------------------------------- E. exhaustive check
# straight-line drawing from the combinatorial embedding
pos = nx.combinatorial_embedding_to_pos(emb)

def winding_around(point, poly):
    """signed winding number of closed polygon poly (list of xy) around point"""
    px, py = point
    tot = 0.0
    k = len(poly)
    for i in range(k):
        x1, y1 = poly[i][0] - px, poly[i][1] - py
        x2, y2 = poly[(i + 1) % k][0] - px, poly[(i + 1) % k][1] - py
        tot += math.atan2(x1 * y2 - x2 * y1, x1 * x2 + y1 * y2)
    return round(tot / (2 * math.pi))

# an interior sample point for every face
import random
random.seed(1)
xs = [p[0] for p in pos.values()]
ys = [p[1] for p in pos.values()]
face_polys = [[pos[v] for v in w] for w in faces]
face_area2 = []
for poly in face_polys:
    a = sum(poly[i][0] * poly[(i + 1) % len(poly)][1]
            - poly[(i + 1) % len(poly)][0] * poly[i][1] for i in range(len(poly)))
    face_area2.append(a)
outer_idx = [i for i, w in enumerate(faces)
             if abs(face_area2[i]) == max(abs(a) for a in face_area2)]
# identify each face's interior point: random sampling, membership by winding
face_point = {}
attempts = 0
while len(face_point) < len(faces) and attempts < 400000:
    attempts += 1
    z = (random.uniform(min(xs), max(xs)), random.uniform(min(ys), max(ys)))
    hits = [i for i, poly in enumerate(face_polys)
            if winding_around(z, poly) != 0]
    inner_hits = [i for i in hits if i not in outer_idx]
    if len(inner_hits) == 1 and inner_hits[0] not in face_point:
        face_point[inner_hits[0]] = z
# outer face: a far-away point
for i in outer_idx:
    face_point[i] = (min(xs) - 1000.0, min(ys) - 1000.0)
assert len(face_point) == len(faces), (len(face_point), len(faces))

# sanity: each sample point lies in exactly its face
cycle_polys = [([pos[v] for v in c], c) for c in cycles]

results_signed = []      # face pairs giving ALL windings == +1 (or all == -1)
results_unsigned = []    # face pairs giving all windings in {+1,-1}
for ip, iq in itertools.permutations(range(len(faces)), 2):
    p = face_point[ip]
    q = face_point[iq]
    ws = []
    ok_signed_pos = ok_signed_neg = ok_unsigned = True
    for poly, c in cycle_polys:
        w = winding_around(p, poly) - winding_around(q, poly)
        ws.append(w)
        if w != 1:
            ok_signed_pos = False
        if w != -1:
            ok_signed_neg = False
        if w not in (1, -1):
            ok_unsigned = False
        if not (ok_signed_pos or ok_signed_neg or ok_unsigned):
            break
    if ok_signed_pos or ok_signed_neg:
        results_signed.append((faces[ip], faces[iq]))
    if ok_unsigned:
        results_unsigned.append((faces[ip], faces[iq]))

print(f"[E] ordered face pairs tested: {len(faces)*(len(faces)-1)}")
print(f"[E] pairs with ALL directed-cycle windings identically +1 (or -1): "
      f"{len(results_signed)}")
print(f"[E] pairs with all windings in {{+1,-1}} (unsigned reading): "
      f"{len(results_unsigned)}")
for fp, fq in results_unsigned:
    print(f"    unsigned-OK pair: p in face {fp}, q in face {fq}")

# focused report for the pair (T1, T2)
i1 = faces.index(f1[0]); i2 = faces.index(f2[0])
p = face_point[i1]; q = face_point[i2]
wT1 = winding_around(p, [pos[v] for v in [0, 2, 4]]) - winding_around(q, [pos[v] for v in [0, 2, 4]])
# careful: use the directed order 0->2->4
wT1 = winding_around(p, [pos[0], pos[2], pos[4]]) - winding_around(q, [pos[0], pos[2], pos[4]])
wT2 = winding_around(p, [pos[6], pos[8], pos[10]]) - winding_around(q, [pos[6], pos[8], pos[10]])
print(f"[E] with p in face {{0,2,4}} and q in face {{6,8,10}}: "
      f"winding(0->2->4->0) = {wT1:+d}, winding(6->8->10->6) = {wT2:+d}")

print()
if not results_signed:
    print("CONCLUSION: no crossing-free annular drawing of D gives every "
          "directed cycle the same winding number +1  --  the writeup's "
          "obstruction is CONFIRMED (signed reading).")
else:
    print("CONCLUSION: counterexample FAILS -- a valid face pair exists.")
