"""Checks on the combinatorial bookkeeping of the writeup:
 (1) the Kneser labelling a..j and the 14 'parent' edges of table (2.1) really are
     Petersen edges, and together with ij they are ALL 15 edges;
 (2) the closure order is valid (each new vertex's two parents come earlier);
 (3) the Petersen graph is a core: every endomorphism is an automorphism
     (brute force count of hom(P,P));
 (4) any two distinct Petersen vertices have at most one common neighbour.
"""
import itertools, networkx as nx
LAB = "abcdefghij"
KN = {'a':(1,2),'b':(1,3),'c':(1,4),'d':(4,5),'e':(3,5),
      'f':(2,5),'g':(2,3),'h':(2,4),'i':(3,4),'j':(1,5)}
E = {frozenset((u,v)) for u,v in itertools.combinations(LAB,2) if not (set(KN[u]) & set(KN[v]))}
P = nx.Graph([tuple(e) for e in E])
print("edges:", P.number_of_edges(), "degrees:", sorted(set(dict(P.degree()).values())),
      "girth-ish: triangles =", sum(nx.triangles(P).values())//3)
print("isomorphic to Petersen:", nx.is_isomorphic(P, nx.petersen_graph()))

parents = [('d','a','b'),('e','a','c'),('f','b','c'),('g','c','d'),
           ('h','b','e'),('i','a','f'),('j','g','h')]
used = set()
known = {'a','b','c'}
for new,p1,p2 in parents:
    assert frozenset((new,p1)) in E and frozenset((new,p2)) in E, (new,p1,p2)
    assert p1 in known and p2 in known, ("bad order", new)
    used |= {frozenset((new,p1)), frozenset((new,p2))}
    known.add(new)
print("parent edges used:", len(used), " leftover edges:", [tuple(sorted(e)) for e in E-used])
assert E - used == {frozenset(('i','j'))}
print("=> the 14 parent edges plus ij are exactly the 15 Petersen edges: OK")

mx = max(len(set(P[u]) & set(P[v])) for u,v in itertools.combinations(LAB,2))
print("max codegree in P over distinct pairs:", mx)

# core check: count all endomorphisms
cnt = 0
V = list(LAB)
def rec(i, asg):
    global cnt
    if i == len(V):
        cnt += 1; return
    u = V[i]
    for w in LAB:
        if all(P.has_edge(w, asg[x]) for x in V[:i] if P.has_edge(u, x)):
            asg[u] = w; rec(i+1, asg); del asg[u]
rec(0, {})
print("hom(P,P) =", cnt, "; |Aut(P)| =", 120, "=> Petersen is a core:", cnt == 120)
