Attack the following open graph-theory problem.

Catalog id: woodalls_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/woodalls_conjecture/
Original entry: http://www.openproblemgarden.org/op/woodalls_conjecture
Problem attributed to: Woodall, Douglas R. (posted 2007-04-05)

=== Problem statement (OpenProblemGarden) ===
Title: Woodall's Conjecture
Conjecture If $ G $ is a directed graph with smallest directed cut of size $ k $ , then $ G $ has $ k $ disjoint dijoins.

=== Discussion / context (OpenProblemGarden) ===
Definitions: Let $ G $ be a directed graph. A directed cut of $ G $ is an edge-cut in which all edges are directed the same way. A dijoin is a set of edges which intersect every directed cut. There is an important theorem of Lucchesi and Younger [LY] which asserts that the dual problem has an optimum integer packing. That is, for every digraph $ G $ in which the smallest dijoin has size $ k $ , there exist $ k $ pairwise disjoint directed cuts. This result implies more generally (in the terminology of Corneujols [C]) that the clutter of (minimal) directed cuts has the max-flow min-cut property (MFMC). It follows from this and Lehman's theorem [L] that the clutter of (minimal) dijoins is ideal. Therefore, if the smallest directed cut of $ G $ has size $ k $ , then there exist nonnegative rational numbers $ x_1,x_2,\ldots,x_m $ summing to $ k $ and dijoins $ J_1,J_2,\ldots,J_m $ so that if each dijoin $ J_i $ is taken with weight $ x_i $ , the total weight of the dijoins containing any edge is at most 1. The above conjecture asserts that such a combination exists with $ x_1,x_2,\ldots,x_m $ integral. Schrijver [Sc80] has found a digraph in which the clutter of (minimal) dijoins does not have the MFMC property. Thus, the weighted version of Woodall's conjecture is not true in general. However, this clutter does have the MFMC property in a number of interesting special cases. One such example (due to Schrijver [Sc82] and Feofiloff, Younger [FY]) is when the digraph is acyclic and every source is joined to every sink by a directed path. Since every such digraph has the MFMC property, every such digraph must satisfy Woodall's conjecture. There seem to be few positive results towards Woodall's conjecture for general digraphs. Although this was probably already known, Seymour and I (M. DeVos) observed that the conjecture is true for $ k=2 $ . To see this, note that the underlying graph is 2-edge-connected, so it may be oriented to give a strongly connected digraph, call it $ H $ . Now partition the edges into two sets $ \{X,Y\} $ where $ X $ consists of those edges which have the same orientation in both $ H $ and $ G $ , and $ Y $ consists of those edges with different orientations in the two graphs. It is immediate that both $ X $ and $ Y $ meet every directed cut, so each is a dijoin. Extending this to $ k=3 $ appears difficult. Indeed, I believe the following weak version of this is still open. Conjecture Prove that there exists a fixed integer $ k $ so that every digraph with all directed cuts of size $ \ge k $ contains three pairwise disjoint dijoins. The restriction of this conjecture to the special case of planar graphs is also open. Here we can use duality to restate the conjecture. Call a set of edges $ A $ a feedback arc-set if $ A $ intersects every directed cycle (or equivalently, $ G-A $ is acyclic). Conjecture If $ G $ is a planar digraph with all directed cycles of length $ \ge k $ , then $ G $ contains $ k $ pairwise disjoint feedback arc-sets. The above conjecture is known to fail when the assumption of planarity is removed. On the other hand, it does hold for digraphs which are orientations of series-parallel graphs [LW]. It is also still open for $ k=3 $ .

=== References listed by OpenProblemGarden ===
- [C] G. Cornuejols, Combinatorial Optimization, Packing and Covering SIAM, Philadelphia (2001). MathSciNet
- [FY] P. Feofiloff and D. H. Younger, Directed cut transversal packing for source-sink connected graphs. Combinatorica 7 (1987), no. 3, 255--263. MathSciNet
- [LW] O. Lee, Y. Wakabayashi, Note on a min-max conjecture of Woodall. J. Graph Theory 38 (2001), no. 1, 36--41. MathSciNet
- [LY] C.L. Lucchesi and D. H. Younger A minimax theorem for directed graphs, Journal of the London Math. Soc. (2) 17 (1978) 369-374. MathSciNet
- [Sc80] A. Schrijver, A counterexample to a conjecture of Edmonds and Giles, Discrete Math. 32 (1980) 213-214. MathSciNet
- [Sc82] A. Schrijver, Min-max relations for directed graphs, Annals of Discrete Math. 16 (1982) 261-280. MathSciNet
- [W] D. R. Woodall, Menger and König systems. Theory and applications of graphs (Proc. Internat. Conf., Western Mich. Univ., Kalamazoo, Mich., 1976), pp. 620--635, Lecture Notes in Math., 642, Springer, Berlin, 1978. MathSciNet

