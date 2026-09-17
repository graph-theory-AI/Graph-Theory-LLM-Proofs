Attack the following open graph-theory problem.

Catalog id: goldbergs_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/goldbergs_conjecture/
Original entry: http://www.openproblemgarden.org/op/goldbergs_conjecture
Problem attributed to: Goldberg, Mark K. (posted 2008-10-04)

=== Problem statement (OpenProblemGarden) ===
Title: Goldberg's conjecture
The overfull parameter is defined as follows: \[ w(G) = \max_{H \subseteq G} \left\lceil \frac{ |E(H)| }{ \lfloor \tfrac{1}{2} |V(H)| \rfloor} \right\rceil. \] Conjecture Every graph $ G $ satisfies $ \chi'(G) \le \max\{ \Delta(G) + 1, w(G) \} $ .

=== Discussion / context (OpenProblemGarden) ===
This important problem remains open despite considerable attention. The same conjecture was independently discovered by Andersen and Seymour. Vizing's Theorem, one of the cornerstones of graph colouring, shows that $ \chi'(G) \le \Delta(G) + 1 $ for every simple graph $ G $ . So, in particular, every simple graph satisfies Goldberg's conjecture. Graphs with parallel edges need not satisfy Vizing's bound. For instance, if $ G $ is the graph obtained from a triangle by adding an extra $ k-1 $ edges in parallel with each existing one, then $ \Delta(G) = 2k $ but $ \chi'(G) = 3k $ . More generally, if $ H $ is a subgraph of $ G $ , then every colour can appear on at most $ \lfloor \frac{1}{2}|V(H)| \rfloor $ edges of $ H $ , so $ \chi'(G) \ge |E(H)| / \lfloor \tfrac{1}{2} |V(H)| \rfloor $ . Thus, $ w(G) $ , our overfull parameter, is a natural lower bound on $ \chi'(G) $ , and Goldberg's conjecture asserts that whenever $ \chi'(G) $ exceeds $ \Delta(G)+1 $ , then it is equal to this lower bound. Although the statement of the conjecture may appear to be the most natural formulation, there are a couple of related conjectures with similar lower bounds. For instance, Seymour's r-graph conjecture is equivalent to the statement that $ \chi'(G) \le \max \{\Delta(G), w(G) \} + 1 $ . Goldberg also conjectured that $ \chi'(G) \le \max\{ \Delta(G), w(G) + 1\} $ . In addition to simple graphs, Goldberg's Conjecture is known to hold for any graph $ G $ which satisfies one of the following \item $ \Delta(G) \le 11 $ \item $ G $ has no minor isomorphic to $ K_5 $ minus an edge. \item $ \Delta(G) $ is sufficiently large in comparison with $ |V(G)| $ . $ \quad $ Packers And Movers Chandigarh Packers And Movers Hyderabad Packers And Movers Bangalore

=== References listed by OpenProblemGarden ===
- *[G] M. K. Goldberg, Multigraphs with a chromatic index that is nearly maximal. (Russian) A collection of articles dedicated to the memory of Vitaliĭ Konstantinovič Korobkov. Diskret. Analiz No. 23 (1973), 3--7, 72. MathSciNet

=== Catalog page (statement + literature review) ===
Goldberg's conjecture — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 Goldberg's conjecture (independently posed by Andersen and Seymour) was proved by Chen, Jing, and Zang: their 2019 arXiv proof is now published in Journal of Combinatorial Optimization (2025). In the OPG notation, every multigraph $G$ satisfies $\chi'(G) \le \max\{\Delta(G)+1, w(G)\}$, equivalently $\chi'(G) \in \{\max\{\Delta(G), \lceil \Gamma(G) \rceil\}, \max\{\Delta(G)+1, \lceil \Gamma(G) \rceil\}\}$. A significantly shorter proof, together with a polynomial-time edge-coloring algorithm confirming the Hochbaum-Nishizeki-Shmoys conjecture, was given by Chen, Hao, Yu, and Zang in 2024.

 Cited literature (3)

 
 
 
proof Proof of the Goldberg-Seymour Conjecture on Edge-Colorings of Multigraphs
 (2025)
 

 
 Guantao Chen, Guangming Jing, Wenan Zang · Journal of Combinatorial Optimization · arXiv:1901.10316 · doi:10.1007/s10878-025-01348-6

Proves the Goldberg-Seymour conjecture: every multigraph $G$ satisfies $\chi'(G) \le \max\{\Delta(G)+1, \lceil \Gamma(G) \rceil\}$, settling Goldberg's conjecture in the affirmative. The proof first appeared as arXiv:1901.10316 in 2019.
 

 
 
proof A short proof of the Goldberg-Seymour conjecture
 (2024)
 

 
 Guantao Chen, Yanli Hao, Xingxing Yu, Wenan Zang · arXiv preprint · arXiv:2407.09403

