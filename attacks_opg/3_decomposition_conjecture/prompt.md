Attack the following open graph-theory problem.

Catalog id: 3_decomposition_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/3_decomposition_conjecture/
Original entry: http://www.openproblemgarden.org/op/3_decomposition_conjecture
Problem attributed to: Arthur, Hoffmann-Ostenhof (posted 2017-01-24)

=== Problem statement (OpenProblemGarden) ===
Title: 3-Decomposition Conjecture
Conjecture (3-Decomposition Conjecture) Every connected cubic graph $ G $ has a decomposition into a spanning tree, a family of cycles and a matching.

=== Discussion / context (OpenProblemGarden) ===
We state the conjecture in a more precise manner: Let $ G $ be a connected cubic graph. Then $ G $ contains a spanning tree $ H_1 $ , a $ 2 $ -regular subgraph $ H_2 $ and a matching $ H_3 $ (where only $ H_3 $ and not $ H_1 $ or $ H_2 $ may be empty) such that $ E(H_1) \cup E(H_2) \cup E(H_3) = E(G) $ and $ E(H_i) \cap E(H_j) =\emptyset $ for every $ \{i,j\} \subseteq \{1,2,3\} $ with $ i\not=j $ . The conjecture holds for all hamiltionian cubic graphs and for all connected planar cubic graphs, see [1] and see also [7]. Every cubic graph G which has a spanning tree T such that every vertex of T has degree three or one (such spanning tree T is called a HIST) obviously satisfies this conjecture. But not every connected cubic graph has a HIST, see [2]. The 3-Decomposition Conjecture has been shown to be equivalent to the following conjecture: Conjecture (2-Decomposition Conjecture) Let $ G $ be connected graph where every vertex has degree two or three. Suppose that for every cycle $ C $ of $ G $ , $ G-E(C) $ is disconnected, then $ G $ has a decomposition into a spanning tree $ T $ and a matching $ M $ , i.e $ G-M=T $ . Note that every cycle $ C $ which passes through a vertex of degree two satisfies the condition that G-E(C) is disconnected. Remark: The 3-Decomposition Conjecture has also been shown to hold for other classes of cubic graphs, see for instance [3,4]. A survey on the 3-Decompostion conjecture has been given by the author 2015 in Pilsen (at that time the planar case was still open) see iti.zcu.cz/plzen15/talks/1-2a-Arthur-Survey_decomposition.ppt (and press play if you find the play button). Note that there are several papers on the problem whether a planar graph $ G $ has a matching $ M $ such that $ G-M $ is acyclic, see for instance [6].

