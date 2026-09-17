Attack the following open graph-theory problem.

Catalog id: minimum_number_of_transitive_subtournaments_of_order_3_in_a_tournament
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/minimum_number_of_transitive_subtournaments_of_order_3_in_a_tournament/
Original entry: http://www.openproblemgarden.org/op/minimum_number_of_transitive_subtournaments_of_order_3_in_a_tournament
Problem attributed to: Yuster, Raphael (posted 2013-05-21)

=== Problem statement (OpenProblemGarden) ===
Title: Minimum number of arc-disjoint transitive subtournaments of order 3 in a tournament
Conjecture If $ T $ is a tournament of order $ n $ , then it contains $ \left \lceil n(n-1)/6 - n/3\right\rceil $ arc-disjoint transitive subtournaments of order 3.

=== Discussion / context (OpenProblemGarden) ===
If true the conjecture would be tight as shown by any tournament whose vertex set can be decomposed into $ 3 $ sets $ V_1, V_2, V_3 $ of size $ \lceil n/3 \rceil $ or $ \lfloor n/3\rfloor $ and such that $ V_1\rightarrow V_2 $ , $ V_2\rightarrow V_3 $ and $ V_3\rightarrow V_1 $ . Let $ TT_3 $ denote the transitive tournament of order 3. A $ TT_3 $ -packing of a digraph $ D $ is a set of arc-disjoint copies of $ TT_3 $ subgraphs of $ D $ . Let $ f(n) $ be the minimum size of a $ TT_3 $ -packing over all tournaments of order $ n $ . The conjecture and its tightness say $ f(n)= \left \lceil n(n-1)/6 - n/3\right\rceil $ . The best lower bound for $ f(n) $ so far is due to Kabiya and Yuster [KY] proved that $ f(n) > \frac{41}{300} n^2(1+o(1)) $ .

=== References listed by OpenProblemGarden ===
- [KY] M. Kabiya and R. Yuster. Packing transitive triples in a tournament. Ann. Comb. 12 (2008), no. 3, 291–-306.
- *[Y] R. Yuster. The number of edge-disjoint transitive triples in a tournament. Discrete Math. 287 (2004). no. 1-3,187--191.

=== Catalog page (statement + literature review) ===
Minimum number of arc-disjoint transitive subtournaments of order 3 in a tournament — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The conjecture that every tournament of order $n$ contains at least $\lceil n(n-1)/6 - n/3 \rceil$ arc-disjoint transitive triples ($TT_3$) remains open. The best lower bound, $f(n) > \frac{41}{300}n^2(1+o(1))$, is due to Kabiya and Yuster (2008) and falls short of the conjectured value of $\approx n^2/6$. No post-2013 paper improving this bound or resolving the conjecture was found.

 Reviewer notes. arXiv:2306.02364 (tournament survey) and SIAM 10.1137/19M1269257 (transitive tournament tilings under degree conditions) address related but distinct problems. The SIAM paper concerns vertex-disjoint tilings with minimum degree conditions (Hajnal–Szemerédi type), not minimum arc-disjoint TT_3 packing. The NSF PDF and Kabiya–Yuster PDF were binary and unreadable by WebFetch. No verifiable post-2013 paper improving on the 41/300 lower bound or resolving the conjecture was found across 5 search queries.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. If $ T $ is a tournament of order $ n $ , then it contains $ \left \lceil n(n-1)/6 - n/3\right\rceil $ arc-disjoint transitive subtournaments of order 3.

Discussion

If true the conjecture would be tight as shown by any tournament whose vertex set can be decomposed into $ 3 $ sets $ V_1, V_2, V_3 $ of size $ \lceil n/3 \rceil $ or $ \lfloor n/3\rfloor $ and such that $ V_1\rightarrow V_2 $ , $ V_2\rightarrow V_3 $ and $ V_3\rightarrow V_1 $ . Let $ TT_3 $ denote the transitive tournament of order 3. A $ TT_3 $ -packing of a digraph $ D $ is a set of arc-disjoint copies of $ TT_3 $ subgraphs of $ D $ . Let $ f(n) $ be the minimum size of a $ TT_3 $ -packing over all tournaments of order $ n $ . The conjecture and its tightness say $ f(n)= \left \lceil n(n-1)/6 - n/3\right\rceil $ . The best lower bound for $ f(n) $ so far is due to Kabiya and Yuster [KY] proved that $ f(n) > \frac{41}{300} n^2(1+o(1)) $ .

Bibliography

 [KY]
 M. Kabiya and R. Yuster. Packing transitive triples in a tournament. Ann. Comb. 12 (2008), no. 3, 291–-306.

★ [Y]
 R. Yuster. The number of edge-disjoint transitive triples in a tournament. Discrete Math. 287 (2004). no. 1-3,187--191.
