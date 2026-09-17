Attack the following open graph-theory problem.

Catalog id: complexity_of_the_h_factor_problem
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/complexity_of_the_h_factor_problem/
Original entry: http://www.openproblemgarden.org/op/complexity_of_the_h_factor_problem
Problem attributed to: Kühn, Daniella, Osthus, Deryk (posted 2013-03-05)

=== Problem statement (OpenProblemGarden) ===
Title: Complexity of the H-factor problem.
An $ H $ -factor in a graph $ G $ is a set of vertex-disjoint copies of $ H $ covering all vertices of $ G $ . Problem Let $ c $ be a fixed positive real number and $ H $ a fixed graph. Is it NP-hard to determine whether a graph $ G $ on $ n $ vertices and minimum degree $ cn $ contains and $ H $ -factor?

=== Discussion / context (OpenProblemGarden) ===
The answer is positive for cliques and a few other graphs [KO06]. If we remove the minimum degree condition, the problem is NP-complete if and only if $ H $ has a component which contains at least 3 vertices, as shown by Hell and Kirkpatrick [HK].

=== References listed by OpenProblemGarden ===
- [HK] P. Hell and D.G. Kirkpatrick, On the complexity of general graph factor problems, SIAM J. Computing 12 (1983), 601-609.
- [KO06] D. Kühn and D. Osthus, Critical chromatic number and the complexity of perfect packings in graphs, Proceedings of the 17th ACM-SIAM Symposium on Discrete Algorithms (SODA), 2006.
- *[KO09] D. Kühn and D. Osthus, The minimum degree threshold for perfect graph packings, Combinatorica 29 (2009), 65-107.

=== Catalog page (statement + literature review) ===
Complexity of the H-factor problem. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Han and Treglown (JCTB 2020) provide a general tool that resolves much of the question: for any graph $H$ and any $\gamma>0$, deciding whether an $n$-vertex graph $G$ with $\delta(G)\ge(1-1/\chi_{cr}(H)+\gamma)n$ contains a perfect $H$-packing is polynomial-time solvable, while a complementary hardness result of Kühn and Osthus (TAMC 2017) shows that for many $H$ (including all complete multipartite $H$ whose second smallest color class has size at least 2) the problem becomes NP-complete just below this critical threshold, so that a sharp $P$/NP-hard dichotomy in the parameter $c$ holds for those $H$. A complete dichotomy at the critical threshold for all graphs $H$ is, however, still not fully established.

 Cited literature (2)

 
 
 
partial The complexity of perfect matchings and packings in dense hypergraphs
 (2020)
 

 
 Jie Han, Andrew Treglown · Journal of Combinatorial Theory, Series B · arXiv:1609.06147 · doi:10.1016/j.jctb.2019.06.004

Gives, for every graph $F$, a minimum degree condition under which deciding existence of a perfect $F$-packing is polynomial-time solvable, and shows the threshold is best possible in many cases (lowering it makes the decision problem NP-complete), thereby largely answering the Kühn–Osthus question.
 

 
 
partial The Complexity of Perfect Packings in Dense Graphs
 (2017)
 

 
 Daniela Kühn, Deryk Osthus · Theory and Applications of Models of Computation (TAMC 2017), LNCS 10185 · doi:10.1007/978-3-319-55911-7_21

Provides the matching NP-hardness side, closing a long-standing hardness gap for all complete multipartite graphs $H$ whose second smallest color class has size at least 2, so that the polynomial/NP-hard transition at the critical chromatic threshold is sharp for these $H$.
 

 

 Reviewer notes. Han–Treglown (arXiv:1609.06147, JCTB 2020) explicitly state that their minimum degree threshold for polynomial solvability is, in many cases, best possible: lowering it makes the decision problem NP-complete. Kühn–Osthus's TAMC 2017 chapter supplies the matching hardness for complete multipartite $H$ whose second-smallest color class has size at least 2, closing the gap for those $H$. Together these substantially answer the OPG question affirmatively in the regime $c<1-1/\chi_{cr}(H)$ for many $H$, and negatively (problem is in P) for $c>1-1/\chi_{cr}(H)$. The Springer page for the Kühn–Osthus chapter required login to inspect the abstract, but its existence, authors, year, and content (closing the hardness gap) are corroborated across multiple independent search results and the Han–Treglown abstract; no arXiv preprint located. A fully tight dichotomy at the critical threshold for every graph $H$ does not yet appear in the literature, so the original problem as stated is best classified as having strong partial progress rather than fully resolved.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Problem. Let $ c $ be a fixed positive real number and $ H $ a fixed graph. Is it NP-hard to determine whether a graph $ G $ on $ n $ vertices and minimum degree $ cn $ contains and $ H $ -factor?

Discussion

The answer is positive for cliques and a few other graphs [KO06]. If we remove the minimum degree condition, the problem is NP-complete if and only if $ H $ has a component which contains at least 3 vertices, as shown by Hell and Kirkpatrick [HK].

Bibliography

 [HK]
 P. Hell and D.G. Kirkpatrick, On the complexity of general graph factor problems, SIAM J. Computing 12 (1983), 601-609.

 [KO06]
 D. Kühn and D. Osthus, Critical chromatic number and the complexity of perfect packings in graphs, Proceedings of the 17th ACM-SIAM Symposium on Discrete Algorithms (SODA), 2006.

★ [KO09]
 D. Kühn and D. Osthus, The minimum degree threshold for perfect graph packings, Combinatorica 29 (2009), 65-107.
