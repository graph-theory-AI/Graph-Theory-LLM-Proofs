Attack the following open graph-theory problem.

Catalog id: 5_flow_conjecture
Source: OpenProblemGarden (importance: Outstanding ✭✭✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/5_flow_conjecture/
Original entry: http://www.openproblemgarden.org/op/5_flow_conjecture
Problem attributed to: Tutte, William T. (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: 5-flow conjecture
Conjecture Every bridgeless graph has a nowhere-zero 5-flow.

=== Discussion / context (OpenProblemGarden) ===
For planar graphs , this theorem follows from flow/coloring duality , and the Five color theorem (every loopless planar graph is 5-colorable). In light of this, we may view this conjecture as a widesweeping generalization of the 5-color-theorem. The Petersen graph does not have a nowhere-zero 4-flow, which shows that this conjecture (if true) is best possible. It is far from obvious that there should exist a fixed number $ k $ so that every bridgeless graph has a nowhere-zero $ k $ -flow. Indeed, this weaker conjecture was also made by Tutte, but was resolved by Kilpatrick [K] and independently Jaeger [J], who both proved that bridgeless graphs have nowhere-zero 8-flows. Seymour [S] improved upon this result by showing that bridgeless graphs have nowhere-zero 6-flows.

=== References listed by OpenProblemGarden ===
- [J] F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216. MathSciNet
- [K] P.A. Kilpatrick, Tutte's First Colour-Cycle Conjecture, Thesis, Cape Town (1975).
- [S] P.D. Seymour, Nowhere-Zero 6-Flows, J. Combinatorial Theory Ser. B 30 (1981) 130-135. MathSciNet
- [T54] W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
- [Tt66] W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet

=== Catalog page (statement + literature review) ===
5-flow conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Tutte's 5-flow conjecture remains open; Seymour's 1981 result (every bridgeless graph has a nowhere-zero 6-flow) is still the best universal bound. Since the OPG posting, partial progress has been made extending the conjecture to special classes of cubic graphs: cyclically 6-edge-connected cubic graphs satisfying certain conditions on 1-factor intersections (Steffen 2015), and cyclically 6-edge-connected cubic graphs with oddness at most 4 (Mazzuoccolo–Steffen 2017).

 Cited literature (2)

 
 
 
partial Intersecting 1-factors and nowhere-zero 5-flows
 (2015)
 

 
 Eckhard Steffen · Combinatorica · arXiv:1306.5645

Proves that a cyclically $n$-edge-connected cubic graph has a nowhere-zero 5-flow if either ($n\ge 6$ and $\mu_2(G)\le 2$) or $n\ge 5\mu_2(G)-3$, where $\mu_2(G)$ is the minimum size of the intersection of two 1-factors.
 

 
 
partial Nowhere-zero 5-flows on cubic graphs with oddness 4
 (2017)
 

 
 Giuseppe Mazzuoccolo, Eckhard Steffen · Journal of Graph Theory · arXiv:1412.5398 · doi:10.1002/jgt.22065

Proves that every cyclically 6-edge-connected cubic graph with oddness at most 4 has a nowhere-zero 5-flow, extending the conjecture's verification to a broader class of potential snarks.
 

 

 Reviewer notes. The Steffen (2010) paper 'Tutte's 5-Flow Conjecture for Highly Cyclically Connected Cubic Graphs' (Discrete Math. 310, 385-389) was on arXiv in July 2006 (before the OPG posting date) and is excluded from since_posted as its content predated the posting, even though the journal publication appeared in 2010. The DOI 10.1002/jgt.22065 for the Mazzuoccolo–Steffen paper was found in search results (Wiley URL) but the journal page returned 403; the arXiv abstract page (fetched successfully) confirmed title, authors, and main theorem. The withdrawn Mkrtchyan (2020) paper arXiv:2008.07152 was found to duplicate earlier work and is not cited. No post-2017 result extending oddness beyond 4 or resolving the conjecture in a wider class was found. Seymour's 6-flow theorem from 1981 remains the best universal result.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 222s.
 

Conjecture. Every bridgeless graph has a nowhere-zero 5-flow.

Keywords:
cubic · nowhere-zero flow

Discussion

For planar graphs , this theorem follows from flow/coloring duality , and the Five color theorem (every loopless planar graph is 5-colorable). In light of this, we may view this conjecture as a widesweeping generalization of the 5-color-theorem. The Petersen graph does not have a nowhere-zero 4-flow, which shows that this conjecture (if true) is best possible. It is far from obvious that there should exist a fixed number $ k $ so that every bridgeless graph has a nowhere-zero $ k $ -flow. Indeed, this weaker conjecture was also made by Tutte, but was resolved by Kilpatrick [K] and independently Jaeger [J], who both proved that bridgeless graphs have nowhere-zero 8-flows. Seymour [S] improved upon this result by showing that bridgeless graphs have nowhere-zero 6-flows.

Bibliography

 [J]
 F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216. MathSciNet
 MathSciNet

 [K]
 P.A. Kilpatrick, Tutte's First Colour-Cycle Conjecture, Thesis, Cape Town (1975).

 [S]
 P.D. Seymour, Nowhere-Zero 6-Flows, J. Combinatorial Theory Ser. B 30 (1981) 130-135. MathSciNet
 MathSciNet

 [T54]
 W.T. Tutte, A Contribution on the Theory of Chromatic Polynomials, Canad. J. Math. 6 (1954) 80-91. MathSciNet
 MathSciNet

 [Tt66]
 W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50. MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 Circular flow numbers of $r$-graphs
 disproved
 Explicit in the OPG context (written by Steffen): truth for even t implies Jaeger's conjecture for (4t'+1)-regular graphs and hence, by a result of Jaeger, the 5-flow conjecture. Self-contained check via t=4: the 5-flow conjecture reduces to 3-edge-connected cubic graphs G. Tripling every edge gives a 9-regular graph 3G whose cuts are 3x those of G, hence >= 9, so 3G is a 9-graph. Fc(3G) <= 2+2/4 = 5/2 is equivalent to a mod-5 orientation of 3G; the net contribution of each parallel triple (three +-1's) to the corresponding edge of G lies in {+-1,+-3}, never 0 mod 5, giving a nowhere-zero Z5-flow on G. Jaeger's reduction (9-edge-connected circular 5/2-flows imply the 5-flow conjecture) is documented in arXiv:1812.09833.
 

 
 implied by
 Jaeger's modular orientation conjecture
 disproved
 The implication is explicitly stated in the source's own OPG context: 'for k=2, Jaeger showed that this conjecture (if true) would imply the 5-flow conjecture.' The full modular orientation conjecture (all k) contains the k=2 case (every 8-edge-connected graph has a modular 5-orientation, equivalently a 5/2-flow), and Jaeger's reduction derives nowhere-zero 5-flows for all bridgeless graphs from it, so truth of the source forces truth of the target. Direction correct. Note the source conjecture has since been disproved (for k >= 3, by Han, Li, Wu, Zhang), but that does not affect the validity of the conditional implication, and the k=2 case relevant to the reduction remains open.
 

 
 implied by
 Real roots of the flow polynomial
 disproved
 For a bridgeless graph G the flow polynomial is monic of degree |E|-|V|+c (only the full edge set attains the maximum nullity when there are no bridges), so it is a nonzero polynomial that is positive for large t; alternatively Phi(G,6)>0 by Seymour's 6-flow theorem. If all its real roots are at most 4, it cannot change sign on (4,infinity), hence Phi(G,5)>0. Phi(G,5) counts nowhere-zero Z5-flows, and by Tutte a nowhere-zero Z5-flow exists iff a nowhere-zero integer 5-flow exists. Thus every bridgeless graph would have a nowhere-zero 5-flow. Self-contained; direction correct (root bound is the stronger statement).
 

 
 implied by
 Unit vector flows
 partial
 The source node contains both conjectures of the OPG entry, whose context states verbatim that 'together they imply Tutte's 5-flow conjecture.' The reduction is standard: the 5-flow conjecture reduces to bridgeless cubic graphs; for such G, an S²-flow φ gives at each vertex three unit vectors summing to zero, hence coplanar at mutual 120° angles, i.e., equidistant on a great circle. Composing φ with the map q of the second conjecture yields values in {±1,...,±4} summing to zero at every vertex (antipodality makes this orientation-consistent), i.e., a nowhere-zero 5-flow. Note the implication needs both conjectures of the entry, which the source node bundles.
 

 
 implied by
 ½-flow-pair existence in bridgeless graphs
 open
 The source's own context states the implication explicitly: given a 1/2-flow-pair (phi_2, phi_4), the combination (5*phi_2 + phi_4)/2 is a circular 5-flow. Checking: if phi_2(e) = ±1 then |5*phi_2(e) + phi_4(e)| ∈ [2,8] (since |phi_4(e)| <= 3), so the value lies in [1,4]; if phi_2(e) = 0 the condition |phi_4(e)| >= 2 gives a value in [1, 3/2]. All edge values lie in [1, 5-1] in absolute value, i.e. a circular 5-flow, and by the standard equivalence (Goddyn-Tarsi-Zhang: flow number = ceiling of circular flow number) the graph then has a nowhere-zero 5-flow. Direction as claimed.
 

 
 related to
 4-flow conjecture
 partial
 No implication either way. The 4-flow conjecture concludes NZ 4-flows only for bridgeless graphs with no Petersen minor and says nothing about graphs containing a Petersen minor (e.g. the Petersen graph itself needs a 5-flow), so it cannot yield the 5-flow conjecture. Conversely a NZ 5-flow never gives a NZ 4-flow, so the 5-flow conjecture does not imply the 4-flow conjecture. The cross-mention in the 4-flow page is purely about proof technique: vertex-splitting reduces the 5-flow conjecture to cubic graphs but fails for the 4-flow conjecture because splitting may create a Petersen minor. Both are Tutte flow conjectures, hence thematically linked only.
 

 
 related to
 5-local-tensions
 open
 The connection is flow/local-tension surface duality: as the source page states, Tutte's 5-flow conjecture implies the companion conjecture 'every loopless graph embedded in an ORIENTABLE surface has a 5-local-tension' (local-tensions on G dualize to flows on G*). But the headline 5-local-tensions conjecture (edge-width >= c implies 5-local-tension) ranges over all surfaces; on non-orientable surfaces duality produces flows on BIDIRECTED graphs (Bouchet's setting, parameter 6, not 5), so the 5-flow conjecture covers only the orientable subfamily of the source conjecture. Nor does the source imply the 5-flow conjecture (it is a statement about embedded graphs of large edge-width, not all bridgeless graphs). Subfamily implication only, hence related_only.
 

 
 related to
 The three 4-flows conjecture
 open
 The mention is a methodological analogy only: 'As with the 5-flow conjecture or the cycle double cover conjecture, establishing this conjecture comes down to proving it for cubic graphs which are not 3-edge-colorable.' No implication is stated or derivable. Combining the 4-flows on G\A1 and G\A2 (which cover all of E(G) since A1,A2 are disjoint) yields only a nowhere-zero Z4xZ4-flow, i.e. a 16-flow, weaker than Seymour's unconditional 6-flow theorem, so the three-4-flows conjecture does not yield a 5-flow; conversely a nowhere-zero 5-flow gives no decomposition into three sets whose complements carry 4-flows. Both reduce to snarks and share the flow framework, so related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
