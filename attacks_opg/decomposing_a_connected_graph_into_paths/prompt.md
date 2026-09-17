Attack the following open graph-theory problem.

Catalog id: decomposing_a_connected_graph_into_paths
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Paths
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/decomposing_a_connected_graph_into_paths/
Original entry: http://www.openproblemgarden.org/op/decomposing_a_connected_graph_into_paths
Problem attributed to: Gallai, Tibor (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Decomposing a connected graph into paths.
Conjecture Every simple connected graph on $ n $ vertices can be decomposed into at most $ \frac{1}{2}(n+1) $ paths.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is tight because a complete graph on $ n $ vertices cannot be covered by less than $ (n+1)/2 $ cycles. There is a similar conjecture about decomposition of an eulerian graph into cycles .

=== References listed by OpenProblemGarden ===
- * [L] L. Lovász, On covering of graphs. In Theory of Graphs (Proc. Colloq., Tihany, 1966), 231--236. Academic Press, New York, 1968.

=== Catalog page (statement + literature review) ===
Decomposing a connected graph into paths. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Gallai's 1968 conjecture — that every connected graph on $n$ vertices decomposes into at most $\lceil n/2 \rceil$ paths — remains open in general. Since the OPG posting date (2013) it has been verified for large families: graphs of maximum degree at most 5 (Bonamy–Perrett, 2016), graphs whose E-subgraph lies in a specific block family (Botler–Sambinelli, 2019), connected planar graphs except $K_3$ and $K_5^-$ (Blanché–Bonamy–Bonichon, 2021), and 2-degenerate graphs (Anto–Basavaraju, 2022). The full conjecture for all connected graphs is still unresolved.

 Cited literature (6)

 
 
 
partial Gallai's path decomposition conjecture for graphs of small maximum degree
 (2016)
 

 
 Marthe Bonamy, Thomas Perrett · arXiv preprint · arXiv:1609.06257

Verifies Gallai's conjecture for every connected graph of maximum degree at most 5.
 

 
 
partial Towards Gallai's path decomposition conjecture
 (2019)
 

 
 Fabio Botler, Maycon Sambinelli · arXiv preprint (later in J. Graph Theory) · arXiv:1911.04546

Verifies the conjecture for the family of graphs whose E-subgraph is a subgraph of a specific block family $\mathcal{G}$, generalising Fan's 2005 result.
 

 
 
partial Gallai's path decomposition in planar graphs
 (2021)
 

 
 Alexandre Blanché, Marthe Bonamy, Nicolas Bonichon · arXiv preprint · arXiv:2110.08870

Proves that every connected planar graph except $K_3$ and $K_5^-$ decomposes into at most $\lfloor n/2 \rfloor$ paths.
 

 
 
partial Gallai's Path Decomposition for 2-degenerate Graphs
 (2023)
 

 
 Nevil Anto, Manu Basavaraju · Discrete Mathematics & Theoretical Computer Science 25:1 · arXiv:2211.07159

Shows that any connected 2-degenerate graph on $n$ vertices, other than the triangle, decomposes into at most $\lfloor n/2 \rfloor$ paths.
 

 
 
partial Gallai's path decomposition conjecture for graphs of small maximum degree
 (2016)
 

 
 Marthe Bonamy, Thomas Perrett · arXiv preprint · arXiv:1609.06257

Proves Gallai's conjecture for all connected graphs $G$ with $\Delta(G) \leq 5$, by showing that any smallest counterexample cannot contain any of five reducible configurations, forcing $G_E$ to be a forest and applying Pyber's earlier theorem.
 

 
 
partial Gallai's path decomposition in planar graphs
 (2022)
 

 
 Alexandre Blanché, Marthe Bonamy, Nicolas Bonichon · arXiv preprint · arXiv:2110.08870

Proves Gallai's conjecture for the entire class of planar graphs (Theorem 1.1): every connected planar graph on $n$ vertices can be decomposed into $\lceil n/2 \rceil$ paths.
 

 

 Reviewer notes. The conjecture is also reported verified for treewidth ≤ 3 (Botler et al., 2020, J. Graph Theory) and treewidth ≤ 4 (more recent work), and for block graphs (AIMS Math, 2025); these were not verified in detail here.

 
 Auto-reviewed 2026-05-08 with claude (main agent, web search + fetch) (web search enabled).
 

Conjecture. Every simple connected graph on $ n $ vertices can be decomposed into at most $ \frac{1}{2}(n+1) $ paths.

Discussion

This conjecture is tight because a complete graph on $ n $ vertices cannot be covered by less than $ (n+1)/2 $ cycles. There is a similar conjecture about decomposition of an eulerian graph into cycles .

Bibliography

★ [L]
 L. Lovász, On covering of graphs. In Theory of Graphs (Proc. Colloq., Tihany, 1966) , 231--236. Academic Press, New York, 1968.
