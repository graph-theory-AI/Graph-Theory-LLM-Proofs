Attack the following open graph-theory problem.

Catalog id: does_the_symmetric_chromatic_function_distinguish_trees
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Algebraic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/does_the_symmetric_chromatic_function_distinguish_trees/
Original entry: http://www.openproblemgarden.org/op/does_the_symmetric_chromatic_function_distinguish_trees
Problem attributed to: Stanley, Richard P. (posted 2009-02-25)

=== Problem statement (OpenProblemGarden) ===
Title: Does the chromatic symmetric function distinguish between trees?
Problem Do there exist non-isomorphic trees which have the same chromatic symmetric function?

=== Discussion / context (OpenProblemGarden) ===
Stanley [S] introduced the following symmetric function associated with a graph. Let $ x_1,x_2,\ldots $ be commuting indeterminates, and for every graph $ G=(V,E) $ let $ {\mathcal C}_G $ be the set of all proper colorings $ f: V \rightarrow {\mathbb N} $ . Then the chromatic symmetric function is defined to be \[ X_G = \sum_{f \in {\mathcal C}_G} \prod_{v \in V} x_{f(v)}. \] So, the coefficient of a term $ x_1^{d_1} x_2^{d_2} \ldots $ in $ X_G $ is precisely the number of proper colorings of $ G $ where color $ i $ appears exactly $ d_i $ times. It is immediate that $ X_G $ is homogeneous of degree $ |V| $ and is symmetric. If we set $ x_1,x_2,\ldots,x_k = 1 $ and $ x_{k+1}, x_{k+2} \ldots = 0 $ and evaluate, we get the number of proper colorings of $ G $ using the colors $ 1,2,\ldots,k $ . Therefore, the chromatic symmetric function contains all of the information of the chromatic polynomial. In fact, the chromatic symmetric function contains strictly more information about the graph, since there exist examples of graphs which have distinct chromatic symmetric functions but have the same chromatic polynomial. This natural problem of Stanley remains wide open. It has recently been established for some special classes of trees, namely caterpillars and spiders [MMW].

=== References listed by OpenProblemGarden ===
- [MMW] J. Martin, M. Morin, and J. D. Wagner, On distinguishing trees by their chromatic symmetric functions. J. Combin. Theory Ser. A 115 (2008), no. 2, 237–253. MathSciNet
- *[S] R. P. Stanley, A symmetric function generalization of the chromatic polynomial of a graph, Advances in Math. 111 (1995), 166–194.

=== Catalog page (statement + literature review) ===
Does the chromatic symmetric function distinguish between trees? — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Stanley's 2009 conjecture that non-isomorphic trees have distinct chromatic symmetric functions remains open in general. Substantial partial progress has been made: the conjecture is now established for caterpillars, spiders, 2-spiders, trees of diameter less than 5, and trees with exactly two vertices of degree $\geq 3$, and has been verified computationally for all trees on up to 29 vertices. The chromatic symmetric function is also known to determine each tree's generalized degree sequence (Crew's conjecture, now proved), but no two non-isomorphic trees sharing the same chromatic symmetric function have been found.

 Cited literature (5)

 
 
 
partial On an Algorithm for Comparing the Chromatic Symmetric Functions of Trees
 (2018)
 

 
 Sam Heil, Caleb Ji · arXiv preprint · arXiv:1801.07363

Presents a probabilistic algorithm and extends the computational verification of Stanley's conjecture to all trees on up to 29 vertices.
 

 
 
partial A Few More Trees the Chromatic Symmetric Function Can Distinguish
 (2020)
 

 
 Jake Huryn · Involve, a Journal of Mathematics · arXiv:1901.04034

Introduces n-spiders (generalising classical spiders) and proves Stanley's conjecture for the class of 2-spiders.
 

 
 
partial Quasisymmetric functions distinguishing trees
 (2022)
 

 
 Jean-Christophe Aval, Karimatou Djenabou, Peter R. W. McNamara · arXiv preprint · arXiv:2201.11763

Proves that the chromatic quasisymmetric function distinguishes rooted trees, and conjectures the same for directed trees.
 

 
 
partial A class of trees determined by their chromatic symmetric functions
 (2023)
 

 
 Yuzhenni Wang, Xingxing Yu, Xiao-Dong Zhang · arXiv preprint · arXiv:2308.03980

Proves Stanley's conjecture for trees with exactly two vertices of degree at least 3, using differentiation with respect to power-sum symmetric functions.
 

 
 
partial Chromatic symmetric functions and polynomial invariants of trees
 (2024)
 

 
 José Aliste-Prieto, Jeremy L. Martin, Jennifer D. Wagner, José Zamora · Bulletin of the London Mathematical Society · arXiv:2402.10333 · doi:10.1112/blms.13144

Proves Crew's conjecture that the chromatic symmetric function of a tree determines its generalized degree sequence, and establishes connections to the subtree polynomial.
 

 

 Reviewer notes. The 2021 Discrete Mathematics paper 'A note on distinguishing trees with the chromatic symmetric function' (ScienceDirect pii/S0012365X21003952) returned HTTP 403 and could not be verified; it is therefore omitted. A 2025 arXiv paper (2507.15986) titled 'On the reconstruction of trees from their chromatic symmetric functions' appeared in search results but was not fetched and is not cited. The e-positivity/Schur-positivity threads (counterexample by Shareshian-Wachs, Li 2025) are related but orthogonal to the isomorphism question.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Problem. Do there exist non-isomorphic trees which have the same chromatic symmetric function?

Keywords:
chromatic polynomial · symmetric function · tree

Discussion

Stanley [S] introduced the following symmetric function associated with a graph. Let $ x_1,x_2,\ldots $ be commuting indeterminates, and for every graph $ G=(V,E) $ let $ {\mathcal C}_G $ be the set of all proper colorings $ f: V \rightarrow {\mathbb N} $ . Then the chromatic symmetric function is defined to be \[ X_G = \sum_{f \in {\mathcal C}_G} \prod_{v \in V} x_{f(v)}. \] So, the coefficient of a term $ x_1^{d_1} x_2^{d_2} \ldots $ in $ X_G $ is precisely the number of proper colorings of $ G $ where color $ i $ appears exactly $ d_i $ times. It is immediate that $ X_G $ is homogeneous of degree $ |V| $ and is symmetric. If we set $ x_1,x_2,\ldots,x_k = 1 $ and $ x_{k+1}, x_{k+2} \ldots = 0 $ and evaluate, we get the number of proper colorings of $ G $ using the colors $ 1,2,\ldots,k $ . Therefore, the chromatic symmetric function contains all of the information of the chromatic polynomial. In fact, the chromatic symmetric function contains strictly more information about the graph, since there exist examples of graphs which have distinct chromatic symmetric functions but have the same chromatic polynomial. This natural problem of Stanley remains wide open. It has recently been established for some special classes of trees, namely caterpillars and spiders [MMW].

Bibliography

 [MMW]
 J. Martin, M. Morin, and J. D. Wagner, On distinguishing trees by their chromatic symmetric functions. J. Combin. Theory Ser. A 115 (2008), no. 2, 237–253. MathSciNet
 MathSciNet

★ [S]
 R. P. Stanley, A symmetric function generalization of the chromatic polynomial of a graph, Advances in Math. 111 (1995), 166–194.
