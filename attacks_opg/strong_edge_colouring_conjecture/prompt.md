Attack the following open graph-theory problem.

Catalog id: strong_edge_colouring_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/strong_edge_colouring_conjecture/
Original entry: http://www.openproblemgarden.org/op/strong_edge_colouring_conjecture
Problem attributed to: Erdos, Paul, Nesetril, Jaroslav (posted 2013-03-01)

=== Problem statement (OpenProblemGarden) ===
Title: Strong edge colouring conjecture
A strong edge-colouring of a graph $ G $ is a edge-colouring in which every colour class is an induced matching; that is, any two vertices belonging to distinct edges with the same colour are not adjacent. The strong chromatic index $ s\chi'(G) $ is the minimum number of colours in a strong edge-colouring of $ G $ . Conjecture $$s\chi'(G) \leq \frac{5\Delta^2}{4}, \text{if $\Delta$ is even,}$$ $$s\chi'(G) \leq \frac{5\Delta^2-2\Delta +1}{4},&\text{if $\Delta$ is odd.}$$

=== Discussion / context (OpenProblemGarden) ===
The conjectured bounds would be sharp. When $ D $ is even, expanding each vertex of a $ 5 $ -cycle into a stable set of size $ \Delta/2 $ yields such a graph with $ 5\Delta^2/4 $ edges in which the largest induced matching has size $ 1 $ . A similar construction achieves the bound when $ \Delta $ is odd. Greedy colouring the edges yields $ s\chi'(G) \leq 2\Delta(\Delta-1)+1 $ . Using probabilistic methods, Molloy and Reed~[MoRe97] proved that there is a positive constant $ \epsilon $ such that, for sufficiently large $ \Delta $ , every graph with maximum degree $ \Delta $ has strong chromatic index at most $ (2-\epsilon)\Delta^2 $ . The greedy bound proves the conjecture for $ \Delta \leq 2 $ . For $ \Delta =3 $ , the conjectured bound of 10 was proved independently by Hor\'ak, He, and Trotter[HHT] and by Andersen [A]. For $ \Delta=4 $ , the conjectured bound is 20, and Cranston [C] proved that 22 colours suffice. For a bipartite graph $ G $ , Faudree et al. [FGST] conjectured that $ s\chi'(G)\leq \Delta^2(G) $ . This is implied by the stronger conjecture due to Kaiser. Conjecture Let $ G=((A_1,A_2),E) $ be a bipartite graph such that every vertex in $ A_1 $ has degree at most $ \Delta_1 $ and every vertex in $ A_2 $ has degree at most $ \Delta_2 $ . Then $ s\chi'(G)\leq \Delta_1\Delta_2 $ .

=== References listed by OpenProblemGarden ===
- [A] L. D. Andersen. The strong chromatic index of a cubic graph is at most 10. Discrete Math., 108(1-3):231--252, 1992.
- [C] D. W. Cranston. Strong edge-coloring of graphs with maximum degree 4 using 22 colors. Discrete Math., 306(21):2772--2778, 2006.
- [FGST] R. J. Faudree, A. Gyárfás, R. H. Schelp, and Zs. Tuza. Induced matchings in bipartite graphs. Discrete Math., 78(1-2):83--87, 1989.
- [HHT] P. Horák, Q. He, and W. T. Trotter. Induced matchings in cubic graphs. J. Graph Theory, 17(2):151--160, 1993.

