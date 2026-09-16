Attack the following open graph-theory problem.

Catalog id: list_colourings_of_complete_multipartite_graphs_with_2_big_parts
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_colourings_of_complete_multipartite_graphs_with_2_big_parts/
Original entry: http://www.openproblemgarden.org/op/list_colourings_of_complete_multipartite_graphs_with_2_big_parts
Problem attributed to: Allagan, Julian (posted 2014-04-12)

=== Problem statement (OpenProblemGarden) ===
Title: List Colourings of Complete Multipartite Graphs with 2 Big Parts
Question Given $ a,b\geq2 $ , what is the smallest integer $ t\geq0 $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ ?

=== Discussion / context (OpenProblemGarden) ===
The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is the minimum $ k $ such that for every assignment of lists of size $ k $ to the vertices of $ G $ there is a proper colouring in which every vertex is mapped to a colour in its own list. For more background on the list chromatic number, see [3]. Given graphs $ G $ and $ H $ , the join of $ G $ and $ H $ , denoted $ G+H $ , is obtained by taking disjoint copies of $ G $ and $ H $ and adding all edges between them. Ohba [1] proved that for every graph $ G $ there exists $ t\geq0 $ such that $ \chi_\ell(G+K_t)= \chi(G+K_t) $ . The question above asks to determine the minimum value of $ t $ in the case that $ G $ is a complete bipartite graph. It seems that it was first studied in [4], although this is unclear; for the time being, we have chosen to attribute this problem to J. Allagan. Define $ \phi(a,b) $ to be the minimum $ t $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ . Note that, if $ G $ is a complete multipartite graph with at most one non-singleton part, then we see that $ \chi_\ell(G)=\chi(G) $ by colouring the vertices of the non-singleton part last. Thus, if $ a $ or $ b $ is equal to 1, then $ \phi(a,b)=0 $ . As it turns out, $ \phi(2,2)=\phi(2,3)=0 $ and $ \phi(3,3)=\phi(2,4)=1 $ . This can be deduced from the following result of [2] and the fact that $ \chi_\ell(K_{3,3})=\chi_\ell(K_{4,2})=3 $ : Theorem (Noel, Reed, Wu (2012)) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \chi_\ell(G)=\chi(G) $ . The above result of [2] implies that if $ a+b\geq 5 $ , then $ \phi(a,b)\leq a+b-5 $ . However it seems that, for most values of $ a,b $ , this bound is far from tight. A simple observation is that, since $ \chi_\ell(K_{a,b}+K_t)\geq \chi_\ell(K_{a,b}) $ for all $ t $ , we must have \[\phi(a,b)\geq \chi_\ell(K_{a,b}) - \chi(K_{a,b}) = \chi_\ell(K_{a,b}) -2.\] The following is a result of Allagan [4]: Theorem (Allagan (2009)) If $ a\geq5 $ , then \[\lfloor \sqrt{a}\rfloor - 1 \leq \phi(a,2)\leq \left\lceil\frac{-7+\sqrt{8a+17}}{2}\right\rceil.\] This implies that $ \phi(a,2)=1 $ for $ 4\leq a\leq 8 $ and that $ \phi(a,2)=2 $ for $ 9\leq a\leq 13 $ .

=== References listed by OpenProblemGarden ===
- [1] K. Ohba. On chromatic-choosable graphs, J. Graph Theory. 40 (2002) 130--135. MathSciNet.
- [2] J. A. Noel, B. A. Reed, H. Wu. A Proof of a Conjecture of Ohba. Submitted. pdf.
- [3] J. A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond. Master's Thesis, McGill University. pdf.
- [4] J. A. D. Allagan. Choice Numbers, Ohba Numbers and Hall Numbers of some complete -partite graphs. PhD Thesis. Auburn University. 2009.

=== Catalog page (statement + literature review) ===
List Colourings of Complete Multipartite Graphs with 2 Big Parts — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The case $a = 2$ (equivalently $b = 2$) of the problem has been fully resolved: Cano, Gutknecht, Kappaganthula, Miller, Mudrock, and Thornburgh (2024) proved that $\tau_0(2,b) = \lfloor\sqrt{b}\rfloor - 1$ for all $b \geq 2$, improving Allagan's 2009 bounds and confirming his conjectured lower bound as exact. For general $a, b \geq 2$ the exact value of $\phi(a,b)$ remains open, with only the asymptotic lower bound $\tau_0(a,b) = \Omega(\sqrt{b})$ as $b\to\infty$ established.

 Cited literature (1)

 
 
 
