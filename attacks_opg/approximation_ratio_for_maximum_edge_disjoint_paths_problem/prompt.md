Attack the following open graph-theory problem.

Catalog id: approximation_ratio_for_maximum_edge_disjoint_paths_problem
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/approximation_ratio_for_maximum_edge_disjoint_paths_problem/
Original entry: http://www.openproblemgarden.org/op/approximation_ratio_for_maximum_edge_disjoint_paths_problem
Problem attributed to: Bentz, Cedric (posted 2010-04-18)

=== Problem statement (OpenProblemGarden) ===
Title: Approximation Ratio for Maximum Edge Disjoint Paths problem
Conjecture Can the approximation ratio $ O(\sqrt{n}) $ be improved for the Maximum Edge Disjoint Paths problem (MaxEDP) in planar graphs or can an inapproximability result stronger than $ \mathcal{APX} $ -hardness?

=== Discussion / context (OpenProblemGarden) ===
Assume a flow graph $ G = (V, E) $ with $ n $ vertices and $ m $ edges. Each edge has a capacity function $ c: E \rightarrow \mathbb{Z}^+ $ ( Flow network ). The graph contains a list $ \mathcal{N} $ of terminal vertices called sources ( $ s_i $ ) and sinks ( $ s_i' $ ). Each pair ( $ s_i, s_i' $ ) defines a net or commodity. A Multiflow is a way of routing commodities from their sources to the respective sinks while ensuring that the flow of each commodity is conserved at each non-terminal vertex and that the sum of the flows of all commodities through an edge does not exceed the capacity of the edge. The Maximum Integer Multiflow problem (MaxIMF) seeks to maximize the number of flow units routed between the nets in the graph. The Maximum Edge Disjoint Paths (MaxEDP) problem seeks to find the maximum number of disjoint paths between the sources and sinks. When the capacities for all edges are set to one, MaxIMF simplifies into the MaxEDP problem. Bentz provides an algorithm to find the MaxEDP with a proven approximation ratio ( Approximation and integrality gap ) of $ O(\sqrt{n}) $ . Can the approximation ratio be improved for MaxEDP in planar graphs, or can an inapproximability result stronger than $ \mathcal{APX} $ -hardness be proved for this problem? And what about the general graphs?

=== References listed by OpenProblemGarden ===
- Cédric Bentz, Edge disjoint paths and max integral muliflow/min multicut theorems in planar graphs, Electronic Notes in Discrete Mathematics 22 (2005), 55–60

=== Catalog page (statement + literature review) ===
Approximation Ratio for Maximum Edge Disjoint Paths problem — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Since the problem was posted, two major developments have occurred. First, Chuzhoy, Kim, and Nimavat (STOC 2018 / Theory of Computing 2021) proved $2^{\Omega(\log^{1-\varepsilon} n)}$-hardness for MaxEDP even in wall graphs (subcubic planar graphs), establishing an inapproximability result far stronger than $\mathcal{APX}$-hardness and thus answering the second half of the posed question affirmatively. Second, Huang, Mari, Mathieu, Schewior, and Vygen (SIAM J. Comput. 2020) achieved a constant-factor approximation for the *fully planar* variant of MaxEDP (where the supply graph together with the demand edges forms a planar graph), improving the $O(\sqrt{n})$ ratio for that special case; however, the $O(\sqrt{n})$ approximation ratio for MaxEDP in general planar graphs (without the fully-planar restriction) remains the best known upper bound.

 Cited literature (3)

 
 
 
partial Almost Polynomial Hardness of Node-Disjoint Paths in Grids
 (2021)
 

 
 Julia Chuzhoy, David H. K. Kim, Rachit Nimavat · Theory of Computing

Proves $2^{\Omega(\log^{1-\varepsilon} n)}$-hardness for NDP and, explicitly, for MaxEDP even in wall graphs (3-regular planar graphs), giving an inapproximability result far stronger than $\mathcal{APX}$-hardness for MaxEDP in planar graphs.
 

 
 
partial An Approximation Algorithm for Fully Planar Edge-Disjoint Paths
 (2020)
 

 
 Chien-Chung Huang, Mathieu Mari, Claire Mathieu, Kevin Schewior, Jens Vygen · SIAM Journal on Computing · arXiv:2001.01715 · doi:10.1137/20M1319401

Achieves a constant-factor approximation (and proves a constant integrality gap for the LP relaxation) for MaxEDP on fully planar instances, where the supply graph together with the demand edges forms a planar graph—a special but natural subclass of planar MaxEDP instances.
 

 
 
partial Improved Approximation for Node-Disjoint Paths in Planar Graphs
 (2016)
 

 
 Julia Chuzhoy, David H. K. Kim, Shi Li · Proceedings of the 48th Annual ACM STOC · arXiv:1603.05520

Breaks the $O(\sqrt{n})$ barrier for the closely related Node-Disjoint Paths (NDP) problem in planar graphs, achieving an $\tilde{O}(n^{9/19})$ approximation; the result is for NDP only and does not directly extend to MaxEDP (edge-disjoint).
 

 

 Reviewer notes. The Springer journal pages (Combinatorica, Mathematical Programming) returned authentication redirects and could not be fetched; the corresponding papers are not cited. The hardness result in the Chuzhoy–Kim–Nimavat ToC paper is stated for wall graphs (a subclass of planar graphs), which suffices to answer the planarity question, but the paper's primary focus is grid graphs and the NDP problem—the EDP extension is stated in the abstract. The Chuzhoy–Kim–Li (2016) Õ(n^{9/19}) result is for NDP, not MaxEDP; it is included as context because it breaks O(√n) for the closely related problem and introduced the LP techniques later useful in this line of work. No post-2010 paper improving O(√n) for MaxEDP in general (unrestricted) planar graphs without congestion was found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 242s.
 

Conjecture. Can the approximation ratio $ O(\sqrt{n}) $ be improved for the Maximum Edge Disjoint Paths problem (MaxEDP) in planar graphs or can an inapproximability result stronger than $ \mathcal{APX} $ -hardness?

Keywords:
approximation algorithms · Disjoint paths · planar graph · polynomial algorithm

Discussion

Assume a flow graph $ G = (V, E) $ with $ n $ vertices and $ m $ edges. Each edge has a capacity function $ c: E \rightarrow \mathbb{Z}^+ $ ( Flow network ). The graph contains a list $ \mathcal{N} $ of terminal vertices called sources ( $ s_i $ ) and sinks ( $ s_i' $ ). Each pair ( $ s_i, s_i' $ ) defines a net or commodity. A Multiflow is a way of routing commodities from their sources to the respective sinks while ensuring that the flow of each commodity is conserved at each non-terminal vertex and that the sum of the flows of all commodities through an edge does not exceed the capacity of the edge. The Maximum Integer Multiflow problem (MaxIMF) seeks to maximize the number of flow units routed between the nets in the graph. The Maximum Edge Disjoint Paths (MaxEDP) problem seeks to find the maximum number of disjoint paths between the sources and sinks. When the capacities for all edges are set to one, MaxIMF simplifies into the MaxEDP problem. Bentz provides an algorithm to find the MaxEDP with a proven approximation ratio ( Approximation and integrality gap ) of $ O(\sqrt{n}) $ . Can the approximation ratio be improved for MaxEDP in planar graphs, or can an inapproximability result stronger than $ \mathcal{APX} $ -hardness be proved for this problem? And what about the general graphs?

Bibliography

 [?]
 Cédric Bentz, Edge disjoint paths and max integral muliflow/min multicut theorems in planar graphs, Electronic Notes in Discrete Mathematics 22 (2005), 55–60
