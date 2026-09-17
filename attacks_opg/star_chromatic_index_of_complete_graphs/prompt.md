Attack the following open graph-theory problem.

Catalog id: star_chromatic_index_of_complete_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/star_chromatic_index_of_complete_graphs/
Original entry: http://www.openproblemgarden.org/op/star_chromatic_index_of_complete_graphs
Problem attributed to: Dvorak, Zdenek, Mohar, Bojan, Samal, Robert (posted 2010-11-16)

=== Problem statement (OpenProblemGarden) ===
Title: Star chromatic index of complete graphs
Conjecture Is it possible to color edges of the complete graph $ K_n $ using $ O(n) $ colors, so that the coloring is proper and no 4-cycle and no 4-edge path is using only two colors? Equivalently: is the star chromatic index of $ K_n $ linear in $ n $ ?

=== Discussion / context (OpenProblemGarden) ===
The star chromatic index $ \chi_s'(G) $ of a graph $ G $ is the minimum number of colors needed to properly color the edges of $ G $ so that no path or cycle of length four is bi-colored. An equivalent definition is that $ \chi_s'(G) $ is the star chromatic number of the line graph $ L(G) $ . Dvořák, Mohar, and Šámal [DMS] show that $ \chi_s'(G) \ge (2+o(1))n $ . On the other hand, the best known upper bound (also in \cite{DMS]) is superlinear: $$ \chi_s'(K_n) \le n \cdot \frac{ 2^{ 2\sqrt2(1+o(1)) \sqrt{\log n} } }{(\log n)^{1/4}} \,. $$ It may be possible to decrease the upper bound by elementary methods.

=== References listed by OpenProblemGarden ===
- *[DMS] Dvořák, Zdeněk; Mohar, Bojan; Šámal, Robert: Star chromatic index, arXiv:1011.3376.

=== Catalog page (statement + literature review) ===
Star chromatic index of complete graphs — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The question of whether $\chi_s'(K_n) = O(n)$ remains open. The bounds established by Dvořák, Mohar, and Šámal in the original paper — a lower bound of $(2+o(1))n$ and a superlinear upper bound of $n \cdot 2^{2\sqrt{2}(1+o(1))\sqrt{\log n}}/(\log n)^{1/4}$ — still represent the state of the art. Multiple searches and the 2020 survey on star edge-coloring confirm that no resolution of the complete graph case has appeared in the literature.

 Reviewer notes. The survey arXiv:2009.08017 (Lei and Shi, 2020) on star edge-coloring was verified to exist but its PDF was not machine-readable; its abstract confirms it collects open problems in the area, suggesting the complete graph linearity question remains open. No citing paper found via four search rounds provided evidence of resolution. Research since 2010 has focused on specific graph classes (sparse graphs, subcubic, planar, multipartite) rather than on the complete graph linearity question.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Is it possible to color edges of the complete graph $ K_n $ using $ O(n) $ colors, so that the coloring is proper and no 4-cycle and no 4-edge path is using only two colors? Equivalently: is the star chromatic index of $ K_n $ linear in $ n $ ?

Keywords:
complete graph · edge coloring · star coloring

Discussion

The star chromatic index $ \chi_s'(G) $ of a graph $ G $ is the minimum number of colors needed to properly color the edges of $ G $ so that no path or cycle of length four is bi-colored. An equivalent definition is that $ \chi_s'(G) $ is the star chromatic number of the line graph $ L(G) $ . Dvořák, Mohar, and Šámal [DMS] show that $ \chi_s'(G) \ge (2+o(1))n $ . On the other hand, the best known upper bound (also in \cite{DMS]) is superlinear: $$ \chi_s'(K_n) \le n \cdot \frac{ 2^{ 2\sqrt2(1+o(1)) \sqrt{\log n} } }{(\log n)^{1/4}} \,. $$ It may be possible to decrease the upper bound by elementary methods.

Bibliography

★ [DMS]
 Dvořák, Zdeněk; Mohar, Bojan; Šámal, Robert: Star chromatic index, arXiv:1011.3376 .
 arXiv:1011.3376
