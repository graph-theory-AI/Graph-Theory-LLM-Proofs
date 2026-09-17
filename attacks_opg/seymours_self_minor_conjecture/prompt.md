Attack the following open graph-theory problem.

Catalog id: seymours_self_minor_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/seymours_self_minor_conjecture/
Original entry: http://www.openproblemgarden.org/op/seymours_self_minor_conjecture
Problem attributed to: Seymour, Paul D. (posted 2007-05-22)

=== Problem statement (OpenProblemGarden) ===
Title: Seymour's self-minor conjecture
Conjecture Every infinite graph is a proper minor of itself.

=== Discussion / context (OpenProblemGarden) ===
Robertson and Seymour famously proved that the set of all finite graphs is well-quasi-ordered by the minor relation. More precisely, if we let $ G_1,G_2,\ldots $ be an infinite sequence of graphs, then there exist $ i < j $ so that $ G_i $ is a minor of $ G_j $ . Their theory also gives us a rough structure theorem for the family of graphs without a fixed minor - a powerful tool for studying minors in finite graphs. On the other hand, there are still large gaps in our understanding of minors of infinite graphs. For instance, while it is known that Wagner's conjecture does not hold in general for infinite graphs [T], it is possible that countably infinite graphs are well quasi-ordered. The conjecture highlighted above is especially interesting, because (if true) it would imply the well quasi-ordering of finite graphs. Indeed, the well quasi-ordering of finite graphs is equivalent to the statement that every infinite set $ \Omega $ of finite graphs contains two distinct members, one of which is a minor of the other. This latter statement follows from the above conjecture, since we may form a single infinite graph $ G $ from the disjoint union of the graphs in $ \Omega $ , and the proper self-minor of $ G $ gives us a pair of graphs in $ \Omega $ with one a minor of the other.

=== References listed by OpenProblemGarden ===
- [T] R. Thomas, A counterexample to "Wagner's conjecture" for infinite graphs. Math. Proc. Cambridge Philos. Soc. 103 (1988), no. 1, 55--57. MathSciNet

=== Catalog page (statement + literature review) ===
Seymour's self-minor conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture as literally stated (every infinite graph is a proper minor of itself) was already disproved by Oporowski for uncountable graphs before the 2007 OPG posting; the interesting open case concerns countable infinite graphs. Georgakopoulos (2025) established a significant partial result, proving Seymour's self-minor conjecture for rayless graphs of any cardinality as a corollary of his work on better-quasi-ordering under graph minors. The case of countable graphs containing rays remains open.

 Cited literature (1)

 
 
 
partial On better-quasi-ordering under graph minors
 (2025)
 

 
 Agelos Georgakopoulos · arXiv preprint · arXiv:2510.19285

Proves Seymour's self-minor conjecture for rayless graphs of any cardinality (i.e., for every infinite rayless graph $G$ there exists a proper minor embedding $g: G \prec G$), a result that was previously open even for countable graphs.
 

 

 Reviewer notes. Oporowski's counterexample (c. 1990) disproves the general conjecture before the OPG posting date; Georgakopoulos (2025) confirms these counterexamples all contain rays. The Semantic Scholar page for Oporowski's paper failed to load so Oporowski could not be directly verified, but the Egres Open page (verified) states the 1990 counterexample clearly. A result by Pott (2009) on infinite trees is mentioned in secondary sources but could not be located and verified directly, so it is omitted from since_posted. The countable-graphs-with-rays case appears to be the remaining open problem.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. Every infinite graph is a proper minor of itself.

Keywords:
infinite graph · minor

Discussion

Robertson and Seymour famously proved that the set of all finite graphs is well-quasi-ordered by the minor relation. More precisely, if we let $ G_1,G_2,\ldots $ be an infinite sequence of graphs, then there exist $ i < j $ so that $ G_i $ is a minor of $ G_j $ . Their theory also gives us a rough structure theorem for the family of graphs without a fixed minor - a powerful tool for studying minors in finite graphs. On the other hand, there are still large gaps in our understanding of minors of infinite graphs. For instance, while it is known that Wagner's conjecture does not hold in general for infinite graphs [T], it is possible that countably infinite graphs are well quasi-ordered. The conjecture highlighted above is especially interesting, because (if true) it would imply the well quasi-ordering of finite graphs. Indeed, the well quasi-ordering of finite graphs is equivalent to the statement that every infinite set $ \Omega $ of finite graphs contains two distinct members, one of which is a minor of the other. This latter statement follows from the above conjecture, since we may form a single infinite graph $ G $ from the disjoint union of the graphs in $ \Omega $ , and the proper self-minor of $ G $ gives us a pair of graphs in $ \Omega $ with one a minor of the other.

Bibliography

 [T]
 R. Thomas, A counterexample to "Wagner's conjecture" for infinite graphs. Math. Proc. Cambridge Philos. Soc. 103 (1988), no. 1, 55--57. MathSciNet
 MathSciNet
