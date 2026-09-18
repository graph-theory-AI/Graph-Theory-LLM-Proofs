"""Lemma 3 of the writeup: every endomorphism of the Petersen graph is an
automorphism (i.e. the Petersen graph is a core).  Exhaustive check."""
import itertools
from collections import defaultdict
import sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from construction2 import PV, PE

adj = defaultdict(set)
for u, v in PE:
    adj[u].add(v); adj[v].add(u)
assert all(len(adj[v]) == 3 for v in PV)
# girth 5 check
import networkx as nx
G = nx.Graph(list(PE))
print("Petersen: n=%d m=%d girth=%d" % (G.number_of_nodes(), G.number_of_edges(),
                                        min(len(c) for c in nx.cycle_basis(G))))
order = PV
homs = 0
autos = 0
f = {}
def rec(i):
    global homs, autos
    if i == len(order):
        homs += 1
        if len(set(f.values())) == 10:
            autos += 1
        return
    v = order[i]
    for w in PV:
        ok = True
        for u in order[:i]:
            if (u in adj[v]) and (f[u] not in adj[w]):
                ok = False; break
        if ok:
            f[v] = w
            rec(i+1)
    f.pop(v, None)
rec(0)
print("total endomorphisms hom(P,P) =", homs, "; of these bijective =", autos)
print("=> every endomorphism is an automorphism:", homs == autos, "; |Aut| =", autos)
