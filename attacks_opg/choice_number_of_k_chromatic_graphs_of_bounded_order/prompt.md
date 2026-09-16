Attack the following open graph-theory problem.

Catalog id: choice_number_of_k_chromatic_graphs_of_bounded_order
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/choice_number_of_k_chromatic_graphs_of_bounded_order/
Original entry: http://www.openproblemgarden.org/op/choice_number_of_k_chromatic_graphs_of_bounded_order
Problem attributed to: Noel, Jonathan A. (posted 2013-02-02)

=== Problem statement (OpenProblemGarden) ===
Title: Choice Number of k-Chromatic Graphs of Bounded Order
Conjecture If $ G $ is a $ k $ -chromatic graph on at most $ mk $ vertices, then $ \text{ch}(G)\leq \text{ch}(K_{m*k}) $ .

=== Discussion / context (OpenProblemGarden) ===
For integers $ m,k\geq1 $ , let $ K_{m*k} $ denote the complete $ k $ -partite graph in which every part has size $ m $ . In one of the original papers on choosability, Erdos, Rubin and Taylor [ERT] proved that $ \text{ch}(K_{2*k})=k $ . Later, Ohba [Ohba] conjectured the following generalization: if $ |V(G)|\leq 2\chi(G)+1 $ , then TeX Embedding failed! .} This was proved by Noel, Reed and Wu [NRW12]. Theorem (Noel, Reed and Wu 2012) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \text{ch}(G)=\chi(G) $ . The above theorem implies that the above conjecture holds for $ m=2 $ . That is, if $ G $ is a $ k $ -chromatic graph on at most $ 2k $ vertices (in fact, at most $ 2k+1 $ vertices), then $ \text{ch}(G)=k=\text{ch}(K_{2*k}) $ . Kierstead [Kie00] proved that $ \text{ch}(K_{3*k})=\left\lceil\frac{4k-1}{3}\right\rceil $ . This was generalized by Noel, West, Wu and Zhu [NWWZ13] to the following: Theorem (Noel, West, Wu and Zhu 2013) For every graph $ G $ , \[\text{ch}(G)\leq\max\left\{\chi(G),\left\lceil\frac{|V(G)|+\chi(G)-1}{3}\right\rceil\right\}.\] Therefore, if $ G $ is a $ k $ -chromatic graph on at most $ 3k $ vertices, then $ \text{ch}(G)\leq \left\lceil\frac{4k-1}{3}\right\rceil=\text{ch}(K_{3*k}) $ . This shows that the conjecture is true for $ m=3 $ . Recently, Kierstead, Salmon and Wang [KSW14] proved the following: Theorem (Kierstead, Salmon and Wang 2014) $ \text{ch}(K_{4*k})=\left\lceil\frac{3k-1}{2}\right\rceil $ . However, it is not known whether the upper bound of $ \left\lceil\frac{3k-1}{2}\right\rceil $ holds for all $ k $ -chromatic graphs on at most $ 4k $ vertices. If true, it would verify the conjecture for $ m=4 $ . The following is a refinement of the conjecture. Conjecture (Noel 2013) For $ n\geq k\geq 1 $ there is a graph $ G_{n,k} $ such that \item $ G_{n,k} $ is a complete $ k $ -partite graph on $ n $ vertices, \item the stability number of $ G_{n,k} $ is $ \left\lceil n/k\right\rceil $ , and \item every $ k $ -chromatic graph $ G $ on at most $ n $ vertices satisfies $ \text{ch}(G)\leq \text{ch}(G_{n,k}) $ .

