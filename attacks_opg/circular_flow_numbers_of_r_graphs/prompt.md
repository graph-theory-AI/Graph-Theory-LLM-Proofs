Attack the following open graph-theory problem.

Catalog id: circular_flow_numbers_of_r_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/circular_flow_numbers_of_r_graphs/
Original entry: http://www.openproblemgarden.org/op/circular_flow_numbers_of_r_graphs
Problem attributed to: Steffen, Eckhard (posted 2015-08-06)

=== Problem statement (OpenProblemGarden) ===
Title: Circular flow numbers of $r$-graphs
A nowhere-zero $ r $ -flow $ (D(G),\phi) $ on $ G $ is an orientation $ D $ of $ G $ together with a function $ \phi $ from the edge set of $ G $ into the real numbers such that $ 1 \leq |\phi(e)| \leq r-1 $ , for all $ e \in E(G) $ , and $ \sum_{e \in E^+(v)}\phi(e) = \sum_{e \in E^-(v)}\phi(e), \textrm{ for all } v \in V(G) $ . A $ (2t+1) $ -regular graph $ G $ is a $ (2t+1) $ -graph if $ |\partial_G(X)| \geq 2t+1 $ for every $ X \subseteq V(G) $ with $ |X| $ odd. Conjecture Let $ t > 1 $ be an integer. If $ G $ is a $ (2t+1) $ -graph, then $ F_c(G) \leq 2 + \frac{2}{t} $ .

=== Discussion / context (OpenProblemGarden) ===
Since every $ (2t+1) $ -regular class 1 graph is a $ (2t+1) $ -graph, the truth of this conjecture would imply the truth of the conjecture on the circular flow number of regular class 1 graphs. If it is true for even $ t $ , say $ t=2t' $ , then Jaeger's modular orientation conjecture is true for $ (4t'+1) $ -regular graphs and hence, by a result of Jaeger, it would imply the truth of Tutte's 5-flow conjecture. For $ t=2 $ it is Tutte's 3-flow conjecture.

=== References listed by OpenProblemGarden ===
- *[ES_2015]E. Steffen, Edge-colorings and circular flow numbers on regular graphs, J. Graph Theory 79, 1–7, 2015

=== Catalog page (statement + literature review) ===
Circular flow numbers of $r$-graphs — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 The conjecture was effectively disproved by Mattiolo and Steffen (2022), who constructed $(2t+1)$-regular class-1 graphs with circular flow number exceeding $2 + 2/t$ for $t = 4k+2$ ($k \geq 1$). The OPG discussion itself notes that every $(2t+1)$-regular class-1 graph is a $(2t+1)$-graph (r-graph), so these are also counterexamples to the stated conjecture; the same paper confirmed that $2 + 2/(2t-1)$ is the infimum of circular flow numbers for $(2t+1)$-regular class-2 graphs.

 Cited literature (1)

 
 
 
counterexample Edge colorings and circular flows on regular graphs
 (2022)
 

 
 Davide Mattiolo, Eckhard Steffen · Journal of Graph Theory · arXiv:2001.02484 · doi:10.1002/jgt.22746

Constructs $(2t+1)$-regular class-1 graphs with $F_c > 2+2/t$ for $t = 4k+2$ ($k \geq 1$), disproving the class-1 version of Steffen's conjecture; since the OPG itself observes that every $(2t+1)$-regular class-1 graph is a $(2t+1)$-graph, these serve as counterexamples to the r-graph conjecture as well, and the paper also confirms that $2+2/(2t-1)$ is the infimum of circular flow numbers for $(2t+1)$-regular class-2 graphs.
 

 

 Reviewer notes. The disproof is indirect but rigorous: it follows from the OPG's own stated implication (every $(2t+1)$-regular class-1 graph is a $(2t+1)$-graph) together with Mattiolo-Steffen's class-1 counterexamples for t = 4k+2. The arXiv page verifies the abstract's disproof claim and lists the journal version as Journal of Graph Theory 99 (2022), 399-413, DOI 10.1002/jgt.22746. A SIAM 2022 paper by Li, Li, Wang ('Flow index of regular class I graphs') appeared in searches but its PDF was unreadable; it may contain additional relevant results. The case t = 2 (Tutte's 3-flow conjecture) was explicitly noted as an instance of the OPG conjecture and remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. Let $ t > 1 $ be an integer. If $ G $ is a $ (2t+1) $ -graph, then $ F_c(G) \leq 2 + \frac{2}{t} $ .

