Attack the following open graph-theory problem.

Catalog id: decomposing_eulerian_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/decomposing_eulerian_graphs/
Original entry: http://www.openproblemgarden.org/op/decomposing_eulerian_graphs

=== Problem statement (OpenProblemGarden) ===
Title: Decomposing eulerian graphs
Conjecture If $ G $ is a 6- edge-connected Eulerian graph and $ P $ is a 2-transition system for $ G $ , then $ (G,P) $ has a compaible decomposition.

=== Discussion / context (OpenProblemGarden) ===
Definition: Let $ G $ be an Eulerian graph and for every vertex $ v $ , let $ P(v) $ be a partition of the edges incident with $ v $ . We call $ P $ a transition system . If every member of $ P(v) $ has size at most $ k $ (for every $ v $ ), then we call $ P $ a $ k $ - transition sytem . A compatible decomposition of $ (G,P) $ is a list of edge-disjoint cycles $ C_1,\ldots,C_n $ with union $ G $ so that every $ C_i $ contains at most one edge from every member of $ P(v) $ . Let $ G $ be a graph and let $ G' $ be the graph obtained from $ G $ by replacing each edge $ e $ of G by two edges $ e',e'' $ in parallel. Let $ P $ be the 2-transition system of $ G $ with $ {e',e''} \in P(v) $ whenever $ e' $ and $ e'' $ are incident with $ v $ . Now, $ G' $ is an Eulerian graph and every compatible decomposition of $ (G',P) $ gives a cycle double cover of $ G $ . Since the cycle double cover conjecture can be reduced to graphs which are 3-edge-connected, the above conjecture would imply the cycle double cover conjecture. We define a transition system $ P $ to be admissable if every member of $ P(v) $ contains no more than half of the edges in any edge-cut. It is easy to see that if there is a compatible decomposition of $ (G,P) $ , then $ P $ must be admissable. The converse of this is not true; There is an admissable 2-transition system of the graph $ K_5 $ which does not admit a compatible decomposition. Recently, G. Fan and C.Q. Zhang [FZ] have proved that $ (G,P) $ does have a compatible decomposition whenever $ P $ is admissable and $ G $ has no $ K_5 $ minor. This result imporoved upon an earlier theorem of Fleischner and Frank [FF]. Very recently, I have proved a weak version of the above conjecture, by showing that $ (G,P) $ also has a compatible decomposition when P is a 2-transition system and G is 80-edge-connected. I'd quite like to see an improvement on this bound. Here is a related conjecture. Conjecture (Sabidussi) Let $ W $ be an Euler tour of the graph $ G $ . If $ G $ has no vertex of degree two, then there is a cycle decomposition of $ G $ , say $ F $ , so that no two consecutive edges of $ W $ are in a common circuit of $ F $ . If $ W $ is given by $ v_1,e_1,v_2,e_2,...,e_{m-1},v_m $ then we may form a 2-transition system $ P $ by putting $ \{e_{i-1},e_i\} $ in $ P(v_i) $ for every $ i $ (working modulo $ m $ ). Now a compatible decomposition of $ (G,P) $ is precisely a cycle decomposition of $ G $ satisfying the above conjecture. Thus, Sabidussi's conjecture is equivalent to the assertion that $ (G,P) $ has a compatible decomposition whenever $ G $ has no vertex of degree two and $ P $ is a 2-transition system which comes from an Euler tour. Let $ G $ be a directed Eulerian graph and for every vertex $ v $ , let $ P(v) $ be a partition of the edges incident with $ v $ into pairs so that every in-edge is paired with an out-edge. We define a compatible decomposition to be a decomposition of $ G $ into directed circuits so that every directed circuit contains at most one edge from every member of $ P(v) $ . Our current techniques don't seem to shed any light on the problem of finding compatible decompositions for Eulerian digraphs. Next I pose a very basic question which is still open. Problem (DeVos) Does there exist a fixed integer $ k $ such that $ (G,P) $ has a compatible decomposition whenever $ G $ is a $ k $ -edge-connected directed Eulerian graph and $ P $ is a 2-transition system?

=== Catalog page (statement + literature review) ===
Decomposing eulerian graphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture that every 6-edge-connected Eulerian graph $G$ with a 2-transition system $P$ admits a compatible decomposition remains open. Since posting, Fleischner, Bagheri Gh., C.-Q. Zhang, and Z. Zhang (2019) completely resolved the conjecture for the class of $K_5$-transition-minor-free Eulerian graphs, extending the earlier Fan–Zhang result for $K_5$-minor-free graphs. No improvement on the 80-edge-connectivity bound (the best general result at posting) appears in the verified literature.

 Cited literature (1)

 
 
 
partial Cycle covers (III) – Compatible circuit decomposition and K5-transition minor
 (2019)
 

 
 Herbert Fleischner, Behrooz Bagheri Gh., Cun-Quan Zhang, Zhang Zhang · Journal of Combinatorial Theory, Series B

