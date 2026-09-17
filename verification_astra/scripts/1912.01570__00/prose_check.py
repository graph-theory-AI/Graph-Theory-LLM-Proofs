"""Guard against a transcription error: rebuild G_1 from the writeup's PROSE description
   "take a square abcda and two disjoint K_4's.  Connect one K_4 to a,c, and the other to
    b,d, using distinct attachment vertices in each K_4"
independently of the formal edge list, and check the two graphs are isomorphic.
Then recompute fvs and fp on the prose version from scratch.
"""
import itertools
import networkx as nx

from build import build, fvs_bruteforce
from embeddings import fp_exact

H = nx.Graph()
H.add_edges_from([("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")])       # the square
for tag in ("X", "Y"):                                                   # two disjoint K_4's
    for u, v in itertools.combinations([tag + str(i) for i in range(4)], 2):
        H.add_edge(u, v)
H.add_edge("a", "X0"); H.add_edge("c", "X1")   # one K_4 attached to a and c
H.add_edge("b", "Y0"); H.add_edge("d", "Y1")   # the other attached to b and d

G = build(1)
print("prose graph: n =", H.number_of_nodes(), " m =", H.number_of_edges())
print("isomorphic to build(1):", nx.is_isomorphic(G, H))
print("planar:", nx.check_planarity(H)[0])
k, S = fvs_bruteforce(H)
print(f"fvs = {k}  witness {sorted(S)}")
best, wit, facial = fp_exact(H)
print(f"fp  = {best}   witness {[sorted(c) for c in wit[0]]}")
print(f"\nConjecture 14 requires fvs <= 2*fp, i.e. {k} <= {2*best}:", k <= 2 * best)