Provides a substantially shorter proof of the Goldberg-Seymour conjecture and an $O(|V|^5|E|^3)$ polynomial-time algorithm computing a $\max\{\Delta(G)+1, \lceil \Gamma(G) \rceil\}$-edge-coloring, also confirming the Hochbaum-Nishizeki-Shmoys conjecture.
 

 
 
partial Goldberg's Conjecture is true for random multigraphs
 (2019)
 

 
 Penny Haxell, Michael Krivelevich, Gal Kronenberg · arXiv preprint · arXiv:1803.00908

Shows Goldberg's conjecture holds (in the stronger form $\chi'(G) = \max\{\Delta(G), \lceil \rho(G) \rceil\}$) for typical random multigraphs in the model $M(n,m)$.
 

 

 Reviewer notes. The OPG-stated conjecture $\chi'(G) \le \max\{\Delta(G)+1, w(G)\}$ is the Goldberg-Seymour conjecture (with $w(G) = \lceil \Gamma(G) \rceil$ the density / overfull parameter). The Chen-Jing-Zang proof first appeared as arXiv:1901.10316 in 2019 and is now verified via the 2025 Journal of Combinatorial Optimization article, DOI 10.1007/s10878-025-01348-6. A short, algorithmic proof by Chen, Hao, Yu, and Zang (arXiv:2407.09403, 2024) further confirms and simplifies the result.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Every graph $ G $ satisfies $ \chi'(G) \le \max\{ \Delta(G) + 1, w(G) \} $ .

Keywords:
edge-coloring · multigraph

Discussion

This important problem remains open despite considerable attention. The same conjecture was independently discovered by Andersen and Seymour. Vizing's Theorem, one of the cornerstones of graph colouring, shows that $ \chi'(G) \le \Delta(G) + 1 $ for every simple graph $ G $ . So, in particular, every simple graph satisfies Goldberg's conjecture. Graphs with parallel edges need not satisfy Vizing's bound. For instance, if $ G $ is the graph obtained from a triangle by adding an extra $ k-1 $ edges in parallel with each existing one, then $ \Delta(G) = 2k $ but $ \chi'(G) = 3k $ . More generally, if $ H $ is a subgraph of $ G $ , then every colour can appear on at most $ \lfloor \frac{1}{2}|V(H)| \rfloor $ edges of $ H $ , so $ \chi'(G) \ge |E(H)| / \lfloor \tfrac{1}{2} |V(H)| \rfloor $ . Thus, $ w(G) $ , our overfull parameter, is a natural lower bound on $ \chi'(G) $ , and Goldberg's conjecture asserts that whenever $ \chi'(G) $ exceeds $ \Delta(G)+1 $ , then it is equal to this lower bound. Although the statement of the conjecture may appear to be the most natural formulation, there are a couple of related conjectures with similar lower bounds. For instance, Seymour's r-graph conjecture is equivalent to the statement that $ \chi'(G) \le \max \{\Delta(G), w(G) \} + 1 $ . Goldberg also conjectured that $ \chi'(G) \le \max\{ \Delta(G), w(G) + 1\} $ . In addition to simple graphs, Goldberg's Conjecture is known to hold for any graph $ G $ which satisfies one of the following \item $ \Delta(G) \le 11 $ \item $ G $ has no minor isomorphic to $ K_5 $ minus an edge. \item $ \Delta(G) $ is sufficiently large in comparison with $ |V(G)| $ . $ \quad $ Packers And Movers Chandigarh Packers And Movers Hyderabad Packers And Movers Bangalore

Bibliography

★ [G]
 M. K. Goldberg, Multigraphs with a chromatic index that is nearly maximal. (Russian) A collection of articles dedicated to the memory of Vitaliĭ Konstantinovič Korobkov. Diskret. Analiz No. 23 (1973), 3--7, 72. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 Seymour's r-graph conjecture
 solved
 Let G be an r-graph, so Δ(G) = r. For any subgraph H with |V(H)| = 2k+1 odd (k ≥ 1): the degree sum over V(H) in G is r(2k+1), and the odd-cut condition forces at least r edge-ends to leave V(H), so |E(H)| ≤ |E(G[V(H)])| ≤ (r(2k+1) − r)/2 = rk, giving ⌈|E(H)|/⌊|V(H)|/2⌋⌉ ≤ r. For even |V(H)| = 2k, r-regularity gives |E(H)| ≤ rk, ratio ≤ r. Hence w(G) ≤ r, and Goldberg's bound χ' ≤ max{Δ+1, w} = max{r+1, r} = r+1 is exactly Seymour's conjecture. This also matches the OPG context, which notes Seymour's conjecture is equivalent to χ' ≤ max{Δ, w} + 1, a consequence of Goldberg's bound since max{Δ+1, w} ≤ max{Δ, w} + 1. Direction correct: Goldberg (all multigraphs) is stronger.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
