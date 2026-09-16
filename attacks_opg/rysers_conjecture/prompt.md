Attack the following open graph-theory problem.

Catalog id: rysers_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Hypergraphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/rysers_conjecture/
Original entry: http://www.openproblemgarden.org/op/rysers_conjecture
Problem attributed to: Ryser, Herbert J. (posted 2007-03-19)

=== Problem statement (OpenProblemGarden) ===
Title: Ryser's conjecture
Conjecture Let $ H $ be an $ r $ - uniform $ r $ -partite hypergraph. If $ \nu $ is the maximum number of pairwise disjoint edges in $ H $ , and $ \tau $ is the size of the smallest set of vertices which meets every edge, then $ \tau \le (r-1) \nu $ .

=== Discussion / context (OpenProblemGarden) ===
Definitions: A (vertex) cover is a set of vertices which meets (has nonempty intersection with) every edge, and we let $ \tau(H) $ denote the size of the smallest vertex cover of $ H $ . A matching is a collection of pairwise disjoint edges, and we let $ \nu(H) $ denote the size of the largest matching in $ H $ . When the hypergraph is clear from context, we just write $ \tau $ or $ \nu $ . It is immediate that $ \nu \le \tau $ , since every cover must contain at least one point from each edge in any matching. For $ r $ -uniform hypergraphs, $ \tau \le r \nu $ , since the union of the edges from any maximal matching is a set of at most $ r \nu $ vertices that which meets every edge. Ryser's conjecture is that this second bound can be improved if $ H $ is $ r $ -uniform and $ r $ -partite (the vertices may be partitioned into $ r $ sets $ V_1,V_2,\ldots,V_r $ so that every edge contains exactly one element of each $ V_i $ ). In the special case when $ r=2 $ our trivial inequality yields $ \nu \le \tau $ and the conjecture implies $ \tau \le \nu $ , so we should have $ \nu = \tau $ . In fact this is true, it is König's theorem on bipartite graphs [K]. Indeed, Ryser's conjecture is probably easiest to view as a high dimensional generalization of this early result of König. Recently, Aharoni [A] has applied the "Hall's theorem for hypergraphs" result of Aharoni and Haxell [AH] to prove this conjecture for $ r=3 $ . However the case $ r=4 $ is still wide open. Some other interesting work on this problem concerns fractional covers and fractional matchings. A fractional cover of $ H = (V,E) $ is a weighting $ a : V \rightarrow {\mathbb R}^+ $ so that $ \sum_{x \in S} a(x) \ge 1 $ for every $ S \in E $ , and the weight of this cover is $ \sum_{x \in V} a(x) $ . The fractional cover number , denoted $ \tau^* $ is the infimum of the set of weights of covers. Similarly, a fractional matching is an edge-weighting $ b : E \rightarrow {\mathbb R}^+ $ so that $ \sum_{S \ni x} b(S) \le 1 $ for every $ x \in V $ , and the weight of this matching is $ \sum_{S \in E} b(S) $ . The fractional matching number , denoted $ \nu^* $ is the supremum of the set of weights of fractional matchings. Fractional covers and matchings are the usual fractional relaxations, and by LP-duality, they satisfy $ \nu^* = \tau^* $ for every hypergraph. For $ r $ -regular $ r $ -partite hypergraphs, Füredi [F] has proved that $ \tau^* \le (r-1)\nu $ and Lovasz [L] has shown $ \tau \le \frac{1}{2} r \nu^* $ .

=== References listed by OpenProblemGarden ===
- [A] R. Aharoni, Ryser's conjecture for tripartite 3-graphs. Combinatorica 21 (2001), no. 1, 1--4. MathSciNet
- [AH] R. Aharoni and P. Haxell, Hall's theorem for hypergraphs. J. Graph Theory 35 (2000), no. 2, 83--88. MathSciNet
- [F] Z. Füredi, Maximum degree and fractional matchings in uniform hypergraphs, Combinatorica 1 (1981), 155--162. MathSciNet
- [K] D. König, Theorie der endlichen und unendlichen Graphen, Leipzig, 1936.
- [L] L. Lovász, On minimax theorems of combinatorics, Ph.D thesis, Matemathikai Lapok 26 (1975), 209--264 (in Hungarian). MathSciNet

