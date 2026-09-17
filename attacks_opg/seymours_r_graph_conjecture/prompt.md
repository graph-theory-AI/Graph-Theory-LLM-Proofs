Attack the following open graph-theory problem.

Catalog id: seymours_r_graph_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/seymours_r_graph_conjecture/
Original entry: http://www.openproblemgarden.org/op/seymours_r_graph_conjecture
Problem attributed to: Seymour, Paul D. (posted 2008-10-03)

=== Problem statement (OpenProblemGarden) ===
Title: Seymour's r-graph conjecture
An $ r $ - graph is an $ r $ -regular graph $ G $ with the property that $ |\delta(X)| \ge r $ for every $ X \subseteq V(G) $ with odd size. Conjecture $ \chi'(G) \le r+1 $ for every $ r $ -graph $ G $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is among the most important unsolved problems in edge coloring. It is very close in nature to Goldberg's Conjecture , and is also closely related to Rizzi's packing postman sets conjecture (see packing T-joins ). If $ G $ is an $ r $ -regular graph and there exists $ X \subseteq V(G) $ with $ |X| $ odd and $ |\delta(X)| < r $ , then it is immediate that $ G $ is not $ r $ -edge-colourable, since every perfect matching must use at least one edge from $ \delta(X) $ . This is in some sense the only obvious obstruction to $ r $ -edge-colorability that we know of. So, $ r $ -graphs are the $ r $ -regular graphs which do not fail to be $ r $ -edge-colorable for this obvious reason. Not every $ r $ -graph is $ r $ -edge-colorable, for instance Petersen's graph is a 3-graph which is not 3-edge-colorable. However, this conjecture asserts that all such graphs are still $ (r+1) $ -edge-colorable. This conjecture has been proved for $ r \le 11 $ by Nishizeki and Kashiwagi [NK].

=== References listed by OpenProblemGarden ===
- [NK] T. Nishizeki and K. Kashiwagi, An upper bound on the chromatic index of multigraphs. Graph theory with applications to algorithms and computer science (Kalamazoo, Mich., 1984), 595--604, Wiley-Intersci. Publ., Wiley, New York, 1985. MathSciNet.
- *[S] P.D. Seymour, On multicolourings of cubic graphs, and conjectures of Fulkerson and Tutte. Proc. London Math. Soc. (3) 38 (1979), no. 3, 423--460. MathSciNet.

=== Catalog page (statement + literature review) ===
Seymour's r-graph conjecture — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 Seymour's r-graph conjecture is a direct corollary of the Goldberg–Seymour conjecture: for any $r$-graph $G$, the condition $|\delta(X)| \ge r$ for every odd $X \subseteq V(G)$ forces $\Gamma(G) \le r$, so the Goldberg–Seymour bound $\chi'(G) \le \max\{\Delta(G)+1, \lceil\Gamma(G)\rceil\}$ reduces to $\chi'(G) \le r+1$. The Goldberg–Seymour conjecture was proved by Chen, Jing, and Zang (2019 preprint; journal version 2025), resolving Seymour's r-graph conjecture as an immediate consequence.

 Cited literature (1)

 
 
 
proof Proof of the Goldberg-Seymour Conjecture on Edge-Colorings of Multigraphs
 (2025)
 

 
 Guantao Chen, Guangming Jing, Wenan Zang · Journal of Combinatorial Optimization · arXiv:1901.10316 · doi:10.1007/s10878-025-01348-6

Proves the Goldberg–Seymour conjecture χ'(G) ≤ max{Δ(G)+1, ⌈Γ(G)⌉} for all multigraphs G; since every r-graph satisfies Γ(G) ≤ r (the r-graph condition bounds subgraph density), this immediately yields χ'(G) ≤ r+1 for every r-graph, resolving Seymour's r-graph conjecture. The proof first appeared as arXiv:1901.10316 in 2019.
 

 

 Reviewer notes. The implication 'Goldberg–Seymour ⟹ r-graph conjecture' is standard: r-regularity gives Δ(G)=r, and for any odd set X the r-graph condition |δ(X)|≥r forces 2|E(G[X])| ≤ r(|X|-1), bounding Γ(G) ≤ r. A search summary mentioned Scheide (2007) made this implication explicit, but the Scheide reference was not independently verified by WebFetch. The Chen-Jing-Zang proof of Goldberg-Seymour first appeared as arXiv:1901.10316 in 2019 and is now verified via the 2025 Journal of Combinatorial Optimization article, DOI 10.1007/s10878-025-01348-6. A related 2023 survey (arXiv:2308.15588, Jing) discusses the Goldberg–Seymour conjecture algorithmically but did not explicitly mention the r-graph conjecture in the retrievable content.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. $ \chi'(G) \le r+1 $ for every $ r $ -graph $ G $ .

