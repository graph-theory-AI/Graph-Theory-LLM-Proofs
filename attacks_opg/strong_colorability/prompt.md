Attack the following open graph-theory problem.

Catalog id: strong_colorability
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/strong_colorability/
Original entry: http://www.openproblemgarden.org/op/strong_colorability
Problem attributed to: Aharoni, Ron, Alon, Noga, Haxell, Penny E. (posted 2007-03-27)

=== Problem statement (OpenProblemGarden) ===
Title: Strong colorability
Let $ r $ be a positive integer. We say that a graph $ G $ is strongly $ r $ -colorable if for every partition of the vertices to sets of size at most $ r $ there is a proper $ r $ -coloring of $ G $ in which the vertices in each set of the partition have distinct colors. Conjecture If $ \Delta $ is the maximal degree of a graph $ G $ , then $ G $ is strongly $ 2 \Delta $ -colorable.

=== Discussion / context (OpenProblemGarden) ===
Haxell proved that if $ \Delta $ is the maximal degree of a graph $ G $ , then $ G $ is strongly $ 3 \Delta - 1 $ -colorable. She later proved that the strong chromatic number $ \chi_S $ is at most $ (2.75+\epsilon)\Delta $ for sufficiently large $ \Delta $ depending on $ \epsilon $ . Aharoni, Berger, and Ziv proved the fractional relaxation.

=== Catalog page (statement + literature review) ===
Strong colorability — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture $\chi_S(G) \leq 2\Delta$ remains open in general. Lo and Sanhueza-Matamala (2019) significantly improved the dense-graph regime, proving $\chi_S(G) \leq (2+o(1))\Delta(G)$ for every graph satisfying $\Delta(G) \geq cn$ for a constant $c > 0$, surpassing Haxell's $(2.75+\epsilon)\Delta$ bound. Additionally, the conjecture has been verified for several subfamilies of 2-regular graphs by McDonald and Puleo (2022), but the full conjecture for all graphs and all $\Delta$ remains open.

 Cited literature (2)

 
 
 
partial An asymptotic bound for the strong chromatic number
 (2019)
 

 
 Allan Lo, Nicolás Sanhueza-Matamala · Combinatorics, Probability and Computing · arXiv:1711.08214

Proves $\chi_S(G) \leq (2+o(1))\Delta(G)$ for every $c>0$ and every graph $G$ on $n$ vertices with $\Delta(G) \geq cn$, improving Haxell's $(2.75+\epsilon)\Delta$ bound in the dense regime; the bound is asymptotically best possible.
 

 
 
partial Strong coloring 2-regular graphs: Cycle restrictions and partial colorings
 (2022)
 

 
 Jessica McDonald, Gregory J. Puleo · Journal of Graph Theory · arXiv:2001.05051

Verifies the strong coloring conjecture ($\chi_S \leq 4 = 2\Delta$) for 2-regular graphs containing at most one odd cycle of length exceeding 3, or at most 3 triangles.
 

 

 Reviewer notes. The Lo-Sanhueza-Matamala result is a major improvement but requires Delta linear in n (dense graphs). For sparse graphs and small constant Delta >= 2, the 2*Delta bound remains unproven in general; the case Delta=2 in particular is still open except for special subfamilies. The Graf-Harris-Haxell 2021 paper (arXiv:1907.00033) gives algorithms for strong colouring but its exact contribution to the bound was not confirmed from the abstract alone and was not cited. No post-2022 paper improving the bound was found within the 4-query budget.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. If $ \Delta $ is the maximal degree of a graph $ G $ , then $ G $ is strongly $ 2 \Delta $ -colorable.

Keywords:
strong coloring

Discussion

Haxell proved that if $ \Delta $ is the maximal degree of a graph $ G $ , then $ G $ is strongly $ 3 \Delta - 1 $ -colorable. She later proved that the strong chromatic number $ \chi_S $ is at most $ (2.75+\epsilon)\Delta $ for sufficiently large $ \Delta $ depending on $ \epsilon $ . Aharoni, Berger, and Ziv proved the fractional relaxation.
