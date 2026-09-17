Attack the following open graph-theory problem.

Catalog id: triangle_free_strongly_regular_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Algebraic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/triangle_free_strongly_regular_graphs/
Original entry: http://www.openproblemgarden.org/op/triangle_free_strongly_regular_graphs

=== Problem statement (OpenProblemGarden) ===
Title: Triangle free strongly regular graphs
Problem Is there an eighth triangle free strongly regular graph?

=== Discussion / context (OpenProblemGarden) ===
A regular graph $ G $ is strongly regular if there exist integers $ \lambda, \mu $ so that every pair of adjacent vertices have exactly $ \lambda $ common neighbors, and every pair of nonadjacent vertices have exactly $ \mu $ common neighbors. To eliminate degeneracies, we shall further assume that $ \mu \ge 1 $ . If $ G $ is $ k $ -regular and $ |V(G)| = n $ , then we say that $ G $ is a $ (n,k,\lambda,\mu) $ strongly regular graph. There are exactly seven triangle-free strongly regular graphs known: The five cycle, the Petersen Graph , The Clebsch Graph, the Hoffman-Singleton Graph , The Gewirtz Graph, the Higman-Sims Graph, and a $ (77,16,0,4) $ strongly regular subgraph of the Higman-Sims graph. Every Moore Graph of diameter 2 is a triangle-free strongly regular graph, so if there is a 57-regular Moore Graph of diameter 2, this would add another to the list. See Andries Brouwer's graph descriptions for more on these graphs.

=== References listed by OpenProblemGarden ===
- [G] C. D. Godsil, Problems in Algebraic Combinatorics, Electronic Journal of Combinatorics, Volume 2, F1

=== Catalog page (statement + literature review) ===
Triangle free strongly regular graphs — Graph-theory open problems

 
 Status
 open
 high confidence
 

 As of 2026, exactly seven triangle-free strongly regular graphs are known (the 5-cycle, Petersen, Clebsch, Hoffman-Singleton, Gewirtz, Higman-Sims, and the $(77,16,0,4)$ Higman-Sims subgraph), and the question of whether an eighth exists remains open. The most natural candidate is the hypothetical Moore graph of degree 57, which would give a strongly regular graph with parameters $(3250, 57, 0, 1)$; a 2020 claimed proof of its non-existence was shown to be flawed (Faber and Keegan, 2022), and the existence question remains one of the most famous open problems in algebraic graph theory.

 Cited literature (2)

 
 
 
reduction Existence of a Moore graph of degree 57 is still open
 (2022)
 

 
 Vance Faber, Jonathan Keegan · arXiv preprint · arXiv:2210.09577 · doi:10.48550/arXiv.2210.09577

Refutes a 2020 claimed proof that no Moore graph of degree 57 exists, showing the underlying system of equations has solutions in each diagonal block, and reformulates the existence question as: the Moore graph exists if and only if a certain family of permutation systems with specific properties has no solutions.
 

 
 
survey Strongly Regular Graphs
 (2022)
 

 
 Andries E. Brouwer, Hendrik Van Maldeghem · Cambridge University Press

Comprehensive monograph on strongly regular graphs covering all known triangle-free examples and the open problem of whether an eighth exists, including a complete table of feasible parameter sets with up to 1300 vertices.
 

 

 Reviewer notes. Several additional post-2007 papers were found in search results but could not be verified due to HTTP 403 responses from MDPI and ScienceDirect: 'The Moore Graph of Diameter 2 and Degree 57 via Cyclic Derangements' (Smith & Montemanni, Axioms 2026, reportedly proving that constructions using only a cyclic group of derangements are impossible), 'Potential Subgraphs of the Missing Moore Graph' (MDPI 2024), and 'The missing Moore graph as an optimization problem' (ScienceDirect 2023). These could not be cited per protocol. The Faber-Keegan paper is the sole directly verifiable post-2007 contribution; it confirms the problem remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Problem. Is there an eighth triangle free strongly regular graph?

Keywords:
strongly regular · triangle free

Discussion

A regular graph $ G $ is strongly regular if there exist integers $ \lambda, \mu $ so that every pair of adjacent vertices have exactly $ \lambda $ common neighbors, and every pair of nonadjacent vertices have exactly $ \mu $ common neighbors. To eliminate degeneracies, we shall further assume that $ \mu \ge 1 $ . If $ G $ is $ k $ -regular and $ |V(G)| = n $ , then we say that $ G $ is a $ (n,k,\lambda,\mu) $ strongly regular graph. There are exactly seven triangle-free strongly regular graphs known: The five cycle, the Petersen Graph , The Clebsch Graph, the Hoffman-Singleton Graph , The Gewirtz Graph, the Higman-Sims Graph, and a $ (77,16,0,4) $ strongly regular subgraph of the Higman-Sims graph. Every Moore Graph of diameter 2 is a triangle-free strongly regular graph, so if there is a 57-regular Moore Graph of diameter 2, this would add another to the list. See Andries Brouwer's graph descriptions for more on these graphs.

Bibliography

 [G]
 C. D. Godsil, Problems in Algebraic Combinatorics , Electronic Journal of Combinatorics, Volume 2, F1
 Problems in Algebraic Combinatorics

Related conjectures

 
 implied by
 57-regular Moore graph?
 open
 A 57-regular Moore graph of diameter 2 and girth 5 has 3250 vertices and is strongly regular with parameters (3250,57,0,1): girth 5 forces lambda=0 (triangle-free) and diameter 2 with girth 5 forces mu=1. None of the seven known triangle-free strongly regular graphs (C5, Petersen, Clebsch, Hoffman-Singleton, Gewirtz, the (77,16,0,4) graph, Higman-Sims) has these parameters, so its existence yields an eighth, answering the target affirmatively. The target's OPG context states this implication verbatim: 'Every Moore Graph of diameter 2 is a triangle-free strongly regular graph, so if there is a 57-regular Moore graph of diameter 2, this would add another to the list.' Direction correct.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
