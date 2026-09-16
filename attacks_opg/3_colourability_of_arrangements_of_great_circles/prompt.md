Attack the following open graph-theory problem.

Catalog id: 3_colourability_of_arrangements_of_great_circles
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/3_colourability_of_arrangements_of_great_circles/
Original entry: http://www.openproblemgarden.org/op/3_colourability_of_arrangements_of_great_circles
Problem attributed to: Felsner, Stefan, Hurtado, Ferran, Noy, Marc, Streinu, Ileana (posted 2009-01-19)

=== Problem statement (OpenProblemGarden) ===
Title: 3-Colourability of Arrangements of Great Circles
Consider a set $ S $ of great circles on a sphere with no three circles meeting at a point. The arrangement graph of $ S $ has a vertex for each intersection point, and an edge for each arc directly connecting two intersection points. So this arrangement graph is 4-regular and planar. Conjecture Every arrangement graph of a set of great circles is $ 3 $ -colourable.

=== Discussion / context (OpenProblemGarden) ===
It is NP-complete to test 3-colourability of planar 4-regular graphs in general [D80]. Arrangement graphs of general circles on the sphere can require four colors [K90]. A stronger conjecture states that the arrangement graph of every set of great circles is $ 3 $ -choosable . A natural approach is to use the machinery of [AT92]. Previously appeared here .

=== References listed by OpenProblemGarden ===
- [AT92] Noga Alon and Michael Tarsi. Colourings and orientations of graphs. Combinatorica 12:125--134, 1992.
- *[FHNS00] Stefan Felsner, Ferran Hurtado, Marc Noy, and Ileana Streinu. Hamiltonicity and colorings of arrangement graphs. In Proc. 11th Annual ACM-SIAM Symp. Discrete Algorithms (SODA), pages 155--164, January 2000.
- [FHNS06] Felsner, Stefan; Hurtado, Ferran; Noy, Marc; Streinu, Ileana. Hamiltonicity and colorings of arrangement graphs. Discrete Appl. Math. 154 (2006), no. 17, 2470--2483.
- [K90] G. Koester. 4-critical, 4-valent planar graphs constructed with crowns. Math. Scand., 67:15--22, 1990.
- [D80] D. P. Dailey. Uniqueness of colorability and colorability of planar 4-regular graphs are NP-complete, Discrete Math. 30:289--193, 2980.

=== Catalog page (statement + literature review) ===
3-Colourability of Arrangements of Great Circles — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that every arrangement graph of great circles is $3$-colourable remains open. Chiu, Felsner, Scheucher, Schröder, Steiner, and Vogtenhuber (2022) proved 3-colourability for $\triangle$-saturated pseudocircle arrangements and showed $\chi_f(A) \le 3 + O(1/n)$ for all pairwise-intersecting pseudocircle arrangements, but neither result resolves the original problem restricted to great circles. A 2004 arXiv preprint by Cahit claiming a full proof was dismissed by the community as not constituting a valid proof.

 Cited literature (1)

 
 
 
partial Coloring circle arrangements: New 4-chromatic planar graphs
 (2022)
 

 
 Man-Kwun Chiu, Stefan Felsner, Manfred Scheucher, Felix Schröder, Raphael Steiner, Birgit Vogtenhuber · European Journal of Combinatorics · arXiv:2205.08181

Proves 3-colourability of the arrangement graph for $\triangle$-saturated pseudocircle arrangements and shows the fractional chromatic number of any pairwise-intersecting pseudocircle arrangement satisfies $\chi_f \le 3 + O(1/n)$; the conjecture for general great-circle arrangements is left open.
 

 

 Reviewer notes. The Cahit arXiv preprint (math/0408363, 2004) predates the OPG posting and was explicitly described by community members on the OPG page as not containing a valid proof; it is excluded from since_posted. The ScienceDirect page for the published Chiu et al. paper (doi via pii S0195669823001579, European J. Combinatorics Vol. 122, 2024) returned HTTP 403 and could not be directly verified; the arXiv abstract page was used instead. The TOPP problem page (p44) confirmed open status but appeared to have last been updated around 2002. No post-2022 paper resolving the conjecture was found.

 
 Auto-reviewed 2026-05-07 with claude-sonnet-4-6 (web search enabled) · 338s.
 

Conjecture. Every arrangement graph of a set of great circles is $ 3 $ -colourable.

Keywords:
arrangement graph · graph coloring

Discussion

It is NP-complete to test 3-colourability of planar 4-regular graphs in general [D80]. Arrangement graphs of general circles on the sphere can require four colors [K90]. A stronger conjecture states that the arrangement graph of every set of great circles is $ 3 $ -choosable . A natural approach is to use the machinery of [AT92]. Previously appeared here .

Bibliography

 [AT92]
 Noga Alon and Michael Tarsi. Colourings and orientations of graphs . Combinatorica 12:125--134, 1992.

★ [FHNS00]
 Stefan Felsner, Ferran Hurtado, Marc Noy, and Ileana Streinu. Hamiltonicity and colorings of arrangement graphs . In Proc. 11th Annual ACM-SIAM Symp. Discrete Algorithms (SODA), pages 155--164, January 2000.

 [FHNS06]
 Felsner, Stefan; Hurtado, Ferran; Noy, Marc; Streinu, Ileana. Hamiltonicity and colorings of arrangement graphs . Discrete Appl. Math. 154 (2006), no. 17, 2470--2483.

 [K90]
 G. Koester. 4-critical, 4-valent planar graphs constructed with crowns. Math. Scand., 67:15--22, 1990.

 [D80]
 D. P. Dailey. Uniqueness of colorability and colorability of planar 4-regular graphs are NP-complete , Discrete Math. 30:289--193, 2980.
