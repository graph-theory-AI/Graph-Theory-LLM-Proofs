Attack the following open graph-theory problem.

Catalog id: pentagon_problem
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Homomorphisms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/pentagon_problem/
Original entry: http://www.openproblemgarden.org/op/pentagon_problem
Problem attributed to: Nesetril, Jaroslav (posted 2007-03-24)

=== Problem statement (OpenProblemGarden) ===
Title: Pentagon problem
Question Let $ G $ be a 3-regular graph that contains no cycle of length shorter than $ g $ . Is it true that for large enough~ $ g $ there is a homomorphism $ G \to C_5 $ ?

=== Discussion / context (OpenProblemGarden) ===
This question was asked by Nesetril at numerous problem sessions (and also appears as [N]). By Brook's theorem any triangle-free cubic graph is 3-colorable. Does a stronger assumption on girth of the graph imply stronger coloring properties? This problem is motivated by complexity considerations [GHN] and also by exploration of density of the homomorphism order: We write $ G \prec H $ if there is a homomorphism $ G \to H $ but there is no homomorphism $ H \to G $ . It is known that whenever $ G \prec H $ holds and $ H $ ~is not bipartite, there is a graph~ $ K $ satisfying $ G \prec K \prec H $ . A negative solution to the Pentagon problem would have the following density consequence: for each cubic graph~ $ H $ for which~ $ C_5 \prec H $ holds, there exists a cubic graph~ $ K $ satisfying $ C_5 \prec K \prec H $ (see [N]). If we replaced $ C_5 $ in the statement of the problem by a longer odd cycle, we would get a stronger statement. It is known that no such strenghthening is true. This was proved by Kostochka, Nesetril, and Smolikova [KNS] for $ C_{11} $ (hence for all $ C_l $ with $ l \ge 11 $ ), by Wanless and Wormald [WW] for $ C_9 $ , and recently by Hatami [H] for $ C_7 $ . Each of these results uses probabilistic arguments (random regular graphs), no constructive proof is known. Haggkvist and Hell [HH] proved that for every integer~ $ g $ there is a graph~ $ U_g $ with odd girth at least~ $ g $ (that is, $ U_g $ does not contain odd cycle of length less than~ $ g $ ) such that every cubic graph of odd girth at least~ $ g $ maps homomorphically to~ $ U_g $ . Here, the graph~ $ U_g $ may have large degrees. This leads to a weaker version of the Pentagon problem: Question Is it true that for every $ k $ there exists a cubic graph $ H_k $ of girth~ $ k $ and an integer~ $ g $ such that every cubic graph of girth at least~ $ g $ maps homomorphically to~ $ H_k $ ? A particular question in this direction: does a high-girth cubic graph map to the Petersen graph? As an approach to this, we mention a result of DeVos and Samal [DS]: a cubic graph of girth at least~ $ 17 $ admits a homomorphism to the Clebsch graph. In context of the Pentagon problem, the following reformulation is particularly appealing: If $ G $ ~is a cubic graph of girth at least~ $ 17 $ , then there is a cut-continuous mapping from~ $ G $ to~ $ C_5 $ ; that is, there is a mapping $ f: E(G) \to E(C_5) $ such that for any cut $ X \subseteq E(C_5) $ the preimage $ f^{-1}(X) $ is a cut. (Here by cut we mean the edge-set of a spanning bipartite subgraph. A more thorough exposition of cut-continuous mappings can be found in~[DNR].)

