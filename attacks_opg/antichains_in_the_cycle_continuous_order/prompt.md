Attack the following open graph-theory problem.

Catalog id: antichains_in_the_cycle_continuous_order
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/antichains_in_the_cycle_continuous_order/
Original entry: http://www.openproblemgarden.org/op/antichains_in_the_cycle_continuous_order
Problem attributed to: DeVos, Matt (posted 2007-05-12)

=== Problem statement (OpenProblemGarden) ===
Title: Antichains in the cycle continuous order
If $ G $ , $ H $ are graphs, a function $ f : E(G) \rightarrow E(H) $ is called cycle-continuous if the pre-image of every element of the (binary) cycle space of $ H $ is a member of the cycle space of $ G $ . Problem Does there exist an infinite set of graphs $ \{G_1,G_2,\ldots \} $ so that there is no cycle continuous mapping between $ G_i $ and $ G_j $ whenever $ i \neq j $ ?

=== Discussion / context (OpenProblemGarden) ===
The definition of a cycle-continuous mapping is based on some work of Jaeger, and the most interesting question on this subject is undoubtedly Jaeger's Petersen coloring conjecture . Let us define a relation on the set of all finite graphs with at least one edge by the rule $ G>H $ if there is a cycle-continuous mapping from $ G $ to $ H $ . It is not difficult to verify that $ > $ is a quasi order (reflexive and transitive). In this order, every Eulerian graph dominates every other graph, and every graph with a cut edge is dominated by every other graph. Let $ A_i $ be the graph on two vertices with $ i $ parallel edges. Then $ A_3 < A_5 < A_7 < ... $ with all the inequalities strict, so this sequence is an infinite chain. Very little else seems to be known about this order. In particular, the problem highlighted above - does there exist an infinite antichain? remains open.

=== Catalog page (statement + literature review) ===
Antichains in the cycle continuous order — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 Šámal (2012, published 2017) answered DeVos's question affirmatively by proving that there exists an infinite set of graphs with no cycle-continuous mapping between any two of them, i.e., an infinite antichain in the cycle-continuous quasi-order. The result is further strengthened to show that every countable poset can be represented by graphs and cycle-continuous mappings.

 Cited literature (1)

 
 
 
proof Cycle-continuous mappings -- order structure
 (2017)
 

 
 Robert Šámal · Journal of Graph Theory · arXiv:1212.6909

Proves the existence of an infinite antichain in the cycle-continuous mapping quasi-order (answering DeVos–Nešetřil–Raspaud), and shows every countable poset embeds in this order; published in J. Graph Theory 85(1):56–73, 2017.
 

 

 Reviewer notes. The arXiv preprint was submitted 2012-12-31, well after the OPG posting date of 2007-05-12. The journal version appeared in J. Graph Theory 85(1):56–73 (May 2017), confirmed via DBLP. The problem was originally attributed to DeVos, Nešetřil, and Raspaud; the OPG page credits only DeVos. The DOI for the JGT article was not directly retrieved but the DBLP entry confirms volume/pages.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 132s.
 

Problem. Does there exist an infinite set of graphs $ \{G_1,G_2,\ldots \} $ so that there is no cycle continuous mapping between $ G_i $ and $ G_j $ whenever $ i \neq j $ ?

Keywords:
antichain · cycle · poset

Discussion

The definition of a cycle-continuous mapping is based on some work of Jaeger, and the most interesting question on this subject is undoubtedly Jaeger's Petersen coloring conjecture . Let us define a relation on the set of all finite graphs with at least one edge by the rule $ G>H $ if there is a cycle-continuous mapping from $ G $ to $ H $ . It is not difficult to verify that $ > $ is a quasi order (reflexive and transitive). In this order, every Eulerian graph dominates every other graph, and every graph with a cut edge is dominated by every other graph. Let $ A_i $ be the graph on two vertices with $ i $ parallel edges. Then $ A_3 < A_5 < A_7 < ... $ with all the inequalities strict, so this sequence is an infinite chain. Very little else seems to be known about this order. In particular, the problem highlighted above - does there exist an infinite antichain? remains open.

Related conjectures

 
 related to
 Petersen coloring conjecture
 partial
 Both problems live in the quasi-order defined by cycle-continuous mappings, and the source page's mention of the Petersen coloring conjecture is only to say it is 'the most interesting question on this subject'. The Petersen coloring conjecture (equivalently: every bridgeless graph admits a cycle-continuous map to the Petersen graph) asserts that all bridgeless graphs dominate one fixed element of the order; the antichain problem asks whether the order contains an infinite antichain. Neither statement forces the other: knowing every bridgeless graph maps to Petersen puts no constraint on comparability among arbitrary pairs of graphs, and existence or non-existence of an infinite antichain says nothing about maps to the Petersen graph specifically. Shared framework, no implication.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
