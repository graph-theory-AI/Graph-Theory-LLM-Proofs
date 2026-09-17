Attack the following open graph-theory problem.

Catalog id: vertex_minor_closed_classes_are_chi_bounded
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/vertex_minor_closed_classes_are_chi_bounded/
Original entry: http://www.openproblemgarden.org/op/vertex_minor_closed_classes_are_chi_bounded
Problem attributed to: Geelen, Jim (posted 2009-05-16)

=== Problem statement (OpenProblemGarden) ===
Title: Are vertex minor closed classes chi-bounded?
Question Is every proper vertex-minor closed class of graphs chi-bounded?

=== Discussion / context (OpenProblemGarden) ===
We say that a family of graphs $ {\mathcal F} $ is $ \chi $ - bounded if there is a function $ f : {\mathbb N} \rightarrow {\mathbb N} $ so that $ \chi(G) \le f( \omega(G)) $ for every $ G \in {\mathcal F} $ . If $ G $ is a simple graph, a vertex minor of $ G $ is any graph which can be obtained by a sequence of the following operations: \item delete a vertex \item choose a vertex $ v $ and complement the neighborhood of $ v $ (i.e. whenever $ u,w $ are neighbors of $ v $ , switch $ u,w $ between adjacent/non-adjacent). Dvorak and Kral [DK] showed that this conjecture is true for class of graphs of bounded rank-width, and the class of graphs having no vertex-minor isomorphic to the wheel $ W_5 $ on $ 6 $ vertices.

=== References listed by OpenProblemGarden ===
- [DK] Z. Dvorak and D. Král. Classes of graphs with small rank decompositions are χ-bounded. European J. Combin., 33(4):679–-683, 2012. MathSciNet

=== Catalog page (statement + literature review) ===
Are vertex minor closed classes chi-bounded? — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 James Davies proved Geelen's conjecture in full: every proper vertex-minor-closed class of graphs is $\chi$-bounded. The proof, posted to arXiv in August 2020 and published in Combinatorica (DOI: 10.1007/s00493-021-4767-3), was preceded by a 2019 partial result of Choi, Kwon, Oum, and Wollan establishing $\chi$-boundedness for graph classes excluding any fixed wheel vertex-minor.

 Cited literature (2)

 
 
 
partial Chi-boundedness of graph classes excluding wheel vertex-minors
 (2019)
 

 
 Hojin Choi, O-joung Kwon, Sang-il Oum, Paul Wollan · Journal of Combinatorial Theory, Series B · arXiv:1702.07851 · doi:10.1016/j.jctb.2018.08.009

Proves that any class of graphs excluding some fixed wheel graph $W_k$ as a vertex-minor is $\chi$-bounded, generalizing the Dvorak–Kral results on $W_5$ and circle graphs.
 

 
 
proof Vertex-minor-closed classes are χ-bounded
 (2022)
 

 
 James Davies · Combinatorica · arXiv:2008.05069 · doi:10.1007/s00493-021-4767-3

Proves Geelen's conjecture in full: every proper vertex-minor-closed class of graphs is $\chi$-bounded.
 

 

 Reviewer notes. The arXiv preprint (2008.05069) directly verifies the proof claim. Combinatorica's published-issues page verifies the journal version, pages 1049-1079, and DOI 10.1007/s00493-021-4767-3; the arXiv submission date is August 2020.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Question. Is every proper vertex-minor closed class of graphs chi-bounded?

Keywords:
chi-bounded · circle graph · coloring · vertex minor

Discussion

We say that a family of graphs $ {\mathcal F} $ is $ \chi $ - bounded if there is a function $ f : {\mathbb N} \rightarrow {\mathbb N} $ so that $ \chi(G) \le f( \omega(G)) $ for every $ G \in {\mathcal F} $ . If $ G $ is a simple graph, a vertex minor of $ G $ is any graph which can be obtained by a sequence of the following operations: \item delete a vertex \item choose a vertex $ v $ and complement the neighborhood of $ v $ (i.e. whenever $ u,w $ are neighbors of $ v $ , switch $ u,w $ between adjacent/non-adjacent). Dvorak and Kral [DK] showed that this conjecture is true for class of graphs of bounded rank-width, and the class of graphs having no vertex-minor isomorphic to the wheel $ W_5 $ on $ 6 $ vertices.

Bibliography

 [DK]
 Z. Dvorak and D. Král. Classes of graphs with small rank decompositions are χ-bounded. European J. Combin., 33(4):679–-683, 2012. MathSciNet
 MathSciNet
