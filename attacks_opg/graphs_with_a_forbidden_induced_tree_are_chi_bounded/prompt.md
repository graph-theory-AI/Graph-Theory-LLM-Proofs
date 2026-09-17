Attack the following open graph-theory problem.

Catalog id: graphs_with_a_forbidden_induced_tree_are_chi_bounded
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/graphs_with_a_forbidden_induced_tree_are_chi_bounded/
Original entry: http://www.openproblemgarden.org/op/graphs_with_a_forbidden_induced_tree_are_chi_bounded
Problem attributed to: Gyarfas, Andras (posted 2009-05-16)

=== Problem statement (OpenProblemGarden) ===
Title: Graphs with a forbidden induced tree are chi-bounded
Say that a family $ {\mathcal F} $ of graphs is $ \chi $ - bounded if there exists a function $ f: {\mathbb N} \rightarrow {\mathbb N} $ so that every $ G \in {\mathcal F} $ satisfies $ \chi(G) \le f (\omega(G)) $ . Conjecture For every fixed tree $ T $ , the family of graphs with no induced subgraph isomorphic to $ T $ is $ \chi $ -bounded.

=== Discussion / context (OpenProblemGarden) ===
This deep conjecture remains open despite considerable effort. Note that the conjecture would be false were the graph $ T $ to be permitted to contain a cycle, since then the class would admit graphs of high girth (where $ \omega = 2 $ ) and high chromatic number. It is an easy exercise to prove this conjecture in the special case when $ T $ is either a path or a star, but things get difficult from here. Kierstead and Penrice solved the special case when $ T $ has radius 2, and Kierstead and Zhu solved the special case when $ T $ has radius 3 and has the property that every vertex incident with the center vertex has degree 2. Scott proved that the class of graphs which exclude all subdivisions of a fixed tree $ T $ as induced subgraphs are $ \chi $ -bounded. It follows from this that Gyarfas's conjecture also holds for subdivisions of stars.

=== Catalog page (statement + literature review) ===
Graphs with a forbidden induced tree are chi-bounded — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Gyárfás–Sumner conjecture remains open in full generality for all trees. Significant recent progress includes Nguyen, Scott, and Seymour (2024) proving that every $H$-free graph (for any forest $H$) with bounded clique number has a stable set of size $|G|^{1-o(1)}$ (near-linear), and Davies and Yuditsky (2024) proving the polynomial version of the conjecture for intersection graphs of axis-aligned boxes (bounded boxicity).

 Cited literature (4)

 
 
 
partial Trees and near-linear stable sets
 (2024)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · Combinatorica · arXiv:2409.09397

For every forest $H$, every $H$-free graph with bounded clique number has a stable set of size $|G|^{1-o(1)}$; moreover, multibrooms satisfy a fractional colouring version of the Gyárfás–Sumner conjecture.
 

 
 
partial Polynomial Gyárfás-Sumner conjecture for graphs of bounded boxicity
 (2024)
 

 
 James Davies, Yelena Yuditsky · arXiv preprint · arXiv:2407.16882

For every positive integer $d$ and forest $F$, the class of intersection graphs of axis-aligned boxes in $\mathbb{R}^d$ with no induced $F$ subgraph is polynomially $\chi$-bounded.
 

 
 
partial Degeneracy of $P_t$-free and $C_{\geq t}$-free graphs with no large complete bipartite subgraphs
 (2021)
 

 
 Marthe Bonamy, Nicolas Bousquet, Michał Pilipczuk, Paweł Rzążewski, Stéphan Thomassé, Bartosz Walczak · arXiv preprint · arXiv:2012.03686

Proves a biclique-exclusion relaxation: every $C_{\geq t}$-free graph containing no $K_{\ell,\ell}$ as a subgraph satisfies $\chi(G) \leq \ell^{f(t)}+1$, giving a polynomial bound in $\ell$ under the additional assumption of no large balanced biclique.
 

 
 
partial Polynomial bounds for chromatic number VI. Adding a four-vertex path
 (2023)
 

 
 Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:2202.10412

Proves that if $H$ is a good forest then the disjoint union of $H$ and $P_4$ is also good (polynomially $\chi$-bounded), in particular showing that $2P_4$-free graphs satisfy $\chi(G) \leq \omega(G)^{16}$; more generally proves polynomial $\chi$-boundedness for $\{H_1, H_2\}$-free graphs when every component of $H_1$ is good and $H_2$ is a broom or disjoint union of a good forest and paths.
 

 

 Reviewer notes. The Scott–Seymour long series on induced subgraphs of graphs with large chromatic number contains many partial results for specific tree families (paths, multibrooms, radius-2 trees), predating the 2024 results cited here. The full conjecture for all trees remains open. Published Springer links for the Combinatorica version of 2409.09397 redirected to a login page and could not be fetched directly.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. For every fixed tree $ T $ , the family of graphs with no induced subgraph isomorphic to $ T $ is $ \chi $ -bounded.

