Attack the following open graph-theory problem.

Catalog id: are_different_notions_of_the_crossing_number_the_same
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/are_different_notions_of_the_crossing_number_the_same/
Original entry: http://www.openproblemgarden.org/op/are_different_notions_of_the_crossing_number_the_same
Problem attributed to: Pach, János, Tóth, Géza (posted 2009-11-03)

=== Problem statement (OpenProblemGarden) ===
Title: Are different notions of the crossing number the same?
Problem Does the following equality hold for every graph $ G $ ? \[ \text{pair-cr}(G) = \text{cr}(G) \] The crossing number $ \text{cr}(G) $ of a graph $ G $ is the minimum number of edge crossings in any drawing of $ G $ in the plane. In the pairwise crossing number $ \text{pair-cr}(G) $ , we minimize the number of pairs of edges that cross.

=== Discussion / context (OpenProblemGarden) ===
Obviously we have $ \text{pair-cr}(G) \leq \text{cr}(G) $ . The problem was first posed by Pach and Tóth in~[PT], who first spotted the possibility that the pairwise crossing number might be different from the crossing number. They proved $ \text{cr}(G) \leq 2k^2 $ for graphs with pairwise crossing number $ k $ , which was later improved by Valtr~[V05] to $ O(k^2/ \log(k)) $ and by Tóth~[T08] to $ O(k^2/ \log^2(k)) $ .

=== References listed by OpenProblemGarden ===
- *[PT] János Pach, Géza Tóth, Which crossing number is it anyway?, Journal of Combinatorial Theory Series B 80 (2000), no. 2, 225--246. MathSciNet
- [V05] Pavel Valtr, On the pair-crossing number, Combinatorial and computational geometry, 52 (2005), 569--575. MathSciNet
- [T08] Géza Tóth, Note on the pair-crossing number and the odd-crossing number, Discrete Comput. Geom., 39 (2008), no. 4, 791--799. MathSciNet

=== Catalog page (statement + literature review) ===
Are different notions of the crossing number the same? — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The equality $\text{pair-cr}(G) = \text{cr}(G)$ remains open for general graphs. Significant partial progress has been made: the best known upper bound on $\text{cr}(G)$ in terms of $k = \text{pair-cr}(G)$ has improved from $O(k^2/\log^2 k)$ (Tóth, 2008) to $O(k^{3/2}\log k)$ (Karl–Tóth, 2021) and then to $O(k^{3/2})$ (Solé Pi, 2022), but no example with $\text{pair-cr}(G) < \text{cr}(G)$ has been found.

 Cited literature (3)

 
 
 
partial A slightly better bound on the crossing number in terms of the pair-crossing number
 (2021)
 

 
 János Karl, Géza Tóth · arXiv preprint · arXiv:2105.14319

Proves $\text{cr}(G) = O(\text{pcr}(G)^{3/2} \log \text{pcr}(G))$, improving the previously known bound of Matoušek by a logarithmic factor.
 

 
 
partial Pair crossing number, cutwidth, and good drawings on arbitrary point sets
 (2022)
 

 
 Oriol Solé Pi · Discrete & Computational Geometry · arXiv:2211.03322 · doi:10.1007/s00454-024-00708-z

Proves $\text{cr}(G) = O(\text{pcr}(G)^{3/2})$ for every graph $G$, removing the remaining logarithmic factor and giving the current best bound.
 

 
 
partial From Local Pair-Crossing Number to Local Crossing Number
 (2025)
 

 
 Jacob Fox, János Pach, Andrew Suk · Graph Drawing 2025 (LIPIcs) · doi:10.4230/LIPIcs.GD.2025.31

Resolves the local variant: if each edge crosses at most $k$ others in some drawing, then a redrawing exists where each edge participates in at most $k^3 + O(k^2)$ crossings, improving a prior exponential bound and answering a question of Ackerman–Schaefer.
 

 

 Reviewer notes. The Springer journal page for 10.1007/s00454-024-00708-z (Discrete & Computational Geometry, 2024 publication of Solé Pi's paper) required authentication and could not be directly fetched; the DOI is confirmed via search results cross-referencing arXiv:2211.03322. The Ackerman–Schaefer (2014) 'A Crossing Lemma for the Pair-Crossing Number' chapter (DOI 10.1007/978-3-662-45803-7_19) also required Springer authentication and could not be verified; it is therefore omitted from since_posted despite appearing in searches. Matoušek's bound (improved by Karl–Tóth 2021) appears to be unpublished or informal; no verifiable arXiv/journal paper by Matoušek on this specific bound was found. The Fox–Pach–Suk (2025) result addresses the local variant of the problem (local pair-crossing vs. local crossing number) rather than the global equality asked in the problem statement.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 1340s.
 

Problem. Does the following equality hold for every graph $ G $ ? \[ \text{pair-cr}(G) = \text{cr}(G) \]

Keywords:
crossing number · pair-crossing number

Discussion

Obviously we have $ \text{pair-cr}(G) \leq \text{cr}(G) $ . The problem was first posed by Pach and Tóth in~[PT], who first spotted the possibility that the pairwise crossing number might be different from the crossing number. They proved $ \text{cr}(G) \leq 2k^2 $ for graphs with pairwise crossing number $ k $ , which was later improved by Valtr~[V05] to $ O(k^2/ \log(k)) $ and by Tóth~[T08] to $ O(k^2/ \log^2(k)) $ .

Bibliography

★ [PT]
 János Pach, Géza Tóth, Which crossing number is it anyway? , Journal of Combinatorial Theory Series B 80 (2000), no. 2, 225--246. MathSciNet
 Which crossing number is it anyway? · MathSciNet

 [V05]
 Pavel Valtr, On the pair-crossing number , Combinatorial and computational geometry, 52 (2005), 569--575. MathSciNet
 On the pair-crossing number · MathSciNet

 [T08]
 Géza Tóth, Note on the pair-crossing number and the odd-crossing number , Discrete Comput. Geom., 39 (2008), no. 4, 791--799. MathSciNet
 Note on the pair-crossing number and the odd-crossing number · MathSciNet
