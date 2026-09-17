Attack the following open graph-theory problem.

Catalog id: triangle_packing_vs_triangle_edge_transversal
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/triangle_packing_vs_triangle_edge_transversal/
Original entry: http://www.openproblemgarden.org/op/triangle_packing_vs_triangle_edge_transversal
Problem attributed to: Tuza, Zsolt (posted 2013-03-06)

=== Problem statement (OpenProblemGarden) ===
Title: Triangle-packing vs triangle edge-transversal.
Conjecture If $ G $ has at most $ k $ edge-disjoint triangles, then there is a set of $ 2k $ edges whose deletion destroys every triangle.

=== Discussion / context (OpenProblemGarden) ===
This conjecture may be rephrased in terms of packing and edge-transversal. A triangle packing is a set of pairwise edge-disjoint triangles. A triangle edge-tranversal is a set of edges meeting all triangles. Denote the maximum size of a triangle packing in $ G $ by $ \nu(G) $ and the minimum size of a triangle edge-transversal of $ G $ by $ \tau(G) $ . Clearly $ \nu(G) \leq \tau(G) $ . The conjecture translates in $ \tau(G)\leq 2\nu(G) $ . This conjecture, if true, is best possible as can be seen by taking, say $ G=K_4 $ or $ G=K_5 $ . Trivially, $ \tau(G)\leq 3\nu(G) $ , since the set of edges of a maximum triangle packing is a triangle edge-transversal. Haxell [H] proved that $ \tau(G) \leq (3-\frac{3}{23})\nu(G) $ edges whose deletion destroys every triangle. As usual, one can define fractional packing and fractional transversal. Let $ {\cal T} $ be the set of triangles of $ G $ . A fractional triangle packing is a function $ f:{\cal T}\rightarrow \mathbb{R}^+ $ such that $ \sum_{T\ni e} \leq 1 $ for every edge $ e $ . A fractional triangle edge-transversal is a function $ g:E\rightarrow \mathbb{R}^+ $ such that $ \sum_{e\in T} g(e)\geq 1 $ for every triangle $ T\in {\cal T} $ . We denote by $ \nu^*(G) $ the maximum of $ \sum_{T\in {\cal T}} f(T) $ over all fractional triangle packing and by $ \tau^*(G) $ the minimum of $ \sum_{e\in E(G)} g(e) $ over all fractional edge-transversals. By duality of linear programming $ \tau^*(G) = \nu^*(G) $ . Krivelevich [K] proved two fractional versions of the conjecture: $ \tau(G) \leq 2\nu^*(G) $ and $ \tau^*(G)\leq 2\nu(G) $ .

=== References listed by OpenProblemGarden ===
- [H] P.Haxell, Packing and covering triangles in graphs, Discrete Mathematics 195 (1999), no. 1–3, 251–254.
- [K] M. Krivelevich, On a conjecture of Tuza about packing and covering of triangles Discrete Mathematics 142 (1995), 281-286.
- *[T] Z. Tuza, A conjecture on triangles of graphs. Graphs Combin. 6 (1990), 373-380.

=== Catalog page (statement + literature review) ===
Triangle-packing vs triangle edge-transversal. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Tuza's conjecture ($\tau(G)\leq 2\nu(G)$) remains open for general graphs. Since the OPG posting, the conjecture has been confirmed for several important graph classes (treewidth $\leq 6$, threshold graphs, random graphs, planar triangulations with the sharper bound $\tau(G)\leq \frac{3}{2}\nu(G)$), and Baron–Kahn showed the factor 2 is asymptotically tight for dense graphs. The best known general bound is still Haxell's $(3-\frac{3}{23})\nu(G)$ from 1999.

 Cited literature (5)

 
 
 
partial Tuza's Conjecture is Asymptotically Tight for Dense Graphs
 (2014)
 

 
 Jacob D. Baron, Jeff Kahn · arXiv preprint · arXiv:1408.4870

Constructs arbitrarily large dense graphs where $\tau(G)/(\nu(G))\to 2$, showing the bound in Tuza's conjecture is asymptotically tight and disproving a conjecture by Yuster that it could be improved.
 

 
 
partial Multi-transversals for Triangles and the Tuza's Conjecture
 (2020)
 

 
 Parinya Chalermsook, Samir Khuller, Pattara Sukprasert, Sumedha Uniyal · arXiv preprint · arXiv:2001.00257

Proves that for every $k\geq 2$ there exists a multiset $F\subseteq E(G)$ with $|F|\leq 2k\nu(G)$ such that every triangle meets $F$ at least $k$ times, strengthening Krivelevich's fractional results.
 

 
 