=== References listed by OpenProblemGarden ===
- [DNR] Matt DeVos, Jaroslav Nesetril, and Andre Raspaud, On edge-maps whose inverse preverses flows and tensions, Graph Theory in Paris: Proceedings of a Conference in Memory of Claude Berge, Birkhäuser 2006.
- [DS] Matt DeVos and Robert Samal, High girth cubic graphs map to the Clebsch graph
- [GHN] Anna Galluccio, Pavol Hell, and Jaroslav Nesetril, The complexity of -colouring of bounded degree graphs, Discrete Math. 222 (2000), no.~1-3, 101--109, MathSciNet
- [HH] Roland Haggkvist and Pavol Hell, Universality of -mote graphs, European J. Combin. 14 (1993), no.~1, 23--27.
- [H] Hamed Hatami, Random cubic graphs are not homomorphic to the cycle of size~7, J. Combin. Theory Ser. B 93 (2005), no.~2, 319--325, MathSciNet
- [KNS] Alexandr~V. Kostochka, Jaroslav Nesetril, and Petra Smolikova, Colorings and homomorphisms of degenerate and bounded degree graphs, Discrete Math. 233 (2001), no.~1-3, 257--276, Fifth Czech-Slovak International Symposium on Combinatorics, Graph Theory, Algorithms and Applications, (Prague, 1998), MathSciNet
- *[N] Jaroslav Nesetril, Aspects of structural combinatorics (graph homomorphisms and their use), Taiwanese J. Math. 3 (1999), no.~4, 381--423, MathSciNet
- [WW] I.M. Wanless and N.C. Wormald, Regular graphs with no homomorphisms onto cycles, J. Combin. Theory Ser. B 82 (2001), no.~1, 155--160, MathSciNet

=== Catalog page (statement + literature review) ===
Pentagon problem — Graph-theory open problems

 
 Status
 open
 high confidence
 

 Nešetřil's Pentagon Problem — whether every 3-regular graph of sufficiently high girth admits a homomorphism to $C_5$ — remains open. The strongest known partial result, that cubic graphs of girth at least 17 admit a homomorphism to the Clebsch graph (DeVos–Šámal), was already recorded in the OPG problem statement. The analogous question for longer odd cycles $C_\ell$ with $\ell \geq 7$ has been answered negatively, but the $C_5$ case has not been resolved.

 Cited literature (1)

 
 
 
partial On Colorings of Graph Powers
 (2007)
 

 
 Hossein Hajiabolhassan · arXiv preprint · arXiv:0708.0704 · doi:10.48550/arXiv.0708.0704

Considers Nešetřil's Pentagon problem and introduces several closely related problems with an analysis of their inter-relations, without resolving the original conjecture.
 

 

 Reviewer notes. The DeVos–Šámal result (cubic graphs of girth ≥ 17 map to the Clebsch graph, arXiv:math/0602580, submitted Feb 2006) was already known before the OPG posting date and is cited in the problem statement; its journal publication in J. Graph Theory (2011) was found in search results but could not be verified (HTTP 403). The OPG page itself was unreachable (ECONNREFUSED). No post-2007 breakthrough or resolution of the Pentagon problem was found across four targeted searches.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Question. Let $ G $ be a 3-regular graph that contains no cycle of length shorter than $ g $ . Is it true that for large enough~ $ g $ there is a homomorphism $ G \to C_5 $ ?

Keywords:
cubic · homomorphism

Discussion

This question was asked by Nesetril at numerous problem sessions (and also appears as [N]). By Brook's theorem any triangle-free cubic graph is 3-colorable. Does a stronger assumption on girth of the graph imply stronger coloring properties? This problem is motivated by complexity considerations [GHN] and also by exploration of density of the homomorphism order: We write $ G \prec H $ if there is a homomorphism $ G \to H $ but there is no homomorphism $ H \to G $ . It is known that whenever $ G \prec H $ holds and $ H $ ~is not bipartite, there is a graph~ $ K $ satisfying $ G \prec K \prec H $ . A negative solution to the Pentagon problem would have the following density consequence: for each cubic graph~ $ H $ for which~ $ C_5 \prec H $ holds, there exists a cubic graph~ $ K $ satisfying $ C_5 \prec K \prec H $ (see [N]). If we replaced $ C_5 $ in the statement of the problem by a longer odd cycle, we would get a stronger statement. It is known that no such strenghthening is true. This was proved by Kostochka, Nesetril, and Smolikova [KNS] for $ C_{11} $ (hence for all $ C_l $ with $ l \ge 11 $ ), by Wanless and Wormald [WW] for $ C_9 $ , and recently by Hatami [H] for $ C_7 $ . Each of these results uses probabilistic arguments (random regular graphs), no constructive proof is known. Haggkvist and Hell [HH] proved that for every integer~ $ g $ there is a graph~ $ U_g $ with odd girth at least~ $ g $ (that is, $ U_g $ does not contain odd cycle of length less than~ $ g $ ) such that every cubic graph of odd girth at least~ $ g $ maps homomorphically to~ $ U_g $ . Here, the graph~ $ U_g $ may have large degrees. This leads to a weaker version of the Pentagon problem: Question Is it true that for every $ k $ there exists a cubic graph $ H_k $ of girth~ $ k $ and an integer~ $ g $ such that every cubic graph of girth at least~ $ g $ maps homomorphically to~ $ H_k $ ? A particular question in this direction: does a high-girth cubic graph map to the Petersen graph? As an approach to this, we mention a result of DeVos and Samal [DS]: a cubic graph of girth at least~ $ 17 $ admits a homomorphism to the Clebsch graph. In context of the Pentagon problem, the following reformulation is particularly appealing: If $ G $ ~is a cubic graph of girth at least~ $ 17 $ , then there is a cut-continuous mapping from~ $ G $ to~ $ C_5 $ ; that is, there is a mapping $ f: E(G) \to E(C_5) $ such that for any cut $ X \subseteq E(C_5) $ the preimage $ f^{-1}(X) $ is a cut. (Here by cut we mean the edge-set of a spanning bipartite subgraph. A more thorough exposition of cut-continuous mappings can be found in~[DNR].)

