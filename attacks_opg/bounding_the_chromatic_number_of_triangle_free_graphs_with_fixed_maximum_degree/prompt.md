Attack the following open graph-theory problem.

Catalog id: bounding_the_chromatic_number_of_triangle_free_graphs_with_fixed_maximum_degree
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/bounding_the_chromatic_number_of_triangle_free_graphs_with_fixed_maximum_degree/
Original entry: http://www.openproblemgarden.org/op/bounding_the_chromatic_number_of_triangle_free_graphs_with_fixed_maximum_degree
Problem attributed to: Kostochka, Alexandr V., Reed, Bruce A. (posted 2009-04-17)

=== Problem statement (OpenProblemGarden) ===
Title: Bounding the chromatic number of triangle-free graphs with fixed maximum degree
Conjecture A triangle-free graph with maximum degree $ \Delta $ has chromatic number at most $ \ceil{\frac{\Delta}{2}}+2 $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is a special case of Reed's $ \omega $ , $ \Delta $ , and $ \chi $ conjecture, which posits that for any graph, $ \chi \leq \lceil\frac 12(\Delta+1+\omega)\rceil $ , where $ \omega $ , $ \Delta $ , and $ \chi $ are the clique number, maximum degree, and chromatic number of the graph respectively. Reed's conjecture is very easy to prove for complements of triangle-free graphs, but the triangle-free case seems challenging and interesting in its own right. This conjecture is very much true for large values of $ \Delta $ ; Johansson proved that triangle-free graphs have chromatic number at most $ \frac{9\Delta}{\ln \Delta} $ . Surprisingly, the question appears to be open for every value of $ \Delta $ greater than four, up until Johansson's result implies the conjecture. Kostochka previously proved that the chromatic number of a triangle-free graph is at most $ \frac{2\Delta}{3}+2 $ , and he proved that for every $ \Delta \geq 5 $ there is a $ g $ for which a graph of girth $ g $ has chromatic number at most $ \frac{\Delta}2+2 $ . Specifically, he showed that $ g \geq 4(\Delta+2)\ln \Delta $ is sufficient. In [K] he posed the general problem: "To find the best upper estimate for the chromatic number of the graph in terms of the maximal degree and density or girth." The conjecture is implied by Brooks' Theorem for $ \Delta\leq 5 $ . The three smallest open values of $ \Delta $ offer natural entry points to this problem. The easiest seems to be: Problem Does there exist a $ 6 $ -chromatic triangle-free graph of maximum degree 6? Perhaps looking at graphs of girth at least five would also be a good starting point.

=== References listed by OpenProblemGarden ===
- [K] Kostochka, A. V., Degree, girth and chromatic number. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, pp. 679--696, Colloq. Math. Soc. János Bolyai, 18, North-Holland, Amsterdam-New York, 1978.
- *[R] Reed, B.A., , and , J. Graph Theory 27 (1998) 177-212.

=== Catalog page (statement + literature review) ===
Bounding the chromatic number of triangle-free graphs with fixed maximum degree — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The Kostochka-Reed conjecture that every triangle-free graph with maximum degree $\Delta$ has chromatic number at most $\lceil \Delta/2 \rceil + 2$ remains open for finite values of $\Delta$ between 6 and the threshold above which Johansson's $O(\Delta/\log\Delta)$ bound (with Molloy's optimal constant) implies it. Computational work by Goedgebeur on minimal triangle-free 6-chromatic graphs has narrowed the smallest open case (whether a 6-chromatic triangle-free graph of maximum degree 6 exists) by showing such a graph would need between 32 and 40 vertices, but no proof or counterexample for the original conjecture has been published.

 Cited literature (1)

 
 
 
partial On minimal triangle-free 6-chromatic graphs
 (2017)
 

 
 Jan Goedgebeur · arXiv preprint · arXiv:1707.07581 · doi:10.1002/jgt.22467

