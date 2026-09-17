Attack the following open graph-theory problem.

Catalog id: negative_association_in_uniform_forests
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Probabilistic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/negative_association_in_uniform_forests/
Original entry: http://www.openproblemgarden.org/op/negative_association_in_uniform_forests
Problem attributed to: Pemantle, Robin (posted 2008-06-30)

=== Problem statement (OpenProblemGarden) ===
Title: Negative association in uniform forests
Conjecture Let $ G $ be a finite graph, let $ e,f \in E(G) $ , and let $ F $ be the edge set of a forest chosen uniformly at random from all forests of $ G $ . Then \[ {\mathbb P}(e \in F \mid f \in F}) \le {\mathbb P}(e \in F) \]

=== Discussion / context (OpenProblemGarden) ===
The FKG inequality is the cornerstone of a respectable theory of positive association; If a natural lattice condition holds, we can use it to deduce positive association. On the other hand, the theory of negative associations is still lacking good techniques. See Pemantle's lovely paper [P] for an excellent description of this situation. The conjecture highlighted above seems to be almost obviously true, but we have no tools to prove it. Modifying the conjecture by replacing "forest" by "spanning tree" gives a true statement which was proved by Feder and Mihail [FM]. Actually, they prove that this holds more generally for uniform bases of balanced matroids. Perhaps surprisingly, this is false for general matroids, see [SW].

=== References listed by OpenProblemGarden ===
- [FM] T. Feder and M. Mihail, Balanced Matroids. Proc 24th Annual STOC 26 - 38 (1992).
- *[P] R. Pemantle, Towards a theory of negative dependence, Journal of Mathematical Physics 41 (2000), 1371–1390.
- [SW] P. D. Seymour and D. J. A. Welsh, Combinatorial applications of an inequality from statistical mechanics. Math. Proc. Camb. Phil. Soc. 77 485 - 495 (1975).

=== Catalog page (statement + literature review) ===
Negative association in uniform forests — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture that a uniformly random forest $F$ of a finite graph $G$ satisfies $\mathbb{P}(e \in F \mid f \in F) \le \mathbb{P}(e \in F)$ for any two edges $e, f$ remains open in full generality. Stark (2011) proved it for complete graphs $K_n$ when $n$ is sufficiently large via enumerative methods; Tang and Zhang (2026) extended pairwise negative correlation to families of uniform spanning subgraphs (forests with a fixed number of components, connected subgraphs with given excess) of $K_n$ for large $n$. The general case resists proof because the uniform forest measure is not strongly Rayleigh, so the Borcea–Brändén–Liggett framework that settles the spanning-tree variant does not apply.

 Cited literature (3)

 
 
 
partial The edge correlation of random forests
 (2011)
 

 
 Dudley Stark · Annals of Combinatorics · doi:10.1007/s00026-011-0104-7

Proves pairwise negative correlation for the uniform random forest on $K_n$ for all sufficiently large $n$ using enumerative methods, confirming the conjecture in this special case.
 

 
 
partial On Negative Correlation of Arboreal Gas on Some Graphs
 (2023)
 

 
 Xiangyu Huang · arXiv preprint · arXiv:2311.00965

Establishes negative correlation for the arboreal gas (a $\beta$-weighted random forest model that specialises to the uniform forest at $\beta=1$) on specific graph families, while explicitly noting that the general conjecture remains open.
 

 
 
partial Pairwise Negative Correlation for Uniform Spanning Subgraphs of the Complete Graph
 (2026)
 

 
 Pengfei Tang, Zibo Zhang · arXiv preprint · arXiv:2603.10738

Proves pairwise negative correlation for uniform forests with exactly $k$ components and for uniform connected spanning subgraphs with given excess on $K_n$ for all sufficiently large $n$.
 

 

 Reviewer notes. The Stark (2011) Springer page was inaccessible due to a paywall redirect; the result is confirmed via the Oxford Mathematical Institute seminar record (maths.ox.ac.uk/node/7029) and independent search summaries. The Grimmett–Winkler (RSA 2004) computational verification for small graphs, the Semple–Welsh (CPC 2008) infinite class of special cases, and the Borcea–Brändén–Liggett (JAMS 2009) strongly Rayleigh framework all predate or nearly coincide with the OPG posting and are not listed in since_posted; they are important context. The arboreal gas at $\beta=1$ coincides with the uniform forest measure, so Huang (2023) is directly relevant. Specific graphs in Huang (2023) could not be extracted from the abstract page alone. The problem is confirmed open as of November 2023 by Huang's explicit statement.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Let $ G $ be a finite graph, let $ e,f \in E(G) $ , and let $ F $ be the edge set of a forest chosen uniformly at random from all forests of $ G $ . Then \[ {\mathbb P}(e \in F \mid f \in F}) \le {\mathbb P}(e \in F) \]

Keywords:
forest · negative association

Discussion

The FKG inequality is the cornerstone of a respectable theory of positive association; If a natural lattice condition holds, we can use it to deduce positive association. On the other hand, the theory of negative associations is still lacking good techniques. See Pemantle's lovely paper [P] for an excellent description of this situation. The conjecture highlighted above seems to be almost obviously true, but we have no tools to prove it. Modifying the conjecture by replacing "forest" by "spanning tree" gives a true statement which was proved by Feder and Mihail [FM]. Actually, they prove that this holds more generally for uniform bases of balanced matroids. Perhaps surprisingly, this is false for general matroids, see [SW].

Bibliography

 [FM]
 T. Feder and M. Mihail, Balanced Matroids. Proc 24th Annual STOC 26 - 38 (1992).

★ [P]
 R. Pemantle, Towards a theory of negative dependence , Journal of Mathematical Physics 41 (2000), 1371–1390.
 Towards a theory of negative dependence

 [SW]
 P. D. Seymour and D. J. A. Welsh, Combinatorial applications of an inequality from statistical mechanics. Math. Proc. Camb. Phil. Soc. 77 485 - 495 (1975).
