Attack the following open graph-theory problem.

Catalog id: minimal_graphs_with_a_prescribed_number_of_spanning_trees
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/minimal_graphs_with_a_prescribed_number_of_spanning_trees/
Original entry: http://www.openproblemgarden.org/op/minimal_graphs_with_a_prescribed_number_of_spanning_trees
Problem attributed to: Azarija, Jernej, Skrekovski, Riste (posted 2012-04-22)

=== Problem statement (OpenProblemGarden) ===
Title: Minimal graphs with a prescribed number of spanning trees
Conjecture Let $ n \geq 3 $ be an integer and let $ \alpha(n) $ denote the least integer $ k $ such that there exists a simple graph on $ k $ vertices having precisely $ n $ spanning trees. Then $ \alpha(n) = o(\log{n}). $

=== Discussion / context (OpenProblemGarden) ===
Observe that $ \alpha(n) $ is well defined for $ n \geq 3 $ since $ C_n $ has $ n $ spanning trees. The function was introduced by Sedlacek [S] who has shown that for large enough $ n $ $ \alpha(n) \leq \frac{n+6}{3} \mbox{if } n \equiv 0 \pmod{3} $ and $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3}. $ Using the fact that almost all positive integers $ n $ are expressible as $ n = ab+ac+bc $ for integers $ 0 < a < b < c $ it can be shown [A] that for large enough $ n $ $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3} $ and $ \alpha(n) \leq \frac{n+9}{4} $ otherwise. Moreover, the only fixed points of $ \alpha $ are 3, 4, 5, 6, 7, 10, 13 and 22. The conjecture is motivated by the following graph (ploted for a very small sample of vertices) The conjecture [C] is justifiable for highly composite numbers $ n $ since in this case one can construct the graph obtained after taking cycles $ C_{p_1}, \ldots,C_{p_k} $ for every odd prime factor $ p_i $ of $ n $ .

=== References listed by OpenProblemGarden ===
- [S] J. Sedlacek, On the minimal graph with a given number of spanning trees, Canad. Math. Bull. 13 (1970) 515-517.
- [A] J. Azarija, R. Skrekovski, Euler's idoneal numbers and an inequality concerning minimal graphs with a prescribed number of spanning trees, IMFM preprints 49 (2011) Link to paper
- * [C] Minimal graphs with a prescribed number of spanning trees

=== Catalog page (statement + literature review) ===
Minimal graphs with a prescribed number of spanning trees — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture $\alpha(n) = o(\log n)$ remains open, but significant progress has been made. Stong (2022) proved a weak version: $\alpha(n) = O((\log n)^{3/2} / \log\log n)$, the current state of the art. More recently, Alon, Bucć, and Gishboliner (2025) proved a modular analogue: for any $N$ and $u < N$, there exists a planar graph on $O(\log N)$ vertices whose spanning tree count is $\equiv u \pmod{N}$.

 Cited literature (2)

 
 
 
partial Minimal graphs with a prescribed number of spanning trees
 (2022)
 

 
 Richard Stong · Australasian Journal of Combinatorics

Proves $\alpha(n) = O((\log n)^{3/2} / \log\log n)$, a weak version of the conjecture $\alpha(n) = o(\log n)$, using algebraic number theory.
 

 
 
partial The spanning tree spectrum: improved bounds and simple proofs
 (2025)
 

 
 Noga Alon, Matija Bucć, Lior Gishboliner · arXiv preprint · arXiv:2503.23648

Proves a modular analogue of the conjecture: for any $N$ and $u < N$, there exists a planar graph on $O(\log N)$ vertices with spanning tree count $\equiv u \pmod{N}$; the full conjecture $\alpha(t) = O(\log t)$ is explicitly noted as still open.
 

 

 Reviewer notes. The Stong (2022) AJC paper PDF could not be directly extracted by WebFetch (binary content), but title/author/year were confirmed via the AJC volume 82 table-of-contents page and corroborated by multiple search results; the main result is also cited as state-of-the-art by the Alon et al. (2025) paper. No arXiv preprint was found for Stong's paper. The Alon et al. paper (arXiv:2503.23648, submitted March 2025) was independently verified via both the abstract and HTML pages.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Let $ n \geq 3 $ be an integer and let $ \alpha(n) $ denote the least integer $ k $ such that there exists a simple graph on $ k $ vertices having precisely $ n $ spanning trees. Then $ \alpha(n) = o(\log{n}). $

Keywords:
number of spanning trees, asymptotics

Discussion

Observe that $ \alpha(n) $ is well defined for $ n \geq 3 $ since $ C_n $ has $ n $ spanning trees. The function was introduced by Sedlacek [S] who has shown that for large enough $ n $ $ \alpha(n) \leq \frac{n+6}{3} \mbox{if } n \equiv 0 \pmod{3} $ and $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3}. $ Using the fact that almost all positive integers $ n $ are expressible as $ n = ab+ac+bc $ for integers $ 0 < a < b < c $ it can be shown [A] that for large enough $ n $ $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3} $ and $ \alpha(n) \leq \frac{n+9}{4} $ otherwise. Moreover, the only fixed points of $ \alpha $ are 3, 4, 5, 6, 7, 10, 13 and 22. The conjecture is motivated by the following graph (ploted for a very small sample of vertices) The conjecture [C] is justifiable for highly composite numbers $ n $ since in this case one can construct the graph obtained after taking cycles $ C_{p_1}, \ldots,C_{p_k} $ for every odd prime factor $ p_i $ of $ n $ .

Bibliography

 [S]
 J. Sedlacek, On the minimal graph with a given number of spanning trees, Canad. Math. Bull. 13 (1970) 515-517.

 [A]
 J. Azarija, R. Skrekovski, Euler's idoneal numbers and an inequality concerning minimal graphs with a prescribed number of spanning trees, IMFM preprints 49 (2011) Link to paper
 Link to paper

★ [C]
 Minimal graphs with a prescribed number of spanning trees
 Minimal graphs with a prescribed number of spanning trees
