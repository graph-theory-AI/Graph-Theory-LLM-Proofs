Attack the following open graph-theory problem.

Catalog id: seagull_problem
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Minors
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/seagull_problem/
Original entry: http://www.openproblemgarden.org/op/seagull_problem
Problem attributed to: Seymour, Paul D. (posted 2008-01-06)

=== Problem statement (OpenProblemGarden) ===
Title: Seagull problem
Conjecture Every $ n $ vertex graph with no independent set of size $ 3 $ has a complete graph on $ \ge \frac{n}{2} $ vertices as a minor.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is significant because it is an interesting unproved consequence of Hadwiger's conjecture (this implication is proved next). In fact, some experts have suggested that this problem might hold the key to finding a counterexample to Hadwiger. I (M. DeVos) have attributed this conjecture to Seymour, but I believe that it may have been independently suggested by Mader and by others. Its curious title will be explained later in this discussion. Hadwiger's conjecture (every loopless graph with chromatic number $ \ge n $ has $ K_n $ as a minor) is one of the outstanding problems in graph theory. This conjecture has been resolved for small values of $ n $ ; when $ n \le 4 $ it is relatively easy, for $ n=5,6 $ it has been proven to be equivalent to the Four color theorem. The Seagull problem concerns the other extreme - when the size of the chromatic number is close to the order of the graph. If $ G $ is an $ n $ vertex graph with no independent set of size 3, then $ \chi(G) \ge \frac{n}{2} $ since each color class has size $ \le 2 $ . If Hadwiger's conjecture holds for $ G $ , it must then have a minor which is a complete graph on $ \ge \frac{n}{2} $ vertices. This is precisely the statement of the Seagull problem. The (essentially) best known bound for the conjecture is that every $ n $ vertex graph $ G $ with no independent set of size 3 has a complete graph on $ \ge \frac{n}{3} $ vertices as a minor. This argument is where the name of this conjecture arises. Let us call a seagull of $ G $ an induced subgraph which is a 2-edge path (such a subgraph may be drawn suggestively as a seagull). Then, for every seagull $ S $ and every vertex $ v $ not in $ S $ , there must be an edge between $ v $ and one of the two endpoints of $ S $ (this follows from the assumption that $ G $ has no independent set of size 3). This feature makes seagulls especially useful for constructing complete graphs as minors - as we now demonstrate. Choose a maximal collection $ {\mathcal S} $ of pairwise disjoint seagulls of $ G $ . The graph $ G' $ obtained from $ G $ by deleting every vertex which appears in a seagull in $ {\mathcal S} $ cannot have any two vertices at distance 2 from one another (since this would yield a seagull), so $ G' $ must be a disjoint union of complete graphs. Since $ G' $ has no independent set of size 3, it is in fact a disjoint union of at most two complete graphs. By deleting every vertex in the smaller complete subgraph of $ G' $ from $ G $ and then contracting both edges in every seagull in $ {\mathcal S} $ , we obtain a complete graph minor of $ G $ with size $ \ge \frac{n}{3} $ . Kawarabayashi, Plummer, and Toft have improved this bound slightly by showing that $ G $ must have a complete graph minor of size $ \ge \frac{n + \omega(G)}{3} $ , but it looks very difficult to get much more out of this type of argument.

=== References listed by OpenProblemGarden ===
- [KPT] K. Kawarabayashi, M. Plummer, and B. Toft, Improvements of the theorem of Duchet and Meynial's theorem on Hadwiger's Conjecture, J. Combin. Theory Ser. B. 95 (2005) 152-167.

=== Catalog page (statement + literature review) ===
Seagull problem — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The seagull conjecture — every $n$-vertex graph with $\alpha(G) \le 2$ contains $K_{\lceil n/2 \rceil}$ as a minor — remains open. Norin and Seymour (2022) proved that every such graph contains an $\lceil n/2 \rceil$-vertex simple minor with approximately $0.98688\binom{\lceil n/2 \rceil}{2} - o(n^2)$ edges, establishing a nearly-complete minor on the right number of vertices but falling short of a complete minor. Chudnovsky and Seymour (2012) gave a complete characterization of when such graphs contain $k$ vertex-disjoint seagulls, a foundational packing result closely related to the minor problem.

 Cited literature (2)

 
 
 
partial Packing seagulls
 (2012)
 

 
 Maria Chudnovsky, Paul Seymour · Combinatorica · doi:10.1007/s00493-012-2594-2

Characterizes exactly when an $n$-vertex graph with no independent set of size 3 contains $k$ vertex-disjoint seagulls (induced 3-vertex paths), providing a polynomial-time algorithm and advancing structural understanding central to the seagull conjecture.
 

 
 
partial Dense minors of graphs with independence number two
 (2022)
 

 
 Sergey Norin, Paul Seymour · arXiv preprint · arXiv:2206.00186

