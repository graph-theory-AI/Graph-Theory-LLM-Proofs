Attack the following open graph-theory problem.

Catalog id: non_edges_vs_feedback_edge_sets_in_digraphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/non_edges_vs_feedback_edge_sets_in_digraphs/
Original entry: http://www.openproblemgarden.org/op/non_edges_vs_feedback_edge_sets_in_digraphs
Problem attributed to: Chudnovsky, Maria, Seymour, Paul D., Sullivan, Blair (posted 2008-07-08)

=== Problem statement (OpenProblemGarden) ===
Title: Non-edges vs. feedback edge sets in digraphs
For any simple digraph $ G $ , we let $ \gamma(G) $ be the number of unordered pairs of nonadjacent vertices (i.e. the number of non-edges), and $ \beta(G) $ be the size of the smallest feedback edge set . Conjecture If $ G $ is a simple digraph without directed cycles of length $ \le 3 $ , then $ \beta(G) \le \frac{1}{2} \gamma(G) $ .

=== Discussion / context (OpenProblemGarden) ===
If $ G $ satisfies $ \gamma(G) = 0 $ , then $ G $ is a tournament, and it is easy to check that $ G $ will have a directed cycle of length three unless it is acyclic, in which case $ \beta(G) = 0 $ . So in this case, the conjecture holds. More generally, it is natural to suspect that a digraph with few non-edges and no directed triangles should be close to acyclic. Indeed, this conjecture asserts a precise relationship of this form. If true, the above conjecture is essentially tight for a number of examples. We noted above that it is tight for transitive tournaments. Here is another basic class: let $ G_k $ be the circulant digraph obtained by placing $ 3k+1 $ vertices in a circle, and adding an edge directed from $ u $ to $ v $ whenever $ v $ is distance $ \le k $ from $ u $ in the clockwise order. Such examples may be nested to obtain new ones. Chudnovsky, Seymour, and Sullivan [CSS] utilized a clever double counting argument to prove that $ \beta(G) \le \gamma(G) $ always holds. They also proved their conjecture in the case when $ V(G) $ is the union of two cliques, and when $ G $ is a circular interval digraph.

=== References listed by OpenProblemGarden ===
- *[CSS] M. Chudnovsky, P.D. Seymour, and B. Sullivan, Cycles in dense digraphs.

=== Catalog page (statement + literature review) ===
Non-edges vs. feedback edge sets in digraphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture $\beta(G) \le \frac{1}{2}\gamma(G)$ for simple digraphs with no directed cycles of length $\le 3$ remains open. The best known general bound is $\beta(G) \le 0.8616\,\gamma(G)$, proved by Chen, Karson, Liu, and Shen, improving an earlier bound of $0.88\gamma(G)$ due to Dunkum, Hamburger, and Pór. Fox, Keevash, and Sudakov proved the more general result that digraphs with directed girth $\ge r \ge 4$ satisfy $\beta(G) \le c\,\gamma(G)/r^2$ for an absolute constant $c$.

 Cited literature (2)

 
 
 
partial On the Chudnovsky-Seymour-Sullivan conjecture on cycles in triangle-free digraphs
 (2015)
 

 
 Kevin Chen, Sean Karson, Dan Liu, Jian Shen · Electronic Journal of Linear Algebra · arXiv:0909.2468

Proves $\beta(G) \le 0.8616\,\gamma(G)$ for digraphs without directed triangles or digons, improving the prior best bound of $0.88\gamma(G)$ by Dunkum, Hamburger, and Pór.
 

 
 
partial Directed Graphs Without Short Cycles
 (2010)
 

 
 Jacob Fox, Peter Keevash, Benny Sudakov · Combinatorics, Probability and Computing

Proves that digraphs with directed girth $\ge r \ge 4$ satisfy $\beta(G) \le c\,\gamma(G)/r^2$ for an absolute constant $c$, tight up to the constant factor; for the CSS setting ($r=4$) this gives a weaker constant than 0.8616.
 

 

 Reviewer notes. The Dunkum-Hamburger-Pór 0.88 bound is cited as prior work in the Chen et al. arXiv preprint but no verifiable online source for that paper was found; it is therefore not listed in since_posted. No post-2015 verified paper was found that further improves the constant or resolves the conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. If $ G $ is a simple digraph without directed cycles of length $ \le 3 $ , then $ \beta(G) \le \frac{1}{2} \gamma(G) $ .

Keywords:
acyclic · digraph · feedback edge set · triangle free

Discussion

If $ G $ satisfies $ \gamma(G) = 0 $ , then $ G $ is a tournament, and it is easy to check that $ G $ will have a directed cycle of length three unless it is acyclic, in which case $ \beta(G) = 0 $ . So in this case, the conjecture holds. More generally, it is natural to suspect that a digraph with few non-edges and no directed triangles should be close to acyclic. Indeed, this conjecture asserts a precise relationship of this form. If true, the above conjecture is essentially tight for a number of examples. We noted above that it is tight for transitive tournaments. Here is another basic class: let $ G_k $ be the circulant digraph obtained by placing $ 3k+1 $ vertices in a circle, and adding an edge directed from $ u $ to $ v $ whenever $ v $ is distance $ \le k $ from $ u $ in the clockwise order. Such examples may be nested to obtain new ones. Chudnovsky, Seymour, and Sullivan [CSS] utilized a clever double counting argument to prove that $ \beta(G) \le \gamma(G) $ always holds. They also proved their conjecture in the case when $ V(G) $ is the union of two cliques, and when $ G $ is a circular interval digraph.

Bibliography

★ [CSS]
 M. Chudnovsky, P.D. Seymour, and B. Sullivan, Cycles in dense digraphs .
 Cycles in dense digraphs
