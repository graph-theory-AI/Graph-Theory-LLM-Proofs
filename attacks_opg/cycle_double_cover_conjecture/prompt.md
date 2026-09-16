Attack the following open graph-theory problem.

Catalog id: cycle_double_cover_conjecture
Source: OpenProblemGarden (importance: Outstanding ✭✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/cycle_double_cover_conjecture/
Original entry: http://www.openproblemgarden.org/op/cycle_double_cover_conjecture
Problem attributed to: Seymour, Paul D., Szekeres, George (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Cycle double cover conjecture
Conjecture For every graph with no bridge , there is a list of cycles so that every edge is contained in exactly two.

=== Discussion / context (OpenProblemGarden) ===
This beautiful conjecture was made independently by Szekeres and Seymour in the 70's and is now widely considered to be among the most important open problems in graph theory. Note the similarity between this conjecture and the Berge-Fulkerson conjecture on perfect matchings. Attempts to prove this conjecture have lead to a variety of conjectured strengthenings, which appear on other pages. See: The circular embedding conjecture , The five cycle double cover conjecture , The faithful cover conjecture , and Decomposing Eulerian graphs . If a graph $ G $ has a nowhere-zero 4-flow then it follows from a result of Tutte that $ G $ satisfies the above conjecture. Thus, by Jaeger's 4-flow theorem [J], the above conjecture is true for every 4-edge-connected graph. A cubic graph has a nowhere-zero 4-flow if and only if it is 3- edge-colorable , so the above conjecture is also true for 3-edge-colorable cubic graphs. In general, it follows from vertex splitting arguments that problem may be reduced to cubic graphs which are not 3-edge-colorable. For a general graph $ G $ with no cut-edge, Bermond, Jackson and Jaeger [BJJ] used Jaeger's 8-flow theorem [J] to prove that $ G $ has a list of circuits so that every edge is contained in exactly four. Fan [F] used Seymour's 6-flow theorem [S81] to prove that G has a list of circuits so that every edge is contained in exactly six. Let $ G $ be a directed graph and let $ C $ be a circuit (not necessarily a directed circuit) of $ G $ . If we choose a direction to travel around $ C $ , then every edge of $ C $ is either traversed forward or backward. The following strengthening of the cycle double cover conjecture takes directions into account. Conjecture (The oriented cycle double cover conjecture) If $ G $ is an orientation of a bridgeless graph, then there is a list $ L $ of circuits of $ G $ with directions so that every edge of $ G $ is traversed forward by exactly one circuit in $ L $ and backward by exactly one circuit in $ L $ . Tutte also showed that every graph with a nowhere-zero 4-flow satisfies this conjecture. Thus, as above this conjecture is true for 4-edge-connected graphs and for 3-edge-colorable cubic graphs. It was mentioned above that for a general graph $ G $ with no bridge, there is a list of circuits containing every edge exactly four times. By taking two copies of each circuit in this list and giving them opposite directions, we have a list of circuits so that every edge is traversed forward and backward exactly four times. Luis Goddyn and I (M. DeVos) have observed that the same ideas used in Fan's article [Fa] can be used to construct a list of circuits with directions so that every edge is traversed forward and backward exactly three times. The following natural question seems to be open. Conjecture (The oriented cycle four cover conjecture) If $ G $ is an orientation of a bridgeless graph, then there is a list $ L $ of circuits of $ G $ with directions so that every edge of $ G $ is traversed forward by exactly two circuits in $ L $ and backward by exactly two circuits in $ L $ . Since every graph with a nowhere-zero 4-flow has a list of circuits with directions traversing every edge forward and backward exactly once, the above conjecture would follow from The three 4-flows conjecture.

=== References listed by OpenProblemGarden ===
- [AGZ] B. Alspach, L. Goddyn, and C-Q Zhang, Graphs with the circuit cover property, Trans. Amer. Math. Soc., 344 (1994), 131-154. MathSciNet
- [BJJ] J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MRhref{0735197}
- [DJS] M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
- [F] G. Fan, Integer flows and cycle covers, J. Combinatorial Theory Ser. B 54 (1992), 113-122. MathSciNet
- [FZ] G. Fan and C.Q. Zhang, Circuit decompositions of Eulerian graphs, J. Combinatorial Theory Ser. B 78 (2000), 1-23. MathSciNet
- [FG] X. Fu and L. Goddyn, Matroids with the circuit cover property, Europ. J. Combinatorics 20 (1999), 61-73. MathSciNet
- [J] F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216. MathSciNet
- [Ki] P.A. Kilpatrick, Tutte's First Colour-Cycle Conjecture, Thesis, Cape Town (1975).
- [Sz] G. Szekeres, Polyhedral decompositions of cubic graphs. Bull. Austral. Math. Soc. 8, 367-387. MathSciNet
- [S91] P.D. Seymour, Nowhere-Zero 6-Flows, J. Combinatorial Theory Ser. B 30 (1981) 130-135. MathSciNet
- [S79] P.D. Seymour, Sums of circuits in Graph Theory and Related Topics edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York/Berlin (1979), 341-355. MathSciNet
- [S95] P.D. Seymour, Nowhere-Zero Flows, in Handbook of Combinatoircs, edited by R. Graham, M. Grotschel and L. Lovasz, (1995) 289-299. MathSciNet
- [T54] W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
- [T66] W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet

=== Catalog page (statement + literature review) ===
Cycle double cover conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Cycle Double Cover Conjecture remains open; no complete proof has been accepted by the mathematical community, and several claimed arXiv proofs (2012, 2015, 2018) were later found to contain errors. Post-2007 progress includes a proof of Jaeger's directed version for lean fork-graphs, exponential lower bounds for the counting version for planar cubic graphs, and approximate results giving nontrivial upper bounds on singular edges in cubic graph embeddings.

 Cited literature (4)

 
 
 
partial Directed Cycle Double Cover Conjecture: Fork Graphs
 (2013)
 

 
 Andrea Jiménez, Martin Loebl · arXiv preprint · arXiv:1310.5539

Proves Jaeger's directed cycle double cover conjecture for lean fork-graphs, an inductively defined class of cubic bridgeless graphs whose members contain subdivisions of all cubic bridgeless graphs as induced subgraphs.
 

 
 
partial Counting circuit double covers
 (2023)
 

 
 Radek Hušek, Robert Šámal · Journal of Graph Theory · arXiv:2303.10615 · doi:10.1002/jgt.23187

Proves an exponential lower bound on the number of circuit double covers for planar bridgeless cubic graphs and an almost-exponential lower bound for graphs with surface embedding representativity at least 4, establishing the first counting results toward CDC.
 

 
 
partial Approximate cycle double cover
 (2025)
 

 
 Babak Ghanbari, Robert Šámal · arXiv preprint · arXiv:2511.07285

Establishes nontrivial upper bounds on the minimum number of singular edges in a 2-cell embedding of a cubic graph (CDC being equivalent to achieving zero singular edges), giving an approximate version of the conjecture with efficient algorithms.
 

 
 
partial Facial diagrams and cycle double cover
 (2026)
 

 
 Babak Ghanbari, Robert Šámal · arXiv preprint · arXiv:2605.01410

Studies circular 2-cell embeddings of cubic graphs via twist operations on edges, derives bounds on singular edges, and develops analytical tools further advancing the approximate CDC program.
 

 

 Reviewer notes. Three arXiv preprints claim to prove the CDC conjecture (1202.0569, 1510.02075, 1811.08719); the 2015 paper (Radcliffe, arXiv:1510.02075) has a confirmed error noted on its own arXiv page. The Fischer 2023 paper (arXiv:2307.06649) claims to prove CDC for simple bridgeless triangle-free cubic graphs using percolation theory, but remains an unreviewed preprint as of March 2025. Wikipedia and the mathematical community confirm the conjecture is still open. Any minimal counterexample is known to have girth at least 12.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. For every graph with no bridge , there is a list of cycles so that every edge is contained in exactly two.

Keywords:
cover · cycle

Discussion

This beautiful conjecture was made independently by Szekeres and Seymour in the 70's and is now widely considered to be among the most important open problems in graph theory. Note the similarity between this conjecture and the Berge-Fulkerson conjecture on perfect matchings. Attempts to prove this conjecture have lead to a variety of conjectured strengthenings, which appear on other pages. See: The circular embedding conjecture , The five cycle double cover conjecture , The faithful cover conjecture , and Decomposing Eulerian graphs . If a graph $ G $ has a nowhere-zero 4-flow then it follows from a result of Tutte that $ G $ satisfies the above conjecture. Thus, by Jaeger's 4-flow theorem [J], the above conjecture is true for every 4-edge-connected graph. A cubic graph has a nowhere-zero 4-flow if and only if it is 3- edge-colorable , so the above conjecture is also true for 3-edge-colorable cubic graphs. In general, it follows from vertex splitting arguments that problem may be reduced to cubic graphs which are not 3-edge-colorable. For a general graph $ G $ with no cut-edge, Bermond, Jackson and Jaeger [BJJ] used Jaeger's 8-flow theorem [J] to prove that $ G $ has a list of circuits so that every edge is contained in exactly four. Fan [F] used Seymour's 6-flow theorem [S81] to prove that G has a list of circuits so that every edge is contained in exactly six. Let $ G $ be a directed graph and let $ C $ be a circuit (not necessarily a directed circuit) of $ G $ . If we choose a direction to travel around $ C $ , then every edge of $ C $ is either traversed forward or backward. The following strengthening of the cycle double cover conjecture takes directions into account. Conjecture (The oriented cycle double cover conjecture) If $ G $ is an orientation of a bridgeless graph, then there is a list $ L $ of circuits of $ G $ with directions so that every edge of $ G $ is traversed forward by exactly one circuit in $ L $ and backward by exactly one circuit in $ L $ . Tutte also showed that every graph with a nowhere-zero 4-flow satisfies this conjecture. Thus, as above this conjecture is true for 4-edge-connected graphs and for 3-edge-colorable cubic graphs. It was mentioned above that for a general graph $ G $ with no bridge, there is a list of circuits containing every edge exactly four times. By taking two copies of each circuit in this list and giving them opposite directions, we have a list of circuits so that every edge is traversed forward and backward exactly four times. Luis Goddyn and I (M. DeVos) have observed that the same ideas used in Fan's article [Fa] can be used to construct a list of circuits with directions so that every edge is traversed forward and backward exactly three times. The following natural question seems to be open. Conjecture (The oriented cycle four cover conjecture) If $ G $ is an orientation of a bridgeless graph, then there is a list $ L $ of circuits of $ G $ with directions so that every edge of $ G $ is traversed forward by exactly two circuits in $ L $ and backward by exactly two circuits in $ L $ . Since every graph with a nowhere-zero 4-flow has a list of circuits with directions traversing every edge forward and backward exactly once, the above conjecture would follow from The three 4-flows conjecture.

Bibliography

 [AGZ]
 B. Alspach, L. Goddyn, and C-Q Zhang, Graphs with the circuit cover property , Trans. Amer. Math. Soc., 344 (1994), 131-154. MathSciNet
 Graphs with the circuit cover property · MathSciNet

 [BJJ]
 J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MRhref{0735197}

 [DJS]
 M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
 Cut-coloring and circuit covering

 [F]
 G. Fan, Integer flows and cycle covers, J. Combinatorial Theory Ser. B 54 (1992), 113-122. MathSciNet
 MathSciNet

 [FZ]
 G. Fan and C.Q. Zhang, Circuit decompositions of Eulerian graphs, J. Combinatorial Theory Ser. B 78 (2000), 1-23. MathSciNet
 MathSciNet

 [FG]
 X. Fu and L. Goddyn, Matroids with the circuit cover property , Europ. J. Combinatorics 20 (1999), 61-73. MathSciNet
 Matroids with the circuit cover property · MathSciNet

 [J]
 F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216. MathSciNet
 MathSciNet

 [Ki]
 P.A. Kilpatrick, Tutte's First Colour-Cycle Conjecture, Thesis, Cape Town (1975).

 [Sz]
 G. Szekeres, Polyhedral decompositions of cubic graphs. Bull. Austral. Math. Soc. 8, 367-387. MathSciNet
 MathSciNet

 [S91]
 P.D. Seymour, Nowhere-Zero 6-Flows, J. Combinatorial Theory Ser. B 30 (1981) 130-135. MathSciNet
 MathSciNet

 [S79]
 P.D. Seymour, Sums of circuits in Graph Theory and Related Topics edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York/Berlin (1979), 341-355. MathSciNet
 MathSciNet

 [S95]
 P.D. Seymour, Nowhere-Zero Flows, in Handbook of Combinatoircs, edited by R. Graham, M. Grotschel and L. Lovasz, (1995) 289-299. MathSciNet
 MathSciNet

 [T54]
 W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
 MathSciNet

 [T66]
 W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 (m,n)-cycle covers
 partial
 Both conjectures quantify over the same class (bridgeless graphs). A (5,2)-cycle-cover is 5 binary cycles (even subgraphs) covering each edge exactly twice; since every binary cycle decomposes into edge-disjoint circuits, decomposing each of the 5 yields a list of circuits covering every edge exactly twice, i.e., a cycle double cover. The source's OPG context states this explicitly: 'the above conjecture is a strengthening of the cycle double cover conjecture.' Direction as claimed.
 

 
 implied by
 Cycle Double Covers Containing Predefined 2-Regular Subgraphs
 partial
 CDC reduces to bridgeless cubic graphs (stated in the target's OPG context), and a minimal cubic counterexample is 3-connected by the standard 2-cut reduction. By Tutte's theorem, a 3-connected graph has a non-separating induced circuit C. If C is Hamiltonian, the cubic graph is 3-edge-colorable (cubic graphs have even order, so the Hamiltonian cycle is even) and therefore has a CDC. Otherwise G−V(C) is connected and, since G is cubic and C induced, each vertex of C sends exactly one edge to G−V(C), so G−E(C) is connected; applying the source conjecture with S = C (a connected 2-regular subgraph of the 2-connected G) yields a CDC of G, contradicting minimality. Every step is a classical theorem; the chain is rigorous.
 

 
 implied by
 Decomposing eulerian graphs
 partial
 DIRECTION FLIPPED from the seed edge (which listed CDC as source). The Decomposing-Eulerian-graphs page states explicitly: "the above conjecture would imply the cycle double cover conjecture", and gives the argument: CDC reduces to 3-edge-connected graphs; replacing each edge of such a G by two parallel edges yields a 6-edge-connected Eulerian graph G' with the 2-transition system P pairing the parallel copies at each endpoint; a compatible decomposition of (G',P) uses at most one copy of each parallel pair per cycle, so projecting back to G gives a list of cycles covering every edge exactly twice, i.e., a CDC. The converse is not claimed anywhere, so this is a one-way implication: Decomposing Eulerian graphs is the stronger statement.
 

 
 implied by
 Decomposing eulerian graphs
 partial
 Explicitly stated in the source context with a valid reduction: given a 3-edge-connected G, replace each edge by two parallel edges to obtain G', which is Eulerian and 6-edge-connected, with the 2-transition system P pairing the parallel copies at each endpoint; a compatible decomposition of (G',P) uses at most one of each parallel pair per cycle at each vertex, so it projects to a list of cycles of G covering every edge exactly twice, i.e. a CDC of G. Since the CDC conjecture reduces (by standard vertex-splitting/cut arguments) to 3-edge-connected graphs, the Eulerian decomposition conjecture implies CDC. Hypothesis class checks out: 6-edge-connectivity of G' follows from 3-edge-connectivity of G because doubling edges doubles every edge cut.
 

 
 implied by
 Faithful cycle covers
 open
 CDC is the p≡2 instance of the faithful cover conjecture. For bridgeless G, p≡2 is admissible: it is nonnegative, p(S)=2|S| is even for every edge-cut, and since bridgelessness forces |S|≥2 for every edge-cut, p(e)=2 ≤ |S| = p(S)/2. All p(e)=2 are even, so the hypothesis of the faithful cover conjecture holds, and a faithful cover of (G,2) is exactly a list of cycles containing each edge twice, i.e., a CDC. (A bridge e would make {e} a cut violating condition (iii), so the bridgeless restriction is exactly right.) The source's own OPG context states this equivalence of the p≡2 case with CDC explicitly.
 

 
 implied by
 Petersen coloring conjecture
 partial
 Via reformulation (2) of the Petersen coloring conjecture (every bridgeless graph has a cycle-continuous map to the Petersen graph P), pulling back a double cover of P by 5 even subgraphs gives 5 even subgraphs of G covering each edge exactly twice — a (5,2)-cycle cover, hence in particular a cycle double cover. The hypothesis class (all bridgeless graphs) matches CDC exactly. This is Jaeger's classical implication; the CDC target page lists the five cycle double cover conjecture (implied by Petersen coloring per the source's OPG context) among its strengthenings.
 

 
 implied by
 Strong 5-cycle double cover conjecture
 partial
 Strong 5-CDC applied to any circuit of a bridgeless cubic graph yields a 5-cycle double cover, hence a CDC, of every bridgeless cubic graph (every such nonempty graph contains a circuit). The CDC conjecture for general bridgeless graphs reduces to cubic graphs via vertex splitting, as stated explicitly in the target's OPG context ('problem may be reduced to cubic graphs'). Decomposing the five even subgraphs into edge-disjoint circuits gives the required list of cycles covering each edge exactly twice. Direction as claimed (source is a double strengthening of CDC, per its own context).
 

 
 implied by
 The circular embedding conjecture
 partial
 The source's OPG context states the implication verbatim: 'This conjecture implies the cycle double cover conjecture, since the list of cycles which bound faces covers each edge exactly twice.' The hypothesis-class gap (2-connected vs bridgeless) is closed by block decomposition: every block of a bridgeless graph is 2-connected (no block is a cut-edge), and the union of the face-boundary CDCs of the blocks is a CDC of the whole graph. Direction as claimed; note the converse is known only for cubic graphs (glue discs to the cycles of a CDC), so the relation is a strict strengthening in general, not an equivalence.
 

 
 related to
 Grunbaum's Conjecture
 disproved
 The source context compares Grunbaum's conjecture with the ORIENTABLE cycle double cover conjecture, and explicitly as a contrast, not an implication: Grunbaum's says every orientable embedding of a snark has a dual loop or parallel edge, while OCDC says some orientable embedding of every snark has no dual loop — near-opposite assertions about the same objects, neither implying the other. The target here is moreover the plain CDC, one step further removed (OCDC implies CDC, but Grunbaum's conjecture implies neither). Grunbaum's conjecture is in fact disproved (Kochol 2009: snarks with polyhedral embeddings in orientable surfaces) while CDC stands open, consistent only with the absence of implication in the other direction too. Twin conjectures about embedding snarks in orientable surfaces: related_only.
 

 
 related to
 The Berge-Fulkerson conjecture
 partial
 The CDC page only says 'Note the similarity between this conjecture and the Berge-Fulkerson conjecture' - an explicit analogy, not an implication. No implication is known in either direction: BF gives (via complements of the 6 matchings) six 2-factors covering each edge exactly 4 times, i.e. a cycle FOUR cover, which is already a theorem (Bermond-Jackson-Jaeger) and does not yield a double cover; conversely CDC says nothing about perfect matchings of cubic graphs. Both are known consequences of the common strengthening (Petersen coloring conjecture), which makes them thematically linked siblings, not logically comparable.
 

 
 related to
 The three 4-flows conjecture
 open
 The truncated mention is misleading: fetching the full CDC page shows 'the above conjecture would follow from The three 4-flows conjecture' refers to the ORIENTED CYCLE FOUR COVER conjecture, a separate weaker statement hosted on the same page, not the CDC node's statement. The three 4-flows page confirms: 'it implies the Orientable cycle four cover conjecture' (each edge lies in exactly two of the graphs G\A_i, each having an orientable CDC via its nowhere-zero 4-flow, summing to a 4-cover). A cycle four cover does not give a double cover, and no implication between three 4-flows and CDC proper is known in either direction; both reduce to non-3-edge-colorable cubic graphs and both follow from Petersen coloring, but that makes them related family members only.
 

 
 related to
 The three 4-flows conjecture
 open
 The mention is the same analogy sentence (both reduce to non-3-edge-colorable cubic graphs). The genuine implication stated in the context goes from three-4-flows to the Orientable cycle FOUR cover conjecture, not to CDC: each G\A_i has a nowhere-zero 4-flow, hence an orientable cycle double cover, and since each edge lies in exactly two of the three subgraphs G\A_i, the union covers every edge exactly four times. A cycle 4-cover is already known unconditionally (Bermond-Jackson-Jaeger via Jaeger's 8-flow theorem), so this route does not give a double cover, and no implication between three-4-flows and CDC is stated or standard in either direction. Hence related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