Proves that every $n$-vertex graph with $\alpha(G) \le 2$ contains an $\lceil n/2 \rceil$-vertex simple minor with $\approx 0.98688\binom{\lceil n/2 \rceil}{2} - o(n^2)$ edges, establishing a dense (but not complete) minor on exactly the number of vertices required by the seagull conjecture.
 

 

 Reviewer notes. The Norin-Seymour result (arXiv 2206.00186) appears to have been published in J. Combin. Theory Ser. B in 2025 (ScienceDirect pii S0095895625000619) but that page returned HTTP 403; only the arXiv version is cited. The Chudnovsky-Seymour Combinatorica paper is verified via Princeton's repository; the Springer page redirected to authentication. The seagull conjecture is explicitly described as open in the Norin-Seymour preprint. The Blasiak (pre-2009) work on clique minors in graphs with alpha=2 mentioned at a 2009 Princeton talk is a precursor but predates or coincides with the posting date and was not separately verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. Every $ n $ vertex graph with no independent set of size $ 3 $ has a complete graph on $ \ge \frac{n}{2} $ vertices as a minor.

Keywords:
coloring · complete graph · minor

Discussion

This conjecture is significant because it is an interesting unproved consequence of Hadwiger's conjecture (this implication is proved next). In fact, some experts have suggested that this problem might hold the key to finding a counterexample to Hadwiger. I (M. DeVos) have attributed this conjecture to Seymour, but I believe that it may have been independently suggested by Mader and by others. Its curious title will be explained later in this discussion. Hadwiger's conjecture (every loopless graph with chromatic number $ \ge n $ has $ K_n $ as a minor) is one of the outstanding problems in graph theory. This conjecture has been resolved for small values of $ n $ ; when $ n \le 4 $ it is relatively easy, for $ n=5,6 $ it has been proven to be equivalent to the Four color theorem. The Seagull problem concerns the other extreme - when the size of the chromatic number is close to the order of the graph. If $ G $ is an $ n $ vertex graph with no independent set of size 3, then $ \chi(G) \ge \frac{n}{2} $ since each color class has size $ \le 2 $ . If Hadwiger's conjecture holds for $ G $ , it must then have a minor which is a complete graph on $ \ge \frac{n}{2} $ vertices. This is precisely the statement of the Seagull problem. The (essentially) best known bound for the conjecture is that every $ n $ vertex graph $ G $ with no independent set of size 3 has a complete graph on $ \ge \frac{n}{3} $ vertices as a minor. This argument is where the name of this conjecture arises. Let us call a seagull of $ G $ an induced subgraph which is a 2-edge path (such a subgraph may be drawn suggestively as a seagull). Then, for every seagull $ S $ and every vertex $ v $ not in $ S $ , there must be an edge between $ v $ and one of the two endpoints of $ S $ (this follows from the assumption that $ G $ has no independent set of size 3). This feature makes seagulls especially useful for constructing complete graphs as minors - as we now demonstrate. Choose a maximal collection $ {\mathcal S} $ of pairwise disjoint seagulls of $ G $ . The graph $ G' $ obtained from $ G $ by deleting every vertex which appears in a seagull in $ {\mathcal S} $ cannot have any two vertices at distance 2 from one another (since this would yield a seagull), so $ G' $ must be a disjoint union of complete graphs. Since $ G' $ has no independent set of size 3, it is in fact a disjoint union of at most two complete graphs. By deleting every vertex in the smaller complete subgraph of $ G' $ from $ G $ and then contracting both edges in every seagull in $ {\mathcal S} $ , we obtain a complete graph minor of $ G $ with size $ \ge \frac{n}{3} $ . Kawarabayashi, Plummer, and Toft have improved this bound slightly by showing that $ G $ must have a complete graph minor of size $ \ge \frac{n + \omega(G)}{3} $ , but it looks very difficult to get much more out of this type of argument.

Bibliography

 [KPT]
 K. Kawarabayashi, M. Plummer, and B. Toft, Improvements of the theorem of Duchet and Meynial's theorem on Hadwiger's Conjecture, J. Combin. Theory Ser. B. 95 (2005) 152-167.

Related conjectures

 
 implied by
 Fractional Hadwiger
 open
 Part (a) of Fractional Hadwiger states chi_f(G) <= had(G). By LP duality (fractional covering by independent sets), chi_f(G) >= n/alpha(G) for every n-vertex G. If G has no independent set of size 3 then alpha(G) <= 2, so chi_f(G) >= n/2, whence had(G) >= n/2; since had(G) is an integer, G has a K_{ceil(n/2)} minor, i.e. a complete minor on >= n/2 vertices — exactly the Seagull problem. The source conjecture is the conjunction of (a),(b),(c), and (a) alone suffices, so the conjecture implies Seagull. (Part (b) alone would not obviously suffice, since had_f >= had; but the edge is from the full conjecture.) Direction correct: Fractional Hadwiger is the stronger statement.
 

 
 implied by
 Independence number lower bound in K_{t+1}-minor-free graphs
 open
 Let G be an n-vertex graph with alpha(G) <= 2 and let h = had(G) be the largest k with a K_k minor. Then G has no K_{h+1} minor, so the source conjecture with t = h gives alpha(G) >= n/h, hence 2 >= n/h and h >= n/2; as h is an integer, G has a K_{ceil(n/2)} minor, which is exactly the Seagull statement. Equivalently, Seagull is the alpha = 2 special case of the conjecture that K_{t+1}-minor-free graphs satisfy alpha >= n/t (both are standard weakenings of Hadwiger's conjecture via chi >= n/alpha resp. chi >= n/2). Parameters are monotone and the specialization is exact; direction as claimed, and all three finder sketches agree with this derivation.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
