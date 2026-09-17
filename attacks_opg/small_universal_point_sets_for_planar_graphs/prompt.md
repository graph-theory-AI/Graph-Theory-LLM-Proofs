Attack the following open graph-theory problem.

Catalog id: small_universal_point_sets_for_planar_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Topological Graph Theory » Drawings
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/small_universal_point_sets_for_planar_graphs/
Original entry: http://www.openproblemgarden.org/op/small_universal_point_sets_for_planar_graphs
Problem attributed to: Mohar, Bojan (posted 2007-05-22)

=== Problem statement (OpenProblemGarden) ===
Title: Universal point sets for planar graphs
We say that a set $ P \subseteq {\mathbb R}^2 $ is $ n $ - universal if every $ n $ vertex planar graph can be drawn in the plane so that each vertex maps to a distinct point in $ P $ , and all edges are (non-intersecting) straight line segments. Question Does there exist an $ n $ -universal set of size $ O(n) $ ?

=== Discussion / context (OpenProblemGarden) ===
More generally, if we let $ f(n) $ denote the size of the smallest $ n $ -universal set, we are interested in the behaviour of $ f $ . The best known upper bound is $ f(n) = O(n^2) $ . Indeed, every $ n $ -vertex planar graph can be drawn as required in the $ n \times n $ grid [dFPP], [S]. On the flip side, it is known that $ f(n) \ge 1.098n $ for sufficiently large $ n $ [CH].

=== References listed by OpenProblemGarden ===
- [CH] M. Chrobak and H.Karloff. A lower bound on the size of universal sets for planar graphs. SIGACT News, 20:83-86, 1989.
- [dFPP] H. de Fraysseix, J. Pach, and R. Pollack. How to draw a planar graph on a grid. Combinatorica, 10(1):41-51, 1990. MathSciNet
- [S] W. Schnyder. Embedding planar graphs on the grid. In Proc. 1st ACM-SIAM Sympos. Discrete Algorithms, pages 138-148, 1990.

=== Catalog page (statement + literature review) ===
Universal point sets for planar graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The question of whether an $n$-universal set of size $O(n)$ exists for all $n$-vertex planar graphs remains open. The best general upper bound has been improved from $n^2/2 - O(n)$ to $n^2/4 - \Theta(n)$ (Bannister et al., 2014), and the lower bound has been raised from $1.098n$ to $(1.293-o(1))n$ (Scheucher et al., 2019). For restricted classes, linear-size universal point sets of size $2n-2$ have been achieved for bipartite planar graphs and planar graphs of maximum degree 3 (Felsner et al., 2023).

 Cited literature (4)

 
 
 
partial Superpatterns and Universal Point Sets
 (2014)
 

 
 Michael J. Bannister, Zhanpeng Cheng, William E. Devanny, David Eppstein · Journal of Graph Algorithms and Applications · arXiv:1308.0403

Improved the upper bound on universal point set size for all planar graphs from $n^2/2 - O(n)$ to $n^2/4 - \Theta(n)$ via superpatterns, and proved near-linear universal point sets suffice for planar graphs of bounded pathwidth.
 

 
 
partial On Universal Point Sets for Planar Graphs
 (2013)
 

 
 Jean Cardinal, Michael Hoffmann, Vincent Kusters · arXiv preprint · arXiv:1209.3594

Proved there is no $n$-universal point set of size $n$ for any $n \geq 15$, and verified via exhaustive search that universal point sets exist for all planar graphs on $n \leq 10$ vertices.
 

 
 
partial A Note On Universal Point Sets for Planar Graphs
 (2019)
 

 
 Manfred Scheucher, Hendrik Schrezenmaier, Raphael Steiner · 27th International Symposium on Graph Drawing and Network Visualization (GD 2019) · arXiv:1811.06482

Improved the lower bound from $1.235n$ to $(1.293-o(1))n$, and showed by exhaustive computer search that no set of 11 points admits straight-line drawings of all planar graphs on 11 vertices.
 

 
 
partial Linear Size Universal Point Sets for Classes of Planar Graphs
 (2023)
 

 
 Stefan Felsner, Hendrik Schrezenmaier, Felix Schröder, Raphael Steiner · 39th International Symposium on Computational Geometry (SoCG 2023) · arXiv:2303.00109 · doi:10.4230/LIPIcs.SoCG.2023.31

Constructed an 'exploding double chain' universal point set of size $2n-2$ for bipartite planar graphs and for planar graphs of maximum degree 3, the first linear-size universal point set for classes beyond outerplanar graphs.
 

 

 Reviewer notes. The $O(n)$ question for ALL planar graphs remains open; the best general bounds are $n^2/4 - \Theta(n)$ (upper) and $(1.293-o(1))n$ (lower). No 2024-2026 breakthroughs were found. The Cardinal et al. 2013 paper is also published as a book chapter (Springer) but the exact conference venue could not be confirmed from a fetched source, so arXiv is listed. The Bannister et al. 2014 JGAA DOI was not directly fetched and is therefore listed as null.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Question. Does there exist an $ n $ -universal set of size $ O(n) $ ?

Keywords:
geometric graph · planar graph · universal set

Discussion

More generally, if we let $ f(n) $ denote the size of the smallest $ n $ -universal set, we are interested in the behaviour of $ f $ . The best known upper bound is $ f(n) = O(n^2) $ . Indeed, every $ n $ -vertex planar graph can be drawn as required in the $ n \times n $ grid [dFPP], [S]. On the flip side, it is known that $ f(n) \ge 1.098n $ for sufficiently large $ n $ [CH].

Bibliography

 [CH]
 M. Chrobak and H.Karloff. A lower bound on the size of universal sets for planar graphs. SIGACT News, 20:83-86, 1989.

 [dFPP]
 H. de Fraysseix, J. Pach, and R. Pollack. How to draw a planar graph on a grid . Combinatorica, 10(1):41-51, 1990. MathSciNet
 How to draw a planar graph on a grid · MathSciNet

 [S]
 W. Schnyder. Embedding planar graphs on the grid. In Proc. 1st ACM-SIAM Sympos. Discrete Algorithms, pages 138-148, 1990.