Keywords:
flow conjectures · nowhere-zero flows

Discussion

Since every $ (2t+1) $ -regular class 1 graph is a $ (2t+1) $ -graph, the truth of this conjecture would imply the truth of the conjecture on the circular flow number of regular class 1 graphs. If it is true for even $ t $ , say $ t=2t' $ , then Jaeger's modular orientation conjecture is true for $ (4t'+1) $ -regular graphs and hence, by a result of Jaeger, it would imply the truth of Tutte's 5-flow conjecture. For $ t=2 $ it is Tutte's 3-flow conjecture.

Bibliography

★ [ES_2015]
 E. Steffen, Edge-colorings and circular flow numbers on regular graphs, J. Graph Theory 79, 1–7, 2015

Related conjectures

 
 implies
 3-flow conjecture
 partial
 Steffen's source paper states explicitly: "Tutte's 3-flow conjecture is equivalent to the statement that Fc(G) <= 3 for every 5-graph G." The t=2 instance of the source conjecture is exactly that statement (2+2/t = 3, 5-graphs). Since the source conjecture asserts the bound for ALL t>1, its truth contains the t=2 case, which is equivalent to (hence implies) the 3-flow conjecture. The converse fails: the 3-flow conjecture says nothing about t>2. So the relation is a strict one-way implication, not equivalence, matching the OPG context "For t=2 it is Tutte's 3-flow conjecture." (Note the source is now disproved for large even t, but the t=2 case and thus the implication route remain intact.)
 

 
 implies
 5-flow conjecture
 partial
 Explicit in the OPG context (written by Steffen): truth for even t implies Jaeger's conjecture for (4t'+1)-regular graphs and hence, by a result of Jaeger, the 5-flow conjecture. Self-contained check via t=4: the 5-flow conjecture reduces to 3-edge-connected cubic graphs G. Tripling every edge gives a 9-regular graph 3G whose cuts are 3x those of G, hence >= 9, so 3G is a 9-graph. Fc(3G) <= 2+2/4 = 5/2 is equivalent to a mod-5 orientation of 3G; the net contribution of each parallel triple (three +-1's) to the corresponding edge of G lies in {+-1,+-3}, never 0 mod 5, giving a nowhere-zero Z5-flow on G. Jaeger's reduction (9-edge-connected circular 5/2-flows imply the 5-flow conjecture) is documented in arXiv:1812.09833.
 

 
 implies
 Circular flow number of regular class 1 graphs
 disproved
 Hypothesis-class containment, stated explicitly in the source's OPG context: every (2t+1)-regular class 1 graph decomposes into 2t+1 perfect matchings, and each perfect matching must contain an edge of every odd cut ∂(X) (a matching covering an odd-cardinality X cannot match X internally), so |∂(X)| ≥ 2t+1 and the graph is a (2t+1)-graph. Hence the r-graph bound F_c ≤ 2+2/t restricted to class 1 regular graphs gives the target for all t > 1. The residual t = 1 case of the target is a known theorem (3-edge-colorable cubic graphs have F_c ≤ 4, noted in the target's context), so the implication holds. Both are now disproved, consistent with the direction.
 

 
 implies
 Jaeger's modular orientation conjecture
 disproved
(plausible) What is explicitly established (Steffen, arXiv:1310.8441 and the OPG context) is only: truth for even t=2t' implies Jaeger's conjecture restricted to (4t'+1)-REGULAR graphs (a 4t'-edge-connected (4t'+1)-regular graph is a (4t'+1)-graph, since its odd cuts are odd hence >= 4t'+1). The target as stated covers all 4k-edge-connected graphs, so the full implication needs the reduction of Jaeger's conjecture to its regular restriction. That equivalence is documented for k=1 (both equal the 3-flow conjecture) and is treated as folklore for general k (papers state Jaeger's conjecture in the regular form; the Han-Li-Wu-Zhang counterexamples are (4p+1)-regular and disprove both statements simultaneously), but I found no explicit general-k equivalence proof, so I stop short of confirming the full implication.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
