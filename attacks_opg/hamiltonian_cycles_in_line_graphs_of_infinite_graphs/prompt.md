Attack the following open graph-theory problem.

Catalog id: hamiltonian_cycles_in_line_graphs_of_infinite_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/hamiltonian_cycles_in_line_graphs_of_infinite_graphs/
Original entry: http://www.openproblemgarden.org/op/hamiltonian_cycles_in_line_graphs_of_infinite_graphs
Problem attributed to: Georgakopoulos, Agelos (posted 2007-07-24)

=== Problem statement (OpenProblemGarden) ===
Title: Hamiltonian cycles in line graphs of infinite graphs
Conjecture \item If $ G $ is a 4-edge-connected locally finite graph, then its line graph is hamiltonian. \item If the line graph $ L(G) $ of a locally finite graph $ G $ is 4-connected, then $ L(G) $ is hamiltonian.

=== Discussion / context (OpenProblemGarden) ===
(Reproduced from [M].) A locally finite graph is hamiltonian, if its Freudenthal compactification (also called the end compactification, see [D]) contains a hamilton circle, i.e. a homeomorphic copy of $ S^1 $ containing all vertices. The first part is known for finite graphs. The proof uses the existence of two edge-disjoint spanning trees in 4-edge-connected graphs. In the infinite case, it would be enough to prove that a 4-edge-connected locally finite graph $ G $ has two edge-disjoint topological spanning trees (see [D]), one of which is connected as a subgraph of $ G $ . The problem is open even for the 1-ended case (where hamilton circles correspond to 2-way-infinite paths). The second part is widely open even in the finite case, where it was proposed by Thomassen [T].

=== References listed by OpenProblemGarden ===
- [D] Reinhard Diestel, Graph Theory, Third Edition, Springer, 2005.
- *[G] A. Georgakopoulos, Oberwolfach reports, 2007.
- [M] Bojan Mohar, Problem of the Month
- [T] Carsten Thomassen, Reflections on graph theory, J. Graph Theory 10 (1986) 309-324, MathSciNet

=== Catalog page (statement + literature review) ===
Hamiltonian cycles in line graphs of infinite graphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture has seen partial progress on Part 1: Florian Lehner proved (arXiv:1109.6787, JCTB 2014) that the line graph of every locally finite, highly edge-connected graph (≥6-edge-connected, in the sense of the end-faithful spanning tree packing result) has a Hamiltonian circle, extending the classical finite result; this is a weakening of the 4-edge-connected threshold asked in the conjecture. Part 2 (4-connected line graph implies Hamiltonian) remains widely open even for finite graphs, and Part 1 in its full 4-edge-connected form is still open.

 Cited literature (2)

 
 
 
partial On spanning tree packings of highly edge connected graphs
 (2014)
 

 
 Florian Lehner · Journal of Combinatorial Theory, Series B · arXiv:1109.6787

Extends the Tutte/Nash-Williams tree-packing theorem to end-faithful packings in certain locally finite graphs, establishing that the line graph of every locally finite, sufficiently highly edge-connected graph has a Hamiltonian circle (a partial result toward the 4-edge-connected conjecture).
 

 
 
partial Extending Cycles Locally to Hamilton Cycles
 (2016)
 

 
 Matthias Hamann, Florian Lehner, Julian Pott · Electronic Journal of Combinatorics

Proves that every connected, locally connected, locally finite, claw-free graph has a Hamilton circle; since line graphs are claw-free, this has implications for Hamiltonicity of line graphs of locally finite graphs with sufficient edge-connectivity.
 

 

 Reviewer notes. PDFs at florian-lehner.net and math.uni-hamburg.de were not text-readable via WebFetch, so exact theorem statements could not be directly verified. The claim that the Lehner 2014 paper covers the '6-edge-connected' case is consistently reported in secondary sources (including Mohar's problem page and search result abstracts) but could not be confirmed by reading the theorem directly. The Hamann-Lehner-Pott 2016 paper's abstract emphasizes claw-free locally connected graphs rather than mentioning line graphs explicitly; a corollary for line graphs may follow but was not directly verified. Both conjectures (4-edge-connected and 4-connected line graph) appear to remain open as of the search date.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. \item If $ G $ is a 4-edge-connected locally finite graph, then its line graph is hamiltonian. \item If the line graph $ L(G) $ of a locally finite graph $ G $ is 4-connected, then $ L(G) $ is hamiltonian.

Keywords:
hamiltonian · infinite graph · line graphs

Discussion

(Reproduced from [M].) A locally finite graph is hamiltonian, if its Freudenthal compactification (also called the end compactification, see [D]) contains a hamilton circle, i.e. a homeomorphic copy of $ S^1 $ containing all vertices. The first part is known for finite graphs. The proof uses the existence of two edge-disjoint spanning trees in 4-edge-connected graphs. In the infinite case, it would be enough to prove that a 4-edge-connected locally finite graph $ G $ has two edge-disjoint topological spanning trees (see [D]), one of which is connected as a subgraph of $ G $ . The problem is open even for the 1-ended case (where hamilton circles correspond to 2-way-infinite paths). The second part is widely open even in the finite case, where it was proposed by Thomassen [T].

Bibliography

 [D]
 Reinhard Diestel, Graph Theory, Third Edition, Springer, 2005.

★ [G]
 A. Georgakopoulos, Oberwolfach reports, 2007.

 [M]
 Bojan Mohar, Problem of the Month
 Problem of the Month

 [T]
 Carsten Thomassen, Reflections on graph theory, J. Graph Theory 10 (1986) 309-324, MathSciNet
 MathSciNet

Related conjectures

 
 implies
 Hamiltonian cycles in line graphs
 partial
 Item 2 of the source asserts: for every locally finite graph G with L(G) 4-connected, L(G) has a Hamilton circle in its Freudenthal compactification. Finite graphs are locally finite and the compactification of a finite graph adds no ends, so a Hamilton circle there is exactly a Hamilton cycle; thus item 2 restricted to finite graphs is verbatim Thomassen's conjecture (every 4-connected line graph is hamiltonian). Truth of the source (a conjunction including item 2) therefore forces the target. The source's own context confirms: 'The second part is widely open even in the finite case, where it was proposed by Thomassen [T].' Direction as claimed is correct: infinite version is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
