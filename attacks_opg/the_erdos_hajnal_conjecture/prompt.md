Attack the following open graph-theory problem.

Catalog id: the_erdos_hajnal_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_erdos_hajnal_conjecture/
Original entry: http://www.openproblemgarden.org/op/the_erdos_hajnal_conjecture
Problem attributed to: Erdos, Paul, Hajnal, Andras (posted 2007-03-18)

=== Problem statement (OpenProblemGarden) ===
Title: The Erdös-Hajnal Conjecture
Conjecture For every fixed graph $ H $ , there exists a constant $ \delta(H) $ , so that every graph $ G $ without an induced subgraph isomorphic to $ H $ contains either a clique or an independent set of size $ |V(G)|^{\delta(H)} $ .

=== Discussion / context (OpenProblemGarden) ===
There are numerous interesting classes of graphs which are based upon forbidding one or more induced subgraphs. For instance: chordal graphs , split graphs , and claw-free graphs. Numerous other natural classes of graphs have been proved to have such characterizations, most famously perfect graphs , but also line graphs and comparability graphs . All of these classes are very well structured (far from random) and their members all either have large cliques or independent sets. On the flip side of this are random graphs . It is well known that a random graph on $ n $ vertices has both clique and independence number highly concentrated around $ 2 \log_2 n $ . The Erdos-Hajnal conjecture suggests a fundamental separation between these two worlds in terms of independence/clique sizes. Erdös and Hajnal proved that this conjecture is true for the recursive class of graphs $ {\mathcal C} $ defined as follows. The one vertex graph is in $ {\mathcal C} $ , and if $ G_1 $ and $ G_2 $ lie in $ {\mathcal C} $ , then the disjoint union of $ G_1 $ and $ G_2 $ lies in $ {\mathcal C} $ , as does the graph obtained from the disjoint union by adding an edge between $ v_1 $ and $ v_2 $ for every $ v_1 \in V(G_1) $ and $ v_2 \in V(G_2) $ . More generally, Alon, Pach, and Solymosi proved that if $ F $ is a graph with $ V(F) = \{v_1,v_2,\ldots,v_n\} $ for which the Erdös-Hajnal conjecture holds, and $ H_1,\ldots,H_n $ are graphs for which the Erdos-Hajnal conjecture holds, then the graph obtained from $ F $ by blowing up each vertex $ v_i $ with a copy of $ H_i $ (more precisely, starting from the disjoint union of $ H_1,H_2,\ldots,H_n $ , we add all possible edges between the vertices of $ V(H_i) $ and $ V(H_j) $ if $ ij \in E(F) $ ) also satisfies the Erdos-Hajnal conjecture. The Erdös-Hajnal property is known to hold for a number of small graphs (and using the above result this may be easily bootstrapped). For instance, the conjecture is known to hold when $ H $ is a path of three edges, and recently M. Chudnovsky and S. Safra have announced a proof when $ H $ is a bull (a triangle plus two pendant edges). However, our knowledge here is still quite limited. In particular, Lovasz has suggested the following very special case which remains open. Question Is the Erdös-Hajnal conjecture true when $ H \cong C_5 $ ?

=== References listed by OpenProblemGarden ===
- [APS] N. Alon, J. Pach, and J. Solymosi, Ramsey-type theorems with forbidden subgraphs, Combinatorica 21 (2001), 155-170.
- [EH] P. Erdös and A. Hajnal, Ramsey-type theorems, Discrete Appl. Math. 25 (1989), 37-52 MathSciNet

=== Catalog page (statement + literature review) ===
The Erdös-Hajnal Conjecture — Graph-theory open problems

 Also at erdosproblems.com #61 (open, fuzzy-match score 68)

 
 Status
 partial
 high confidence
 

 The full Erdős–Hajnal conjecture remains open for a general graph $H$, but remarkable progress has been made since 2021. Chudnovsky, Scott, Seymour, and Spirkl proved the conjecture for $H = C_5$, the specific case raised by Lovász; Nguyen, Scott, and Seymour subsequently proved it for $H = P_5$ and for infinitely many previously unknown prime graphs; and the first improvement to the general lower bound in nearly five decades was established, raising it from $2^{c\sqrt{\log n}}$ to $2^{c\sqrt{\log n\,\log\log n}}$.

 Cited literature (22)

 
 
 
proof Erdos-Hajnal for graphs with no 5-hole
 (2021)
 

 
 Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl · Proceedings of the London Mathematical Society · arXiv:2102.04994 · doi:10.1112/plms.12504

Proves the Erdős–Hajnal conjecture for $H = C_5$ (the five-cycle), settling the specific case highlighted by Lovász in the OPG discussion.
 

 
 
