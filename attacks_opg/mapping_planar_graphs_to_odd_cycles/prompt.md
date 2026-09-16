Attack the following open graph-theory problem.

Catalog id: mapping_planar_graphs_to_odd_cycles
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Homomorphisms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/mapping_planar_graphs_to_odd_cycles/
Original entry: http://www.openproblemgarden.org/op/mapping_planar_graphs_to_odd_cycles
Problem attributed to: Jaeger, Francois (posted 2007-06-24)

=== Problem statement (OpenProblemGarden) ===
Title: Mapping planar graphs to odd cycles
Conjecture Every planar graph of girth $ \ge 4k $ has a homomorphism to $ C_{2k+1} $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is Jaeger's modular orientation conjecture restricted to planar graphs and then dualized. To see this duality, first note that circular coloring and circular flows are dual for planar graphs, and then observe that $ (2k+1) $ -orientations are equivalent to $ 2 + \frac{1}{k} $ -flows and $ 2 + \frac{1}{k} $ -colorings are equivalent to homomorphisms to $ C_{2k+1} $ . So if $ G $ and $ G^* $ are dual planar graphs, then we have the following equivalences. \item $ G $ has a $ (2k+1) $ -orientation. \item $ G $ has a $ 2 + \frac{1}{k} $ -flow. \item $ G^* $ has a $ 2 + \frac{1}{k} $ -coloring. \item $ G^* $ has a homomorphism to $ C_{2k+1} $ . There is an easy family of graphs which show that the above conjecture (if true) is best possible. Let $ H_k $ be the graph obtained from an odd circuit of length $ 4k-1 $ by adding a new vertex $ u $ joined to every existing vertex by a path of length $ 2k-1 $ . Now, $ H_k $ is a planar graph of girth $ 4k-1 $ , but there is no homomorphism from $ H_k $ to $ C_{2k+1} $ . To see the latter claim, suppose (for a contradiction) that such a homomorphsim $ f $ exists, let $ C $ be the unique circuit of $ H_k \setminus u $ and let $ a=f(u) $ . Now, no vertex in $ C $ can map to $ a $ since every such vertex is distance $ 2k-1 $ from $ u $ . However we must then have a homomorphism from $ C $ to $ C_{2k+1} \setminus a $ , which is impossible since $ C $ is an odd circuit and $ C_{2k+1} \setminus u $ is bipartite. The k=1 case of the above conjecture asserts that every (loopless) triangle free planar graph has a homomorphism to the triangle. In other words, every (loopless) triangle free planar graph is 3-colorable. This is a well known theorem of Grotszch. For every k>1, the above conjecture is still open. Actually, I think this conjecture is already quite interesting for k=2. One reason is that this case of the conjecture implies the 5-color theorem for planar graphs. To see this implication, suppose that the above conjecture is true for k=2, let G be a simple loopless planar graph, and let G' be the graph obtained from G by subdividing each edge two times. Now, G' has girth at least 9, so by our assumption there is a homomorphism from G' to C_5. It is easy to see that adjacent vertices of G must map to different vertices of C_5 under this homomorphism. Thus, we have a proper 5-coloring of G as desired. Let us call a homomorphism to $ C_{2k+1} $ a $ C_{2k+1} $ - coloring . It is quite easy to show that every planar graph of girth > 10k has a $ C_{2k+1} $ -coloring. This follows from a simple degeneracy argument: Every such (nonempty) graph must have a either a vertex of degree $ \le 1 $ , or a path $ P $ of length $ 2k-1 $ all of whose internal vertices have degree two. Both of these configurations are reducible, in the sense that we may delete either a vertex of degree $ \le 1 $ or the interior vertices of $ P $ and then extend any $ C_{2k+1} $ -coloring of the resulting graph to a $ C_{2k+1} $ -coloring of the original. By more complicated, but similar degeneracy arguments, we can approach this conjecture. To my knowledge, the best result to date is as follows. Theorem (Borodin, Kim, Kostochka, West) Every planar graph of girth $ \ge \frac{20k-2}{3} $ has a homomorphism to $ C_{2k+1} $ . For the special case of the conjecture when $ k=2 $ , Matt DeVos and Adam Deckelbaum have an unpublished improvement showing that every planar graph with odd girth $ \ge 11 $ has a homomorphism to $ C_5 $ .

=== References listed by OpenProblemGarden ===
- [BKKW] O. V. Borodin, S. J. Kim, A. V. Kostochka, D. B. West, Homomorphisms from sparse graphs with large girth. Dedicated to Adrian Bondy and U. S. R. Murty. J. Combin. Theory Ser. B 90 (2004), no. 1, 147--159. MathSciNet
- [Ja] F. Jaeger, On circular flows in graphs in Finite and Infinite Sets, volume 37 of Colloquia Mathematica Societatis Janos Bolyai, edited by A. Hajnal, L. Lovasz, and V.T. Sos. North-Holland (1981) 391-402.
- [Zh] X. Zhu, Circular chromatic number of planar graphs of large odd girth, Electronic Journal of Combinatorics Vol. 8 no. 1 (2001).

