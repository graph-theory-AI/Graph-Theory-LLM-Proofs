Attack the following open graph-theory problem.

Catalog id: the_berge_fulkerson_conjecture
Source: OpenProblemGarden (importance: Outstanding ✭✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Matchings
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_berge_fulkerson_conjecture/
Original entry: http://www.openproblemgarden.org/op/the_berge_fulkerson_conjecture
Problem attributed to: Berge, Claude, Fulkerson, Delbert R. (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: The Berge-Fulkerson conjecture
Conjecture If $ G $ is a bridgeless cubic graph, then there exist 6 perfect matchings $ M_1,\ldots,M_6 $ of $ G $ with the property that every edge of $ G $ is contained in exactly two of $ M_1,\ldots,M_6 $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is due to Berge and Fulkerson, and appears first in [F] (see [S79b]). If $ G $ is 3- edge-colorable , then we may choose three perfect matchings $ M_1,M_2,M_3 $ so that every edge is in exactly one. Taking each of these twice gives us 6 perfect matchings with the properties described above. Thus, the above conjecture holds trivially for 3-edge-colorable graphs. There do exist bridgeless cubic graphs which are not 3-edge-colorable (for instance the Petersen graph ), but the above conjecture asserts that every such graph is close to being 3-edge-colorable. Definition: An $ r $ -graph is an $ r $ - regular graph $ G $ on an even number of vertices with the property that every edge-cut which separates $ V(G) $ into two sets of odd cardinality has size at least $ r $ . Observe that a cubic graph is a 3-graph if and only if it has no bridge. If G is an $ r $ -regular graph which has an $ r $ -edge-coloring, then every color class is a perfect matching, so $ |V(G)| $ must be even, and every color must appear in every edge-cut which separates $ V(G) $ into two sets of odd size, so every edge-cut of this form must have size at least $ r $ . Thus, every $ r $ -edge-colorable $ r $ -regular graph is an $ r $ -graph. In a sense, we may view the $ r $ -graphs as the $ r $ -regular graphs which have the obvious necessary conditions to be $ r $ -edge-colorable. Seymour [S79b] defined $ r $ -graphs and offered the following generalization of the Berge-Fulkerson conjecture. Conjecture (The generalized Berge-Fulkerson conjecture (Seymour)) Let $ G $ be an $ r $ -graph. Then there exist $ 2r $ perfect matchings $ M_1,\ldots,M_{2r} $ of $ G $ with the property that every edge of $ G $ is contained in exactly two of $ M_1,\ldots,M_{2r} $ . More generally, for a graph $ G=(V,E) $ , one may consider the vector space of real numbers indexed by $ E $ . We associate every perfect matching $ M $ with its characteristic vector. In this context, the Berge-Fulkerson conjecture asserts that for every 3-graph, the vector which is identically 1 may be written as a half-integer combination of perfect matchings. Edmonds matching polytope theorem [E] gives a complete characterization of what vectors in $ {\mathbb R}^E $ which can be written as a nonnegative real combination of perfect matchings. A particular consequence of this theorem is that the vector which is identically 1 can be written as a nonnegative rational combination of perfect matchings if G is an $ r $ -graph. It follows from this that for every $ r $ -graph $ G $ , there is a list of perfect matchings $ M_1,\ldots,M_{kr} $ so that every edge is contained in exactly $ k $ of them. Unfortunately, the particular $ k $ depends on the graph. The following weak version of the Berge-Fulkerson conjecture asserts that this dependence is inessential. Conjecture (the weak Berge-Fulkerson conjecture) There exists a positive integer $ k $ with the following property. Every 3-graph $ G $ has a list of $ 3k $ perfect matchings such that every edge of $ G $ is contained in exactly $ k $ of them. There is a fascinating theorem of Lovasz [L] that characterizes which vectors in $ {\mathbb Z}^E $ can be written as an integer combination of perfect matchings. However, very little is known about nonnegative integer combinations of perfect matchings. In particular, if the Berge-Fulkerson conjecture is true, then for every 3-graph $ G=(V,E) $ , there is a list of 5 perfect matchings with union $ E $ (take any 5 of the 6 perfect matchings given by the conjecture). The following weakening of this (suggested by Berge) is still open. Conjecture There exists a fixed integer $ k $ such that the edge set of every 3-graph can be written as a union of $ k $ perfect matchings. Another consequence of the Berge-Fulkerson conjecture would be that every 3-graph has 3 perfect matchings with empty intersection (take any 3 of the 6 perfect matchings given by the conjecture). The following weakening of this (also suggested by Berge) is still open. Conjecture There exists a fixed integer $ k $ such that every 3-graph has a list of $ k $ perfect matchings with empty intersection.

=== References listed by OpenProblemGarden ===
- [E] J. Edmonds, Maximum matching and a polyhedron with 0,1-vertices, J. Res. Nat. Bur Stand B, Math & Math Phys. 69B (1965), 125-130.
- [F] D.R. Fulkerson, Blocking and anti-blocking pairs of polyhedra, Math. Programming 1 (1971) 168-194. MathSciNet
- [KKN] T. Kaiser, D. Kral, and S. Norine, Unions of perfect matchings in cubic graphs
- [L] L. Lovasz, Matching structure and the matching lattice, J. Combin. Theory Ser. B 43 (1987), 187-222. MathSciNet
- [R] R. Rizzi, Indecomposable r-graphs and some other counterexamples, J. Graph Theory 32 (1999), 1-15. MathSciNet
- [S79a] P.D. Seymour, "Some unsolved problems on one-factorizations of graphs", Graph theory and Related Topics, J.A. Bondy and U.S.R. Murty (Editors), Academic, New York (1979), 367-368.
- [S79b] P.D. Seymour, On multi-colourings of cubic graphs, and conjectures of Fulkerson and Tutte, Proc. London Math Soc. 38 (1979), 423-460. MathSciNet

=== Catalog page (statement + literature review) ===
The Berge-Fulkerson conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Berge-Fulkerson conjecture remains open in full generality. Notable post-posting progress includes the proof of Mazzuoccolo's conjecture (any finite collection of disjoint odd circuits in a bridgeless cubic graph is hit by a single perfect matching), the verification of Berge's covering conjecture for cubic graphs with colouring defect at most 3, and the introduction and partial verification of an oriented variant for Isaacs flower snarks. Repeated attempts to verify the conjecture for various families of snarks have succeeded for those families but left the general conjecture untouched.

 Cited literature (3)

 
 
 
partial Disjoint odd circuits in a bridgeless cubic graph can be quelled by a single perfect matching
 (2023)
 

 
 František Kardoš, Edita Máčajová, Jean Paul Zerafa · Journal of Combinatorial Theory, Series B · arXiv:2204.10021 · doi:10.1016/j.jctb.2022.12.003

Proves Mazzuoccolo's conjecture: for any collection of disjoint odd circuits in a bridgeless cubic graph G, there exists a perfect matching of G containing at least one edge from each circuit — a consequence that would follow from the Berge-Fulkerson conjecture.
 

 
 
partial Berge's conjecture for cubic graphs with small colouring defect
 (2022)
 

 
 Ján Karabáš, Edita Máčajová, Roman Nedela, Martin Škoviera · arXiv preprint · arXiv:2210.13234

Proves Berge's conjecture (the edge set of every bridgeless cubic graph is coverable by 5 perfect matchings) for graphs with colouring defect at most 3, and shows that cyclically 4-edge-connected such graphs need only 4 matchings (Petersen graph excepted).
 

 
 
partial Graph Puzzles I.1: Oriented Berge-Fulkerson Conjecture
 (2025)
 

 
 Nikolay Ulyanov · arXiv preprint · arXiv:2501.05348

Proposes an oriented variant of the Berge-Fulkerson conjecture and proves it for the family of Isaacs flower snarks, establishing connections to ribbon graphs and oriented cycle double covers.
 

 

 Reviewer notes. Several ScienceDirect and Wiley journal pages returned HTTP 403 (including papers on rotation snarks by Máčajová–Škoviera, superposition snarks, and C(12)-linked permutation graphs by Liu et al., J. Graph Theory 2021); these could not be verified and are therefore excluded from since_posted. The Karabáš et al. preprint (2210.13234) was revised as recently as January 2025 but no peer-reviewed journal publication was confirmed. The full Berge-Fulkerson conjecture remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. If $ G $ is a bridgeless cubic graph, then there exist 6 perfect matchings $ M_1,\ldots,M_6 $ of $ G $ with the property that every edge of $ G $ is contained in exactly two of $ M_1,\ldots,M_6 $ .

Keywords:
cubic · perfect matching

Discussion

This conjecture is due to Berge and Fulkerson, and appears first in [F] (see [S79b]). If $ G $ is 3- edge-colorable , then we may choose three perfect matchings $ M_1,M_2,M_3 $ so that every edge is in exactly one. Taking each of these twice gives us 6 perfect matchings with the properties described above. Thus, the above conjecture holds trivially for 3-edge-colorable graphs. There do exist bridgeless cubic graphs which are not 3-edge-colorable (for instance the Petersen graph ), but the above conjecture asserts that every such graph is close to being 3-edge-colorable. Definition: An $ r $ -graph is an $ r $ - regular graph $ G $ on an even number of vertices with the property that every edge-cut which separates $ V(G) $ into two sets of odd cardinality has size at least $ r $ . Observe that a cubic graph is a 3-graph if and only if it has no bridge. If G is an $ r $ -regular graph which has an $ r $ -edge-coloring, then every color class is a perfect matching, so $ |V(G)| $ must be even, and every color must appear in every edge-cut which separates $ V(G) $ into two sets of odd size, so every edge-cut of this form must have size at least $ r $ . Thus, every $ r $ -edge-colorable $ r $ -regular graph is an $ r $ -graph. In a sense, we may view the $ r $ -graphs as the $ r $ -regular graphs which have the obvious necessary conditions to be $ r $ -edge-colorable. Seymour [S79b] defined $ r $ -graphs and offered the following generalization of the Berge-Fulkerson conjecture. Conjecture (The generalized Berge-Fulkerson conjecture (Seymour)) Let $ G $ be an $ r $ -graph. Then there exist $ 2r $ perfect matchings $ M_1,\ldots,M_{2r} $ of $ G $ with the property that every edge of $ G $ is contained in exactly two of $ M_1,\ldots,M_{2r} $ . More generally, for a graph $ G=(V,E) $ , one may consider the vector space of real numbers indexed by $ E $ . We associate every perfect matching $ M $ with its characteristic vector. In this context, the Berge-Fulkerson conjecture asserts that for every 3-graph, the vector which is identically 1 may be written as a half-integer combination of perfect matchings. Edmonds matching polytope theorem [E] gives a complete characterization of what vectors in $ {\mathbb R}^E $ which can be written as a nonnegative real combination of perfect matchings. A particular consequence of this theorem is that the vector which is identically 1 can be written as a nonnegative rational combination of perfect matchings if G is an $ r $ -graph. It follows from this that for every $ r $ -graph $ G $ , there is a list of perfect matchings $ M_1,\ldots,M_{kr} $ so that every edge is contained in exactly $ k $ of them. Unfortunately, the particular $ k $ depends on the graph. The following weak version of the Berge-Fulkerson conjecture asserts that this dependence is inessential. Conjecture (the weak Berge-Fulkerson conjecture) There exists a positive integer $ k $ with the following property. Every 3-graph $ G $ has a list of $ 3k $ perfect matchings such that every edge of $ G $ is contained in exactly $ k $ of them. There is a fascinating theorem of Lovasz [L] that characterizes which vectors in $ {\mathbb Z}^E $ can be written as an integer combination of perfect matchings. However, very little is known about nonnegative integer combinations of perfect matchings. In particular, if the Berge-Fulkerson conjecture is true, then for every 3-graph $ G=(V,E) $ , there is a list of 5 perfect matchings with union $ E $ (take any 5 of the 6 perfect matchings given by the conjecture). The following weakening of this (suggested by Berge) is still open. Conjecture There exists a fixed integer $ k $ such that the edge set of every 3-graph can be written as a union of $ k $ perfect matchings. Another consequence of the Berge-Fulkerson conjecture would be that every 3-graph has 3 perfect matchings with empty intersection (take any 3 of the 6 perfect matchings given by the conjecture). The following weakening of this (also suggested by Berge) is still open. Conjecture There exists a fixed integer $ k $ such that every 3-graph has a list of $ k $ perfect matchings with empty intersection.

Bibliography

 [E]
 J. Edmonds, Maximum matching and a polyhedron with 0,1-vertices, J. Res. Nat. Bur Stand B, Math & Math Phys. 69B (1965), 125-130.

 [F]
 D.R. Fulkerson, Blocking and anti-blocking pairs of polyhedra, Math. Programming 1 (1971) 168-194. MathSciNet
 MathSciNet

 [KKN]
 T. Kaiser, D. Kral, and S. Norine, Unions of perfect matchings in cubic graphs
 Unions of perfect matchings in cubic graphs

 [L]
 L. Lovasz, Matching structure and the matching lattice, J. Combin. Theory Ser. B 43 (1987), 187-222. MathSciNet
 MathSciNet

 [R]
 R. Rizzi, Indecomposable r-graphs and some other counterexamples, J. Graph Theory 32 (1999), 1-15. MathSciNet
 MathSciNet

 [S79a]
 P.D. Seymour, "Some unsolved problems on one-factorizations of graphs", Graph theory and Related Topics, J.A. Bondy and U.S.R. Murty (Editors), Academic, New York (1979), 367-368.

 [S79b]
 P.D. Seymour, On multi-colourings of cubic graphs, and conjectures of Fulkerson and Tutte, Proc. London Math Soc. 38 (1979), 423-460. MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 Petersen coloring conjecture
 partial
 Both conjectures concern bridgeless cubic graphs, so the hypothesis classes coincide. A Petersen coloring maps the three edges incident to any vertex of G to three mutually adjacent edges of the Petersen graph P, i.e., to the edge-triple at a vertex of P. P has six perfect matchings covering every edge of P exactly twice; the preimage under the coloring of each is a perfect matching of G (exactly one of the three edges at each vertex of G is mapped into it), and each edge e of G lies in exactly two of the six preimages, since f(e) lies in exactly two of P's matchings. This is Jaeger's classical observation, and the OPG source context states explicitly that the Petersen coloring conjecture implies the Berge-Fulkerson conjecture.
 

 
 implies
 The intersection of two perfect matchings
 partial
 Rigorous: any perfect matching meets every odd edge-cut delta(X) in an odd (hence >=1) number of edges, since the odd set X cannot be perfectly matched internally. Given a Fulkerson cover M1..M6 with every edge in exactly two matchings, if an odd cut C were contained in M1 cap M2, every edge of C would already have both its memberships used by M1 and M2, forcing M3 cap C to be empty -- contradicting that the perfect matching M3 meets C. So M1 cap M2 contains no odd edge-cut, which is exactly the target. Direction correct: Berge-Fulkerson is the stronger statement.
 

 
 related to
 (m,n)-cycle covers
 partial
 The source statement (every bridgeless graph has a (5,2)-cycle cover) is exactly the 5-cycle-double-cover conjecture, the (5,2) entry of the OPG chart; Berge-Fulkerson is equivalent (via complementing the six perfect matchings by 2-factors, extended from cubic graphs) to the (6,4) entry of the same chart. So the mention is that both conjectures are different boxes of the same (m,n)-cycle-cover table, not that one implies the other. No implication between 5CDC and Berge-Fulkerson is known in either direction (even whether BF implies the ordinary CDC is open); a (5,2)-cover does not yield a (6,4)-cover by any simple combination, nor conversely. Hence: strongly thematically linked, no established implication.
 

 
 related to
 Cycle double cover conjecture
 partial
 The CDC page only says 'Note the similarity between this conjecture and the Berge-Fulkerson conjecture' - an explicit analogy, not an implication. No implication is known in either direction: BF gives (via complements of the 6 matchings) six 2-factors covering each edge exactly 4 times, i.e. a cycle FOUR cover, which is already a theorem (Bermond-Jackson-Jaeger) and does not yield a double cover; conversely CDC says nothing about perfect matchings of cubic graphs. Both are known consequences of the common strengthening (Petersen coloring conjecture), which makes them thematically linked siblings, not logically comparable.
 

 
 related to
 Faithful cycle covers
 open
 The OPG page explicitly says only 'Note the similarity of this to The Berge-Fulkerson conjecture' — a thematic comparison, not an implication. No implication holds via the obvious route: Berge-Fulkerson is equivalent (by complementing the 6 perfect matchings into 2-factors) to covering a cubic graph by six 2-factors using each edge exactly 4 times, but a faithful cover of (G,4) imposes neither the 2-factor structure nor the count of six cycles; indeed Bermond-Jackson-Jaeger already proved every bridgeless graph has a cycle cover using each edge exactly 4 times, yet Berge-Fulkerson remains open. Conversely Berge-Fulkerson concerns perfect matchings of cubic graphs and says nothing about general even admissible weightings. Companion conjectures with no known implication either way: related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
