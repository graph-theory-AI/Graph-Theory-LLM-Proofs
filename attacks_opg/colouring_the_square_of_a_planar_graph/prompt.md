Attack the following open graph-theory problem.

Catalog id: colouring_the_square_of_a_planar_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/colouring_the_square_of_a_planar_graph/
Original entry: http://www.openproblemgarden.org/op/colouring_the_square_of_a_planar_graph
Problem attributed to: Wegner (posted 2013-03-13)

=== Problem statement (OpenProblemGarden) ===
Title: Colouring the square of a planar graph
Conjecture Let $ G $ be a planar graph of maximum degree $ \Delta $ . The chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ .

=== Discussion / context (OpenProblemGarden) ===
The square of a graph $ G $ is the graph $ G^2 $ on the same set of vertices, in which two vertices are adjacent when their distance in $ G $ is at most 2. Wegner [W] also gave examples showing that these bounds would be tight. For $ \Delta\geq 8 $ , they are the following. For $ 4\leq \Delta \leq 9 $ , the examples are planar graphs on $ \Delta+5 $ with maximum degree $ \Delta $ whose square is a complete graph. This conjecture has also been generalized to the list chromatic number . Conjecture Let $ G $ be a planar graph of maximum degree $ \Delta $ . The list chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ . Cranston and Kim [CK] showed that the square of every connected graph (non necessarily planar) which is subcubic (i.e., with $ \Delta\le3 $ ) is 8-choosable, except for the Petersen graph. However, the 7-choosability of the square of subcubic planar graphs is still open. Havet et al. [HHMR] proved the conjecture asymptotically: Theorem The square of every planar graph $ G $ of maximum degree $ \Delta $ has list chromatic number at most $ (1+o(1))\,\frac32\,\Delta $ . In fact, they proved this results for more general classes of graph. This led them to pose the following problem. Problem Is it true that for every minor-closed family $ {\cal F} $ of graphs (with $ {\cal F} $ not the set of all graphs), we have $ \chi(G^2)\le \bigl(\frac32+o(1)\bigr) \Delta(G) $ for all $ G\in{\cal F} $ ?

=== References listed by OpenProblemGarden ===
- [HHMR] F. Havet, J. van den Heuvel, C. McDiarmid, and B. Reed. List Colouring Squares of Planar Graphs. Research Report RR-6586, INRIA, July 2008.
- [CK] D. W. Cranston and S.-J. Kim. List-coloring the square of a subcubic graph, J. Graph Theory, 57(1):65--87, 2008.
- *[W] G. Wegner. Graphs with given diameter and a coloring problem. Technical report, 1977.

=== Catalog page (statement + literature review) ===
Colouring the square of a planar graph — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Significant partial progress has been made since the 2013 OPG posting. The $\Delta=3$ case of Wegner's conjecture ($\chi(G^2)\le 7$) has been fully proved — independently by Hartke, Jahanbekam, and Thomas (2016) and by Thomassen (2018). For larger $\Delta$ the conjecture remains open: improved general upper bounds such as $2\Delta+7$ (for $\Delta\ge 6$) and $3\Delta+4$ have been established, and the clique bound $\omega(G^2)\le\lfloor\frac{3}{2}\Delta\rfloor+1$ has been verified for $\Delta\ge 36$, but the full conjecture (all three cases) is still unresolved.

 Cited literature (8)

 
 
 
proof The chromatic number of the square of subcubic planar graphs
 (2016)
 

 
 Stephen G. Hartke, Sogol Jahanbekam, Brent Thomas · arXiv preprint · arXiv:1604.06504

Proves Wegner's conjecture for $\Delta=3$: the square of every subcubic planar graph is 7-colorable, using the discharging method and computational verification of reducible configurations.
 

 
 
proof The square of a planar cubic graph is 7-colorable
 (2018)
 

 
 Carsten Thomassen · Journal of Combinatorial Theory, Series B · doi:10.1016/j.jctb.2017.08.010

Independent proof of Wegner's conjecture for $\Delta=3$ (cubic planar graphs): $\chi(G^2)\le 7$; published in JCTB 128 (2018) 192–218.
 

 
 
partial Coloring squares of planar graphs with small maximum degree
 (2021)
 

 
 Mateusz Krzyżyński, Paweł Rzążewski, Szymon Tur · arXiv preprint · arXiv:2105.11235

Proves $\chi(G^2)\le 3\Delta+4$ for every planar graph $G$, giving the best-known bound for $6\le\Delta\le 14$.
 

 
 
partial Improved square coloring of planar graphs
 (2021)
 

 
 Nicolas Bousquet, Quentin Deschamps, Lucas de Meyer, Théo Pierron · arXiv preprint · arXiv:2112.12512

Shows that $2\Delta+7$ colors suffice to square-color any planar graph, improving the best-known bounds for $6\le\Delta\le 31$.
 

 
 
