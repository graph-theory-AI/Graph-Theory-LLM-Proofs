Attack the following open graph-theory problem.

Catalog id: drawing_disconnected_graphs_on_surfaces
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/drawing_disconnected_graphs_on_surfaces/
Original entry: http://www.openproblemgarden.org/op/drawing_disconnected_graphs_on_surfaces
Problem attributed to: DeVos, Matt, Mohar, Bojan, Samal, Robert (posted 2007-05-12)

=== Problem statement (OpenProblemGarden) ===
Title: Drawing disconnected graphs on surfaces
Conjecture Let $ G $ be the disjoint union of the graphs $ G_1 $ and $ G_2 $ and let $ \Sigma $ be a surface. Is it true that every optimal drawing of $ G $ on $ \Sigma $ has the property that $ G_1 $ and $ G_2 $ are disjoint?

=== Discussion / context (OpenProblemGarden) ===
We insist on the usual restrictions for drawings (as in The Crossing Number of the Complete Graph ). Although both crossing numbers and embeddings of graphs on general surfaces are rich and well-studied subjects, their common generalization - drawing graphs on general surfaces has received very little attention. The question highlighted here appears to be quite basic in nature, but due to the combined difficulties of crossings and general surfaces, it may be quite difficult to resolve. This conjecture is trivially true when $ \Sigma $ is the plane, and DeVos, Mohar, and Samal have proved that it also holds when $ \Sigma $ is the projective plane. It is open for all other surfaces to the best of my (M. DeVos) knowledge.

=== Catalog page (statement + literature review) ===
Drawing disconnected graphs on surfaces — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Since the problem was posted, the conjecture has been proved for the Klein bottle by Beaudou, Gerbaud, Grappe, and Palesi (2010): every optimal drawing of a disconnected graph on the Klein bottle draws the connected components disjointly. The conjecture thus holds for the plane (trivially), the projective plane (DeVos–Mohar–Šámal, pre-posting), and the Klein bottle, but remains open for the torus and all other surfaces. A 2015 extended abstract by Cabello, Mohar, and Šámal reports a partial result for the torus by reducing the problem to a question in the geometry of numbers, but the torus case is not fully resolved.

 Cited literature (1)

 
 
 
partial Drawing disconnected graphs on the Klein bottle
 (2010)
 

 
 Laurent Beaudou, Antoine Gerbaud, Roland Grappe, Frederic Palesi · Graphs and Combinatorics · arXiv:0810.0508 · doi:10.1007/s00373-010-0928-7

Proves the DeVos–Mohar–Šámal conjecture for the Klein bottle: in any crossing-optimal drawing of a disconnected graph on the Klein bottle, the connected components must be drawn in disjoint regions.
 

 

 Reviewer notes. A 2015 extended abstract 'Drawing a disconnected graph on the torus' by Cabello, Mohar, and Šámal (Electronic Notes in Discrete Mathematics 49, pp. 779–786, arXiv not found) reports reduction to a geometry-of-numbers question and a partial result for the torus, but could not be verified via WebFetch (ScienceDirect and PDF returned 403/binary). This paper was therefore not included in since_posted despite strong search-result evidence of its existence. The DOI 10.1007/s00373-010-0928-7 for the Klein bottle paper was confirmed by multiple search results but the Springer page required authentication; the arXiv preprint at 0810.0508 was directly verified. No papers resolving the conjecture for the torus or any orientable surface of genus ≥ 1 were found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Let $ G $ be the disjoint union of the graphs $ G_1 $ and $ G_2 $ and let $ \Sigma $ be a surface. Is it true that every optimal drawing of $ G $ on $ \Sigma $ has the property that $ G_1 $ and $ G_2 $ are disjoint?

Keywords:
crossing number · surface

Discussion

We insist on the usual restrictions for drawings (as in The Crossing Number of the Complete Graph ). Although both crossing numbers and embeddings of graphs on general surfaces are rich and well-studied subjects, their common generalization - drawing graphs on general surfaces has received very little attention. The question highlighted here appears to be quite basic in nature, but due to the combined difficulties of crossings and general surfaces, it may be quite difficult to resolve. This conjecture is trivially true when $ \Sigma $ is the plane, and DeVos, Mohar, and Samal have proved that it also holds when $ \Sigma $ is the projective plane. It is open for all other surfaces to the best of my (M. DeVos) knowledge.

Related conjectures

 
 related to
 The Crossing Number of the Complete Graph
 partial
 The mention is purely definitional: the source page says 'We insist on the usual restrictions for drawings (as in The Crossing Number of the Complete Graph)', importing the standard good-drawing conditions and nothing more. There is no logical dependence: the truth of the exact formula for cr(K_n) in the plane neither forces nor follows from the statement that optimal drawings of a disconnected graph on an arbitrary surface keep the components disjoint (the latter is about arbitrary graphs G_1, G_2 and arbitrary surfaces, the former about one specific family in the plane). They share only the theme of crossing-minimal drawings.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
