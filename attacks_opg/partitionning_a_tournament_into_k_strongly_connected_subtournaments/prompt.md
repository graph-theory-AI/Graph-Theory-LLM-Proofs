Attack the following open graph-theory problem.

Catalog id: partitionning_a_tournament_into_k_strongly_connected_subtournaments
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs » Tournaments
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/partitionning_a_tournament_into_k_strongly_connected_subtournaments/
Original entry: http://www.openproblemgarden.org/op/partitionning_a_tournament_into_k_strongly_connected_subtournaments
Problem attributed to: Thomassen, Carsten (posted 2013-03-15)

=== Problem statement (OpenProblemGarden) ===
Title: Partitionning a tournament into k-strongly connected subtournaments.
Problem Let $ k_1, \dots , k_p $ be positve integer Does there exists an integer $ g(k_1, \dots , k_p) $ such that every $ g(k_1, \dots , k_p) $ -strong tournament $ T $ admits a partition $ (V_1\dots , V_p) $ of its vertex set such that the subtournament induced by $ V_i $ is a non-trivial $ k_i $ -strong for all $ 1\leq i\leq p $ .

=== Discussion / context (OpenProblemGarden) ===
If $ k_i=1 $ for $ 2\leq k_i\leq k_p $ , then $ g(k_1, \dots , k_p) $ exists and is at most $ k_1+3p-3 $ . This follows by an easy induction on $ p $ , by taking $ V_p $ to be a set inducing a directed $ 3 $ -cycle. The following example shows that if it exists $ g(k_1, \dots , k_p)\geq k_1+\cdots + k_p $ . Set $ s=k_1 + \cdots + k_p -1 $ . For $ n\geq 3s $ , let $ R_s(n) $ be a tournament on $ n $ vertices having a set $ R $ of $ s $ vertices such that $ T-R $ a transitive tournament of order $ n-s $ with hamiltonian path $ (v_1,\dots , v_{n-s}) $ , and $ R $ dominates $ \{v_1, \dots , v_{s}\} $ and is dominated by $ \{v_{n-2s+1}, \dots , v_{n-s}\} $ . It easy to check that $ R_s(n) $ is $ s $ -strongly connected. However, every (non-trivial) $ k $ -strong tournament of $ R_s(n) $ must contain at least $ k $ vertices of $ R $ . Hence $ R_s(n) $ does not have a partition $ (V_1\dots , V_p) $ of its vertex set such that the subtournament induced by $ V_i $ is a non-trivial $ k_i $ -strong for all $ 1\leq i\leq p $ . Some small examples give better lower bound. For example, the Paley tournament on 7 vertices which is 3-strong cannot be partionned into two strong subtournaments. However, there are only finitely many known such tournaments. Chen, Gould, and Li [CGL] showed that every $ k $ -strongly connected tournament with at least $ 8k $ vertices has a partition into $ k $ strongly connected tournaments. The existence of $ g(2,2) $ is still open.

=== References listed by OpenProblemGarden ===
- [CGL] G. Chen, R.J. Gould, and H. Li, Partitioning vertices of a tournament into independent cycles, J. combin. Theory Ser B, Vol 83, no. 2 (2001) 213-220.
- *[R] K.B. Reid, Three problems on tournaments, Graph Theory and Its Applications, East. and West. Ann. New York Acad. Sci. 576 (1989), 466-473.

=== Catalog page (statement + literature review) ===
Partitionning a tournament into k-strongly connected subtournaments. — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 Kühn, Osthus, and Townsend (2016) proved that $f_t(k,\ldots,k) = O(k^7 t^4)$ exists, giving an affirmative answer to Thomassen's partition question for the uniform case; the general non-uniform case (different $k_i$) follows trivially by setting $k = \max_i k_i$. Girão and Letzter (2025) subsequently confirmed the optimal linear bound $f_t(k,\ldots,k) = O(kt)$, matching the lower bound up to a constant.

 Cited literature (2)

 
 
 
proof Proof of a tournament partition conjecture and an application to 1-factors with prescribed cycle lengths
 (2016)
 

 
 Daniela Kühn, Deryk Osthus, Timothy Townsend · Combinatorica · arXiv:1309.7677 · doi:10.1007/s00493-015-3186-8