partial On the Ohba Number and Generalized Ohba Numbers of Complete Bipartite Graphs
 (2024)
 

 
 Kennedy Cano, Emily Gutknecht, Gautham Kappaganthula, George Miller, Jeffrey A. Mudrock, Ezekiel Thornburgh · arXiv preprint · arXiv:2403.06291

Proves $\tau_0(2,b) = \lfloor\sqrt{b}\rfloor - 1$ for all $b\geq 2$ (settling the $K_{2,b}$ case of the problem exactly) and shows $\tau_0(a,b)=\Omega(\sqrt{b})$ for general $a\geq 2$.
 

 

 Reviewer notes. The 2024 paper uses the notation tau_0(a,b) for the same quantity as the OPG's phi(a,b). The paper had a latest revision dated February 2026 and may be under journal review. The Noel-Reed-Wu paper (reference [2] in OPG) was published in J. Graph Theory in 2015 (DOI 10.1002/jgt.21819), confirming Ohba's conjecture, but the journal page returned HTTP 403 so it was not verifiable via WebFetch. No paper was found that fully determines phi(a,b) for all a,b >= 2.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Question. Given $ a,b\geq2 $ , what is the smallest integer $ t\geq0 $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ ?

Keywords:
complete bipartite graph · complete multipartite graph · list coloring

Discussion

The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is the minimum $ k $ such that for every assignment of lists of size $ k $ to the vertices of $ G $ there is a proper colouring in which every vertex is mapped to a colour in its own list. For more background on the list chromatic number, see [3]. Given graphs $ G $ and $ H $ , the join of $ G $ and $ H $ , denoted $ G+H $ , is obtained by taking disjoint copies of $ G $ and $ H $ and adding all edges between them. Ohba [1] proved that for every graph $ G $ there exists $ t\geq0 $ such that $ \chi_\ell(G+K_t)= \chi(G+K_t) $ . The question above asks to determine the minimum value of $ t $ in the case that $ G $ is a complete bipartite graph. It seems that it was first studied in [4], although this is unclear; for the time being, we have chosen to attribute this problem to J. Allagan. Define $ \phi(a,b) $ to be the minimum $ t $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ . Note that, if $ G $ is a complete multipartite graph with at most one non-singleton part, then we see that $ \chi_\ell(G)=\chi(G) $ by colouring the vertices of the non-singleton part last. Thus, if $ a $ or $ b $ is equal to 1, then $ \phi(a,b)=0 $ . As it turns out, $ \phi(2,2)=\phi(2,3)=0 $ and $ \phi(3,3)=\phi(2,4)=1 $ . This can be deduced from the following result of [2] and the fact that $ \chi_\ell(K_{3,3})=\chi_\ell(K_{4,2})=3 $ : Theorem (Noel, Reed, Wu (2012)) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \chi_\ell(G)=\chi(G) $ . The above result of [2] implies that if $ a+b\geq 5 $ , then $ \phi(a,b)\leq a+b-5 $ . However it seems that, for most values of $ a,b $ , this bound is far from tight. A simple observation is that, since $ \chi_\ell(K_{a,b}+K_t)\geq \chi_\ell(K_{a,b}) $ for all $ t $ , we must have \[\phi(a,b)\geq \chi_\ell(K_{a,b}) - \chi(K_{a,b}) = \chi_\ell(K_{a,b}) -2.\] The following is a result of Allagan [4]: Theorem (Allagan (2009)) If $ a\geq5 $ , then \[\lfloor \sqrt{a}\rfloor - 1 \leq \phi(a,2)\leq \left\lceil\frac{-7+\sqrt{8a+17}}{2}\right\rceil.\] This implies that $ \phi(a,2)=1 $ for $ 4\leq a\leq 8 $ and that $ \phi(a,2)=2 $ for $ 9\leq a\leq 13 $ .

Bibliography

 [1]
 K. Ohba. On chromatic-choosable graphs, J. Graph Theory. 40 (2002) 130--135. MathSciNet .
 MathSciNet

 [2]
 J. A. Noel, B. A. Reed, H. Wu. A Proof of a Conjecture of Ohba. Submitted. pdf .
 pdf

 [3]
 J. A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond. Master's Thesis, McGill University. pdf .
 pdf

 [4]
 J. A. D. Allagan. Choice Numbers, Ohba Numbers and Hall Numbers of some complete $ k $ -partite graphs. PhD Thesis. Auburn University. 2009.