Keywords:
chi-bounded · coloring · excluded subgraph · tree

Discussion

This deep conjecture remains open despite considerable effort. Note that the conjecture would be false were the graph $ T $ to be permitted to contain a cycle, since then the class would admit graphs of high girth (where $ \omega = 2 $ ) and high chromatic number. It is an easy exercise to prove this conjecture in the special case when $ T $ is either a path or a star, but things get difficult from here. Kierstead and Penrice solved the special case when $ T $ has radius 2, and Kierstead and Zhu solved the special case when $ T $ has radius 3 and has the property that every vertex incident with the center vertex has degree 2. Scott proved that the class of graphs which exclude all subdivisions of a fixed tree $ T $ as induced subgraphs are $ \chi $ -bounded. It follows from this that Gyarfas's conjecture also holds for subdivisions of stars.

Related conjectures

 
 equivalent to
 Forb(H) χ-bounded iff H is forest
 partial
 Verified in the paper's text (Conjecture 2, about undirected graphs H): 'an easy argument shows that the conjecture is equivalent to the following one. Conjecture 2. Forb(H) is χ-bounded if and only if H is a forest.' The claimed implication holds immediately: the 'if' direction at H = T (a tree is a forest) is exactly Gyárfás–Sumner. The converse also holds, so the relation is in fact an equivalence: the 'only if' direction follows from Erdős's girth theorem (high-girth high-χ graphs avoid any H with a cycle), and the forest case follows from the tree case since any forest is an induced subgraph of a tree. Note: the finder's sketch misreads H as an oriented forest; Conjecture 2 in the paper is about undirected graphs, which makes the implication direct.
 

 
 equivalent to
 Forb(H) χ-bounded iff H is forest
 partial
 The source's own context explicitly states that an easy argument shows the biconditional 'Forb(H) is chi-bounded iff H is a forest' is equivalent to the Gyarfas-Sumner conjecture (the target). Verification: (target => source) the 'only if' half of the source is Erdos's girth theorem (if H contains a cycle, graphs of girth > |H| and huge chromatic number are H-free with omega = 2), and the 'if' half for a forest H follows from the tree case by a standard easy induction on components (this closure under disjoint union is known for ordinary chi-boundedness, unlike the polynomial version). (source => target) trivial restriction: a tree is a forest. So the two are genuinely equivalent, as claimed.
 

 
 implied by
 Forests are multibounding chromatic bound
 open
 Stated in the source's context: 'Every multibounding graph must be a forest satisfying the Gyarfas-Sumner conjecture.' Self-contained derivation: fix a tree T (a forest, hence multibounding by the source). Take t = 1, so K_d(1) = K_d; a T-free graph G with omega(G) < d has no K_d subgraph, so the multibounding property gives chi(G) <= f_d(1). Setting g(omega) = f_{omega+1}(1) yields a chi-bounding function for the class of T-free graphs, which is exactly the target. Direction correct: multibounding is the quantitatively stronger, K_d(t)-parameterized statement specializing at t=1 to plain chi-boundedness.
 

 
 implied by
 Polynomial χ-boundedness for forest-free graphs
 partial
 Direct weakening in two independent ways: every tree T is a forest, so the source instantiated at H = T applies; and a polynomial χ-bounding function f is in particular a χ-bounding function. So if for every forest H there is a polynomial f with χ(G) ≤ f(ω(G)) for H-free G, then for every tree T the class of T-free graphs is χ-bounded, which is exactly the Gyárfás–Sumner conjecture as stated in the target. Hypothesis classes and parameterization (χ vs ω, induced-subgraph exclusion) match exactly. Direction is correct: source is strictly stronger (polynomial vs arbitrary bounding function, forests vs trees).
 

 
 implied by
 Polynomial χ-bounding in Gyárfás-Sumner
 partial
 The source asserts that for every fixed tree T the class of T-free graphs admits a chi-bounding function polynomial in the clique number; a polynomial chi-bounding function is in particular a chi-bounding function, so the target (Gyárfás-Sumner: T-free graphs are chi-bounded) follows immediately. Strictly stronger statement, same hypothesis class (T-free graphs for every fixed tree T), monotone strengthening of the conclusion only. Direction as claimed. (The source is phrased informally as 'it is possible that...', but read as a conjecture the implication is trivial.)
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
