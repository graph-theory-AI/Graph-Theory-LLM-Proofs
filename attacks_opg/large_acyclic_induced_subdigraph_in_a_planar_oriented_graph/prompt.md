Attack the following open graph-theory problem.

Catalog id: large_acyclic_induced_subdigraph_in_a_planar_oriented_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/large_acyclic_induced_subdigraph_in_a_planar_oriented_graph/
Original entry: http://www.openproblemgarden.org/op/large_acyclic_induced_subdigraph_in_a_planar_oriented_graph
Problem attributed to: Harutyunyan, Ararat (posted 2013-06-25)

=== Problem statement (OpenProblemGarden) ===
Title: Large acyclic induced subdigraph in a planar oriented graph.
Conjecture Every planar oriented graph $ D $ has an acyclic induced subdigraph of order at least $ \frac{3}{5} |V(D)| $ .

=== Discussion / context (OpenProblemGarden) ===
Borodin's 5-Colour Theorem states that every planar graph has an acyclic 5-colouring This implies that every planar oriented graph $ D $ has an acyclic induced subdigraph of order at least $ \frac{2}{5} |V(D)| $ . Already improving this bound to $ \frac{1}{2} |V(D)| $ would be interesting: it is a relaxtion of both a Conjecture of Albertson and Berman stating that every planar graph $ G $ has an induced forest of order $ \frac{1}{2} |V(G)| $ and a Conjecture of Neumann-Lara stating that every planar oriented graph can be split into two acyclic subdigraphs. If true, this conjecture would be best possible.

=== Catalog page (statement + literature review) ===
Large acyclic induced subdigraph in a planar oriented graph. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that every planar oriented graph has an acyclic induced subdigraph of order at least $\frac{3}{5}|V|$ remains open in full generality. Golowich and Rolnick (2015) proved it for planar oriented graphs in which every directed cycle has length at least 8, and established the general lower bound $(1 - 3/g)n$ for graphs with shortest cycle length $g$. The baseline $\frac{2}{5}|V|$ bound from Borodin's 5-colouring theorem has not been improved for arbitrary planar oriented graphs.

 Cited literature (1)

 
 
 
partial Acyclic Subgraphs of Planar Digraphs
 (2015)
 

 
 Noah Golowich, David Rolnick · The Electronic Journal of Combinatorics · arXiv:1407.8045

Proves Harutyunyan's 3/5 conjecture for planar oriented graphs in which every directed cycle has length at least 8, and establishes the general bound $(1-3/g)n$ for digraphs with shortest cycle length $g$.
 

 

 Reviewer notes. The Golowich-Rolnick result (EJC 2015, arXiv:1407.8045) is the only verified post-posting paper with a direct contribution. The paper by Harutyunyan, McDiarmid, and Puig i Surroca (arXiv:2603.02947, 2026) focuses on degree/cycle-length restrictions in general digraphs, not the planar 3/5 bound. A related result attributed to Harutyunyan and Mohar—proving the Neumann-Lara 2-colouring conjecture for planar digraphs of digirth 5 (implying a 1/2 bound)—appeared in several search summaries but could not be verified via a fetchable source; it is therefore not cited. The conjecture as stated (for all planar oriented graphs) remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Every planar oriented graph $ D $ has an acyclic induced subdigraph of order at least $ \frac{3}{5} |V(D)| $ .

Discussion

Borodin's 5-Colour Theorem states that every planar graph has an acyclic 5-colouring This implies that every planar oriented graph $ D $ has an acyclic induced subdigraph of order at least $ \frac{2}{5} |V(D)| $ . Already improving this bound to $ \frac{1}{2} |V(D)| $ would be interesting: it is a relaxtion of both a Conjecture of Albertson and Berman stating that every planar graph $ G $ has an induced forest of order $ \frac{1}{2} |V(G)| $ and a Conjecture of Neumann-Lara stating that every planar oriented graph can be split into two acyclic subdigraphs. If true, this conjecture would be best possible.
