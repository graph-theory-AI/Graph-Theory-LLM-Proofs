Attack the following open graph-theory problem.

Catalog id: laplacian_degrees_of_a_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Algebraic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/laplacian_degrees_of_a_graph/
Original entry: http://www.openproblemgarden.org/op/laplacian_degrees_of_a_graph
Problem attributed to: Guo, Ji-Ming (posted 2007-06-22)

=== Problem statement (OpenProblemGarden) ===
Title: Laplacian Degrees of a Graph
Conjecture If $ G $ is a connected graph on $ n $ vertices, then $ c_k(G) \ge d_k(G) $ for $ k = 1, 2, \dots, n-1 $ .

=== Discussion / context (OpenProblemGarden) ===
(Reproduced from [M].) Let $ L = D - A $ be the Laplacian matrix of a graph $ G $ of order $ n $ . Let $ t_k $ be the $ k $ -th largest eigenvalue of $ L $ ( $ k = 1,\dots,n $ ). For the purpose of this problem, we call the number $$ c_k = c_k(G) = t_k + k - 2 $$ the $ k $ -th Laplacian degree of $ G $ . In addition to that, let $ d_k(G) $ be the $ k $ -th largest (usual) degree in $ G $ . It is known that every connected graph satisfies $ c_k(G) \ge d_k(G) $ for $ k = 1 $ [GM], $ k = 2 $ [LP] and for $ k = 3 $ [G].

=== References listed by OpenProblemGarden ===
- [GM] R. Grone, R. Merris, The Laplacian spectrum of a graph II, SIAM J. Discrete Math.7 (1994) 221-229. MathSciNet
- [LP] J.S. Li, Y.L. Pan, A note on the second largest eigenvalue of the Laplacian matrix of a graph, Linear Multilin. Algebra 48 (2000) 117-121. MathSciNet
- *[G] J.-M. Guo, On the third largest Laplacian eigenvalue of a graph, Linear Multilin. Algebra 55 (2007) 93-102. MathSciNet
- [M] B. Mohar, Problem of the Month

=== Catalog page (statement + literature review) ===
Laplacian Degrees of a Graph — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 The conjecture was fully proved by Brouwer and Haemers in 2008. They showed that for any connected graph on $n$ vertices, the $j$-th largest Laplacian eigenvalue $\mu_j$ satisfies $\mu_j \geq d_j - j + 2$ for $j = 1, \ldots, n-1$, which is exactly the statement $c_k(G) \geq d_k(G)$ in the problem's notation.

 Cited literature (1)

 
 
 
proof A Lower Bound for the Laplacian Eigenvalues of a Graph-Proof of a Conjecture by Guo
 (2008)
 

 
 Andries E. Brouwer, Willem H. Haemers · Linear Algebra and its Applications · doi:10.1016/j.laa.2008.06.008

Proves that the $j$-th largest Laplacian eigenvalue $\mu_j \geq d_j - j + 2$ for $j = 1, \ldots, n-1$ in any connected graph, fully resolving Guo's conjecture.
 

 

 Reviewer notes. The ScienceDirect and SSRN pages for the Brouwer-Haemers paper returned HTTP 403; verification was completed via the Tilburg University institutional repository. The DOI 10.1016/j.laa.2008.06.008 was confirmed to resolve to pii/S002437950800311X (Linear Algebra and its Applications). No arXiv preprint was found for this paper.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. If $ G $ is a connected graph on $ n $ vertices, then $ c_k(G) \ge d_k(G) $ for $ k = 1, 2, \dots, n-1 $ .

Keywords:
degree sequence · Laplacian matrix

Discussion

(Reproduced from [M].) Let $ L = D - A $ be the Laplacian matrix of a graph $ G $ of order $ n $ . Let $ t_k $ be the $ k $ -th largest eigenvalue of $ L $ ( $ k = 1,\dots,n $ ). For the purpose of this problem, we call the number $$ c_k = c_k(G) = t_k + k - 2 $$ the $ k $ -th Laplacian degree of $ G $ . In addition to that, let $ d_k(G) $ be the $ k $ -th largest (usual) degree in $ G $ . It is known that every connected graph satisfies $ c_k(G) \ge d_k(G) $ for $ k = 1 $ [GM], $ k = 2 $ [LP] and for $ k = 3 $ [G].

Bibliography

 [GM]
 R. Grone, R. Merris, The Laplacian spectrum of a graph II, SIAM J. Discrete Math.7 (1994) 221-229. MathSciNet
 MathSciNet

 [LP]
 J.S. Li, Y.L. Pan, A note on the second largest eigenvalue of the Laplacian matrix of a graph, Linear Multilin. Algebra 48 (2000) 117-121. MathSciNet
 MathSciNet

★ [G]
 J.-M. Guo, On the third largest Laplacian eigenvalue of a graph, Linear Multilin. Algebra 55 (2007) 93-102. MathSciNet
 MathSciNet

 [M]
 B. Mohar, Problem of the Month
 Problem of the Month
