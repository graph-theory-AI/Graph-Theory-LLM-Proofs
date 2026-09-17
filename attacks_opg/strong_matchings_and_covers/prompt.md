Attack the following open graph-theory problem.

Catalog id: strong_matchings_and_covers
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/strong_matchings_and_covers/
Original entry: http://www.openproblemgarden.org/op/strong_matchings_and_covers
Problem attributed to: Aharoni, Ron (posted 2007-10-23)

=== Problem statement (OpenProblemGarden) ===
Title: Strong matchings and covers
Let $ H $ be a hypergraph . A strongly maximal matching is a matching $ F \subseteq E(H) $ so that $ |F' \setminus F| \le |F \setminus F'| $ for every matching $ F' $ . A strongly minimal cover is a (vertex) cover $ X \subseteq V(H) $ so that $ |X' \setminus X| \ge |X \setminus X'| $ for every cover $ X' $ . Conjecture If $ H $ is a (possibly infinite) hypergraph in which all edges have size $ \le k $ for some integer $ k $ , then $ H $ has a strongly maximal matching and a strongly minimal cover.

=== Discussion / context (OpenProblemGarden) ===
The theory of matching in finite graphs is quite well understood. Now, thanks to the work of Aharoni and others, much of this theory has been extended to infinite graphs. On the other hand, matching in hypergraphs - both finite and infinite - is a subject where our knowledge apears to be lacking. The above conjecture asserts a rather basic property of hypergraphs which would be nice to verify. This conjecture is (of course) trivial for finite hypergraphs, but it looks very difficult for infinite ones. It has been proved by Aharoni [A2] for the case when $ k=2 $ , that is, for infinite graphs. Here the key tool is an infinite version of the Tutte-Edmonds-Gallai decomposition theorem [A1]. Next we offer another interesting conjecture of Aharoni on minimal covers. Conjecture If $ G $ is a (possibly infinite) graph and $ H $ is the hypergraph of independent sets in $ G $ , then $ H $ has a strongly minimal cover.

=== References listed by OpenProblemGarden ===
- [A1] R. Aharoni, Matchings in infinite graphs. J. Combin. Theory Ser. B 44 (1988), no. 1, 87--125. MathSciNet.
- *[A2] R. Aharoni, Infinite matching theory. Directions in infinite graph theory and combinatorics (Cambridge, 1989). Discrete Math. 95 (1991), no. 1-3, 5--22. MathSciNet.

=== Catalog page (statement + literature review) ===
Strong matchings and covers — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 The conjecture that every (possibly infinite) hypergraph with edges of size $\leq k$ has a strongly maximal matching and a strongly minimal cover has been disproved. Hollom and Shaw (2025 preprint; published 2026) explicitly construct a 3-uniform hypergraph with no strongly maximal matching (Theorem 1.2) and a 3-uniform hypergraph with no strongly minimal edge-cover (Theorem 1.3), settling both parts of the conjecture in the negative for $k \geq 3$. The case $k=2$ (infinite graphs), proved by Aharoni prior to the posting, remains the only known affirmative case.

 Cited literature (2)

 
 
 
survey Strongly maximal matchings and strongly minimal covers
 (2022)
 

 
 Ron Aharoni · arXiv preprint · arXiv:2206.02576

Reference/survey paper that carefully states the main conjecture (existence of strongly maximal matchings and strongly minimal covers in hypergraphs with edges of bounded size) and summarises what is known; confirms the conjecture is proved only for $k=2$ and remains open for larger $k$.
 

 
 
counterexample Counterexamples to conjectures on strong maximality and minimality
 (2026)
 

 
 Lawrence Hollom, Benedict Randall Shaw · Electronic Journal of Combinatorics · arXiv:2511.13709 · doi:10.37236/14243

Constructs a 3-uniform hypergraph with no strongly maximal matching and a 3-uniform hypergraph with no strongly minimal edge-cover, directly disproving both parts of Aharoni's conjecture for $k=3$ (and hence all $k\geq 3$); also disproves the related conjecture on strongly minimal graph colourings. The paper first appeared as arXiv:2511.13709 in 2025.
 

 

 Reviewer notes. The Hollom-Shaw counterexamples use 3-uniform hypergraphs, which have all edges of size exactly 3 (hence size ≤ 3), directly refuting the conjecture as stated on OPG. The case k=2 (proved by Aharoni using the infinite Tutte-Edmonds-Gallai decomposition) is unaffected and remains valid. The 2022 Aharoni preprint is explicitly not intended for journal publication. Hollom and Shaw's counterexample paper is now published in Electronic Journal of Combinatorics 33(2), P2.11 (2026), DOI 10.37236/14243.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. If $ H $ is a (possibly infinite) hypergraph in which all edges have size $ \le k $ for some integer $ k $ , then $ H $ has a strongly maximal matching and a strongly minimal cover.

Keywords:
cover · infinite graph · matching

Discussion

The theory of matching in finite graphs is quite well understood. Now, thanks to the work of Aharoni and others, much of this theory has been extended to infinite graphs. On the other hand, matching in hypergraphs - both finite and infinite - is a subject where our knowledge apears to be lacking. The above conjecture asserts a rather basic property of hypergraphs which would be nice to verify. This conjecture is (of course) trivial for finite hypergraphs, but it looks very difficult for infinite ones. It has been proved by Aharoni [A2] for the case when $ k=2 $ , that is, for infinite graphs. Here the key tool is an infinite version of the Tutte-Edmonds-Gallai decomposition theorem [A1]. Next we offer another interesting conjecture of Aharoni on minimal covers. Conjecture If $ G $ is a (possibly infinite) graph and $ H $ is the hypergraph of independent sets in $ G $ , then $ H $ has a strongly minimal cover.

Bibliography

 [A1]
 R. Aharoni, Matchings in infinite graphs. J. Combin. Theory Ser. B 44 (1988), no. 1, 87--125. MathSciNet .
 MathSciNet

★ [A2]
 R. Aharoni, Infinite matching theory. Directions in infinite graph theory and combinatorics (Cambridge, 1989). Discrete Math. 95 (1991), no. 1-3, 5--22. MathSciNet .
 MathSciNet