=== References listed by OpenProblemGarden ===
- [1] Arthur Hoffmann-Ostenhof, Tomáš Kaiser, Kenta Ozeki, \arXiv[Decomposing planar cubic graphs] 1609.05059 [math.CO]
 [2] Arthur Hoffmann-Ostenhof, Kenta Ozeki, \arXiv[On HISTs in Cubic Graphs] 1507.07689 [math.CO]
 [3] F. Abdolhosseini, S. Akbari, H. Hashemi, M.S. Moradian, \arXiv[Hoffmann-Ostenhof's conjecture for traceable cubic graphs] 1607.04768[math.CO] 
 [4] Anna Bachstein, Dong Ye (talk): www.rwoodroofe.math.msstate.edu/workshop2014/bachstein_slides.pdf
 [5] Arthur Hoffmann-Ostenhof (talk): www.iti.zcu.cz/plzen15/talks/1-2a-Arthur-Survey_decomposition.ppt
 [6] Yingqian Wang, Qijun Zhang, Discrete Mathematics 311 (2011) 844–849, Decomposing a planar graph with girth at least 8 into a forest and a matching
 [7] Kenta Ozeki, Dong Ye, Decomposing plane cubic graphs, European Journal of Combinatorics 52 (2016) 40-46.

=== Catalog page (statement + literature review) ===
3-Decomposition Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The 3-Decomposition Conjecture remains open for general connected cubic graphs. Since the 2017 posting, the conjecture has been verified for claw-free cubic graphs, claw-free and 4-chordal subcubic graphs, 3-connected star-like graphs, and 3-connected graphs of tree-width at most 3 or path-width at most 4; computational verification has been extended to all cubic graphs on at most 28 vertices. All evidence indicates the full conjecture is still unproved.

 Cited literature (5)

 
 
 
partial Decomposing Claw-free Subcubic Graphs and 4-Chordal Subcubic Graphs
 (2018)
 

 
 Elham Aboomahigir, Milad Ahanjideh, Saieed Akbari · arXiv preprint · arXiv:1806.11009

Proves Hoffmann-Ostenhof's conjecture for connected claw-free subcubic graphs and for connected 4-chordal subcubic graphs.
 

 
 
partial Hoffmann-Ostenhof's conjecture for claw-free cubic graphs
 (2018)
 

 
 Milad Ahanjideh, Elham Aboomahigir · arXiv preprint · arXiv:1810.00074

Establishes the 3-decomposition conjecture for the class of connected claw-free cubic graphs.
 

 
 
partial Reductions for the 3-Decomposition Conjecture
 (2021)
 

 
 Oliver Bachtler, Irene Heinrich · arXiv preprint · arXiv:2104.15113

Proves the conjecture for all 3-connected cubic graphs of tree-width at most 3 or path-width at most 4, identifies several reducible configurations (triangle, $K_{2,3}$, etc.), and computationally verifies the conjecture for all cubic graphs on at most 20 vertices.
 

 
 
partial Towards Obtaining a 3-Decomposition From a Perfect Matching
 (2022)
 

 
 Oliver Bachtler, Sven O. Krumke · Electronic Journal of Combinatorics · arXiv:2008.09549

Proves the conjecture for 3-connected star-like cubic graphs (those whose 2-factor, when contracted, yields a star graph), generalising the previously known Hamiltonian case.
 

 
 
partial The 3-Decomposition Conjecture: A SAT-Based Approach with Specialized Propagators
 (2025)
 

 
 Tianwei Zhang, Stefan Szeider · 31st International Conference on Principles and Practice of Constraint Programming (CP 2025) · doi:10.4230/LIPIcs.CP.2025.39

Using a SAT / Satisfiability Modulo Symmetries framework augmented with specialised propagators exploiting properties of minimal counterexamples, computationally verifies the conjecture for all connected cubic graphs on at most 28 vertices.
 

 

 Reviewer notes. Two 2025 papers appeared in searches but could not be fetched for content verification (HTTP 403 or auth redirect): (1) 'Hoffmann-Ostenhof's 3-Decomposition Conjecture' (Fan and Zhou, Discrete Mathematics 348:114454, 2025, pii/S0012365X25000627), reportedly proving a quantitative partial result bounding the number of $P_2$ paths in a near-decomposition; (2) 'The 3-decomposition conjecture of cubic graphs' (Fan, Guo, Zhou, Science China Mathematics, DOI 10.1007/s11425-025-2498-x), apparently a similar partial result. Neither could be cited per rules. The paper at Springer redirected to an authentication portal; the ScienceDirect page returned 403. A third unverified 2020 ScienceDirect paper 'Decomposition of cubic graphs with a 2-factor consisting of three cycles' (pii/S0012365X20300303) also appeared consistently in searches but 403'd. No source found suggesting the full conjecture has been resolved.

 
 Auto-reviewed 2026-05-07 with claude-sonnet-4-6 (web search enabled) · 195s.
 

Conjecture. (3-Decomposition Conjecture) Every connected cubic graph $ G $ has a decomposition into a spanning tree, a family of cycles and a matching.

Keywords:
cubic graph

Discussion

We state the conjecture in a more precise manner: Let $ G $ be a connected cubic graph. Then $ G $ contains a spanning tree $ H_1 $ , a $ 2 $ -regular subgraph $ H_2 $ and a matching $ H_3 $ (where only $ H_3 $ and not $ H_1 $ or $ H_2 $ may be empty) such that $ E(H_1) \cup E(H_2) \cup E(H_3) = E(G) $ and $ E(H_i) \cap E(H_j) =\emptyset $ for every $ \{i,j\} \subseteq \{1,2,3\} $ with $ i\not=j $ . The conjecture holds for all hamiltionian cubic graphs and for all connected planar cubic graphs, see [1] and see also [7]. Every cubic graph G which has a spanning tree T such that every vertex of T has degree three or one (such spanning tree T is called a HIST) obviously satisfies this conjecture. But not every connected cubic graph has a HIST, see [2]. The 3-Decomposition Conjecture has been shown to be equivalent to the following conjecture: Conjecture (2-Decomposition Conjecture) Let $ G $ be connected graph where every vertex has degree two or three. Suppose that for every cycle $ C $ of $ G $ , $ G-E(C) $ is disconnected, then $ G $ has a decomposition into a spanning tree $ T $ and a matching $ M $ , i.e $ G-M=T $ . Note that every cycle $ C $ which passes through a vertex of degree two satisfies the condition that G-E(C) is disconnected. Remark: The 3-Decomposition Conjecture has also been shown to hold for other classes of cubic graphs, see for instance [3,4]. A survey on the 3-Decompostion conjecture has been given by the author 2015 in Pilsen (at that time the planar case was still open) see iti.zcu.cz/plzen15/talks/1-2a-Arthur-Survey_decomposition.ppt (and press play if you find the play button). Note that there are several papers on the problem whether a planar graph $ G $ has a matching $ M $ such that $ G-M $ is acyclic, see for instance [6].

Bibliography

 [1]
 Arthur Hoffmann-Ostenhof, Tomáš Kaiser, Kenta Ozeki, \arXiv[Decomposing planar cubic graphs] 1609.05059 [math.CO] [2] Arthur Hoffmann-Ostenhof, Kenta Ozeki, \arXiv[On HISTs in Cubic Graphs] 1507.07689 [math.CO] [3] F. Abdolhosseini, S. Akbari, H. Hashemi, M.S. Moradian, \arXiv[Hoffmann-Ostenhof's conjecture for traceable cubic graphs] 1607.04768[math.CO] [4] Anna Bachstein, Dong Ye (talk): www.rwoodroofe.math.msstate.edu/workshop2014/bachstein_slides.pdf [5] Arthur Hoffmann-Ostenhof (talk): www.iti.zcu.cz/plzen15/talks/1-2a-Arthur-Survey_decomposition.ppt [6] Yingqian Wang, Qijun Zhang, Discrete Mathematics 311 (2011) 844–849, Decomposing a planar graph with girth at least 8 into a forest and a matching [7] Kenta Ozeki, Dong Ye, Decomposing plane cubic graphs, European Journal of Combinatorics 52 (2016) 40-46.
