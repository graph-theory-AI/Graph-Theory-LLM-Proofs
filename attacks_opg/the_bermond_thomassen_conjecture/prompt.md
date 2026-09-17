Attack the following open graph-theory problem.

Catalog id: the_bermond_thomassen_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_bermond_thomassen_conjecture/
Original entry: http://www.openproblemgarden.org/op/the_bermond_thomassen_conjecture
Problem attributed to: Bermond, Jean-Claude, Thomassen, Carsten (posted 2007-10-01)

=== Problem statement (OpenProblemGarden) ===
Title: The Bermond-Thomassen Conjecture
Conjecture For every positive integer $ k $ , every digraph with minimum out-degree at least $ 2k-1 $ contains $ k $ disjoint cycles.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is a simple observation when $ k=1 $ . It was proved by Thomassen~[Tho83] in 1983 when $ k=2 $ , and more recently the case $ k=3 $ was settled~[LPS07]. The bound offered would be optimal — just consider a symmetric complete graph on $ 2k-1 $ vertices. In 1996, Alon~[Alo96] proved that the statement is true with $ 2k-1 $ replaced by $ 64k $ . The conjecture was also verified for tournaments of minimum in-degree at least $ 2k-1 $ ~[BLS07]. Bang-Jensen et al. [BBT] made a stronger conjecture for digraph with sufficiently large girth. Conjecture For every integer $ g >1 $ , every digraph $ D $ with girth at least $ g $ and with minimum out-degree at least $ \frac{g}{g-1}k $ contains $ k $ disjoint cycles. The constant $ \frac{g}{g-1} $ is best possible. Indeed, for every integers $ p $ and $ g $ , consider the digraph $ D(g,p) $ on $ n = p(g − 1) + 1 $ vertices with vertex set $ \{x_1, \dots , x_n\} $ and arc set $ \{x_ix_j : j − i \mod n \in \{1,\dots p\}\} $ . It has girth $ g $ and out-degree $ p = \left \lfloor \frac{g}{g−1} k \right \rfloor $ . Moreover, for $ n = 0 \mod g $ , the digraph $ D(g,p) $ admits a partition into $ k $ vertex disjoint 3-cycles and no more. For g = 3, the first case of this conjecture which differs from Bermond-Thomassen Conjecture and which is not already known corresponds to the following question: Question Does every digraph D without 2-cycles and out-degree at least 6 admit four vertex disjoint cycles?

=== References listed by OpenProblemGarden ===
- [Alo96] N. Alon: Disjoint directed cycles, J. Combin. Theory Ser. B, 68(2):167--178, 1996. PDF
- [BBT] J. Bang-Jensen, S. Bessy and S. Thomassé, Disjoint 3-cycles in tournaments: a proof of the Bermond-Thomassen conjecture for tournaments, J. Graph Theory, to appear.
- *[BeTh81] J.-C. Bermond and C.~Thomassen: Cycles in digraphs---a survey, J. Graph Theory, 5(1):1--43, 1981. MathSciNet
- [BLS07] S.~Bessy, N.~Lichiardopol, and J.-S. Sereni: Two proofs of the {B}ermond-{T}homassen conjecture for tournaments with bounded minimum in-degree, Discrete Math., Special Issue dedicated to CS06, to appear.
- [LPS07] N.~Lichiardopol, A.~ P\'or, and J.-S. Sereni: A step towards the Bermond-Thomassen conjecture about disjoint cycles in digraphs, Submitted, 2007.
- [Tho83] C.~Thomassen, Disjoint cycles in digraphs, Combinatorica, 3(3-4):393--396, 1983. MathSciNet

=== Catalog page (statement + literature review) ===
The Bermond-Thomassen Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Bermond-Thomassen conjecture ($\delta^+(D) \geq 2k-1 \Rightarrow k$ disjoint cycles) remains open for general digraphs with $k \geq 4$. Significant post-2007 advances include a new shorter proof for $k=3$ (Bai and Manoussakis, 2018) and verification for triangle-free multipartite and 3-partite tournaments (Gutin et al., 2023). Notably, the stronger conjecture of Bang-Jensen, Bessy, and Thomassé on girth conditions (listed in the OPG discussion) was disproved by Bai and Manoussakis (2018).

 Cited literature (4)

 
 
 
partial On the number of vertex-disjoint cycles in digraphs
 (2018)
 

 
 Yandong Bai, Yannis Manoussakis · arXiv preprint · arXiv:1805.02999

Provides a new shorter proof of the Bermond-Thomassen conjecture for $k=3$, and disproves the stronger Bang-Jensen--Bessy--Thomassé conjecture on girth-conditioned vertex-disjoint cycles.
 

 
 
partial Two disjoint cycles in digraphs
 (2022)
 

 
 Mikołaj Lewandowski, Joanna Polcyn, Christian Reiher · arXiv preprint · arXiv:2205.10826

Characterises all outdegree sequences forcing $k$ vertex-disjoint cycles for $k \leq 2$, giving a complete answer for the two-cycle case that strengthens the Bermond-Thomassen bound.
 

 
 