partial Towards the Erdős-Hajnal conjecture for $P_5$-free graphs
 (2022)
 

 
 Pablo Blanco, Matija Bucić · Research in the Mathematical Sciences · arXiv:2210.10755

Improves the best known lower bound for $P_5$-free $n$-vertex graphs from $2^{\Omega(\sqrt{\log n})}$ to $2^{\Omega((\log n)^{2/3})}$, the strongest bound known before the full $P_5$ case was proved.
 

 
 
partial Induced subgraph density. I. A loglog step towards Erdos-Hajnal
 (2023)
 

 
 Matija Bucić, Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2301.10147

Improves the universal lower bound (for all forbidden $H$) from $2^{c\sqrt{\log n}}$ to $2^{c\sqrt{\log n\,\log\log n}}$, the first improvement to the general bound in nearly 45 years.
 

 
 
partial Induced subgraphs density. IV. New graphs with the Erdős-Hajnal property
 (2023)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2307.06455

Proves that infinitely many prime graphs satisfy the Erdős–Hajnal property, vastly expanding the known list beyond the three prime graphs previously confirmed.
 

 
 
proof Induced subgraph density. VII. The five-vertex path
 (2023)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2312.15333

Proves the Erdős–Hajnal conjecture for $H = P_5$ (the five-vertex path), which was the smallest open case prior to this work.
 

 
 
partial Erdos-Hajnal conjecture for graphs with bounded VC-dimension
 (2017)
 

 
 Jacob Fox, János Pach, Andrew Suk · arXiv preprint · arXiv:1710.03745

Proves (Theorem 1.1) that every $n$-vertex graph with VC-dimension at most $d$ contains a clique or an independent set of size at least $e^{(\log n)^{1-o(1)}}$, nearly matching the conjectured polynomial lower bound $n^{\varepsilon(\mathcal{P})}$ and improving the general lower bound $e^{\varepsilon\sqrt{\log n}}$ of Erdős and Hajnal for all hereditary properties.
 

 
 
partial Near-domination in graphs
 (2019)
 

 
 Bruce Reed, Alex Scott, Paul Seymour · arXiv preprint · arXiv:1710.06680

Applies the main result (Theorem 1.1, that every $t$-dominating graph has bounded local difference from a $0$-dominating graph) to the Erdős-Hajnal conjecture; the details are in the final section of the paper.
 

 
 
partial Caterpillars in Erdős-Hajnal
 (2018)
 

 
 Anita Liebenau, Marcin Pilipczuk, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:1810.00811

Proves that for every caterpillar subdivision $H$ there exists $c > 0$ such that every graph $G$ that is both $H$-free and $\bar{H}$-free satisfies $\max(\omega(G), \alpha(G)) \geq |V(G)|^c$, extending results of Bousquet–Lagoutte–Thomassé (paths) and Choromanski–Falik–Liebenau–Patel–Pilipczuk (hooks).
 

 
 
partial Bounded VC-dimension implies the Schur-Erdos conjecture
 (2019)
 

 
 Jacob Fox, Janos Pach, Andrew Suk · arXiv preprint · arXiv:1912.02342

Not proved here; mentioned in the concluding remarks as an important open problem motivating future work on graphs with bounded VC-dimension.
 

 
 
partial Erdos-Hajnal for graphs with no 5-hole
 (2021)
 

 
 Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:2102.04994

Proves the conjecture for $H = C_5$: every $C_5$-free graph $G$ satisfies $\max(\alpha(G), \omega(G)) \geq |G|^\tau$ for some absolute constant $\tau > 0$.
 

 
 
partial Induced subgraph density. III. Cycles and subdivisions
 (2024)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2307.06379

Proves that $\{H,\overline{J}\}$ has the Erdős-Hajnal property for any two cycles $H,J$, and more generally when $H$ and $J$ are obtained from smaller graphs by subdividing every edge exactly twice (or, for one of them, by subdividing every non-forest edge at least five times); this simultaneously extends the $C_5$ result and resolves the open question from [6] about longer cycles.
 

 
 
partial Equivalence between Erdős-Hajnal and polynomial Rödl and Nikiforov conjectures
 (2024)
 

 
 Matija Bucić, Jacob Fox, Huy Tuan Pham · arXiv preprint · arXiv:2403.08303

Proves that the Erdős-Hajnal conjecture is equivalent to both the polynomial Rödl conjecture (Conjecture 2) and the polynomial Nikiforov conjecture (Conjecture 3), extending several previous partial equivalence results.
 

 
 
partial Induced subgraph density. VII. The five-vertex path
 (2026)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2312.15333

Proves that $P_5$ satisfies the Erdős-Hajnal conjecture (Theorem 1.2), thereby completing the verification of the conjecture for all five-vertex graphs.
 

 
 