Proves existence of $f_t(k,\ldots,k) = O(k^7 t^4)$, establishing an affirmative answer to Thomassen's question: every sufficiently strongly connected tournament can be partitioned into $t$ parts each inducing a strongly $k$-connected subtournament.
 

 
 
proof Partitioning a tournament into sub-tournaments of high connectivity
 (2025)
 

 
 António Girão, Shoham Letzter · Combinatorica · arXiv:2210.17371 · doi:10.1007/s00493-025-00161-3

Proves the optimal linear bound $f_t(k,\ldots,k) = O(kt)$, confirming a 2016 conjecture of Kühn, Osthus, and Townsend and showing the bound is tight up to a constant factor.
 

 

 Reviewer notes. The Kühn-Osthus-Townsend paper (arXiv:1309.7677, submitted 2013-09-29, published Combinatorica ~2016) formally treats the uniform case (all $k_i = k$). The non-uniform Thomassen problem reduces to the uniform case via $k = \max_i k_i$, so $g(k_1,\ldots,k_p) \leq f_p(\max_i k_i, \ldots, \max_i k_i)$. The Springer pages for both Combinatorica articles were authentication-blocked; publication years and DOIs are inferred from arXiv metadata (last revision June 2025 for Girão-Letzter) and DOI string patterns. The Girão-Letzter paper (arXiv:2210.17371) was confirmed published in Combinatorica with DOI 10.1007/s00493-025-00161-3.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Problem. Let $ k_1, \dots , k_p $ be positve integer Does there exists an integer $ g(k_1, \dots , k_p) $ such that every $ g(k_1, \dots , k_p) $ -strong tournament $ T $ admits a partition $ (V_1\dots , V_p) $ of its vertex set such that the subtournament induced by $ V_i $ is a non-trivial $ k_i $ -strong for all $ 1\leq i\leq p $ .

Discussion

If $ k_i=1 $ for $ 2\leq k_i\leq k_p $ , then $ g(k_1, \dots , k_p) $ exists and is at most $ k_1+3p-3 $ . This follows by an easy induction on $ p $ , by taking $ V_p $ to be a set inducing a directed $ 3 $ -cycle. The following example shows that if it exists $ g(k_1, \dots , k_p)\geq k_1+\cdots + k_p $ . Set $ s=k_1 + \cdots + k_p -1 $ . For $ n\geq 3s $ , let $ R_s(n) $ be a tournament on $ n $ vertices having a set $ R $ of $ s $ vertices such that $ T-R $ a transitive tournament of order $ n-s $ with hamiltonian path $ (v_1,\dots , v_{n-s}) $ , and $ R $ dominates $ \{v_1, \dots , v_{s}\} $ and is dominated by $ \{v_{n-2s+1}, \dots , v_{n-s}\} $ . It easy to check that $ R_s(n) $ is $ s $ -strongly connected. However, every (non-trivial) $ k $ -strong tournament of $ R_s(n) $ must contain at least $ k $ vertices of $ R $ . Hence $ R_s(n) $ does not have a partition $ (V_1\dots , V_p) $ of its vertex set such that the subtournament induced by $ V_i $ is a non-trivial $ k_i $ -strong for all $ 1\leq i\leq p $ . Some small examples give better lower bound. For example, the Paley tournament on 7 vertices which is 3-strong cannot be partionned into two strong subtournaments. However, there are only finitely many known such tournaments. Chen, Gould, and Li [CGL] showed that every $ k $ -strongly connected tournament with at least $ 8k $ vertices has a partition into $ k $ strongly connected tournaments. The existence of $ g(2,2) $ is still open.

Bibliography

 [CGL]
 G. Chen, R.J. Gould, and H. Li, Partitioning vertices of a tournament into independent cycles , J. combin. Theory Ser B, Vol 83, no. 2 (2001) 213-220.
 Partitioning vertices of a tournament into independent cycles

★ [R]
 K.B. Reid, Three problems on tournaments, Graph Theory and Its Applications, East. and West. Ann. New York Acad. Sci. 576 (1989), 466-473.
