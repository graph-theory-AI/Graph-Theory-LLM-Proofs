Attack the following open graph-theory problem.

Catalog id: linear_hypergraphs_with_dimension_3
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Drawings
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/linear_hypergraphs_with_dimension_3/
Original entry: http://www.openproblemgarden.org/op/linear_hypergraphs_with_dimension_3
Problem attributed to: de Fraysseix, Hubert, Ossona de Mendez, Patrice, Rosenstiehl, Pierre (posted 2007-09-26)

=== Problem statement (OpenProblemGarden) ===
Title: Linear Hypergraphs with Dimension 3
Conjecture Any linear hypergraph with incidence poset of dimension at most 3 is the intersection hypergraph of a family of triangles and segments in the plane.

=== Discussion / context (OpenProblemGarden) ===
A hypergraph is linear if any two edges may share at most one vertex. The incidence poset of a hypergraph is the vertex-edge inclusion poset. The dimension of a poset $ P $ is the minimum number of linear extentions of $ P $ , whose intersection is $ P $ [DM]. Schnyder proved that the incidence poset of a graph $ G $ has dimension at most $ 3 $ if and only if $ G $ is planar [S89]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar graph has a representation by contacts of triangles [FOR94] and Scheinerman conjectured that every planar graph has a representation by intersection of segments [S84] (claimed to be proved by Gonçalves et al.). A hypergraph is planar if its vertex-edge incidence graph is planar [W]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar linear hypergraph has a representation by contacts of triangles [FOR07] and it has been conjectured that they have a representation by intersection of straight line segments [FO07] (cf Straight line representation of planar linear hypergraphs ). Although the incidence poset of a simple planar hypergraph has dimension at most $ 3 $ (what follows from [BT]), the converse is false: The linear hypergraph with vertices $ 1,\dots,5 $ and edge set $ \{\{1,2\},\{2,3\},\{3,4\},\{1,4\},\{1,3,5\},\{2,4,5\}\} $ has incidence dimension $ 3 $ but is not planar (its vertex-edge incidence graph is a subdivision of $ K_{3,3} $ ). It follows from [O] that the vertices of simple hypergraphs with incidence posets of dimensions $ d $ can be represented by convex sets of the Euclidean space of dimension $ d-1 $ , in such a way that the edges of the hypergraph are exactly the maximal subsets of vertices, such that the corresponding subset of convexes has a non-empty intersection.

=== References listed by OpenProblemGarden ===
- [BT] G.~Brightwell and W.T. Trotter, The order dimension of planar maps, SIAM journal on Discrete Mathematics 10 (1997), no.~4, 515--528.
- [DM] B.~Dushnik and E.W. Miller, Partially ordered sets, Amer. J. Math. 63 (1941), 600--610.
- [FO07] Hubert de Fraysseix, Patrice Ossona de Mendez: Stretching of Jordan arc contact systems, Discrete Applied Mathematics 155 (2007), no. 9, 1079--1095.
- [FOR94] H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, On triangle contact graphs, Combinatorics, Probability and Computing 3 (1994), 233--246.
- *[FOR07] H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, Representation of Planar Hypergraphs by Contacts of Triangles, Proc. of Graph Drawing '07, to appear.
- [O] P.~Ossona~de Mendez, Realization of posets, Journal of Graph Algorithms and Applications 6 (2002), no.~1, 149--153.
- [S84] E.R. Scheinerman, Intersection classes and multiple intersection parameters of graphs, Ph.D. thesis, Princeton University, 1984.
- [S89] W.~Schnyder, Planar graphs and poset dimension, Order 5 (1989), 323--343.
- [W] T.R.S. Walsh, Hypermaps versus bipartite maps, J. Combinatorial Theory 18(B) (1975), 155--163.