Bibliography

 [DNR]
 Matt DeVos, Jaroslav Nesetril, and Andre Raspaud, On edge-maps whose inverse preverses flows and tensions, Graph Theory in Paris: Proceedings of a Conference in Memory of Claude Berge, Birkhäuser 2006.

 [DS]
 Matt DeVos and Robert Samal, High girth cubic graphs map to the Clebsch graph
 High girth cubic graphs map to the Clebsch graph

 [GHN]
 Anna Galluccio, Pavol Hell, and Jaroslav Nesetril, The complexity of $ H $ -colouring of bounded degree graphs, Discrete Math. 222 (2000), no.~1-3, 101--109, MathSciNet
 MathSciNet

 [HH]
 Roland Haggkvist and Pavol Hell, Universality of $ A $ -mote graphs, European J. Combin. 14 (1993), no.~1, 23--27.

 [H]
 Hamed Hatami, Random cubic graphs are not homomorphic to the cycle of size~7, J. Combin. Theory Ser. B 93 (2005), no.~2, 319--325, MathSciNet
 MathSciNet

 [KNS]
 Alexandr~V. Kostochka, Jaroslav Nesetril, and Petra Smolikova, Colorings and homomorphisms of degenerate and bounded degree graphs, Discrete Math. 233 (2001), no.~1-3, 257--276, Fifth Czech-Slovak International Symposium on Combinatorics, Graph Theory, Algorithms and Applications, (Prague, 1998), MathSciNet
 MathSciNet

★ [N]
 Jaroslav Nesetril, Aspects of structural combinatorics (graph homomorphisms and their use), Taiwanese J. Math. 3 (1999), no.~4, 381--423, MathSciNet
 MathSciNet

 [WW]
 I.M. Wanless and N.C. Wormald, Regular graphs with no homomorphisms onto cycles, J. Combin. Theory Ser. B 82 (2001), no.~1, 155--160, MathSciNet
 MathSciNet

Related conjectures

 
 related to
 Weak pentagon problem
 partial
 Conclusion-wise the Pentagon problem is stronger: a homomorphism G -> C5 induces a cut-continuous mapping G -> C5, which is exactly the Weak pentagon conclusion (equivalently, edge 5-coloring with bipartite color-class complements / homomorphism to the Clebsch graph); the OPG text calls the weak conjecture 'a weaker version' for this reason. But the hypothesis classes are not nested in the required direction: Pentagon assumes girth at least g for sufficiently large g, while Weak pentagon covers ALL triangle-free (girth >= 4) cubic graphs. A positive Pentagon answer would establish the weak conclusion only for high-girth graphs, leaving girths 4..g-1 unsettled, so the full statements do not stand in an implication; the connection is instance-wise on a subfamily. Hence related_only (Pentagon truth would settle the high-girth part and be strong evidence).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
