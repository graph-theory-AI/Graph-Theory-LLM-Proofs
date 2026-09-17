Attack the following open graph-theory problem.

Catalog id: vertex_coloring_of_graph_fractional_powers
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/vertex_coloring_of_graph_fractional_powers/
Original entry: http://www.openproblemgarden.org/op/vertex_coloring_of_graph_fractional_powers
Problem attributed to: Iradmusa, Moharram (posted 2011-04-23)

=== Problem statement (OpenProblemGarden) ===
Title: Vertex Coloring of graph fractional powers
Conjecture Let $ G $ be a graph and $ k $ be a positive integer. The $ k- $ power of $ G $ , denoted by $ G^k $ , is defined on the vertex set $ V(G) $ , by connecting any two distinct vertices $ x $ and $ y $ with distance at most $ k $ . In other words, $ E(G^k)=\{xy:1\leq d_G(x,y)\leq k\} $ . Also $ k- $ subdivision of $ G $ , denoted by $ G^\frac{1}{k} $ , is constructed by replacing each edge $ ij $ of $ G $ with a path of length $ k $ . Note that for $ k=1 $ , we have $ G^\frac{1}{1}=G^1=G $ . Now we can define the fractional power of a graph as follows: Let $ G $ be a graph and $ m,n\in \mathbb{N} $ . The graph $ G^{\frac{m}{n}} $ is defined by the $ m- $ power of the $ n- $ subdivision of $ G $ . In other words $ G^{\frac{m}{n}}\isdef (G^{\frac{1}{n}})^m $ . Conjecture. Let $ G $ be a connected graph with $ \Delta(G)\geq3 $ and $ m $ be a positive integer greater than 1. Then for any positive integer $ n>m $ , we have $ \chi(G^{\frac{m}{n}})=\omega(G^\frac{m}{n}) $ . In [1], it was shown that this conjecture is true in some special cases.

=== References listed by OpenProblemGarden ===
- [1] Iradmusa, Moharram N., On colorings of graph fractional powers. Discrete Math. 310 (2010), no. 10-11, 1551–1556.

=== Catalog page (statement + literature review) ===
Vertex Coloring of graph fractional powers — Graph-theory open problems

 
 Status
 disproved
 medium confidence
 

 Hartke, Liu, and Petříčková (2012) disproved the conjecture by constructing a graph $H$ for which $\chi(H^{3/5}) > \omega(H^{3/5})$ (taking $m=3$, $n=5$ satisfies $n > m$). They also showed the conjecture holds when $m$ is even, and established the weaker bound $\chi(G^{m/n}) \leq \omega(G^{m/n}) + 2$ for odd $m$ and $\Delta(G) \geq 4$.

 Cited literature (1)

 
 
 
counterexample On coloring of fractional powers of graphs
 (2012)
 

 
 Stephen Hartke, Hong Liu, Šárka Petříčková · arXiv preprint · arXiv:1212.3898

Disproves the conjecture by exhibiting a graph H with χ(H^{3/5}) > ω(H^{3/5}); also proves the conjecture holds when m is even and gives χ(G^{m/n}) ≤ ω(G^{m/n}) + 2 for odd m and Δ(G) ≥ 4.
 

 

 Reviewer notes. The Hartke–Liu–Petříčková PDF directly verifies the conjecture statement and the counterexample $\chi(H^{3/5})>\omega(H^{3/5})$. The result appears to exist only as an arXiv preprint (1212.3898; submitted December 2012, PDF timestamp November 2018); no journal publication was found, which lowers confidence to medium. Additional follow-up papers were found in search results — 'Coloring 3-power of 3-subdivision of subcubic graph' (WorldScientific, 2018) and 'A Short Proof of 7-Colorability of 3/3-Power of Subcubic Graphs' (Springer, 2020) — but these address the case n = m (outside the conjecture's scope n > m). An Opuscula Mathematica 2023 paper on incidence coloring of fractional powers cites the Hartke-Liu-Petříčková arXiv preprint and a 2025 Indonesian Journal of Combinatorics paper explicitly mentions their counterexample.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Let $ G $ be a graph and $ k $ be a positive integer. The $ k- $ power of $ G $ , denoted by $ G^k $ , is defined on the vertex set $ V(G) $ , by connecting any two distinct vertices $ x $ and $ y $ with distance at most $ k $ . In other words, $ E(G^k)=\{xy:1\leq d_G(x,y)\leq k\} $ . Also $ k- $ subdivision of $ G $ , denoted by $ G^\frac{1}{k} $ , is constructed by replacing each edge $ ij $ of $ G $ with a path of length $ k $ . Note that for $ k=1 $ , we have $ G^\frac{1}{1}=G^1=G $ . Now we can define the fractional power of a graph as follows: Let $ G $ be a graph and $ m,n\in \mathbb{N} $ . The graph $ G^{\frac{m}{n}} $ is defined by the $ m- $ power of the $ n- $ subdivision of $ G $ . In other words $ G^{\frac{m}{n}}\isdef (G^{\frac{1}{n}})^m $ . Conjecture. Let $ G $ be a connected graph with $ \Delta(G)\geq3 $ and $ m $ be a positive integer greater than 1. Then for any positive integer $ n>m $ , we have $ \chi(G^{\frac{m}{n}})=\omega(G^\frac{m}{n}) $ . In [1], it was shown that this conjecture is true in some special cases.

Keywords:
chromatic number, fractional power of graph, clique number

Bibliography

 [1]
 Iradmusa, Moharram N., On colorings of graph fractional powers. Discrete Math. 310 (2010), no. 10-11, 1551–1556.
