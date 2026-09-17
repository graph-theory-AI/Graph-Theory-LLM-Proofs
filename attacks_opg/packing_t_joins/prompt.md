Attack the following open graph-theory problem.

Catalog id: packing_t_joins
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/packing_t_joins/
Original entry: http://www.openproblemgarden.org/op/packing_t_joins
Problem attributed to: DeVos, Matt (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Packing T-joins
Conjecture There exists a fixed constant $ c $ (probably $ c=1 $ suffices) so that every graft with minimum $ T $ -cut size at least $ k $ contains a $ T $ -join packing of size at least $ (2/3)k-c $ .

=== Discussion / context (OpenProblemGarden) ===
Definitions: A graft consists of a graph $ G=(V,E) $ together with a distinguished set $ T \subseteq V $ of even cardinality. A $ T $ - cut is an edge-cut $ \delta(X) $ of $ G $ with the property that $ |X \cap T| $ is odd. A $ T $ - join is a set $ S \subseteq E $ with the property that a vertex of $ (V,S) $ has odd degree if and only if it is in $ T $ . A $ T $ -join packing is a set of pairwise disjoint T-joins. It is an easy fact that every $ T $ -join and every $ T $ -cut intersect in an odd number of elements. It follows easily from this that the maximum size of a $ T $ -join packing is always less than or equal to the minimum size of a $ T $ -cut. There is a simple example of a graft with $ |T|=4 $ with minimum $ T $ -cut size $ k $ which contains only $ (2/3)k $ disjoint T-joins. The above conjecture asserts that this is essentially the worst case. DeVos and Seymour [DS] have obtained a partial result toward the above conjecture, proving that every graft with minimum $ T $ -cut size $ k $ contains a $ T $ -join packing of size at least the floor of $ (1/3)k $ . Definition: We say that a graft $ G $ is an $ r $ - graph if $ G $ is $ r $ -regular, $ T=V $ , and every $ T $ -cut of G has size at least $ r $ . Conjecture (Rizzi) If $ G $ is an $ r $ -graph, then $ G $ contains a $ T $ -join packing of size at least $ r-2 $ . In an $ r $ -graph, every perfect matching is a $ T $ -join, so the above conjecture is true with room to spare for $ r $ -graphs which are $ r $ -edge-colorable. Indeed, Seymour had earlier conjectured that every $ r $ -graph contains $ r-2 $ disjoint perfect matchings. This however was disproved by Rizzi [R] who constructed for every $ r>2 $ an $ r $ -graph in which every two perfect matchings intersect. Rizzi suggested the above problem as a possible fix for Seymour's conjecture. DeVos and Seymour have proved that every $ r $ -graph has a $ T $ -join packing of size at least the floor of $ r/2 $ . Definition: Let $ G $ be a graph and let $ T $ be the set of vertices of $ G $ of odd degree. A $ T $ -join of $ (G,T) $ is defined to be a postman set . Note that when $ T $ is the set of vertices of odd degree, a cocycle of $ G $ is a $ T $ -cut if and only if it has odd size. Rizzi has shown that the following conjecture is equivalent to the above conjecture in the special case when $ r $ is odd. Conjecture (The packing postman sets conjecture (Rizzi)) If every odd edge-cut of $ G $ has size $ >2k+1 $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. The Petersen graph (or more generally any non $ (2k+1) $ -edge-colorable $ (2k+1) $ -graph) shows that the above conjecture would be false with the weaker assumption that every odd edge-cut has size $ >2k $ . The following conjecture asserts that odd edge-cut size $ >2k $ is enough (for the same conclusion) if we assume in addition that G has no Petersen minor. Conjecture (Conforti, Johnson) If $ G $ has no Petersen minor and every odd edge-cut of $ G $ has size $ >2k $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. Gerard Cornuejols [C] has kindly offered $5000 for a solution to this conjecture. However, it will be tough to find a quick proof since this conjecture does imply the 4-color theorem. Robertson, Seymour, Sanders, and Thomas [RSST] have proved the above conjecture for cubic graphs. Conforti and Johnson [CJ] proved it under the added hypothesis that G has no 4-wheel minor.

=== References listed by OpenProblemGarden ===
- [CJ] M. Conforti and E.L. Johnson, Two min-max theorems for graphs noncontractible to a four wheel, preprint.
- [C] G. Cornuejols, Combinatorial Optimization, packing and covering, SIAM, Philadelphia (2001).
- [R] R. Rizzi, Indecomposable r-Graphs and Some Other Counterexamples, J. Graph Theory 32 (1999) 1-15. MathSciNet
- [RSST] N. Robertson, D.P. Sanders, P.D. Seymour, and R. Thomas, A New Proof of the Four-Color Theorem, Electron. Res. Announc., Am. Math. Soc. 02, no 1 (1996) 17-25.
- [S] P.D. Seymour, Some Unsolved Problems on One-Factorizations of Graphs, in Graph Theory and Related Topics, edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York 1979) 367-368.

