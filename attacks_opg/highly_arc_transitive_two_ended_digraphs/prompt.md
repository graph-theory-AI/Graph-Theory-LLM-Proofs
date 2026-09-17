Attack the following open graph-theory problem.

Catalog id: highly_arc_transitive_two_ended_digraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/highly_arc_transitive_two_ended_digraphs/
Original entry: http://www.openproblemgarden.org/op/highly_arc_transitive_two_ended_digraphs
Problem attributed to: Cameron, Peter J., Praeger, Cheryl E., Wormald, Nicholas C. (posted 2007-10-29)

=== Problem statement (OpenProblemGarden) ===
Title: Highly arc transitive two ended digraphs
Conjecture If $ G $ is a highly arc transitive digraph with two ends, then every tile of $ G $ is a disjoint union of complete bipartite graphs.

=== Discussion / context (OpenProblemGarden) ===
It follows from a theorem of Dunwoody [D] that every vertex transitive graph $ G $ with two ends has a system of imprimitivity $ \{ X_i : i \in {\mathbb Z} \} $ with finite blocks so that the cyclic order $ \ldots X_{-2}, X_{-1},X_0,X_1,X_2,\ldots $ is preserved by the automorphism group (of $ G $ ). If $ G $ is edge-transitive, then every edge of $ G $ must have its ends in two consecutive blocks, so in this case $ G $ is an edge-disjoint union of the (isomorphic) bipartite graphs $ G[X_i,X_{i+1}] $ for $ i \in {\mathbb Z} $ - which we shall call tiles . Note that the tiles are edge-transitive. This gives us a good description of edge-transitive graphs with two ends; each is made up by gluing together copies of a tile in a linear order. If $ G $ is a 2-arc transitive digraph with two ends, then all edges in each tile must be oriented consistently, so by possibly reordering, we may assume that every edge in $ G[X_i,X_{i+1}] $ is oriented from $ X_i $ to $ X_{i+1} $ . The above conjecture asserts that under the added symmetry condition of high arc transitivity, each tile has a simple structure - namely it is a union of (consistently oriented) complete bipartite graphs. It is easy to construct a highly arc transitive two ended graph by simply using the complete bipartite graph $ K_{n,n} $ (with all edges oriented consistently) as a tile. Mckay and Praeger found the following pretty construction of a highly arc transitive digraph with tiles isomorphic to a disjoint union of complete bipartite graphs: Let $ S $ be a finite set, let $ n $ be a positive integer, and define $ G $ to be the digraph with vertex set $ {\mathbb Z} \times S^n $ and an edge from $ (i, \mathbf{x}, y) $ to $ (i+1, z, \mathbf{x}) $ if $ i \in {\mathbb Z} $ , $ \mathbf{x} \in S^{n-1} $ , and $ y,z \in S $ . A generalized (twisted) version of this construction was introduced by Cameron, Praeger, and Wormald [CPW], but again, every tile in this construction is a disjoint unions of bipartite graphs, and it looks hard to do anything else.

=== References listed by OpenProblemGarden ===
- *[CPW] P. J. Cameron, C. E. Praeger, and N. C. Wormald, Infinite highly arc transitive digraphs and universal covering digraphs. Combinatorica 13 (1993), no. 4, 377--396. MathSciNet.
- [D] M. J. Dunwoody, Cutting up graphs. Combinatorica 2 (1982), no. 1, 15--23. MathSciNet

=== Catalog page (statement + literature review) ===
Highly arc transitive two ended digraphs — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 The Cameron–Praeger–Wormald conjecture was disproved by DeVos, Mohar, and Šámal, who constructed locally finite two-ended highly arc-transitive digraphs whose tiles are finite bipartite graphs that are *not* disjoint unions of complete bipartite graphs — exactly what the conjecture asserted to be impossible. Further structural results, including a complete classification of two-ended highly arc-transitive digraphs with prime in- and out-valencies, were subsequently obtained by Möller, Potočnik, and Seifter.

 Cited literature (2)

 
 
 