=== References listed by OpenProblemGarden ===
- [Alo92] N. Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.
- [ERT80] P. Erdos, A. L. Rubin, and H. Taylor. Choosability in graphs. Congress. Numer., XXVI, pages 125–157, 1980.
- [Kie00] H. A. Kierstead. On the choosability of complete multipartite graphs with part size three. Discrete Math., 211(1-3):255–259, 2000.
- [KSW14] H. A. Kierstead, A. Salmon and R. Wang. On the Choice Number of Complete Multipartite Graphs With Part Size Four.
- *[Noe13] J. A. Noel. Choosability of Graphs With Bounded Order: Ohba's Conjecture and Beyond. Master's thesis, McGill University, Montreal. pdf
- [NRW12] J. A. Noel, B. A. Reed, and H. Wu. A Proof of a Conjecture of Ohba. Preprint, arXiv:1211.1999v1, November 2012. Webpage
- [NWWZ13] J. A. Noel, D. B. West, H. Wu, and X. Zhu. Beyond Ohba's Conjecture: A bound on the choice number of -chromatic graphs with vertices. Preprint, arXiv:1308.6739v1, August 2013. pdf
- [Ohb02] K. Ohba. On chromatic-choosable graphs. J. Graph Theory, 40(2):130–135, 2002.
- [Yan03] D. Yang. Extension of the game coloring number and some results on the choosability of complete multipartite graphs. PhD thesis, Arizona State University, Tempe, Arizona, 2003.

=== Catalog page (statement + literature review) ===
Choice Number of k-Chromatic Graphs of Bounded Order — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture has been verified for $m = 2$ (before posting) and $m = 3$ (proved by Noel, West, Wu, and Zhu in 2013, published 2015). Kierstead, Salmon, and Wang determined $\text{ch}(K_{4*k}) = \lceil(3k-1)/2\rceil$ in 2014, establishing what the bound should be for $m = 4$, but the general upper bound $\text{ch}(G) \leq \lceil(3k-1)/2\rceil$ for all $k$-chromatic graphs on at most $4k$ vertices (and the full conjecture for $m \geq 4$) remains open.

 Cited literature (2)

 
 
 
partial Beyond Ohba's Conjecture: A bound on the choice number of k-chromatic graphs with n vertices
 (2015)
 

 
 Jonathan A. Noel, Douglas B. West, Hehui Wu, Xuding Zhu · European Journal of Combinatorics · arXiv:1308.6739 · doi:10.1016/j.ejc.2014.08.032

Proves that ch(G) ≤ max{χ(G), ⌈(|V(G)|+χ(G)-1)/3⌉} for every graph G, which implies the conjecture for m=3: every k-chromatic graph on at most 3k vertices satisfies ch(G) ≤ ⌈(4k-1)/3⌉ = ch(K_{3*k}).
 

 
 
partial On the choice number of complete multipartite graphs with part size four
 (2014)
 

 
 H. A. Kierstead, Andrew Salmon, Ran Wang · arXiv preprint · arXiv:1407.3817