partial Induced subgraph density. IV. New graphs with the Erdős-Hajnal property
 (2026)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2307.06455

Proves infinitely many prime graphs satisfy the conjecture: all graphs $H$ whose every non-trivial prime induced subgraph $H'$ has a vertex of degree one and a vertex of degree $|H'|-2$; more generally, proves it whenever $H_1$ and $\overline{H_2}$ are both buildable (every prime induced subgraph with at least three vertices has a vertex of degree one).
 

 
 
partial Polynomial bounds for chromatic number. IV. A near-polynomial bound for excluding the five-vertex path
 (2022)
 

 
 Alex Scott, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:2110.00278

Proves the near-polynomial bound $\chi(G) \leq \omega(G)^{\log_2(\omega(G))}$ for $P_5$-free graphs with $\omega(G) \geq 3$, significantly improving the previously best known exponential bound $(5/27)3^{\omega(G)}$ within the Gyárfás-Sumner framework.
 

 
 
partial Induced subgraph density. VI. Bounded VC-dimension
 (2025)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2312.15572

Proves the conjecture for every two-colourable tournament, which in particular completes the verification of the conjecture for all six-vertex tournaments.
 

 
 
partial Pure pairs. IV. Trees in bipartite graphs
 (2023)
 

 
 Alex Scott, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:2009.09426

Proves bipartite analogues of the strong Erdős-Hajnal property (Theorems 1.5 and 1.6), establishing that excluding a forest bigraph and its bicomplement forces linear-sized pure pairs in each part, and providing one-sided sparse versions; these results imply bipartite Erdős-Hajnal-type bounds.
 

 
 
partial Holes with hats and Erdős-Hajnal
 (2020)
 

 
 Maria Chudnovsky, Paul Seymour · arXiv preprint · arXiv:2005.02896

Proves the conjecture for the class of hole-with-hat-free graphs: there exists $\varepsilon > 0$ such that every hole-with-hat-free graph $G$ has a clique or stable set of cardinality at least $|G|^\varepsilon$. This strictly generalises the house-free case (since hole-with-hat-free implies house-free) but does not resolve the house/$P_5$ open case.
 

 
 
partial Pure pairs. I. Trees and linear anticomplete pairs
 (2020)
 

 
 Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:1809.00919

Proves that for every forest $H$ there exists $c > 0$ such that every graph $G$ that is both $H$-free and $\bar{H}$-free satisfies $\alpha(G)\omega(G) \geq |G|^c$, establishing the Erdős-Hajnal property for all finitely-defined ideals excluding a forest and its complement.
 

 
 
partial Induced subgraph density. I. A loglog step towards Erdos-Hajnal
 (2024)
 

 
 Matija Bucić, Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2301.10147

Proves that every $H$-free graph $G$ with $|G|\geq 2$ satisfies $\kappa(G)\geq 2^{c\sqrt{\log|G|}\,\log\log|G|}$ (Theorem 1.3), the first improvement over the $2^{c\sqrt{\log|G|}}$ bound for general $H$ since 1977, obtained as a corollary of a stronger quantitative result (Theorem 1.8) that also strengthens theorems of Rödl, Nikiforov, and Fox–Sudakov.
 

 
 
partial Towards Erdos-Hajnal for graphs with no 5-hole
 (2018)
 

 
 Maria Chudnovsky, Jacob Fox, Alex Scott, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:1803.03588

Proves that for every $C_5$-free graph $G$ with $n > 1$ vertices, $\max(\alpha(G), \omega(G)) \geq 2^{c\sqrt{\log n \log \log n}}$, improving the previously best known general bound of $2^{c\sqrt{\log n}}$ when $H = C_5$.
 

 
 
partial Pure pairs. II. Excluding all subdivisions of a graph
 (2020)
 

 
 Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:1804.01060

Establishes equivalence with Conjecture 2.1 via Rödl's theorem (Lemma 3.1), and verifies the statement for ideals defined by excluding induced subdivisions of a fixed graph in both $G$ and $\bar{G}$.
 

 

 Reviewer notes. The DOI 10.1112/plms.12504 for the C5 paper was identified via a Wiley search result; the journal page returned HTTP 403 so direct WebFetch verification was not possible, but the arXiv abstract fully confirms the paper. The venue 'Research in the Mathematical Sciences' for 2210.10755 was identified via a Springer search result but not directly WebFetch-verified; the arXiv URL is used. The 'Induced subgraph density' series by Nguyen–Scott–Seymour spans at least seven papers (I–VII); only those most directly relevant to the Erdős–Hajnal conjecture are included here. The full conjecture for arbitrary H remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. For every fixed graph $ H $ , there exists a constant $ \delta(H) $ , so that every graph $ G $ without an induced subgraph isomorphic to $ H $ contains either a clique or an independent set of size $ |V(G)|^{\delta(H)} $ .

