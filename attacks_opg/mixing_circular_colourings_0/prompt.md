Attack the following open graph-theory problem.

Catalog id: mixing_circular_colourings_0
Source: OpenProblemGarden (importance: Low ✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/mixing_circular_colourings_0/
Original entry: http://www.openproblemgarden.org/op/mixing_circular_colourings_0
Problem attributed to: Brewster, Richard C., Noel, Jonathan A. (posted 2012-09-22)

=== Problem statement (OpenProblemGarden) ===
Title: Mixing Circular Colourings
Question Is $ \mathfrak{M}_c(G) $ always rational?

=== Discussion / context (OpenProblemGarden) ===
Given a proper $ k $ -colouring $ f $ of a graph $ G $ , consider the following 'mixing process:' \item choose a vertex $ v\in V(G) $ ; \item change the colour of $ v $ (if possible) to yield a different $ k $ -colouring $ f' $ of $ G $ . A natural problem arises: Can every $ k $ -colouring of $ G $ be generated from $ f $ by repeatedly applying this process? If so, we say that $ G $ is $ k $ -mixing . The problem of determining if a graph is $ k $ -mixing and several related problems have been studied in a series of recent papers [1,2,4-6]. The authors of [4] provide examples which show that a graph can be $ k $ -mixing but not $ k' $ -mixing for integers $ k' > k $ . For example, given $ m\geq3 $ consider the bipartite graph $ L_m $ which is obtained by deleting a perfect matching from $ K_{m,m} $ . It is an easy exercise to show that for $ L_m $ is $ k $ -mixing if and only if $ k\geq3 $ and $ k\neq m $ . This example motivates the following definition. Definition Define the mixing threshold of $ G $ to be $$\mathfrak{M}(G) := \min\{\ell\in\mathbb{N}: G\text{ is }k\text{-mixing whenever } k\geq\ell\}.$$ An analogous definition can be made for circular colouring. Recall, a $ (k,q) $ -colouring of a graph is a mapping $ f:V(G)\to \{0,1,\dots,k-1\} $ such that if $ uv\in E(G) $ , then $ q\leq |f(u)-f(v)|\leq k-q $ . As with ordinary colourings, we say that a graph $ G $ is $ (k,q) $ -mixing if all $ (k,q) $ -colourings of $ G $ can be generated from a single $ (k,q) $ -colouring $ f $ by recolouring one vertex at a time. Definition Define the circular mixing threshold of $ G $ to be $$\mathfrak{M}_c(G) := \inf\{\ell\in\mathbb{Q}: G\text{ is }(k,q)\text{-mixing whenever } k/q \geq\ell\}.$$ Several bounds on the circular mixing threshold are obtained in [3], including the following which relates the circular mixing threshold to the mixing threshold. Theorem (Brewster and Noel $ [3)</b> $ ] For every graph $ G $ , $$\mathfrak{M}_c(G)\leq\max\left\{\frac{|V(G)|+1}{2}, \mathfrak{M}(G)\right\}.$$ As a corollary, we have the following: if $ |V(G)|\leq 2\mathfrak{M}(G)-1 $ , then $ \mathfrak{M}_c(G)\leq \mathfrak{M}(G) $ . However, examples in [3] show that the ratio $ \mathfrak{M}_c/\mathfrak{M} $ can be arbitrarily large in general. Regarding the problem of determining if $ \mathfrak{M}_c $ is rational, it is worth mentioning that there are no known examples of graphs $ G $ for which $ \mathfrak{M}_c(G) $ is not an integer. Other problems are also given in [3]. One can check that $ \mathfrak{M}_c(K_2) = 2 $ and $ \mathfrak{M}(K_2) = 3 $ . However, the only graphs which are known to satisfy $ \mathfrak{M}_c < \mathfrak{M} $ are in some sense related to $ K_2 $ , eg. trees and complete bipartite graphs. Question Is there a non-bipartite graph $ G $ such that $ \mathfrak{M}_c(G) < \mathfrak{M}(G) $ ? Using an example from [4], it is shown in [3] that if $ m\geq2 $ is an integer, then there is a graph $ G $ such that $ \mathfrak{M}_c(G) = \chi(G) = m $ if and only if $ m\neq 3 $ . A natural question to ask is whether a similar result holds for the circular chromatic number. Again, certain bipartite graphs are an exception. Question Is there a non-bipartite graph $ G $ such that $ \mathfrak{M}_c(G) =\chi_c(G) $ ? Also, the example of $ K_2 $ shows that the circular mixing threshold is, in general, not attained. However, the following problem is open. Question Is the circular mixing threshold always attained for non-bipartite graphs? For more precise versions of the last three questions, see [3].

=== References listed by OpenProblemGarden ===
- [1] P. Bonsma and L. Cereceda. Finding paths between graph colourings: PSPACE-completeness and superpolynomial distances. Theoret. Comput. Sci. 410 (2009), (50): 5215--5226.
- [2] P. Bonsma, L. Cereceda, J. van den Heuvel, and M. Johnson. Finding paths between graph colourings: Computational complexity and possible distances. Electronic Notes in Discrete Mathematics 29 (2007): 463--469.
- *[3] R. C. Brewster and J. A. Noel. Mixing Homomorphisms and Extending Circular Colourings. Submitted. pdf.
- [4] L. Cereceda, J. van den Heuvel, and M. Johnson. Connectedness of the graph of vertex-colourings. Discrete Math. 308 (2008), (5-6): 913--919.
- [5] L. Cereceda, J. van den Heuvel, and M. Johnson. Mixing 3-colourings in bipartite graphs. European J. Combin. 30 (2009), (7): 1593--1606.
- [6] L. Cereceda, J. van den Heuvel, and M. Johnson. Finding paths between 3-colorings. Journal of Graph Theory, 67 (2011), (1): 69--82.
- [7] J. A. Noel. "Jonathan Noel - Mixing Circular Colourings." Webpage.

=== Catalog page (statement + literature review) ===
Mixing Circular Colourings — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The specific question of whether $\mathfrak{M}_c(G)$ is always rational remains open. Since the problem was posted, Brewster, McGuinness, Moore, and Noel (2016) proved a complexity dichotomy for circular colouring reconfiguration (polynomial-time for $p/q < 4$, PSPACE-complete for $p/q \geq 4$), and Brewster and Moore (2022/2023) gave a full characterization of $(p,q)$-mixing for $2 < p/q < 4$ and settled a conjecture of Brewster–Noel that the circular mixing number of bipartite graphs equals $2$; neither result resolves the rationality question.

 Cited literature (2)

 
 
 
partial A Dichotomy Theorem for Circular Colouring Reconfiguration
 (2016)
 

 
 Richard C. Brewster, Sean McGuinness, Benjamin Moore, Jonathan A. Noel · Theoretical Computer Science · arXiv:1508.05573

Establishes a complexity dichotomy: deciding $(p,q)$-mixing is solvable in polynomial time when $p/q < 4$ and is PSPACE-complete when $p/q \geq 4$.
 

 
 
partial Characterizing circular colouring mixing for p/q < 4
 (2022)
 

 
 Richard C. Brewster, Benjamin Moore · Journal of Graph Theory · doi:10.1002/jgt.22870

Gives a full graph-theoretic characterization of $(p,q)$-mixing for $2 < p/q < 4$ in terms of cycle winds, proves $(2k+1,k)$-mixing is co-NP-complete for all $k$, and settles the Brewster–Noel conjecture that the circular mixing number of bipartite graphs equals $2$.
 

 

 Reviewer notes. The Wiley Online Library and ResearchGate pages returned HTTP 403; the Brewster–Moore 2023 paper was verified via colab.ws only. Jonathan Noel's personal open-problems page (jonathannoel.ca/openprobs) returned 404. The rationality question is not mentioned as resolved in any source found; all evidence suggests it remains open. The foundational Brewster–Noel paper (arXiv:1412.3493, JGT 2015) was already cited as [3] in the OPG discussion and is not listed as new since_posted progress.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Question. Is $ \mathfrak{M}_c(G) $ always rational?

Keywords:
discrete homotopy · graph colourings · mixing

Discussion

Given a proper $ k $ -colouring $ f $ of a graph $ G $ , consider the following 'mixing process:' \item choose a vertex $ v\in V(G) $ ; \item change the colour of $ v $ (if possible) to yield a different $ k $ -colouring $ f' $ of $ G $ . A natural problem arises: Can every $ k $ -colouring of $ G $ be generated from $ f $ by repeatedly applying this process? If so, we say that $ G $ is $ k $ -mixing . The problem of determining if a graph is $ k $ -mixing and several related problems have been studied in a series of recent papers [1,2,4-6]. The authors of [4] provide examples which show that a graph can be $ k $ -mixing but not $ k' $ -mixing for integers $ k' > k $ . For example, given $ m\geq3 $ consider the bipartite graph $ L_m $ which is obtained by deleting a perfect matching from $ K_{m,m} $ . It is an easy exercise to show that for $ L_m $ is $ k $ -mixing if and only if $ k\geq3 $ and $ k\neq m $ . This example motivates the following definition. Definition Define the mixing threshold of $ G $ to be $$\mathfrak{M}(G) := \min\{\ell\in\mathbb{N}: G\text{ is }k\text{-mixing whenever } k\geq\ell\}.$$ An analogous definition can be made for circular colouring. Recall, a $ (k,q) $ -colouring of a graph is a mapping $ f:V(G)\to \{0,1,\dots,k-1\} $ such that if $ uv\in E(G) $ , then $ q\leq |f(u)-f(v)|\leq k-q $ . As with ordinary colourings, we say that a graph $ G $ is $ (k,q) $ -mixing if all $ (k,q) $ -colourings of $ G $ can be generated from a single $ (k,q) $ -colouring $ f $ by recolouring one vertex at a time. Definition Define the circular mixing threshold of $ G $ to be $$\mathfrak{M}_c(G) := \inf\{\ell\in\mathbb{Q}: G\text{ is }(k,q)\text{-mixing whenever } k/q \geq\ell\}.$$ Several bounds on the circular mixing threshold are obtained in [3], including the following which relates the circular mixing threshold to the mixing threshold. Theorem (Brewster and Noel $ [3)</b> $ ] For every graph $ G $ , $$\mathfrak{M}_c(G)\leq\max\left\{\frac{|V(G)|+1}{2}, \mathfrak{M}(G)\right\}.$$ As a corollary, we have the following: if $ |V(G)|\leq 2\mathfrak{M}(G)-1 $ , then $ \mathfrak{M}_c(G)\leq \mathfrak{M}(G) $ . However, examples in [3] show that the ratio $ \mathfrak{M}_c/\mathfrak{M} $ can be arbitrarily large in general. Regarding the problem of determining if $ \mathfrak{M}_c $ is rational, it is worth mentioning that there are no known examples of graphs $ G $ for which $ \mathfrak{M}_c(G) $ is not an integer. Other problems are also given in [3]. One can check that $ \mathfrak{M}_c(K_2) = 2 $ and $ \mathfrak{M}(K_2) = 3 $ . However, the only graphs which are known to satisfy $ \mathfrak{M}_c < \mathfrak{M} $ are in some sense related to $ K_2 $ , eg. trees and complete bipartite graphs. Question Is there a non-bipartite graph $ G $ such that $ \mathfrak{M}_c(G) < \mathfrak{M}(G) $ ? Using an example from [4], it is shown in [3] that if $ m\geq2 $ is an integer, then there is a graph $ G $ such that $ \mathfrak{M}_c(G) = \chi(G) = m $ if and only if $ m\neq 3 $ . A natural question to ask is whether a similar result holds for the circular chromatic number. Again, certain bipartite graphs are an exception. Question Is there a non-bipartite graph $ G $ such that $ \mathfrak{M}_c(G) =\chi_c(G) $ ? Also, the example of $ K_2 $ shows that the circular mixing threshold is, in general, not attained. However, the following problem is open. Question Is the circular mixing threshold always attained for non-bipartite graphs? For more precise versions of the last three questions, see [3].

Bibliography

 [1]
 P. Bonsma and L. Cereceda. Finding paths between graph colourings: PSPACE-completeness and superpolynomial distances. Theoret. Comput. Sci. 410 (2009), (50): 5215--5226.

 [2]
 P. Bonsma, L. Cereceda, J. van den Heuvel, and M. Johnson. Finding paths between graph colourings: Computational complexity and possible distances. Electronic Notes in Discrete Mathematics 29 (2007): 463--469.

★ [3]
 R. C. Brewster and J. A. Noel. Mixing Homomorphisms and Extending Circular Colourings. Submitted. pdf .
 pdf

 [4]
 L. Cereceda, J. van den Heuvel, and M. Johnson. Connectedness of the graph of vertex-colourings . Discrete Math. 308 (2008), (5-6): 913--919.
 Connectedness of the graph of vertex-colourings

 [5]
 L. Cereceda, J. van den Heuvel, and M. Johnson. Mixing 3-colourings in bipartite graphs. European J. Combin. 30 (2009), (7): 1593--1606.

 [6]
 L. Cereceda, J. van den Heuvel, and M. Johnson. Finding paths between 3-colorings. Journal of Graph Theory, 67 (2011), (1): 69--82.

 [7]
 J. A. Noel. "Jonathan Noel - Mixing Circular Colourings." Webpage .
 Webpage
