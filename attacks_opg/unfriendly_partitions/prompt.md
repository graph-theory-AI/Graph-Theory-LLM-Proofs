Attack the following open graph-theory problem.

Catalog id: unfriendly_partitions
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/unfriendly_partitions/
Original entry: http://www.openproblemgarden.org/op/unfriendly_partitions
Problem attributed to: Cowan, Robert H., Emerson, William R. (posted 2007-10-22)

=== Problem statement (OpenProblemGarden) ===
Title: Unfriendly partitions
If $ G $ is a graph, we say that a partition of $ V(G) $ is unfriendly if every vertex has at least as many neighbors in the other classes as in its own. Problem Does every countably infinite graph have an unfriendly partition into two sets?

=== Discussion / context (OpenProblemGarden) ===
It is a simple property that every finite graph $ G $ has an unfriendly partition into two sets - just choose a partition of $ V(G) $ into two sets so that the number of edges with one end in each is maximum. Cowan and Emerson [CE] conjectured that the same property should hold true of infinite graphs. A counterexample to this was constructed by Milner and Shelah [MS], but their construction uses uncountably many vertices, leaving the countable case (highlighted above) still open. In the same article by Milner and Shelah [MS], they show that every graph does have an unfriendly partition into three sets. Curiously, it is quite easy to see that the answer to the above question is yes in the case when all vertices have finite degree, and also in the case when all vertices have infinite degree. The former follows from the unfriendly partition property for finite graphs together with a standard compactness argument. The latter can be achieved with a "back and forth" construction. Thus, the difficult case is the mixed one. Aharoni, Milner, and Prikry [AMP] showed that every graph with only finitely many vertices of infinite degree has an unfriendly partition into two sets, but this seems the extent of our knowledge. It does not appear that there is any consensus among experts as to whether this conjecture should be true or false.

=== References listed by OpenProblemGarden ===
- *[CE] R. Cowan and W. Emerson, Proportional colorings of graphs, unpublished.
- [MS] E. C. Milner and S. Shelah, Graphs with no unfriendly partitions. A tribute to Paul Erdös, 373--384, Cambridge Univ. Press, Cambridge, 1990. MathSciNet.
- [AMP] R. Aharoni, E. C. Milner, K. Prikry, Unfriendly partitions of a graph. J. Combin. Theory Ser. B 50 (1990), no. 1, 1--10. MathSciNet

=== Catalog page (statement + literature review) ===
Unfriendly partitions — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The problem of whether every countably infinite graph has an unfriendly partition into two sets remains open. Significant partial results have appeared since 2007: the conjecture has been confirmed for rayless graphs, for graphs not containing a subdivision of an infinite clique, for line graphs of any cardinality, and most recently (2024) for all countable graphs without alternating rays — rays that pass through infinitely many vertices of both finite and infinite degree. The difficult case of countable graphs that do admit alternating rays is still unresolved.

 Cited literature (4)

 
 
 
partial Unfriendly or weakly unfriendly partitions of graphs
 (2014)
 

 
 Francis Oger · arXiv preprint · arXiv:1402.0067

Proves an equivalence: the existence of unfriendly partitions for all countable graphs is equivalent to their existence for all countable graphs lacking induced subgraphs of infinite minimum degree, and establishes omega_n-unfriendly partitions for graphs with infinite minimum degree.
 

 
 
partial List majority edge-colorings of graphs
 (2023)
 

 
 Rafał Kalinowski, Monika Pilśniak, Marcin Stawiski · arXiv preprint · arXiv:2312.00922 · doi:10.1007/s00493-024-00131-1

Proves the Unfriendly Partition Conjecture for line graphs of any cardinality by showing they admit majority vertex-colorings from lists of size 2.
 

 
 
partial Unfriendly partitions when avoiding vertices of finite degree
 (2023)
 

 
 Leandro Fiorini Aurichi, Lucas Real · arXiv preprint · arXiv:2304.02580

Shows that the minimum cardinality of a graph (without vertices of finite degree) that admits no unfriendly partition cannot be determined in ZFC, establishing a set-theoretic independence result.
 

 
 
partial Remarks on the countable case of the Unfriendly Partition Problem
 (2024)
 

 
 Leandro Aurichi, Lucas Real · arXiv preprint · arXiv:2412.14151

Proves that every countable graph without alternating rays admits an unfriendly partition, strictly generalizing results of Aharoni-Milner-Prikry and Bruhn-Diestel-Georgakopoulos-Sprüssel.
 

 

 Reviewer notes. The Bruhn-Diestel-Georgakopoulos-Sprüssel (2010) paper on rayless graphs and the Berger (2017) paper on graphs without a subdivision of an infinite clique are both cited in verified sources as important post-2007 partial results, but their direct URLs could not be individually fetched and confirmed in this review, so they are not listed in since_posted. The published journal version of the line graphs paper (Combinatorica 45, 2025, DOI 10.1007/s00493-024-00131-1) was inaccessible via Springer; the arXiv preprint (2312.00922) was verified instead. The December 2024 paper (2412.14151) explicitly states the problem remains open for countable graphs that do admit alternating rays.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Problem. Does every countably infinite graph have an unfriendly partition into two sets?

Keywords:
coloring · infinite graph · partition

Discussion

It is a simple property that every finite graph $ G $ has an unfriendly partition into two sets - just choose a partition of $ V(G) $ into two sets so that the number of edges with one end in each is maximum. Cowan and Emerson [CE] conjectured that the same property should hold true of infinite graphs. A counterexample to this was constructed by Milner and Shelah [MS], but their construction uses uncountably many vertices, leaving the countable case (highlighted above) still open. In the same article by Milner and Shelah [MS], they show that every graph does have an unfriendly partition into three sets. Curiously, it is quite easy to see that the answer to the above question is yes in the case when all vertices have finite degree, and also in the case when all vertices have infinite degree. The former follows from the unfriendly partition property for finite graphs together with a standard compactness argument. The latter can be achieved with a "back and forth" construction. Thus, the difficult case is the mixed one. Aharoni, Milner, and Prikry [AMP] showed that every graph with only finitely many vertices of infinite degree has an unfriendly partition into two sets, but this seems the extent of our knowledge. It does not appear that there is any consensus among experts as to whether this conjecture should be true or false.

Bibliography

★ [CE]
 R. Cowan and W. Emerson, Proportional colorings of graphs, unpublished.

 [MS]
 E. C. Milner and S. Shelah, Graphs with no unfriendly partitions. A tribute to Paul Erdös, 373--384, Cambridge Univ. Press, Cambridge, 1990. MathSciNet .
 MathSciNet

 [AMP]
 R. Aharoni, E. C. Milner, K. Prikry, Unfriendly partitions of a graph. J. Combin. Theory Ser. B 50 (1990), no. 1, 1--10. MathSciNet
 MathSciNet

Related conjectures

 
 related to
 Friendly partitions
 partial
 Dual notions in disjoint settings with no logical link. Friendly partitions (DeVos) asks whether all but finitely many finite r-regular graphs admit a partition where every vertex has at least as many neighbours in its own class; the unfriendly-partition problem (Cowan-Emerson) asks whether every countably infinite graph has a partition where every vertex has at least as many neighbours in the other class. The source page mentions unfriendly partitions only as contrast/motivation ('every finite graph has an unfriendly partition ... finding friendly partitions appears to be considerably more difficult'). One statement is about finite regular graphs with the 'friendly' inequality, the other about countably infinite graphs with the opposite inequality; truth of either has no bearing on the other. Thematically linked, no implication: related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
