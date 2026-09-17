Attack the following open graph-theory problem.

Catalog id: faithful_cycle_covers
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/faithful_cycle_covers/
Original entry: http://www.openproblemgarden.org/op/faithful_cycle_covers
Problem attributed to: Seymour, Paul D. (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Faithful cycle covers
Conjecture If $ G = (V,E) $ is a graph, $ p : E \rightarrow {\mathbb Z} $ is admissable, and $ p(e) $ is even for every $ e \in E(G) $ , then $ (G,p) $ has a faithful cover.

=== Discussion / context (OpenProblemGarden) ===
Definition: Let $ G=(V,E) $ be a graph and let $ p:E \rightarrow {\mathbb Z} $ . A list $ L $ of cycles of $ G $ is a faithful (cycle) cover of $ (G,p) $ if every edge $ e $ of $ G $ occurs in exactly $ p(e) $ cycles of $ L $ . Thus, the cycle double cover conjecture is equivalent to the statement that $ (G,2) $ has a faithful cover for every graph $ G $ with no bridge . We define the map $ p $ to be admissable if $ p(e) $ satisfies the following properties: i $ p $ is nonnegative. ii $ p(S) $ is even for every edge-cut $ S $ . iii $ p(e) \le p(S)/2 $ for every edge-cut $ S $ and edge $ e \in S $ . It is easy to see that $ G $ has a faithful cover only if $ p $ is admissable. However, the converse is false. A counterexample is obtained by taking the Petersen graph, putting weight $ 2 $ on the edges of a perfect matching, and $ 1 $ elsewhere. More generally, for a graph G=(V,E), one may consider the vector space of real numbers indexed by E. We associate every circuit C with its incidence vector. Most of the basic questions about this space are solved. Seymour [S] has shown that a vector p can be written as a nonnegative rational combination of cycles if and only if it satisfies conditions (i) and (iii) in the definition of admissable. It is an easy exercise to show that for a 3-edge-connected graph G, a vector p can be written as an integer combination of cycles if and only if p satisfies (ii) in the definition of admissable. Seymour's conjecture is equivalent to the statement that every admissable map may be realized as a half-integer combination of circuits. Note the similarity of this to The Berge-Fulkerson conjecture . The most interesting result about faithful covers is a theorem of Alspach, Goddyn, and Zhang which resolved a conjecture of Seymour. They prove that whenever $ G $ has no minor isomorphic to Petersen , every admissable map has a corresponding faithful cover. For a general graph $ G $ with no bridge, Bermond, Jackson, and Jaeger [BJJ] proved that $ (G,4) $ has a faithful cover and Fan [F] proveed that $ (G,6) $ has a faithful cover. DeVos, Johnson, and Seymour [DJS] proved that $ (G,p) $ has a faithful cover whenever $ p $ is admissable and there is a nonnegative integer $ k $ such that $ 32k+83 < p(e) < 36k+88 $ holds for every edge $ e $ . However, little else seems to be known. In particular, it does not appear to be known if there exist integers $ a,b $ with $ a-b $ arbitrarily large so that $ (G,p) $ has a faithful cover whenever $ p $ is an admissable function taking on only the values $ a,b $ . Such a result would appear to require an idea not contained in any of the aforementioned papers. The analogous problem for oriented circuit covers does not appear to be very promising. It is easy to see that for an orientation of a series parallel graph G and a map $ p:E(G) \rightarrow G $ which satisfies the obvious conditions, that $ (G,p) $ will have a circuit cover using every edge in its given direction. However, even with a $ K_4 $ minor, there is a great deal of forcing, and nothing much looks like it would be true.

=== References listed by OpenProblemGarden ===
- \[AGZ] B. Alspach, L. Goddyn, and C-Q Zhang, Graphs with the circuit cover property, Trans. Amer. Math. Soc., 344 (1994), 131-154. MathSciNet
- [BJJ] J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MathSciNet
- [DJS] M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
- [F] G. Fan, Integer flows and cycle covers, J. Combinatorial Theory Ser. B 54 (1992), 113-122. MathSciNet
- [S] P.D. Seymour, Sums of circuits in Graph Theory and Related Topics edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York/Berlin (1979), 341-355. MathSciNet

=== Catalog page (statement + literature review) ===
Faithful cycle covers — Graph-theory open problems

 
 Status
 open
 low confidence
 

 Seymour's faithful cycle cover conjecture (every graph $G$ with an admissible even integer weighting $p$ has a faithful cover) remains open as stated. Web searches surfaced a 2025 Discrete Mathematics paper 'Limits of cycles and cover conjectures' that, by introducing $\mathcal{F}$-limits of cycles, reduces the conjecture for arbitrary infinite graphs to the finite (or countable) case, but the underlying finite conjecture is unresolved; the paper's full bibliographic details could not be verified within the time budget, so it is not cited here.

 Reviewer notes. The most promising recent item is 'Limits of cycles and cover conjectures' (Discrete Math., 2025; PII S0012365X25003322), which uses $\mathcal{F}$-limits to give a uniform infinite-graph treatment and reduces the Faithful Cycle Cover Conjecture for all graphs to the (finite/countable) case. ScienceDirect returned 403 on the abstract page and the paper is not on arXiv under any title-level search; the authors could not be confirmed (search snippets hint at Bowler/Carmesin but their public pages do not list this title), so the citation is omitted to avoid an unverified reference. No post-2007 paper resolving Seymour's original conjecture for finite bridgeless graphs was found; results in the area (e.g., Cycle covers I/II by Lai, Zhang and collaborators) concern Hamilton-weight contra pairs and the cycle double cover variant rather than the general admissible-even conjecture. Status reported as 'open' with low confidence given the unresolved 2025 reduction paper.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. If $ G = (V,E) $ is a graph, $ p : E \rightarrow {\mathbb Z} $ is admissable, and $ p(e) $ is even for every $ e \in E(G) $ , then $ (G,p) $ has a faithful cover.

Keywords:
cover · cycle

Discussion

Definition: Let $ G=(V,E) $ be a graph and let $ p:E \rightarrow {\mathbb Z} $ . A list $ L $ of cycles of $ G $ is a faithful (cycle) cover of $ (G,p) $ if every edge $ e $ of $ G $ occurs in exactly $ p(e) $ cycles of $ L $ . Thus, the cycle double cover conjecture is equivalent to the statement that $ (G,2) $ has a faithful cover for every graph $ G $ with no bridge . We define the map $ p $ to be admissable if $ p(e) $ satisfies the following properties: i $ p $ is nonnegative. ii $ p(S) $ is even for every edge-cut $ S $ . iii $ p(e) \le p(S)/2 $ for every edge-cut $ S $ and edge $ e \in S $ . It is easy to see that $ G $ has a faithful cover only if $ p $ is admissable. However, the converse is false. A counterexample is obtained by taking the Petersen graph, putting weight $ 2 $ on the edges of a perfect matching, and $ 1 $ elsewhere. More generally, for a graph G=(V,E), one may consider the vector space of real numbers indexed by E. We associate every circuit C with its incidence vector. Most of the basic questions about this space are solved. Seymour [S] has shown that a vector p can be written as a nonnegative rational combination of cycles if and only if it satisfies conditions (i) and (iii) in the definition of admissable. It is an easy exercise to show that for a 3-edge-connected graph G, a vector p can be written as an integer combination of cycles if and only if p satisfies (ii) in the definition of admissable. Seymour's conjecture is equivalent to the statement that every admissable map may be realized as a half-integer combination of circuits. Note the similarity of this to The Berge-Fulkerson conjecture . The most interesting result about faithful covers is a theorem of Alspach, Goddyn, and Zhang which resolved a conjecture of Seymour. They prove that whenever $ G $ has no minor isomorphic to Petersen , every admissable map has a corresponding faithful cover. For a general graph $ G $ with no bridge, Bermond, Jackson, and Jaeger [BJJ] proved that $ (G,4) $ has a faithful cover and Fan [F] proveed that $ (G,6) $ has a faithful cover. DeVos, Johnson, and Seymour [DJS] proved that $ (G,p) $ has a faithful cover whenever $ p $ is admissable and there is a nonnegative integer $ k $ such that $ 32k+83 < p(e) < 36k+88 $ holds for every edge $ e $ . However, little else seems to be known. In particular, it does not appear to be known if there exist integers $ a,b $ with $ a-b $ arbitrarily large so that $ (G,p) $ has a faithful cover whenever $ p $ is an admissable function taking on only the values $ a,b $ . Such a result would appear to require an idea not contained in any of the aforementioned papers. The analogous problem for oriented circuit covers does not appear to be very promising. It is easy to see that for an orientation of a series parallel graph G and a map $ p:E(G) \rightarrow G $ which satisfies the obvious conditions, that $ (G,p) $ will have a circuit cover using every edge in its given direction. However, even with a $ K_4 $ minor, there is a great deal of forcing, and nothing much looks like it would be true.

Bibliography

 [?]
 \[AGZ] B. Alspach, L. Goddyn, and C-Q Zhang, Graphs with the circuit cover property , Trans. Amer. Math. Soc., 344 (1994), 131-154. MathSciNet
 Graphs with the circuit cover property · MathSciNet

 [BJJ]
 J.C. Bermond, B. Jackson, and F. Jaeger, Shortest covering of graphs with cycles, J. Combinatorial Theory Ser. B 35 (1983), 297-308. MathSciNet
 MathSciNet

 [DJS]
 M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
 Cut-coloring and circuit covering

 [F]
 G. Fan, Integer flows and cycle covers, J. Combinatorial Theory Ser. B 54 (1992), 113-122. MathSciNet
 MathSciNet

 [S]
 P.D. Seymour, Sums of circuits in Graph Theory and Related Topics edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York/Berlin (1979), 341-355. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 Cycle double cover conjecture
 partial
 CDC is the p≡2 instance of the faithful cover conjecture. For bridgeless G, p≡2 is admissible: it is nonnegative, p(S)=2|S| is even for every edge-cut, and since bridgelessness forces |S|≥2 for every edge-cut, p(e)=2 ≤ |S| = p(S)/2. All p(e)=2 are even, so the hypothesis of the faithful cover conjecture holds, and a faithful cover of (G,2) is exactly a list of cycles containing each edge twice, i.e., a CDC. (A bridge e would make {e} a cut violating condition (iii), so the bridgeless restriction is exactly right.) The source's own OPG context states this equivalence of the p≡2 case with CDC explicitly.
 

 
 related to
 The Berge-Fulkerson conjecture
 partial
 The OPG page explicitly says only 'Note the similarity of this to The Berge-Fulkerson conjecture' — a thematic comparison, not an implication. No implication holds via the obvious route: Berge-Fulkerson is equivalent (by complementing the 6 perfect matchings into 2-factors) to covering a cubic graph by six 2-factors using each edge exactly 4 times, but a faithful cover of (G,4) imposes neither the 2-factor structure nor the count of six cycles; indeed Bermond-Jackson-Jaeger already proved every bridgeless graph has a cycle cover using each edge exactly 4 times, yet Berge-Fulkerson remains open. Conversely Berge-Fulkerson concerns perfect matchings of cubic graphs and says nothing about general even admissible weightings. Companion conjectures with no known implication either way: related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
