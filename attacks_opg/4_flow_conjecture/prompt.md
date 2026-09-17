Attack the following open graph-theory problem.

Catalog id: 4_flow_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/4_flow_conjecture/
Original entry: http://www.openproblemgarden.org/op/4_flow_conjecture
Problem attributed to: Tutte, William T. (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: 4-flow conjecture
Conjecture Every bridgeless graph with no Petersen minor has a nowhere-zero 4-flow.

=== Discussion / context (OpenProblemGarden) ===
It is a consequence of a theorem of Tutte that a cubic graph has a nowhere-zero 4-flow if and only if it is 3- edge-colorable . Thus, the 4-flow conjecture implies that every bridgeless cubic graph with no Petersen minor is 3-edge-colorable (another conjecture of Tutte). Note that the Four Color Theorem is equivalent to the assertion that planar cubic graphs without bridges are 3-edge-colorable, so even this weaker conjecture is a strengthening of the Four Color Theorem. This weaker conjecture was recently proved by Robertson, Seymour, and Thomas [RST]. Their proof involves a reduction to the case of nearly planar graphs, and then an application of 4-color-theorem type techniques (computer assisted) to color these graphs. Most conjectures about flows can be easily reduced to the case of cubic graphs by splitting arguments. The idea is to take a vertex $ v $ incident with edges $ e_1,\ldots,e_k $ and "split" $ v $ , that is, replace $ v $ by two new vertices $ v_1 $ and $ v_2 $ , and for every edge $ e_i $ join it to either $ v_1 $ or $ v_2 $ (sometimes the edge $ v_1 v_2 $ is also added). For instance, this technique can be used to reduce the general 5-flow conjecture down to the special case of cubic graphs. Unfortunately, that technique does not apply here, since splitting a vertex may introduce a Petersen minor. Petersen's graph is not an apex graph (deleting any vertex still leaves a nonplanar graph). It follows that no apex graph can have a Petersen minor, so the above conjecture implies that every bridgeless apex graph has a nowhere-zero 4-flow. By splitting the vertices which lie in the plane this can be reduced to the special case where all vertices which lie in the plane have degree 3. This is then equivalent to the following old conjecture of Gr\"{o}tzsch. Conjecture (Gr\"{o}tzsch) If $ G $ is a 2-connected connected planar graph of maximum degree 3, then $ G $ is 3-edge-colorable unless it has exactly one vertex of degree 2.

=== References listed by OpenProblemGarden ===
- [AH] K. Appel, W. Haken, Every Planar Map is Four Colorable, Bull. Amer. Math. Soc. 82 (1976) 711-712. MathSciNet
- [RSST] N. Robertson, D.P. Sanders, P.D. Seymour, and R. Thomas, A New Proof of the Four-Color Theorem, Electron. Res. Announc., Am. Math. Soc. 02, no 1 (1996) 17-25. MathSciNet
- [RST] N. Robertson, P.D. Seymour, and R. Thomas, Tutte's edge-colouring conjecture. J. Combin. Theory Ser. B 70 (1997), no. 1, 166--183. MathSciNet
- [Tut54] W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
- [Tut66] W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet

=== Catalog page (statement + literature review) ===
4-flow conjecture — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 Tutte's 4-flow conjecture remains open for general bridgeless graphs. For cubic graphs the equivalent snark conjecture was announced as proved by Robertson–Sanders–Seymour–Thomas in 1999, but the complete proof is still unpublished; two published steps (2016 and 2019) establish the doublecross and structural minor cases needed for the reduction. No breakthrough on the non-cubic general case has been reported.

 Cited literature (5)

 
 
 
partial Three-edge-colouring doublecross cubic graphs
 (2016)
 

 
 Katherine Edwards, Daniel P. Sanders, Paul Seymour, Robin Thomas · Journal of Combinatorial Theory, Series B · arXiv:1411.4352

Proves every two-edge-connected doublecross cubic graph is 3-edge-colourable, completing the doublecross case in the reduction strategy for Tutte's snark conjecture (the cubic-graph case of the 4-flow conjecture); JCTB 119 (2016) 66–95.
 

 
 
partial Excluded minors in cubic graphs
 (2019)
 

 
 Neil Robertson, Paul Seymour, Robin Thomas · Journal of Combinatorial Theory, Series B · arXiv:1403.2118

Establishes a structural characterisation of cubic graphs excluding Petersen minors, serving as a key building block in the announced but still-unpublished full proof of Tutte's snark conjecture; JCTB 138 (2019) 219–285.
 

 
 
partial Exponentially many nowhere-zero $Z_3$-, $Z_4$-, and $Z_6$-flows
 (2019)
 

 
 Zdeněk Dvořák, Bojan Mohar, Robert Šámal · arXiv preprint · arXiv:1708.09579

Proves counting analogues in related settings: at least $2^{n/7}$ nowhere-zero $Z_2\times Z_3$-flows in 3-edge-connected graphs ($2^{2(m-n)/9}$ for 2-edge-connected), at least $2^{n/250}$ nowhere-zero $Z_2^2$-flows in 4-edge-connected graphs, and at least $2^{(n-2)/12}$ nowhere-zero $Z_3$-flows in 6-edge-connected graphs. These are exponential counting versions of the existence theorems that are partial results toward Tutte's conjectures, but do not directly resolve them.
 

 
 
partial Three-edge-coloring (Tait coloring) cubic graphs on the torus: A proof of Grünbaum's conjecture
 (2025)
 

 
 Yuta Inoue, Ken-ichi Kawarabayashi, Atsuyuki Miyashita, Bojan Mohar, Tomohiro Sonobe · arXiv preprint · arXiv:2505.07002

Proves that every 2-edge-connected graph embedded in the torus admits a nowhere-zero 4-flow unless it is Petersen-like (in which case it provably does not); this vastly strengthens the Tutte 4-Flow Conjecture on the torus because almost all toroidal graphs contain a Petersen minor but almost none are Petersen-like.
 

 
 
partial Three-edge-coloring projective planar cubic graphs: A generalization of the Four Color Theorem
 (2024)
 

 
 Yuta Inoue, Ken-ichi Kawarabayashi, Atsuyuki Miyashita, Bojan Mohar, Tomohiro Sonobe · arXiv preprint · arXiv:2405.16586

Proves a strengthening of the conjecture for the projective plane: a 2-connected graph embedded in the projective plane admits a nowhere-zero 4-flow if and only if it is not Petersen-like (Theorem 1.6 and Corollary 1.3).
 

 

 Reviewer notes. The Wang–Zhang paper 'Nowhere-zero 4-flow in almost Petersen-minor free graphs' (Discrete Mathematics, ~2008, ScienceDirect pii/S0012365X07009673) appeared in search results but could not be verified via WebFetch (403 errors from ScienceDirect and ResearchGate); it is excluded from since_posted. The Robertson–Seymour–Thomas arXiv preprint 1403.2118 was submitted in 2014 but published in JCTB 138 (2019) per Wikipedia; arXiv fetch did not confirm the journal. The complete snark-theorem proof (implying the cubic case of the 4-flow conjecture) has been announced since 1999 but remains unpublished as of 2026.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. Every bridgeless graph with no Petersen minor has a nowhere-zero 4-flow.

Keywords:
minor · nowhere-zero flow · Petersen graph

Discussion

It is a consequence of a theorem of Tutte that a cubic graph has a nowhere-zero 4-flow if and only if it is 3- edge-colorable . Thus, the 4-flow conjecture implies that every bridgeless cubic graph with no Petersen minor is 3-edge-colorable (another conjecture of Tutte). Note that the Four Color Theorem is equivalent to the assertion that planar cubic graphs without bridges are 3-edge-colorable, so even this weaker conjecture is a strengthening of the Four Color Theorem. This weaker conjecture was recently proved by Robertson, Seymour, and Thomas [RST]. Their proof involves a reduction to the case of nearly planar graphs, and then an application of 4-color-theorem type techniques (computer assisted) to color these graphs. Most conjectures about flows can be easily reduced to the case of cubic graphs by splitting arguments. The idea is to take a vertex $ v $ incident with edges $ e_1,\ldots,e_k $ and "split" $ v $ , that is, replace $ v $ by two new vertices $ v_1 $ and $ v_2 $ , and for every edge $ e_i $ join it to either $ v_1 $ or $ v_2 $ (sometimes the edge $ v_1 v_2 $ is also added). For instance, this technique can be used to reduce the general 5-flow conjecture down to the special case of cubic graphs. Unfortunately, that technique does not apply here, since splitting a vertex may introduce a Petersen minor. Petersen's graph is not an apex graph (deleting any vertex still leaves a nonplanar graph). It follows that no apex graph can have a Petersen minor, so the above conjecture implies that every bridgeless apex graph has a nowhere-zero 4-flow. By splitting the vertices which lie in the plane this can be reduced to the special case where all vertices which lie in the plane have degree 3. This is then equivalent to the following old conjecture of Gr\"{o}tzsch. Conjecture (Gr\"{o}tzsch) If $ G $ is a 2-connected connected planar graph of maximum degree 3, then $ G $ is 3-edge-colorable unless it has exactly one vertex of degree 2.

Bibliography

 [AH]
 K. Appel, W. Haken, Every Planar Map is Four Colorable, Bull. Amer. Math. Soc. 82 (1976) 711-712. MathSciNet
 MathSciNet

 [RSST]
 N. Robertson, D.P. Sanders, P.D. Seymour, and R. Thomas, A New Proof of the Four-Color Theorem , Electron. Res. Announc., Am. Math. Soc. 02, no 1 (1996) 17-25. MathSciNet
 A New Proof of the Four-Color Theorem · MathSciNet

 [RST]
 N. Robertson, P.D. Seymour, and R. Thomas, Tutte's edge-colouring conjecture. J. Combin. Theory Ser. B 70 (1997), no. 1, 166--183. MathSciNet
 MathSciNet

 [Tut54]
 W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
 MathSciNet

 [Tut66]
 W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet
 MathSciNet

Related conjectures

 
 related to
 5-flow conjecture
 partial
 No implication either way. The 4-flow conjecture concludes NZ 4-flows only for bridgeless graphs with no Petersen minor and says nothing about graphs containing a Petersen minor (e.g. the Petersen graph itself needs a 5-flow), so it cannot yield the 5-flow conjecture. Conversely a NZ 5-flow never gives a NZ 4-flow, so the 5-flow conjecture does not imply the 4-flow conjecture. The cross-mention in the 4-flow page is purely about proof technique: vertex-splitting reduces the 5-flow conjecture to cubic graphs but fails for the 4-flow conjecture because splitting may create a Petersen minor. Both are Tutte flow conjectures, hence thematically linked only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
