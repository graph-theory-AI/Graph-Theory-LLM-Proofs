Attack the following open graph-theory problem.

Catalog id: three_4_flows_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/three_4_flows_conjecture/
Original entry: http://www.openproblemgarden.org/op/three_4_flows_conjecture
Problem attributed to: DeVos, Matt (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: The three 4-flows conjecture
Conjecture For every graph $ G $ with no bridge , there exist three disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G \setminus A_i $ has a nowhere-zero 4-flow for $ 1 \le i \le 3 $ .

=== Discussion / context (OpenProblemGarden) ===
A graph $ G $ has a nowhere-zero 4-flow if and only if there exist disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G\A_i $ has a nowhere-zero 2-flow for $ 1 \le i \le 3 $ . Thus, the above conjecture is true with room to spare for such graphs. Since every 4-edge-connected graph and every 3- edge-colorable cubic graph has a nowhere-zero 4-flow, this conjecture is automatically true for these families. As with the 5-flow conjecture or the cycle double cover conjecture , establishing this conjecture comes down to proving it for cubic graphs which are not 3-edge-colorable. This conjecture is a consequence of the Petersen coloring conjecture , and it implies the Orientable cycle four cover conjecture . The latter implication follows immediately from the fact that every graph with a nowhere-zero 4-flow has an orientable cycle double cover. Actually, it is possible that for every graph $ G $ with no cut-edge, there exist disjoint sets $ A_B_1,B_2 \subseteq E(G) $ with $ A \cup B_1 \cup B_2 = E(G) $ and so that $ G\B_1 $ and $ G\B_2 $ have nowhere-zero 3-flows and $ G\A $ has a nowhere-zero 2-flow. The Petersen graph has such a decomposition ( $ B_1 $ and $ B_2 $ should be alternate edges of some 8-circuit) and so does every graph with a nowhere-zero 4-flow. If this stronger statement is true, then it would imply the oriented eight cycle four cover conjecture.

=== References listed by OpenProblemGarden ===
- [J] F. Jaeger, On circular flows in graphs. Finite and infinite sets, Vol. I, II (Eger, 1981), 391--402, Colloq. Math. Soc. János Bolyai, 37, North-Holland, Amsterdam, 1984.. MathSciNet

=== Catalog page (statement + literature review) ===
The three 4-flows conjecture — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The three 4-flows conjecture, which asks for a partition of the edge set of every bridgeless graph into three sets each of which can be removed to leave a graph with a nowhere-zero 4-flow, remains open. No post-2007 paper resolving or substantially partially resolving this conjecture was found; the problem reduces to cubic snarks and is implied by the Petersen coloring conjecture, itself still open.

 Reviewer notes. The OPG page (openproblemgarden.org) returned ECONNREFUSED. Five search queries were run; none returned a paper specifically addressing the three 4-flows conjecture. The arXiv paper 2511.01556 (Mattiolo, Nov 2025) on removable edge subsets in graphs with nowhere-zero 4-flows is related but does not address the conjecture directly. The Petersen coloring conjecture (which implies the three 4-flows conjecture) and the orientable cycle four cover conjecture (which is implied by it) are both still open, confirming the problem likely remains unresolved. Confidence is medium rather than high because the specific conjecture did not appear in any indexed paper by name, making it difficult to rule out niche partial results.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. For every graph $ G $ with no bridge , there exist three disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G \setminus A_i $ has a nowhere-zero 4-flow for $ 1 \le i \le 3 $ .

Keywords:
nowhere-zero flow

Discussion

A graph $ G $ has a nowhere-zero 4-flow if and only if there exist disjoint sets $ A_1,A_2,A_3 \subseteq E(G) $ with $ A_1 \cup A_2 \cup A_3 = E(G) $ so that $ G\A_i $ has a nowhere-zero 2-flow for $ 1 \le i \le 3 $ . Thus, the above conjecture is true with room to spare for such graphs. Since every 4-edge-connected graph and every 3- edge-colorable cubic graph has a nowhere-zero 4-flow, this conjecture is automatically true for these families. As with the 5-flow conjecture or the cycle double cover conjecture , establishing this conjecture comes down to proving it for cubic graphs which are not 3-edge-colorable. This conjecture is a consequence of the Petersen coloring conjecture , and it implies the Orientable cycle four cover conjecture . The latter implication follows immediately from the fact that every graph with a nowhere-zero 4-flow has an orientable cycle double cover. Actually, it is possible that for every graph $ G $ with no cut-edge, there exist disjoint sets $ A_B_1,B_2 \subseteq E(G) $ with $ A \cup B_1 \cup B_2 = E(G) $ and so that $ G\B_1 $ and $ G\B_2 $ have nowhere-zero 3-flows and $ G\A $ has a nowhere-zero 2-flow. The Petersen graph has such a decomposition ( $ B_1 $ and $ B_2 $ should be alternate edges of some 8-circuit) and so does every graph with a nowhere-zero 4-flow. If this stronger statement is true, then it would imply the oriented eight cycle four cover conjecture.

Bibliography

 [J]
 F. Jaeger, On circular flows in graphs. Finite and infinite sets, Vol. I, II (Eger, 1981), 391--402, Colloq. Math. Soc. János Bolyai, 37, North-Holland, Amsterdam, 1984.. MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 Petersen coloring conjecture
 partial
 The implication is stated explicitly in the target's OPG context: 'This conjecture is a consequence of the Petersen coloring conjecture.' The mechanism is standard: the Petersen coloring conjecture is equivalent to every bridgeless graph having a cycle-continuous map f to the Petersen graph; the Petersen graph's edge set partitions into three sets P_1,P_2,P_3 whose complements have nowhere-zero 4-flows, and the pullbacks A_i = f^{-1}(P_i) partition E(G) with G\A_i inheriting a nowhere-zero 4-flow (4-flows are a cycle-space property preserved under cycle-continuous preimages). Direction is correct: Petersen coloring is the stronger statement.
 

 
 related to
 5-flow conjecture
 partial
 The mention is a methodological analogy only: 'As with the 5-flow conjecture or the cycle double cover conjecture, establishing this conjecture comes down to proving it for cubic graphs which are not 3-edge-colorable.' No implication is stated or derivable. Combining the 4-flows on G\A1 and G\A2 (which cover all of E(G) since A1,A2 are disjoint) yields only a nowhere-zero Z4xZ4-flow, i.e. a 16-flow, weaker than Seymour's unconditional 6-flow theorem, so the three-4-flows conjecture does not yield a 5-flow; conversely a nowhere-zero 5-flow gives no decomposition into three sets whose complements carry 4-flows. Both reduce to snarks and share the flow framework, so related_only.
 

 
 related to
 Cycle double cover conjecture
 partial
 The truncated mention is misleading: fetching the full CDC page shows 'the above conjecture would follow from The three 4-flows conjecture' refers to the ORIENTED CYCLE FOUR COVER conjecture, a separate weaker statement hosted on the same page, not the CDC node's statement. The three 4-flows page confirms: 'it implies the Orientable cycle four cover conjecture' (each edge lies in exactly two of the graphs G\A_i, each having an orientable CDC via its nowhere-zero 4-flow, summing to a 4-cover). A cycle four cover does not give a double cover, and no implication between three 4-flows and CDC proper is known in either direction; both reduce to non-3-edge-colorable cubic graphs and both follow from Petersen coloring, but that makes them related family members only.
 

 
 related to
 Cycle double cover conjecture
 partial
 The mention is the same analogy sentence (both reduce to non-3-edge-colorable cubic graphs). The genuine implication stated in the context goes from three-4-flows to the Orientable cycle FOUR cover conjecture, not to CDC: each G\A_i has a nowhere-zero 4-flow, hence an orientable cycle double cover, and since each edge lies in exactly two of the three subgraphs G\A_i, the union covers every edge exactly four times. A cycle 4-cover is already known unconditionally (Bermond-Jackson-Jaeger via Jaeger's 8-flow theorem), so this route does not give a double cover, and no implication between three-4-flows and CDC is stated or standard in either direction. Hence related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
