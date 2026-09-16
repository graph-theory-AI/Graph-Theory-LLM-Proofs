Attack the following open graph-theory problem.

Catalog id: edge_list_coloring_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/edge_list_coloring_conjecture/
Original entry: http://www.openproblemgarden.org/op/edge_list_coloring_conjecture

=== Problem statement (OpenProblemGarden) ===
Title: Edge list coloring conjecture
Conjecture Let $ G $ be a loopless multigraph. Then the edge chromatic number of $ G $ equals the list edge chromatic number of $ G $ .

=== Discussion / context (OpenProblemGarden) ===
The list edge chromatic number of $ G $ is also known as the list chromatic index , the edge choosability , or the edge choice number of $ G $ . It is the list chromatic number of the line graph of $ G $ . Similarly, the edge chromatic number of $ G $ is also known as the edge chromatic index , and it is the chromatic number of the line graph of $ G $ . The chromatic number of a graph is always less than or equal to the list chromatic number; the two quantities differ in general, but the conjecture says that they coincide for line graphs. Sometime the conjecture is simply referred to as the list coloring conjecture , although this is perhaps poor terminology since there exist other conjectures about list coloring. Perhaps the most famous partial result is Galvin's theorem [G] that the conjecture holds for bipartite multigraphs. Galvin's result settled the well-known Dinitz conjecture in the affirmative. The conjecture has been attributed to many different people. See [JT, Problem 12.20] for a history of the problem up to 1995.

=== References listed by OpenProblemGarden ===
- [G] Fred Galvin, The list chromatic index of a bipartite multigraph. J. Combin. Theory Ser. B 63 (1995), 153–158.
- [JT] Tommy R. Jensen and Bjarne Toft, Graph Coloring Problems. New York: Wiley-Interscience, 1995.

=== Catalog page (statement + literature review) ===
Edge list coloring conjecture — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The List Edge Coloring Conjecture (sometimes called the List Coloring Conjecture) remains open in general. The strongest known general result is still Kahn's asymptotic theorem from 1996/2000, with Galvin's theorem (1995) settling the bipartite multigraph case. Recent work (e.g. Bonamy-Delcourt-Lang-Postle 2020/2023) has refined Kahn's asymptotic result to a local-list-size version and to hypergraph/correspondence-coloring generalizations, but the original conjecture for all (multi)graphs is still unproved.

 Cited literature (2)

 
 
 
partial Edge-colouring graphs with local list sizes
 (2023)
 

 
 Marthe Bonamy, Michelle Delcourt, Richard Lang, Luke Postle · Journal of Combinatorial Theory, Series B (also arXiv:2007.14944) · arXiv:2007.14944 · doi:10.1016/j.jctb.2023.10.010

Proves a local-list-size strengthening of Kahn's asymptotic List Coloring Conjecture: for graphs of sufficiently large maximum degree and minimum degree at least $\ln^{25}\Delta$, lists of size $(1+o(1))\max\{\deg(u),\deg(v)\}$ on each edge $uv$ suffice for a proper edge list-colouring; extended to hypergraphs and correspondence colouring.
 

 
 
partial Multigraph edge-coloring with local list sizes
 (2023)
 

 
 Abhishek Dhawan · arXiv preprint (later Discrete Mathematics) · arXiv:2307.12094

Extends the local-list-size approach to multigraphs, recovering local analogues of Vizing's and Shannon's theorems and a result of Conley-Grebik-Pikhurko in the list/local setting; gives further asymptotic-style partial progress toward the list edge coloring conjecture for multigraphs.
 

 

 Reviewer notes. The conjecture is widely cited as one of the central open problems in edge colouring; Wikipedia (as of 2025) still lists it as an Unsolved Problem. Verified that no full proof or counterexample has appeared after the 2008-09-25 OPG posting date. Cited entries are partial/asymptotic results (extending Kahn 1996/2000) verified via their arXiv abstract pages; the Bonamy-Delcourt-Lang-Postle paper is accepted in JCTB with DOI 10.1016/j.jctb.2023.10.010 (the publisher landing page returned 403/redirect, but the arXiv metadata explicitly states the JCTB acceptance). Did not chase planar / class-1 / specific-graph-class results beyond what was already mentioned in the OPG entry.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Let $ G $ be a loopless multigraph. Then the edge chromatic number of $ G $ equals the list edge chromatic number of $ G $ .

Discussion

The list edge chromatic number of $ G $ is also known as the list chromatic index , the edge choosability , or the edge choice number of $ G $ . It is the list chromatic number of the line graph of $ G $ . Similarly, the edge chromatic number of $ G $ is also known as the edge chromatic index , and it is the chromatic number of the line graph of $ G $ . The chromatic number of a graph is always less than or equal to the list chromatic number; the two quantities differ in general, but the conjecture says that they coincide for line graphs. Sometime the conjecture is simply referred to as the list coloring conjecture , although this is perhaps poor terminology since there exist other conjectures about list coloring. Perhaps the most famous partial result is Galvin's theorem [G] that the conjecture holds for bipartite multigraphs. Galvin's result settled the well-known Dinitz conjecture in the affirmative. The conjecture has been attributed to many different people. See [JT, Problem 12.20] for a history of the problem up to 1995.

Bibliography

 [G]
 Fred Galvin, The list chromatic index of a bipartite multigraph. J. Combin. Theory Ser. B 63 (1995), 153–158.

 [JT]
 Tommy R. Jensen and Bjarne Toft, Graph Coloring Problems. New York: Wiley-Interscience, 1995.

Related conjectures

 
 implies
 List Ramsey R_ℓ(K_{1,2}, k) parity gap
 open
 The target's context explicitly states that the odd-k case of determining R_ell(K_{1,2}, k) is equivalent to the List Colouring Conjecture restricted to cliques of even order, i.e. to whether chi'_ell(K_n) = n-1 for even n. The full LCC (source) asserts chi'_ell(G) = chi'(G) for every loopless multigraph; restricting to G = K_n with n even, where chi'(K_n) = n-1 (K_n is Class 1 for even n), the LCC gives chi'_ell(K_n) = n-1 and thus settles the target question. This is a clean restriction (hypothesis-class containment: even cliques are loopless multigraphs), so the source is strictly stronger and the claimed direction is correct; the target only pins down the even-clique case, so 'implies', not 'equivalent_to'.
 

 
 related to
 Total Colouring Conjecture
 partial
 The TCC page states only that the Edge List Coloring Conjecture 'would imply chi''(G) <= Delta(G)+3' (via ch'(G)=chi'(G) <= Delta+1 by Vizing and chi'' <= ch'+2). Delta+3 is strictly weaker than TCC's Delta+2 bound, so ELCC does NOT imply TCC. Conversely TCC, a statement about the total chromatic number, says nothing about list edge colorings, so it does not imply ELCC. The connection is a weak-bound consequence only: the correct classification is related_only, with no implication in either direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