partial On Tuza's conjecture for triangulations and graphs with small treewidth
 (2020)
 

 
 Fábio Botler, Cristina G. Fernandes, Juan Gutiérrez · arXiv preprint · arXiv:2002.07925

Verifies Tuza's conjecture for all graphs with treewidth at most 6, and proves the sharper bound $\tau(G)\leq\frac{3}{2}\nu(G)$ for planar triangulations other than $K_4$.
 

 
 
partial Closing the Random Graph Gap in Tuza's Conjecture Through the Online Triangle Packing Process
 (2020)
 

 
 Patrick Bennett, Ryan Cushman, Andrzej Dudek · SIAM Journal on Discrete Mathematics · arXiv:2007.04478 · doi:10.1137/20M1351771

Proves that Tuza's conjecture holds with high probability in the Erdős–Rényi random graph $G(n,m)$ for all ranges of $m$, closing a previously open gap.
 

 
 
partial Tuza's Conjecture for Threshold Graphs
 (2021)
 

 
 Marthe Bonamy, Łukasz Bożyk, Andrzej Grzesik, Meike Hatzel, Tomáš Masařík, Jana Novotná, Karolina Okrasa · arXiv preprint · arXiv:2105.09871

Confirms Tuza's conjecture for threshold graphs (simultaneously split graphs and cographs) and for co-chain graphs satisfying certain divisibility conditions.
 

 

 Reviewer notes. The SIAM journal page for Bennett–Cushman–Dudek returned HTTP 403; the DOI 10.1137/20M1351771 is taken from the URL that appeared in search results, while the paper details were confirmed via the arXiv abstract. The 2024 arXiv:2406.06501 paper (Parker) concerns the Aharoni–Zerbib generalization to k-uniform hypergraphs, not Tuza's original conjecture, and was therefore excluded from since_posted. The best general bound remains Haxell's $(3-3/23)\nu(G)$ from 1999; no improvement to the general case was found in post-2013 literature.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. If $ G $ has at most $ k $ edge-disjoint triangles, then there is a set of $ 2k $ edges whose deletion destroys every triangle.

Discussion

This conjecture may be rephrased in terms of packing and edge-transversal. A triangle packing is a set of pairwise edge-disjoint triangles. A triangle edge-tranversal is a set of edges meeting all triangles. Denote the maximum size of a triangle packing in $ G $ by $ \nu(G) $ and the minimum size of a triangle edge-transversal of $ G $ by $ \tau(G) $ . Clearly $ \nu(G) \leq \tau(G) $ . The conjecture translates in $ \tau(G)\leq 2\nu(G) $ . This conjecture, if true, is best possible as can be seen by taking, say $ G=K_4 $ or $ G=K_5 $ . Trivially, $ \tau(G)\leq 3\nu(G) $ , since the set of edges of a maximum triangle packing is a triangle edge-transversal. Haxell [H] proved that $ \tau(G) \leq (3-\frac{3}{23})\nu(G) $ edges whose deletion destroys every triangle. As usual, one can define fractional packing and fractional transversal. Let $ {\cal T} $ be the set of triangles of $ G $ . A fractional triangle packing is a function $ f:{\cal T}\rightarrow \mathbb{R}^+ $ such that $ \sum_{T\ni e} \leq 1 $ for every edge $ e $ . A fractional triangle edge-transversal is a function $ g:E\rightarrow \mathbb{R}^+ $ such that $ \sum_{e\in T} g(e)\geq 1 $ for every triangle $ T\in {\cal T} $ . We denote by $ \nu^*(G) $ the maximum of $ \sum_{T\in {\cal T}} f(T) $ over all fractional triangle packing and by $ \tau^*(G) $ the minimum of $ \sum_{e\in E(G)} g(e) $ over all fractional edge-transversals. By duality of linear programming $ \tau^*(G) = \nu^*(G) $ . Krivelevich [K] proved two fractional versions of the conjecture: $ \tau(G) \leq 2\nu^*(G) $ and $ \tau^*(G)\leq 2\nu(G) $ .

Bibliography

 [H]
 P.Haxell, Packing and covering triangles in graphs, Discrete Mathematics 195 (1999), no. 1–3, 251–254.

 [K]
 M. Krivelevich, On a conjecture of Tuza about packing and covering of triangles Discrete Mathematics 142 (1995), 281-286.

★ [T]
 Z. Tuza, A conjecture on triangles of graphs. Graphs Combin. 6 (1990), 373-380.
