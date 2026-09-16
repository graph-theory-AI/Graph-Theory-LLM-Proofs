Attack the following open graph-theory problem.

Catalog id: m_n_cycle_covers
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/m_n_cycle_covers/
Original entry: http://www.openproblemgarden.org/op/m_n_cycle_covers
Problem attributed to: Celmins, Uldis A., Preissmann, Myriam (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: (m,n)-cycle covers
Conjecture Every bridgeless graph has a (5,2)-cycle-cover.

=== Discussion / context (OpenProblemGarden) ===
Definition: If $ G=(V,E) $ is a graph, a binary cycle of $ G $ is a set $ C \subseteq E $ such that every vertex of the graph $ (V,C) $ has even degree. An $ (m,n) $ - cycle-cover of $ G $ is a list $ L $ consisting of $ m $ cycles so that every edge of $ G $ is contained in exactly $ n $ of these cycles. Since every binary cycle can be written as a disjoint union of edge sets of ordinary cycles, the above conjecture is a strengthening of the cycle double cover conjecture. For positive integers $ m,n $ it is natural to ask what family of graphs have $ (m,n) $ -cycle-covers. The following chart gives some information about this question for small values of $ m $ and $ n $ . A "yes" in the $ (m,n) $ box indicates that every graph with no cut-edge has an $ (m,n) $ -cycle-cover. A "no" indicates that no graph has an $ (m,n) $ -cycle-cover. A more detailed explanation of the entries in this chart appears below it. m n 2 3 4 5 6 7 8 9 10 11 2 Eulerian NZ 4-flow NZ 4-flow 5CDC conj open 4 no Eulerian 5 post. sets B-F conj yes [BJJ] yes 6 no Eulerian 7 post. sets ? ? yes [F] yes We did not include odd values of n, since any graph with an $ (m,n) $ -cycle-cover for an odd integer $ n $ must be Eulerian . The entry "NZ 4-flow" is short for nowhere-zero 4-flow. Thus, our chart indicates that ( $ G $ has a nowhere-zero 4-flow) if and only if ( $ G $ has a $ (3,2) $ -cycle-cover) if and only if ( $ G $ has a $ (4,2) $ -cycle-cover). These equivalences were discovered by Tutte [Tu]. Two of the $ (m,n) $ boxes are conjectures. The 5CDC conj is the 5 cycle double cover conjecture and the B-F conjecture is the Berge-Fulkerson conjecture . In both of these cases, the conjecture is equivalent to the assertion that every graph with no cut-edge has an $ (m,n) $ -cycle-cover (i.e. it would be accurate to put a "yes" in the corresponding. box). For emphasis, we state the Berge-Fulkerson conjecture again below in this new form. Conjecture (The Berge-Fulkerson conjecture) Every graph with no cut-edge has a (6,4)-cycle-cover. The fact that the above conjecture is equivalent to the usual statement of the Berge-Fulkerson conjecture was discovered by Jaeger [J]. For cubic graphs this equivalence is easy to see, since $ M_1,\ldots,M_6 $ satisfy the Berge-Fulkerson conjecture if and only if $ E\M_1,\ldots,E\M_6 $ is a $ (6,4) $ -cycle-cover. By Jaeger's argument, the weak Berge-Fulkerson conjecture is equivalent to the statement that there exists a fixed integer $ k $ so that every bridgeless graph has a $ (3k,2k) $ -cycle-cover. A postman set is a set of edges $ J $ such that $ E(G)\J $ is a cycle. The entry "k post. sets" in the $ (k,k-1) $ box of the above chart indicates that a graph G has a $ (k,k-1) $ -cycle-cover if and only if it is possible to partition the edges of $ G $ into $ k $ postman sets. This equivalence follows immediately from the definition. Rizzi's Packing postman sets conjecture is thus equivalent to the following conjecture on cycle-covers. Conjecture (the packing postman sets conjecture) If every odd edge-cut of $ G $ has size $ \ge 2k+1 $ , then $ G $ has a $ (2k+1,2k) $ -cycle-cover. Next we turn our attention to orientable cycle covers. If $ H $ is a directed graph a map $ \phi:E(H) \rightarrow \{-1,0,1\} $ is a 2-flow or an oriented cycle if at every vertex of $ H $ , the sum of $ \phi $ on the incoming edges is equal to the sum of $ \phi $ on the outgoing edges. It is easy to see that the support of a 2-flow is always a cycle. Furthermore, for any oriented cycle, there is a list $ L $ of edge-disjoint circuits with directions so that an edge $ e $ is forward (backward) in a circuit of $ L $ if and only if $ \phi(e)=1 $ ( $ \phi(e)=-1 $ ). So as in the unoriented case, an oriented cycle may be viewed as the edge-disjoint union of oriented circuits. For an even integer $ n $ , a $ (m,n) $ -oriented-cycle-cover of a graph $ G $ is a list of $ m $ oriented cycles so that every edge of $ G $ appears as a forward edge $ n/2 $ times and a backward edge $ n/2 $ times. The following conjecture is the common generalization of the orientable cycle double cover conjecture and the five cycle double cover conjecture. It is due to Archdeacon and Jaeger. Conjecture (The orientable five cycle double cover conjecture) Every graph without a cut-edge has a (5,2)-oriented-cycle-cover. Considerably less is known about $ (m,n) $ -oriented-cycle-covers. We sumarize some of what is known for small values of $ m $ and $ n $ below. m n 2 3 4 5 6 7 8 9 10 11 2 Eulerian NZ 3-flow NZ 4-flow O5CDC conj open 4 no Eulerian ? ? ? conj. open 6 no Eulerian ? ? ? ? yes [DG] Every graph with an $ (m,n) $ -cycle-cover also has a $ (2m,2n) $ -oriented-cycle-cover obtained by taking two copies of each cycle with opposite orientations. Thus, by Bermond, Jackson, and Jaeger's $ (7,4) $ -cycle-cover theorem, every bridgeless graph with no has a $ (14,8) $ -oriented-cycle-cover. DeVos and Goddyn have observed that Seymour's 6-flow theorem can be used to construct an $ (11,6) $ -oriented-cycle-cover for every bridgeless graph. By combining these, we find that for every even integer $ n \ge 10 $ there exists an $ m $ so that every bridgeless graph has an $ (m,n) $ -oriented-cycle-cover. This question is still open for $ n=2,4,10 $ . The following conjecture appears in the above chart. Conjecture (The orientable eight cycle four cover conjecture) Every graph with no cut-edge has a (8,4)-oriented-cycle-cover. This conjecture may be viewed as a sort of oriented version of the Berge-Fulkerson conjecture. To see this analogy, note that ( $ G $ has a nowhere-zero 4-flow) if and only if ( $ G $ has a $ (3,2) $ -cycle-cover) if and only if ( $ G $ has a $ (4,2) $ -oriented-cycle-cover). The Berge-Fulkerson conjecture and the above conjecture assert respectively that every bridgeless graph has a $ (6,4) $ -cycle-cover and a $ (8,4) $ -oriented-cycle-cover (i.e. a cover with double the parameters which are equivalent to a nowhere-zero 4-flow). 

=== References listed by OpenProblemGarden ===
- [A] D. Archdeacon, Face coloring of embedded graphs. J. Graph Theory, 8(1984), 387-398.
- [BJJ] J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MathSciNet
- *[C] A. U. Celmins, On cubic graphs that do not have an edge-3-colouring, Ph.D. Thesis, Department of Combinatorics and Optimization, University of Waterloo, Waterloo, Canada, 1984.
- [F] G. Fan, Integer flows and cycle covers, J. Combinatorial Theory Ser. B 54 (1992), 113-122. MathSciNet
- [J] F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216. MathSciNet
- [J88] F. Jaeger, Nowhere zero flow problems. Selected Topics in Graph Theory 3 (L.W.Beineke and R.J.Wilson eds.), Academic Press, London (1988), 71-95.
- *[P] M. Preissmann, Sur les colorations des arêtes des graphes cubiques, Thèse de 3ème cycle, Grenoble (1981) .
- [T54] W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
- [T66] W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet

=== Catalog page (statement + literature review) ===
(m,n)-cycle covers — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The (5,2)-cycle cover conjecture — that every bridgeless graph has a 5-cycle double cover — remains open as of 2026. Since it was posted, partial progress includes a characterisation of when a 2-regular subgraph of a bridgeless cubic graph can be extended to a 5-cycle double cover, and verification of the 5-CDC conjecture for several families of snarks via nowhere-zero 4-flow methods; the full conjecture, which strictly strengthens the still-open cycle double cover conjecture, is unresolved.

 Cited literature (1)

 
 
 
partial A note on 5-cycle double covers
 (2012)
 

 
 Arthur Hoffmann-Ostenhof · arXiv preprint · arXiv:1209.0096

Establishes necessary and sufficient conditions for a 2-regular subgraph of a bridgeless cubic graph to be containable in a 5-cycle double cover, advancing the strong 5-CDC conjecture.
 

 

 Reviewer notes. Two further post-2007 papers were found in search results but could not be accessed via WebFetch (journal paywalls/redirects): (1) Liu, Hao, Luo, Zhang, '5-Cycle Double Covers, 4-Flows, and Catlin Reduction', SIAM J. Discrete Math. 37(1):253–267, 2023, DOI:10.1137/22M1472425 — verifies 5-CDC for several snark families using Catlin reduction; (2) Zhang, 'Five-cycle double cover and shortest cycle cover', J. Graph Theory 108:39–49, 2025, DOI:10.1002/jgt.23164 — studies 5-CDC for weak-oddness-2 cubic graphs. arXiv:2511.07285 (approximate CDC, 2025) addresses general CDC but not specifically the (5,2)-cover. The (5,2)-cover conjecture is strictly stronger than the CDC conjecture, which is itself still open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. Every bridgeless graph has a (5,2)-cycle-cover.

Keywords:
cover · cycle

Discussion

Definition: If $ G=(V,E) $ is a graph, a binary cycle of $ G $ is a set $ C \subseteq E $ such that every vertex of the graph $ (V,C) $ has even degree. An $ (m,n) $ - cycle-cover of $ G $ is a list $ L $ consisting of $ m $ cycles so that every edge of $ G $ is contained in exactly $ n $ of these cycles. Since every binary cycle can be written as a disjoint union of edge sets of ordinary cycles, the above conjecture is a strengthening of the cycle double cover conjecture. For positive integers $ m,n $ it is natural to ask what family of graphs have $ (m,n) $ -cycle-covers. The following chart gives some information about this question for small values of $ m $ and $ n $ . A "yes" in the $ (m,n) $ box indicates that every graph with no cut-edge has an $ (m,n) $ -cycle-cover. A "no" indicates that no graph has an $ (m,n) $ -cycle-cover. A more detailed explanation of the entries in this chart appears below it. m n 2 3 4 5 6 7 8 9 10 11 2 Eulerian NZ 4-flow NZ 4-flow 5CDC conj open 4 no Eulerian 5 post. sets B-F conj yes [BJJ] yes 6 no Eulerian 7 post. sets ? ? yes [F] yes We did not include odd values of n, since any graph with an $ (m,n) $ -cycle-cover for an odd integer $ n $ must be Eulerian . The entry "NZ 4-flow" is short for nowhere-zero 4-flow. Thus, our chart indicates that ( $ G $ has a nowhere-zero 4-flow) if and only if ( $ G $ has a $ (3,2) $ -cycle-cover) if and only if ( $ G $ has a $ (4,2) $ -cycle-cover). These equivalences were discovered by Tutte [Tu]. Two of the $ (m,n) $ boxes are conjectures. The 5CDC conj is the 5 cycle double cover conjecture and the B-F conjecture is the Berge-Fulkerson conjecture . In both of these cases, the conjecture is equivalent to the assertion that every graph with no cut-edge has an $ (m,n) $ -cycle-cover (i.e. it would be accurate to put a "yes" in the corresponding. box). For emphasis, we state the Berge-Fulkerson conjecture again below in this new form. Conjecture (The Berge-Fulkerson conjecture) Every graph with no cut-edge has a (6,4)-cycle-cover. The fact that the above conjecture is equivalent to the usual statement of the Berge-Fulkerson conjecture was discovered by Jaeger [J]. For cubic graphs this equivalence is easy to see, since $ M_1,\ldots,M_6 $ satisfy the Berge-Fulkerson conjecture if and only if $ E\M_1,\ldots,E\M_6 $ is a $ (6,4) $ -cycle-cover. By Jaeger's argument, the weak Berge-Fulkerson conjecture is equivalent to the statement that there exists a fixed integer $ k $ so that every bridgeless graph has a $ (3k,2k) $ -cycle-cover. A postman set is a set of edges $ J $ such that $ E(G)\J $ is a cycle. The entry "k post. sets" in the $ (k,k-1) $ box of the above chart indicates that a graph G has a $ (k,k-1) $ -cycle-cover if and only if it is possible to partition the edges of $ G $ into $ k $ postman sets. This equivalence follows immediately from the definition. Rizzi's Packing postman sets conjecture is thus equivalent to the following conjecture on cycle-covers. Conjecture (the packing postman sets conjecture) If every odd edge-cut of $ G $ has size $ \ge 2k+1 $ , then $ G $ has a $ (2k+1,2k) $ -cycle-cover. Next we turn our attention to orientable cycle covers. If $ H $ is a directed graph a map $ \phi:E(H) \rightarrow \{-1,0,1\} $ is a 2-flow or an oriented cycle if at every vertex of $ H $ , the sum of $ \phi $ on the incoming edges is equal to the sum of $ \phi $ on the outgoing edges. It is easy to see that the support of a 2-flow is always a cycle. Furthermore, for any oriented cycle, there is a list $ L $ of edge-disjoint circuits with directions so that an edge $ e $ is forward (backward) in a circuit of $ L $ if and only if $ \phi(e)=1 $ ( $ \phi(e)=-1 $ ). So as in the unoriented case, an oriented cycle may be viewed as the edge-disjoint union of oriented circuits. For an even integer $ n $ , a $ (m,n) $ -oriented-cycle-cover of a graph $ G $ is a list of $ m $ oriented cycles so that every edge of $ G $ appears as a forward edge $ n/2 $ times and a backward edge $ n/2 $ times. The following conjecture is the common generalization of the orientable cycle double cover conjecture and the five cycle double cover conjecture. It is due to Archdeacon and Jaeger. Conjecture (The orientable five cycle double cover conjecture) Every graph without a cut-edge has a (5,2)-oriented-cycle-cover. Considerably less is known about $ (m,n) $ -oriented-cycle-covers. We sumarize some of what is known for small values of $ m $ and $ n $ below. m n 2 3 4 5 6 7 8 9 10 11 2 Eulerian NZ 3-flow NZ 4-flow O5CDC conj open 4 no Eulerian ? ? ? conj. open 6 no Eulerian ? ? ? ? yes [DG] Every graph with an $ (m,n) $ -cycle-cover also has a $ (2m,2n) $ -oriented-cycle-cover obtained by taking two copies of each cycle with opposite orientations. Thus, by Bermond, Jackson, and Jaeger's $ (7,4) $ -cycle-cover theorem, every bridgeless graph with no has a $ (14,8) $ -oriented-cycle-cover. DeVos and Goddyn have observed that Seymour's 6-flow theorem can be used to construct an $ (11,6) $ -oriented-cycle-cover for every bridgeless graph. By combining these, we find that for every even integer $ n \ge 10 $ there exists an $ m $ so that every bridgeless graph has an $ (m,n) $ -oriented-cycle-cover. This question is still open for $ n=2,4,10 $ . The following conjecture appears in the above chart. Conjecture (The orientable eight cycle four cover conjecture) Every graph with no cut-edge has a (8,4)-oriented-cycle-cover. This conjecture may be viewed as a sort of oriented version of the Berge-Fulkerson conjecture. To see this analogy, note that ( $ G $ has a nowhere-zero 4-flow) if and only if ( $ G $ has a $ (3,2) $ -cycle-cover) if and only if ( $ G $ has a $ (4,2) $ -oriented-cycle-cover). The Berge-Fulkerson conjecture and the above conjecture assert respectively that every bridgeless graph has a $ (6,4) $ -cycle-cover and a $ (8,4) $ -oriented-cycle-cover (i.e. a cover with double the parameters which are equivalent to a nowhere-zero 4-flow). As with most of the conjectures in this area, the above conjecture is trivially true for graphs with nowhere-zero 4-flows and it holds for the Petersen graph.

Bibliography

 [A]
 D. Archdeacon, Face coloring of embedded graphs. J. Graph Theory, 8(1984), 387-398.

 [BJJ]
 J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MathSciNet
 MathSciNet

★ [C]
 A. U. Celmins, On cubic graphs that do not have an edge-3-colouring, Ph.D. Thesis, Department of Combinatorics and Optimization, University of Waterloo, Waterloo, Canada, 1984.

 [F]
 G. Fan, Integer flows and cycle covers, J. Combinatorial Theory Ser. B 54 (1992), 113-122. MathSciNet
 MathSciNet

 [J]
 F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216. MathSciNet
 MathSciNet

 [J88]
 F. Jaeger, Nowhere zero flow problems. Selected Topics in Graph Theory 3 (L.W.Beineke and R.J.Wilson eds.), Academic Press, London (1988), 71-95.

★ [P]
 M. Preissmann, Sur les colorations des arêtes des graphes cubiques, Thèse de 3ème cycle, Grenoble (1981) .

 [T54]
 W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
 MathSciNet

 [T66]
 W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 Cycle double cover conjecture
 partial
 Both conjectures quantify over the same class (bridgeless graphs). A (5,2)-cycle-cover is 5 binary cycles (even subgraphs) covering each edge exactly twice; since every binary cycle decomposes into edge-disjoint circuits, decomposing each of the 5 yields a list of circuits covering every edge exactly twice, i.e., a cycle double cover. The source's OPG context states this explicitly: 'the above conjecture is a strengthening of the cycle double cover conjecture.' Direction as claimed.
 

 
 implied by
 Petersen coloring conjecture
 partial
 The target, 'every bridgeless graph has a (5,2)-cycle-cover', is exactly the five cycle double cover conjecture (the OPG (m,n) chart labels the (5,2) entry '5CDC conj'). The source's equivalent reformulation (2), stated in its context, is that every bridgeless graph admits a cycle-continuous map f to the Petersen graph P. P has a double cover by 5 even subgraphs; the preimage of each is an even subgraph of G (cycle-continuity), and each edge e of G is covered exactly as many times as f(e), namely twice, yielding a (5,2)-cycle-cover of G. The OPG source page states explicitly that Petersen coloring implies the five cycle double cover conjecture. Hypothesis classes match (all bridgeless graphs via reformulation (2)).
 

 
 implied by
 Strong 5-cycle double cover conjecture
 partial
 The source context states it strengthens the 5-cycle double cover conjecture, and the target's chart labels the (5,2) entry '5CDC conj', identifying the general (5,2)-cover conjecture with the 5-CDC conjecture. Chain: any nonempty bridgeless cubic graph has a circuit C; strong 5-CDC applied to C gives a 5-CDC of that graph. The general bridgeless case reduces to cubic by Fleischner's splitting lemma (expand vertices of degree >=4 preserving bridgelessness); restricting each of the 5 even subgraphs of the cubic expansion to E(G) is even at every original vertex (parity argument across the gadget) and covers each original edge exactly twice, yielding a (5,2)-cycle-cover of G. This is the standard reduction of 5-CDC to cubic graphs. Direction as claimed.
 

 
 related to
 The Berge-Fulkerson conjecture
 partial
 The source statement (every bridgeless graph has a (5,2)-cycle cover) is exactly the 5-cycle-double-cover conjecture, the (5,2) entry of the OPG chart; Berge-Fulkerson is equivalent (via complementing the six perfect matchings by 2-factors, extended from cubic graphs) to the (6,4) entry of the same chart. So the mention is that both conjectures are different boxes of the same (m,n)-cycle-cover table, not that one implies the other. No implication between 5CDC and Berge-Fulkerson is known in either direction (even whether BF implies the ordinary CDC is open); a (5,2)-cover does not yield a (6,4)-cover by any simple combination, nor conversely. Hence: strongly thematically linked, no established implication.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
