Attack the following open graph-theory problem.

Catalog id: 5_local_tensions
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/5_local_tensions/
Original entry: http://www.openproblemgarden.org/op/5_local_tensions
Problem attributed to: DeVos, Matt (posted 2007-06-22)

=== Problem statement (OpenProblemGarden) ===
Title: 5-local-tensions
Conjecture There exists a fixed constant $ c $ (probably $ c=4 $ suffices) so that every embedded (loopless) graph with edge-width $ \ge c $ has a 5-local-tension.

=== Discussion / context (OpenProblemGarden) ===
The edge-width of an embedded graph is the length of the shortest non-contractible cycle. Definition Let $ G $ be a directed graph, let $ \Gamma $ be an abelian group, and let $ \phi : E(G) \rightarrow \Gamma $ . Define the height of a walk $ W $ to be the sum of $ \phi $ on the forward edges of $ W $ minus the sum of $ \phi $ on the backward edges of $ W $ (edges are counted according to multiplicity). We call $ \phi $ a tension if the height of every closed walk is zero, and if $ G $ is an embedded graph, we call $ \phi $ a local-tension if the height of every closed walk which forms a contractible curve is zero. If in addition, $ \Gamma = {\mathbb Z} $ and $ 0 < \phi(e) < k $ for some $ k \in {\mathbb Z} $ , we say that $ \phi $ is a $ k $ - tension or a $ k $ - local-tension . If we reverse an edge $ e $ and replace $ \phi(e) $ by $ -\phi(e) $ , this preserves the properties of tension or local-tension. Accordingly, we say that an undirected graph (embedded graph) $ G $ has a $ k $ -tension ( $ k $ -local-tension) if some and thus every orientation of it admits such a map. Proposition A graph has a $ k $ -tension if and only if it is $ k $ -colorable. Proof To see the "if" direction, let $ f : V(G) \rightarrow \{0,\ldots,k-1\} $ be a coloring, orient the edges of $ G $ arbitrarily, and defining $ \phi : E(G) \rightarrow {\mathbb Z} $ by the rule $ \phi(uv) = f(v) - f(u) $ . It is straightforward to check that $ \phi $ is a $ k $ -tension. For the "only if" direction, let $ \phi : E(G) \rightarrow {\mathbb Z} $ be a $ k $ -tension. Now choose a point $ u \in V(G) $ and define the map $ f : V(G) \rightarrow {\mathbb Z}_k $ by the rule that $ f(v) $ is the height of some (and thus every) walk from $ u $ to $ v $ modulo $ k $ . Again, it is straightforward to check that this defines a proper $ k $ -coloring. For graphs on orientable surfaces, local-tensions are dual to flows. More precisely, if $ G $ and $ G^* $ are dual graphs embedded in an orientable surface, then $ G $ has a $ k $ -local-tension if and only if $ G^* $ has a nowhere-zero $ k $ -flow. On non-orientable surfaces, there is a duality between $ k $ -local-tensions in $ G $ and nowhere-zero $ k $ -flows in a bidirected $ G^* $ . Based on this duality we have a couple of conjectures. The first follows from Tutte's 5-flow conjecture , the second from Bouchet's 6-flow conjecture . Conjecture (Tutte) Every loopless graph embedded in an orientable surface has a 5-local-tension. Conjecture (Bouchet) Every loopless graph embedded in any surface has a 6-local-tension. So although, graphs on surfaces may have high chromatic number, thanks to some partial results toward the above conjectures, we know that they always have small local-tensions. For orientable surfaces, there is a famous Conjecture of Grunbaum which is equivalent to the following. Conjecture (Grunbaum) If $ G $ is a simple loopless graph embedded in an orientable surface with edge-width $ \ge 3 $ , then $ G $ has a 4-local-tension. On non-orientable surfaces, it is known that there are graphs of arbitrarily high edge-width which do not admit 4-local-tensions (see [DGMVZ]). However, it remains open whether sufficiently high edge-width forces the existence of a 5-local-tension. Indeed, as suggested by the conjecture at the start of this page, it may be that edge-width at least 4 is enough. Edge-width 3 does not suffice since the embedding of $ K_6 $ in the projective plane does not admit a 5-local-tension.

