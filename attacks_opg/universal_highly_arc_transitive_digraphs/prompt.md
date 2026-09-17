Attack the following open graph-theory problem.

Catalog id: universal_highly_arc_transitive_digraphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/universal_highly_arc_transitive_digraphs/
Original entry: http://www.openproblemgarden.org/op/universal_highly_arc_transitive_digraphs
Problem attributed to: Cameron, Peter J., Praeger, Cheryl E., Wormald, Nicholas C. (posted 2007-10-21)

=== Problem statement (OpenProblemGarden) ===
Title: Universal highly arc transitive digraphs
An alternating walk in a digraph is a walk $ v_0,e_1,v_1,\ldots,v_m $ so that the vertex $ v_i $ is either the head of both $ e_i $ and $ e_{i+1} $ or the tail of both $ e_i $ and $ e_{i+1} $ for every $ 1 \le i \le m-1 $ . A digraph is universal if for every pair of edges $ e,f $ , there is an alternating walk containing both $ e $ and $ f $ Question Does there exist a locally finite highly arc transitive digraph which is universal?

=== Discussion / context (OpenProblemGarden) ===
Let $ D $ be a digraph. For a nonnegative integer $ s $ , a $ s $ - arc in $ D $ is a sequence $ (x_0,x_1,\ldots,x_s) $ of vertices so that $ (x_i,x_{i+1}) $ is an edge for every $ 0 \le i \le s-1 $ and $ x_{i-1} \neq x_{i+1} $ for every $ 1 \le i \le s-1 $ . We say that $ D $ is $ s $ - arc transitive if its automorphism group acts transitively on the set of $ s $ arcs, and we say that $ D $ is highly arc transitive if it is $ s $ -arc transitive for every $ s $ . Note that the condition $ 0 $ -arc transitive is precisely equivalent to vertex transitive. It is an easy exercise to show that the only finite digraphs which are highly arc transitive are directed cycles. Since such graphs have only trivial alternating walks (only one edge can be used), they are not universal. Thus, any graph satisfying the criteria of the conjecture must be infinite. Let $ P $ be a two way infinite directed path (i.e. the Cayley graph on $ {\mathbb Z} $ with generating set $ \{1\} $ ). The digraph $ P $ is not universal, but moreover, any digraph with a homomorphism onto $ P $ cannot be universal. In the same article where the above question was posed, the authors asked wether there exist infinite highly transitive digraphs with no homomorphism onto $ P $ . This question has since been resolved in the affirmative: Evans [E] constructed such a digraph with infinite indegree, and Malnic et. al. [MMSZ] have constructed a locally finite one. In a vertex transitive digraph, every vertex must have the same indegree and the same outdegree, and we shall denote these by $ d^- $ and $ d^+ $ respectively. A theorem of Praeger [P] shows that every locally finite highly transitive digraph for which $ d^- \neq d^+ $ has a homomorphism onto $ P $ and thus is not universal. More recently, Malnic et. al. [MMMSTZ] have established a condition on edge stabilizers in arc transitive digraphs which implies that any such digraph with $ d^- = d^+ $ a prime is not universal. It follows that any digraph satisfying the conditions of the highlighted question must have $ d^+ = d^- $ a composite number.

=== References listed by OpenProblemGarden ===
- *[CPW] P. J. Cameron, C. E. Praeger, and N. C. Wormald, Infinite highly arc transitive digraphs and universal covering digraphs. Combinatorica 13 (1993), no. 4, 377--396. MathSciNet.
- [E] D. M. Evans, An infinite highly arc-transitive digraph, European J. Combin., 18 (1997) 281--286. MathSciNet.
- [MMMSTZ] A. Malnic, D. Marusic, R. G. Moller, N. Seifter, V. Trofimov, and B. Zgrablic, Highly arc transitive digraphs: reachability, topological groups. European J. Combin. 26 (2005), no. 1, 19--28. MathSciNet.
- [MMSZ] A. Malnic, D. Marusic, N. Seifter, and B. Zgrablic, Highly arc-transitive digraphs with no homomorphism onto Z. Combinatorica 22 (2002), no. 3, 435--443. MathSciNet
- [P] C. E. Praeger, On homomorphic images of edge transitive directed graphs, Australas. J. Combin., 3 (1991), 207--210. MathSciNet.

=== Catalog page (statement + literature review) ===
Universal highly arc transitive digraphs — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 The question was answered affirmatively by DeVos, Mohar, and Šámal (arXiv 2011, Combinatorica 2014), who explicitly constructed a locally finite highly arc-transitive digraph with universal reachability relation (a single equivalence class), thereby resolving the open problem of Cameron, Praeger, and Wormald. Their paper also disproves a second conjecture from the same 1993 article by producing 2-ended highly arc-transitive digraphs whose 'building blocks' are finite bipartite graphs that are not disjoint unions of complete bipartite graphs. Earlier work (Malnic et al., 2005) had established that any such universal locally finite example must have $d^+ = d^-$ equal to a composite number, consistent with the construction.

 Cited literature (1)

 
 
 
