Attack the following open graph-theory problem.

Catalog id: oriented_trees_in_n_chromatic_digraphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/oriented_trees_in_n_chromatic_digraphs/
Original entry: http://www.openproblemgarden.org/op/oriented_trees_in_n_chromatic_digraphs
Problem attributed to: Burr, S. A. (posted 2013-02-25)

=== Problem statement (OpenProblemGarden) ===
Title: Oriented trees in n-chromatic digraphs
Conjecture Every digraph with chromatic number at least $ 2k-2 $ contains every oriented tree of order $ k $ as a subdigraph.

=== Discussion / context (OpenProblemGarden) ===
The conjectured bound is best possible, because a regular tournament of order $ 2k-3 $ does not contain the oriented tree consisting of a vertex dominating $ k-1 $ leaves. Let $ f $ be the function $ f $ such that every oriented tree of order $ k $ is $ f(k) $ -universal, that is contained in every digraph with chromatic number at least $ f(k) $ . Burr proved that $ f(k) \leq (k-1)^2 $ . This was slightly improved by Addario-Berry et al. [AHL+] who proved $ f(k)\leq k^2/2-k/2+1 $ . Burr's conjecture has been proved only in few particular cases of digraphs: tournaments, and acyclic digraphs. Kühn, Mycroft, and Osthus [KMS] showed that every oriented tree of order $ k $ is contained in every tournament of order $ 2k-2 $ for all sufficiently large $ k $ (so proving a Conjecture of Sumner); Addario-Berry et al. [AHL+] proved that every acyclic digraph with chromatic number $ k $ contains every oriented tree of order $ k $ . Burr's conjecture or some approximation have been also proved for special classes of trees. Gallai-Roy's celebrated theorem states that every directed path of order $ k $ is $ k $ -universal; El-Sahili [E] proved that every oriented path of order $ 4 $ is $ 4 $ -universal and that the antidirected path of order $ 5 $ is $ 5 $ -universal; Addario-Berry, Havet, and Thomassé [AHT] showed that every oriented path of order $ k $ whose vertex set can be partioned into two directed paths is $ k $ -universal; Addario-Berry et al. [AHL+] showed that antidirected trees (oriented trees in which every vertex has in-degree $ 0 $ or out-degree $ 0 $ ) are $ 5k $ -universal. Havet, generalizing a conjecture of Havet and Thomassé (see [H]) on tournaments, conjectured that the following could also be true. Conjecture Every digraph with chromatic number at least $ k+\ell+1 $ contains every oriented tree of order $ k $ with $ k $ leaves.

=== References listed by OpenProblemGarden ===
- [AHL+] L. Addario-Berry, F. Havet, C. Linhares Sales, B. Reed, and S. Thomassé. Oriented trees in digraphs. Discrete Mathematics, 313(8):967-974, 2013.
- [AHT] L. Addario-Berry, F. Havet, and S. Thomassé, Paths with two blocks in -chromatic digraphs, J. of Combinatorial Theory Ser. B, 97 (2007), 620--626.
- * [B] A. Burr, Subtrees of directed graphs and hypergraphs, Proceedings of the Eleventh Southeastern Conference on Combinatorics, Graph Theory and Computing, Boca Raton, Congr. Numer., 28 (1980), 227--239.
- [H] F. Havet, Trees in tournaments. Discrete Mathematics 243 (2002), no. 1-3, 121--134.
- [KOM] D. Kühn, D. Osthus, and R. Mycroft, A proof of Sumner's universal tournament conjecture for large tournaments, Proceedings of the London Mathematical Society 102 (2011), 731--766.

=== Catalog page (statement + literature review) ===
Oriented trees in n-chromatic digraphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Burr's conjecture (every $(2k-2)$-chromatic digraph contains every oriented tree of order $k$) remains open in full generality. The strongest general upper bound has been improved from quadratic to subquadratic: Bessy, Gonçalves, and Reinald (2024) proved that every digraph with chromatic number $8\sqrt{2/15}\,k\sqrt{k}+O(k)$ contains any oriented tree of order $k$, the first subquadratic bound. A 2024 survey by Stein provides a comprehensive review of the state of the problem.

 Cited literature (2)

 
 
 
partial Oriented trees in O(k√k)-chromatic digraphs, a subquadratic bound for Burr's conjecture
 (2024)
 

 
 Stéphane Bessy, Daniel Gonçalves, Amadeus Reinald · Graph-Theoretic Concepts in Computer Science (WG 2024), Springer LNCS 15153 · arXiv:2402.19351 · doi:10.1007/978-3-031-75409-8_6

First subquadratic bound for Burr's conjecture: every digraph with chromatic number $8\sqrt{2/15}\,k\sqrt{k}+O(k)$ contains any oriented tree of order $k$; also gives improved bounds for arborescences ($\sqrt{4/3}\,k\sqrt{k}+O(k)$) and paths on $b$ blocks ($(b-1)(k-3)+3$).
 

 
 
survey Oriented trees and paths in digraphs
 (2024)
 

 
 Maya Stein · Surveys in Combinatorics 2024, Cambridge University Press · arXiv:2310.18719 · doi:10.1017/9781009490559.010

