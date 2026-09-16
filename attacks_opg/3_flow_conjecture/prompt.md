Attack the following open graph-theory problem.

Catalog id: 3_flow_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/3_flow_conjecture/
Original entry: http://www.openproblemgarden.org/op/3_flow_conjecture
Problem attributed to: Tutte, William T. (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: 3-flow conjecture
Conjecture Every 4- edge-connected graph has a nowhere-zero 3-flow.

=== Discussion / context (OpenProblemGarden) ===
Grotzsch proved that every triangle free (and loopless) planar graph is 3- colorable . By flow/coloring duality , this is equivalent to the statement that every 4-edge-connected planar graph has a nowhere-zero 3-flow. The 3-flow conjecture asserts that this is still true without the assumption of planarity. Jaeger proved that 4-edge-connected graphs have nowhere-zero 4-flows, but very little is known about nowhere-zero 3-flows. In particular, the following weak version of the 3-flow conjecture is still wide open. Conjecture (The weak 3-flow conjecture (Jaeger)) There exists a fixed integer $ k $ so that every $ k $ -edge-connected graph has a nowhere-zero 3-flow. Lai and Zhang [LZ] have proved that if $ G $ has $ n $ vertices and edge-connectivity at least $ 4 \log_2(n) $ then $ G $ has a nowhere-zero 3-flow. A similar result (edge connectivity at least $ 4 \log(n) + 2 $ ) also follows from a theorem of Alon, Linial, and Meshulam [ALM] on additive bases of vector spaces.

=== References listed by OpenProblemGarden ===
- [ALM] N. Alon, N. Linial, and R. Meshulam Additive Bases of Vector Spaces over Prime Fields J. Combinatorial Theory Ser. A 57 (1991), 203-210.
- [J] F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216.
- [LZ] H.J. Lai and C.Q. Zhang, Nowhere-Zero 3-Flows of Highly Connected Graphs, Discrete Math 110 (1992) 179-183.
- [T54] W.T. Tutte, A Contribution on the Theory of Chromatic Polynomial, Canad. J. Math. 6 (1954) 80-91.
- [T66] W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50.

=== Catalog page (statement + literature review) ===
3-flow conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Tutte's 3-flow conjecture (every 4-edge-connected graph has a nowhere-zero 3-flow) remains open. Thomassen (2012) resolved the long-standing weak 3-flow conjecture of Jaeger by proving every 8-edge-connected graph admits a nowhere-zero 3-flow; Lovász, Thomassen, Wu, and Zhang (2013) subsequently sharpened this to every 6-edge-connected graph being $\mathbb{Z}_3$-connected. The gap from 4-edge-connected to 6-edge-connected remains unresolved, though the conjecture has also been confirmed for several restricted graph classes including toroidal graphs (Li et al., 2022) and projective planar graphs.

 Cited literature (4)

 
 
 
partial The weak 3-flow conjecture and the weak circular flow conjecture
 (2012)
 

 
 Carsten Thomassen · Journal of Combinatorial Theory, Series B · doi:10.1016/j.jctb.2011.09.003

Proves Jaeger's weak 3-flow conjecture by showing every 8-edge-connected graph is $\mathbb{Z}_3$-connected and hence admits a nowhere-zero 3-flow.
 

 
 
partial Nowhere-zero 3-flows and modulo k-orientations
 (2013)
 

 
 László Miklós Lovász, Carsten Thomassen, Yezhou Wu, Cun-Quan Zhang · Journal of Combinatorial Theory, Series B · doi:10.1016/j.jctb.2013.06.003

Improves Thomassen's bound: every 6-edge-connected graph is $\mathbb{Z}_3$-connected and thus admits a nowhere-zero 3-flow, as the special case $k=3$ of a result on modulo $k$-orientations.
 

 
 
partial A note on nowhere-zero 3-flow and Z_3-connectivity
 (2014)
 

 
 Fuyuan Chen, Bo Ning · arXiv preprint · arXiv:1406.1554

Proves Tutte's 3-flow conjecture holds for every 4-edge-connected graph with at most seven 5-edge-cuts, contributing partial results toward the conjecture.
 

 
 
partial Flow-critical graphs
 (2026)
 

 
 Arnbjörg Soffía Árnadóttir, Zdeněk Dvořák, Bernard Lidický, Benjamin Moore, Evelyne Smith-Roberge, Robert Šámal · arXiv preprint · arXiv:2502.01451

Proves a density bound $|E(G)| \leq 3|V(G)| - 5$ for flow-critical graphs with at most one vertex of degree at least 7 (Theorem 1.6), and extends the Lovász et al. 6-edge-connectivity theorem to allow the tip vertex $z$ to have arbitrary degree when another high-degree vertex exists with no small separating cut.
 

 

 Reviewer notes. The toroidal graphs result (Li, Ma, Miao, Shi, Wang, Zhang, J. Comb. Theory Ser. B 153, 2022, pp. 61–80) was consistently reported in search results but could not be verified via WebFetch (ScienceDirect returned HTTP 403) and no arXiv preprint was found; it is therefore omitted from since_posted. Kochol's 2001 reduction (sufficiency of 5-edge-connected) predates the 2007 posting date and was not included. The current state-of-the-art lower bound is 6-edge-connectivity (LTWZ 2013); closing the gap to 4-edge-connectivity remains the principal open challenge.

 
 Auto-reviewed 2026-05-07 with claude-sonnet-4-6 (web search enabled) · 205s.
 

Conjecture. Every 4- edge-connected graph has a nowhere-zero 3-flow.

Keywords:
nowhere-zero flow

Discussion

Grotzsch proved that every triangle free (and loopless) planar graph is 3- colorable . By flow/coloring duality , this is equivalent to the statement that every 4-edge-connected planar graph has a nowhere-zero 3-flow. The 3-flow conjecture asserts that this is still true without the assumption of planarity. Jaeger proved that 4-edge-connected graphs have nowhere-zero 4-flows, but very little is known about nowhere-zero 3-flows. In particular, the following weak version of the 3-flow conjecture is still wide open. Conjecture (The weak 3-flow conjecture (Jaeger)) There exists a fixed integer $ k $ so that every $ k $ -edge-connected graph has a nowhere-zero 3-flow. Lai and Zhang [LZ] have proved that if $ G $ has $ n $ vertices and edge-connectivity at least $ 4 \log_2(n) $ then $ G $ has a nowhere-zero 3-flow. A similar result (edge connectivity at least $ 4 \log(n) + 2 $ ) also follows from a theorem of Alon, Linial, and Meshulam [ALM] on additive bases of vector spaces.

Bibliography

 [ALM]
 N. Alon, N. Linial, and R. Meshulam Additive Bases of Vector Spaces over Prime Fields J. Combinatorial Theory Ser. A 57 (1991), 203-210.

 [J]
 F. Jaeger, Flows and Generalized Coloring Theorems in Graphs, J. Combinatorial Theory Ser. B 26 (1979) 205-216.

 [LZ]
 H.J. Lai and C.Q. Zhang, Nowhere-Zero 3-Flows of Highly Connected Graphs, Discrete Math 110 (1992) 179-183.

 [T54]
 W.T. Tutte, A Contribution on the Theory of Chromatic Polynomial, Canad. J. Math. 6 (1954) 80-91.

 [T66]
 W.T. Tutte, On the Algebraic Theory of Graph Colorings, J. Combinatorial Theory 1 (1966) 15-50.

Related conjectures

 
 implied by
 Circular flow numbers of $r$-graphs
 disproved
 Steffen's source paper states explicitly: "Tutte's 3-flow conjecture is equivalent to the statement that Fc(G) <= 3 for every 5-graph G." The t=2 instance of the source conjecture is exactly that statement (2+2/t = 3, 5-graphs). Since the source conjecture asserts the bound for ALL t>1, its truth contains the t=2 case, which is equivalent to (hence implies) the 3-flow conjecture. The converse fails: the 3-flow conjecture says nothing about t>2. So the relation is a strict one-way implication, not equivalence, matching the OPG context "For t=2 it is Tutte's 3-flow conjecture." (Note the source is now disproved for large even t, but the t=2 case and thus the implication route remain intact.)
 

 
 implied by
 Jaeger's modular orientation conjecture
 disproved
 The k=1 case of Jaeger's conjecture concerns 4-edge-connected graphs and asks for a modular 3-orientation (indegree-outdegree = 0 mod 3), which by Tutte's theorem is equivalent to a nowhere-zero Z3-flow and hence to a nowhere-zero 3-flow. So the target is precisely the k=1 instance of the source, and the universally quantified source implies it by restriction. The source's own OPG context states verbatim: 'For k=1, this problem is precisely the 3-flow conjecture.' The disproof of the general conjecture (for k>=3) does not affect this logical implication; the k=1 case remains open.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
