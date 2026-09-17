Attack the following open graph-theory problem.

Catalog id: domination_in_plane_triangulations
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/domination_in_plane_triangulations/
Original entry: http://www.openproblemgarden.org/op/domination_in_plane_triangulations
Problem attributed to: Matheson, Lesley R., Tarjan, Robert E. (posted 2009-05-04)

=== Problem statement (OpenProblemGarden) ===
Title: Domination in plane triangulations
Conjecture Every sufficiently large plane triangulation $ G $ has a dominating set of size $ \le \frac{1}{4} |V(G)| $ .

=== Discussion / context (OpenProblemGarden) ===
Motivated by some problems in multigrid computations, Matheson and Tarjan [MT] considered the problem of finding small dominating sets in plane triangulations. They proved that every such graph $ G $ has a dominating set of size $ \le \frac{1}{3} |V(G)| $ and posed the above question. The Octahedron is a triangulation with 6 vertices for which every dominating set has size $ \ge 2 $ , so no constant better than $ \frac{1}{3} $ can be achieved in general. However, it appears that one can do better for larger graphs. The most extreme examples here (also from [MT]) are constructed as follows: Start with $ n $ disjoint copies of $ K_4 $ embedded in the plane, and then add edges to complete this graph to a triangulation (with $ 4n $ vertices). Now each of the original copies of $ K_4 $ has an inner vertex which has degree 3 in the final graph, and in order to cover it, one must take at least one vertex from this $ K_4 $ . It follows that every dominating set has size $ \ge n $ . Since the Matheson-Tarjan proof is short and instructive, we sketch it here. In fact, we shall prove (as they did) the stronger statement that every near-triangulation (a graph embedded in the plane with all finite faces of size three) has a (possibly improper) 3-coloring so that each color class is a dominating set and so that the subgraph induced by those vertices incident with the infinite face is properly colored. This stronger fact we prove by induction. If the infinite face is not bounded by a cycle or the infinite face is bounded by a cycle which has a chord, then the graph may be written as the union of two near-triangulations $ G_1,G_2 $ where $ G_1 $ and $ G_2 $ either share one vertex or two adjacent vertices and one edge. In either case, the result follows by applying induction to $ G_1 $ and $ G_2 $ . Otherwise, choose a vertex $ v $ on the infinite face, delete $ v $ and apply induction. Since the neighbors of $ v $ are all on the infinite face, and do not form an independent set, there are at least two colors, say $ 1 $ and $ 2 $ , which appear on the neighbors of $ v $ . Now giving $ v $ the color $ 3 $ gives a solution.

=== References listed by OpenProblemGarden ===
- [MT] L. R. Matheson, R. E. Tarjan, Dominating sets in planar graphs. European J. Combin. 17 (1996), no. 6, 565--568. MathSciNet

=== Catalog page (statement + literature review) ===
Domination in plane triangulations — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Matheson–Tarjan conjecture that every sufficiently large plane triangulation has a dominating set of size at most $n/4$ remains open. The general upper bound has been steadily improved from $n/3$ to $17n/53$ (Špaçapan 2020) and then to $2n/7 \approx 0.286n$ (Christiansen–Rotenberg–Rutschmann 2023), while the full $n/4$ bound has been confirmed for the special case of plane triangulations with maximum degree at most 6 (King–Pelsmajer 2010).

 Cited literature (4)

 
 
 
partial Dominating sets in plane triangulations
 (2010)
 

 
 Erika L. C. King, Michael J. Pelsmajer · Discrete Mathematics · arXiv:0806.2421 · doi:10.1016/j.disc.2010.03.022

Proves the Matheson–Tarjan $n/4$ conjecture for the special case of plane triangulations with maximum degree at most 6.
 

 
 
partial Dominating Plane Triangulations
 (2016)
 

 
 Michael D. Plummer, Dong Ye, Xiaoya Zha · Discrete Applied Mathematics · arXiv:1408.4530

