Attack the following open graph-theory problem.

Catalog id: cycle_double_covers_containing_predefined_2_regular_subgraphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/cycle_double_covers_containing_predefined_2_regular_subgraphs/
Original entry: http://www.openproblemgarden.org/op/cycle_double_covers_containing_predefined_2_regular_subgraphs
Problem attributed to: Arthur, Hoffmann-Ostenhof (posted 2017-06-21)

=== Problem statement (OpenProblemGarden) ===
Title: Cycle Double Covers Containing Predefined 2-Regular Subgraphs
Conjecture Let $ G $ be a $ 2 $ -connected cubic graph and let $ S $ be a $ 2 $ -regular subgraph such that $ G-E(S) $ is connected. Then $ G $ has a cycle double cover which contains $ S $ (i.e all cycles of $ S $ ).

=== Discussion / context (OpenProblemGarden) ===
Used definitions in the above conjecture: a "cycle" is a connected 2-regular subgraph, a "cycle double cover" of a graph $ G $ is a set of cycles of $ G $ such that every edge of $ G $ is contained in precisely two cycles of the set. This conjecture has been motivated by Theorem 3, respectively, Theorem 4 in www.arxiv.org/abs/1711.10614. A weaker conjecture (Conjecture 14) has been stated in "Snarks with special spanning trees" (see www.arxiv.org/abs/1706.05595).

=== Catalog page (statement + literature review) ===
Cycle Double Covers Containing Predefined 2-Regular Subgraphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture of Arthur and Hoffmann-Ostenhof asks whether every 2-connected cubic graph $G$ with a 2-regular subgraph $S$ such that $G-E(S)$ is connected has a cycle double cover containing all cycles of $S$. The motivating paper of Hoffmann-Ostenhof, Zhang, and Zhang (Eur. J. Combin., 2019) established the special case where $S$ has at most 3 circuits and $G-E(S)$ is a spanning tree, and Li, Hao, Luo, and Zhang (Discrete Math., 2025) extended the single-cycle ($S=C$ non-separating) case by producing a 5-CDC or 6-CDC containing $C$ depending on Petersen-contractibility. The full conjecture as stated for arbitrary 2-regular $S$ appears to remain open.

 Cited literature (2)

 
 
 
partial Cycle double covers and non-separating cycles
 (2019)
 

 
 Arthur Hoffmann-Ostenhof, Cun-Quan Zhang, Zhang Zhang · European Journal of Combinatorics · arXiv:1711.10614 · doi:10.1016/j.ejc.2019.03.011

Proves that every 2-connected cubic graph that decomposes into a spanning tree and a 2-regular subgraph $C$ consisting of at most 3 circuits has a cycle double cover containing $C$, addressing the motivating special case of the conjecture.
 

 
 
partial Non-separating cycles and 5-cycle double covers
 (2025)
 

 
 Xiaoyu Li, Rong-Xia Hao, Rong Luo, Cun-Quan Zhang · Discrete Mathematics

Strengthens the single non-separating cycle case: if a 2-edge-connected graph $G$ has a non-separating cycle $C$ satisfying certain conditions, then $G$ admits a 5-CDC containing $C$ (or a 6-CDC if $G$ is contractible to the Petersen graph).
 

 

 Reviewer notes. The OPG conjecture is for 2-regular subgraphs $S$ that may consist of multiple disjoint cycles (with $G-E(S)$ connected, not necessarily a tree). The 2019 paper (already cited in the OPG entry) covers $S$ with at most 3 components when $G-E(S)$ is a spanning tree. The 2025 Li-Hao-Luo-Zhang paper handles the single-cycle (k=1) non-separating case more strongly (5-CDC/6-CDC); ScienceDirect abstract page returned 403 so confirmation relied on indexed search snippets. No WebFetch-verified post-2017 source establishes the full conjecture for arbitrary k or refutes it, so the original conjecture is treated as open with meaningful partial progress.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Let $ G $ be a $ 2 $ -connected cubic graph and let $ S $ be a $ 2 $ -regular subgraph such that $ G-E(S) $ is connected. Then $ G $ has a cycle double cover which contains $ S $ (i.e all cycles of $ S $ ).

Discussion

Used definitions in the above conjecture: a "cycle" is a connected 2-regular subgraph, a "cycle double cover" of a graph $ G $ is a set of cycles of $ G $ such that every edge of $ G $ is contained in precisely two cycles of the set. This conjecture has been motivated by Theorem 3, respectively, Theorem 4 in www.arxiv.org/abs/1711.10614. A weaker conjecture (Conjecture 14) has been stated in "Snarks with special spanning trees" (see www.arxiv.org/abs/1706.05595).

Related conjectures

 
 implies
 Cycle double cover conjecture
 partial
 CDC reduces to bridgeless cubic graphs (stated in the target's OPG context), and a minimal cubic counterexample is 3-connected by the standard 2-cut reduction. By Tutte's theorem, a 3-connected graph has a non-separating induced circuit C. If C is Hamiltonian, the cubic graph is 3-edge-colorable (cubic graphs have even order, so the Hamiltonian cycle is even) and therefore has a CDC. Otherwise G−V(C) is connected and, since G is cubic and C induced, each vertex of C sends exactly one edge to G−V(C), so G−E(C) is connected; applying the source conjecture with S = C (a connected 2-regular subgraph of the 2-connected G) yields a CDC of G, contradicting minimality. Every step is a classical theorem; the chain is rigorous.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
