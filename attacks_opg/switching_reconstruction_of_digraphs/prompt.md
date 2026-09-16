Attack the following open graph-theory problem.

Catalog id: switching_reconstruction_of_digraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/switching_reconstruction_of_digraphs/
Original entry: http://www.openproblemgarden.org/op/switching_reconstruction_of_digraphs
Problem attributed to: Bondy, J. Adrian, Mercier, Fabien (posted 2013-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Switching reconstruction of digraphs
Question Are there any switching-nonreconstructible digraphs on twelve or more vertices?

=== Discussion / context (OpenProblemGarden) ===
To switch a vertex of a digraph is to reverse all the arcs incident to it. The digraph so obtained is called a switching of the digraph. The collection of switchings of a digraph $ D $ is called the switching deck of $ D $ . A digraph is switching-reconstructible if every digraph with the same deck as $ D $ is isomorphic to $ D $ . The problem is a directed analogue of switching reconstruction of graphs in which one complements the edges at a vertex, instead of reversing each of its incident arcs. Bondy and Mercier proved an analogue to Stanley's result for switching reconstruction of graphs. They proved that a digraph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . They also proved many other common results for both switching reconstructions. One significant difference between the directed and undirected problems is that there exist switching-nonreconstructible directed graphs on eight vertices, while Stanley's conjecture that every simple graph on five or more vertices is switching-reconstructible.

=== References listed by OpenProblemGarden ===
- *[BM] J. A. Bondy and F. Mercier. Switching reconstruction of digraphs. J. Graph Theory 67(2011), no. 4, 332-348.

=== Catalog page (statement + literature review) ===
Switching reconstruction of digraphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 McKay and Schweitzer (2014) made meaningful progress by showing that there are exactly 44 switching-nonreconstructible oriented graphs whose underlying undirected graphs have maximum degree at most 2, and by determining the complete family of switching-stable oriented graphs; the largest known nonreconstructible examples still have only 8 vertices. The original question — whether switching-nonreconstructible digraphs on 12 or more vertices exist — remains open.

 Cited literature (1)

 
 
 
partial Switching Reconstruction of Digraphs
 (2014)
 

 
 Brendan D. McKay, Pascal Schweitzer · Journal of Graph Theory · arXiv:1308.0675

Proved that there are exactly 44 switching-nonreconstructible oriented graphs whose underlying graphs have maximum degree at most 2, and determined all switching-stable oriented graphs, without resolving existence of nonreconstructible digraphs on 12 or more vertices.
 

 

 Reviewer notes. The McKay–Schweitzer paper was submitted to arXiv on 2013-08-03 (after the OPG posting date 2013-03-07) and published in J. Graph Theory 76 (2014) 279–296. I could not determine from the abstract alone whether any of their 44 nonreconstructible examples lie on 12+ vertices, but search summaries consistently state that 'the largest known nonreconstructible oriented graphs have 8 vertices'. A related paper 'The r-switching-stable graphs' appeared on ScienceDirect (pii S0166218X18306565, likely 2018–2019) but returned HTTP 403, so it was not verified and is not cited. The Bondy–Mercier result that digraphs with n ≢ 0 (mod 4) are switching-reconstructible means n = 12 (≡ 0 mod 4) is the smallest open case.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Question. Are there any switching-nonreconstructible digraphs on twelve or more vertices?

Discussion

To switch a vertex of a digraph is to reverse all the arcs incident to it. The digraph so obtained is called a switching of the digraph. The collection of switchings of a digraph $ D $ is called the switching deck of $ D $ . A digraph is switching-reconstructible if every digraph with the same deck as $ D $ is isomorphic to $ D $ . The problem is a directed analogue of switching reconstruction of graphs in which one complements the edges at a vertex, instead of reversing each of its incident arcs. Bondy and Mercier proved an analogue to Stanley's result for switching reconstruction of graphs. They proved that a digraph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . They also proved many other common results for both switching reconstructions. One significant difference between the directed and undirected problems is that there exist switching-nonreconstructible directed graphs on eight vertices, while Stanley's conjecture that every simple graph on five or more vertices is switching-reconstructible.

Bibliography

★ [BM]
 J. A. Bondy and F. Mercier. Switching reconstruction of digraphs. J. Graph Theory 67(2011), no. 4, 332-348.
