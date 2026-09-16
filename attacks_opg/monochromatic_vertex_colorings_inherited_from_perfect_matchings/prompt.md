Attack the following open graph-theory problem.

Catalog id: monochromatic_vertex_colorings_inherited_from_perfect_matchings
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/monochromatic_vertex_colorings_inherited_from_perfect_matchings/
Original entry: http://www.openproblemgarden.org/op/monochromatic_vertex_colorings_inherited_from_perfect_matchings

=== Problem statement (OpenProblemGarden) ===
Title: Monochromatic vertex colorings inherited from Perfect Matchings
Conjecture For which values of $ n $ and $ d $ are there bi-colored graphs on $ n $ vertices and $ d $ different colors with the property that all the $ d $ monochromatic colorings have unit weight, and every other coloring cancels out?

=== Discussion / context (OpenProblemGarden) ===
Background : This and many related questions are directly inspired from quantum physics, and their solutions would directly contribute to new understanding in quantum physics. Bi-Colored Graph : A bi-colored weighted graph $ G=(V(G),E(G)) $ , on $ n $ vertices with $ d $ colors is an undirected, not necessarily simple graph where there is a fixed ordering of the vertices $ V(G)=v_1, \ldots, v_n $ and to each edge $ e \in E(G) $ there is a complex weight $ w_e $ and an ordered pair of (not necessarily different) colors $ (c_1(e),c_2(e)) $ associated with it from the $ d $ possible colors. We say that an edge is monochromatic if the associated pair of colors are not different, otherwise the edge is bi-chromatic. Moreover, if $ e $ is an edge incident to the vertices $ v_i,v_j \in V(G) $ with $ i<j $ and the associated ordered pair of colors to $ e $ is $ (c_1(e),c_2(e)) $ then we say that $ e $ is colored $ c_1 $ at $ v_i $ and $ c_2 $ at $ v_j $ . We will be interested in a special coloring of this graph: Inherited Vertex Coloring : Let $ G $ be a bi-colored weighted graph and $ PM $ denote a perfect matching in $ G $ . We associate a coloring of the vertices of G with PM in the natural way: for every vertex $ v_i $ there is a single edge $ e(v_i) \in PM $ that is incident to $ v_i $ , let the color of $ v_i $ be the color of $ e(v_i) $ at $ v_i $ . We call this coloring $ c $ , the inherited vertex coloring (IVC) of the perfect matching PM. Now we are ready to define how constructive and destructive interference during an experiment is governed by perfect matchings of a bi-colored graph. Weight of Vertex Coloring : Let $ G $ be a bi-colored weighted graph. Let $ \mathcal{M} $ be the set of perfect matchings of $ G $ which have the coloring $ c $ as their inherited vertex coloring. We define the weight of $ c $ as $$w(c) := \sum_{PM \in \mathcal{M}} \prod_{e \in PM}w_e. $$ Moreover, if $ w(c) $ =1 we say that the coloring gets unit weight, and if $ w(c) $ =0 we say that the coloring cancels out.

=== References listed by OpenProblemGarden ===
- Questions on the Structure of Perfect Matchings inspired by Quantum Physics

=== Catalog page (statement + literature review) ===
Monochromatic vertex colorings inherited from Perfect Matchings — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The problem of determining for which $n$ and $d$ bi-colored graphs exist such that all $d$ monochromatic colorings have unit weight and every other coloring cancels is equivalent to the Krenn–Gu conjecture on the matching index of graphs. Significant partial progress has been made: Chandran, Gajjala, and Illickan (2024) proved the conjecture for cubic graphs and graphs with vertex connectivity at most 2, and showed any minimal counterexample must be 4-connected, while an earlier paper characterizes graphs with matching index 1 or 2. The general problem remains open and a €3,000 prize for a full resolution is unclaimed.

 Cited literature (2)

 
 
 