Proves that Hamiltonian plane triangulations with minimum degree at least 4 satisfy $\gamma(G) \le \lfloor 5n/16 \rfloor$ for $n \ge 26$, improving upon the $n/3$ bound for this class.
 

 
 
partial The domination number of plane triangulations
 (2020)
 

 
 Simon Špaçapan · Journal of Combinatorial Theory, Series B · arXiv:1806.06932

Improves the general upper bound on the domination number of plane triangulations from $n/3$ to $17n/53 \approx 0.321n$ for all $n > 6$.
 

 
 
partial Triangulations Admit Dominating Sets of Size $2n/7$
 (2023)
 

 
 Aleksander B. G. Christiansen, Eva Rotenberg, Daniel Rutschmann · arXiv preprint · arXiv:2310.11254

Proves that every plane triangulation on $n > 10$ vertices has a dominating set of size at most $2n/7 \approx 0.286n$, the current best general upper bound, substantially improving upon $17n/53$.
 

 

 Reviewer notes. The King–Pelsmajer arXiv preprint (0806.2421) was submitted June 2008, before the OPG posting date; the Discrete Mathematics journal version appeared in 2010 and is cited here. Search results suggest the Christiansen–Rotenberg–Rutschmann paper may have been published at SODA 2024, but this could not be confirmed via WebFetch (access denied); listed as arXiv preprint. DOIs for Špaçapan (J. Comb. Theory B 143:42–64, 2020) and Plummer–Ye–Zha (Discrete Appl. Math. 211:175–182, 2016) were not retrieved due to paywall restrictions, but their journal venues were confirmed via DBLP.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. Every sufficiently large plane triangulation $ G $ has a dominating set of size $ \le \frac{1}{4} |V(G)| $ .

Keywords:
coloring · domination · multigrid · planar graph · triangulation

Discussion

Motivated by some problems in multigrid computations, Matheson and Tarjan [MT] considered the problem of finding small dominating sets in plane triangulations. They proved that every such graph $ G $ has a dominating set of size $ \le \frac{1}{3} |V(G)| $ and posed the above question. The Octahedron is a triangulation with 6 vertices for which every dominating set has size $ \ge 2 $ , so no constant better than $ \frac{1}{3} $ can be achieved in general. However, it appears that one can do better for larger graphs. The most extreme examples here (also from [MT]) are constructed as follows: Start with $ n $ disjoint copies of $ K_4 $ embedded in the plane, and then add edges to complete this graph to a triangulation (with $ 4n $ vertices). Now each of the original copies of $ K_4 $ has an inner vertex which has degree 3 in the final graph, and in order to cover it, one must take at least one vertex from this $ K_4 $ . It follows that every dominating set has size $ \ge n $ . Since the Matheson-Tarjan proof is short and instructive, we sketch it here. In fact, we shall prove (as they did) the stronger statement that every near-triangulation (a graph embedded in the plane with all finite faces of size three) has a (possibly improper) 3-coloring so that each color class is a dominating set and so that the subgraph induced by those vertices incident with the infinite face is properly colored. This stronger fact we prove by induction. If the infinite face is not bounded by a cycle or the infinite face is bounded by a cycle which has a chord, then the graph may be written as the union of two near-triangulations $ G_1,G_2 $ where $ G_1 $ and $ G_2 $ either share one vertex or two adjacent vertices and one edge. In either case, the result follows by applying induction to $ G_1 $ and $ G_2 $ . Otherwise, choose a vertex $ v $ on the infinite face, delete $ v $ and apply induction. Since the neighbors of $ v $ are all on the infinite face, and do not form an independent set, there are at least two colors, say $ 1 $ and $ 2 $ , which appear on the neighbors of $ v $ . Now giving $ v $ the color $ 3 $ gives a solution.

Bibliography

 [MT]
 L. R. Matheson, R. E. Tarjan, Dominating sets in planar graphs. European J. Combin. 17 (1996), no. 6, 565--568. MathSciNet
 MathSciNet
