Attack the following open graph-theory problem.

Catalog id: weak_saturation_of_the_cube_in_the_clique
Source: OpenProblemGarden (importance: Low ✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/weak_saturation_of_the_cube_in_the_clique/
Original entry: http://www.openproblemgarden.org/op/weak_saturation_of_the_cube_in_the_clique
Problem attributed to: Morrison, Natasha, Noel, Jonathan A. (posted 2016-04-06)

=== Problem statement (OpenProblemGarden) ===
Title: Weak saturation of the cube in the clique
Problem Determine $ \text{wsat}(K_n,Q_3) $ .

=== Discussion / context (OpenProblemGarden) ===
Given graphs $ G $ and $ H $ , let $ \text{wsat}(G,H) $ denote the minimum number of edges in a subgraph $ F $ of $ G $ such that the edges of $ E(G)\setminus E(F) $ can be added to $ F $ , one edge at a time, so that each edge completes a copy of $ H $ when it is added. Of course, if one can solve the problem above, then a natural next step is to determine $ \text{wsat}(K_n,Q_m) $ for all $ n $ and $ m $ . Morrison, Noel and Scott [MNS] solved the related problem of determining $ \text{wsat}(Q_d,Q_m) $ for all $ d $ and $ m $ .

=== References listed by OpenProblemGarden ===
- [MNS] N. Morrison, J. A. Noel, A. Scott. Saturation in the hypercube and bootstrap percolation. To appear in Combin. Probab. Comput.

=== Catalog page (statement + literature review) ===
Weak saturation of the cube in the clique — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem of determining $\text{wsat}(K_n, Q_3)$ — the minimum number of edges in a weakly $Q_3$-saturated subgraph of $K_n$ — remains open. The related problem of $\text{wsat}(Q_d, Q_m)$ (hypercube host) was resolved by Morrison, Noel, and Scott, but no paper found addresses the complete-graph host case. Active research on weak saturation in the clique has focused on bipartite graphs and multipartite structures, leaving the hypercube case open.

 Reviewer notes. Searches found extensive recent literature on weak saturation in cliques (complete bipartite, tensor products, multipartite hypergraphs) but nothing specifically addressing wsat(K_n, Q_m) for any m. The MNS paper (arXiv:1408.5488) solved wsat(Q_d, Q_m) but that is for the hypercube host, not the complete graph host. The Springer Combinatorica 2025 paper on 'weak saturation rank' could not be fully accessed due to redirects. The problem likely remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Problem. Determine $ \text{wsat}(K_n,Q_3) $ .

Keywords:
bootstrap percolation · hypercube · Weak saturation

Discussion

Given graphs $ G $ and $ H $ , let $ \text{wsat}(G,H) $ denote the minimum number of edges in a subgraph $ F $ of $ G $ such that the edges of $ E(G)\setminus E(F) $ can be added to $ F $ , one edge at a time, so that each edge completes a copy of $ H $ when it is added. Of course, if one can solve the problem above, then a natural next step is to determine $ \text{wsat}(K_n,Q_m) $ for all $ n $ and $ m $ . Morrison, Noel and Scott [MNS] solved the related problem of determining $ \text{wsat}(Q_d,Q_m) $ for all $ d $ and $ m $ .

Bibliography

 [MNS]
 N. Morrison, J. A. Noel, A. Scott. Saturation in the hypercube and bootstrap percolation. To appear in Combin. Probab. Comput.