partial Edge-coloured graphs with only monochromatic perfect matchings and their connection to quantum physics
 (2022)
 

 
 L. Sunil Chandran, Rishikesh Gajjala · arXiv preprint · arXiv:2202.05562

Completely characterizes graphs with matching index 1 or 2, provides an efficient algorithm to compute the matching index, and settles the Krenn–Gu conjecture for a subclass of graphs.
 

 
 
partial Krenn-Gu conjecture for sparse graphs
 (2024)
 

 
 L. Sunil Chandran, Rishikesh Gajjala, Abraham M. Illickan · Mathematical Foundations of Computer Science (MFCS 2024) · arXiv:2407.00303 · doi:10.4230/LIPIcs.MFCS.2024.41

Proves the Krenn–Gu conjecture for cubic graphs and graphs with vertex connectivity at most 2, and establishes that any minimal counterexample must be 4-connected.
 

 

 Reviewer notes. The Krenn blog (mariokrenn.wordpress.com) reports additional partial results from April 2023 (in simple graphs, monochromatic structures cannot occur when the maximum degree exceeds n/√2) and September 2023 (for n=4, d=4 is impossible), attributed to individual researchers but not found as standalone verifiable arXiv papers; these may be incorporated into the revised version of 2202.05562 (revised November 2023). The €3,000 prize for a full proof or counterexample remained unclaimed as of the search date.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. For which values of $ n $ and $ d $ are there bi-colored graphs on $ n $ vertices and $ d $ different colors with the property that all the $ d $ monochromatic colorings have unit weight, and every other coloring cancels out?

Discussion

Background : This and many related questions are directly inspired from quantum physics, and their solutions would directly contribute to new understanding in quantum physics. Bi-Colored Graph : A bi-colored weighted graph $ G=(V(G),E(G)) $ , on $ n $ vertices with $ d $ colors is an undirected, not necessarily simple graph where there is a fixed ordering of the vertices $ V(G)=v_1, \ldots, v_n $ and to each edge $ e \in E(G) $ there is a complex weight $ w_e $ and an ordered pair of (not necessarily different) colors $ (c_1(e),c_2(e)) $ associated with it from the $ d $ possible colors. We say that an edge is monochromatic if the associated pair of colors are not different, otherwise the edge is bi-chromatic. Moreover, if $ e $ is an edge incident to the vertices $ v_i,v_j \in V(G) $ with $ i<j $ and the associated ordered pair of colors to $ e $ is $ (c_1(e),c_2(e)) $ then we say that $ e $ is colored $ c_1 $ at $ v_i $ and $ c_2 $ at $ v_j $ . We will be interested in a special coloring of this graph: Inherited Vertex Coloring : Let $ G $ be a bi-colored weighted graph and $ PM $ denote a perfect matching in $ G $ . We associate a coloring of the vertices of G with PM in the natural way: for every vertex $ v_i $ there is a single edge $ e(v_i) \in PM $ that is incident to $ v_i $ , let the color of $ v_i $ be the color of $ e(v_i) $ at $ v_i $ . We call this coloring $ c $ , the inherited vertex coloring (IVC) of the perfect matching PM. Now we are ready to define how constructive and destructive interference during an experiment is governed by perfect matchings of a bi-colored graph. Weight of Vertex Coloring : Let $ G $ be a bi-colored weighted graph. Let $ \mathcal{M} $ be the set of perfect matchings of $ G $ which have the coloring $ c $ as their inherited vertex coloring. We define the weight of $ c $ as $$w(c) := \sum_{PM \in \mathcal{M}} \prod_{e \in PM}w_e. $$ Moreover, if $ w(c) $ =1 we say that the coloring gets unit weight, and if $ w(c) $ =0 we say that the coloring cancels out.

Bibliography

 [?]
 Questions on the Structure of Perfect Matchings inspired by Quantum Physics
 Questions on the Structure of Perfect Matchings inspired by Quantum Physics
