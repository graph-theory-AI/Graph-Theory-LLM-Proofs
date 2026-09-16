Attack the following open graph-theory problem.

Catalog id: strong_5_cycle_double_cover_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/strong_5_cycle_double_cover_conjecture/
Original entry: http://www.openproblemgarden.org/op/strong_5_cycle_double_cover_conjecture
Problem attributed to: Arthur, Hoffmann-Ostenhof (posted 2010-08-03)

=== Problem statement (OpenProblemGarden) ===
Title: Strong 5-cycle double cover conjecture
Conjecture Let $ C $ be a circuit in a bridgeless cubic graph $ G $ . Then there is a five cycle double cover of $ G $ such that $ C $ is a subgraph of one of these five cycles.

=== Discussion / context (OpenProblemGarden) ===
A cycle in $ G $ is meant to be a $ 2 $ -regular subgraph of $ G $ . A five cycle double cover of $ G $ is a set of five cycles of $ G $ such that every edge of $ G $ is contained in exactly two of these cycles. This conjecture is a combination and thus strengthening of the $ 5 $ -cycle double cover conjecture and the strong cycle double cover conjecture.

=== Catalog page (statement + literature review) ===
Strong 5-cycle double cover conjecture — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The strong 5-cycle double cover conjecture remains open. Hoffmann-Ostenhof (2012) established a necessary and sufficient condition for a 2-regular subgraph to be contained in a 5-cycle double cover of a cubic graph, providing a partial characterisation. Further partial progress includes results showing that when a non-separating cycle is present in a 2-connected cubic graph with suitable structure, a cycle double cover (or 5-cycle double cover) containing that cycle exists, but the full conjecture in generality has not been proved.

 Cited literature (2)

 
 
 
partial A note on 5-cycle double covers
 (2012)
 

 
 Arthur Hoffmann-Ostenhof · Graphs and Combinatorics · arXiv:1209.0096 · doi:10.1007/s00373-012-1169-8

Establishes a necessary and sufficient condition for a 2-regular subgraph to be contained in a 5-cycle double cover of a bridgeless cubic graph, directly relevant to the strong 5-CDC conjecture.
 

 
 
partial Cycle double covers and non-separating cycles
 (2017)
 

 
 Arthur Hoffmann-Ostenhof, Cun-Quan Zhang, Zhang Zhang · arXiv preprint · arXiv:1711.10614

Proves that every 2-connected cubic graph admitting a decomposition into a spanning tree and a 2-regular subgraph C with at most 3 circuits has a cycle double cover containing C, giving a partial approach toward the strong CDC and strong 5-CDC conjectures.
 

 

 Reviewer notes. A 2025 Discrete Mathematics paper 'Non-separating cycles and 5-cycle double covers' (ScienceDirect pii/S0012365X25001232) appears to extend the non-separating-cycle approach to 5-CDCs, but direct access returned 403; it could not be verified and is not cited. arXiv:1607.04768 appeared in searches but is about a different Hoffmann-Ostenhof conjecture (graph decomposition into spanning tree + matching + cycles). The 2026 paper arXiv:2605.01410 and the 2025 paper arXiv:2511.07285 address the general CDC conjecture approximately but do not tackle the strong 5-CDC conjecture specifically. The Springer page for the 2012 'Strong 5-Cycle Double Covers of Graphs' paper (10.1007/s00373-012-1266-8) redirected to authentication; it could not be verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. Let $ C $ be a circuit in a bridgeless cubic graph $ G $ . Then there is a five cycle double cover of $ G $ such that $ C $ is a subgraph of one of these five cycles.

Keywords:
cycle cover

Discussion

A cycle in $ G $ is meant to be a $ 2 $ -regular subgraph of $ G $ . A five cycle double cover of $ G $ is a set of five cycles of $ G $ such that every edge of $ G $ is contained in exactly two of these cycles. This conjecture is a combination and thus strengthening of the $ 5 $ -cycle double cover conjecture and the strong cycle double cover conjecture.

Related conjectures

 
 implies
 (m,n)-cycle covers
 partial
 The source context states it strengthens the 5-cycle double cover conjecture, and the target's chart labels the (5,2) entry '5CDC conj', identifying the general (5,2)-cover conjecture with the 5-CDC conjecture. Chain: any nonempty bridgeless cubic graph has a circuit C; strong 5-CDC applied to C gives a 5-CDC of that graph. The general bridgeless case reduces to cubic by Fleischner's splitting lemma (expand vertices of degree >=4 preserving bridgelessness); restricting each of the 5 even subgraphs of the cubic expansion to E(G) is even at every original vertex (parity argument across the gadget) and covers each original edge exactly twice, yielding a (5,2)-cycle-cover of G. This is the standard reduction of 5-CDC to cubic graphs. Direction as claimed.
 

 
 implies
 Cycle double cover conjecture
 partial
 Strong 5-CDC applied to any circuit of a bridgeless cubic graph yields a 5-cycle double cover, hence a CDC, of every bridgeless cubic graph (every such nonempty graph contains a circuit). The CDC conjecture for general bridgeless graphs reduces to cubic graphs via vertex splitting, as stated explicitly in the target's OPG context ('problem may be reduced to cubic graphs'). Decomposing the five even subgraphs into edge-disjoint circuits gives the required list of cycles covering each edge exactly twice. Direction as claimed (source is a double strengthening of CDC, per its own context).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
