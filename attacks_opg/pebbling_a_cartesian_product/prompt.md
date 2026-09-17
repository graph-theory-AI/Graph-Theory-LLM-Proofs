Attack the following open graph-theory problem.

Catalog id: pebbling_a_cartesian_product
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/pebbling_a_cartesian_product/
Original entry: http://www.openproblemgarden.org/op/pebbling_a_cartesian_product
Problem attributed to: Graham, Ronald L. (posted 2007-09-24)

=== Problem statement (OpenProblemGarden) ===
Title: Pebbling a cartesian product
We let $ p(G) $ denote the pebbling number of a graph $ G $ . Conjecture $ p(G_1 \Box G_2) \le p(G_1) p(G_2) $ .

=== Discussion / context (OpenProblemGarden) ===
The pebbling number of a graph $ G $ , denoted $ p(G) $ , is the smallest integer $ k $ so that however $ k $ pebbles are distributed onto the vertices of $ G $ , it is possible to move a pebble to any vertex by a sequence of steps, where in each step we remove two pebbles from one vertex, and then place one on an adjacent vertex. The cartesian product of two graphs $ G_1 $ and $ G_2 $ , denoted $ G_1 \Box G_2 $ , is the graph with vertex set $ V(G_1) \times V(G_2) $ and an edge from $ (v,w) $ to $ (v',w') $ if either $ v=v' $ and $ w \sim w' $ (in $ G_2 $ ) or $ w=w' $ and $ v \sim v' $ (in $ G_1 $ ). Graph Pebbling arose out of the study of zero-sum subsequences in groups, but has proved to be a rich and interesting topic in graph theory. See Glenn Hurlbert's wonderful graph pebbling page for much more on this topic (and this problem in particular). Graham's conjecture was stated in one of the first papers on this subject by Fan Chung [C], and has since generated considerable interest. There are a number of partial results toward this conjecture. Chung [C] proved that $ p(P_{d_1+1} \Box P_{d_2+1} \ldots \Box P_{d_{\ell}+1}) = 2^{d_1 + d_2 \ldots + d_{\ell}} $ , thus settling the conjecture for products of paths (here $ P_n $ denotes a path with $ n $ vertices). It is also known when $ G_1,G_2 $ are both trees, both cycles, and for graphs with high minimum degree. Again, we encourage the interested reader to see the graph pebbling page for more details.

=== References listed by OpenProblemGarden ===
- *[C] F. Chung, Pebbling in hypercubes SIAM J. Disc. Math. 2 (1989), 467--472.

=== Catalog page (statement + literature review) ===
Pebbling a cartesian product — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Graham's conjecture that $p(G_1 \Box G_2) \le p(G_1)p(G_2)$ remains open in full generality. Since the 2007 posting, the conjecture has been verified for additional graph families, including Cartesian products of middle graphs of some even cycles (Xia et al., 2017) and products with sufficiently large complete graphs (Pleanmani, 2020). The Lemke graph product $L \Box L$ is the key potential counterexample still under active investigation.

 Cited literature (2)

 
 
 
partial Graham's pebbling conjecture on Cartesian product of the middle graphs of even cycles
 (2017)
 

 
 Zheng-Jiang Xia, Yong-Liang Pan, Jun-Ming Xu, Xi-Ming Cheng · arXiv preprint · arXiv:1705.00191

Proves Graham's pebbling conjecture for Cartesian products of the middle graphs of some even cycles.
 

 
 
partial Graham's Pebbling Conjecture Holds for the Product of a Graph and a Sufficiently Large Complete Graph
 (2020)
 

 
 Nopparat Pleanmani · Theory and Applications of Graphs

Proves that $p(G \Box K_n) \le p(G)p(K_n)$ whenever $K_n$ has sufficiently large order relative to the graph parameters of $G$.
 

 

 Reviewer notes. The Pleanmani 2019 World Scientific paper on complete bipartite graphs could not be verified (HTTP 403) and was excluded. Yang, Yerger, and Zhou (2023/2024, arXiv:2310.00580) improve weight-function bounds for Q4 and lollipop graphs but do not directly address Graham's conjecture. Hurlbert and Seddiq (arXiv:2011.10623) proved the Target Pebbling Conjecture for 2-paths and Kneser graphs, which is a related but distinct problem. The Lemke graph Cartesian product L□L remains the canonical potential counterexample to Graham's conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. $ p(G_1 \Box G_2) \le p(G_1) p(G_2) $ .

Keywords:
pebbling · zero sum

Discussion

The pebbling number of a graph $ G $ , denoted $ p(G) $ , is the smallest integer $ k $ so that however $ k $ pebbles are distributed onto the vertices of $ G $ , it is possible to move a pebble to any vertex by a sequence of steps, where in each step we remove two pebbles from one vertex, and then place one on an adjacent vertex. The cartesian product of two graphs $ G_1 $ and $ G_2 $ , denoted $ G_1 \Box G_2 $ , is the graph with vertex set $ V(G_1) \times V(G_2) $ and an edge from $ (v,w) $ to $ (v',w') $ if either $ v=v' $ and $ w \sim w' $ (in $ G_2 $ ) or $ w=w' $ and $ v \sim v' $ (in $ G_1 $ ). Graph Pebbling arose out of the study of zero-sum subsequences in groups, but has proved to be a rich and interesting topic in graph theory. See Glenn Hurlbert's wonderful graph pebbling page for much more on this topic (and this problem in particular). Graham's conjecture was stated in one of the first papers on this subject by Fan Chung [C], and has since generated considerable interest. There are a number of partial results toward this conjecture. Chung [C] proved that $ p(P_{d_1+1} \Box P_{d_2+1} \ldots \Box P_{d_{\ell}+1}) = 2^{d_1 + d_2 \ldots + d_{\ell}} $ , thus settling the conjecture for products of paths (here $ P_n $ denotes a path with $ n $ vertices). It is also known when $ G_1,G_2 $ are both trees, both cycles, and for graphs with high minimum degree. Again, we encourage the interested reader to see the graph pebbling page for more details.

Bibliography

★ [C]
 F. Chung, Pebbling in hypercubes SIAM J. Disc. Math. 2 (1989), 467--472.
 Pebbling in hypercubes