=== Catalog page (statement + literature review) ===
Ryser's conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Ryser's conjecture remains open for all $r \geq 4$. The $r = 3$ case was proved by Aharoni in 2001 (before the problem was posted). Since posting, Haxell and Scott (c. 2012) proved the weaker bound $\tau \leq (r - \varepsilon)\nu$ for $r = 4, 5$; DeBiasio et al. (2021) surveyed known results, improved some, and introduced new stronger variants; and Bishnoi et al. (2020) resolved the $t$-intersecting variant for $r \leq \tfrac{36}{7}t - 5$.

 Cited literature (4)

 
 
 
survey Generalizations and strengthenings of Ryser's conjecture
 (2021)
 

 
 Louis DeBiasio, Yigal Kamel, Grace McCourt, Hannah Sheats · Electronic Journal of Combinatorics · arXiv:2009.07239

Surveys known results on Ryser's conjecture (open for $r \geq 4$), improves some bounds, and introduces new stronger conjectures and generalizations to multipartite graphs and hypergraphs.
 

 
 
partial Ryser's Conjecture for $t$-intersecting hypergraphs
 (2020)
 

 
 Anurag Bishnoi, Shagnik Das, Patrick Morris, Tibor Szabó · arXiv preprint · arXiv:2001.04132

Proves the $t$-intersecting variant of Ryser's conjecture ($\tau(\mathcal{H}) \leq r - t$) for all $r \leq \tfrac{36}{7}t - 5$, significantly extending the previously known range.
 

 
 
partial A note on intersecting hypergraphs with large cover number
 (2017)
 

 
 Penny Haxell, Alex Scott · arXiv preprint · arXiv:1609.05458

Constructs $r$-partite $r$-uniform intersecting hypergraphs with cover number at least $r-4$ for all sufficiently large $r$, showing that Ryser's Conjecture is close to best possible for every value of $r$.
 

 
 
partial A Counterexample to a Conjecture of Lovász
 (2025)
 

 
 Alexander Clow, Penny Haxell, Bojan Mohar · arXiv preprint · arXiv:2505.05339

Disproves the conjecture for $r=3$ by exhibiting the line hypergraph of the Biggs-Smith graph (a cubic edge-transitive graph on 102 vertices) as an explicit counterexample; a second counterexample, the line hypergraph of the graph F168D on 168 vertices, is also identified.
 

 

 Reviewer notes. The most significant post-2007 general result is by Haxell and Scott (c. 2012): $\tau(H) \leq (r - \varepsilon)\nu(H)$ for some $\varepsilon > 0$ when $r \in \{4,5\}$ — but the paper PDF at https://people.maths.ox.ac.uk/scott/Papers/ryser.pdf was not machine-readable, so it could not be included as a verified citation. Tuza's result ($\nu=1$, $r \leq 5$) and Aharoni's $r=3$ proof both predate the posting. The Bishnoi et al. paper also appeared in J. Combin. Theory Ser. A (pii/S0097316520301588) but only the arXiv URL was verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Let $ H $ be an $ r $ - uniform $ r $ -partite hypergraph. If $ \nu $ is the maximum number of pairwise disjoint edges in $ H $ , and $ \tau $ is the size of the smallest set of vertices which meets every edge, then $ \tau \le (r-1) \nu $ .

Keywords:
hypergraph · matching · packing

Discussion

