Attack the following open graph-theory problem.

Catalog id: grahams_conjecture_on_tree_reconstruction
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/grahams_conjecture_on_tree_reconstruction/
Original entry: http://www.openproblemgarden.org/op/grahams_conjecture_on_tree_reconstruction
Problem attributed to: Graham, Ronald L. (posted 2007-03-18)

=== Problem statement (OpenProblemGarden) ===
Title: Graham's conjecture on tree reconstruction
Problem for every graph $ G $ , we let $ L(G) $ denote the line graph of $ G $ . Given that $ G $ is a tree, can we determine it from the integer sequence $ |V(G)|, |V(L(G))|, |V(L(L(G)))|, \ldots $ ?

=== Discussion / context (OpenProblemGarden) ===
Graph reconstruction is a notoriously difficult subject. This conjecture is an unusual type of reconstruction problem where our class of graphs is very limited - just trees, but we are also given relatively little information - just a sequence of integers.

=== References listed by OpenProblemGarden ===
- [GR] C. Godsil and G. Royle, Algebraic graph theory. Graduate Texts in Mathematics, 207. Springer-Verlag, New York, 2001 (page 18).

=== Catalog page (statement + literature review) ===
Graham's conjecture on tree reconstruction — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Graham's conjecture remains open. Cooper, Kay, and Swifton (arXiv 2011, J. Combinatorics 2018) showed that the number of trees on $n$ vertices distinguishable by their Graham sequence is at least $e^{\Omega((\log n)^{3/2})}$, by constructing many caterpillars via the Prouhet-Tarry-Escott problem; this gives a strong lower bound but does not resolve the conjecture. Weatherspoon and Zeilberger (2025, experimental note) computationally verified the conjecture for all trees up to 11 vertices, with partial verification up to 16 vertices.

 Cited literature (3)

 
 
 
partial Graham's Tree Reconstruction Conjecture and a Waring-Type Problem on Partitions
 (2011)
 

 
 Joshua Cooper, Bill Kay, Anton Swifton · arXiv preprint (later J. Combinatorics 9(3), 2018) · arXiv:1109.0522

Provides a lower bound: the number of trees on $n$ vertices distinguishable by their iterated line-graph vertex-count sequence is at least $e^{\Omega((\log n)^{3/2})}$, via caterpillar constructions linked to the Prouhet-Tarry-Escott problem.
 

 
 
partial An Experimental Note on Graham's Tree Reconstruction Conjecture
 (2025)
 

 
 Kaylee Weatherspoon, Doron Zeilberger · Personal Journal of Shalosh B. Ekhad and Doron Zeilberger

Computationally verifies Graham's conjecture for all trees on up to 11 vertices, with partial verification for trees on 12-16 vertices.
 

 
 
partial Addressing Johnson graphs, complete multipartite graphs, odd cycles and other graphs
 (2018)
 

 
 Noga Alon, Sebastian M. Cioabă, Brandon D. Gilbert, Jack H. Koolen, Brendan D. McKay · arXiv preprint · arXiv:1808.04757

Resolves the question: the formula is confirmed for $n \in \{6, 7, 8, 9\}$ (corresponding odd cycles $C_{13}, C_{15}, C_{17}, C_{19}$) but shown to fail for $n = 11$.
 

 

 Reviewer notes. The arXiv version (1109.0522) was verified directly; the published Journal of Combinatorics 2018 PDF (Int. Press) returned only binary content via WebFetch but its existence and TOC reference is consistent with the arXiv v2 (Aug 2017) timing. Weatherspoon-Zeilberger note is verified via Zeilberger's personal journal listing and HTML version; it is not on arXiv. The original conjecture as stated remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Problem. for every graph $ G $ , we let $ L(G) $ denote the line graph of $ G $ . Given that $ G $ is a tree, can we determine it from the integer sequence $ |V(G)|, |V(L(G))|, |V(L(L(G)))|, \ldots $ ?

Keywords:
reconstruction · tree

Discussion

Graph reconstruction is a notoriously difficult subject. This conjecture is an unusual type of reconstruction problem where our class of graphs is very limited - just trees, but we are also given relatively little information - just a sequence of integers.

Bibliography

 [GR]
 C. Godsil and G. Royle, Algebraic graph theory. Graduate Texts in Mathematics, 207. Springer-Verlag, New York, 2001 (page 18).
