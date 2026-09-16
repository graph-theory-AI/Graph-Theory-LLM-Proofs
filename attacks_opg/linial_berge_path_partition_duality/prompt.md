Attack the following open graph-theory problem.

Catalog id: linial_berge_path_partition_duality
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/linial_berge_path_partition_duality/
Original entry: http://www.openproblemgarden.org/op/linial_berge_path_partition_duality
Problem attributed to: Berge, Claude, Linial, Nathan (posted 2007-03-27)

=== Problem statement (OpenProblemGarden) ===
Title: Linial-Berge path partition duality
Conjecture The minimum $ k $ -norm of a path partition on a directed graph $ D $ is no more than the maximal size of an induced $ k $ -colorable subgraph.

=== Discussion / context (OpenProblemGarden) ===
Definitions: Let $ D $ be a directed graph. A path partition of $ D $ is a set of vertex disjoint paths in it (some might be singletons), covering all vertices. Let $ k $ be a positive integer. The $ k $ norm of a path partition is the sum of $ \min\{|V(P)|,k\} $ for all paths $ P $ in it. This conjecture is known for acyclic graphs and for $ k =1,2 $ .

=== Catalog page (statement + literature review) ===
Linial-Berge path partition duality — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Linial-Berge path partition duality conjecture remains open for general directed graphs. After the problem was posted, the conjecture was proved for $k=2$ (Berger and Hartman, 2008) and for locally in/out-semicomplete digraphs (Sambinelli et al., 2019). A 2026 arXiv paper (de Paula Silva, da Silva, and Lee) establishes relaxations of both Linial conjectures by replacing stable sets with induced acyclic subdigraphs, but the original conjecture for arbitrary $k$ and general digraphs remains open.

 Cited literature (3)

 
 
 
partial Proof of Berge's strong path partition conjecture for k=2
 (2008)
 

 
 Eli Berger, Irith Ben-Arroyo Hartman · European Journal of Combinatorics

Proves Berge's stronger path partition conjecture (which implies Linial's conjecture) for all digraphs when k=2, settling the first non-trivial open case after k=1.
 

 
 
partial Berge's Conjecture and Aharoni-Hartman-Hoffman's Conjecture for locally in-semicomplete digraphs
 (2019)
 

 
 Maycon Sambinelli, Carla Negri Lintzmayer, Cândida Nunes da Silva, Orlando Lee · Graphs and Combinatorics · arXiv:1708.06691 · doi:10.1007/s00373-019-02046-x

Proves Berge's path partition conjecture (and the related Aharoni-Hartman-Hoffman conjecture) for the class of locally in/out-semicomplete digraphs.
 

 
 
partial Orthogonality between acyclic subdigraphs and paths in digraphs
 (2026)
 

 
 Caroline A. de Paula Silva, Cândida Nunes da Silva, Orlando Lee · arXiv preprint · arXiv:2603.17115

Proves relaxations of both of Linial's 1981 conjectures (including the path partition duality conjecture) by replacing stable sets with induced acyclic subdigraphs, establishing new orthogonality theorems that generalize the Gallai-Milgram and Gallai-Hasse-Roy-Vitaver theorems.
 

 

 Reviewer notes. Multiple papers about a different 'Berge α-diperfect conjecture' (which concerns anti-directed odd cycles as forbidden induced subdigraphs) appeared in searches; these are distinct from the Linial-Berge path partition duality and were excluded. The Herskovics paper proving the conjecture for k ≥ λ-3 (published ca. 2015 in Discrete Applied Mathematics, pii S0166218X15003923) is mentioned in multiple reliable secondary sources (EGRES Open, Discrete Math survey) but could not be directly verified via WebFetch (ScienceDirect and ResearchGate both returned 403); it is therefore omitted from since_posted but is credible. The DOI 10.1007/s00373-019-02046-x for the Sambinelli et al. paper was found in search results and matches the Springer Graphs and Combinatorics 2019 link; the arXiv version was directly verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. The minimum $ k $ -norm of a path partition on a directed graph $ D $ is no more than the maximal size of an induced $ k $ -colorable subgraph.

Keywords:
coloring · directed path · partition

Discussion

Definitions: Let $ D $ be a directed graph. A path partition of $ D $ is a set of vertex disjoint paths in it (some might be singletons), covering all vertices. Let $ k $ be a positive integer. The $ k $ norm of a path partition is the sum of $ \min\{|V(P)|,k\} $ for all paths $ P $ in it. This conjecture is known for acyclic graphs and for $ k =1,2 $ .
