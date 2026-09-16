Attack the following open graph-theory problem.

Catalog id: the_circular_embedding_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_circular_embedding_conjecture/
Original entry: http://www.openproblemgarden.org/op/the_circular_embedding_conjecture
Problem attributed to: Haggard, Gary (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: The circular embedding conjecture
Conjecture Every 2- connected graph may be embedded in a surface so that the boundary of each face is a cycle.

=== Discussion / context (OpenProblemGarden) ===
This conjecture implies the cycle double cover conjecture , since the list of cycles which bound faces covers each edge exactly twice. Let $ G $ be a cubic graph, let $ L $ be a list of cycles covering every edge of $ G $ exactly two times, and form a topological space by gluing a disc to each circuit in $ L $ . This space is a surface, and every face is bounded by a cycle. Thus, the circular embedding conjecture and the cycle double cover conjecture are equivalent for cubic graphs. For general graphs, this construction may fail since the neighborhood of a vertex may not be a disc (it could be a pinchpoint). A stronger variant of this conjecture asserts that it is possible to find an embedding as above with the added condition that the dual graph is 5-colorable. This variant implies The five cycle double cover conjecture since the circuits bounding faces of a given color class may be grouped into a cycle. Next we state a different strengthening which asserts that we may find an embedding as above into an orientable surface. Conjecture (The oriented circular embedding conjecture) Every 2-connected graph may be embedded in an orientable surface so that the boundary of each face is a circuit. If this conjecture is true, then the oriented cycle double cover conjecture (see cycle double cover ) is also true, since the list of circuits bounding faces all traversed in the clockwise direction cover each edge exactly once in each direction (since the surface is orientable, we may specify a global clockwise orientation). As was the case above, the oriented circular embedding conjecture is equivalent to the oriented cycle double cover conjecture for cubic graphs. Also as above, there is a strengthening of this conjecture which asserts that the graph may be embedded so that the dual graph is 5-colorable. If true, this would imply The orientable five cycle double cover conjecture.

=== References listed by OpenProblemGarden ===
- [H] G. Haggard, Edmonds characterization of disc embeddings. Proceedings of the Eighth Southeastern Conference on Combinatorics, Graph Theory and Computing (Louisiana State Univ., Baton Rouge, La., 1977), pp. 291--302. MathSciNet

=== Catalog page (statement + literature review) ===
The circular embedding conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The circular embedding conjecture (equivalently, the strong embedding conjecture) remains open for general 2-connected graphs. Ellingham and Zha (2011) proved the oriented variant for 2-connected projective-planar cubic graphs, showing every such graph has a closed 2-cell embedding in some orientable surface. The conjecture is equivalent to the cycle double cover conjecture for cubic graphs, and both remain major open problems in topological graph theory.

 Cited literature (2)

 
 
 
partial Orientable embeddings and orientable cycle double covers of projective-planar graphs
 (2009)
 

 
 M. N. Ellingham, Xiaoya Zha · arXiv preprint (journal: European Journal of Combinatorics, 2011) · arXiv:0911.2713

Proves that every 2-connected projective-planar cubic graph has a closed 2-cell (circular) embedding in some orientable surface, and that every 2-edge-connected projective-planar graph has an orientable cycle double cover, establishing the oriented circular embedding conjecture for this graph class.
 

 
 
partial Facial diagrams and cycle double cover
 (2026)
 

 
 Babak Ghanbari, Robert Šámal · arXiv preprint · arXiv:2605.01410

Introduces a facial-diagram framework for circular 2-cell embeddings of cubic graphs, studies an edge-twisting operation that transforms one 2-cell embedding into another, and derives bounds on the number of singular edges, providing new tools for attacking the circular embedding / cycle double cover conjecture.
 

 

 Reviewer notes. Mohar (2009/2010, arXiv:0908.1933) showed that closed 2-cell embeddings may require surfaces of genus proportional to the order of the graph for some cubic graphs, disproving a minimum-genus folklore conjecture attributed to Tutte, but this does not disprove the circular embedding conjecture (which asks for existence on any surface). Ellingham and Zha (2015, arXiv:1501.06043) developed a partial-duality characterisation of closed 2-cell embeddings. A claim circulating in survey literature that 'any 2-connected graph without the Möbius 4-ladder as a minor has a closed 2-cell embedding' could not be traced to a verifiable source within the search budget. The ScienceDirect page for the Ellingham-Zha journal paper returned HTTP 403; the arXiv preprint was verified instead.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. Every 2- connected graph may be embedded in a surface so that the boundary of each face is a cycle.

Keywords:
cover · cycle

Discussion

This conjecture implies the cycle double cover conjecture , since the list of cycles which bound faces covers each edge exactly twice. Let $ G $ be a cubic graph, let $ L $ be a list of cycles covering every edge of $ G $ exactly two times, and form a topological space by gluing a disc to each circuit in $ L $ . This space is a surface, and every face is bounded by a cycle. Thus, the circular embedding conjecture and the cycle double cover conjecture are equivalent for cubic graphs. For general graphs, this construction may fail since the neighborhood of a vertex may not be a disc (it could be a pinchpoint). A stronger variant of this conjecture asserts that it is possible to find an embedding as above with the added condition that the dual graph is 5-colorable. This variant implies The five cycle double cover conjecture since the circuits bounding faces of a given color class may be grouped into a cycle. Next we state a different strengthening which asserts that we may find an embedding as above into an orientable surface. Conjecture (The oriented circular embedding conjecture) Every 2-connected graph may be embedded in an orientable surface so that the boundary of each face is a circuit. If this conjecture is true, then the oriented cycle double cover conjecture (see cycle double cover ) is also true, since the list of circuits bounding faces all traversed in the clockwise direction cover each edge exactly once in each direction (since the surface is orientable, we may specify a global clockwise orientation). As was the case above, the oriented circular embedding conjecture is equivalent to the oriented cycle double cover conjecture for cubic graphs. Also as above, there is a strengthening of this conjecture which asserts that the graph may be embedded so that the dual graph is 5-colorable. If true, this would imply The orientable five cycle double cover conjecture.

Bibliography

 [H]
 G. Haggard, Edmonds characterization of disc embeddings. Proceedings of the Eighth Southeastern Conference on Combinatorics, Graph Theory and Computing (Louisiana State Univ., Baton Rouge, La., 1977), pp. 291--302. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 Cycle double cover conjecture
 partial
 The source's OPG context states the implication verbatim: 'This conjecture implies the cycle double cover conjecture, since the list of cycles which bound faces covers each edge exactly twice.' The hypothesis-class gap (2-connected vs bridgeless) is closed by block decomposition: every block of a bridgeless graph is 2-connected (no block is a cut-edge), and the union of the face-boundary CDCs of the blocks is a CDC of the whole graph. Direction as claimed; note the converse is known only for cubic graphs (glue discs to the cycles of a CDC), so the relation is a strict strengthening in general, not an equivalence.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
