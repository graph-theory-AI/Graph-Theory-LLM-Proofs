Attack the following open graph-theory problem.

Catalog id: obstacle_number_of_planar_graphs
Source: OpenProblemGarden (importance: Low ✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/obstacle_number_of_planar_graphs/
Original entry: http://www.openproblemgarden.org/op/obstacle_number_of_planar_graphs
Problem attributed to: Alpert, Hanna, Koch, Christina, Laison, Joshua D. (posted 2011-11-23)

=== Problem statement (OpenProblemGarden) ===
Title: Obstacle number of planar graphs
Does there exist a planar graph with obstacle number greater than 1? Is there some $ k $ such that every planar graph has obstacle number at most $ k $ ?

=== Discussion / context (OpenProblemGarden) ===
A $ k $ -obstacle drawing of a graph $ G $ is a mapping of the vertices of $ G $ to points in the plane, along with a set of polygonal obstacles $ P_1,\ldots, P_k $ , such that two vertices are adjacent precisely if the line segment connecting their corresponding points in $ \mathbb R^2 $ does not intersect any obstacle. The {\em obstacle number} of a graph $ G $ is the minimum $ k $ such that $ G $ has a $ k $ -obstacle drawing. This invariant was recently introduced by Alpert, Koch, and Laison [AKL], who proved that every outerplanar graph has obstacle number 1. The next question, then, follows naturally: what is the obstacle number of a planar graph? So far no planar graph has been proved to have obstacle number greater than 1. Alpert, Koch, and Laison specifically ask what the obstacle numbers of the icosahedron and dodecahedron are [AKL].

=== References listed by OpenProblemGarden ===
- [AKL] Hannah Alpert, Christina Koch, and Joshua D. Laison: Obstacle numbers of graphs. Discrete Comput. Geom. (2010) 44:223-244.

=== Catalog page (statement + literature review) ===
Obstacle number of planar graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The first part of the problem has been resolved: Berman, Chappell, Faudree, Gimbel, Hartman, and Williams proved that the icosahedron has obstacle number 2, showing that planar graphs can indeed have obstacle number greater than 1. However, the second question — whether there exists a constant $k$ such that every planar graph has obstacle number at most $k$ — remains open; the best known upper bound for an $n$-vertex planar graph is $O(n)$.

 Cited literature (3)

 
 
 
partial Graphs with Obstacle Number Greater than One
 (2017)
 

 
 Leah Wrenn Berman, Glenn G. Chappell, Jill R. Faudree, John Gimbel, Chris Hartman, Gordon I. Williams · Journal of Graph Algorithms and Applications · arXiv:1606.03782

Proves that the icosahedron has obstacle number exactly 2 (using a SAT-solver-assisted proof), answering the question of Alpert, Koch, and Laison and showing that planar graphs are not all representable with a single obstacle; also shows the gyroelongated 4-bipyramid (order 10) has obstacle number 2.
 

 
 
partial Obstacle Numbers of Planar Graphs
 (2017)
 

 
 John Gimbel, Patrice Ossona de Mendez, Pavel Valtr · arXiv preprint · arXiv:1706.06992

Establishes that the maximum planar obstacle number (non-crossing visibility representation) of an $n$-vertex planar graph is $n-3$, and proves that every bipartite planar graph of order at least 3 has (standard) obstacle number 1.
 

 
 
partial Bounding and Computing Obstacle Numbers of Graphs
 (2024)
 

 
 Martin Balko, Steven Chaplick, Robert Ganian, Siddharth Gupta, Michael Hoffmann, Pavel Valtr, Alexander Wolff · SIAM Journal on Discrete Mathematics · arXiv:2206.15414 · doi:10.1137/23M1585088

Improves general lower bounds on obstacle number (to $\Omega(n/\log\log n)$ for simple polygon obstacles and $\Omega(n)$ for convex obstacles) and shows FPT algorithms for obstacle number parameterized by vertex cover, but no new constant bound for planar graphs.
 

 

 Reviewer notes. The two-part problem is partially resolved: the first question (existence of a planar graph with obstacle number > 1) was answered affirmatively by Berman et al. 2017 via computer-assisted proof. The second question (existence of a universal constant bound k for all planar graphs) remains fully open as of 2026; the patmorin survey page notes it is 'plausible that planar graphs have bounded obstacle number' but no proof exists. The Gimbel et al. paper (1706.06992) mainly studies the planar obstacle number variant (non-crossing drawings), which is a different (and harder) variant; its n-3 upper bound does not directly answer the constant-bound question for standard obstacle numbers. The Springer chapter version of the Gimbel paper (WG 2017 proceedings) could not be fetched due to authentication redirect.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Does there exist a planar graph with obstacle number greater than 1? Is there some $ k $ such that every planar graph has obstacle number at most $ k $ ?

Keywords:
graph drawing · obstacle number · planar graph · visibility graph

Discussion

A $ k $ -obstacle drawing of a graph $ G $ is a mapping of the vertices of $ G $ to points in the plane, along with a set of polygonal obstacles $ P_1,\ldots, P_k $ , such that two vertices are adjacent precisely if the line segment connecting their corresponding points in $ \mathbb R^2 $ does not intersect any obstacle. The {\em obstacle number} of a graph $ G $ is the minimum $ k $ such that $ G $ has a $ k $ -obstacle drawing. This invariant was recently introduced by Alpert, Koch, and Laison [AKL], who proved that every outerplanar graph has obstacle number 1. The next question, then, follows naturally: what is the obstacle number of a planar graph? So far no planar graph has been proved to have obstacle number greater than 1. Alpert, Koch, and Laison specifically ask what the obstacle numbers of the icosahedron and dodecahedron are [AKL].

Bibliography

 [AKL]
 Hannah Alpert, Christina Koch, and Joshua D. Laison: Obstacle numbers of graphs. Discrete Comput. Geom. (2010) 44:223-244.
