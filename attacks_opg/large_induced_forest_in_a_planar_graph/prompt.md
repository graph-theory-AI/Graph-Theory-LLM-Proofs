Attack the following open graph-theory problem.

Catalog id: large_induced_forest_in_a_planar_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/large_induced_forest_in_a_planar_graph/
Original entry: http://www.openproblemgarden.org/op/large_induced_forest_in_a_planar_graph
Problem attributed to: Abertson, Michael O., Berman, David M. (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Large induced forest in a planar graph.
Conjecture Every planar graph on $ n $ verices has an induced forest with at least $ n/2 $ vertices.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is best possible. (See [AW]). It follows from Borodin's theorem stating that every planar graph has an acyclic $ 5 $ -colouring that every planar graph on $ n $ verices has an induced forest with at least $ 2n/5 $ vertices. The conjecture holds for planar graph with girth at least $ 5 $ , because they can be partitionned into a stable set and a forest [BG] (see also [KT]). Akiyama-Watanabe [AW] conjectured an even larger induced forest for bipartite planar graphs. Conjecture Every bipartite planar graph on $ n $ verices has an induced forest with at least $ 5n/8 $ vertices. This conjecture is also best possible. (See [AW]).

=== References listed by OpenProblemGarden ===
- *[AB] M. O. Albertson and D. M. Berman. A conjecture on planar graphs. Graph Theory and Related Topics (J. A. Bondy and U. S. R. Murty, eds.), (Academic Press, 1979), 357.
- [AW] J. Akiyama and M. Watanabe. Maximum induced forests of planar graphs. Graphs and Combinatorics 3 (1987), 201--202.
- [B] O. V. Borodin. A proof of B. Grünbaum's conjecture on the acyclic 5-colorability of planar graphs. (Russian) Dokl. Akad. Nauk SSSR 231 (1976), no. 1, 18--20.
- [BG] O. V. Borodin and A. N. Glebov. On the partition of a planar graph of girth 5 into an empty graph and an acyclic subgraph. Diskretn. Anal. Issled. Oper. Ser. 1 8:34–53, 2001
- [KT] K. Kawarabayashi and C. Thomassen. Decomposing a planar graph of girth 5 into an independent set and a forest. Journal of Combinatorial Theory, Series B 99(4):674–684, 2009.

=== Catalog page (statement + literature review) ===
Large induced forest in a planar graph. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Albertson–Berman conjecture that every planar graph on $n$ vertices has an induced forest on at least $n/2$ vertices remains open; the best known lower bound for general planar graphs is still $2n/5$ from Borodin's acyclic 5-coloring theorem (proved before the problem was posted). Since 2013, meaningful partial progress has been made for special graph classes: improved bounds for triangle-free planar graphs (up to $(6n+7)/11$), for bipartite planar graphs (up to $\lceil(4n+3)/7\rceil$, toward the Akiyama–Watanabe conjecture of $5n/8$), and an extension of the problem to multigraphs.

 Cited literature (5)

 
 
 
partial Large induced forests in planar graphs with girth 4 or 5
 (2014)
 

 
 François Dross, Mickael Montassier, Alexandre Pinlou · arXiv preprint · arXiv:1409.1348

Proves that every triangle-free planar graph on $n$ vertices has an induced forest on at least $(6n+7)/11$ vertices, and every planar graph of girth $\geq 5$ has one on at least $(44n+50)/69$ vertices, improving on Salavatipour's bounds.
 

 
 
partial A lower bound on the order of the largest induced forest in planar graphs with high girth
 (2015)
 

 
 François Dross, Mickael Montassier, Alexandre Pinlou · arXiv preprint · arXiv:1504.01949

Shows that a planar graph with girth $g$ and $m$ edges has a feedback vertex set of size at most $4m/(3g)$, improving on the trivial bound $2m/g$ and giving stronger induced-forest lower bounds for high-girth planar graphs.
 

 
 
partial Induced Forests in Bipartite Planar Graphs
 (2016)
 

 
 Yan Wang, Qiqin Xie, Xingxing Yu · arXiv preprint · arXiv:1605.00047

Proves via the discharging method that every simple bipartite planar graph on $n$ vertices contains an induced forest on at least $\lceil(4n+3)/7\rceil \approx 4n/7$ vertices, making progress toward the Akiyama–Watanabe conjecture of $5n/8$.
 

 
 
partial Contributions to conjectures on planar graphs: Induced Subgraphs, Treewidth, and Dominating Sets
 (2025)
 

 
 Kengo Enami, Naoki Matsumoto, Takamasa Yashima · arXiv preprint · arXiv:2506.10471

Establishes that if a planar graph has a $K_4$-minor-free induced subgraph of order at least $2n/3$, then it contains an induced forest of order at least $4n/9$, conditionally improving Borodin's $2n/5$ bound; also clarifies relations between induced outerplanar subgraphs and the Albertson–Berman conjecture.
 

 
 
partial Large induced forests in planar multigraphs
 (2026)
 

 
 Mikhail Makarov · arXiv preprint · arXiv:2601.04637

Extends the Albertson–Berman problem to multigraphs, proving $a(M) \geq n/4$ for any planar multigraph and the stronger bound $a(M) \geq 2n/5 - k/10$ when exactly $k$ vertex pairs carry parallel edges.
 

 

 Reviewer notes. The 2018 Springer paper 'A Better Bound on the Largest Induced Forests in Triangle-Free Planar Graph' by Dross, Montassier, Pinlou (Graphs and Combinatorics 34:1217–1246, 2018) reportedly improves the triangle-free bound further to 5n/9 ≈ 0.556n, but could not be verified via WebFetch due to paywall redirect; no arXiv preprint was found, so it was excluded from since_posted. The main Albertson–Berman conjecture for general planar graphs (best unconditional bound still 2n/5) remains open as of 2026.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. Every planar graph on $ n $ verices has an induced forest with at least $ n/2 $ vertices.

Discussion

This conjecture is best possible. (See [AW]). It follows from Borodin's theorem stating that every planar graph has an acyclic $ 5 $ -colouring that every planar graph on $ n $ verices has an induced forest with at least $ 2n/5 $ vertices. The conjecture holds for planar graph with girth at least $ 5 $ , because they can be partitionned into a stable set and a forest [BG] (see also [KT]). Akiyama-Watanabe [AW] conjectured an even larger induced forest for bipartite planar graphs. Conjecture Every bipartite planar graph on $ n $ verices has an induced forest with at least $ 5n/8 $ vertices. This conjecture is also best possible. (See [AW]).

Bibliography

★ [AB]
 M. O. Albertson and D. M. Berman. A conjecture on planar graphs. Graph Theory and Related Topics (J. A. Bondy and U. S. R. Murty, eds.), (Academic Press, 1979), 357.

 [AW]
 J. Akiyama and M. Watanabe. Maximum induced forests of planar graphs. Graphs and Combinatorics 3 (1987), 201--202.

 [B]
 O. V. Borodin. A proof of B. Grünbaum's conjecture on the acyclic 5-colorability of planar graphs. (Russian) Dokl. Akad. Nauk SSSR 231 (1976), no. 1, 18--20.

 [BG]
 O. V. Borodin and A. N. Glebov. On the partition of a planar graph of girth 5 into an empty graph and an acyclic subgraph. Diskretn. Anal. Issled. Oper. Ser. 1 8:34–53, 2001

 [KT]
 K. Kawarabayashi and C. Thomassen. Decomposing a planar graph of girth 5 into an independent set and a forest. Journal of Combinatorial Theory, Series B 99(4):674–684, 2009.

Related conjectures

 
 implied by
 Fractional vertex-arboricity ≤ 2 planar graphs
 open
 Standard fractional-covering bound, stated explicitly in the source paper's own context: |V(G)|/a(G) <= va_f(G), where a(G) is the maximum size of an induced forest. Proof: va_f is the minimum total weight of a fractional cover of V(G) by induced forests; if the total weight is w, then n = sum_v sum_{F containing v} w_F <= sum_F w_F |F| <= w * a(G). So va_f(G) <= 2 for every planar G forces a(G) >= n/2, exactly the Albertson-Berman conjecture (the target). Direction correct: the fractional statement is stronger; the converse is not claimed. Hypothesis classes match (all planar graphs on both sides).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
