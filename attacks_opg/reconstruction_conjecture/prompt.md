Attack the following open graph-theory problem.

Catalog id: reconstruction_conjecture
Source: OpenProblemGarden (importance: Outstanding ✭✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/reconstruction_conjecture/
Original entry: http://www.openproblemgarden.org/op/reconstruction_conjecture
Problem attributed to: Kelly, Paul J., Ulam, Stanislaw M. (posted 2007-10-18)

=== Problem statement (OpenProblemGarden) ===
Title: Reconstruction conjecture
The deck of a graph $ G $ is the multiset consisting of all unlabelled subgraphs obtained from $ G $ by deleting a vertex in all possible ways (counted according to multiplicity). Conjecture If two graphs on $ \ge 3 $ vertices have the same deck, then they are isomorphic.

=== Discussion / context (OpenProblemGarden) ===
See Wikipedia's Reconstruction Conjecture for more on this problem.

=== References listed by OpenProblemGarden ===
- *[K] P. J. Kelly, A congruence theorem for trees, Pacific J. Math., 7 (1957), 961–968.
- *[U] S. M. Ulam, A collection of mathematical problems, Wiley, New York, 1960.

=== Catalog page (statement + literature review) ===
Reconstruction conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Reconstruction Conjecture remains open for general graphs. Since the problem was posted in 2007, notable partial progress includes: computational verification for all graphs up to 13 vertices (McKay 2021), improved reconstruction-from-smaller-decks results for trees (Groenland–Johnston–Scott–Tan 2021), and a proof that every interval graph on at least 3 vertices is reconstructible (Heinrich–Kiyomi–Otachi–Schweitzer 2025). No counterexample or general proof has been established.

 Cited literature (4)

 
 
 
partial Reconstruction of small graphs and digraphs
 (2021)
 

 
 Brendan D. McKay · arXiv preprint · arXiv:2102.01942

Computationally verifies the graph reconstruction conjecture for all graphs up to 13 vertices (and tournaments up to 13, digraphs up to 9), extending the previously established verification bound.
 

 
 
partial Reconstruction from smaller cards
 (2021)
 

 
 Carla Groenland, Tom Johnston, Alex Scott, Jane Tan · arXiv preprint · arXiv:2103.13359

Shows trees can be reconstructed from their $(n-r)$-deck for $r \le n/9 + o(n)$, and proves connectivity and degree-sequence can be recovered from much smaller partial decks.
 

 
 
partial Interval Graphs are Reconstructible
 (2025)
 

 
 Irene Heinrich, Masashi Kiyomi, Yota Otachi, Pascal Schweitzer · arXiv preprint · arXiv:2504.02353

Proves that every interval graph on at least 3 vertices is reconstructible (and reconstructible in polynomial time), resolving a longstanding open case via new structural techniques for graph separations.
 

 
 
survey Shuffling the Deck: Invariant Theory and the Graph Reconstruction Conjecture
 (2026)
 

 
 Emilie Dufresne, Gabriela Jeronimo, Jenny Kenkel, Haydee Lindo, Nelly Villamizar · arXiv preprint · arXiv:2604.16567

Surveys the reconstruction conjecture and develops an invariant-theoretic algebraic reformulation, aiming to show that polynomials distinguishing decks also distinguish the original graphs.
 

 

 Reviewer notes. A 2023 paper in Information Sciences (ScienceDirect pii/S0020025523014433) titled 'Vertex-substitution framework verifies the reconstruction conjecture for finite undirected graphs' claims a general proof, but could not be accessed (HTTP 403) and Wikipedia does not list it as a resolution — likely a flawed or unaccepted claimed proof. The arXiv:2501.19081 paper (Kim–Lee 2025) concerns matching polynomial reconstruction for hypergraphs and is not directly about the graph reconstruction conjecture. McKay's paper was submitted in 2021 with a final arXiv revision in January 2022; journal venue not confirmed from available pages. Groenland et al. 2103.13359 was last revised November 2023, possibly in press.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. If two graphs on $ \ge 3 $ vertices have the same deck, then they are isomorphic.

Keywords:
reconstruction

Discussion

See Wikipedia's Reconstruction Conjecture for more on this problem.

Bibliography

★ [K]
 P. J. Kelly, A congruence theorem for trees, Pacific J. Math., 7 (1957), 961–968.

★ [U]
 S. M. Ulam, A collection of mathematical problems, Wiley, New York, 1960.

Related conjectures

 
 implies
 Edge Reconstruction Conjecture
 open
 Classical result of Greenwell (1971): every vertex-reconstructible graph with at least four edges is edge-reconstructible (the vertex count, and hence the isolated vertices, of a graph with >= 4 edges is recoverable from its edge deck, and the vertex deck can then be recovered by counting arguments). Hence truth of the Reconstruction Conjecture forces truth of the Edge Reconstruction Conjecture, which only concerns graphs with at least 4 edges. The target's own OPG context states this implication verbatim: 'It is known that if a graph is vertex reconstructible then it is edge reconstructible.' Direction is correct: vertex reconstruction is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