Definitions: A (vertex) cover is a set of vertices which meets (has nonempty intersection with) every edge, and we let $ \tau(H) $ denote the size of the smallest vertex cover of $ H $ . A matching is a collection of pairwise disjoint edges, and we let $ \nu(H) $ denote the size of the largest matching in $ H $ . When the hypergraph is clear from context, we just write $ \tau $ or $ \nu $ . It is immediate that $ \nu \le \tau $ , since every cover must contain at least one point from each edge in any matching. For $ r $ -uniform hypergraphs, $ \tau \le r \nu $ , since the union of the edges from any maximal matching is a set of at most $ r \nu $ vertices that which meets every edge. Ryser's conjecture is that this second bound can be improved if $ H $ is $ r $ -uniform and $ r $ -partite (the vertices may be partitioned into $ r $ sets $ V_1,V_2,\ldots,V_r $ so that every edge contains exactly one element of each $ V_i $ ). In the special case when $ r=2 $ our trivial inequality yields $ \nu \le \tau $ and the conjecture implies $ \tau \le \nu $ , so we should have $ \nu = \tau $ . In fact this is true, it is König's theorem on bipartite graphs [K]. Indeed, Ryser's conjecture is probably easiest to view as a high dimensional generalization of this early result of König. Recently, Aharoni [A] has applied the "Hall's theorem for hypergraphs" result of Aharoni and Haxell [AH] to prove this conjecture for $ r=3 $ . However the case $ r=4 $ is still wide open. Some other interesting work on this problem concerns fractional covers and fractional matchings. A fractional cover of $ H = (V,E) $ is a weighting $ a : V \rightarrow {\mathbb R}^+ $ so that $ \sum_{x \in S} a(x) \ge 1 $ for every $ S \in E $ , and the weight of this cover is $ \sum_{x \in V} a(x) $ . The fractional cover number , denoted $ \tau^* $ is the infimum of the set of weights of covers. Similarly, a fractional matching is an edge-weighting $ b : E \rightarrow {\mathbb R}^+ $ so that $ \sum_{S \ni x} b(S) \le 1 $ for every $ x \in V $ , and the weight of this matching is $ \sum_{S \in E} b(S) $ . The fractional matching number , denoted $ \nu^* $ is the supremum of the set of weights of fractional matchings. Fractional covers and matchings are the usual fractional relaxations, and by LP-duality, they satisfy $ \nu^* = \tau^* $ for every hypergraph. For $ r $ -regular $ r $ -partite hypergraphs, Füredi [F] has proved that $ \tau^* \le (r-1)\nu $ and Lovasz [L] has shown $ \tau \le \frac{1}{2} r \nu^* $ .

Bibliography

 [A]
 R. Aharoni, Ryser's conjecture for tripartite 3-graphs. Combinatorica 21 (2001), no. 1, 1--4. MathSciNet
 MathSciNet

 [AH]
 R. Aharoni and P. Haxell, Hall's theorem for hypergraphs. J. Graph Theory 35 (2000), no. 2, 83--88. MathSciNet
 MathSciNet

 [F]
 Z. Füredi, Maximum degree and fractional matchings in uniform hypergraphs, Combinatorica 1 (1981), 155--162. MathSciNet
 MathSciNet

 [K]
 D. König, Theorie der endlichen und unendlichen Graphen, Leipzig, 1936.

 [L]
 L. Lovász, On minimax theorems of combinatorics, Ph.D thesis, Matemathikai Lapok 26 (1975), 209--264 (in Hungarian). MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 Matching number drop by k(r−1) deletions
 open
 Rigorous by induction on nu. Base: nu=0 means no edges, tau=0. Step: the source conjecture gives k in [1,r-1] and a set S of k(r-1) vertices with nu(H-S) <= nu-k (necessarily k <= nu, since nu cannot drop by more than nu). H-S is still r-partite r-uniform, so by induction tau(H-S) <= (r-1)(nu-k); the cover of H-S together with S covers H, of size <= (r-1)(nu-k)+k(r-1) = (r-1)nu, i.e. tau <= (r-1)nu, which is Ryser's conjecture. Direction correct: the deletion conjecture is the stronger statement. The source's own context also states it is 'a weakening of Lovász's conjecture that still implies Ryser's conjecture'.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