=== Catalog page (statement + literature review) ===
Linear Hypergraphs with Dimension 3 — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture that any linear hypergraph whose incidence poset has dimension at most 3 is the intersection hypergraph of a family of triangles and segments in the plane was posted in 2007 and remains open to the best of available evidence. No proof, disproof, or substantial partial result addressing the conjecture as stated could be found in the literature after the posting date. The closely related special case of planar linear hypergraphs was established by de Fraysseix, Ossona de Mendez, and Rosenstiehl (contacts of triangles), but the full poset-dimension-3 conjecture extends beyond planarity and no resolution has been verified.

 Reviewer notes. The Open Problem Garden page was unreachable (ECONNREFUSED), so no on-site status update could be verified. Searches turned up no post-2007 paper specifically addressing this conjecture. The arXiv paper 2411.13985 (Representing Hypergraphs by Point-Line Incidences, 2024) is thematically adjacent but does not address the incidence-poset-dimension-3 conjecture. The Sparsity and Dimension paper (arXiv:1507.01120) addresses poset dimension in the context of sparse graphs but not this hypergraph geometric realization conjecture. Confidence is medium rather than high because exhaustive search of Ossona de Mendez's publication list was not possible (arXiv search timed out).

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. Any linear hypergraph with incidence poset of dimension at most 3 is the intersection hypergraph of a family of triangles and segments in the plane.

Keywords:
Hypergraphs

Discussion

A hypergraph is linear if any two edges may share at most one vertex. The incidence poset of a hypergraph is the vertex-edge inclusion poset. The dimension of a poset $ P $ is the minimum number of linear extentions of $ P $ , whose intersection is $ P $ [DM]. Schnyder proved that the incidence poset of a graph $ G $ has dimension at most $ 3 $ if and only if $ G $ is planar [S89]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar graph has a representation by contacts of triangles [FOR94] and Scheinerman conjectured that every planar graph has a representation by intersection of segments [S84] (claimed to be proved by Gonçalves et al.). A hypergraph is planar if its vertex-edge incidence graph is planar [W]. Fraysseix, Rosenstiehl and Ossona de Mendez proved that every planar linear hypergraph has a representation by contacts of triangles [FOR07] and it has been conjectured that they have a representation by intersection of straight line segments [FO07] (cf Straight line representation of planar linear hypergraphs ). Although the incidence poset of a simple planar hypergraph has dimension at most $ 3 $ (what follows from [BT]), the converse is false: The linear hypergraph with vertices $ 1,\dots,5 $ and edge set $ \{\{1,2\},\{2,3\},\{3,4\},\{1,4\},\{1,3,5\},\{2,4,5\}\} $ has incidence dimension $ 3 $ but is not planar (its vertex-edge incidence graph is a subdivision of $ K_{3,3} $ ). It follows from [O] that the vertices of simple hypergraphs with incidence posets of dimensions $ d $ can be represented by convex sets of the Euclidean space of dimension $ d-1 $ , in such a way that the edges of the hypergraph are exactly the maximal subsets of vertices, such that the corresponding subset of convexes has a non-empty intersection.

Bibliography

 [BT]
 G.~Brightwell and W.T. Trotter, The order dimension of planar maps, SIAM journal on Discrete Mathematics 10 (1997), no.~4, 515--528.

 [DM]
 B.~Dushnik and E.W. Miller, Partially ordered sets, Amer. J. Math. 63 (1941), 600--610.

 [FO07]
 Hubert de Fraysseix, Patrice Ossona de Mendez: Stretching of Jordan arc contact systems, Discrete Applied Mathematics 155 (2007), no. 9, 1079--1095.

 [FOR94]
 H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, On triangle contact graphs, Combinatorics, Probability and Computing 3 (1994), 233--246.

★ [FOR07]
 H.~de Fraysseix, P.~Ossona~de Mendez, and P.~Rosenstiehl, Representation of Planar Hypergraphs by Contacts of Triangles, Proc. of Graph Drawing '07, to appear.

 [O]
 P.~Ossona~de Mendez, Realization of posets, Journal of Graph Algorithms and Applications 6 (2002), no.~1, 149--153.

 [S84]
 E.R. Scheinerman, Intersection classes and multiple intersection parameters of graphs, Ph.D. thesis, Princeton University, 1984.

 [S89]
 W.~Schnyder, Planar graphs and poset dimension, Order 5 (1989), 323--343.

 [W]
 T.R.S. Walsh, Hypermaps versus bipartite maps, J. Combinatorial Theory 18(B) (1975), 155--163.