Keywords:
edge-coloring · r-graph

Discussion

This conjecture is among the most important unsolved problems in edge coloring. It is very close in nature to Goldberg's Conjecture , and is also closely related to Rizzi's packing postman sets conjecture (see packing T-joins ). If $ G $ is an $ r $ -regular graph and there exists $ X \subseteq V(G) $ with $ |X| $ odd and $ |\delta(X)| < r $ , then it is immediate that $ G $ is not $ r $ -edge-colourable, since every perfect matching must use at least one edge from $ \delta(X) $ . This is in some sense the only obvious obstruction to $ r $ -edge-colorability that we know of. So, $ r $ -graphs are the $ r $ -regular graphs which do not fail to be $ r $ -edge-colorable for this obvious reason. Not every $ r $ -graph is $ r $ -edge-colorable, for instance Petersen's graph is a 3-graph which is not 3-edge-colorable. However, this conjecture asserts that all such graphs are still $ (r+1) $ -edge-colorable. This conjecture has been proved for $ r \le 11 $ by Nishizeki and Kashiwagi [NK].

Bibliography

 [NK]
 T. Nishizeki and K. Kashiwagi, An upper bound on the chromatic index of multigraphs. Graph theory with applications to algorithms and computer science (Kalamazoo, Mich., 1984), 595--604, Wiley-Intersci. Publ., Wiley, New York, 1985. MathSciNet .
 MathSciNet

★ [S]
 P.D. Seymour, On multicolourings of cubic graphs, and conjectures of Fulkerson and Tutte. Proc. London Math. Soc. (3) 38 (1979), no. 3, 423--460. MathSciNet .
 MathSciNet

Related conjectures

 
 implied by
 Goldberg's conjecture
 solved
 Let G be an r-graph, so Δ(G) = r. For any subgraph H with |V(H)| = 2k+1 odd (k ≥ 1): the degree sum over V(H) in G is r(2k+1), and the odd-cut condition forces at least r edge-ends to leave V(H), so |E(H)| ≤ |E(G[V(H)])| ≤ (r(2k+1) − r)/2 = rk, giving ⌈|E(H)|/⌊|V(H)|/2⌋⌉ ≤ r. For even |V(H)| = 2k, r-regularity gives |E(H)| ≤ rk, ratio ≤ r. Hence w(G) ≤ r, and Goldberg's bound χ' ≤ max{Δ+1, w} = max{r+1, r} = r+1 is exactly Seymour's conjecture. This also matches the OPG context, which notes Seymour's conjecture is equivalent to χ' ≤ max{Δ, w} + 1, a consequence of Goldberg's bound since max{Δ+1, w} ≤ max{Δ, w} + 1. Direction correct: Goldberg (all multigraphs) is stronger.
 

 
 related to
 Packing T-joins
 partial
 The mention says Seymour's r-graph conjecture 'is also closely related to Rizzi's packing postman sets conjecture (see packing T-joins)'. The target page's headline conjecture is about general grafts ((2/3)k - c disjoint T-joins), which Seymour's conjecture (chi' <= r+1 for r-graphs) cannot imply: it concerns arbitrary grafts, not r-regular graphs with T=V. Even for Rizzi's r-graph subcase (r-2 disjoint T-joins), an (r+1)-edge-coloring yields matchings that need not be perfect, hence not T-joins, so no direct implication follows; the pages assert closeness 'in nature' only. Both live in the same circle of ideas (Goldberg, r-graphs, matching/T-join decompositions) without a proven implication either way.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
