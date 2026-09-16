Attack the following open graph-theory problem.

Catalog id: circular_flow_number_of_regular_class_1_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/circular_flow_number_of_regular_class_1_graphs/
Original entry: http://www.openproblemgarden.org/op/circular_flow_number_of_regular_class_1_graphs
Problem attributed to: Steffen, Eckhard (posted 2015-08-05)

=== Problem statement (OpenProblemGarden) ===
Title: Circular flow number of regular class 1 graphs
A nowhere-zero $ r $ -flow $ (D(G),\phi) $ on $ G $ is an orientation $ D $ of $ G $ together with a function $ \phi $ from the edge set of $ G $ into the real numbers such that $ 1 \leq |\phi(e)| \leq r-1 $ , for all $ e \in E(G) $ , and $ \sum_{e \in E^+(v)}\phi(e) = \sum_{e \in E^-(v)}\phi(e), \textrm{ for all } v \in V(G) $ . The circular flow number of $ G $ is inf $ \{ r | G $ has a nowhere-zero $ r $ -flow $ \} $ , and it is denoted by $ F_c(G) $ . A graph with maximum vertex degree $ k $ is a class 1 graph if its edge chromatic number is $ k $ . Conjecture Let $ t \geq 1 $ be an integer and $ G $ a $ (2t+1) $ -regular graph. If $ G $ is a class 1 graph, then $ F_c(G) \leq 2 + \frac{2}{t} $ .

=== Discussion / context (OpenProblemGarden) ===
The conjecture is true for $ t=1 $ , i.e. for cubic graphs. It says, that the circular flow number of $ (2t+1) $ -regular class 1 graphs is bounded by the circular flow number of the complete graph on $ 2t+2 $ vertices.

=== References listed by OpenProblemGarden ===
- [ES_2001] E. Steffen, Circular flow numbers of regular multigraphs, J. Graph Theory 36, 24 – 34 (2001)
- *[ES_2015] E. Steffen, Edge-colorings and circular flow numbers on regular graphs, J. Graph Theory 79, 1–7, 2015

=== Catalog page (statement + literature review) ===
Circular flow number of regular class 1 graphs — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 Mattiolo and Steffen (J. Graph Theory, 2022) explicitly disproved Steffen's conjecture by constructing $(2t+1)$-regular class 1 graphs with circular flow number greater than $2+\frac{2}{t}$; the counterexamples are built from a family of graphs originally used to disprove Jaeger's Circular Flow Conjecture and apply to $t = 4k+2$ for all integers $k \geq 1$. A subsequent SIAM (2022) paper by Li, Li, and Wang on the 'flow index of regular Class I graphs' extends the family of counterexample values of $t$ further; however, the conjecture remains true for $t=1$ (cubic graphs), and the exact set of $t$ for which it holds is still under investigation.

 Cited literature (1)

 
 
 
counterexample Edge colorings and circular flows on regular graphs
 (2022)
 

 
 Davide Mattiolo, Eckhard Steffen · Journal of Graph Theory · arXiv:2001.02484 · doi:10.1002/jgt.22746

Disproves the conjecture that every $(2t+1)$-regular class 1 graph has circular flow number at most $2+2/t$, and also confirms that $2+2/(2t-1)$ is the infimum of circular flow numbers for $(2t+1)$-regular class 2 graphs.
 

 

 Reviewer notes. A second 2022 paper, 'The Flow Index of Regular Class I Graphs' by Jiaao Li, Xueliang Li, and Meiling Wang (SIAM J. Discrete Math.), is cited across multiple sources as extending the counterexamples to t in {6,8,10} and all t≥12; but I could not verify this paper via any accessible URL (the PDF hosts returned binary content and the SIAM page returned 403), so it is excluded from since_posted. The disproof in the verified Mattiolo–Steffen paper applies to t = 4k+2 for k ≥ 1 (i.e., t ∈ {6,10,14,…}); the arXiv page lists the journal version as Journal of Graph Theory 99 (2022), 399-413, DOI 10.1002/jgt.22746. The conjecture is still true for t=1 and its status for t ∈ {2,3,4,5} and odd t > 5 is not fully resolved.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 174s.
 

Conjecture. Let $ t \geq 1 $ be an integer and $ G $ a $ (2t+1) $ -regular graph. If $ G $ is a class 1 graph, then $ F_c(G) \leq 2 + \frac{2}{t} $ .

Keywords:
nowhere-zero flow, edge-colorings, regular graphs

Discussion

The conjecture is true for $ t=1 $ , i.e. for cubic graphs. It says, that the circular flow number of $ (2t+1) $ -regular class 1 graphs is bounded by the circular flow number of the complete graph on $ 2t+2 $ vertices.

Bibliography

 [ES_2001]
 E. Steffen, Circular flow numbers of regular multigraphs, J. Graph Theory 36, 24 – 34 (2001)

★ [ES_2015]
 E. Steffen, Edge-colorings and circular flow numbers on regular graphs, J. Graph Theory 79, 1–7, 2015

Related conjectures

 
 implied by
 Circular flow numbers of $r$-graphs
 disproved
 Hypothesis-class containment, stated explicitly in the source's OPG context: every (2t+1)-regular class 1 graph decomposes into 2t+1 perfect matchings, and each perfect matching must contain an edge of every odd cut ∂(X) (a matching covering an odd-cardinality X cannot match X internally), so |∂(X)| ≥ 2t+1 and the graph is a (2t+1)-graph. Hence the r-graph bound F_c ≤ 2+2/t restricted to class 1 regular graphs gives the target for all t > 1. The residual t = 1 case of the target is a known theorem (3-edge-colorable cubic graphs have F_c ≤ 4, noted in the target's context), so the implication holds. Both are now disproved, consistent with the direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
