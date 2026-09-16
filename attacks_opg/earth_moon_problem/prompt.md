Attack the following open graph-theory problem.

Catalog id: earth_moon_problem
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/earth_moon_problem/
Original entry: http://www.openproblemgarden.org/op/earth_moon_problem
Problem attributed to: Ringel, G. (posted 2013-03-06)

=== Problem statement (OpenProblemGarden) ===
Title: Earth-Moon Problem
Problem What is the maximum number of colours needed to colour countries such that no two countries sharing a common border have the same colour in the case where each country consists of one region on earth and one region on the moon ?

=== Discussion / context (OpenProblemGarden) ===
In term of graphs, it can be rephrased as follows. What is the maximum chromatic number of a graph $ G $ which is the union of two planar graphs (on the same vertex set)? If a graph $ G $ on $ n $ vertices is the union of two planar graphs, then it has at most $ 2(3n-6) $ edges, and so it is has a vertex of degree at most $ 11 $ . An easy induction shows that $ G $ is 12-colourable, as observed by Heawood [He]. Gardner [G] reported an example requiring 9 colours (the join of $ C_5 $ and $ K_6 $ ). It is not known if configurations exist requiring 10, 11, or 12 colours. More generally, one may ask for the maximum chromatic number of the union of $ k $ planar graphs. Problem What is the maximum chromatic number of a graph $ G $ which is the union of $ k $ planar graphs? The same reasoning as above shows that $ 6k $ colours are always sufficient. The minimum number of planar graphs to decompose a complete graph [BW] gives a lower bound of $ 6k-2 $ for $ k \ne 2 $ .

=== References listed by OpenProblemGarden ===
- [BW] L. W. Beineke and A. T. White, Topological Graph Theory, Selected Topics in Graph Theory, L. W. Beineke and R. J. Wilson, eds., Academic Press, 15-50, 1978.
- [G] M. Gardner, Mathematical Recreations: The Coloring of Unusual Maps Leads Into Uncharted Territory. Sci. Amer. 242, 14-22, 1980.
- [He] P.J. Heawood, Map Colour Theorems. Quart. J. Pure Appl. Math. 24, 332-338, 1890.
- *[R] G. Ringel, Färbungsprobleme auf Flachen und Graphen. Berlin: Deutsche Verlag der Wissenschaften, 1959.

=== Catalog page (statement + literature review) ===
Earth-Moon Problem — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Earth–Moon problem—finding the maximum chromatic number of a biplanar graph (union of two planar graphs)—remains open with bounds $9 \leq \chi \leq 12$ unchanged since the problem was posted. In 2023, Eppstein disproved Gethner's conjecture that 2-blowups of planar graphs are always biplanar, using iterated Kleetopes as counterexamples; and Kirchweger, Scheucher, and Szeider used SAT-based methods to show that at least one of Gethner's proposed 10-chromatic candidate graphs is not biplanar.

 Cited literature (2)

 
 
 
partial On the Biplanarity of Blowups
 (2023)
 

 
 David Eppstein · 31st International Symposium on Graph Drawing and Network Visualization (GD 2023) · arXiv:2301.09246

Disproves Gethner's conjecture that 2-blowups of planar graphs are always biplanar by constructing iterated Kleetopes whose 2-blowups are not biplanar, while also giving positive biplanarity results for certain graph classes.
 

 
 
partial SAT-Based Generation of Planar Graphs
 (2023)
 

 
 Markus Kirchweger, Manfred Scheucher, Stefan Szeider · 26th International Conference on Theory and Applications of Satisfiability Testing (SAT 2023) · doi:10.4230/LIPIcs.SAT.2023.14

Applies SAT encodings with dynamic symmetry breaking to test biplanarity, and shows that a graph derived from $C_5 \boxtimes K_4$ with one vertex removed (one of Gethner's candidate 10-chromatic biplanar graphs) is not biplanar.
 

 

 Reviewer notes. Gethner's 2018 survey 'To the Moon and Beyond' (Springer book chapter in 'Graph Theory: Favorite Conjectures and Open Problems – 2', edited by Gera, Haynes, Hedetniemi) introduced the conjecture that the answer is 11 and proposed $C_7 \boxtimes K_4$ and a vertex deletion from $C_5 \boxtimes K_4$ as candidate 10-chromatic biplanar graphs; the Springer page was inaccessible due to authentication redirect so this paper is not in since_posted. The fundamental bounds ($9 \leq \chi \leq 12$) are unchanged. Eppstein's paper won Best Paper at GD 2023 and was subsequently published in the Journal of Graph Algorithms and Applications (2024). The DROPS page for Kirchweger et al. confirmed the venue and DOI but the full text (PDF) was unreadable by WebFetch; the specific Earth-Moon result attributed to that paper (eliminating one of Gethner's candidates) is reported in Wikipedia's Earth–Moon problem article.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Problem. What is the maximum number of colours needed to colour countries such that no two countries sharing a common border have the same colour in the case where each country consists of one region on earth and one region on the moon ?

Discussion

In term of graphs, it can be rephrased as follows. What is the maximum chromatic number of a graph $ G $ which is the union of two planar graphs (on the same vertex set)? If a graph $ G $ on $ n $ vertices is the union of two planar graphs, then it has at most $ 2(3n-6) $ edges, and so it is has a vertex of degree at most $ 11 $ . An easy induction shows that $ G $ is 12-colourable, as observed by Heawood [He]. Gardner [G] reported an example requiring 9 colours (the join of $ C_5 $ and $ K_6 $ ). It is not known if configurations exist requiring 10, 11, or 12 colours. More generally, one may ask for the maximum chromatic number of the union of $ k $ planar graphs. Problem What is the maximum chromatic number of a graph $ G $ which is the union of $ k $ planar graphs? The same reasoning as above shows that $ 6k $ colours are always sufficient. The minimum number of planar graphs to decompose a complete graph [BW] gives a lower bound of $ 6k-2 $ for $ k \ne 2 $ .

Bibliography

 [BW]
 L. W. Beineke and A. T. White, Topological Graph Theory, Selected Topics in Graph Theory, L. W. Beineke and R. J. Wilson, eds., Academic Press, 15-50, 1978.

 [G]
 M. Gardner, Mathematical Recreations: The Coloring of Unusual Maps Leads Into Uncharted Territory. Sci. Amer. 242, 14-22, 1980.

 [He]
 P.J. Heawood, Map Colour Theorems. Quart. J. Pure Appl. Math. 24, 332-338, 1890.

★ [R]
 G. Ringel, Färbungsprobleme auf Flachen und Graphen. Berlin: Deutsche Verlag der Wissenschaften, 1959.
