Attack the following open graph-theory problem.

Catalog id: weighted_colouring_of_hexagonal_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/weighted_colouring_of_hexagonal_graphs/
Original entry: http://www.openproblemgarden.org/op/weighted_colouring_of_hexagonal_graphs
Problem attributed to: McDiarmid, Colin, Reed, Bruce A. (posted 2013-03-13)

=== Problem statement (OpenProblemGarden) ===
Title: Weighted colouring of hexagonal graphs.
Conjecture There is an absolute constant $ c $ such that for every hexagonal graph $ G $ and vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ , $$\chi(G,p) \leq \frac{9}{8}\omega(G,p) + c $$

=== Discussion / context (OpenProblemGarden) ===
A hexagonal graph is an induced subgraph of the triangular lattice. The triangular lattice $ TL $ may be described as follows. The vertices are all integer linear combinations $ a\mathbf{e_1} + b\mathbf{e_2} $ of the two vectors $ \mathbf{e_1}=(1,0) $ and $ \mathbf{e_2}=(\frac{1}{2}, \frac{\sqrt{3}}{2}) $ . Two vertices are adjacent when the Euclidean distance between them is 1. Let $ G $ be a graph and $ p $ a vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ . The weighted clique number of $ (G,p) $ , denoted by $ \omega(G,p) $ , is the maximum weight of a clique, that is $ \max \{p(C) \tq C \mbox{ clique of } G\} $ , where $ p(C)=\sum_{v\in C} p(v) $ . A $ k $ -colouring of a $ (G,p) $ is a mapping $ C:V(G)\ra {\cal P}(\{1, \dots , k\}) $ such that for every vertex $ v\in V(G) $ , $ |C(v)|=p(v) $ and for all edge $ uv\in E(G) $ , $ C(u)\cap C(v)=\emptyset $ . The chromatic number of $ (G,p) $ , denoted by $ \chi(G,p) $ , is the least integer $ t $ such that $ (G,p) $ admits a $ t $ -colouring. The conjecture would be tight because of $ C_9 $ the cycle of length 9. The maximum size of stable set in $ C_9 $ is $ 4 $ . Thus $ \chi(C_9,\mathbf{k})\geq 9k/4 $ and $ \omega(G,\mathbf{k})=2k $ , where $ \mathbf{k} $ is the all $ k $ function. McDiarmid and Reed [MR] proved that $ \chi(G,p)\leq \frac{4\omega(G,p)+1}{3} $ for any hexagonal graph $ G $ and vertex weighting $ p $ . Havet [H] proved that if a hexagonal graph $ G $ is triangle-free, then $ \chi(G,p)\leq\frac{7}{6}\omega(G,p) + 5 $ (See also [SV]). The conjecture would be implied by the following one, where $ \mathbf{4} $ is the all $ 4 $ function. Conjecture $ \chi(G,\mathbf{4})\leq 9 $ for every hexagonal graph. Since $ \chi(G,\mathbf{4}) \geq 4|V(G)|/\alpha(G) $ , where $ \alpha(G) $ is the stability number (the maximum size of a stable set). A first step to this later conjecture would be to prove the following conjecture of McDiarmid. Conjecture Let $ G $ be a triangle-free hexagonal graph. $$\alpha(G)\geq \frac{4}{9}|V(G)|$$

=== References listed by OpenProblemGarden ===
- [H] F.Havet. Channel assignment and multicolouring of the induced subgraphs of the triangular lattice. Discrete Mathematics 233:219--231, 2001.
- *[MR] C. McDiarmid and B. Reed. Channel assignment and weighted coloring, Networks, 36:114--117, 2000.
- [SV] K. S. Sudeep and S. Vishwanathan. A technique for multicoloring triangle-free hexagonal graphs. Discrete Mathematics, 300(1-3), 256--259, 2005.

=== Catalog page (statement + literature review) ===
Weighted colouring of hexagonal graphs. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that $\chi(G,p) \leq \frac{9}{8}\omega(G,p) + c$ for every hexagonal graph remains open. Žerovnik (2016) improved the best-known upper bound on the asymptotic ratio from $\frac{4}{3}$ (McDiarmid–Reed 2000) to $\frac{5}{4}$, showing $\chi(G,p) \leq 15\lfloor\omega(G,p)/12\rfloor + 18$. Godin and Togni (2018) developed reducible-configuration techniques and provided computational evidence that the implied $(9,4)$-colorability sub-conjecture holds across millions of randomly generated triangle-free hexagonal graphs, though no complete proof has appeared.

 Cited literature (2)

 
 
 
