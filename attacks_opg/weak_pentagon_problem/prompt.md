Attack the following open graph-theory problem.

Catalog id: weak_pentagon_problem
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Homomorphisms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/weak_pentagon_problem/
Original entry: http://www.openproblemgarden.org/op/weak_pentagon_problem
Problem attributed to: Samal, Robert (posted 2007-07-13)

=== Problem statement (OpenProblemGarden) ===
Title: Weak pentagon problem
Conjecture If $ G $ is a cubic graph not containing a triangle, then it is possible to color the edges of $ G $ by five colors, so that the complement of every color class is a bipartite graph.

=== Discussion / context (OpenProblemGarden) ===
This conjecture has several reformulations: the conclusion of the conjecture can be replaced by either of the following: \item $ G $ has a homomorphism to the Clebsch graph . \item there is a cut-continuous mapping from $ G $ to $ C_5 $ . For the latter variant, few definitions are in place. A cut-continuous mapping from a graph~ $ G $ to a graph~ $ H $ is a mapping $ f : E(G) \to E(H) $ such that the preimage of every cut in~ $ H $ is a cut in~ $ G $ . Here, by a cut in~ $ H $ we mean the edge-set of a spanning bipartite subgraph of~ $ H $ ---less succinctly, it is the set of all edges leaving some subset of vertices of~ $ H $ . Cut-continuous mappings are closely related with graph homomorphisms (see [DNR], [S]). In particular, every homomorphism from~ $ G $ to~ $ H $ naturally induces a cut-continuous mapping from~ $ G $ to~ $ H $ ; thus, the presented conjecture can be thought of as a weaker version of Nesetril's Pentagon problem . We mention a generalization of the conjecture, that deals with longer cycles/larger number of colors. The $ n $ -dimensional projective cube , denoted $ PQ_n $ , is the simple graph obtained from the $ (n+1) $ -dimensional cube~ $ Q_{n+1} $ by identifying pairs of antipodal vertices (vertices that differ in all coordinates). Note that $ PQ_4 $ is the Clebsch graph . Question What is the largest integer $ k $ with the property that all cubic graphs of sufficiently high girth have a homomorphism to $ PQ_{2k} $ ? Again, the question has several reformulations due to the following simple proposition. Proposition For every graph $ G $ and nonnegative integer $ k $ , the following properties are equivalent. \item There exists a coloring of~ $ E(G) $ by $ 2k+1 $ colors so that the complement of every color class is a bipartite graph. \item $ G $ has a homomorphism to $ PQ_{2k} $ \item $ G $ has a cut-continuous mapping to~ $ C_{2k+1} $ There are high-girth cubic graphs with the largest cut of size less then $ 0.94\cdot |E| $ . Such graphs do not admit a homomorphism to $ PQ_{2k} $ for any $ k \ge 8 $ , so there is indeed some largest integer~ $ k $ in the above question. To bound this largest~ $ k $ from below, recall that every cubic graph maps homomorphically to $ K_4 = PQ_2 $ . Moreover, it is known [DS] that cubic graphs of girth at least 17 admit a homomorphism to $ PQ_4 $ (the Clebsch graph). This shows $ k\ge 2 $ (and also provides a support for the main conjecture).

=== References listed by OpenProblemGarden ===
- [DNR] Matt DeVos, Jaroslav Nesetril and Andre Raspaud: On edge-maps whose inverse preserves flows and tensions, \MRref{MR2279171}
- *[DS] Matt Devos, Robert Samal: \arXiv[High Girth Cubic Graphs Map to the Clebsch Graph}{math.CO/0602580}
- [S] Robert Samal, On XY mappings, PhD thesis, Charles University 2006, tech. report

=== Catalog page (statement + literature review) ===
Weak pentagon problem — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The weak pentagon conjecture — equivalently, that every triangle-free cubic graph admits a homomorphism to the Clebsch graph $PQ_4$ — remains open in full generality. The strongest verified positive evidence is still structural/special-class progress: DeVos–Šámal proved the high-girth case before the OPG posting, Naserasr proved the triangle-free planar case before the posting and later showed the Clebsch graph is the smallest triangle-free planar bound, and Naserasr–Nigussie–Škrekovski extended the Clebsch-homomorphism result to all triangle-free graphs with no $K_5$ minor.

 Cited literature (2)

 
 
 
partial Homomorphisms of triangle-free graphs without a K5-minor
 (2009)
 

 
 Reza Naserasr, Yared Nigussie, Riste Škrekovski · Discrete Mathematics · doi:10.1016/j.disc.2009.04.032

Extends the Clebsch-graph homomorphism result from triangle-free planar graphs to all triangle-free graphs with no $K_5$ minor, giving a post-posting special class that includes cubic examples.
 

 
 
partial Mapping planar graphs into projective cubes
 (2013)
 

 
 Reza Naserasr · Journal of Graph Theory · doi:10.1002/jgt.21708

