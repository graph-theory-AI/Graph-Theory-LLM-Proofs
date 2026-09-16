Attack the following open graph-theory problem.

Catalog id: complete_bipartite_subgraphs_of_perfect_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/complete_bipartite_subgraphs_of_perfect_graphs/
Original entry: http://www.openproblemgarden.org/op/complete_bipartite_subgraphs_of_perfect_graphs
Problem attributed to: Fox, Jacob (posted 2008-06-17)

=== Problem statement (OpenProblemGarden) ===
Title: Complete bipartite subgraphs of perfect graphs
Problem Let $ G $ be a perfect graph on $ n $ vertices. Is it true that either $ G $ or $ \bar{G} $ contains a complete bipartite subgraph with bipartition $ (A,B) $ so that $ |A|, |B| \ge n^{1 - o(1)} $ ?

=== Discussion / context (OpenProblemGarden) ===
Every perfect graph on $ n $ vertices either has a clique or an independent set of size $ \ge n^{1/2} $ , so weakening the bound on $ |A| $ , $ |B| $ to $ \lfloor \frac{1}{2} n^{1/2} \rfloor $ gives a true statement. Jacob Fox [F] has proved that every comparability graph $ G $ on $ n $ vertices has a complete bipartite subgraph of size $ \ge c \frac{n}{\log n} $ , and (up to the constant) this is best possible.

=== References listed by OpenProblemGarden ===
- [F] J. Fox, A Bipartite Analogue of Dilworth’s Theorem, Order 23 (2006), 197-209.

=== Catalog page (statement + literature review) ===
Complete bipartite subgraphs of perfect graphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 Fox's 2008 problem asking whether every perfect graph $G$ on $n$ vertices has $G$ or $\bar{G}$ containing a complete bipartite subgraph $K_{A,B}$ with $|A|,|B|\ge n^{1-o(1)}$ appears to remain open. The best-known bound of $\Omega(n/\log n)$ for the special case of comparability graphs (Fox 2006) was extended to a multipartite setting for partial orders by Fox and Pham (2024), but no comparable advance for general perfect graphs has been found in the literature.

 Cited literature (1)

 
 
 
partial A multipartite analogue of Dilworth's Theorem
 (2024)
 

 
 Jacob Fox, Huy Tuan Pham · arXiv preprint · arXiv:2401.00827

Proves a multipartite extension of Fox's 2006 bipartite Dilworth result for partially ordered sets: every poset on $n$ elements contains $k$ subsets each of size $\Omega(n/k^5)$ forming a chain structure, or $\Omega(n/(k^2 \log n))$ that are pairwise incomparable. This advances the comparability-graph case (a subclass of perfect graphs) but does not address general perfect graphs.
 

 

 Reviewer notes. No paper was found that directly solves or makes progress on the perfect-graph problem as stated. The Fox–Pham 2024 paper (arXiv:2401.00827; the corresponding Springer Order 2025 publication at DOI 10.1007/s11083-025-09722-z could not be accessed due to a paywall redirect and is therefore not included in verified_urls) addresses a multipartite Dilworth theorem for posets — i.e., the comparability-graph subcase — and answers Fox's 2006 open question about multipartite generalisations, but leaves the general perfect-graph conjecture untouched. The Springer Combinatorica 2025 paper 'The Largest Subgraph Without A Forbidden Induced Subgraph' appeared in initial search results but was not verified by WebFetch and is therefore not cited. Confidence is medium rather than high because the problem is niche enough that a resolution in a specialised venue might not surface prominently in general web searches.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 162s.
 

Problem. Let $ G $ be a perfect graph on $ n $ vertices. Is it true that either $ G $ or $ \bar{G} $ contains a complete bipartite subgraph with bipartition $ (A,B) $ so that $ |A|, |B| \ge n^{1 - o(1)} $ ?

Keywords:
perfect graph

Discussion

Every perfect graph on $ n $ vertices either has a clique or an independent set of size $ \ge n^{1/2} $ , so weakening the bound on $ |A| $ , $ |B| $ to $ \lfloor \frac{1}{2} n^{1/2} \rfloor $ gives a true statement. Jacob Fox [F] has proved that every comparability graph $ G $ on $ n $ vertices has a complete bipartite subgraph of size $ \ge c \frac{n}{\log n} $ , and (up to the constant) this is best possible.

Bibliography

 [F]
 J. Fox, A Bipartite Analogue of Dilworth’s Theorem , Order 23 (2006), 197-209.
 A Bipartite Analogue of Dilworth’s Theorem
