Attack the following open graph-theory problem.

Catalog id: bouchets_6_flow_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/bouchets_6_flow_conjecture/
Original entry: http://www.openproblemgarden.org/op/bouchets_6_flow_conjecture
Problem attributed to: Bouchet, Andre (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Bouchet's 6-flow conjecture
Conjecture Every bidirected graph with a nowhere-zero $ k $ -flow for some $ k $ , has a nowhere-zero $ 6 $ -flow.

=== Discussion / context (OpenProblemGarden) ===
Definition: A bidirected graph is a graph in which every edge has two arrowheads, one next to each endpoint. If the edge $ e $ has ends $ u $ and $ v $ , then the arrowheads nearest $ u $ and $ v $ may point either toward $ u $ or toward $ v $ (giving four possibilities in all). If $ G $ is a bidirected graph, a $ k $ -flow of G is a map $ \phi:E(G)\to \{-(k-1),...,-1,0,1,...,k-1\} $ with the property that at every vertex, the sum of $ \phi $ on the edges whose ends at $ v $ are directed into $ v $ is equal to the sum of $ \phi $ on the edges whose ends at $ v $ are directed out of $ v $ . We say that $ \phi $ is nowhere-zero if $ \phi(e) \neq 0 $ for every $ e \in E(G) $ (see nowhere-zero flows ). Flows on bidirected graphs arise naturally as duals of local-tensions on a non-orientable surface. For more on this relationship, see [B]. Bouchet proved that the above conjecture is true with 6 replaced by 216, and exhibited a bidirected Petersen graph as above which shows that 6 is the best value possible. Zyka [Z] and independently Fouquet improved upon this result proving that the above conjecture is true with 6 replaced by 30. Khelladi [K] proved that for 4-connected graphs, the above conjecture is true with 6 replaced by 18. DeVos [D] proved that the above conjecture holds with 6 replaced by 12, and showed that every 4-edge-connected bidirected graph with a nowhere-zero integer flow also has a nowhere-zero 4-flow.

=== References listed by OpenProblemGarden ===
- [B] A. Bouchet, Nowhere-Zero Integral Flows on a Bidirected Graph, J. Combinatorial Theory Ser. B 34 (1983) 279-292. MathSciNet
- [D] M. DeVos, Flows on Bidirected Graphs, preprint.
- [K] A. Khelladi, Nowhere-Zero Integral Chains and Flows in Bidirected Graphs, J. Combinatorial Theory Ser. B 43 (1987) 95-115. MathSciNet
- [Z] O. Zyka, Bidirected Nowhere-Zero Flows, Thesis, Charles University, Praha (1988).

=== Catalog page (statement + literature review) ===
Bouchet's 6-flow conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Bouchet's 6-flow conjecture for bidirected (signed) graphs remains open in full generality. Since posting, the best known general bound has been improved from 12 (DeVos, preprint known at posting time) to 11 for all flow-admissible signed graphs (DeVos et al., 2019), and further to 8 for all 3-edge-connected flow-admissible signed graphs (DeVos, Nurse, Šámal, 2025). The conjecture has been fully verified for cyclically 5-edge-connected cubic signed graphs (Nurse, 2026).

 Cited literature (5)

 
 
 
partial Flows on flow-admissible signed graphs
 (2019)
 

 
 Matt DeVos, Jiaao Li, You Lu, Rong Luo, Cun-Quan Zhang, Zhang Zhang · arXiv preprint · arXiv:1908.10853

Every flow-admissible signed graph admits a nowhere-zero 11-flow, improving the best previously known general bound from 12 to 11.
 

 
 
partial Nowhere-zero 8-flows in cyclically 5-edge-connected, flow-admissible signed graphs
 (2023)
 

 
 Matt DeVos, Kathryn Nurse, Robert Sámal · arXiv preprint · arXiv:2309.00704

Every cyclically 5-edge-connected, flow-admissible signed graph has a nowhere-zero 8-flow.
 

 
 
partial An 8-flow theorem for signed graphs
 (2024)
 

 
 Rong Luo, Edita Máčajová, Martin Škoviera, Cun-Quan Zhang · arXiv preprint · arXiv:2402.12883

Every flow-admissible signed graph whose underlying unsigned graph admits a nowhere-zero 4-flow also admits a nowhere-zero 8-flow.
 

 
 
partial Nowhere-zero 8-flows in 3-edge-connected signed graphs
 (2025)
 

 
 Matt DeVos, Kathryn Nurse, Robert Šámal · arXiv preprint · arXiv:2512.18923

Every flow-admissible 3-edge-connected signed graph has a nowhere-zero 8-flow, substantially improving the best known bound for this connectivity class.
 

 
 
partial Bouchet's conjecture for cyclically 5-edge-connected, cubic signed graphs
 (2026)
 

 
 Kathryn Nurse · arXiv preprint · arXiv:2601.05692

Bouchet's 6-flow conjecture is established in full for cyclically 5-edge-connected cubic signed graphs.
 

 

 Reviewer notes. Bidirected graphs and signed graphs are equivalent frameworks for this problem and the modern literature uses 'signed graph' exclusively. The arXiv page for 1908.10853 did not list a journal reference, but secondary sources (ResearchGate, search snippets) consistently cite publication in J. Combin. Theory Ser. B 149 (2021): 198–221; I use 2019 (arXiv year) as the conservative verified date. The Springer page for the 2011 Wei–Tang–Wang paper ('Flows in 3-edge-connected bidirected graphs', Frontiers of Math. China) and the 2014 Wei–Tang–Ye paper ('Nowhere-zero 15-flow in 3-edge-connected bidirected graphs', Acta Math. Sinica) redirected to an authentication wall and could not be verified, so they are excluded despite appearing in search results. The full conjecture (bound 6 for all flow-admissible bidirected graphs) remains open as of 2026.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 1347s.
 

Conjecture. Every bidirected graph with a nowhere-zero $ k $ -flow for some $ k $ , has a nowhere-zero $ 6 $ -flow.

Keywords:
bidirected graph · nowhere-zero flow

Discussion

Definition: A bidirected graph is a graph in which every edge has two arrowheads, one next to each endpoint. If the edge $ e $ has ends $ u $ and $ v $ , then the arrowheads nearest $ u $ and $ v $ may point either toward $ u $ or toward $ v $ (giving four possibilities in all). If $ G $ is a bidirected graph, a $ k $ -flow of G is a map $ \phi:E(G)\to \{-(k-1),...,-1,0,1,...,k-1\} $ with the property that at every vertex, the sum of $ \phi $ on the edges whose ends at $ v $ are directed into $ v $ is equal to the sum of $ \phi $ on the edges whose ends at $ v $ are directed out of $ v $ . We say that $ \phi $ is nowhere-zero if $ \phi(e) \neq 0 $ for every $ e \in E(G) $ (see nowhere-zero flows ). Flows on bidirected graphs arise naturally as duals of local-tensions on a non-orientable surface. For more on this relationship, see [B]. Bouchet proved that the above conjecture is true with 6 replaced by 216, and exhibited a bidirected Petersen graph as above which shows that 6 is the best value possible. Zyka [Z] and independently Fouquet improved upon this result proving that the above conjecture is true with 6 replaced by 30. Khelladi [K] proved that for 4-connected graphs, the above conjecture is true with 6 replaced by 18. DeVos [D] proved that the above conjecture holds with 6 replaced by 12, and showed that every 4-edge-connected bidirected graph with a nowhere-zero integer flow also has a nowhere-zero 4-flow.

Bibliography

 [B]
 A. Bouchet, Nowhere-Zero Integral Flows on a Bidirected Graph, J. Combinatorial Theory Ser. B 34 (1983) 279-292. MathSciNet
 MathSciNet

 [D]
 M. DeVos, Flows on Bidirected Graphs, preprint.

 [K]
 A. Khelladi, Nowhere-Zero Integral Chains and Flows in Bidirected Graphs, J. Combinatorial Theory Ser. B 43 (1987) 95-115. MathSciNet
 MathSciNet

 [Z]
 O. Zyka, Bidirected Nowhere-Zero Flows, Thesis, Charles University, Praha (1988).

Related conjectures

 
 related to
 5-local-tensions
 open
 Bouchet's conjecture concerns nowhere-zero 6-flows on bidirected graphs, which by duality (as both pages note: 'flows on bidirected graphs arise naturally as duals of local-tensions on a non-orientable surface') implies a 6-LOCAL-TENSION statement for graphs embedded in non-orientable surfaces. The headline source conjecture asks for a 5-local-tension under an edge-width >= c hypothesis; the parameters differ (6 vs 5), so Bouchet's conjecture does not imply it, and the source conjecture, being restricted to large edge-width embeddings and to the number 5, does not imply Bouchet's statement about all bidirected graphs. They are linked by the same duality framework and Bouchet's conjecture is evidence/motivation, but there is no implication in either direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
