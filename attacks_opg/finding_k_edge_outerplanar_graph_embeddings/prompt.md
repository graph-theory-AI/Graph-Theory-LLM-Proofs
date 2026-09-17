Attack the following open graph-theory problem.

Catalog id: finding_k_edge_outerplanar_graph_embeddings
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/finding_k_edge_outerplanar_graph_embeddings/
Original entry: http://www.openproblemgarden.org/op/finding_k_edge_outerplanar_graph_embeddings
Problem attributed to: Bentz, Cedric (posted 2010-04-18)

=== Problem statement (OpenProblemGarden) ===
Title: Finding k-edge-outerplanar graph embeddings
Conjecture It has been shown that a $ k $ -outerplanar embedding for which $ k $ is minimal can be found in polynomial time. Does a similar result hold for $ k $ -edge-outerplanar graphs?

=== Discussion / context (OpenProblemGarden) ===
A $ k $ -outerplanar graph [Baker] with $ k > 0 $ is a planar graph having an embedding with at most $ k $ layers of vertices such that after removing iteratively the vertices (and their adjacent edges) lying on the outer face $ k $ times, we obtain the empty graph. A $ k $ -edge-outerplanar graph [Bentz] is defined to be a planar graph having an embedding with at most $ k $ layers of edges such that after removing iteratively the edges lying on the outer face $ k $ times, we obtain a graph with no edge. All $ k $ -edge-outerplanar graphs are $ k $ -outerplanar graphs. Given a planar graph, Bienstock and Monma have shown that a $ k $ -outerplanar embedding for which $ k $ is minimal can be found in polynomial time. Does a similar result hold for $ k $ -edge-outerplanar graphs?

=== References listed by OpenProblemGarden ===
- C. Bentz, “Disjoint paths in sparse graphs,” Discrete Appl. Math., vol. 157, no. 17, pp. 3558–3568, 2009
- D. Bienstock and C. L. Monma, “On the complexity of embedding planar graphs to minimize certain distance measures,” Algorithmica, vol. 5, no. 1–4, pp. 93–109, 1990
- B. S. Baker, “Approximation algorithms for np-complete problems on planar graphs,” J. ACM, vol. 41, no. 1, pp. 153–180, 1994

=== Catalog page (statement + literature review) ===
Finding k-edge-outerplanar graph embeddings — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 No verifiable post-2010 result resolves whether a $k$-edge-outerplanar embedding of a planar graph with minimum $k$ can be computed in polynomial time. Recent work on outerplanarity (e.g., Biedl-Mondal 2024) treats the vertex-based notion and gives combinatorial bounds, not the algorithmic edge-outerplanarity question raised by Bentz. Searches and follow-ups to Bentz's 2009 paper did not surface any published proof or refutation.

 Reviewer notes. The Biedl-Mondal paper (arXiv:2407.04282, WG 2024) gives improved bounds for vertex-outerplanarity of planar graphs but does not address the algorithmic question of computing minimum k-edge-outerplanarity, so it is not cited as progress. Several Springer/ResearchGate URLs returned 403 and could not be verified. A more thorough search of Bentz's later papers and proceedings of WG/ISAAC/ESA 2010-2026 might still uncover relevant work; status 'open' is reported with medium confidence based on absence of evidence rather than a definitive negative result.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. It has been shown that a $ k $ -outerplanar embedding for which $ k $ is minimal can be found in polynomial time. Does a similar result hold for $ k $ -edge-outerplanar graphs?

Keywords:
planar graph · polynomial algorithm

Discussion

A $ k $ -outerplanar graph [Baker] with $ k > 0 $ is a planar graph having an embedding with at most $ k $ layers of vertices such that after removing iteratively the vertices (and their adjacent edges) lying on the outer face $ k $ times, we obtain the empty graph. A $ k $ -edge-outerplanar graph [Bentz] is defined to be a planar graph having an embedding with at most $ k $ layers of edges such that after removing iteratively the edges lying on the outer face $ k $ times, we obtain a graph with no edge. All $ k $ -edge-outerplanar graphs are $ k $ -outerplanar graphs. Given a planar graph, Bienstock and Monma have shown that a $ k $ -outerplanar embedding for which $ k $ is minimal can be found in polynomial time. Does a similar result hold for $ k $ -edge-outerplanar graphs?

Bibliography

 [?]
 C. Bentz, “Disjoint paths in sparse graphs,” Discrete Appl. Math., vol. 157, no. 17, pp. 3558–3568, 2009

 [?]
 D. Bienstock and C. L. Monma, “On the complexity of embedding planar graphs to minimize certain distance measures,” Algorithmica, vol. 5, no. 1–4, pp. 93–109, 1990

 [?]
 B. S. Baker, “Approximation algorithms for np-complete problems on planar graphs,” J. ACM, vol. 41, no. 1, pp. 153–180, 1994