=== Catalog page (statement + literature review) ===
Packing T-joins — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The main DeVos conjecture — that every graft with minimum $T$-cut size $k$ admits a $T$-join packing of size at least $(2/3)k - c$ — remains open; the best verified general lower bound is still $\lfloor k/3 \rfloor$ from DeVos–Seymour (pre-posting). Post-2007, Abdi and Guenin proved the packing result for the special class of clutters of odd $T$-joins with at most two terminals in the signed-graft setting, confirming the Cycling Conjecture in that case.

 Cited literature (1)

 
 
 
partial Packing odd $T$-joins with at most two terminals
 (2018)
 

 
 Ahmad Abdi, Bertrand Guenin · Journal of Graph Theory · arXiv:1410.7423 · doi:10.1002/jgt.22178

Proves that a signed graft packs if it is Eulerian and excludes two special non-packing minors, confirming the Cycling Conjecture for odd T-joins with at most two terminals; corollaries include T-join packing with at most four terminals.
 

 

 Reviewer notes. The Abdi–Guenin paper (arXiv:1410.7423, JGT 2018) works in the signed-graft / odd-T-join framework, which is related but not identical to the plain graft T-join packing of the DeVos conjecture; it is cited as a partial result for a special case. The Edwards 2011 McGill thesis ('Optimization and packings of T-joins and T-cuts') contains further planar-graph results but could not be fully read due to PDF encoding issues, so it is not cited. The 2025 paper arXiv:2510.26975 (Kita) concerns grafts with connected minimum joins and does not address the main packing bound. No post-2007 paper found that improves the general floor(k/3) bound toward the conjectured (2/3)k−c.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. There exists a fixed constant $ c $ (probably $ c=1 $ suffices) so that every graft with minimum $ T $ -cut size at least $ k $ contains a $ T $ -join packing of size at least $ (2/3)k-c $ .

Keywords:
packing · T-join

Discussion

