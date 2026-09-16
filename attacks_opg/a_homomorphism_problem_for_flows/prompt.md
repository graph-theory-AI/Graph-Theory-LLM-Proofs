Attack the following open graph-theory problem.

Catalog id: a_homomorphism_problem_for_flows
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/a_homomorphism_problem_for_flows/
Original entry: http://www.openproblemgarden.org/op/a_homomorphism_problem_for_flows
Problem attributed to: DeVos, Matt (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: A homomorphism problem for flows
Conjecture Let $ M,M' $ be abelian groups and let $ B \subseteq M $ and $ B' \subseteq M' $ satisfy $ B=-B $ and $ B' = -B' $ . If there is a homomorphism from $ Cayley(M,B) $ to $ Cayley(M',B') $ , then every graph with a B-flow has a B'-flow.

=== Discussion / context (OpenProblemGarden) ===
Definition: Let $ G $ be a directed graph, Let $ M $ be an abelian group, and let $ B $ be a subset of $ M $ such that $ B=-B $ . We say that a flow or a tension $ \phi:E(G) \rightarrow M $ is a $ B $ -flow or a $ B $ -tension if the range is a subset of $ B $ . If $ \phi $ is a $ B $ -flow ( $ B $ -tension) of $ G $ and we reverse the direction of the edge $ e $ , then we may obtain a new $ B $ -flow ( $ B $ -tension) by changing $ \phi(e) $ to $ -\phi(e) $ . Thus, the existence of a $ B $ -flow or $ B $ -tension does not depend on the orientation, and we say that an undirected graph has a $ B $ -flow or a $ B $ -tension if some (and thus every) orientation of it admits such a map. We define the Cayley graph $ Cayley(M,B) $ to be the simple graph with vertex set $ M $ in which two vertices $ u,v $ are joined by an edge if and only if $ u-v \in B $ . It is well known that a graph has a $ B $ -tension if and only if it has a homomorphism to $ Cayley(M,B) $ . So, if $ M,M',B,B' $ are as in the conjecture and there is a homomorphism from $ Cayley(M,B) $ to $ Cayley(M',B') $ , then every graph G with a $ B $ -tension has a $ B' $ -tension. This follows from the previous sentence and the fact that the composition of two homomorphisms is another homomorphism. In essence, the above conjecture states that the same equivalence should hold true for flows. If $ H $ and $ H^* $ are directed planar dual graphs (each edge of $ H^* $ crosses left to right over the corresponding edge of $ H $ ), then a map $ \phi:E(H) \to M $ is a tension if and only if the dual map $ \phi^*:E(H^*) \to M $ ( $ \phi^* $ is given by the rule $ \phi^*(e^*)=\phi(e) $ ) is a flow of $ H^* $ . Thus, planar duality exchanges flows and tensions. For two undirected planar dual graphs, $ G $ and $ G^* $ we have that G has a $ B $ -flow if and only if $ G^* $ has a $ B $ -tension. It follows from this duality and the observation from the previous paragraph, that the above conjecture is true for planar graphs. This conjecture is also known in the special case when $ B=M\setminus \{0\} $ and $ B'=M'\setminus \{0\} $ . In this case, $ Cayley(M,B) $ and $ Cayley(M',B') $ are the complete graphs on $ |M| $ and $ |M'| $ vertices respectively, so there is a homomorphism from $ Cayley(M,B) $ to $ Cayley(M',B') $ if and only if $ |M'| $ is greater than or equal to $ |M| $ . Thus, in this case the conjecture is equivalent to the assertion that every graph with a nowhere-zero $ M $ -flow also has a nowhere-zero $ M' $ -flow if $ |M'| $ is at least $ |M| $ . This statement is true by a result of Tutte.

=== Catalog page (statement + literature review) ===
A homomorphism problem for flows — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 DeVos's conjecture remains open in general. Hušek and Šámal (2020) showed that a natural strengthening of the conjecture fails universally, proved partial results for a restricted subclass of Cayley graph homomorphisms, and established that the conjecture (if true) would imply the existence of an oriented cycle double cover with a bounded number of cycles. The conjecture is known to hold for planar graphs (via planar duality) and in the special case $B = M \setminus \{0\}$ by Tutte's theorem, but the general case is unresolved.

 Cited literature (1)

 
 
 
partial Homomorphisms of Cayley graphs and Cycle Double Covers
 (2020)
 

 
 Radek Hušek, Robert Šámal · The Electronic Journal of Combinatorics · arXiv:1901.03112

Shows that a natural strengthening of DeVos's conjecture does not hold in general, proves partial results for a restricted subclass, and establishes that the original conjecture implies the existence of an oriented cycle double cover with a small number of cycles.
 

 

 Reviewer notes. The OPG mirror at garden.irmacs.sfu.ca was unreachable (ECONNREFUSED). No post-2020 paper directly addressing the original DeVos conjecture was found; the most recent search sweep (up to 2026) turned up no resolution. The Springer link for 'Flow modules and nowhere-zero flows' (10.1007/s10801-022-01177-4) redirected to an authentication wall and could not be verified, so it is not cited. The ScienceDirect URL for the Hušek–Šámal paper (pii/S157106531730183X) appears to be a different publication venue or version and was not separately verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 120s.
 

Conjecture. Let $ M,M' $ be abelian groups and let $ B \subseteq M $ and $ B' \subseteq M' $ satisfy $ B=-B $ and $ B' = -B' $ . If there is a homomorphism from $ Cayley(M,B) $ to $ Cayley(M',B') $ , then every graph with a B-flow has a B'-flow.

Keywords:
homomorphism · nowhere-zero flow · tension

Discussion

Definition: Let $ G $ be a directed graph, Let $ M $ be an abelian group, and let $ B $ be a subset of $ M $ such that $ B=-B $ . We say that a flow or a tension $ \phi:E(G) \rightarrow M $ is a $ B $ -flow or a $ B $ -tension if the range is a subset of $ B $ . If $ \phi $ is a $ B $ -flow ( $ B $ -tension) of $ G $ and we reverse the direction of the edge $ e $ , then we may obtain a new $ B $ -flow ( $ B $ -tension) by changing $ \phi(e) $ to $ -\phi(e) $ . Thus, the existence of a $ B $ -flow or $ B $ -tension does not depend on the orientation, and we say that an undirected graph has a $ B $ -flow or a $ B $ -tension if some (and thus every) orientation of it admits such a map. We define the Cayley graph $ Cayley(M,B) $ to be the simple graph with vertex set $ M $ in which two vertices $ u,v $ are joined by an edge if and only if $ u-v \in B $ . It is well known that a graph has a $ B $ -tension if and only if it has a homomorphism to $ Cayley(M,B) $ . So, if $ M,M',B,B' $ are as in the conjecture and there is a homomorphism from $ Cayley(M,B) $ to $ Cayley(M',B') $ , then every graph G with a $ B $ -tension has a $ B' $ -tension. This follows from the previous sentence and the fact that the composition of two homomorphisms is another homomorphism. In essence, the above conjecture states that the same equivalence should hold true for flows. If $ H $ and $ H^* $ are directed planar dual graphs (each edge of $ H^* $ crosses left to right over the corresponding edge of $ H $ ), then a map $ \phi:E(H) \to M $ is a tension if and only if the dual map $ \phi^*:E(H^*) \to M $ ( $ \phi^* $ is given by the rule $ \phi^*(e^*)=\phi(e) $ ) is a flow of $ H^* $ . Thus, planar duality exchanges flows and tensions. For two undirected planar dual graphs, $ G $ and $ G^* $ we have that G has a $ B $ -flow if and only if $ G^* $ has a $ B $ -tension. It follows from this duality and the observation from the previous paragraph, that the above conjecture is true for planar graphs. This conjecture is also known in the special case when $ B=M\setminus \{0\} $ and $ B'=M'\setminus \{0\} $ . In this case, $ Cayley(M,B) $ and $ Cayley(M',B') $ are the complete graphs on $ |M| $ and $ |M'| $ vertices respectively, so there is a homomorphism from $ Cayley(M,B) $ to $ Cayley(M',B') $ if and only if $ |M'| $ is greater than or equal to $ |M| $ . Thus, in this case the conjecture is equivalent to the assertion that every graph with a nowhere-zero $ M $ -flow also has a nowhere-zero $ M' $ -flow if $ |M'| $ is at least $ |M| $ . This statement is true by a result of Tutte.
