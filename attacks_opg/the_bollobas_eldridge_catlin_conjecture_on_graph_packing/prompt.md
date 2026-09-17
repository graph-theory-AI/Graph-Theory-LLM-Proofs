Attack the following open graph-theory problem.

Catalog id: the_bollobas_eldridge_catlin_conjecture_on_graph_packing
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_bollobas_eldridge_catlin_conjecture_on_graph_packing/
Original entry: http://www.openproblemgarden.org/op/the_bollobas_eldridge_catlin_conjecture_on_graph_packing

=== Problem statement (OpenProblemGarden) ===
Title: The Bollobás-Eldridge-Catlin Conjecture on graph packing
Conjecture (BEC-conjecture) If $ G_1 $ and $ G_2 $ are $ n $ -vertex graphs and $ (\Delta(G_1) + 1) (\Delta(G_2) + 1) < n + 1 $ , then $ G_1 $ and $ G_2 $ pack.

=== Discussion / context (OpenProblemGarden) ===
A pair of $ n $ -vertex graphs $ G_1 $ and $ G_2 $ are said to $ {\it pack} $ if they are edge-disjoint subgraphs of the complete graph on $ n $ vertices. The main conjecture in the area of graph packing is the abovementioned conjecture by Bollobás, Eldridge [BE] and Catlin [C]. In support of the BEC-conjecture, Sauer and Spencer [SS] proved that if $ G_1 $ and $ G_2 $ are $ n $ -vertex graphs and $ 2 \Delta(G_1) \Delta(G_2) < n $ then $ G_1 $ and $ G_2 $ pack. Given a graph $ G $ , $ L(G) $ denotes the line graph of $ G $ and $ \Theta(G) $ denotes the number $ \Delta(L(G)) + 2 $ . Kostochka and Yu [KY1] proved that if $ G_1 $ and $ G_2 $ are two $ n $ -vertex graphs with $ \Theta(G_1) \Delta(G_2) \leq n $ , then $ G_1 $ and $ G_2 $ pack with the following exceptions: (1) $ G_1 $ is a perfect matching and $ G_2 $ is either $ K_{n/2,n/2} $ with $ n/2 $ odd or contains $ K_{n/2 + 1} $ or (2) $ G_2 $ is a perfect matching and $ G_1 $ is $ K_{r,n-r} $ with $ r $ odd or contains $ K_{n/2 + 1} $ . Kostachka and Yu [KY2] conjectured that if $ G_1 $ and $ G_2 $ are $ n $ -vertex graphs with $ \Theta(G_1) \Theta(G_2) < 2n $ then $ G_1 $ and $ G_2 $ pack.

=== References listed by OpenProblemGarden ===
- *[BE] B. Bollabás and S. E. Eldridge, Maximal matchings in graphs with given maximal and minimal degrees, Congr. Numer. XV (1976), 165--168.
- *[C] P. A. Catlin, Embedding subgraphs and coloring graphs under extremal degree conditions, Ph. D. Thesis, Ohio State Univ., Columbus (1976).
- [KY1] A. V. Kostochka and G. Yu, An Ore-type analogue of the Sauer-Spencer Theorem, Graphs Combin. 23 (2007), 419--424.
- [KY2] A. V. Kostochka and G. Yu, An Ore-type graph packing problems, Combin. Probab. Comput. 16 (2007), 167--169.
- [SS] N. Sauer and J. Spencer, Edge disjoint placement of graphs, J. Combin. Theory Ser. B 25 (1978), 295--302.

=== Catalog page (statement + literature review) ===
The Bollobás-Eldridge-Catlin Conjecture on graph packing — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The BEC conjecture remains open in general. Since the problem was posted, Cames van Batenburg and Kang proved it for $K_{2,t}$-free graphs satisfying $\Delta(G_1) > 17t \cdot \Delta(G_2)$, and also for pairs of graphs with even girth at least 10 when at least one graph has $\Delta \geq 940060$.

 Cited literature (2)

 
 
 
