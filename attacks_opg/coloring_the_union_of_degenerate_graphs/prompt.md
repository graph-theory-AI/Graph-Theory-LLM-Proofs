Attack the following open graph-theory problem.

Catalog id: coloring_the_union_of_degenerate_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/coloring_the_union_of_degenerate_graphs/
Original entry: http://www.openproblemgarden.org/op/coloring_the_union_of_degenerate_graphs
Problem attributed to: Tarsi, Michael (posted 2013-03-03)

=== Problem statement (OpenProblemGarden) ===
Title: Coloring the union of degenerate graphs
Conjecture The union of a $ 1 $ -degenerate graph (a forest) and a $ 2 $ -degenerate graph is $ 5 $ -colourable.

=== Discussion / context (OpenProblemGarden) ===
A graph is $ k $ -degenerate if it can be reduced to $ K_1 $ (the graph with a unique vertex) by repeatedly deleting vertices of degree at most $ k $ . A $ 1 $ -degenerate graph $ G_1 $ admits a proper $ 2 $ -colouring $ c_1 $ , and a $ 2 $ -degenerate graph $ G_2 $ admits a proper $ 3 $ -colouring $ c_2 $ . Thus, $ (c_1,c_2) $ is a proper $ 6 $ -colouring of $ G_1 $ and $ G_2 $ . The conjecture is tigth because $ K_5 $ is the union of a $ 1 $ -degenerate graph and a $ 2 $ -degenerate graph. Based on a decompostion of the complete graph, Klein and Schönheim [KlSc93] generalised this conjecture to $ (m_1, \dots, m_s) $ -composed graphs, which are unions of $ s $ graphs $ G_1, \dots , G_s $ such that $ G_i $ is $ m_i $ -degenerate, $ 1\leq i\leq s $ . Conjecture Every $ (m_1, \dots, m_s) $ -composed graph is $ \left(\sum_{i=1}^s m_i+\bigg\lfloor\frac{1}{2}\bigg(1+\sqrt{1+8\sum_{1\leq i<j\leq s}m_i m_j}\bigg)\bigg\rfloor\right) $ -colourable. Partial results towards this conjecture are obtained in [KlSc95].

=== References listed by OpenProblemGarden ===
- *[K] R. Klein. On the colorability of {}-composed graphs. Discrete Math. 133 (1994), 181--190.
- [KlSc93] R. Klein and J. Schönheim. Decomposition of {} into degenerate graphs. In Combinatorics and graph theory (Hefei, 1992), pages 141--155. World Sci. Publ., River Edge, NJ, 1993.
- [KlSc95] R. Klein and J. Schönheim. On the colorability of graphs decomposable into degenerate graphs with specified degeneracy. Australas. J. Combin., 12:201--208, 1995.

=== Catalog page (statement + literature review) ===
Coloring the union of degenerate graphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 Tarsi's conjecture that the union of a forest (1-degenerate graph) and a 2-degenerate graph is 5-colorable appears to remain open. No post-2013 paper resolving or substantially advancing the conjecture was found across six targeted searches covering arXiv, web-wide queries, and author-specific terms. The best-known upper bound remains 6, obtained by taking the product of the individual optimal colorings (2-coloring of the forest and 3-coloring of the 2-degenerate graph), and the lower bound $K_5$ shows 5 would be tight.

 Reviewer notes. The OPG problem page (http://www.openproblemgarden.org/op/coloring_the_union_of_degenerate_graphs) returned ECONNREFUSED and could not be fetched directly, so any post-2013 discussion or bibliography updates there were not visible. The Wesleyan thesis PDF (2024) retrieved from Wesleyan's digital collections was unreadable binary data; it might discuss the conjecture but could not be verified. The arXiv paper 2601.15245 ('Coloring small locally sparse degenerate graphs and related problems', January 2026) deals with related degeneracy-coloring questions but does not address this specific conjecture. No other post-2013 candidate paper was found, consistent with the conjecture being an unresolved open problem in the literature.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 136s.
 

Conjecture. The union of a $ 1 $ -degenerate graph (a forest) and a $ 2 $ -degenerate graph is $ 5 $ -colourable.

Discussion

A graph is $ k $ -degenerate if it can be reduced to $ K_1 $ (the graph with a unique vertex) by repeatedly deleting vertices of degree at most $ k $ . A $ 1 $ -degenerate graph $ G_1 $ admits a proper $ 2 $ -colouring $ c_1 $ , and a $ 2 $ -degenerate graph $ G_2 $ admits a proper $ 3 $ -colouring $ c_2 $ . Thus, $ (c_1,c_2) $ is a proper $ 6 $ -colouring of $ G_1 $ and $ G_2 $ . The conjecture is tigth because $ K_5 $ is the union of a $ 1 $ -degenerate graph and a $ 2 $ -degenerate graph. Based on a decompostion of the complete graph, Klein and Schönheim [KlSc93] generalised this conjecture to $ (m_1, \dots, m_s) $ -composed graphs, which are unions of $ s $ graphs $ G_1, \dots , G_s $ such that $ G_i $ is $ m_i $ -degenerate, $ 1\leq i\leq s $ . Conjecture Every $ (m_1, \dots, m_s) $ -composed graph is $ \left(\sum_{i=1}^s m_i+\bigg\lfloor\frac{1}{2}\bigg(1+\sqrt{1+8\sum_{1\leq i<j\leq s}m_i m_j}\bigg)\bigg\rfloor\right) $ -colourable. Partial results towards this conjecture are obtained in [KlSc95].

Bibliography

★ [K]
 R. Klein. On the colorability of { $ m $ }-composed graphs. Discrete Math. 133 (1994), 181--190.

 [KlSc93]
 R. Klein and J. Schönheim. Decomposition of { $ K_n $ } into degenerate graphs. In Combinatorics and graph theory (Hefei, 1992), pages 141--155. World Sci. Publ., River Edge, NJ, 1993.

 [KlSc95]
 R. Klein and J. Schönheim. On the colorability of graphs decomposable into degenerate graphs with specified degeneracy. Australas. J. Combin., 12:201--208, 1995.