Shows that the Clebsch graph is the smallest triangle-free graph bounding all triangle-free planar graphs, strengthening the planar special case relevant to the weak pentagon conjecture.
 

 

 Reviewer notes. The core high-girth theorem of DeVos–Šámal (arXiv:math/0602580; author PDFs also verified) predates the 2007-07-13 OPG posting and is already cited in the OPG statement, so it is not listed in since_posted. Naserasr's 'Homomorphisms and edge-colourings of planar graphs' (JCTB 97(3), 2007; DOI 10.1016/j.jctb.2006.07.001) also predates the posting and proves the triangle-free planar case via the Clebsch graph. The post-posting 2009 Discrete Mathematics paper verifies a broader minor-closed special class, and the 2013 Journal of Graph Theory paper verifies optimality of the planar Clebsch bound; neither resolves arbitrary triangle-free cubic graphs. Targeted searches for a proof or counterexample to Šámal's full cubic triangle-free conjecture found no resolution.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. If $ G $ is a cubic graph not containing a triangle, then it is possible to color the edges of $ G $ by five colors, so that the complement of every color class is a bipartite graph.

Keywords:
Clebsch graph · cut-continuous mapping · edge-coloring · homomorphism · pentagon

Discussion

This conjecture has several reformulations: the conclusion of the conjecture can be replaced by either of the following: \item $ G $ has a homomorphism to the Clebsch graph . \item there is a cut-continuous mapping from $ G $ to $ C_5 $ . For the latter variant, few definitions are in place. A cut-continuous mapping from a graph~ $ G $ to a graph~ $ H $ is a mapping $ f : E(G) \to E(H) $ such that the preimage of every cut in~ $ H $ is a cut in~ $ G $ . Here, by a cut in~ $ H $ we mean the edge-set of a spanning bipartite subgraph of~ $ H $ ---less succinctly, it is the set of all edges leaving some subset of vertices of~ $ H $ . Cut-continuous mappings are closely related with graph homomorphisms (see [DNR], [S]). In particular, every homomorphism from~ $ G $ to~ $ H $ naturally induces a cut-continuous mapping from~ $ G $ to~ $ H $ ; thus, the presented conjecture can be thought of as a weaker version of Nesetril's Pentagon problem . We mention a generalization of the conjecture, that deals with longer cycles/larger number of colors. The $ n $ -dimensional projective cube , denoted $ PQ_n $ , is the simple graph obtained from the $ (n+1) $ -dimensional cube~ $ Q_{n+1} $ by identifying pairs of antipodal vertices (vertices that differ in all coordinates). Note that $ PQ_4 $ is the Clebsch graph . Question What is the largest integer $ k $ with the property that all cubic graphs of sufficiently high girth have a homomorphism to $ PQ_{2k} $ ? Again, the question has several reformulations due to the following simple proposition. Proposition For every graph $ G $ and nonnegative integer $ k $ , the following properties are equivalent. \item There exists a coloring of~ $ E(G) $ by $ 2k+1 $ colors so that the complement of every color class is a bipartite graph. \item $ G $ has a homomorphism to $ PQ_{2k} $ \item $ G $ has a cut-continuous mapping to~ $ C_{2k+1} $ There are high-girth cubic graphs with the largest cut of size less then $ 0.94\cdot |E| $ . Such graphs do not admit a homomorphism to $ PQ_{2k} $ for any $ k \ge 8 $ , so there is indeed some largest integer~ $ k $ in the above question. To bound this largest~ $ k $ from below, recall that every cubic graph maps homomorphically to $ K_4 = PQ_2 $ . Moreover, it is known [DS] that cubic graphs of girth at least 17 admit a homomorphism to $ PQ_4 $ (the Clebsch graph). This shows $ k\ge 2 $ (and also provides a support for the main conjecture).

Bibliography

 [DNR]
 Matt DeVos, Jaroslav Nesetril and Andre Raspaud: On edge-maps whose inverse preserves flows and tensions, \MRref{MR2279171}

★ [DS]
 Matt Devos, Robert Samal: \arXiv[High Girth Cubic Graphs Map to the Clebsch Graph}{math.CO/0602580}

 [S]
 Robert Samal, On XY mappings, PhD thesis, Charles University 2006, tech. report
 tech. report

Related conjectures

 
 related to
 Pentagon problem
 open
 Conclusion-wise the Pentagon problem is stronger: a homomorphism G -> C5 induces a cut-continuous mapping G -> C5, which is exactly the Weak pentagon conclusion (equivalently, edge 5-coloring with bipartite color-class complements / homomorphism to the Clebsch graph); the OPG text calls the weak conjecture 'a weaker version' for this reason. But the hypothesis classes are not nested in the required direction: Pentagon assumes girth at least g for sufficiently large g, while Weak pentagon covers ALL triangle-free (girth >= 4) cubic graphs. A positive Pentagon answer would establish the weak conclusion only for high-girth graphs, leaving girths 4..g-1 unsettled, so the full statements do not stand in an implication; the connection is instance-wise on a subfamily. Hence related_only (Pentagon truth would settle the high-girth part and be strong evidence).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
