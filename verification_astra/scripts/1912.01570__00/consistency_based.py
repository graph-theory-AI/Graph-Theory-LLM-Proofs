"""Cross-check against Barnkopf-Gyori (arXiv:2401.07376), Remark 2.5:
   every BASED planar graph (one having a face adjacent to every other face)
   satisfies fvs(G) <= 2*fp(G).
If G_1 were based planar in some embedding, that remark would contradict our
fvs(G_1)=5 > 4 = 2*fp(G_1).  So G_1 had better NOT be based planar.  We check every
planar embedding of G_1.
"""
import itertools
from build import build
from embeddings import rotation_choices, faces_of

G = build(1)
V = list(G.nodes())
E = G.number_of_edges()
per = [rotation_choices(sorted(G.neighbors(v))) for v in V]

n_planar = 0
based = 0
for combo in itertools.product(*per):
    rot = dict(zip(V, combo))
    F = faces_of(rot, E)
    if len(V) - E + len(F) != 2:
        continue
    n_planar += 1
    # faces as edge sets (undirected)
    fe = [frozenset(frozenset(d) for d in walk) for walk in F]
    for i, f in enumerate(fe):
        if all(i == k or (f & g) for k, g in enumerate(fe)):
            based += 1
            break

print(f"planar embeddings of G_1 examined: {n_planar}")
print(f"embeddings in which G_1 is 'based' (some face adjacent to all others): {based}")
print("=> G_1 is based planar:", based > 0)
print("   (must be False, otherwise it would contradict Remark 2.5 of arXiv:2401.07376)")