proof Highly arc-transitive digraphs -- counterexamples and structure
 (2014)
 

 
 Matt DeVos, Bojan Mohar, Robert Šámal · Combinatorica · arXiv:1110.2945 · doi:10.1007/s00493-014-3040-4

Constructs a locally finite highly arc-transitive digraph with universal reachability relation, resolving the Cameron-Praeger-Wormald open problem; also disproves a second conjecture from the same 1993 paper on the structure of 2-ended highly arc-transitive digraphs.
 

 

 Reviewer notes. The Springer journal page for the Combinatorica article (10.1007/s00493-014-3040-4) returned an authentication redirect and could not be fetched directly; the arXiv abstract page was successfully verified and confirms all key claims. The year 2014 for Combinatorica is inferred from the DOI path segment 's00493-014'. A second paper (Möller, Potočnik, Seifter, arXiv:1811.02995, 2018) on two-ended highly arc-transitive digraphs with prime valency is relevant background but does not change the solved status.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Question. Does there exist a locally finite highly arc transitive digraph which is universal?

Keywords:
arc transitive · digraph

Discussion

Let $ D $ be a digraph. For a nonnegative integer $ s $ , a $ s $ - arc in $ D $ is a sequence $ (x_0,x_1,\ldots,x_s) $ of vertices so that $ (x_i,x_{i+1}) $ is an edge for every $ 0 \le i \le s-1 $ and $ x_{i-1} \neq x_{i+1} $ for every $ 1 \le i \le s-1 $ . We say that $ D $ is $ s $ - arc transitive if its automorphism group acts transitively on the set of $ s $ arcs, and we say that $ D $ is highly arc transitive if it is $ s $ -arc transitive for every $ s $ . Note that the condition $ 0 $ -arc transitive is precisely equivalent to vertex transitive. It is an easy exercise to show that the only finite digraphs which are highly arc transitive are directed cycles. Since such graphs have only trivial alternating walks (only one edge can be used), they are not universal. Thus, any graph satisfying the criteria of the conjecture must be infinite. Let $ P $ be a two way infinite directed path (i.e. the Cayley graph on $ {\mathbb Z} $ with generating set $ \{1\} $ ). The digraph $ P $ is not universal, but moreover, any digraph with a homomorphism onto $ P $ cannot be universal. In the same article where the above question was posed, the authors asked wether there exist infinite highly transitive digraphs with no homomorphism onto $ P $ . This question has since been resolved in the affirmative: Evans [E] constructed such a digraph with infinite indegree, and Malnic et. al. [MMSZ] have constructed a locally finite one. In a vertex transitive digraph, every vertex must have the same indegree and the same outdegree, and we shall denote these by $ d^- $ and $ d^+ $ respectively. A theorem of Praeger [P] shows that every locally finite highly transitive digraph for which $ d^- \neq d^+ $ has a homomorphism onto $ P $ and thus is not universal. More recently, Malnic et. al. [MMMSTZ] have established a condition on edge stabilizers in arc transitive digraphs which implies that any such digraph with $ d^- = d^+ $ a prime is not universal. It follows that any digraph satisfying the conditions of the highlighted question must have $ d^+ = d^- $ a composite number.

Bibliography

★ [CPW]
 P. J. Cameron, C. E. Praeger, and N. C. Wormald, Infinite highly arc transitive digraphs and universal covering digraphs. Combinatorica 13 (1993), no. 4, 377--396. MathSciNet .
 MathSciNet

 [E]
 D. M. Evans, An infinite highly arc-transitive digraph, European J. Combin., 18 (1997) 281--286. MathSciNet .
 MathSciNet

 [MMMSTZ]
 A. Malnic, D. Marusic, R. G. Moller, N. Seifter, V. Trofimov, and B. Zgrablic, Highly arc transitive digraphs: reachability, topological groups. European J. Combin. 26 (2005), no. 1, 19--28. MathSciNet .
 MathSciNet

 [MMSZ]
 A. Malnic, D. Marusic, N. Seifter, and B. Zgrablic, Highly arc-transitive digraphs with no homomorphism onto Z . Combinatorica 22 (2002), no. 3, 435--443. MathSciNet
 Highly arc-transitive digraphs with no homomorphism onto Z · MathSciNet

 [P]
 C. E. Praeger, On homomorphic images of edge transitive directed graphs, Australas. J. Combin., 3 (1991), 207--210. MathSciNet .
 MathSciNet