partial Relaxation of Wegner's Planar Graph Conjecture for maximum degree 4
 (2022)
 

 
 Eun-Kyung Cho, Ilkyoo Choi, Bernard Lidický · arXiv preprint · arXiv:2212.10643

Shows that a relaxation of $G^2$-coloring for planar $G$ with $\Delta=4$ is achievable with 9 colors (the conjectured bound), by allowing at most one repeated color in neighborhoods of degree-4 vertices.
 

 
 
partial The square of every subcubic planar graph of girth at least 6 is 7-choosable
 (2023)
 

 
 Seog-Jin Kim, Xiaopan Lian · arXiv preprint · arXiv:2305.05194

Proves the list-chromatic version of Wegner's conjecture ($\chi_\ell(G^2)\le 7$) for subcubic planar graphs of girth at least 6.
 

 
 
partial Bounding Clique Size in Squares of Planar Graphs
 (2023)
 

 
 Daniel W. Cranston · European Journal of Combinatorics · arXiv:2308.09585

Proves that $\omega(G^2)\le\lfloor\frac{3}{2}\Delta(G)\rfloor+1$ for plane graphs with $\Delta(G)\ge 36$, confirming the clique-number analogue of Wegner's conjecture for large degree.
 

 
 
partial Squares of subcubic planar graphs without cycles of length 4-8 are 6-choosable
 (2025)
 

 
 Seog-Jin Kim, Rong Luo · arXiv preprint · arXiv:2512.10175

Shows $\chi_\ell(G^2)\le 6$ for subcubic planar graphs containing no cycles of length 4 through 8, improving the 7-choosable bound under additional girth/cycle restrictions.
 

 

 Reviewer notes. The Thomassen 2018 paper (doi:10.1016/j.jctb.2017.08.010) was verified via Wikidata and DTU Orbit since ScienceDirect returned HTTP 403. The Hartke–Jahanbekam–Thomas paper (arXiv:1604.06504) appears to remain a preprint (not yet found in a peer-reviewed journal page that was accessible). The Δ=4 case of the original conjecture (χ(G²)≤9) remains open with best known upper bound of 12. The list-chromatic version of the conjecture for subcubic planar graphs (7-choosability without girth restriction) also remains open. The paper on Δ=5 square coloring (Graphs and Combinatorics 2023, doi:10.1007/s00373-023-02615-1) was found in search but could not be fetched due to authentication redirect and was therefore not included.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 166s.
 

Conjecture. Let $ G $ be a planar graph of maximum degree $ \Delta $ . The chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ .

Discussion

The square of a graph $ G $ is the graph $ G^2 $ on the same set of vertices, in which two vertices are adjacent when their distance in $ G $ is at most 2. Wegner [W] also gave examples showing that these bounds would be tight. For $ \Delta\geq 8 $ , they are the following. For $ 4\leq \Delta \leq 9 $ , the examples are planar graphs on $ \Delta+5 $ with maximum degree $ \Delta $ whose square is a complete graph. This conjecture has also been generalized to the list chromatic number . Conjecture Let $ G $ be a planar graph of maximum degree $ \Delta $ . The list chromatic number of its square is \item at most $ 7 $ if $ \Delta =3 $ , \item at most $ \Delta+5 $ if $ 4\leq\Delta\leq 7 $ , \item at most $ \left\lfloor\frac32\,\Delta\right\rfloor+1 $ if $ \Delta\ge8 $ . Cranston and Kim [CK] showed that the square of every connected graph (non necessarily planar) which is subcubic (i.e., with $ \Delta\le3 $ ) is 8-choosable, except for the Petersen graph. However, the 7-choosability of the square of subcubic planar graphs is still open. Havet et al. [HHMR] proved the conjecture asymptotically: Theorem The square of every planar graph $ G $ of maximum degree $ \Delta $ has list chromatic number at most $ (1+o(1))\,\frac32\,\Delta $ . In fact, they proved this results for more general classes of graph. This led them to pose the following problem. Problem Is it true that for every minor-closed family $ {\cal F} $ of graphs (with $ {\cal F} $ not the set of all graphs), we have $ \chi(G^2)\le \bigl(\frac32+o(1)\bigr) \Delta(G) $ for all $ G\in{\cal F} $ ?

Bibliography

 [HHMR]
 F. Havet, J. van den Heuvel, C. McDiarmid, and B. Reed. List Colouring Squares of Planar Graphs . Research Report RR-6586, INRIA, July 2008.
 List Colouring Squares of Planar Graphs

 [CK]
 D. W. Cranston and S.-J. Kim. List-coloring the square of a subcubic graph, J. Graph Theory, 57(1):65--87, 2008.

★ [W]
 G. Wegner. Graphs with given diameter and a coloring problem. Technical report, 1977.
