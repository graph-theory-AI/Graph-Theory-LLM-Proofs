"""Check 3b: dense case of Lemma 2, where Pr(D[S] acyclic) < 1.
S = all 9 edges of K_{3,3} (and K_{3,3} minus one edge): exact enumeration of all
prod d_z! local-order systems vs A(L(G_S)).
"""
import itertools, math
from check3_lemma2 import exact_probability, line_graph, count_acyclic_orientations

for name, S in [
    ("K33", [(('x', i), ('y', j)) for i in range(3) for j in range(3)]),
    ("K33-e", [(('x', i), ('y', j)) for i in range(3) for j in range(3)][:-1]),
]:
    verts = sorted(set(v for e in S for v in e))
    deg = {z: sum(1 for e in S if z in e) for z in verts}
    fav, total = exact_probability(S)
    A = count_acyclic_orientations(len(S), line_graph(S))
    s = len(S); n = 3
    bound1 = 1
    for u, v in S: bound1 *= deg[u] + deg[v] - 1
    p = fav / total
    print(f"{name}: s={s}, prod d_z! = {total}, favorable = {fav}, A(L(G_S)) = {A}, "
          f"Pr = {p:.6f}, Lemma1 bound/total = {bound1/total:.4f}, (2e^2 n/s)^s = {(2*math.e**2*n/s)**s:.3g}")
    assert fav == A, "favorable != acyclic orientations of L(G_S)"
    assert p <= bound1 / total + 1e-12
print("CHECK3B PASSED")