Keywords:
induced subgraph

Discussion

There are numerous interesting classes of graphs which are based upon forbidding one or more induced subgraphs. For instance: chordal graphs , split graphs , and claw-free graphs. Numerous other natural classes of graphs have been proved to have such characterizations, most famously perfect graphs , but also line graphs and comparability graphs . All of these classes are very well structured (far from random) and their members all either have large cliques or independent sets. On the flip side of this are random graphs . It is well known that a random graph on $ n $ vertices has both clique and independence number highly concentrated around $ 2 \log_2 n $ . The Erdos-Hajnal conjecture suggests a fundamental separation between these two worlds in terms of independence/clique sizes. Erdös and Hajnal proved that this conjecture is true for the recursive class of graphs $ {\mathcal C} $ defined as follows. The one vertex graph is in $ {\mathcal C} $ , and if $ G_1 $ and $ G_2 $ lie in $ {\mathcal C} $ , then the disjoint union of $ G_1 $ and $ G_2 $ lies in $ {\mathcal C} $ , as does the graph obtained from the disjoint union by adding an edge between $ v_1 $ and $ v_2 $ for every $ v_1 \in V(G_1) $ and $ v_2 \in V(G_2) $ . More generally, Alon, Pach, and Solymosi proved that if $ F $ is a graph with $ V(F) = \{v_1,v_2,\ldots,v_n\} $ for which the Erdös-Hajnal conjecture holds, and $ H_1,\ldots,H_n $ are graphs for which the Erdos-Hajnal conjecture holds, then the graph obtained from $ F $ by blowing up each vertex $ v_i $ with a copy of $ H_i $ (more precisely, starting from the disjoint union of $ H_1,H_2,\ldots,H_n $ , we add all possible edges between the vertices of $ V(H_i) $ and $ V(H_j) $ if $ ij \in E(F) $ ) also satisfies the Erdos-Hajnal conjecture. The Erdös-Hajnal property is known to hold for a number of small graphs (and using the above result this may be easily bootstrapped). For instance, the conjecture is known to hold when $ H $ is a path of three edges, and recently M. Chudnovsky and S. Safra have announced a proof when $ H $ is a bull (a triangle plus two pendant edges). However, our knowledge here is still quite limited. In particular, Lovasz has suggested the following very special case which remains open. Question Is the Erdös-Hajnal conjecture true when $ H \cong C_5 $ ?

Bibliography

 [APS]
 N. Alon, J. Pach, and J. Solymosi, Ramsey-type theorems with forbidden subgraphs , Combinatorica 21 (2001), 155-170.
 Ramsey-type theorems with forbidden subgraphs

 [EH]
 P. Erdös and A. Hajnal, Ramsey-type theorems, Discrete Appl. Math. 25 (1989), 37-52 MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 Multicolour Erdős--Hajnal Conjecture
 partial
 Standard specialization to m=2. Given a graph H on k >= 2 vertices, let chi be the 2-colouring of E(K_k) with colour 1 on edges of H and colour 2 on non-edges. A 2-colouring of E(K_n) is exactly a graph G on n vertices (colour 1 = edge). The multicolour conjecture for (k, chi, m=2) gives epsilon > 0 such that G contains either k vertices whose pairs are coloured according to chi -- an induced copy of H -- or n^epsilon vertices whose pairs use at most m-1 = 1 colour -- a clique or an independent set of size n^epsilon. So every H-free G has a clique or independent set of size n^epsilon, which is Erdos-Hajnal with delta(H) = epsilon. Quantifying over all k and chi covers every fixed H (H with <= 1 vertex is trivial). Direction correct: multicolour is the stronger statement; its m=2 instance is classical EH.
 

 
 implies
 Polynomial clique/independent set in bounded VC-dimension graphs
 solved
 Let H_d be the fixed bipartite graph with parts {v_1,...,v_{d+1}} and {w_S : S ⊆ [d+1]}, where w_S is adjacent exactly to {v_i : i ∈ S}. In H_d the set {v_1,...,v_{d+1}} is shattered by neighbourhoods, so VC-dim(H_d) ≥ d+1. VC-dimension is monotone under induced subgraphs (neighbourhoods of an induced subgraph are traces of neighbourhoods of the host), so every graph of VC-dimension ≤ d is induced-H_d-free. Hence the class of VC-dim ≤ d graphs is contained in the H_d-free class, and Erdős–Hajnal applied to the single graph H = H_d yields a clique or independent set of size n^{δ(H_d)}, giving the target with ε(d) = δ(H_d). Direction is as claimed: EH is the stronger, general statement. The target's own context calls it 'the VC-dimension specialisation of the Erdős–Hajnal conjecture'.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
