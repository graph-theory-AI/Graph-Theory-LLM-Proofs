Attack the following open graph-theory problem.

Catalog id: circular_chromatic_number_of_triangle_free_planar_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/circular_chromatic_number_of_triangle_free_planar_graphs/
Original entry: http://www.openproblemgarden.org/op/circular_chromatic_number_of_triangle_free_planar_graphs
Problem attributed to: Ghebleh, Mohammad, Zhu, Xuding (posted 2007-06-20)

=== Problem statement (OpenProblemGarden) ===
Title: Circular coloring triangle-free subcubic planar graphs
Problem Does every triangle-free planar graph of maximum degree three have circular chromatic number at most $ \frac{20}{7} $ ?

=== Discussion / context (OpenProblemGarden) ===
Throughout, we let $ \chi_c(G) $ denote the circular chromatic number of the graph $ G $ . A well-known Question of Nesetril asks if $ \chi_c(G) \le \frac{5}{2} $ for all cubic graphs $ G $ of sufficiently high girth. A conjecture of Jaeger asserts that $ \chi_c(G) \le 2 + \frac{1}{k} $ for every planar graph $ G $ of girth $ 4k+1 $ . There are numerous partial results on these problems, and there are many interesting questions concerning the circular chromatic numbers of restricted families of graphs. Here we are restricted to planar graphs of girth $ \ge 4 $ with maximum degree $ \le 3 $ . The dodecahedron lives in this class and has $ \chi_c = \frac{20}{7} $ . It remains unclear if anyone else in this class might have $ \chi_c $ larger. A related conjecture of X. Zhu asserts that for every triangle-free planar graph $ G $ with $ \Delta(G)\le 4 $ and $ |V(G)|<3k $ one has $ \chi_c(G)\le 3-1/k $ .

=== Catalog page (statement + literature review) ===
Circular coloring triangle-free subcubic planar graphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem of whether every triangle-free planar graph of maximum degree three satisfies $\chi_c(G) \leq 20/7$ remains open as of all accessible literature. The bound is tight: the dodecahedron belongs to this class and achieves $\chi_c = 20/7$. No proof or counterexample was found in the literature reachable by web search and verified fetch.

 Reviewer notes. Zhu's personal open-problems status page (math.nsysu.edu.tw/~zhu/open-problems/status.htm and chic-k3free-planar.htm) returned TLS certificate errors and could not be fetched; it may contain updates. The OPG page itself was also unreachable (ECONNREFUSED). The paper arXiv:2204.12683 (Dvořák et al., 2022/2025) establishes $\chi_f(G) \leq 11/4$ for subcubic triangle-free graphs (up to two exceptions including the Petersen graph; the dodecahedron likely being a second exception with $\chi_f = \chi_c = 20/7$), but this concerns the fractional chromatic number — a different and weaker parameter since $\chi_f \leq \chi_c$ — and does not resolve the circular coloring question. No arXiv papers combining all three key terms (circular chromatic, triangle-free, planar, subcubic/degree-3) were returned by any search.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 232s.
 

Problem. Does every triangle-free planar graph of maximum degree three have circular chromatic number at most $ \frac{20}{7} $ ?

Keywords:
circular coloring · planar graph · triangle free

Discussion

Throughout, we let $ \chi_c(G) $ denote the circular chromatic number of the graph $ G $ . A well-known Question of Nesetril asks if $ \chi_c(G) \le \frac{5}{2} $ for all cubic graphs $ G $ of sufficiently high girth. A conjecture of Jaeger asserts that $ \chi_c(G) \le 2 + \frac{1}{k} $ for every planar graph $ G $ of girth $ 4k+1 $ . There are numerous partial results on these problems, and there are many interesting questions concerning the circular chromatic numbers of restricted families of graphs. Here we are restricted to planar graphs of girth $ \ge 4 $ with maximum degree $ \le 3 $ . The dodecahedron lives in this class and has $ \chi_c = \frac{20}{7} $ . It remains unclear if anyone else in this class might have $ \chi_c $ larger. A related conjecture of X. Zhu asserts that for every triangle-free planar graph $ G $ with $ \Delta(G)\le 4 $ and $ |V(G)|<3k $ one has $ \chi_c(G)\le 3-1/k $ .
