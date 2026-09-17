Attack the following open graph-theory problem.

Catalog id: oriented_chromatic_number_of_planar_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/oriented_chromatic_number_of_planar_graphs/
Original entry: http://www.openproblemgarden.org/op/oriented_chromatic_number_of_planar_graphs

=== Problem statement (OpenProblemGarden) ===
Title: Oriented chromatic number of planar graphs
An oriented colouring of an oriented graph is assignment $ c $ of colours to the vertices such that no two arcs receive ordered pairs of colours $ (c_1,c_2) $ and $ (c_2,c_1) $ . It is equivalent to a homomorphism of the digraph onto some tournament of order $ k $ . Problem What is the maximal possible oriented chromatic number of an oriented planar graph?

=== Discussion / context (OpenProblemGarden) ===
Raspaud and Sopena [RS] showed using Borodin's result about acyclic chromatic number of planar graphs, that every planar oriented graph has oriented chromatic number at most 80. (Their motivation came from a work of Courcelle [C] concerning the monadic second-order logic of graphs. That, however, deals with a stronger variant of coloring.) On the other hand, Marshall [M] showed that there is an oriented planar graph with oriented chromatic number at least~17.

=== References listed by OpenProblemGarden ===
- [C] B. Courcelle, The monadic second order logic of graphs VI: On several representations of graphs by relational structures, Discrete Appl. Math. 54 ( 1994),
- [M] T. H. Marshall. On -universal graphs. Research Report 2001-510, KAM-DIMATIA Series, 2001.
- *[RS] A. Raspaud and E. Sopena. Good and semi-strong colorings of oriented planar graphs. Inform. Process. Lett., 51(4):171–174, 1994. MathSciNet

=== Catalog page (statement + literature review) ===
Oriented chromatic number of planar graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The problem remains open. The upper bound of 80 (Raspaud–Sopena, 1994) has not been improved for general oriented planar graphs. The lower bound, stated as 17 in the 2007 OPG posting, was subsequently raised to 18 by Marshall in a paper published in Ars Combinatoria 120 (2015), so the answer is known to lie in $[18, 80]$.

 Cited literature (1)

 
 
 
partial On Oriented Graphs with Certain Extension Properties
 (2015)
 

 
 T.H. Marshall · Ars Combinatoria

Proves the existence of an oriented planar graph with oriented chromatic number at least 18, improving the previously known lower bound of 17.
 

 

 Reviewer notes. Sopena's authoritative 'Oriented Coloring Page' (last updated February 2022) confirms the bounds are 18 ≤ χo(planar) ≤ 80 as of that date. The Marshall 2015 paper (cited as [Ma12] on Sopena's page, appearing in Ars Combinatoria vol. 120) is confirmed in DBLP. ArXiv:2409.13076 (Clow, 2024) gives asymptotically improved bounds for graphs on surfaces of genus g but does not specifically improve the planar (genus 0) bound of 80. A 2025 SFU PhD thesis by Clow on 'Colouring Oriented Graphs on Surfaces' likely discusses this problem, but the PDF was unreadable by WebFetch. Results for special subclasses (triangle-free, bounded girth) exist with tighter bounds, but the main problem for all planar graphs is open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Problem. What is the maximal possible oriented chromatic number of an oriented planar graph?

Keywords:
oriented coloring · oriented graph · planar graph

Discussion

Raspaud and Sopena [RS] showed using Borodin's result about acyclic chromatic number of planar graphs, that every planar oriented graph has oriented chromatic number at most 80. (Their motivation came from a work of Courcelle [C] concerning the monadic second-order logic of graphs. That, however, deals with a stronger variant of coloring.) On the other hand, Marshall [M] showed that there is an oriented planar graph with oriented chromatic number at least~17.

Bibliography

 [C]
 B. Courcelle, The monadic second order logic of graphs VI: On several representations of graphs by relational structures, Discrete Appl. Math. 54 ( 1994),

 [M]
 T. H. Marshall. On $ \cal P $ -universal graphs . Research Report 2001-510, KAM-DIMATIA Series, 2001.
 On -universal graphs

★ [RS]
 A. Raspaud and E. Sopena. Good and semi-strong colorings of oriented planar graphs. Inform. Process. Lett., 51(4):171–174, 1994. MathSciNet
 MathSciNet
