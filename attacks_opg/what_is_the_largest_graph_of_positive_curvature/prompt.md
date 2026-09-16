Attack the following open graph-theory problem.

Catalog id: what_is_the_largest_graph_of_positive_curvature
Source: OpenProblemGarden (importance: Low ✭)
Subject: Graph Theory » Topological Graph Theory » Planar graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/what_is_the_largest_graph_of_positive_curvature/
Original entry: http://www.openproblemgarden.org/op/what_is_the_largest_graph_of_positive_curvature
Problem attributed to: DeVos, Matt, Mohar, Bojan (posted 2007-03-10)

=== Problem statement (OpenProblemGarden) ===
Title: What is the largest graph of positive curvature?
Problem What is the largest connected planar graph of minimum degree 3 which has everywhere positive combinatorial curvature, but is not a prism or antiprism ?

=== Discussion / context (OpenProblemGarden) ===
Definition: For a graph $ G $ embedded in the sphere, the combinatorial curvature of a vertex $ v $ is defined to be $ 1 - \frac{ {\mathit deg}(v)}{2} + \sum_{f \sim v} \frac{1}{ {\mathit size}(f) } $ (here the summation is over all faces $ f $ incident with $ v $ ). Let $ G $ be a graph embedded in the sphere, and consider the polygonal surface formed by treating each face of size $ n $ as a regular $ n $ -gon of side length $ 1 $ . The gaussian curvature at a vertex $ v $ is defined to be $ 2 \pi $ minus the sum of the angles incident with $ v $ . So, our vertex $ v $ has positive curvature if the sum of the incident angles is less than $ 2 \pi $ . In fact, the combinatorial curvature at $ v $ is exactly $ 2 \pi $ times the gaussian curvature, so these quantities will always have the same sign. Let us call a convex polyhedron regular-faced if each face is a regular polygon. Based on the previous discussion, we know that every convex regular-faced polyhedron gives us a graph with everywhere positive combinatorial curvature. Indeed, we may view planar graphs with everywhere positive curvature as a kind of generalization of these polyhedra. The polyhedra in this class have been studied and classified. The Platonic solids and Archimedean solids are all convex and regular faced, and there are two infinite families: prisms and antiprisms . In addition to this, there are 92 other exceptional ones, known as Johnson Solids . Euler's formula tells us that the sum of the combinatorial curvatures over all of the vertices is equal to 2. Indeed, the combinatorial curvature is exactly what we get when we assign $ 1 $ to each vertex and face, $ -1 $ to each edge, and then "discharge" evenly onto the vertices. So, if we wish to construct large planar graphs where every vertex has positive curvature, we will need to make the curvature arbitrarily small. This can be achieved with prisms and antiprisms, but apart from these two families, all other graphs with everywhere positive curvature have a bounded number of vertices. Improving upon [DM], Zhang [Z] has shown this upper bound to be at most 580. The great rhombicosidodecahedron has 120 vertices and everywhere positive curvature (this is the largest regular-faced convex polyhedron which is not a prism or antiprism). Reti, Bitay, and Kosztolanyi [RBK] have improved upon this lower bound by constructing a graph with everywhere positive curvature and 138 vertices. These are the best bounds I (M. DeVos) know of.

=== References listed by OpenProblemGarden ===
- [DM] M. DeVos and B. Mohar, An analogue of the Descarte-Euler formula for infinite graphs and Higuchi's conjecture preprint.
- [H] Y. Higuchi, Combinatorial curvature for planar graph, J. Graph Theory, Vol 38 (2001), no. 4, 220-229. MathSciNet
- [RBK] T. Reti, E. Bitay, and Zs. Kosztolanyi, On the polyhedral graphs with positive combinatorial curvature, Acta Polytechnica Hungarica Vol. 2, No. 2 (2005) 19-37.
- [Z] L. Zhang, A result on combinatorial curvature for embedded graphs on a surface, Discrete Math (2007) in press

=== Catalog page (statement + literature review) ===
What is the largest graph of positive curvature? — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 The problem is completely resolved: the largest connected planar graph of minimum degree 3 with everywhere positive combinatorial curvature (and not a prism or antiprism) has exactly 208 vertices. The lower bound of 208 was first achieved by Nicholson and Sneddon (2011), while Ghidelli (arXiv 2017; JCTB 2023) proved the matching upper bound using a refined discharging technique, showing moreover that all faces have at most 41 sides.

 Cited literature (2)

 
 
 
proof On the largest planar graphs with everywhere positive combinatorial curvature (extended arxiv version)
 (2023)
 

 
 Luca Ghidelli · Journal of Combinatorial Theory, Series B · arXiv:1708.08502 · doi:10.1016/j.jctb.2022.08.009

