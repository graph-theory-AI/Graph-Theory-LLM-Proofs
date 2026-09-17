Attack the following open graph-theory problem.

Catalog id: coloring_the_odd_distance_graph
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/coloring_the_odd_distance_graph/
Original entry: http://www.openproblemgarden.org/op/coloring_the_odd_distance_graph
Problem attributed to: Rosenfeld, Moshe (posted 2007-10-03)

=== Problem statement (OpenProblemGarden) ===
Title: Coloring the Odd Distance Graph
The Odd Distance Graph , denoted $ {\mathcal O} $ , is the graph with vertex set $ {\mathbb R}^2 $ and two points adjacent if the distance between them is an odd integer. Question Is $ \chi({\mathcal O}) = \infty $ ?

=== Discussion / context (OpenProblemGarden) ===
This question is a relative of the famous problem about coloring the Unit Distance Graph (the graph on $ {\mathbb R}^2 $ where two points are adjacent if the distance between them is 1). See Moshe's online lecture Famous and lesser known problems in “elementary” combinatorial geometry and number theory at time 15:20 for a nice introduction. Perhaps the first property of $ {\mathcal O} $ to determine is the size of the largest complete subgraph (were $ {\mathcal O} $ to contain arbitrarily large complete subgraphs, its chromatic number would be $ \infty $ ). It is obvious that $ {\mathcal O} $ contains triangles, but perhaps surprisingly, it does not contain a complete subgraph on four vertices. In other words, there do not exist four points in $ {\mathbb R}^2 $ so that all pairwise distances are odd. This was a problem on the Putnam Exam in 1993, and is proved by Rosenfeld in [R1] and [R2]. A natural strengthening of the above question is to ask if there exists a proper $ n $ -coloring $ f: V({\mathcal O}) \rightarrow \{1,2,\ldots,n\} $ so that $ f^{-1}(\{i\}) $ is a measurable set for every $ i $ . Such colorings are called measurable colorings , and interestingly, the Odd Distance Graph has no finite measurable coloring. This follows from immediately from a theorem of Furstenberg, Katznelson and Weiss [FKW] which asserts that for every measurable subset $ A \subseteq {\mathbb R}^2 $ with positive upper density, there exists a number $ r $ so that $ A $ contains a pair of points at distance $ r' $ for every $ r' > r $ . This theorem has a number of independent proofs, see also Falconer and Marstrand [FM], Bourgain [Bo], and Bukh [Bu]. All that seems to be known about the (usual) chromatic number of $ {\mathcal O} $ is that $ \chi({\mathcal O}) \ge 5 $ .

=== References listed by OpenProblemGarden ===
- [Bo] J. Bourgain, A Szemerédi type theorem for sets of positive density in . Israel J. Math. 54 (1986), no. 3, 307--316. MathSciNet
- [Bu] B. Bukh, Measurable sets with excluded distances.
- [FM] K. J. Falconer and J. M. Marstrand, Plane sets with positive density at infinity contain all large distances. Bull. London Math. Soc. 18 (1986), no. 5, 471--474. MathSciNet
- [FKM] H. Furstenberg, Y. Katznelson, and B. Weiss, Ergodic theory and configurations in sets of positive density. Mathematics of Ramsey theory, 184--198, Algorithms Combin., 5, Springer, Berlin, 1990. MathSciNet
- [R1] M. Rosenfeld, Odd integral distances among points in the plane. Geombinatorics 5 (1996), no. 4, 156--159. MathSciNet
- [R2] M. Rosenfeld Famous and lesser known problems in “elementary” combinatorial geometry and number theory (video lecture - time 15:20)

=== Catalog page (statement + literature review) ===
Coloring the Odd Distance Graph — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 James Davies proved in 2022 that every finite colouring of the plane contains a monochromatic pair of points at an odd distance, which directly implies $\chi(\mathcal{O}) = \infty$ and resolves the problem affirmatively. The result was published in Geometric and Functional Analysis in 2024 and subsequently extended by Davies, McCarty, and Pilipczuk to prime and polynomial integer distances.

 Cited literature (3)

 
 
 
partial On Coloring the Odd-Distance Graph
 (2009)
 

 
 Jacob Steinhardt · arXiv preprint · arXiv:0908.1452

Provides a spectral-method proof that the odd-distance graph admits no finite measurable coloring, giving an alternative to the Furstenberg–Katznelson–Weiss ergodic-theory argument already cited in the problem statement.
 

 
 
proof Odd distances in colourings of the plane
 (2024)
 

 
 James Davies · Geometric and Functional Analysis · arXiv:2209.15598 · doi:10.1007/s00039-024-00659-w

