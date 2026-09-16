Attack the following open graph-theory problem.

Catalog id: partitioning_planar_digraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/partitioning_planar_digraphs/
Original entry: http://www.openproblemgarden.org/op/partitioning_planar_digraphs
Problem attributed to: Neumann-Lara, Victor (posted 2007-03-26)

=== Problem statement (OpenProblemGarden) ===
Title: The Two Color Conjecture
Conjecture If $ G $ is an orientation of a simple planar graph, then there is a partition of $ V(G) $ into $ \{X_1,X_2\} $ so that the graph induced by $ X_i $ is acyclic for $ i=1,2 $ .

=== Discussion / context (OpenProblemGarden) ===
This is a type of coloring digraphs introduced by V. Neumann-Lara. More generally, if $ G $ is a digraph, we wish to partition the vertex set of $ G $ into as few parts as possible so that each induces an acyclic subgraph.

=== References listed by OpenProblemGarden ===
- * [N] V. Neumann-Lara (1985). Vertex colourings in digraphs. Some problems. Technical report, University of Waterloo.

=== Catalog page (statement + literature review) ===
The Two Color Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Two Color Conjecture remains open in full generality: it is unknown whether every orientation of a simple planar graph admits a vertex partition into two acyclic sets. Meaningful partial progress exists: the conjecture is confirmed for planar digraphs of digirth at least 5 (Harutyunyan–Mohar, 2014) and digirth at least 4 (Li–Mohar, 2016), and has been shown equivalent to 2-colorability of all oriented $K_5$-minor-free graphs (Steiner, 2021).

 Cited literature (4)

 
 
 
partial Planar digraphs of digirth five are 2-colorable
 (2014)
 

 
 Ararat Harutyunyan, Bojan Mohar · arXiv preprint · arXiv:1401.2213

Every planar digraph of digirth at least 5 is 2-colorable (vertices partitioned into 2 acyclic sets); the result also holds for list colorings.
 

 
 
partial Planar digraphs of digirth four are 2-colourable
 (2016)
 

 
 Zhentao Li, Bojan Mohar · SIAM Journal on Discrete Mathematics · arXiv:1606.06114 · doi:10.1137/16M108080X

Every planar digraph of digirth at least 4 is 2-colourable, strengthening the digirth-5 result of Harutyunyan and Mohar.
 

 
 
reduction A Note on Graphs of Dichromatic Number 2
 (2021)
 

 
 Raphael Steiner · Discrete Mathematics & Theoretical Computer Science · arXiv:1907.00351 · doi:10.23638/DMTCS-22-4-11

The Two Color Conjecture is equivalent to the statement that every oriented $K_5$-minor-free graph is 2-colourable, providing a new reformulation of the problem.
 

 
 
partial A Note on Graphs of Dichromatic Number 2
 (2019)
 

 
 Raphael Steiner · arXiv preprint · arXiv:1907.00351

Shows that Neumann-Lara's Conjecture is equivalent to the more general statement that every $K_5$-minor-free graph $G$ satisfies $\vec{\chi}(G) \leq 2$ and moreover any orientation of $G$ admits an acyclic 2-colouring without monochromatic triangles.
 

 

 Reviewer notes. The full conjecture (digirth >= 3, i.e., arbitrary planar digraphs) remains open as of 2026. The SIAM page for the Li-Mohar paper returned HTTP 403; the DOI 10.1137/16M108080X is taken from the SIAM URL found in search results. A 2026 arXiv preprint (2603.01020, Harutyunyan-Picasarri-Arrieta-Puig i Surroca) proves the list version of the related Erdos-Neumann-Lara conjecture but does not directly resolve the Two Color Conjecture for planar digraphs.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. If $ G $ is an orientation of a simple planar graph, then there is a partition of $ V(G) $ into $ \{X_1,X_2\} $ so that the graph induced by $ X_i $ is acyclic for $ i=1,2 $ .

Keywords:
acyclic · digraph · planar

Discussion

This is a type of coloring digraphs introduced by V. Neumann-Lara. More generally, if $ G $ is a digraph, we wish to partition the vertex set of $ G $ into as few parts as possible so that each induces an acyclic subgraph.

Bibliography

★ [N]
 V. Neumann-Lara (1985). Vertex colourings in digraphs. Some problems. Technical report, University of Waterloo.