Completely resolves the compatible circuit decomposition conjecture for Eulerian graphs that are $K_5$-transition-minor-free, generalising the earlier Fan–Zhang theorem for $K_5$-minor-free graphs.
 

 

 Reviewer notes. The Fleischner–Genest–Jackson preprint 'Compatible Circuit Decompositions of Eulerian Graphs' (September 2006 manuscript visible on Jackson's QMUL page) predates the OPG posting and was not found to have been published as a journal article after 2007-03-07; it was not cited. The 2019 JCTB paper (Cycle Covers III) was confirmed via the WVU directory of C.-Q. Zhang, listing it as JCTB 137 (2019): 25-54. The ScienceDirect full-text page and ResearchGate abstract both returned 403, so detailed abstract text could not be read directly; the characterisation of the paper's result relies on the search-engine AI summaries and the WVU author page listing, which are consistent. No evidence was found that the 80-edge-connectivity general bound has been improved in the post-2007 period. The main 6-edge-connected conjecture appears to remain open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. If $ G $ is a 6- edge-connected Eulerian graph and $ P $ is a 2-transition system for $ G $ , then $ (G,P) $ has a compaible decomposition.

Keywords:
cover · cycle · Eulerian

Discussion

Definition: Let $ G $ be an Eulerian graph and for every vertex $ v $ , let $ P(v) $ be a partition of the edges incident with $ v $ . We call $ P $ a transition system . If every member of $ P(v) $ has size at most $ k $ (for every $ v $ ), then we call $ P $ a $ k $ - transition sytem . A compatible decomposition of $ (G,P) $ is a list of edge-disjoint cycles $ C_1,\ldots,C_n $ with union $ G $ so that every $ C_i $ contains at most one edge from every member of $ P(v) $ . Let $ G $ be a graph and let $ G' $ be the graph obtained from $ G $ by replacing each edge $ e $ of G by two edges $ e',e'' $ in parallel. Let $ P $ be the 2-transition system of $ G $ with $ {e',e''} \in P(v) $ whenever $ e' $ and $ e'' $ are incident with $ v $ . Now, $ G' $ is an Eulerian graph and every compatible decomposition of $ (G',P) $ gives a cycle double cover of $ G $ . Since the cycle double cover conjecture can be reduced to graphs which are 3-edge-connected, the above conjecture would imply the cycle double cover conjecture. We define a transition system $ P $ to be admissable if every member of $ P(v) $ contains no more than half of the edges in any edge-cut. It is easy to see that if there is a compatible decomposition of $ (G,P) $ , then $ P $ must be admissable. The converse of this is not true; There is an admissable 2-transition system of the graph $ K_5 $ which does not admit a compatible decomposition. Recently, G. Fan and C.Q. Zhang [FZ] have proved that $ (G,P) $ does have a compatible decomposition whenever $ P $ is admissable and $ G $ has no $ K_5 $ minor. This result imporoved upon an earlier theorem of Fleischner and Frank [FF]. Very recently, I have proved a weak version of the above conjecture, by showing that $ (G,P) $ also has a compatible decomposition when P is a 2-transition system and G is 80-edge-connected. I'd quite like to see an improvement on this bound. Here is a related conjecture. Conjecture (Sabidussi) Let $ W $ be an Euler tour of the graph $ G $ . If $ G $ has no vertex of degree two, then there is a cycle decomposition of $ G $ , say $ F $ , so that no two consecutive edges of $ W $ are in a common circuit of $ F $ . If $ W $ is given by $ v_1,e_1,v_2,e_2,...,e_{m-1},v_m $ then we may form a 2-transition system $ P $ by putting $ \{e_{i-1},e_i\} $ in $ P(v_i) $ for every $ i $ (working modulo $ m $ ). Now a compatible decomposition of $ (G,P) $ is precisely a cycle decomposition of $ G $ satisfying the above conjecture. Thus, Sabidussi's conjecture is equivalent to the assertion that $ (G,P) $ has a compatible decomposition whenever $ G $ has no vertex of degree two and $ P $ is a 2-transition system which comes from an Euler tour. Let $ G $ be a directed Eulerian graph and for every vertex $ v $ , let $ P(v) $ be a partition of the edges incident with $ v $ into pairs so that every in-edge is paired with an out-edge. We define a compatible decomposition to be a decomposition of $ G $ into directed circuits so that every directed circuit contains at most one edge from every member of $ P(v) $ . Our current techniques don't seem to shed any light on the problem of finding compatible decompositions for Eulerian digraphs. Next I pose a very basic question which is still open. Problem (DeVos) Does there exist a fixed integer $ k $ such that $ (G,P) $ has a compatible decomposition whenever $ G $ is a $ k $ -edge-connected directed Eulerian graph and $ P $ is a 2-transition system?

Related conjectures

 
 implies
 Cycle double cover conjecture
 partial
 DIRECTION FLIPPED from the seed edge (which listed CDC as source). The Decomposing-Eulerian-graphs page states explicitly: "the above conjecture would imply the cycle double cover conjecture", and gives the argument: CDC reduces to 3-edge-connected graphs; replacing each edge of such a G by two parallel edges yields a 6-edge-connected Eulerian graph G' with the 2-transition system P pairing the parallel copies at each endpoint; a compatible decomposition of (G',P) uses at most one copy of each parallel pair per cycle, so projecting back to G gives a list of cycles covering every edge exactly twice, i.e., a CDC. The converse is not claimed anywhere, so this is a one-way implication: Decomposing Eulerian graphs is the stronger statement.
 

 
 implies
 Cycle double cover conjecture
 partial
 Explicitly stated in the source context with a valid reduction: given a 3-edge-connected G, replace each edge by two parallel edges to obtain G', which is Eulerian and 6-edge-connected, with the 2-transition system P pairing the parallel copies at each endpoint; a compatible decomposition of (G',P) uses at most one of each parallel pair per cycle at each vertex, so it projects to a list of cycles of G covering every edge exactly twice, i.e. a CDC of G. Since the CDC conjecture reduces (by standard vertex-splitting/cut arguments) to 3-edge-connected graphs, the Eulerian decomposition conjecture implies CDC. Hypothesis class checks out: 6-edge-connectivity of G' follows from 3-edge-connectivity of G because doubling edges doubles every edge cut.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