partial Packing Graphs of Bounded Codegree
 (2018)
 

 
 Wouter Cames van Batenburg, Ross J. Kang · Combinatorics, Probability and Computing · doi:10.1017/S0963548318000032

Proves the BEC conjecture under the additional hypothesis that $G_1$ contains no $K_{2,t}$ and $\Delta(G_1) > 17t \cdot \Delta(G_2)$.
 

 
 
partial The Bollobás-Eldridge-Catlin conjecture for even girth at least 10
 (2017)
 

 
 Wouter Cames van Batenburg, Ross J. Kang · arXiv preprint · arXiv:1703.05149 · doi:10.48550/arXiv.1703.05149

Proves the BEC conjecture when neither $G_1$ nor $G_2$ contains a 4-, 6-, or 8-cycle (even girth $\geq 10$) and at least one has maximum degree $\geq 940060$.
 

 

 Reviewer notes. The Kaul-Kostochka-Yu (2008) Combinatorica paper on the BEC conjecture predates the 2013 OPG posting and is not included. A Radboud University repository page titled 'Packing two graphs of even girth 10' by the same authors returned HTTP 403 and could not be verified; it may be a published journal version of arXiv:1703.05149. No full proof or disproof of the conjecture was found in the post-2013 literature.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture (BEC-conjecture). If $ G_1 $ and $ G_2 $ are $ n $ -vertex graphs and $ (\Delta(G_1) + 1) (\Delta(G_2) + 1) < n + 1 $ , then $ G_1 $ and $ G_2 $ pack.

Keywords:
graph packing

Discussion

A pair of $ n $ -vertex graphs $ G_1 $ and $ G_2 $ are said to $ {\it pack} $ if they are edge-disjoint subgraphs of the complete graph on $ n $ vertices. The main conjecture in the area of graph packing is the abovementioned conjecture by Bollobás, Eldridge [BE] and Catlin [C]. In support of the BEC-conjecture, Sauer and Spencer [SS] proved that if $ G_1 $ and $ G_2 $ are $ n $ -vertex graphs and $ 2 \Delta(G_1) \Delta(G_2) < n $ then $ G_1 $ and $ G_2 $ pack. Given a graph $ G $ , $ L(G) $ denotes the line graph of $ G $ and $ \Theta(G) $ denotes the number $ \Delta(L(G)) + 2 $ . Kostochka and Yu [KY1] proved that if $ G_1 $ and $ G_2 $ are two $ n $ -vertex graphs with $ \Theta(G_1) \Delta(G_2) \leq n $ , then $ G_1 $ and $ G_2 $ pack with the following exceptions: (1) $ G_1 $ is a perfect matching and $ G_2 $ is either $ K_{n/2,n/2} $ with $ n/2 $ odd or contains $ K_{n/2 + 1} $ or (2) $ G_2 $ is a perfect matching and $ G_1 $ is $ K_{r,n-r} $ with $ r $ odd or contains $ K_{n/2 + 1} $ . Kostachka and Yu [KY2] conjectured that if $ G_1 $ and $ G_2 $ are $ n $ -vertex graphs with $ \Theta(G_1) \Theta(G_2) < 2n $ then $ G_1 $ and $ G_2 $ pack.

Bibliography

★ [BE]
 B. Bollabás and S. E. Eldridge, Maximal matchings in graphs with given maximal and minimal degrees, Congr. Numer. XV (1976), 165--168.

★ [C]
 P. A. Catlin, Embedding subgraphs and coloring graphs under extremal degree conditions, Ph. D. Thesis, Ohio State Univ., Columbus (1976).

 [KY1]
 A. V. Kostochka and G. Yu, An Ore-type analogue of the Sauer-Spencer Theorem, Graphs Combin. 23 (2007), 419--424.

 [KY2]
 A. V. Kostochka and G. Yu, An Ore-type graph packing problems, Combin. Probab. Comput. 16 (2007), 167--169.

 [SS]
 N. Sauer and J. Spencer, Edge disjoint placement of graphs, J. Combin. Theory Ser. B 25 (1978), 295--302.