partial Note on Disjoint Cycles in Multipartite Tournaments
 (2023)
 

 
 Gregory Gutin, Wei Li, Shujing Wang, Anders Yeo, Yacong Zhou · arXiv preprint · arXiv:2311.13369

Verifies the Bermond-Thomassen conjecture for the special classes of triangle-free multipartite tournaments and 3-partite tournaments.
 

 
 
partial Vertex-disjoint cycles of different lengths in tournaments
 (2024)
 

 
 Yandong Bai, Wenpei Jia · arXiv preprint · arXiv:2403.03692

Proves that every tournament with minimum outdegree $\geq 2k-1$ ($k \geq 5$) contains $k$ disjoint cycles with at least three of different lengths, a variant of the Bermond-Thomassen problem in the tournament setting.
 

 

 Reviewer notes. The conjecture is open for $k \geq 4$ in general digraphs. The Bang-Jensen--Bessy--Thomassé stronger conjecture (mentioned in the OPG discussion) was disproved by Bai--Manoussakis 2018. Publication venue details for arXiv papers could not be verified from fetches alone; all are listed as preprints. The 2022 Lewandowski--Polcyn--Reiher and 2023 Gutin et al. papers may have appeared in journals by now but this was not confirmed.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. For every positive integer $ k $ , every digraph with minimum out-degree at least $ 2k-1 $ contains $ k $ disjoint cycles.

Keywords:
cycles

Discussion

This conjecture is a simple observation when $ k=1 $ . It was proved by Thomassen~[Tho83] in 1983 when $ k=2 $ , and more recently the case $ k=3 $ was settled~[LPS07]. The bound offered would be optimal — just consider a symmetric complete graph on $ 2k-1 $ vertices. In 1996, Alon~[Alo96] proved that the statement is true with $ 2k-1 $ replaced by $ 64k $ . The conjecture was also verified for tournaments of minimum in-degree at least $ 2k-1 $ ~[BLS07]. Bang-Jensen et al. [BBT] made a stronger conjecture for digraph with sufficiently large girth. Conjecture For every integer $ g >1 $ , every digraph $ D $ with girth at least $ g $ and with minimum out-degree at least $ \frac{g}{g-1}k $ contains $ k $ disjoint cycles. The constant $ \frac{g}{g-1} $ is best possible. Indeed, for every integers $ p $ and $ g $ , consider the digraph $ D(g,p) $ on $ n = p(g − 1) + 1 $ vertices with vertex set $ \{x_1, \dots , x_n\} $ and arc set $ \{x_ix_j : j − i \mod n \in \{1,\dots p\}\} $ . It has girth $ g $ and out-degree $ p = \left \lfloor \frac{g}{g−1} k \right \rfloor $ . Moreover, for $ n = 0 \mod g $ , the digraph $ D(g,p) $ admits a partition into $ k $ vertex disjoint 3-cycles and no more. For g = 3, the first case of this conjecture which differs from Bermond-Thomassen Conjecture and which is not already known corresponds to the following question: Question Does every digraph D without 2-cycles and out-degree at least 6 admit four vertex disjoint cycles?

Bibliography

 [Alo96]
 N. Alon: Disjoint directed cycles, J. Combin. Theory Ser. B, 68(2):167--178, 1996. PDF
 PDF

 [BBT]
 J. Bang-Jensen, S. Bessy and S. Thomassé, Disjoint 3-cycles in tournaments: a proof of the Bermond-Thomassen conjecture for tournaments, J. Graph Theory, to appear.

★ [BeTh81]
 J.-C. Bermond and C.~Thomassen: Cycles in digraphs---a survey, J. Graph Theory, 5(1):1--43, 1981. MathSciNet
 MathSciNet

 [BLS07]
 S.~Bessy, N.~Lichiardopol, and J.-S. Sereni: Two proofs of the {B}ermond-{T}homassen conjecture for tournaments with bounded minimum in-degree, Discrete Math., Special Issue dedicated to CS06, to appear.

 [LPS07]
 N.~Lichiardopol, A.~ P\'or, and J.-S. Sereni: A step towards the Bermond-Thomassen conjecture about disjoint cycles in digraphs, Submitted, 2007.

 [Tho83]
 C.~Thomassen, Disjoint cycles in digraphs, Combinatorica, 3(3-4):393--396, 1983. MathSciNet
 MathSciNet

Related conjectures

 
 related to
 Splitting a digraph with minimum outdegree constraints
 partial
 The OPG context explicitly states only a case-level equivalence: the d=1 case of the splitting problem (Thomassen's f(1)=3) is equivalent to the k=2 case of Bermond-Thomassen (min outdegree 3 gives 2 disjoint cycles); indeed a bipartition with both parts of min outdegree >=1 yields two disjoint cycles, and conversely per Thomassen. But the full statements do not imply each other: for general d, splitting into two parts of min outdegree d says nothing about packing k disjoint cycles under the specific 2k-1 bound, and k disjoint cycles do not yield an outdegree-preserving bipartition. The problems are thematically linked with one coinciding special case, so related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
