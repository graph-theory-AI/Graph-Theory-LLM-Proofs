Attack the following open graph-theory problem.

Catalog id: acyclic_edge_coloring
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/acyclic_edge_coloring/
Original entry: http://www.openproblemgarden.org/op/acyclic_edge_coloring
Problem attributed to: Fiamcik, Jozef (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Acyclic edge-colouring
Conjecture Every simple graph with maximum degree $ \Delta $ has a proper $ (\Delta+2) $ - edge-colouring so that every cycle contains edges of at least three distinct colours.

=== Discussion / context (OpenProblemGarden) ===
An edge-colouring with the property that every cycle contains edges of at least three distinct colours is called an acyclic edge-colouring. It is known (see [AMR]) that every graph of maximum degree $ \Delta $ has an acyclic edge-colouring of size $ O(\Delta ) $ . The best upper bound so far is $ 4\Delta -4 $ and is due to Esperet and Parreau [EP]. It is also known (see [ASZ]) that this conjecture is true for graphs with girth at least $ C \Delta \log(\Delta ) $ (for some fixed constant $ C $ ).

=== References listed by OpenProblemGarden ===
- [AMR] N. Alon, C. McDiarmid and B. Reed, Acyclic colouring of graphs, Random Structures and Algorithms 2 (1991), 277-288. MathSciNet
- [ASZ] N. Alon, B. Sudakov and A. Zaks, Acyclic edge-colorings of graphs, J. Graph Theory 37 (2001), 157-167. MathSciNet
- [EP] L. Esperet and A. Parreau, Acyclic edge-coloring using entropy compression, arXiv:1206.1535 [math.CO].

=== Catalog page (statement + literature review) ===
Acyclic edge-colouring — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that every simple graph with maximum degree $\Delta$ has a proper acyclic edge-colouring using at most $\Delta+2$ colours remains open. Since the problem was posted, the general upper bound has been reduced below $4\Delta-4$, reaching approximately $3.142(\Delta-1)+1$ as of 2026, and the conjecture has been confirmed for several special classes including 3-sparse graphs; moreover, Delcourt, Li, and Postle announced in 2023 that $(1+o(1))\Delta$ colours always suffice, though the exact Fiamčík bound is still unproved for general graphs.

 Cited literature (4)

 
 
 
partial Acyclic Edge Coloring of 3-sparse Graphs
 (2025)
 

 
 Nevil Anto, Manu Basavaraju, Shashanka Kulamarva · Discrete Mathematics · arXiv:2501.11281 · doi:10.1016/j.disc.2026.115135

Proves Fiamčík's conjecture ($a'(G) \leq \Delta+2$) for all 3-sparse graphs, i.e., graphs in which every edge has at least one endpoint of degree at most 3.
 

 
 
partial An improvement on the bound for the acyclic chromatic index
 (2026)
 

 
 Lefteris Kirousis, John Livieratos, Alexandros Singh · arXiv preprint · arXiv:2602.14859

Proves the general upper bound $a'(G) \leq 3.142(\Delta-1)+1$ for any graph with maximum degree $\Delta$, improving the previous best bound due to Fialho et al. (2020).
 

 
 
partial Upper Bounds on the Acyclic Chromatic Index of Degenerate Graphs
 (2023)
 

 
 Nevil Anto, Manu Basavaraju, Suresh Manjanath Hegde, Shashanka Kulamarva · Discrete Mathematics · arXiv:2305.01948

Proves $a'(G) \leq \Delta+5$ for all 3-degenerate graphs, narrowing the gap to the conjectured $\Delta+2$ for this class.
 

 
 
partial Planar graphs are acyclically edge $(\Delta + 5)$-colorable
 (2023)
 

 
 Qiaojun Shu, Guohui Lin · arXiv preprint · arXiv:2306.15813

Shows that every planar graph satisfies $a'(G) \leq \Delta+5$ via discharging, giving the current best bound for planar graphs while the conjecture ($\Delta+2$) remains open for this class.
 

 

 Reviewer notes. An important announced result — Delcourt, Li, and Postle, 'The Acyclic Edge Coloring Conjecture holds asymptotically,' showing $(1+o(1))\Delta$ colours suffice — was presented at the Georgia Tech Graph Theory Seminar on 17 October 2023, but no arXiv preprint or journal URL was locatable; it cannot be included in since_posted. A 2022 arXiv preprint (arXiv:2202.13846, Kirousis–Livieratos) claimed the stronger bound $2\Delta-1$ but was subsequently withdrawn due to errors in key lemmas and must not be cited. The intermediate general-bound improvement by Fialho et al. (2020) — referenced as the prior best in arXiv:2602.14859 — was not independently verified and is therefore not listed.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 193s.
 

Conjecture. Every simple graph with maximum degree $ \Delta $ has a proper $ (\Delta+2) $ - edge-colouring so that every cycle contains edges of at least three distinct colours.

Keywords:
edge-coloring

Discussion

An edge-colouring with the property that every cycle contains edges of at least three distinct colours is called an acyclic edge-colouring. It is known (see [AMR]) that every graph of maximum degree $ \Delta $ has an acyclic edge-colouring of size $ O(\Delta ) $ . The best upper bound so far is $ 4\Delta -4 $ and is due to Esperet and Parreau [EP]. It is also known (see [ASZ]) that this conjecture is true for graphs with girth at least $ C \Delta \log(\Delta ) $ (for some fixed constant $ C $ ).

Bibliography

 [AMR]
 N. Alon, C. McDiarmid and B. Reed, Acyclic colouring of graphs, Random Structures and Algorithms 2 (1991), 277-288. MathSciNet
 MathSciNet

 [ASZ]
 N. Alon, B. Sudakov and A. Zaks, Acyclic edge-colorings of graphs , J. Graph Theory 37 (2001), 157-167. MathSciNet
 Acyclic edge-colorings of graphs · MathSciNet

 [EP]
 L. Esperet and A. Parreau, Acyclic edge-coloring using entropy compression , arXiv:1206.1535 [math.CO].
 Acyclic edge-coloring using entropy compression