Computationally shows that the smallest triangle-free 6-chromatic graphs have between 32 and 40 vertices and catalogues triangle-free 5-chromatic graphs up to 24 vertices, providing partial computational support for Reed's conjecture (and hence the Kostochka-Reed $\lceil\Delta/2\rceil+2$ bound) on triangle-free graphs of small order, directly relevant to the smallest open case ($\Delta=6$) of the conjecture.
 

 

 Reviewer notes. ScienceDirect paywalls (HTTP 403) prevented direct verification of 'A note on Reed's conjecture for triangle-free graphs' (Discrete Math. 2023, S0012365X23002959), so it is not cited despite being relevant. Several asymptotic results (Johansson 1996, Molloy 2019, Bonamy-Kelly-Nelson-Postle, Davies-Illingworth) confirm the conjecture for sufficiently large $\Delta$ but were already implied by Johansson's bound at the time of OPG posting; the conjecture's challenge is for fixed small $\Delta\geq 6$, and there no full proof or counterexample has been verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. A triangle-free graph with maximum degree $ \Delta $ has chromatic number at most $ \ceil{\frac{\Delta}{2}}+2 $ .

Keywords:
chromatic number · girth · maximum degree · triangle free

Discussion

This conjecture is a special case of Reed's $ \omega $ , $ \Delta $ , and $ \chi $ conjecture, which posits that for any graph, $ \chi \leq \lceil\frac 12(\Delta+1+\omega)\rceil $ , where $ \omega $ , $ \Delta $ , and $ \chi $ are the clique number, maximum degree, and chromatic number of the graph respectively. Reed's conjecture is very easy to prove for complements of triangle-free graphs, but the triangle-free case seems challenging and interesting in its own right. This conjecture is very much true for large values of $ \Delta $ ; Johansson proved that triangle-free graphs have chromatic number at most $ \frac{9\Delta}{\ln \Delta} $ . Surprisingly, the question appears to be open for every value of $ \Delta $ greater than four, up until Johansson's result implies the conjecture. Kostochka previously proved that the chromatic number of a triangle-free graph is at most $ \frac{2\Delta}{3}+2 $ , and he proved that for every $ \Delta \geq 5 $ there is a $ g $ for which a graph of girth $ g $ has chromatic number at most $ \frac{\Delta}2+2 $ . Specifically, he showed that $ g \geq 4(\Delta+2)\ln \Delta $ is sufficient. In [K] he posed the general problem: "To find the best upper estimate for the chromatic number of the graph in terms of the maximal degree and density or girth." The conjecture is implied by Brooks' Theorem for $ \Delta\leq 5 $ . The three smallest open values of $ \Delta $ offer natural entry points to this problem. The easiest seems to be: Problem Does there exist a $ 6 $ -chromatic triangle-free graph of maximum degree 6? Perhaps looking at graphs of girth at least five would also be a good starting point.

Bibliography

 [K]
 Kostochka, A. V., Degree, girth and chromatic number. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, pp. 679--696, Colloq. Math. Soc. János Bolyai, 18, North-Holland, Amsterdam-New York, 1978.

★ [R]
 Reed, B.A., $ \omega, \Delta $ , and $ \chi $ , J. Graph Theory 27 (1998) 177-212.

Related conjectures

 
 implied by
 Reed's omega, delta, and chi conjecture
 partial
 Triangle-free means omega(G) <= 2. Reed's conjectured bound then gives chi <= ceil((Delta+1)/2 + 1) = ceil((Delta+3)/2). For even Delta this equals Delta/2 + 2 = ceil(Delta/2)+2; for odd Delta it equals (Delta+3)/2 = ceil(Delta/2)+1 <= ceil(Delta/2)+2. So Reed's conjecture (source) implies the triangle-free conjecture (target) by restriction to omega <= 2, with the correct rounding check. The target's own Open Problem Garden context states explicitly: 'This conjecture is a special case of Reed's omega, Delta, and chi conjecture.' Direction as claimed.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
