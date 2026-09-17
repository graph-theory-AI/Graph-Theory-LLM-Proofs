Attack the following open graph-theory problem.

Catalog id: partitioning_edge_connectivity
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Connectivity
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/partitioning_edge_connectivity/
Original entry: http://www.openproblemgarden.org/op/partitioning_edge_connectivity
Problem attributed to: DeVos, Matt (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Partitioning edge-connectivity
Question Let $ G $ be an $ (a+b+2) $ - edge-connected graph. Does there exist a partition $ \{A,B\} $ of $ E(G) $ so that $ (V,A) $ is $ a $ -edge-connected and $ (V,B) $ is $ b $ -edge-connected?

=== Discussion / context (OpenProblemGarden) ===
By the Nash-Williams/Tutte theorem ([NW] or [T]) on disjoint spanning trees, the above conjecture is true if $ G $ is $ 2(a+b) $ -edge-connected. This is the only partial result I know of. Here is a related conjecture. Conjecture There exists a fixed integer $ k $ so that every $ k $ -edge-connected graph $ G=(V,E) $ has a subset of edges $ S $ with the property that every edge-cut of $ G $ has between $ \frac{1}{3} $ and $ \frac{2}{3} $ of its edges in $ S $ . The values $ \frac{1}{3} $ and $ \frac{2}{3} $ are of no special importance in the above conjecture. Indeed, an affirmative answer to the above problem with $ \frac{1}{3} $ and $ \frac{2}{3} $ replaced by $ \frac{1}{t} $ and $ 1 - \frac{1}{t} $ for any $ t > 0 $ would still be valuable - and in particular, would imply the 2+epsilon flow conjecture . Definition: Let $ G=(V,E) $ be a graph and let $ P=\{E_1,E_2,...,E_t\} $ be a partition of $ E $ . We say that $ P $ is $ k $ -courteous if $ G \setminus E_i $ is $ k $ -edge-connected for every $ 1 \le i \le t $ . Problem What is the smallest integer $ t $ so that every 3-edge-connected graph has a 2-courteous coloring of size $ t $ ? It is known (see [DJS]) that $ 4 \le t \le 10 $ . It would be quite interesting if the truth were in fact $ t=4 $ . An improvement on the current upper bound would have some consequences for certain flow problems and cycle-cover problems. In general, one may define a function $ H : {\mathbb Z}^2 \rightarrow {\mathbb Z} \cup \{\infty\} $ so that $ H(a,b) $ is the smallest integer $ t $ (or $ \infty $ if none exists) so that every $ a $ -edge-connected graph has a $ b $ -courteous coloring of size $ t $ . It is known (see [DJS]) that $ H(2k+2,2k+1) = \infty $ , and that $ 2k+1 < H(2k+1,2k) < C 100^k $ . Two special cases when better values are known are $ 2 < H(4,2) < 5 $ and $ 5 < H(5,4) < 31 $ .

=== References listed by OpenProblemGarden ===
- [DJS] M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
- [Ed] J. Edmonds, Minimum Partition of a Matriod into Independent Subsets, J. Res. Nat. Bur. Standards 69B (1965) 67-72. MathSciNet
- [NW] C.S.J.A. Nash-Williams, Edge Disjoint Spanning Trees of Finite Graphs, J. London Math. Soc. 36 (1961) 445-450. MathSciNet
- [T] W.T. Tutte, On the problem of decomposing a graph into n connected factors, J. London Math. Soc. 36 (1961), 221-230. MathSciNet

=== Catalog page (statement + literature review) ===
Partitioning edge-connectivity — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The question of whether every $(a+b+2)$-edge-connected graph can have its edges partitioned into an $a$-edge-connected and a $b$-edge-connected spanning subgraph remains open. The only known partial result is via the Nash-Williams/Tutte theorem: if $G$ is $2(a+b)$-edge-connected, one can pack $a+b$ edge-disjoint spanning trees and assign $a$ to one part and $b$ to the other. No published paper appears to have closed the gap between $a+b+2$ and $2(a+b)$.

 Reviewer notes. The DJS paper (DeVos-Johnson-Seymour 'Cut-coloring and circuit covering') predates the 2007 posting date and is background, not new progress. The Princeton PDF (DJS) could not be parsed as text. The OPG page itself was unreachable (ECONNREFUSED). No arXiv or journal paper post-2007 specifically advancing the (a+b+2) partition conjecture was found across four search queries; the problem is likely still open but a definitive survey or MathSciNet search could confirm.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Question. Let $ G $ be an $ (a+b+2) $ - edge-connected graph. Does there exist a partition $ \{A,B\} $ of $ E(G) $ so that $ (V,A) $ is $ a $ -edge-connected and $ (V,B) $ is $ b $ -edge-connected?

Keywords:
edge-coloring · edge-connectivity

Discussion

By the Nash-Williams/Tutte theorem ([NW] or [T]) on disjoint spanning trees, the above conjecture is true if $ G $ is $ 2(a+b) $ -edge-connected. This is the only partial result I know of. Here is a related conjecture. Conjecture There exists a fixed integer $ k $ so that every $ k $ -edge-connected graph $ G=(V,E) $ has a subset of edges $ S $ with the property that every edge-cut of $ G $ has between $ \frac{1}{3} $ and $ \frac{2}{3} $ of its edges in $ S $ . The values $ \frac{1}{3} $ and $ \frac{2}{3} $ are of no special importance in the above conjecture. Indeed, an affirmative answer to the above problem with $ \frac{1}{3} $ and $ \frac{2}{3} $ replaced by $ \frac{1}{t} $ and $ 1 - \frac{1}{t} $ for any $ t > 0 $ would still be valuable - and in particular, would imply the 2+epsilon flow conjecture . Definition: Let $ G=(V,E) $ be a graph and let $ P=\{E_1,E_2,...,E_t\} $ be a partition of $ E $ . We say that $ P $ is $ k $ -courteous if $ G \setminus E_i $ is $ k $ -edge-connected for every $ 1 \le i \le t $ . Problem What is the smallest integer $ t $ so that every 3-edge-connected graph has a 2-courteous coloring of size $ t $ ? It is known (see [DJS]) that $ 4 \le t \le 10 $ . It would be quite interesting if the truth were in fact $ t=4 $ . An improvement on the current upper bound would have some consequences for certain flow problems and cycle-cover problems. In general, one may define a function $ H : {\mathbb Z}^2 \rightarrow {\mathbb Z} \cup \{\infty\} $ so that $ H(a,b) $ is the smallest integer $ t $ (or $ \infty $ if none exists) so that every $ a $ -edge-connected graph has a $ b $ -courteous coloring of size $ t $ . It is known (see [DJS]) that $ H(2k+2,2k+1) = \infty $ , and that $ 2k+1 < H(2k+1,2k) < C 100^k $ . Two special cases when better values are known are $ 2 < H(4,2) < 5 $ and $ 5 < H(5,4) < 31 $ .

Bibliography

 [DJS]
 M. DeVos, T. Johnson, P.D. Seymour, Cut-coloring and circuit covering
 Cut-coloring and circuit covering

 [Ed]
 J. Edmonds, Minimum Partition of a Matriod into Independent Subsets, J. Res. Nat. Bur. Standards 69B (1965) 67-72. MathSciNet
 MathSciNet

 [NW]
 C.S.J.A. Nash-Williams, Edge Disjoint Spanning Trees of Finite Graphs, J. London Math. Soc. 36 (1961) 445-450. MathSciNet
 MathSciNet

 [T]
 W.T. Tutte, On the problem of decomposing a graph into n connected factors, J. London Math. Soc. 36 (1961), 221-230. MathSciNet
 MathSciNet
