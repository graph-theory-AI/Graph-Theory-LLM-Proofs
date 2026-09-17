Attack the following open graph-theory problem.

Catalog id: antidirected_trees_in_digraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/antidirected_trees_in_digraphs/
Original entry: http://www.openproblemgarden.org/op/antidirected_trees_in_digraphs
Problem attributed to: Addario-Berry, Louigi, Havet, Frédéric, Linhares Sales, Claudia, Reed, Bruce A., Thomassé, Stéphan (posted 2013-02-26)

=== Problem statement (OpenProblemGarden) ===
Title: Antidirected trees in digraphs
An antidirected tree is an orientation of a tree in which every vertex has either indegree 0 or outdergree 0. Conjecture Let $ D $ be a digraph. If $ |A(D)| > (k-2) |V(D)| $ , then $ D $ contains every antidirected tree of order $ k $ .

=== Discussion / context (OpenProblemGarden) ===
The value $ k-2 $ would be best possible, since the oriented tree consisting of a vertex dominating $ k-1 $ other vertices is not contained in any digraph in which every vertex has outdegree $ k-2 $ . The condition on the trees be antidirected cannot be suppressed. In a bipartite digraph $ D $ with bipartition $ (A,B) $ such that all arcs are directed from $ A $ to $ B $ , all the trees contained in $ D $ are antidirected. This conjecture for symmetric digraphs is equivalent to the celebrated Erdös-Sos conjecture for undirected graphs. (see [E]). Conjecture Let $ G $ be a graph. If $ |E(G)| > \frac{1}{2} (k-2) |V(G)| $ , then $ G $ contains every tree of order $ k $ . Addario-Berry et al. Conjecture also implies Burr's conjecture (see Oriented trees in n-chromatic digraphs ) for antidirected trees, since every digraph with chromatic number $ 2k-2 $ contains a colour-critical digraph has minimum degree at least $ 2k-3 $ , and so whose number of vertices is at least $ \frac{2k-3}{2}|V(D)| $ , which exceeds $ (k-2) |V(D)| $ . This conjecture has only been proved [AHL+] for antidirected trees of diameter at most $ 3 $ .

=== References listed by OpenProblemGarden ===
- *[AHL+] L. Addario-Berry, F. Havet, C. Linhares Sales, B. Reed, and S. Thomassé. Oriented trees in digraphs. Discrete Mathematics, 313(8):967-974, 2013.
- [E] P. Erdös, Some problems in graph theory, Theory of Graphs and Its Applications, M. Fielder, Editor, Academic Press, New York, 1965, pp. 29--36.

=== Catalog page (statement + literature review) ===
Antidirected trees in digraphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture remains open in general. The most significant post-2013 advances are: Stein and Trujillo-Negrete (2024) proved the conjecture for all antidirected caterpillars (achieving $|A(D)|>(k-1)|V(D)|$ implies every antidirected $k$-arc caterpillar is present) and for $K_{2,s}$-free digraphs with $s=\lceil k/12\rceil$; Stein and Zárate-Guerén (2022) showed the conjecture is asymptotically true in oriented graphs for all balanced antidirected trees of bounded maximum degree and of size linear in $n$. The full conjecture for arbitrary antidirected trees under pure arc-density conditions is still open.

 Cited literature (5)

 
 
 
partial Antidirected subgraphs of oriented graphs
 (2022)
 

 
 Maya Stein, Camila Zárate-Guerén · arXiv preprint · arXiv:2212.00769

Proves the Addario-Berry et al. conjecture is asymptotically true in $n$-vertex oriented graphs for all balanced antidirected trees of bounded maximum degree and of size linear in $n$, using minimum semidegree $>(1+\eta)(k-1)$ as density surrogate.
 

 
 
partial Semidegree, edge density and antidirected subgraphs
 (2023)
 

 
 Maya Stein, Camila Zárate-Guerén · European Conference on Combinatorics, Graph Theory and Applications (EuroComb 2023)

Conference version presenting asymptotic results for balanced antidirected trees of bounded degree in oriented graphs with high minimum semidegree, addressing the Addario-Berry et al. arc-density conjecture.
 

 
 