=== Catalog page (statement + literature review) ===
Strong edge colouring conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Erdős–Nešetřil strong edge-colouring conjecture ($s\chi'(G) \leq \frac{5\Delta^2}{4}$ for even $\Delta$) remains open. The best asymptotic bound for large $\Delta$ is $1.93\Delta^2$ (Bruhn–Joos, 2018), improving the earlier $(2-\varepsilon)\Delta^2$ of Molloy–Reed. For $\Delta=4$ the conjectured bound of 20 is still unresolved; the current best is 21 colors (Huang–Santana–Yu, 2018).

 Cited literature (3)

 
 
 
partial A Stronger Bound for the Strong Chromatic Index
 (2018)
 

 
 Henning Bruhn, Felix Joos · Combinatorics, Probability and Computing · arXiv:1504.02583 · doi:10.1017/S0963548317000244

Proves $\chi'_s(G) \leq 1.93\Delta(G)^2$ for graphs with sufficiently large maximum degree, strictly improving the $(2-\varepsilon)\Delta^2$ bound of Molloy and Reed.
 

 
 
partial Strong chromatic index of graphs with maximum degree four
 (2018)
 

 
 Mingfang Huang, Michael Santana, Gexin Yu · arXiv preprint · arXiv:1806.07012

Proves $\chi'_s(G) \leq 21$ for graphs with maximum degree 4, improving Cranston's 2006 bound of 22; the conjectured bound of 20 remains open.
 

 
 
partial The strong chromatic index of $(3,\Delta)$-bipartite graphs
 (2018)
 

 
 Mingfang Huang, Gexin Yu, Xiangqian Zhou · arXiv preprint · arXiv:1806.07017

Proves that every bipartite graph with one part of maximum degree at most 3 and the other of maximum degree $\Delta$ admits a strong edge-colouring with at most $3\Delta$ colours, confirming the Brualdi–Quinn Massey conjecture for this class.
 

 

 Reviewer notes. The Bruhn–Joos paper was submitted to arXiv in April 2015 (after the 2013-03-01 posting date) and published in CPC in 2018; year listed as 2018. Huang–Santana–Yu (1806.07012) is listed as an arXiv preprint; journal publication not confirmed. For 1806.07017 the fetched content mentioned 'published in Discrete Mathematics, 2017', conflicting with the June 2018 arXiv submission date — possible extraction error; treated as 2018 arXiv preprint. Cames van Batenburg et al. (2019, arXiv:1905.06031) on K_4-minor-free graphs is a tangential partial result and was not included in since_posted. No complete proof or disproof was found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. $$s\chi'(G) \leq \frac{5\Delta^2}{4}, \text{if $\Delta$ is even,}$$ $$s\chi'(G) \leq \frac{5\Delta^2-2\Delta +1}{4},&\text{if $\Delta$ is odd.}$$

Discussion

The conjectured bounds would be sharp. When $ D $ is even, expanding each vertex of a $ 5 $ -cycle into a stable set of size $ \Delta/2 $ yields such a graph with $ 5\Delta^2/4 $ edges in which the largest induced matching has size $ 1 $ . A similar construction achieves the bound when $ \Delta $ is odd. Greedy colouring the edges yields $ s\chi'(G) \leq 2\Delta(\Delta-1)+1 $ . Using probabilistic methods, Molloy and Reed~[MoRe97] proved that there is a positive constant $ \epsilon $ such that, for sufficiently large $ \Delta $ , every graph with maximum degree $ \Delta $ has strong chromatic index at most $ (2-\epsilon)\Delta^2 $ . The greedy bound proves the conjecture for $ \Delta \leq 2 $ . For $ \Delta =3 $ , the conjectured bound of 10 was proved independently by Hor\'ak, He, and Trotter[HHT] and by Andersen [A]. For $ \Delta=4 $ , the conjectured bound is 20, and Cranston [C] proved that 22 colours suffice. For a bipartite graph $ G $ , Faudree et al. [FGST] conjectured that $ s\chi'(G)\leq \Delta^2(G) $ . This is implied by the stronger conjecture due to Kaiser. Conjecture Let $ G=((A_1,A_2),E) $ be a bipartite graph such that every vertex in $ A_1 $ has degree at most $ \Delta_1 $ and every vertex in $ A_2 $ has degree at most $ \Delta_2 $ . Then $ s\chi'(G)\leq \Delta_1\Delta_2 $ .

Bibliography

 [A]
 L. D. Andersen. The strong chromatic index of a cubic graph is at most 10. Discrete Math., 108(1-3):231--252, 1992.

 [C]
 D. W. Cranston. Strong edge-coloring of graphs with maximum degree 4 using 22 colors. Discrete Math., 306(21):2772--2778, 2006.

 [FGST]
 R. J. Faudree, A. Gyárfás, R. H. Schelp, and Zs. Tuza. Induced matchings in bipartite graphs. Discrete Math., 78(1-2):83--87, 1989.

 [HHT]
 P. Horák, Q. He, and W. T. Trotter. Induced matchings in cubic graphs. J. Graph Theory, 17(2):151--160, 1993.