Proves that ch(K_{4*k}) = ⌈(3k-1)/2⌉, determining the target bound for the m=4 case of the conjecture, but does not establish this upper bound for all k-chromatic graphs on at most 4k vertices.
 

 

 Reviewer notes. The m=2 and m=3 cases of the conjecture are settled (m=2 follows from the proof of Ohba's conjecture; m=3 from NWWZ13/2015). The m=4 case reduces to showing ch(G) ≤ ⌈(3k-1)/2⌉ for all k-chromatic G on ≤4k vertices, which is explicitly stated as open in the OPG discussion. No papers resolving m=4 or any m≥5 case were found in exhaustive searching through 2025. Jonathan Noel's recent arXiv profile returned only unrelated work (bootstrap percolation), and his university homepage was unreachable. The KSW14 paper's journal publication venue could not be confirmed from verified sources (ADS shows only arXiv preprint).

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 231s.
 

Conjecture. If $ G $ is a $ k $ -chromatic graph on at most $ mk $ vertices, then $ \text{ch}(G)\leq \text{ch}(K_{m*k}) $ .

Keywords:
choosability · complete multipartite graph · list coloring

Discussion

For integers $ m,k\geq1 $ , let $ K_{m*k} $ denote the complete $ k $ -partite graph in which every part has size $ m $ . In one of the original papers on choosability, Erdos, Rubin and Taylor [ERT] proved that $ \text{ch}(K_{2*k})=k $ . Later, Ohba [Ohba] conjectured the following generalization: if $ |V(G)|\leq 2\chi(G)+1 $ , then TeX Embedding failed! .} This was proved by Noel, Reed and Wu [NRW12]. Theorem (Noel, Reed and Wu 2012) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \text{ch}(G)=\chi(G) $ . The above theorem implies that the above conjecture holds for $ m=2 $ . That is, if $ G $ is a $ k $ -chromatic graph on at most $ 2k $ vertices (in fact, at most $ 2k+1 $ vertices), then $ \text{ch}(G)=k=\text{ch}(K_{2*k}) $ . Kierstead [Kie00] proved that $ \text{ch}(K_{3*k})=\left\lceil\frac{4k-1}{3}\right\rceil $ . This was generalized by Noel, West, Wu and Zhu [NWWZ13] to the following: Theorem (Noel, West, Wu and Zhu 2013) For every graph $ G $ , \[\text{ch}(G)\leq\max\left\{\chi(G),\left\lceil\frac{|V(G)|+\chi(G)-1}{3}\right\rceil\right\}.\] Therefore, if $ G $ is a $ k $ -chromatic graph on at most $ 3k $ vertices, then $ \text{ch}(G)\leq \left\lceil\frac{4k-1}{3}\right\rceil=\text{ch}(K_{3*k}) $ . This shows that the conjecture is true for $ m=3 $ . Recently, Kierstead, Salmon and Wang [KSW14] proved the following: Theorem (Kierstead, Salmon and Wang 2014) $ \text{ch}(K_{4*k})=\left\lceil\frac{3k-1}{2}\right\rceil $ . However, it is not known whether the upper bound of $ \left\lceil\frac{3k-1}{2}\right\rceil $ holds for all $ k $ -chromatic graphs on at most $ 4k $ vertices. If true, it would verify the conjecture for $ m=4 $ . The following is a refinement of the conjecture. Conjecture (Noel 2013) For $ n\geq k\geq 1 $ there is a graph $ G_{n,k} $ such that \item $ G_{n,k} $ is a complete $ k $ -partite graph on $ n $ vertices, \item the stability number of $ G_{n,k} $ is $ \left\lceil n/k\right\rceil $ , and \item every $ k $ -chromatic graph $ G $ on at most $ n $ vertices satisfies $ \text{ch}(G)\leq \text{ch}(G_{n,k}) $ .

Bibliography

 [Alo92]
 N. Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.

 [ERT80]
 P. Erdos, A. L. Rubin, and H. Taylor. Choosability in graphs. Congress. Numer., XXVI, pages 125–157, 1980.

 [Kie00]
 H. A. Kierstead. On the choosability of complete multipartite graphs with part size three. Discrete Math., 211(1-3):255–259, 2000.

 [KSW14]
 H. A. Kierstead, A. Salmon and R. Wang. On the Choice Number of Complete Multipartite Graphs With Part Size Four .
 On the Choice Number of Complete Multipartite Graphs With Part Size Four

★ [Noe13]
 J. A. Noel. Choosability of Graphs With Bounded Order: Ohba's Conjecture and Beyond. Master's thesis, McGill University, Montreal. pdf
 pdf

 [NRW12]
 J. A. Noel, B. A. Reed, and H. Wu. A Proof of a Conjecture of Ohba. Preprint, arXiv:1211.1999v1, November 2012. Webpage
 Webpage

 [NWWZ13]
 J. A. Noel, D. B. West, H. Wu, and X. Zhu. Beyond Ohba's Conjecture: A bound on the choice number of $ k $ -chromatic graphs with $ n $ vertices. Preprint, arXiv:1308.6739v1, August 2013. pdf
 pdf

 [Ohb02]
 K. Ohba. On chromatic-choosable graphs. J. Graph Theory, 40(2):130–135, 2002.

 [Yan03]
 D. Yang. Extension of the game coloring number and some results on the choosability of complete multipartite graphs. PhD thesis, Arizona State University, Tempe, Arizona, 2003.