=== Catalog page (statement + literature review) ===
Woodall's Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Woodall's conjecture remains open for general digraphs. The most significant recent advance (Cornuéjols–Liu–Ravi, 2023/2025) proves that every digraph with minimum dicut size $\tau$ contains at least $\lfloor\tau/6\rfloor$ pairwise disjoint dijoins, via nowhere-zero flow theory; the full conjecture would require $\tau$ disjoint dijoins. Partial results for special graph classes (3-trees, chordal underlying graphs) and restricted families of dicuts have also been established.

 Cited literature (6)

 
 
 
partial Disjoint dijoins
 (2014)
 

 
 Maria Chudnovsky, Katherine Edwards, Ringi Kim, Alex Scott, Paul Seymour · Journal of Combinatorial Theory, Series B · arXiv:1412.1415

Proves a weakened form of Woodall's k=2 conjecture (with an extra connectivity constraint) for planar digraphs and for digraphs where the relevant subgraph is a subdivision of a caterpillar.
 

 
 
partial Disjoint dijoins for classes of dicuts in finite and infinite digraphs
 (2021)
 

 
 J. Pascal Gollin, Karl Heuer, Konstantinos Stavropoulos · arXiv preprint · arXiv:2109.03518

Verifies a generalised version of Woodall's conjecture for restricted classes of dicuts, including nested finite dicuts, minimum-size dicuts, and infinite dibonds.
 

 
 
partial Approximately Packing Dijoins via Nowhere-Zero Flows
 (2023)
 

 
 Gérard Cornuéjols, Siyue Liu, R. Ravi · Combinatorica · arXiv:2311.04337 · doi:10.1007/s00493-025-00159-x

Proves that every digraph with minimum dicut size $\tau$ contains at least $\lfloor\tau/6\rfloor$ pairwise disjoint dijoins by reducing the problem to nowhere-zero circular flows; as a corollary any digraph with $\tau\ge3$ contains three disjoint dijoins.
 

 
 
partial Towards a Dual Version of Woodall's Conjecture for Partial 3-Trees
 (2024)
 

 
 Juan Gutiérrez · arXiv preprint · arXiv:2408.05703

Proves the dual planar formulation of Woodall's conjecture (on feedback arc-set packing) for digraphs whose underlying graph is a 3-tree or a partial 3-tree with girth 3.
 

 
 
partial Packing Dijoins in Weighted Chordal Digraphs
 (2025)
 

 
 Gérard Cornuéjols, Siyue Liu, R. Ravi · arXiv preprint · arXiv:2501.10918