counterexample Highly arc-transitive digraphs -- counterexamples and structure
 (2014)
 

 
 Matt DeVos, Bojan Mohar, Robert Šámal · Combinatorica · arXiv:1110.2945 · doi:10.1007/s00493-014-3040-4

Constructs 2-ended locally finite highly arc-transitive digraphs whose tiles are finite bipartite graphs that are not disjoint unions of complete bipartite graphs, thereby disproving the Cameron–Praeger–Wormald conjecture.
 

 
 
partial Infinite arc-transitive and highly-arc-transitive digraphs
 (2018)
 

 
 Rögnvaldur G. Möller, Primož Potočnik, Norbert Seifter · European Journal of Combinatorics · arXiv:1811.02995

Gives a detailed structural description of two-ended arc-transitive digraphs and achieves a complete classification of two-ended highly arc-transitive digraphs with prime in- and out-valencies.
 

 

 Reviewer notes. The Springer Combinatorica page (DOI 10.1007/s00493-014-3040-4) redirected to an authentication wall and could not be fetched; the DOI is inferred from the search result metadata and arXiv record which lists the journal publication. The ScienceDirect page for the Möller–Potočnik–Seifter paper returned 403; the venue (European Journal of Combinatorics, ISSN 0195-6698) and DOI are inferred from the URL PII. A December 2025 arXiv preprint (2512.17244) on quasiprimitive highly-arc-transitive digraphs was found but not fetched — it post-dates the disproof and appears to be follow-up structural work.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. If $ G $ is a highly arc transitive digraph with two ends, then every tile of $ G $ is a disjoint union of complete bipartite graphs.

Keywords:
arc transitive · digraph · infinite graph

Discussion

It follows from a theorem of Dunwoody [D] that every vertex transitive graph $ G $ with two ends has a system of imprimitivity $ \{ X_i : i \in {\mathbb Z} \} $ with finite blocks so that the cyclic order $ \ldots X_{-2}, X_{-1},X_0,X_1,X_2,\ldots $ is preserved by the automorphism group (of $ G $ ). If $ G $ is edge-transitive, then every edge of $ G $ must have its ends in two consecutive blocks, so in this case $ G $ is an edge-disjoint union of the (isomorphic) bipartite graphs $ G[X_i,X_{i+1}] $ for $ i \in {\mathbb Z} $ - which we shall call tiles . Note that the tiles are edge-transitive. This gives us a good description of edge-transitive graphs with two ends; each is made up by gluing together copies of a tile in a linear order. If $ G $ is a 2-arc transitive digraph with two ends, then all edges in each tile must be oriented consistently, so by possibly reordering, we may assume that every edge in $ G[X_i,X_{i+1}] $ is oriented from $ X_i $ to $ X_{i+1} $ . The above conjecture asserts that under the added symmetry condition of high arc transitivity, each tile has a simple structure - namely it is a union of (consistently oriented) complete bipartite graphs. It is easy to construct a highly arc transitive two ended graph by simply using the complete bipartite graph $ K_{n,n} $ (with all edges oriented consistently) as a tile. Mckay and Praeger found the following pretty construction of a highly arc transitive digraph with tiles isomorphic to a disjoint union of complete bipartite graphs: Let $ S $ be a finite set, let $ n $ be a positive integer, and define $ G $ to be the digraph with vertex set $ {\mathbb Z} \times S^n $ and an edge from $ (i, \mathbf{x}, y) $ to $ (i+1, z, \mathbf{x}) $ if $ i \in {\mathbb Z} $ , $ \mathbf{x} \in S^{n-1} $ , and $ y,z \in S $ . A generalized (twisted) version of this construction was introduced by Cameron, Praeger, and Wormald [CPW], but again, every tile in this construction is a disjoint unions of bipartite graphs, and it looks hard to do anything else.

Bibliography

★ [CPW]
 P. J. Cameron, C. E. Praeger, and N. C. Wormald, Infinite highly arc transitive digraphs and universal covering digraphs. Combinatorica 13 (1993), no. 4, 377--396. MathSciNet .
 MathSciNet

 [D]
 M. J. Dunwoody, Cutting up graphs. Combinatorica 2 (1982), no. 1, 15--23. MathSciNet
 MathSciNet
