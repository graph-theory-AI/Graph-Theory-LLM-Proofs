Attack the following open graph-theory problem.

Catalog id: decomposing_an_eulerian_graph_into_cycles
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/decomposing_an_eulerian_graph_into_cycles/
Original entry: http://www.openproblemgarden.org/op/decomposing_an_eulerian_graph_into_cycles
Problem attributed to: Hajós, G. (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Decomposing an eulerian graph into cycles.
Conjecture Every simple eulerian graph on $ n $ vertices can be decomposed into at most $ \frac{1}{2}(n-1) $ cycles.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is tight because a complete graph on $ 2k+1 $ vertices cannot be covered by less than $ k $ cycles. There is a similar conjecture about decomposition of a connected graph into paths .

=== References listed by OpenProblemGarden ===
- * [L] L. Lovász, On covering of graphs. In Theory of Graphs (Proc. Colloq., Tihany, 1966), 231--236. Academic Press, New York, 1968.

=== Catalog page (statement + literature review) ===
Decomposing an eulerian graph into cycles. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Hajós' 1968 conjecture — that every simple Eulerian graph on $n$ vertices decomposes into at most $\lfloor (n-1)/2 \rfloor$ cycles — is still open in general. Since the OPG posting date (2013), it has been verified for several restricted classes: graphs of treewidth at most 3 (Botler–Sambinelli–Coelho–Lee, 2017), Eulerian graphs of pathwidth at most 6 (Fuchs–Gellert–Heinrich, 2017), and computationally for all Eulerian graphs of order at most 12 (Heinrich–Natale–Streicher, 2017). Approximate versions in dense graphs and progress on the closely related Erdős–Gallai cycle decomposition problem (Bucić–Montgomery, 2022) have also appeared.

 Cited literature (3)

 
 
 
partial On Gallai's and Hajós' Conjectures for graphs with treewidth at most 3
 (2017)
 

 
 Fábio Botler, Maycon Sambinelli, Rafael S. Coelho, Orlando Lee · arXiv preprint · arXiv:1706.04334

Verifies both Gallai's path decomposition conjecture and Hajós' cycle decomposition conjecture for graphs of treewidth at most 3.
 

 
 
partial Cycle decompositions of pathwidth-6 graphs
 (2017)
 

 
 Elke Fuchs, Laura Gellert, Irene Heinrich · arXiv preprint (later in J. Graph Theory, 2020) · arXiv:1705.07066

Verifies Hajós' conjecture for Eulerian graphs of pathwidth at most 6 and shows these graphs satisfy the small cycle double cover conjecture.
 

 
 
partial Hajós' cycle conjecture for small graphs
 (2017)
 

 
 Irene Heinrich, Marco V. Natale, Manuel Streicher · arXiv preprint · arXiv:1705.08724

Computationally verifies Hajós' conjecture for all simple Eulerian graphs on at most 12 vertices using preprocessing, heuristics, and integer programming.
 

 

 Reviewer notes. Search results also mentioned an approximate Hajós result for dense graphs by Girão, Granet, Kühn, Osthus (Path and cycle decompositions of dense graphs, arXiv:1911.05501) — not verified in detail here. Bucić–Montgomery (arXiv:2211.07689) addresses the related Erdős–Gallai cycle decomposition conjecture, not Hajós directly, so it is not cited as evidence on this problem.

 
 Auto-reviewed 2026-05-08 with claude (main agent, web search + fetch) (web search enabled).
 

Conjecture. Every simple eulerian graph on $ n $ vertices can be decomposed into at most $ \frac{1}{2}(n-1) $ cycles.

Discussion

This conjecture is tight because a complete graph on $ 2k+1 $ vertices cannot be covered by less than $ k $ cycles. There is a similar conjecture about decomposition of a connected graph into paths .

Bibliography

★ [L]
 L. Lovász, On covering of graphs. In Theory of Graphs (Proc. Colloq., Tihany, 1966), 231--236. Academic Press, New York, 1968.
