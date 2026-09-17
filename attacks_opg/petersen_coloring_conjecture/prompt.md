Attack the following open graph-theory problem.

Catalog id: petersen_coloring_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/petersen_coloring_conjecture/
Original entry: http://www.openproblemgarden.org/op/petersen_coloring_conjecture
Problem attributed to: Jaeger, Francois (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Petersen coloring conjecture
Conjecture Let $ G $ be a cubic graph with no bridge . Then there is a coloring of the edges of $ G $ using the edges of the Petersen graph so that any three mutually adjacent edges of $ G $ map to three mutually adjancent edges in the Petersen graph.

=== Discussion / context (OpenProblemGarden) ===
This extrordainary conjecture asserts that in a very strong sense, every bridgeless cubic graph has all of the cycle-space properties posessed by the Petersen graph. If true, this conjecture would imply both The Berge-Fulkerson conjecture and The five cycle double cover conjecture . If $ G $ is a graph and $ C \subseteq E(G) $ we say that $ C $ is a binary cycle if every vertex in the graph $ (V(G),C) $ has even degree. If $ H $ is a graph and $ f : E(G) \rightarrow E(H) $ is a map, we say that $ f $ is cycle-continuous if the pre-image of every binary cycle is a binary cycle. The following conjecture is an equivalent reformulation of the Petersen coloring conjecture. Conjecture (Petersen coloring conjecture (2)) Every bridgeless graph has a cycle-continuous mapping to the Petersen graph.

=== Catalog page (statement + literature review) ===
Petersen coloring conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Jaeger's Petersen coloring conjecture (every bridgeless cubic graph admits a cycle-continuous mapping to the Petersen graph, equivalently a normal 5-edge-coloring) remains open. Significant partial results have been established: every bridgeless cubic graph admits a proper 5-edge-coloring in which at least $(4/5)|E(G)|$ edges are normal, and the conjecture has been verified for specific families such as snarks superpositioned by flower snarks. The problem has also been reformulated in terms of sublinear approximation bounds on abnormal edges.

 Cited literature (5)

 
 
 
partial A remark on Petersen coloring conjecture of Jaeger
 (2012)
 

 
 Vahan V. Mkrtchyan · arXiv preprint · arXiv:1201.4472

Introduces the Sylvester coloring conjecture as a stepping-stone and proves structural constraints: if a connected bridgeless cubic graph $G$ satisfies $G \prec P$ (Petersen) or $G \prec S$ (Sylvester), then $G$ equals that graph.
 

 
 
partial Partially normal 5-edge-colorings of cubic graphs
 (2019)
 

 
 Ligang Jin, Yingli Kang · arXiv preprint · arXiv:1911.06759

Proves that every bridgeless cubic graph admits a proper 5-edge-coloring in which at least $|E(G)| - \mu_3(G) \geq (4/5)|E(G)|$ edges are normal, providing a quantitative approximation to the Petersen coloring conjecture.
 

 
 
partial Variations on the Petersen Colouring Conjecture
 (2020)
 

 
 François Pirot, Jean-Sébastien Sereni, Riste Škrekovski · The Electronic Journal of Combinatorics · arXiv:1905.07913 · doi:10.37236/8515

Proves that every bridgeless cubic graph $G$ admits an edge-colouring with 4 colours such that at most $(4/5)|V(G)|$ edges fail the normality condition, and shows this bound is tight with the Petersen graph as the extremal example.
 

 
 
partial On sublinear approximations for the Petersen coloring conjecture
 (2021)
 

 
 Davide Mattiolo, Giuseppe Mazzuoccolo, Vahan Mkrtchyan · arXiv preprint · arXiv:2104.09241

Reformulates the Petersen coloring conjecture as equivalent to the existence of a sublinear function bounding abnormal edges in normal 5-edge-colorings, providing a new quantitative perspective on the conjecture.
 

 
 
partial Normal 5-edge-coloring of some snarks superpositioned by Flower snarks
 (2023)
 

 
 Jelena Sedlar, Riste Škrekovski · arXiv preprint · arXiv:2306.13340

Establishes sufficient conditions for the Petersen coloring conjecture to hold in snarks superpositioned by flower snarks, verifying the conjecture for this specific infinite family.
 

 

 Reviewer notes. The conjecture remains fully open. The 4/5 normal-edge fraction appears in both Jin-Kang (2019) and Pirot-Sereni-Škrekovski (2020) with slightly different formulations (5-coloring vs. 4-coloring). The Mkrtchyan 2012 paper was published in Australasian Journal of Combinatorics 2013 but DOI was not confirmed. No counterexample or full proof was found in the literature searched. The ScienceDirect result for 'Normal 5-edge-coloring of some snarks superpositioned by the Petersen graph' was not fetched independently and is therefore not cited.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. Let $ G $ be a cubic graph with no bridge . Then there is a coloring of the edges of $ G $ using the edges of the Petersen graph so that any three mutually adjacent edges of $ G $ map to three mutually adjancent edges in the Petersen graph.

Keywords:
cubic · edge-coloring · Petersen graph

Discussion

This extrordainary conjecture asserts that in a very strong sense, every bridgeless cubic graph has all of the cycle-space properties posessed by the Petersen graph. If true, this conjecture would imply both The Berge-Fulkerson conjecture and The five cycle double cover conjecture . If $ G $ is a graph and $ C \subseteq E(G) $ we say that $ C $ is a binary cycle if every vertex in the graph $ (V(G),C) $ has even degree. If $ H $ is a graph and $ f : E(G) \rightarrow E(H) $ is a map, we say that $ f $ is cycle-continuous if the pre-image of every binary cycle is a binary cycle. The following conjecture is an equivalent reformulation of the Petersen coloring conjecture. Conjecture (Petersen coloring conjecture (2)) Every bridgeless graph has a cycle-continuous mapping to the Petersen graph.

Related conjectures

 
 implies
 (m,n)-cycle covers
 partial
 The target, 'every bridgeless graph has a (5,2)-cycle-cover', is exactly the five cycle double cover conjecture (the OPG (m,n) chart labels the (5,2) entry '5CDC conj'). The source's equivalent reformulation (2), stated in its context, is that every bridgeless graph admits a cycle-continuous map f to the Petersen graph P. P has a double cover by 5 even subgraphs; the preimage of each is an even subgraph of G (cycle-continuity), and each edge e of G is covered exactly as many times as f(e), namely twice, yielding a (5,2)-cycle-cover of G. The OPG source page states explicitly that Petersen coloring implies the five cycle double cover conjecture. Hypothesis classes match (all bridgeless graphs via reformulation (2)).
 

 
 implies
 Cycle double cover conjecture
 partial
 Via reformulation (2) of the Petersen coloring conjecture (every bridgeless graph has a cycle-continuous map to the Petersen graph P), pulling back a double cover of P by 5 even subgraphs gives 5 even subgraphs of G covering each edge exactly twice — a (5,2)-cycle cover, hence in particular a cycle double cover. The hypothesis class (all bridgeless graphs) matches CDC exactly. This is Jaeger's classical implication; the CDC target page lists the five cycle double cover conjecture (implied by Petersen coloring per the source's OPG context) among its strengthenings.
 

 
 implies
 The Berge-Fulkerson conjecture
 partial
 Both conjectures concern bridgeless cubic graphs, so the hypothesis classes coincide. A Petersen coloring maps the three edges incident to any vertex of G to three mutually adjacent edges of the Petersen graph P, i.e., to the edge-triple at a vertex of P. P has six perfect matchings covering every edge of P exactly twice; the preimage under the coloring of each is a perfect matching of G (exactly one of the three edges at each vertex of G is mapped into it), and each edge e of G lies in exactly two of the six preimages, since f(e) lies in exactly two of P's matchings. This is Jaeger's classical observation, and the OPG source context states explicitly that the Petersen coloring conjecture implies the Berge-Fulkerson conjecture.
 

 
 implies
 The three 4-flows conjecture
 open
 The implication is stated explicitly in the target's OPG context: 'This conjecture is a consequence of the Petersen coloring conjecture.' The mechanism is standard: the Petersen coloring conjecture is equivalent to every bridgeless graph having a cycle-continuous map f to the Petersen graph; the Petersen graph's edge set partitions into three sets P_1,P_2,P_3 whose complements have nowhere-zero 4-flows, and the pullbacks A_i = f^{-1}(P_i) partition E(G) with G\A_i inheriting a nowhere-zero 4-flow (4-flows are a cycle-space property preserved under cycle-continuous preimages). Direction is correct: Petersen coloring is the stronger statement.
 

 
 related to
 Antichains in the cycle continuous order
 solved
 Both problems live in the quasi-order defined by cycle-continuous mappings, and the source page's mention of the Petersen coloring conjecture is only to say it is 'the most interesting question on this subject'. The Petersen coloring conjecture (equivalently: every bridgeless graph admits a cycle-continuous map to the Petersen graph) asserts that all bridgeless graphs dominate one fixed element of the order; the antichain problem asks whether the order contains an infinite antichain. Neither statement forces the other: knowing every bridgeless graph maps to Petersen puts no constraint on comparability among arbitrary pairs of graphs, and existence or non-existence of an infinite antichain says nothing about maps to the Petersen graph specifically. Shared framework, no implication.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