=== References listed by OpenProblemGarden ===
- *[DGMVZ] M. DeVos, L. Goddyn, B. Mohar, D. Vertigan, and X. Zhu, Coloring-flow duality of embedded graphs. Trans. Amer. Math. Soc. 357 (2005), no. 10 MathSciNet

=== Catalog page (statement + literature review) ===
5-local-tensions — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture that every loopless graph embedded in a non-orientable surface with edge-width at least some fixed constant $c$ (probably $c=4$) admits a $5$-local-tension remains open. No post-2007 paper resolving or substantially advancing this specific conjecture was found in the literature. Related progress on Bouchet's 6-flow conjecture for signed/bidirected graphs (e.g., DeVos 2013 establishing a nowhere-zero 12-flow bound for bidirected graphs) does not directly settle this edge-width-conditioned variant.

 Reviewer notes. The OPG page itself (http://www.openproblemgarden.org/op/5_local_tensions) returned ECONNREFUSED and could not be checked for editorial updates. The arXiv search for 'local tension' combined with 'non-orientable' and 'edge-width' returned no results, suggesting the specific conjecture has attracted little direct attention in the literature under that terminology. DeVos's 2013 arXiv preprint 1310.8406 (Flows on Bidirected Graphs) is the closest post-2007 related work: it shows every bidirected graph admitting a nowhere-zero ℤ-flow has a nowhere-zero 12-flow, which by the non-orientable duality framework of DGMVZ gives a 12-local-tension bound for embedded graphs—far weaker than the conjectured 5-local-tension. Progress on Bouchet's 6-flow conjecture for signed graphs (recent papers proving it for cyclically 5-edge-connected cubic signed graphs, arxiv 2601.05692) is in a closely related but technically distinct setting. The Grünbaum conjecture (4-local-tension on orientable surfaces with edge-width ≥ 3) remains open on the orientable side; the non-orientable 5-local-tension conjecture is separate.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 226s.
 

Conjecture. There exists a fixed constant $ c $ (probably $ c=4 $ suffices) so that every embedded (loopless) graph with edge-width $ \ge c $ has a 5-local-tension.

Keywords:
coloring · surface · tension

Discussion

The edge-width of an embedded graph is the length of the shortest non-contractible cycle. Definition Let $ G $ be a directed graph, let $ \Gamma $ be an abelian group, and let $ \phi : E(G) \rightarrow \Gamma $ . Define the height of a walk $ W $ to be the sum of $ \phi $ on the forward edges of $ W $ minus the sum of $ \phi $ on the backward edges of $ W $ (edges are counted according to multiplicity). We call $ \phi $ a tension if the height of every closed walk is zero, and if $ G $ is an embedded graph, we call $ \phi $ a local-tension if the height of every closed walk which forms a contractible curve is zero. If in addition, $ \Gamma = {\mathbb Z} $ and $ 0 < \phi(e) < k $ for some $ k \in {\mathbb Z} $ , we say that $ \phi $ is a $ k $ - tension or a $ k $ - local-tension . If we reverse an edge $ e $ and replace $ \phi(e) $ by $ -\phi(e) $ , this preserves the properties of tension or local-tension. Accordingly, we say that an undirected graph (embedded graph) $ G $ has a $ k $ -tension ( $ k $ -local-tension) if some and thus every orientation of it admits such a map. Proposition A graph has a $ k $ -tension if and only if it is $ k $ -colorable. Proof To see the "if" direction, let $ f : V(G) \rightarrow \{0,\ldots,k-1\} $ be a coloring, orient the edges of $ G $ arbitrarily, and defining $ \phi : E(G) \rightarrow {\mathbb Z} $ by the rule $ \phi(uv) = f(v) - f(u) $ . It is straightforward to check that $ \phi $ is a $ k $ -tension. For the "only if" direction, let $ \phi : E(G) \rightarrow {\mathbb Z} $ be a $ k $ -tension. Now choose a point $ u \in V(G) $ and define the map $ f : V(G) \rightarrow {\mathbb Z}_k $ by the rule that $ f(v) $ is the height of some (and thus every) walk from $ u $ to $ v $ modulo $ k $ . Again, it is straightforward to check that this defines a proper $ k $ -coloring. For graphs on orientable surfaces, local-tensions are dual to flows. More precisely, if $ G $ and $ G^* $ are dual graphs embedded in an orientable surface, then $ G $ has a $ k $ -local-tension if and only if $ G^* $ has a nowhere-zero $ k $ -flow. On non-orientable surfaces, there is a duality between $ k $ -local-tensions in $ G $ and nowhere-zero $ k $ -flows in a bidirected $ G^* $ . Based on this duality we have a couple of conjectures. The first follows from Tutte's 5-flow conjecture , the second from Bouchet's 6-flow conjecture . Conjecture (Tutte) Every loopless graph embedded in an orientable surface has a 5-local-tension. Conjecture (Bouchet) Every loopless graph embedded in any surface has a 6-local-tension. So although, graphs on surfaces may have high chromatic number, thanks to some partial results toward the above conjectures, we know that they always have small local-tensions. For orientable surfaces, there is a famous Conjecture of Grunbaum which is equivalent to the following. Conjecture (Grunbaum) If $ G $ is a simple loopless graph embedded in an orientable surface with edge-width $ \ge 3 $ , then $ G $ has a 4-local-tension. On non-orientable surfaces, it is known that there are graphs of arbitrarily high edge-width which do not admit 4-local-tensions (see [DGMVZ]). However, it remains open whether sufficiently high edge-width forces the existence of a 5-local-tension. Indeed, as suggested by the conjecture at the start of this page, it may be that edge-width at least 4 is enough. Edge-width 3 does not suffice since the embedding of $ K_6 $ in the projective plane does not admit a 5-local-tension.

Bibliography

★ [DGMVZ]
 M. DeVos, L. Goddyn, B. Mohar, D. Vertigan, and X. Zhu, Coloring-flow duality of embedded graphs. Trans. Amer. Math. Soc. 357 (2005), no. 10 MathSciNet
 MathSciNet

Related conjectures

 
 related to
 5-flow conjecture
 partial
 The connection is flow/local-tension surface duality: as the source page states, Tutte's 5-flow conjecture implies the companion conjecture 'every loopless graph embedded in an ORIENTABLE surface has a 5-local-tension' (local-tensions on G dualize to flows on G*). But the headline 5-local-tensions conjecture (edge-width >= c implies 5-local-tension) ranges over all surfaces; on non-orientable surfaces duality produces flows on BIDIRECTED graphs (Bouchet's setting, parameter 6, not 5), so the 5-flow conjecture covers only the orientable subfamily of the source conjecture. Nor does the source imply the 5-flow conjecture (it is a statement about embedded graphs of large edge-width, not all bridgeless graphs). Subfamily implication only, hence related_only.
 

 
 related to
 Bouchet's 6-flow conjecture
 partial
 Bouchet's conjecture concerns nowhere-zero 6-flows on bidirected graphs, which by duality (as both pages note: 'flows on bidirected graphs arise naturally as duals of local-tensions on a non-orientable surface') implies a 6-LOCAL-TENSION statement for graphs embedded in non-orientable surfaces. The headline source conjecture asks for a 5-local-tension under an edge-width >= c hypothesis; the parameters differ (6 vs 5), so Bouchet's conjecture does not imply it, and the source conjecture, being restricted to large edge-width embeddings and to the number 5, does not imply Bouchet's statement about all bidirected graphs. They are linked by the same duality framework and Bouchet's conjecture is evidence/motivation, but there is no implication in either direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