Proves that every planar PCC graph has at most 208 vertices and every face has at most 41 sides; since examples with 208 vertices were already known (Nicholson–Sneddon 2011), this completely solves the problem.
 

 
 
partial Characterizing the polyhedral graphs with positive combinatorial curvature
 (2017)
 

 
 Paul Richard Oldridge · University of Victoria, MSc thesis

Constructs a PCC graph with 208 vertices (with two 39-faces), enumerates all 3-regular PCC graphs up to order 132, and proves conditionally (assuming no face larger than 122 edges) an upper bound of 244.
 

 

 Reviewer notes. Ghidelli's arXiv abstract directly defines planar PCC graphs as the exact class in the OPG problem (simple connected planar, positive combinatorial curvature, not a prism or antiprism, minimum degree at least 3) and proves the 208 upper bound. The ScienceDirect page verifies the journal version: J. Combin. Theory Ser. B 158, Part 2 (2023), pp. 226-263, DOI 10.1016/j.jctb.2022.08.009. Nicholson–Sneddon ('New Graphs with Thinly Spread Positive Combinatorial Curvature', New Zealand J. Math. 41 (2011), pp. 39-43) established the 208-vertex lower bound; this is explicitly referenced in Ghidelli's verified source and visible in ResearchGate search snippets, but the paper itself was not directly fetched, so it is not included as a since_posted citation. The Mohar problem page (sfu.ca) appeared outdated relative to the arXiv/JCTB result.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Problem. What is the largest connected planar graph of minimum degree 3 which has everywhere positive combinatorial curvature, but is not a prism or antiprism ?

Keywords:
curvature · planar graph

Discussion

Definition: For a graph $ G $ embedded in the sphere, the combinatorial curvature of a vertex $ v $ is defined to be $ 1 - \frac{ {\mathit deg}(v)}{2} + \sum_{f \sim v} \frac{1}{ {\mathit size}(f) } $ (here the summation is over all faces $ f $ incident with $ v $ ). Let $ G $ be a graph embedded in the sphere, and consider the polygonal surface formed by treating each face of size $ n $ as a regular $ n $ -gon of side length $ 1 $ . The gaussian curvature at a vertex $ v $ is defined to be $ 2 \pi $ minus the sum of the angles incident with $ v $ . So, our vertex $ v $ has positive curvature if the sum of the incident angles is less than $ 2 \pi $ . In fact, the combinatorial curvature at $ v $ is exactly $ 2 \pi $ times the gaussian curvature, so these quantities will always have the same sign. Let us call a convex polyhedron regular-faced if each face is a regular polygon. Based on the previous discussion, we know that every convex regular-faced polyhedron gives us a graph with everywhere positive combinatorial curvature. Indeed, we may view planar graphs with everywhere positive curvature as a kind of generalization of these polyhedra. The polyhedra in this class have been studied and classified. The Platonic solids and Archimedean solids are all convex and regular faced, and there are two infinite families: prisms and antiprisms . In addition to this, there are 92 other exceptional ones, known as Johnson Solids . Euler's formula tells us that the sum of the combinatorial curvatures over all of the vertices is equal to 2. Indeed, the combinatorial curvature is exactly what we get when we assign $ 1 $ to each vertex and face, $ -1 $ to each edge, and then "discharge" evenly onto the vertices. So, if we wish to construct large planar graphs where every vertex has positive curvature, we will need to make the curvature arbitrarily small. This can be achieved with prisms and antiprisms, but apart from these two families, all other graphs with everywhere positive curvature have a bounded number of vertices. Improving upon [DM], Zhang [Z] has shown this upper bound to be at most 580. The great rhombicosidodecahedron has 120 vertices and everywhere positive curvature (this is the largest regular-faced convex polyhedron which is not a prism or antiprism). Reti, Bitay, and Kosztolanyi [RBK] have improved upon this lower bound by constructing a graph with everywhere positive curvature and 138 vertices. These are the best bounds I (M. DeVos) know of.

Bibliography

 [DM]
 M. DeVos and B. Mohar, An analogue of the Descarte-Euler formula for infinite graphs and Higuchi's conjecture preprint.
 An analogue of the Descarte-Euler formula for infinite graphs and Higuchi's conjecture

 [H]
 Y. Higuchi, Combinatorial curvature for planar graph, J. Graph Theory, Vol 38 (2001), no. 4, 220-229. MathSciNet
 MathSciNet

 [RBK]
 T. Reti, E. Bitay, and Zs. Kosztolanyi, On the polyhedral graphs with positive combinatorial curvature , Acta Polytechnica Hungarica Vol. 2, No. 2 (2005) 19-37.
 On the polyhedral graphs with positive combinatorial curvature

 [Z]
 L. Zhang, A result on combinatorial curvature for embedded graphs on a surface, Discrete Math (2007) in press