survey Oriented trees and paths in digraphs
 (2024)
 

 
 Maya Stein · Surveys in Combinatorics 2024, Cambridge University Press · arXiv:2310.18719

Comprehensive survey covering all known results on oriented tree containment in digraphs; confirms the Addario-Berry et al. conjecture remains open, with the caterpillar case and diameter-$\leq 3$ case as the main resolved classes.
 

 
 
partial Antidirected trees in dense digraphs
 (2024)
 

 
 Maya Stein, Ana Trujillo-Negrete · arXiv preprint · arXiv:2404.10750

Proves the conjecture fully for antidirected caterpillars (every digraph with $>\!(k-1)n$ arcs contains every antidirected $k$-arc caterpillar), and for $K_{2,\lceil k/12\rceil}$-free digraphs under the same arc-density threshold.
 

 
 
partial Antidirected trees in directed graphs
 (2025)
 

 
 George Kontogeorgiou, Giovanne Santos, Maya Stein · arXiv preprint · arXiv:2501.11726

Establishes minimum semidegree and maximum degree conditions (replacing arc-density conditions) that guarantee containment of balanced antidirected trees of bounded maximum degree, extending prior asymptotic results.
 

 

 Reviewer notes. All verified papers use the edge convention 'k arcs in the tree' (i.e., tree order k+1), which is consistent with the OPG formulation after shifting k by 1. The EuroComb 2023 entry (Stein–Zárate-Guerén) may be a conference version of arXiv:2212.00769; if so, only the arXiv paper need be cited. No paper fully resolves the conjecture for all antidirected trees under arc-density conditions. The Klimošová–Stein 2023 result on antidirected paths in oriented graphs was mentioned in the survey but could not be independently verified within the search budget.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 164s.
 

Conjecture. Let $ D $ be a digraph. If $ |A(D)| > (k-2) |V(D)| $ , then $ D $ contains every antidirected tree of order $ k $ .

Discussion

The value $ k-2 $ would be best possible, since the oriented tree consisting of a vertex dominating $ k-1 $ other vertices is not contained in any digraph in which every vertex has outdegree $ k-2 $ . The condition on the trees be antidirected cannot be suppressed. In a bipartite digraph $ D $ with bipartition $ (A,B) $ such that all arcs are directed from $ A $ to $ B $ , all the trees contained in $ D $ are antidirected. This conjecture for symmetric digraphs is equivalent to the celebrated Erdös-Sos conjecture for undirected graphs. (see [E]). Conjecture Let $ G $ be a graph. If $ |E(G)| > \frac{1}{2} (k-2) |V(G)| $ , then $ G $ contains every tree of order $ k $ . Addario-Berry et al. Conjecture also implies Burr's conjecture (see Oriented trees in n-chromatic digraphs ) for antidirected trees, since every digraph with chromatic number $ 2k-2 $ contains a colour-critical digraph has minimum degree at least $ 2k-3 $ , and so whose number of vertices is at least $ \frac{2k-3}{2}|V(D)| $ , which exceeds $ (k-2) |V(D)| $ . This conjecture has only been proved [AHL+] for antidirected trees of diameter at most $ 3 $ .

Bibliography

★ [AHL+]
 L. Addario-Berry, F. Havet, C. Linhares Sales, B. Reed, and S. Thomassé. Oriented trees in digraphs. Discrete Mathematics, 313(8):967-974, 2013.

 [E]
 P. Erdös, Some problems in graph theory, Theory of Graphs and Its Applications, M. Fielder, Editor, Academic Press, New York, 1965, pp. 29--36.

Related conjectures

 
 related to
 Oriented trees in n-chromatic digraphs
 partial
 The OPG page explicitly states and proves that the Addario-Berry et al. conjecture implies Burr's conjecture ONLY for antidirected trees: chi(D) >= 2k-2 yields a colour-critical subdigraph of min degree >= 2k-3, hence arc density > (k-2)|V|, triggering the source conjecture. But Burr's conjecture concerns ALL oriented trees, so the source does not imply the full target (subfamily-only implication). The converse also fails: high arc density does not force high chromatic number (bipartite digraphs with all arcs one way have chi=2 and arbitrary density, as the source context notes). Genuine partial-implication link, but no full implication in either direction, so related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
