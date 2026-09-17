Attack the following open graph-theory problem.

Catalog id: matching_cut_and_girth
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/matching_cut_and_girth/
Original entry: http://www.openproblemgarden.org/op/matching_cut_and_girth

=== Problem statement (OpenProblemGarden) ===
Title: Matching cut and girth
Question For every $ d $ does there exists a $ g $ such that every graph with average degree smaller than $ d $ and girth at least $ g $ has a matching-cut?

=== Discussion / context (OpenProblemGarden) ===
Let $ G=(V,E) $ be a graph. A matching $ M $ is a matching-cut if there exists a set $ S\subset V $ such that $ M = E(S:V\setminus S) $ . Graphs having a matching-cut are called decomposable. It is known that every graph with $ |E| < 3(|V|-1)/2 $ is decomposable [BFP11].

=== References listed by OpenProblemGarden ===
- [C84] V. Chvátal, Recognizing decomposable graphs, J Graph Theory 8 (1984), 51–53
- [BFP11] P. Bonsma, A. Farley, A. Proskurowski, Extremal graphs having no matching cuts, J Graph Theory (2011)

=== Catalog page (statement + literature review) ===
Matching cut and girth — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The original existence question — whether for every $d$ there exists $g$ such that every graph with average degree less than $d$ and girth at least $g$ has a matching-cut — remains open as stated. Feghali, Lucke, Paulusma, and Ries (2022/2023) proved that Matching Cut is NP-complete for bipartite graphs of girth at least $g$ (any $g \geq 3$) and maximum degree at most 60, resolving a 20-year-old complexity question and implying that high girth alone does not force a matching cut even in bounded-degree graphs. The structural existence question for specific ranges of average degree $d$ remains unresolved.

 Cited literature (1)

 
 
 
partial Matching Cuts in Graphs of High Girth and H-Free Graphs
 (2023)
 

 
 Carl Feghali, Felicia Lucke, Daniël Paulusma, Bernard Ries · 34th International Symposium on Algorithms and Computation (ISAAC 2023), LIPIcs vol. 283 · arXiv:2212.12317 · doi:10.4230/LIPIcs.ISAAC.2023.31

Proves Matching Cut is NP-complete for bipartite graphs of girth at least $g$ (for every fixed $g \geq 3$) and maximum degree at most 60, resolving a 20-year-old complexity question; this implies the existence of high-girth bounded-degree graphs with no matching cut, which has negative implications for the OPG existence question for large average degree.
 

 

 Reviewer notes. The OPG existence question (structural: does high girth + low average degree guarantee a matching cut?) is distinct from the complexity question resolved by Feghali et al. The Feghali et al. NP-completeness result implies there are NO-instances (graphs without matching cuts) with high girth and max degree ≤ 60, but the average degree of those specific NO-instances is not confirmed from the abstract; for small d (e.g., d ≤ 3) the existence question may still be open. Bonsma's 2009 result that every planar graph of girth ≥ 6 has a matching cut predates the 2011 OPG posting. The Springer journal version (Algorithmica 2025, DOI 10.1007/s00453-025-01318-8) could not be verified due to access redirect.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Question. For every $ d $ does there exists a $ g $ such that every graph with average degree smaller than $ d $ and girth at least $ g $ has a matching-cut?

Keywords:
matching cut, matching, cut

Discussion

Let $ G=(V,E) $ be a graph. A matching $ M $ is a matching-cut if there exists a set $ S\subset V $ such that $ M = E(S:V\setminus S) $ . Graphs having a matching-cut are called decomposable. It is known that every graph with $ |E| < 3(|V|-1)/2 $ is decomposable [BFP11].

Bibliography

 [C84]
 V. Chvátal, Recognizing decomposable graphs, J Graph Theory 8 (1984), 51–53

 [BFP11]
 P. Bonsma, A. Farley, A. Proskurowski, Extremal graphs having no matching cuts, J Graph Theory (2011)
