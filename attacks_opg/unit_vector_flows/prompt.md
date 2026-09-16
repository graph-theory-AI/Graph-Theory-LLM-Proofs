Attack the following open graph-theory problem.

Catalog id: unit_vector_flows
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/unit_vector_flows/
Original entry: http://www.openproblemgarden.org/op/unit_vector_flows
Problem attributed to: Jain, Kamal (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Unit vector flows
Conjecture For every graph $ G $ without a bridge , there is a flow $ \phi : E(G) \rightarrow S^2 = \{ x \in {\mathbb R}^3 : |x| = 1 \} $ . Conjecture There exists a map $ q:S^2 \rightarrow \{-4,-3,-2,-1,1,2,3,4\} $ so that antipodal points of $ S^2 $ receive opposite values, and so that any three points which are equidistant on a great circle have values which sum to zero.

=== Discussion / context (OpenProblemGarden) ===
The main interest in these two conjectures is that together they imply Tutte's 5-flow conjecture . This follows easily from the fact that the 5-flow conjecture can be reduced to cubic graphs without bridges, and for such a graph $ G $ , the composition of the maps $ \phi $ and $ q $ (given by the above conjectures) is a nowhere-zero 5-flow. There are a couple of easy partial results toward the first conjecture which follow from well-known flow/cycle-cover results. First, Tutte showed that every graph with a nowhere-zero 4-flow has a list of three 2-flows $ f_1,f_2,f_3 : E(G) \to \{-1,0,1\} $ so that every edge is in the support of exactly two of these flows. Combining these flows and normalizing appropriately gives an $ S^2 $ -flow. Bermond, Jackson, and Jaeger [BJJ] showed that every graph with no bridge has a list of seven 2-flows so that every edge is in the support of exactly four of these flows. Combining these and normalizing appropriately gives an $ S^6 $ -flow. It seems likely that a graph has an $ S^1 $ -flow if and only if it has a nowhere-zero 3-flow. The "if" direction of this implication isn't hard to show and the "only if" direction looks quite possible. A dual concept to that of a flow is that of a tension. Observe that a graph $ G $ has a $ S^n $ tension if and only if can be embedded in $ {\mathbb R}^{n+1} $ so that all edges are unit length line segments. Such embeddings have received some attention over the years. In particular, there is considerable interest in finding the best possible upper bound on the chromatic number of graphs which embed in $ {\mathbb R}^2 $ in this manner. This is Hadwinger-Nelson problem on coloring the plane.

=== References listed by OpenProblemGarden ===
- [BJJ] J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MRhref{0735197}
- [T54] W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
- [T66] W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet

=== Catalog page (statement + literature review) ===
Unit vector flows — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Jain's second conjecture—that a map $q:S^2\to\{-4,-3,-2,-1,1,2,3,4\}$ with the required properties exists—was disproved in March 2026 by Ulyanov, who exhibited explicit point sets on $S^2$ that force the additional values $\pm 5$. The first conjecture (every bridgeless graph admits a flow $\phi:E(G)\to S^2$) remains open, though partial results since 2023 establish geometric characterisations and bounds on related $d$-dimensional flow numbers.

 Cited literature (4)

 
 
 
partial On $d$-dimensional nowhere-zero $r$-flows on a graph
 (2023)
 

 
 Davide Mattiolo, Giuseppe Mazzuoccolo, Jozef Rajník, Gloria Tabarelli · arXiv preprint · arXiv:2304.14231

Proves $\phi_2(G)\le 1+\sqrt{5}$ for all bridgeless graphs and shows the oriented 5-cycle double cover conjecture would imply the bound $\phi_2(G)\le\tau^2$ (golden ratio squared), giving the first quantitative upper bounds for 2-dimensional unit-vector flows.
 

 
 
partial Geometric description of $d$-dimensional flows of a graph
 (2025)
 

 
 Davide Mattiolo, Giuseppe Mazzuoccolo, Jozef Rajník, Gloria Tabarelli · arXiv preprint · arXiv:2510.19411

Establishes that existence of a suitable cycle double cover is equivalent to the graph admitting a geometrically constructed $(r,d)$-nowhere-zero flow, linking the first unit-vector flows conjecture to the cycle double cover programme.
 

 
 
partial 2-dimensional unit vector flows
 (2026)
 

 
 Hussein Houdrouge, Bobby Miraftab, Pat Morin · arXiv preprint · arXiv:2602.21526 · doi:10.48550/arXiv.2602.21526

Gives a geometric characterisation of cubic graphs that admit an $S^2$-flow (i.e., satisfy Jain's first conjecture) and shows this class is closed under specific composition operations, extending algebraic rank methods from $S^1$-flows to $S^2$-flows.
 

 
 
counterexample Graph Puzzles II.1: Counterexamples to Jain's Second Unit Vector Flows Conjecture
 (2026)
 

 
 Nikolay Ulyanov · arXiv preprint · arXiv:2603.23328

Constructs explicit point sets on $S^2$ (including one derived from the icosidodecahedron) that are counterexamples to Jain's second conjecture: these sets require the additional values $\pm 5$, so no map $q:S^2\to\{-4,-3,-2,-1,1,2,3,4\}$ with the required antipodal and great-circle-sum properties exists.
 

 

 Reviewer notes. Jain's second conjecture is definitively refuted (Ulyanov 2026), closing off the specific two-conjecture route to Tutte's 5-flow conjecture. Jain's first conjecture (S²-flows for all bridgeless graphs) remains open and is the active focus of the 2026 Houdrouge–Miraftab–Morin preprint. The 2023 and 2025 Mattiolo et al. papers work in the more general (r,d)-nowhere-zero flow setting rather than targeting the S² conjecture directly. No journal-published versions of the 2023–2026 arXiv papers were confirmed.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. For every graph $ G $ without a bridge , there is a flow $ \phi : E(G) \rightarrow S^2 = \{ x \in {\mathbb R}^3 : |x| = 1 \} $ .

Conjecture. There exists a map $ q:S^2 \rightarrow \{-4,-3,-2,-1,1,2,3,4\} $ so that antipodal points of $ S^2 $ receive opposite values, and so that any three points which are equidistant on a great circle have values which sum to zero.

Keywords:
nowhere-zero flow

Discussion

The main interest in these two conjectures is that together they imply Tutte's 5-flow conjecture . This follows easily from the fact that the 5-flow conjecture can be reduced to cubic graphs without bridges, and for such a graph $ G $ , the composition of the maps $ \phi $ and $ q $ (given by the above conjectures) is a nowhere-zero 5-flow. There are a couple of easy partial results toward the first conjecture which follow from well-known flow/cycle-cover results. First, Tutte showed that every graph with a nowhere-zero 4-flow has a list of three 2-flows $ f_1,f_2,f_3 : E(G) \to \{-1,0,1\} $ so that every edge is in the support of exactly two of these flows. Combining these flows and normalizing appropriately gives an $ S^2 $ -flow. Bermond, Jackson, and Jaeger [BJJ] showed that every graph with no bridge has a list of seven 2-flows so that every edge is in the support of exactly four of these flows. Combining these and normalizing appropriately gives an $ S^6 $ -flow. It seems likely that a graph has an $ S^1 $ -flow if and only if it has a nowhere-zero 3-flow. The "if" direction of this implication isn't hard to show and the "only if" direction looks quite possible. A dual concept to that of a flow is that of a tension. Observe that a graph $ G $ has a $ S^n $ tension if and only if can be embedded in $ {\mathbb R}^{n+1} $ so that all edges are unit length line segments. Such embeddings have received some attention over the years. In particular, there is considerable interest in finding the best possible upper bound on the chromatic number of graphs which embed in $ {\mathbb R}^2 $ in this manner. This is Hadwinger-Nelson problem on coloring the plane.

Bibliography

 [BJJ]
 J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MRhref{0735197}

 [T54]
 W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
 MathSciNet

 [T66]
 W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 5-flow conjecture
 partial
 The source node contains both conjectures of the OPG entry, whose context states verbatim that 'together they imply Tutte's 5-flow conjecture.' The reduction is standard: the 5-flow conjecture reduces to bridgeless cubic graphs; for such G, an S²-flow φ gives at each vertex three unit vectors summing to zero, hence coplanar at mutual 120° angles, i.e., equidistant on a great circle. Composing φ with the map q of the second conjecture yields values in {±1,...,±4} summing to zero at every vertex (antipodality makes this orientation-consistent), i.e., a nowhere-zero 5-flow. Note the implication needs both conjectures of the entry, which the source node bundles.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