=== Catalog page (statement + literature review) ===
Mapping planar graphs to odd cycles — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Jaeger's conjecture remains open for all $k \ge 2$. Significant partial progress has been made in specific cases: for $k=2$ the girth hypothesis for a $C_5$ homomorphism has been reduced to $\ge 10$ (Dvo\u0159\u00e1k\u2013Postle 2014); for $k=3$, girth $\ge 16$ suffices for a $C_7$ homomorphism (Postle\u2013Smith-Roberge 2019); and for $k=4$, odd-girth $\ge 23$ suffices for $C_9$ (Cranston\u2013Li\u2013Wang\u2013Wei 2024), all improving on the 2004 Borodin\u2013Kim\u2013Kostochka\u2013West bound.

 Cited literature (4)

 
 
 
partial Planar Graphs of Odd-Girth at Least 9 are Homomorphic to the Petersen Graph
 (2008)
 

 
 Zdeněk Dvořák, Riste Škrekovski, Tomáš Valla · SIAM Journal on Discrete Mathematics · doi:10.1137/060650507

Every planar graph of odd-girth at least 9 is $(5,2)$-colorable and admits a homomorphism to the Petersen graph (fractional chromatic number $\le 5/2$), relevant to the $k=2$ case.
 

 
 
partial Density of 5/2-critical graphs
 (2014)
 

 
 Zdeněk Dvořák, Luke Postle · arXiv preprint · arXiv:1411.6668

Every planar or projective-planar graph of girth at least 10 admits a homomorphism to $C_5$, improving the BKKW bound of girth $\ge 13$ for $k=2$ (conjecture predicts girth $\ge 8$ suffices).
 

 
 
partial On the Density of C7-Critical Graphs
 (2019)
 

 
 Luke Postle, Evelyne Smith-Roberge · arXiv preprint · arXiv:1903.04453

Every planar graph of girth at least 16 admits a homomorphism to $C_7$, improving the BKKW bound of girth $\ge 20$ for $k=3$ (conjecture predicts girth $\ge 12$ suffices).
 

 
 
partial Planar Graphs with Homomorphisms to the 9-cycle
 (2024)
 

 
 Daniel W. Cranston, Jiaao Li, Zhouningxin Wang, Chunyan Wei · arXiv preprint · arXiv:2402.02689 · doi:10.48550/arXiv.2402.02689

Every planar graph of odd-girth at least 23 admits a homomorphism to $C_9$, improving the Lovász–Thomassen–Wu–Zhang general bound of odd-girth $\ge 6k+1=25$ for $k=4$ (conjecture predicts girth $\ge 16$ suffices).
 

 

 Reviewer notes. The Lovász–Thomassen–Wu–Zhang 2013 general result (odd-girth ≥ 6k+1 → C_{2k+1} homomorphism for planar graphs) is cited in Cranston et al. 2024 but no directly accessible URL was found to independently verify it, so it is not listed in since_posted. The Dvořák–Postle and Postle–Smith-Roberge papers were published in Combinatorica (DOIs 10.1007/s00493-016-3356-3 and 10.1007/s00493-020-4177-y respectively per search metadata) but those Springer pages required authentication; only the arXiv preprint versions are cited here. The Dvořák–Škrekovski–Valla (2008) result targets the Petersen graph rather than C_5 directly; a Petersen homomorphism does not imply a C_5 homomorphism. The k=2 gap (girth ≥ 8 conjectured, girth ≥ 10 known) and k=3 gap (girth ≥ 12 conjectured, girth ≥ 16 known) show the conjecture remains substantially open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. Every planar graph of girth $ \ge 4k $ has a homomorphism to $ C_{2k+1} $ .

Keywords:
girth · homomorphism · planar graph

Discussion

