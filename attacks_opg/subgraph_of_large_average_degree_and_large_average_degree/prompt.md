Attack the following open graph-theory problem.

Catalog id: subgraph_of_large_average_degree_and_large_average_degree
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/subgraph_of_large_average_degree_and_large_average_degree/
Original entry: http://www.openproblemgarden.org/op/subgraph_of_large_average_degree_and_large_average_degree
Problem attributed to: Thomassen, Carsten (posted 2013-03-05)

=== Problem statement (OpenProblemGarden) ===
Title: Subgraph of large average degree and large girth.
Conjecture For all positive integers $ g $ and $ k $ , there exists an integer $ d $ such that every graph of average degree at least $ d $ contains a subgraph of average degree at least $ k $ and girth greater than $ g $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is true for regular graphs as observed by Alon (see [KO]). The case $ g\leq 4 $ was proved in [KO].

=== References listed by OpenProblemGarden ===
- [KO] D. Kühn and D. Osthus, Every graph of sufficiently large average degree contains a C4-free subgraph of large average degree, Combinatorica, 24 (2004), 155-162.
- *[T] C. Thomassen, Girth in graphs, J. Combin. Theory B 35 (1983), 129–141.

=== Catalog page (statement + literature review) ===
Subgraph of large average degree and large girth. — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 Thomassen's conjecture remains open for $g \geq 5$. The case $g \leq 4$ — finding a $C_4$-free subgraph of large average degree — was established before the 2013 posting by Kühn and Osthus; since then, Montgomery, Pokrovskiy, and Sudakov (2021) improved the required average degree bound from doubly-exponential to singly-exponential in $t$, showing $2^{ct^2 \log t}$ suffices. No further values of $g$ are known to have been resolved as of this review.

 Cited literature (1)

 
 
 
partial C4-free subgraphs with large average degree
 (2021)
 

 
 Richard Montgomery, Alexey Pokrovskiy, Benny Sudakov · Israel Journal of Mathematics · arXiv:2004.03564 · doi:10.1007/s11856-021-2236-8

Proves that any graph of average degree at least $2^{ct^2\log t}$ contains a $C_4$-free subgraph of average degree at least $t$, reducing the doubly-exponential Kühn–Osthus bound to singly-exponential for the $g=4$ case of Thomassen's conjecture, and establishes a matching lower bound of $t^{3-o(1)}$.
 

 

 Reviewer notes. The conjecture is open for g ≥ 5 (girth > 5). The g = 4 case (C4-free) was known pre-2013; Montgomery–Pokrovskiy–Sudakov (2021) improved it post-2013. Some search-result summaries mentioned a 'girth at least 6' case being settled, but no specific post-2013 paper could be identified or verified for this; the claim may arise from notational ambiguity (different papers parameterize the conjecture as 'girth ≥ g' vs. 'girth > g') or from the Kühn–Osthus 2004 result being described differently. Dellamonica and Rödl proved a variant for all g with an extra log log Δ(G) dependence (insufficient for Thomassen's conjecture), but no arXiv preprint or journal paper could be located to verify this. A 2025 paper by Christoph, Janzer, Petrova, and Steiner (arXiv:2510.11311) extends Thomassen's conjecture to directed graphs and shows that the direct digraph extension fails, while confirming the undirected problem remains of active interest. Janzer, Sudakov, and Tomon (2022, Combinatorica 2024, arXiv:2207.02170) studied small dense subgraphs but without girth constraints; not directly relevant. Search query budget exceeded (6 queries used against a limit of 4); some leads on g = 5 case were not fully pursued.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. For all positive integers $ g $ and $ k $ , there exists an integer $ d $ such that every graph of average degree at least $ d $ contains a subgraph of average degree at least $ k $ and girth greater than $ g $ .

Discussion

This conjecture is true for regular graphs as observed by Alon (see [KO]). The case $ g\leq 4 $ was proved in [KO].

Bibliography

 [KO]
 D. Kühn and D. Osthus, Every graph of sufficiently large average degree contains a C4-free subgraph of large average degree, Combinatorica, 24 (2004), 155-162.

★ [T]
 C. Thomassen, Girth in graphs, J. Combin. Theory B 35 (1983), 129–141.

Related conjectures

 
 implies
 High-chromatic subgraph with large average degree
 open
 Standard fact: a graph with chromatic number ≥ c contains a c-critical subgraph, which has minimum (hence average) degree ≥ c−1. Given k and g, let d = d(k,g) be the constant from Thomassen's conjecture applied with girth parameter g. Set c(k,g) = d+1. If χ(G) ≥ c(k,g), G has a subgraph of average degree ≥ d, which by Thomassen contains a subgraph of average degree ≥ k and girth > g, in particular girth ≥ g as the target requires. The hypothesis class of the target (large chromatic number) maps into the hypothesis class of the source (large average degree) with the same conclusion, so Thomassen's conjecture is the stronger statement, matching the claimed direction. The target's context confirms it was proposed as a weakening of Thomassen's conjecture.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
