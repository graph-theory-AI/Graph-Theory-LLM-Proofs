Attack the following open graph-theory problem.

Catalog id: counting_3_colorings_of_the_hex_lattice
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/counting_3_colorings_of_the_hex_lattice/
Original entry: http://www.openproblemgarden.org/op/counting_3_colorings_of_the_hex_lattice
Problem attributed to: Thomassen, Carsten (posted 2008-07-05)

=== Problem statement (OpenProblemGarden) ===
Title: Counting 3-colorings of the hex lattice
Problem Find $ \lim_{n \rightarrow \infty} (\chi( H_n , 3)) ^{ 1 / |V(H_n)| } $ .

=== Discussion / context (OpenProblemGarden) ===
We'll begin by putting in place the necessary notation. Let $ {\mathcal T} $ be the regular triangular tiling of the plane. For every $ n \ge 1 $ there is a regular map which triangulates the torus, denoted $ T_n $ , which may be obtained from a regular hexagonal piece of $ {\mathcal T} $ of side-length $ n $ by identifying points on opposite edges of this hexagon. Let $ H_n $ be the dual of $ T_n $ (on the torus). Then $ H_n $ is a regular map on the torus - a hexagonal tiling. One last definition: for any graph $ G $ and any positive integer $ k $ we let $ \chi(G,k) $ denote the number of proper $ k $ -coloring of $ G $ . A famous theorem of Lieb [L] shows that $ \lim_{n \rightarrow \infty} (\chi(Q_n,3))^{1 / |V(Q_n)|} = (\frac{4}{3})^{3/2} $ where $ Q_n $ denotes the $ n \times n $ quadrangulation of the torus. This theorem is usually stated in terms of Eulerian orientations, and is of interest to physicists as the constant $ (\frac{4}{3})^{3/2} $ (called Lieb's Ice Constant) determines the "residual entropy for square ice". Thomassen proved that every planar graph $ G $ with girth $ \ge 5 $ has exponentially many proper 3-colorings. More precisely, he showed that $ (\chi(G,3))^{ 1 / |V(G)| } \ge 2 ^{1 / 10000} $ . This gives a lower bound on the limit in the above problem (assuming it exists).

=== References listed by OpenProblemGarden ===
- [L] E. H. Lieb, Exact Solution of the Problem of the Entropy of Two-Dimensional Ice. Phys. Rev. Lett. 18, 692-694, 1967.

=== Catalog page (statement + literature review) ===
Counting 3-colorings of the hex lattice — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem asks for the exact value of $\lim_{n\to\infty}(\chi(H_n,3))^{1/|V(H_n)|}$ for proper vertex 3-colorings of the hexagonal tiling $H_n$ of the torus, the analogue of Lieb's ice-constant theorem for the square lattice. No post-2008 rigorous mathematical proof establishing the existence or value of this limit has been found; the physics literature contains closely related entropy calculations (Baxter 1970 for bond/edge colorings of the hexagonal lattice, giving $W\approx 1.2087$), but the vertex-coloring version appears to remain open as a mathematical theorem. A 2016 physics paper by Cépas studies structural properties of these vertex colorings (even/odd chirality classes), confirming equal entropy for the two classes but not proving the per-site limit.

 Cited literature (1)

 
 
 
partial Colorings of odd or even chirality on hexagonal lattices
 (2017)
 

 
 O. Cépas · Physical Review B · arXiv:1611.02925

Shows that even and odd chirality classes of vertex 3-colorings of the hexagonal lattice have the same entropy in the thermodynamic limit, and introduces an ergodic Monte Carlo algorithm for sampling them; does not prove the per-site limit asked by the problem.
 

 

 Reviewer notes. Baxter's 1970 paper 'Colorings of a Hexagonal Lattice' (J. Math. Phys. 11:784) is behind a paywall and could not be fully verified; search results indicate it computes entropy for bond (edge) 3-colorings of the hexagonal lattice (W≈1.2087 = √3·Γ(1/3)^{3/2}/(2π)), which is a different problem from the vertex 3-colorings asked here. The OPG problem formulation explicitly presents the hexagonal case as open (in contrast to Lieb's proved square-lattice result), suggesting no pre-2008 rigorous mathematical proof existed for vertex colorings. The paper arXiv:0805.0669 (submitted May 2008) studies functional equations for the three-coloring statistical model with domain wall boundary conditions, extending Baxter's toroidal calculation, but without explicit chromatic-polynomial asymptotics. No post-2008 paper proving the limit was found in four search passes.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Problem. Find $ \lim_{n \rightarrow \infty} (\chi( H_n , 3)) ^{ 1 / |V(H_n)| } $ .

Keywords:
coloring · Lieb's Ice Constant · tiling · torus

Discussion

We'll begin by putting in place the necessary notation. Let $ {\mathcal T} $ be the regular triangular tiling of the plane. For every $ n \ge 1 $ there is a regular map which triangulates the torus, denoted $ T_n $ , which may be obtained from a regular hexagonal piece of $ {\mathcal T} $ of side-length $ n $ by identifying points on opposite edges of this hexagon. Let $ H_n $ be the dual of $ T_n $ (on the torus). Then $ H_n $ is a regular map on the torus - a hexagonal tiling. One last definition: for any graph $ G $ and any positive integer $ k $ we let $ \chi(G,k) $ denote the number of proper $ k $ -coloring of $ G $ . A famous theorem of Lieb [L] shows that $ \lim_{n \rightarrow \infty} (\chi(Q_n,3))^{1 / |V(Q_n)|} = (\frac{4}{3})^{3/2} $ where $ Q_n $ denotes the $ n \times n $ quadrangulation of the torus. This theorem is usually stated in terms of Eulerian orientations, and is of interest to physicists as the constant $ (\frac{4}{3})^{3/2} $ (called Lieb's Ice Constant) determines the "residual entropy for square ice". Thomassen proved that every planar graph $ G $ with girth $ \ge 5 $ has exponentially many proper 3-colorings. More precisely, he showed that $ (\chi(G,3))^{ 1 / |V(G)| } \ge 2 ^{1 / 10000} $ . This gives a lower bound on the limit in the above problem (assuming it exists).

Bibliography

 [L]
 E. H. Lieb, Exact Solution of the Problem of the Entropy of Two-Dimensional Ice. Phys. Rev. Lett. 18, 692-694, 1967.