This conjecture is Jaeger's modular orientation conjecture restricted to planar graphs and then dualized. To see this duality, first note that circular coloring and circular flows are dual for planar graphs, and then observe that $ (2k+1) $ -orientations are equivalent to $ 2 + \frac{1}{k} $ -flows and $ 2 + \frac{1}{k} $ -colorings are equivalent to homomorphisms to $ C_{2k+1} $ . So if $ G $ and $ G^* $ are dual planar graphs, then we have the following equivalences. \item $ G $ has a $ (2k+1) $ -orientation. \item $ G $ has a $ 2 + \frac{1}{k} $ -flow. \item $ G^* $ has a $ 2 + \frac{1}{k} $ -coloring. \item $ G^* $ has a homomorphism to $ C_{2k+1} $ . There is an easy family of graphs which show that the above conjecture (if true) is best possible. Let $ H_k $ be the graph obtained from an odd circuit of length $ 4k-1 $ by adding a new vertex $ u $ joined to every existing vertex by a path of length $ 2k-1 $ . Now, $ H_k $ is a planar graph of girth $ 4k-1 $ , but there is no homomorphism from $ H_k $ to $ C_{2k+1} $ . To see the latter claim, suppose (for a contradiction) that such a homomorphsim $ f $ exists, let $ C $ be the unique circuit of $ H_k \setminus u $ and let $ a=f(u) $ . Now, no vertex in $ C $ can map to $ a $ since every such vertex is distance $ 2k-1 $ from $ u $ . However we must then have a homomorphism from $ C $ to $ C_{2k+1} \setminus a $ , which is impossible since $ C $ is an odd circuit and $ C_{2k+1} \setminus u $ is bipartite. The k=1 case of the above conjecture asserts that every (loopless) triangle free planar graph has a homomorphism to the triangle. In other words, every (loopless) triangle free planar graph is 3-colorable. This is a well known theorem of Grotszch. For every k>1, the above conjecture is still open. Actually, I think this conjecture is already quite interesting for k=2. One reason is that this case of the conjecture implies the 5-color theorem for planar graphs. To see this implication, suppose that the above conjecture is true for k=2, let G be a simple loopless planar graph, and let G' be the graph obtained from G by subdividing each edge two times. Now, G' has girth at least 9, so by our assumption there is a homomorphism from G' to C_5. It is easy to see that adjacent vertices of G must map to different vertices of C_5 under this homomorphism. Thus, we have a proper 5-coloring of G as desired. Let us call a homomorphism to $ C_{2k+1} $ a $ C_{2k+1} $ - coloring . It is quite easy to show that every planar graph of girth > 10k has a $ C_{2k+1} $ -coloring. This follows from a simple degeneracy argument: Every such (nonempty) graph must have a either a vertex of degree $ \le 1 $ , or a path $ P $ of length $ 2k-1 $ all of whose internal vertices have degree two. Both of these configurations are reducible, in the sense that we may delete either a vertex of degree $ \le 1 $ or the interior vertices of $ P $ and then extend any $ C_{2k+1} $ -coloring of the resulting graph to a $ C_{2k+1} $ -coloring of the original. By more complicated, but similar degeneracy arguments, we can approach this conjecture. To my knowledge, the best result to date is as follows. Theorem (Borodin, Kim, Kostochka, West) Every planar graph of girth $ \ge \frac{20k-2}{3} $ has a homomorphism to $ C_{2k+1} $ . For the special case of the conjecture when $ k=2 $ , Matt DeVos and Adam Deckelbaum have an unpublished improvement showing that every planar graph with odd girth $ \ge 11 $ has a homomorphism to $ C_5 $ .

Bibliography

 [BKKW]
 O. V. Borodin, S. J. Kim, A. V. Kostochka, D. B. West, Homomorphisms from sparse graphs with large girth. Dedicated to Adrian Bondy and U. S. R. Murty. J. Combin. Theory Ser. B 90 (2004), no. 1, 147--159. MathSciNet
 MathSciNet

 [Ja]
 F. Jaeger, On circular flows in graphs in Finite and Infinite Sets, volume 37 of Colloquia Mathematica Societatis Janos Bolyai, edited by A. Hajnal, L. Lovasz, and V.T. Sos. North-Holland (1981) 391-402.

 [Zh]
 X. Zhu, Circular chromatic number of planar graphs of large odd girth, Electronic Journal of Combinatorics Vol. 8 no. 1 (2001).

Related conjectures

 
 implied by
 Jaeger's modular orientation conjecture
 disproved
 Let G be planar with girth >= 4k and let G* be its planar dual. Cycles of G correspond to minimal edge cuts of G*, so girth(G) >= 4k makes G* 4k-edge-connected. Jaeger's conjecture applied to G* gives a modular (2k+1)-orientation, which Jaeger showed is equivalent to a circular (2+1/k)-flow of G*; by planar flow/coloring duality this is a (2+1/k)-circular-coloring of G, i.e., a homomorphism G -> C_{2k+1}. The target's OPG page states this explicitly: 'This conjecture is Jaeger's modular orientation conjecture restricted to planar graphs and then dualized,' listing the chain of equivalences. Direction correct: the general-graph orientation conjecture is stronger. Note the source is now disproved for k >= 3 (Han-Li-Wu-Zhang), which does not affect the implication; the planar/dual case remains open.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
