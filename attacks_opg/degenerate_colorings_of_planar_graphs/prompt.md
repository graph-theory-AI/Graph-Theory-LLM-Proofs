Attack the following open graph-theory problem.

Catalog id: degenerate_colorings_of_planar_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Topological Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/degenerate_colorings_of_planar_graphs/
Original entry: http://www.openproblemgarden.org/op/degenerate_colorings_of_planar_graphs
Problem attributed to: Borodin, Oleg V. (posted 2008-05-21)

=== Problem statement (OpenProblemGarden) ===
Title: Degenerate colorings of planar graphs
A graph $ G $ is $ k $ - degenerate if every subgraph of $ G $ has a vertex of degree $ \le k $ . Conjecture Every simple planar graph has a 5-coloring so that for $ 1 \le k \le 4 $ , the union of any $ k $ color classes induces a $ (k-1) $ -degenerate graph.

=== Discussion / context (OpenProblemGarden) ===
An acyclic coloring of a graph $ G $ is a proper coloring with the added property that the union of any two color classes induces a forest. Grunbaum famously conjectured that every simple planar graph has an acyclic 5-coloring. Following a sequence of partial results, Borodin [B] resolved this conjecture with an impressive and detailed argument. In the same paper, Borodin made the above conjecture, which, if true, would give a stronger result (as forests are precisely the 1-degenerate graphs). A degenerate coloring of a graph $ G $ is a proper coloring with the added property that the union of any $ k $ color classes induces a $ (k-1) $ -degenerate graph. A planar graph of minimum degree 5 cannot have a degenerate 5-coloring, but if the above conjecture holds, something just short of this is true. Rautenbach [R] proved that every planar graph has a degenerate 18-coloring, and recently, Mohar, Spacepan, and Zhu showed that every planar graph has a degenerate 9-coloring.

=== References listed by OpenProblemGarden ===
- *[B] O. V. Borodin, A proof of B. Grünbaum's conjecture on the acyclic -colorability of planar graphs. Dokl. Akad. Nauk SSSR 231 (1976), no. 1, 18--20. MathSciNet
- [R] D. Rautenbach, A conjecture of Borodin and a coloring of Grünbaum. Fifth Cracow Conference on Graph Theory USTRON '06, 187--194 Electron. Notes Discrete Math., 24, Elsevier, Amsterdam, 2006.

=== Catalog page (statement + literature review) ===
Degenerate colorings of planar graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Borodin's conjecture that every planar graph has a degenerate 5-coloring remains open. The most significant post-2008 progress is the formal proof by Kierstead, Mohar, Spacapan, Yang, and Zhu (2009) that the two-coloring number of any planar graph is at most 8, from which it follows that the degenerate list chromatic number of every planar graph is at most 9. No further improvement to this bound or resolution of the conjecture has been found in the literature through 2025.

 Cited literature (1)

 
 
 
partial The Two-Coloring Number and Degenerate Colorings of Planar Graphs
 (2009)
 

 
 Hal Kierstead, Bojan Mohar, Simon Spacapan, Daquing Yang, Xuding Zhu · SIAM Journal on Discrete Mathematics · doi:10.1137/070703697

Proved that the two-coloring number of every planar graph is at most 8, implying the degenerate list chromatic number of every planar graph is at most 9 (volume 23, pages 1548–1560).
 

 

 Reviewer notes. The degenerate 9-coloring result is already referenced in the OPG discussion text (attributed to 'Mohar, Spacepan, and Zhu'), so the result was likely known as a preprint before the 2008-05-21 posting; the formal SIAM paper (with Kierstead and Yang as additional co-authors) was published in 2009. The SIAM DOI URL returned HTTP 403; the paper was confirmed via Bojan Mohar's own bibliography page. The 2001 Thomassen result (decomposing any planar graph into an independent set and a 3-degenerate graph, J. Combin. Theory B 83:262–271) predates the posting. Subsequent papers on 'weak degeneracy' of planar graphs (2023–2025) address Thomassen-type list-coloring results, not Borodin's degenerate coloring conjecture directly. A 2021 blog post by Gil Kalai confirmed the conjecture was still open and expressed uncertainty about the current color-count record, consistent with no progress beyond 9 since 2009.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. Every simple planar graph has a 5-coloring so that for $ 1 \le k \le 4 $ , the union of any $ k $ color classes induces a $ (k-1) $ -degenerate graph.

Keywords:
coloring · degenerate · planar

Discussion

An acyclic coloring of a graph $ G $ is a proper coloring with the added property that the union of any two color classes induces a forest. Grunbaum famously conjectured that every simple planar graph has an acyclic 5-coloring. Following a sequence of partial results, Borodin [B] resolved this conjecture with an impressive and detailed argument. In the same paper, Borodin made the above conjecture, which, if true, would give a stronger result (as forests are precisely the 1-degenerate graphs). A degenerate coloring of a graph $ G $ is a proper coloring with the added property that the union of any $ k $ color classes induces a $ (k-1) $ -degenerate graph. A planar graph of minimum degree 5 cannot have a degenerate 5-coloring, but if the above conjecture holds, something just short of this is true. Rautenbach [R] proved that every planar graph has a degenerate 18-coloring, and recently, Mohar, Spacepan, and Zhu showed that every planar graph has a degenerate 9-coloring.

Bibliography

★ [B]
 O. V. Borodin, A proof of B. Grünbaum's conjecture on the acyclic $ 5 $ -colorability of planar graphs. Dokl. Akad. Nauk SSSR 231 (1976), no. 1, 18--20. MathSciNet
 MathSciNet

 [R]
 D. Rautenbach, A conjecture of Borodin and a coloring of Grünbaum. Fifth Cracow Conference on Graph Theory USTRON '06, 187--194 Electron. Notes Discrete Math., 24, Elsevier, Amsterdam, 2006.
