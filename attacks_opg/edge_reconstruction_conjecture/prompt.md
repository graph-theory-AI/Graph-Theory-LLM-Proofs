Attack the following open graph-theory problem.

Catalog id: edge_reconstruction_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/edge_reconstruction_conjecture/
Original entry: http://www.openproblemgarden.org/op/edge_reconstruction_conjecture
Problem attributed to: Harary, Frank (posted 2008-05-23)

=== Problem statement (OpenProblemGarden) ===
Title: Edge Reconstruction Conjecture
Conjecture Every simple graph with at least 4 edges is reconstructible from it's edge deleted subgraphs

=== Discussion / context (OpenProblemGarden) ===
It is known that if a graph is vertex reconstructible then it is edge reconstructible.

=== References listed by OpenProblemGarden ===
- J.A.Bondy, A graph reconstruction manual, Surveys in Combinatorics, LMS-Lecture Note Series 166(1991)

=== Catalog page (statement + literature review) ===
Edge Reconstruction Conjecture — Graph-theory open problems

 
 Status
 open
 high confidence
 

 Harary's Edge Reconstruction Conjecture (1964) — that every simple graph with at least 4 edges is determined up to isomorphism by its multiset of edge-deleted subgraphs — remains open. Recent work since 2008 has produced reformulations (e.g., a combinatorial $K$-theory framework) and partial results for restricted graph classes (e.g., unicyclic graphs with three non-isomorphic subtrees) and for reconstructing graph polynomials from the edge-deck, but no proof or counterexample to the original conjecture has appeared.

 Cited literature (4)

 
 
 
reduction A combinatorial $K$-theory perspective on the Edge Reconstruction Conjecture in graph theory
 (2024)
 

 
 Maxine E. Calle, Julian J. Gould · arXiv preprint · arXiv:2402.14986

Reformulates the edge reconstruction conjecture using the $K$-theory of categories with covering families, providing an abstract algebraic framework for the problem rather than a resolution.
 

 
 
partial Reconstructing edge-deleted unicyclic graphs
 (2024)
 

 
 Anthony E. Pizzimenti, Umarkhon Rakhimov · arXiv preprint · arXiv:2411.03133

Proves that the edge reconstruction conjecture holds for unicyclic graphs (graphs with exactly one cycle) that have three non-isomorphic subtrees attached to the cycle.
 

 
 
partial On the edge reconstruction of the characteristic and permanental polynomials of a simple graph
 (2023)
 

 
 Jingyuan Zhang, Xian'an Jin, Weigen Yan, Qinghai Liu · arXiv preprint · arXiv:2310.07104

Shows that for a simple graph $G$ with $|V|\neq|E|$, the characteristic, permanental, and Laplacian polynomials of $G$ can be reconstructed from polynomial information of edge-deleted and vertex-pair-deleted subgraphs.
 

 
 
partial Reconstructing the degree sequence of a sparse graph from a partial deck
 (2022)
 

 
 Carla Groenland, Tom Johnston, Andrey Kupavskii, Kitty Meeks, Alex Scott, Jane Tan · arXiv preprint · arXiv:2102.08679

Proves that the degree sequence of any graph with average degree at most $d$ can be reconstructed from any deck missing at most $\frac{n}{10^4 d^3}$ cards; in particular, for graphs embeddable on a fixed surface (e.g., planar graphs), the degree sequence is reconstructible even when a linear number of cards are missing.
 

 

 Reviewer notes. The conjecture remains open as of 2026; partial results since 2008 address restricted graph classes (e.g., unicyclic graphs) or reconstruct invariants weaker than the graph itself (polynomials). The combinatorial $K$-theory approach (Calle-Gould 2024) is a reformulation rather than a proof. Müller's 1977 result (graphs with $e>n\log_2 n$) and Lovász's earlier result predate the OPG posting date and are not cited above.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Every simple graph with at least 4 edges is reconstructible from it's edge deleted subgraphs

Keywords:
reconstruction

Discussion

It is known that if a graph is vertex reconstructible then it is edge reconstructible.

Bibliography

 [?]
 J.A.Bondy, A graph reconstruction manual, Surveys in Combinatorics, LMS-Lecture Note Series 166(1991)

Related conjectures

 
 implied by
 Reconstruction conjecture
 partial
 Classical result of Greenwell (1971): every vertex-reconstructible graph with at least four edges is edge-reconstructible (the vertex count, and hence the isolated vertices, of a graph with >= 4 edges is recoverable from its edge deck, and the vertex deck can then be recovered by counting arguments). Hence truth of the Reconstruction Conjecture forces truth of the Edge Reconstruction Conjecture, which only concerns graphs with at least 4 edges. The target's own OPG context states this implication verbatim: 'It is known that if a graph is vertex reconstructible then it is edge reconstructible.' Direction is correct: vertex reconstruction is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