partial Improved approximative multicoloring of hexagonal graphs
 (2016)
 

 
 Janez Žerovnik · arXiv preprint · arXiv:1606.01328 · doi:10.48550/arXiv.1606.01328

Improves the best-known asymptotic ratio from 4/3 to 5/4, establishing χ(G,p) ≤ 15⌊ω(G,p)/12⌋ + 18 for every hexagonal graph.
 

 
 
partial New reducible configurations for graph multicoloring with application to the experimental resolution of McDiarmid-Reed's Conjecture (extended version)
 (2018)
 

 
 Jean-Christophe Godin, Olivier Togni · arXiv preprint · arXiv:1812.01911

Develops reducible-configuration tools for (a,b)-colorings and provides computational evidence that all tested triangle-free induced subgraphs of the triangular lattice are (9,4)-colorable.
 

 

 Reviewer notes. The Žerovnik 2016 paper was listed as 'submitted to Information Processing Letters' but journal publication could not be confirmed; cited as arXiv preprint. The Godin–Togni paper (1812.01911) was last revised October 2023 but remains without a confirmed journal publication. A DMTCS 2013 paper by Witkowski–Žerovnik on a 33/24-competitive distributed algorithm is related but addresses a different competitive-ratio setting (not the conjecture directly). No proof or disproof of the full conjecture was found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. There is an absolute constant $ c $ such that for every hexagonal graph $ G $ and vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ , $$\chi(G,p) \leq \frac{9}{8}\omega(G,p) + c $$

Discussion

A hexagonal graph is an induced subgraph of the triangular lattice. The triangular lattice $ TL $ may be described as follows. The vertices are all integer linear combinations $ a\mathbf{e_1} + b\mathbf{e_2} $ of the two vectors $ \mathbf{e_1}=(1,0) $ and $ \mathbf{e_2}=(\frac{1}{2}, \frac{\sqrt{3}}{2}) $ . Two vertices are adjacent when the Euclidean distance between them is 1. Let $ G $ be a graph and $ p $ a vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ . The weighted clique number of $ (G,p) $ , denoted by $ \omega(G,p) $ , is the maximum weight of a clique, that is $ \max \{p(C) \tq C \mbox{ clique of } G\} $ , where $ p(C)=\sum_{v\in C} p(v) $ . A $ k $ -colouring of a $ (G,p) $ is a mapping $ C:V(G)\ra {\cal P}(\{1, \dots , k\}) $ such that for every vertex $ v\in V(G) $ , $ |C(v)|=p(v) $ and for all edge $ uv\in E(G) $ , $ C(u)\cap C(v)=\emptyset $ . The chromatic number of $ (G,p) $ , denoted by $ \chi(G,p) $ , is the least integer $ t $ such that $ (G,p) $ admits a $ t $ -colouring. The conjecture would be tight because of $ C_9 $ the cycle of length 9. The maximum size of stable set in $ C_9 $ is $ 4 $ . Thus $ \chi(C_9,\mathbf{k})\geq 9k/4 $ and $ \omega(G,\mathbf{k})=2k $ , where $ \mathbf{k} $ is the all $ k $ function. McDiarmid and Reed [MR] proved that $ \chi(G,p)\leq \frac{4\omega(G,p)+1}{3} $ for any hexagonal graph $ G $ and vertex weighting $ p $ . Havet [H] proved that if a hexagonal graph $ G $ is triangle-free, then $ \chi(G,p)\leq\frac{7}{6}\omega(G,p) + 5 $ (See also [SV]). The conjecture would be implied by the following one, where $ \mathbf{4} $ is the all $ 4 $ function. Conjecture $ \chi(G,\mathbf{4})\leq 9 $ for every hexagonal graph. Since $ \chi(G,\mathbf{4}) \geq 4|V(G)|/\alpha(G) $ , where $ \alpha(G) $ is the stability number (the maximum size of a stable set). A first step to this later conjecture would be to prove the following conjecture of McDiarmid. Conjecture Let $ G $ be a triangle-free hexagonal graph. $$\alpha(G)\geq \frac{4}{9}|V(G)|$$

Bibliography

 [H]
 F.Havet. Channel assignment and multicolouring of the induced subgraphs of the triangular lattice . Discrete Mathematics 233:219--231, 2001.
 Channel assignment and multicolouring of the induced subgraphs of the triangular lattice

★ [MR]
 C. McDiarmid and B. Reed. Channel assignment and weighted coloring, Networks, 36:114--117, 2000.

 [SV]
 K. S. Sudeep and S. Vishwanathan. A technique for multicoloring triangle-free hexagonal graphs . Discrete Mathematics, 300(1-3), 256--259, 2005.
 A technique for multicoloring triangle-free hexagonal graphs