Proves that every finite colouring of the plane contains a monochromatic pair of points at an odd (integer) distance, establishing $\chi(\mathcal{O}) = \infty$ and solving the problem.
 

 
 
partial Prime and polynomial distances in colourings of the plane
 (2025)
 

 
 James Davies, Rose McCarty, Michał Pilipczuk · Israel Journal of Mathematics · arXiv:2308.02483 · doi:10.1007/s11856-025-2857-4

Extends Davies's odd-distance result: every finite colouring of the plane contains a monochromatic pair at prime distance, and at distance $f(n)$ for any non-constant polynomial $f$ with positive leading integer coefficient.
 

 

 Reviewer notes. The Springer GAFA page for Davies is now directly verified: Geometric and Functional Analysis 34 (2024), 19-31, DOI 10.1007/s00039-024-00659-w. The Davies-McCarty-Pilipczuk extension is now published open access in Israel Journal of Mathematics (published 30 November 2025), DOI 10.1007/s11856-025-2857-4. The Steinhardt 2009 paper concerns measurable colorings only; the ordinary chromatic number lower bound $\chi(\mathcal{O}) \geq 5$ (attributed to Ardal, Maňuch, Rosenfeld, Shelah, and Stacho, ~2009) was not tracked to a verifiable arXiv or journal URL within the search budget and so is not included in since_posted.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 186s.
 

Question. Is $ \chi({\mathcal O}) = \infty $ ?

Keywords:
coloring · geometric graph · odd distance

Discussion

This question is a relative of the famous problem about coloring the Unit Distance Graph (the graph on $ {\mathbb R}^2 $ where two points are adjacent if the distance between them is 1). See Moshe's online lecture Famous and lesser known problems in “elementary” combinatorial geometry and number theory at time 15:20 for a nice introduction. Perhaps the first property of $ {\mathcal O} $ to determine is the size of the largest complete subgraph (were $ {\mathcal O} $ to contain arbitrarily large complete subgraphs, its chromatic number would be $ \infty $ ). It is obvious that $ {\mathcal O} $ contains triangles, but perhaps surprisingly, it does not contain a complete subgraph on four vertices. In other words, there do not exist four points in $ {\mathbb R}^2 $ so that all pairwise distances are odd. This was a problem on the Putnam Exam in 1993, and is proved by Rosenfeld in [R1] and [R2]. A natural strengthening of the above question is to ask if there exists a proper $ n $ -coloring $ f: V({\mathcal O}) \rightarrow \{1,2,\ldots,n\} $ so that $ f^{-1}(\{i\}) $ is a measurable set for every $ i $ . Such colorings are called measurable colorings , and interestingly, the Odd Distance Graph has no finite measurable coloring. This follows from immediately from a theorem of Furstenberg, Katznelson and Weiss [FKW] which asserts that for every measurable subset $ A \subseteq {\mathbb R}^2 $ with positive upper density, there exists a number $ r $ so that $ A $ contains a pair of points at distance $ r' $ for every $ r' > r $ . This theorem has a number of independent proofs, see also Falconer and Marstrand [FM], Bourgain [Bo], and Bukh [Bu]. All that seems to be known about the (usual) chromatic number of $ {\mathcal O} $ is that $ \chi({\mathcal O}) \ge 5 $ .

Bibliography

 [Bo]
 J. Bourgain, A Szemerédi type theorem for sets of positive density in $ R\sp k $ . Israel J. Math. 54 (1986), no. 3, 307--316. MathSciNet
 MathSciNet

 [Bu]
 B. Bukh, Measurable sets with excluded distances .
 Measurable sets with excluded distances

 [FM]
 K. J. Falconer and J. M. Marstrand, Plane sets with positive density at infinity contain all large distances. Bull. London Math. Soc. 18 (1986), no. 5, 471--474. MathSciNet
 MathSciNet

 [FKM]
 H. Furstenberg, Y. Katznelson, and B. Weiss, Ergodic theory and configurations in sets of positive density. Mathematics of Ramsey theory, 184--198, Algorithms Combin., 5, Springer, Berlin, 1990. MathSciNet
 MathSciNet

 [R1]
 M. Rosenfeld, Odd integral distances among points in the plane. Geombinatorics 5 (1996), no. 4, 156--159. MathSciNet
 MathSciNet

 [R2]
 M. Rosenfeld Famous and lesser known problems in “elementary” combinatorial geometry and number theory (video lecture - time 15:20)
 Famous and lesser known problems in “elementary” combinatorial geometry and number theory
