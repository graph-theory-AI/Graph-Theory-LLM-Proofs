Attack the following open graph-theory problem.

Catalog id: covering_powers_of_cycles_with_equivalence_subgraphs
Source: OpenProblemGarden (importance: Low ✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/covering_powers_of_cycles_with_equivalence_subgraphs/
Original entry: http://www.openproblemgarden.org/op/covering_powers_of_cycles_with_equivalence_subgraphs

=== Problem statement (OpenProblemGarden) ===
Title: Covering powers of cycles with equivalence subgraphs
Conjecture Given $ k $ and $ n $ , the graph $ C_{n}^k $ has equivalence covering number $ \Omega(k) $ .

=== Discussion / context (OpenProblemGarden) ===
Given a graph $ G $ , a subgraph $ H $ of $ G $ is an equivalence subgraph of $ G $ if $ H $ a disjoint union of cliques. The quivalence covering number of $ G $ , denoted $ eq(G) $ , is the least number of equivalence subgraphs needed to cover the edges of $ G $ . This problem has been studied by various people since the 80s [A]. For line graphs, the equivalence covering number is known to within a constant factor [EGK]. It is therefore tempting to examine the situation for quasi-line graphs and claw-free graphs. Powers of cycles are perhaps the simplest interesting class of claw-free graphs that are not necessarily line graphs. However, even for $ n $ very large compared to $ k $ , no upper bound is known beyond trivial linear bounds of order $ \Theta(k) $ . Furthermore, it is not even certain that a nontrivial lower bound (i.e. going to infinity as $ k $ goes to infinity) is known. It is possible that this can be related somehow to a known result, but for now it seems at least superficially that this problem is wide open.

=== References listed by OpenProblemGarden ===
- [A] N. Alon, Covering graphs with the minimum number of equivalence relations, Combinatorica 6 (1986) 201–206.
- [EGK] L. Esperet, J. Gimbel, A. King, Covering line graphs with equivalence relations, Discrete Applied Mathematics Volume 158, Issue 17, 28 October 2010, Pages 1902-1907.

=== Catalog page (statement + literature review) ===
Covering powers of cycles with equivalence subgraphs — Graph-theory open problems

 
 Status
 open
 low confidence
 

 The conjecture that $\mathrm{eq}(C_n^k) = \Omega(k)$ for $n$ large relative to $k$ was described as 'wide open' at the time of posting, with no known non-trivial lower bound and only trivial $\Theta(k)$ upper bounds. My literature search found no post-2011 papers specifically addressing the equivalence covering number of powers of cycles or resolving this conjecture.

 Reviewer notes. Douglas West's research page (dwest.web.illinois.edu/regs/eqcov.html, dated 2010) frames this as an open problem, asking whether eq(C_n^k) is unbounded for fixed k and whether a sublinear upper bound exists — matching the OPG statement closely. The page predates the OPG posting and no updates were visible. A 2016/2018 paper by Javadi and Hajebi (arXiv:1608.07723, J. Graph Theory) proves that the edge clique cover number cc(C_n^k) = n for powers of cycles, but this is a different quantity from the equivalence covering number eq(G) (every clique cover is an equivalence cover, but not vice versa), so it does not address the conjecture. The ScienceDirect page for the 2020 claw-free clique coverings paper returned HTTP 403 and could not be verified or cited.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. Given $ k $ and $ n $ , the graph $ C_{n}^k $ has equivalence covering number $ \Omega(k) $ .

Discussion

Given a graph $ G $ , a subgraph $ H $ of $ G $ is an equivalence subgraph of $ G $ if $ H $ a disjoint union of cliques. The quivalence covering number of $ G $ , denoted $ eq(G) $ , is the least number of equivalence subgraphs needed to cover the edges of $ G $ . This problem has been studied by various people since the 80s [A]. For line graphs, the equivalence covering number is known to within a constant factor [EGK]. It is therefore tempting to examine the situation for quasi-line graphs and claw-free graphs. Powers of cycles are perhaps the simplest interesting class of claw-free graphs that are not necessarily line graphs. However, even for $ n $ very large compared to $ k $ , no upper bound is known beyond trivial linear bounds of order $ \Theta(k) $ . Furthermore, it is not even certain that a nontrivial lower bound (i.e. going to infinity as $ k $ goes to infinity) is known. It is possible that this can be related somehow to a known result, but for now it seems at least superficially that this problem is wide open.

Bibliography

 [A]
 N. Alon, Covering graphs with the minimum number of equivalence relations, Combinatorica 6 (1986) 201–206.

 [EGK]
 L. Esperet, J. Gimbel, A. King, Covering line graphs with equivalence relations, Discrete Applied Mathematics Volume 158, Issue 17, 28 October 2010, Pages 1902-1907.