Definitions: A graft consists of a graph $ G=(V,E) $ together with a distinguished set $ T \subseteq V $ of even cardinality. A $ T $ - cut is an edge-cut $ \delta(X) $ of $ G $ with the property that $ |X \cap T| $ is odd. A $ T $ - join is a set $ S \subseteq E $ with the property that a vertex of $ (V,S) $ has odd degree if and only if it is in $ T $ . A $ T $ -join packing is a set of pairwise disjoint T-joins. It is an easy fact that every $ T $ -join and every $ T $ -cut intersect in an odd number of elements. It follows easily from this that the maximum size of a $ T $ -join packing is always less than or equal to the minimum size of a $ T $ -cut. There is a simple example of a graft with $ |T|=4 $ with minimum $ T $ -cut size $ k $ which contains only $ (2/3)k $ disjoint T-joins. The above conjecture asserts that this is essentially the worst case. DeVos and Seymour [DS] have obtained a partial result toward the above conjecture, proving that every graft with minimum $ T $ -cut size $ k $ contains a $ T $ -join packing of size at least the floor of $ (1/3)k $ . Definition: We say that a graft $ G $ is an $ r $ - graph if $ G $ is $ r $ -regular, $ T=V $ , and every $ T $ -cut of G has size at least $ r $ . Conjecture (Rizzi) If $ G $ is an $ r $ -graph, then $ G $ contains a $ T $ -join packing of size at least $ r-2 $ . In an $ r $ -graph, every perfect matching is a $ T $ -join, so the above conjecture is true with room to spare for $ r $ -graphs which are $ r $ -edge-colorable. Indeed, Seymour had earlier conjectured that every $ r $ -graph contains $ r-2 $ disjoint perfect matchings. This however was disproved by Rizzi [R] who constructed for every $ r>2 $ an $ r $ -graph in which every two perfect matchings intersect. Rizzi suggested the above problem as a possible fix for Seymour's conjecture. DeVos and Seymour have proved that every $ r $ -graph has a $ T $ -join packing of size at least the floor of $ r/2 $ . Definition: Let $ G $ be a graph and let $ T $ be the set of vertices of $ G $ of odd degree. A $ T $ -join of $ (G,T) $ is defined to be a postman set . Note that when $ T $ is the set of vertices of odd degree, a cocycle of $ G $ is a $ T $ -cut if and only if it has odd size. Rizzi has shown that the following conjecture is equivalent to the above conjecture in the special case when $ r $ is odd. Conjecture (The packing postman sets conjecture (Rizzi)) If every odd edge-cut of $ G $ has size $ >2k+1 $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. The Petersen graph (or more generally any non $ (2k+1) $ -edge-colorable $ (2k+1) $ -graph) shows that the above conjecture would be false with the weaker assumption that every odd edge-cut has size $ >2k $ . The following conjecture asserts that odd edge-cut size $ >2k $ is enough (for the same conclusion) if we assume in addition that G has no Petersen minor. Conjecture (Conforti, Johnson) If $ G $ has no Petersen minor and every odd edge-cut of $ G $ has size $ >2k $ then the edges of $ G $ may be partitioned into $ 2k+1 $ postman sets. Gerard Cornuejols [C] has kindly offered $5000 for a solution to this conjecture. However, it will be tough to find a quick proof since this conjecture does imply the 4-color theorem. Robertson, Seymour, Sanders, and Thomas [RSST] have proved the above conjecture for cubic graphs. Conforti and Johnson [CJ] proved it under the added hypothesis that G has no 4-wheel minor.

Bibliography

 [CJ]
 M. Conforti and E.L. Johnson, Two min-max theorems for graphs noncontractible to a four wheel, preprint.

 [C]
 G. Cornuejols, Combinatorial Optimization, packing and covering, SIAM, Philadelphia (2001).

 [R]
 R. Rizzi, Indecomposable r-Graphs and Some Other Counterexamples, J. Graph Theory 32 (1999) 1-15. MathSciNet
 MathSciNet

 [RSST]
 N. Robertson, D.P. Sanders, P.D. Seymour, and R. Thomas, A New Proof of the Four-Color Theorem, Electron. Res. Announc., Am. Math. Soc. 02, no 1 (1996) 17-25.

 [S]
 P.D. Seymour, Some Unsolved Problems on One-Factorizations of Graphs, in Graph Theory and Related Topics, edited by J.A. Bondy and U.S.R. Murty, Academic Press, New York 1979) 367-368.

Related conjectures

 
 related to
 Seymour's r-graph conjecture
 solved
 The mention says Seymour's r-graph conjecture 'is also closely related to Rizzi's packing postman sets conjecture (see packing T-joins)'. The target page's headline conjecture is about general grafts ((2/3)k - c disjoint T-joins), which Seymour's conjecture (chi' <= r+1 for r-graphs) cannot imply: it concerns arbitrary grafts, not r-regular graphs with T=V. Even for Rizzi's r-graph subcase (r-2 disjoint T-joins), an (r+1)-edge-coloring yields matchings that need not be perfect, hence not T-joins, so no direct implication follows; the pages assert closeness 'in nature' only. Both live in the same circle of ideas (Goldberg, r-graphs, matching/T-join decompositions) without a proven implication either way.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
