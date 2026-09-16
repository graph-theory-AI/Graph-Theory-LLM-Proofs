Attack the following open graph-theory problem.

Catalog id: coloring_and_immersion
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/coloring_and_immersion/
Original entry: http://www.openproblemgarden.org/op/coloring_and_immersion
Problem attributed to: Abu-Khzam, Faisal N., Langston, Michael A. (posted 2007-09-04)

=== Problem statement (OpenProblemGarden) ===
Title: Coloring and immersion
Conjecture For every positive integer $ t $ , every (loopless) graph $ G $ with $ \chi(G) \ge t $ immerses $ K_t $ .

=== Discussion / context (OpenProblemGarden) ===
Let $ G $ be a graph and let $ uv, vw \in E(G) $ . The operation of deleting the edges $ uv $ and $ vw $ and then adding a new edge between $ v $ and $ w $ is called a split . We say that a graph $ G $ immerses a graph $ H $ if a graph isomorphic to $ H $ may be obtained from $ G $ by repeatedly making splits and deleting vertices and edges. The graph containment relations of minor and topological minor have been thoroughly studied with respect to graph coloring. In particular, there are two famous conjectures: Hajos conjectured that every graph with chromatic number $ \ge t $ contains a subdivision of the complete graph $ K_t $ as a subgraph. Hadwiger conjectured that every graph with chromatic number $ \ge t $ contains $ K_t $ as a minor. While Hajos' Conjecture is false for $ t \ge 8 $ (indeed it is actually false on average), Hadwiger's Conjecture remains open, and is one of the outstanding problems in Graph Theory. On the other hand, the relationship between graph coloring and immersions seems to have been largely ignored until Abu-Khzam and Langston made the above conjecture. In addition to formulating this conjecture, they proved it for $ t \le 4 $ and showed that a minimal counterexample to it must be 4-connected and $ t $ -edge-connected. Recently, DeVos, Kawarabayashi, Mohar, and Okamura have resolved the conjecture for $ t \le 7 $ .

=== References listed by OpenProblemGarden ===
- * Faisal N. Abu-Khzam and Michael A. Langston, Graph Coloring and the Immersion Order

=== Catalog page (statement + literature review) ===
Coloring and immersion — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that every graph $G$ with $\chi(G) \ge t$ immerses $K_t$ remains open in full generality. Post-posting, DeVos–Kawarabayashi–Mohar–Okamura (2010) confirmed it for $t \le 7$ via the stronger fact that minimum degree $t-1$ suffices; Gauthier–Le–Wollan (2017) showed chromatic number at least $3.54t+4$ guarantees a $K_t$-immersion; and Fox–Pach–Suk (2025) proved the conjecture for graphs on at most $(1.64-o(1))t$ vertices.

 Cited literature (3)

 
 
 
partial Immersing small complete graphs
 (2010)
 

 
 Matt DeVos, Ken-ichi Kawarabayashi, Bojan Mohar, Haruko Okamura · Ars Mathematica Contemporanea

Proves the conjecture for $t \le 7$ via the stronger result that every graph with minimum degree $t-1$ immerses $K_t$.
 

 
 
partial Forcing clique immersions through chromatic number
 (2017)
 

 
 Gregory Gauthier, Tien-Nam Le, Paul Wollan · arXiv preprint · arXiv:1703.08235

Shows that every graph with chromatic number at least $3.54t+4$ immerses $K_t$, a linear sufficient condition weaker than the conjectured threshold of $t$.
 

 
 
partial Immersions and Albertson's conjecture
 (2025)
 

 
 Jacob Fox, Janos Pach, Andrew Suk · arXiv preprint · arXiv:2510.05893

Proves the Abu-Khzam–Langston/Lescure–Meyniel conjecture for graphs on at most $(1.64-o(1))k$ vertices, where $k$ is the chromatic number.
 

 

 Reviewer notes. The conjecture was independently formulated by Lescure and Meyniel in 1989, predating Abu-Khzam–Langston. No journal publication was located for the Gauthier–Le–Wollan arXiv preprint (1703.08235). The Fox–Pach–Suk (2025) paper targets Albertson's crossing-number conjecture but proves the immersion conjecture as an intermediate result for graphs with at most $(1.64-o(1))k$ vertices; it is an arXiv preprint as of the review date. The conjecture itself remains fully open for all $t$.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 152s.
 

Conjecture. For every positive integer $ t $ , every (loopless) graph $ G $ with $ \chi(G) \ge t $ immerses $ K_t $ .

Keywords:
coloring · complete graph · immersion

Discussion

Let $ G $ be a graph and let $ uv, vw \in E(G) $ . The operation of deleting the edges $ uv $ and $ vw $ and then adding a new edge between $ v $ and $ w $ is called a split . We say that a graph $ G $ immerses a graph $ H $ if a graph isomorphic to $ H $ may be obtained from $ G $ by repeatedly making splits and deleting vertices and edges. The graph containment relations of minor and topological minor have been thoroughly studied with respect to graph coloring. In particular, there are two famous conjectures: Hajos conjectured that every graph with chromatic number $ \ge t $ contains a subdivision of the complete graph $ K_t $ as a subgraph. Hadwiger conjectured that every graph with chromatic number $ \ge t $ contains $ K_t $ as a minor. While Hajos' Conjecture is false for $ t \ge 8 $ (indeed it is actually false on average), Hadwiger's Conjecture remains open, and is one of the outstanding problems in Graph Theory. On the other hand, the relationship between graph coloring and immersions seems to have been largely ignored until Abu-Khzam and Langston made the above conjecture. In addition to formulating this conjecture, they proved it for $ t \le 4 $ and showed that a minimal counterexample to it must be 4-connected and $ t $ -edge-connected. Recently, DeVos, Kawarabayashi, Mohar, and Okamura have resolved the conjecture for $ t \le 7 $ .

Bibliography

★ [?]
 Faisal N. Abu-Khzam and Michael A. Langston, Graph Coloring and the Immersion Order
 Graph Coloring and the Immersion Order