Proves the weighted Edmonds–Giles conjecture (the capacitated analogue of Woodall's conjecture) for digraphs whose underlying undirected graph is chordal, with a strongly polynomial algorithm.
 

 
 
partial Disproof of a Conjecture by Woodall
 (2022)
 

 
 Raphael Steiner · arXiv preprint · arXiv:2201.09115

Disproves the conjecture in a strong form: for every $\varepsilon > 0$ and $C \geq 1$ there exists $N = N(\varepsilon, C)$ such that for all integers $s, t$ with $N \leq s \leq t \leq Cs$, there exists a graph without a $K_{s,t}$-minor and list chromatic number greater than $(1-\varepsilon)(2s+t)$, substantially exceeding the conjectured bound of $s+t-1$.
 

 

 Reviewer notes. The SIAM paper 'On Packing Dijoins in Digraphs and Weighted Digraphs' (Abdi, Cornuéjols, Zlatin; DOI 10.1137/22M1506511) appeared in search results but returned HTTP 403 on fetch and could not be verified; it was therefore excluded from since_posted. The Chudnovsky et al. (2014) paper addresses a modified, weaker version of the k=2 case rather than Woodall's original conjecture, and the arXiv submission year 2014 is used (journal publication in JCTB appears to be 2016 based on the pii URL, but this could not be independently confirmed). The Cornuéjols–Liu–Ravi nowhere-zero flow result is the most impactful advance for the general conjecture, answering the long-open question of whether 3 disjoint dijoins always exist when $\tau\ge3$.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. If $ G $ is a directed graph with smallest directed cut of size $ k $ , then $ G $ has $ k $ disjoint dijoins.

Keywords:
digraph · packing

Discussion

Definitions: Let $ G $ be a directed graph. A directed cut of $ G $ is an edge-cut in which all edges are directed the same way. A dijoin is a set of edges which intersect every directed cut. There is an important theorem of Lucchesi and Younger [LY] which asserts that the dual problem has an optimum integer packing. That is, for every digraph $ G $ in which the smallest dijoin has size $ k $ , there exist $ k $ pairwise disjoint directed cuts. This result implies more generally (in the terminology of Corneujols [C]) that the clutter of (minimal) directed cuts has the max-flow min-cut property (MFMC). It follows from this and Lehman's theorem [L] that the clutter of (minimal) dijoins is ideal. Therefore, if the smallest directed cut of $ G $ has size $ k $ , then there exist nonnegative rational numbers $ x_1,x_2,\ldots,x_m $ summing to $ k $ and dijoins $ J_1,J_2,\ldots,J_m $ so that if each dijoin $ J_i $ is taken with weight $ x_i $ , the total weight of the dijoins containing any edge is at most 1. The above conjecture asserts that such a combination exists with $ x_1,x_2,\ldots,x_m $ integral. Schrijver [Sc80] has found a digraph in which the clutter of (minimal) dijoins does not have the MFMC property. Thus, the weighted version of Woodall's conjecture is not true in general. However, this clutter does have the MFMC property in a number of interesting special cases. One such example (due to Schrijver [Sc82] and Feofiloff, Younger [FY]) is when the digraph is acyclic and every source is joined to every sink by a directed path. Since every such digraph has the MFMC property, every such digraph must satisfy Woodall's conjecture. There seem to be few positive results towards Woodall's conjecture for general digraphs. Although this was probably already known, Seymour and I (M. DeVos) observed that the conjecture is true for $ k=2 $ . To see this, note that the underlying graph is 2-edge-connected, so it may be oriented to give a strongly connected digraph, call it $ H $ . Now partition the edges into two sets $ \{X,Y\} $ where $ X $ consists of those edges which have the same orientation in both $ H $ and $ G $ , and $ Y $ consists of those edges with different orientations in the two graphs. It is immediate that both $ X $ and $ Y $ meet every directed cut, so each is a dijoin. Extending this to $ k=3 $ appears difficult. Indeed, I believe the following weak version of this is still open. Conjecture Prove that there exists a fixed integer $ k $ so that every digraph with all directed cuts of size $ \ge k $ contains three pairwise disjoint dijoins. The restriction of this conjecture to the special case of planar graphs is also open. Here we can use duality to restate the conjecture. Call a set of edges $ A $ a feedback arc-set if $ A $ intersects every directed cycle (or equivalently, $ G-A $ is acyclic). Conjecture If $ G $ is a planar digraph with all directed cycles of length $ \ge k $ , then $ G $ contains $ k $ pairwise disjoint feedback arc-sets. The above conjecture is known to fail when the assumption of planarity is removed. On the other hand, it does hold for digraphs which are orientations of series-parallel graphs [LW]. It is also still open for $ k=3 $ .

Bibliography

 [C]
 G. Cornuejols, Combinatorial Optimization, Packing and Covering SIAM, Philadelphia (2001). MathSciNet
 MathSciNet

 [FY]
 P. Feofiloff and D. H. Younger, Directed cut transversal packing for source-sink connected graphs. Combinatorica 7 (1987), no. 3, 255--263. MathSciNet
 MathSciNet

 [LW]
 O. Lee, Y. Wakabayashi, Note on a min-max conjecture of Woodall. J. Graph Theory 38 (2001), no. 1, 36--41. MathSciNet
 MathSciNet

 [LY]
 C.L. Lucchesi and D. H. Younger A minimax theorem for directed graphs, Journal of the London Math. Soc. (2) 17 (1978) 369-374. MathSciNet
 MathSciNet

 [Sc80]
 A. Schrijver, A counterexample to a conjecture of Edmonds and Giles , Discrete Math. 32 (1980) 213-214. MathSciNet
 A counterexample to a conjecture of Edmonds and Giles · MathSciNet

 [Sc82]
 A. Schrijver, Min-max relations for directed graphs, Annals of Discrete Math. 16 (1982) 261-280. MathSciNet
 MathSciNet

 [W]
 D. R. Woodall, Menger and König systems. Theory and applications of graphs (Proc. Internat. Conf., Western Mich. Univ., Kalamazoo, Mich., 1976), pp. 620--635, Lecture Notes in Math., 642, Springer, Berlin, 1978. MathSciNet
 MathSciNet