Comprehensive survey of conditions (chromatic number, edge density, minimum out-degree, semidegree) guaranteeing the presence of all oriented paths or trees of given order in a digraph, including the status of Burr's conjecture and related open problems.
 

 

 Reviewer notes. The Springer chapter link (10.1007/978-3-031-75409-8_6) redirected to an auth wall and could not be fetched directly; venue confirmed from the arXiv abstract metadata. The 2025 Yuster paper (arXiv:2512.21950) on acyclic subgraphs of high-chromatic digraphs is tangentially related but does not directly advance Burr's conjecture. The conjecture remains fully open at the stated bound of $2k-2$.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. Every digraph with chromatic number at least $ 2k-2 $ contains every oriented tree of order $ k $ as a subdigraph.

Discussion

The conjectured bound is best possible, because a regular tournament of order $ 2k-3 $ does not contain the oriented tree consisting of a vertex dominating $ k-1 $ leaves. Let $ f $ be the function $ f $ such that every oriented tree of order $ k $ is $ f(k) $ -universal, that is contained in every digraph with chromatic number at least $ f(k) $ . Burr proved that $ f(k) \leq (k-1)^2 $ . This was slightly improved by Addario-Berry et al. [AHL+] who proved $ f(k)\leq k^2/2-k/2+1 $ . Burr's conjecture has been proved only in few particular cases of digraphs: tournaments, and acyclic digraphs. Kühn, Mycroft, and Osthus [KMS] showed that every oriented tree of order $ k $ is contained in every tournament of order $ 2k-2 $ for all sufficiently large $ k $ (so proving a Conjecture of Sumner); Addario-Berry et al. [AHL+] proved that every acyclic digraph with chromatic number $ k $ contains every oriented tree of order $ k $ . Burr's conjecture or some approximation have been also proved for special classes of trees. Gallai-Roy's celebrated theorem states that every directed path of order $ k $ is $ k $ -universal; El-Sahili [E] proved that every oriented path of order $ 4 $ is $ 4 $ -universal and that the antidirected path of order $ 5 $ is $ 5 $ -universal; Addario-Berry, Havet, and Thomassé [AHT] showed that every oriented path of order $ k $ whose vertex set can be partioned into two directed paths is $ k $ -universal; Addario-Berry et al. [AHL+] showed that antidirected trees (oriented trees in which every vertex has in-degree $ 0 $ or out-degree $ 0 $ ) are $ 5k $ -universal. Havet, generalizing a conjecture of Havet and Thomassé (see [H]) on tournaments, conjectured that the following could also be true. Conjecture Every digraph with chromatic number at least $ k+\ell+1 $ contains every oriented tree of order $ k $ with $ k $ leaves.

Bibliography

 [AHL+]
 L. Addario-Berry, F. Havet, C. Linhares Sales, B. Reed, and S. Thomassé. Oriented trees in digraphs. Discrete Mathematics, 313(8):967-974, 2013.

 [AHT]
 L. Addario-Berry, F. Havet, and S. Thomassé, Paths with two blocks in $ n $ -chromatic digraphs, J. of Combinatorial Theory Ser. B, 97 (2007), 620--626.

★ [B]
 A. Burr, Subtrees of directed graphs and hypergraphs, Proceedings of the Eleventh Southeastern Conference on Combinatorics, Graph Theory and Computing, Boca Raton, Congr. Numer., 28 (1980), 227--239.

 [H]
 F. Havet, Trees in tournaments. Discrete Mathematics 243 (2002), no. 1-3, 121--134.

 [KOM]
 D. Kühn, D. Osthus, and R. Mycroft, A proof of Sumner's universal tournament conjecture for large tournaments, Proceedings of the London Mathematical Society 102 (2011), 731--766.

Related conjectures

 
 implies
 χ-Mader bound for oriented trees
 solved
 mader_chi(T) is the least c such that every digraph with (underlying) chromatic number at least c contains a subdivision of T. Burr's conjecture asserts that chromatic number at least 2k-2 forces every oriented tree T of order k as a subdigraph; a copy of T is a trivial subdivision of T, hence chi >= 2k-2 forces a subdivision of T, i.e. mader_chi(T) <= 2k-2. Both statements use the chromatic number of the underlying graph, and the target's context explicitly states it is 'a direct consequence' of Burr's Conjecture 10. Direction correct: Burr's conjecture is the stronger statement.
 

 
 related to
 Antidirected trees in digraphs
 partial
 The OPG page explicitly states and proves that the Addario-Berry et al. conjecture implies Burr's conjecture ONLY for antidirected trees: chi(D) >= 2k-2 yields a colour-critical subdigraph of min degree >= 2k-3, hence arc density > (k-2)|V|, triggering the source conjecture. But Burr's conjecture concerns ALL oriented trees, so the source does not imply the full target (subfamily-only implication). The converse also fails: high arc density does not force high chromatic number (bipartite digraphs with all arcs one way have chi=2 and arbitrary density, as the source context notes). Genuine partial-implication link, but no full implication in either direction, so related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
