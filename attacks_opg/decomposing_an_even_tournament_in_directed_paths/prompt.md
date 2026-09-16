Attack the following open graph-theory problem.

Catalog id: decomposing_an_even_tournament_in_directed_paths
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs » Tournaments
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/decomposing_an_even_tournament_in_directed_paths/
Original entry: http://www.openproblemgarden.org/op/decomposing_an_even_tournament_in_directed_paths
Problem attributed to: Alspach, Brian, Mason, David W., Pullman, Norman J. (posted 2013-02-26)

=== Problem statement (OpenProblemGarden) ===
Title: Decomposing an even tournament in directed paths.
Conjecture Every tournament $ D $ on an even number of vertices can be decomposed into $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\} $ directed paths.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is clearly tight, because in a decomposition of a directed graph in directed paths, at least $ \max \{0,d^+(v)-d^-(v)\} $ directed paths must start at vertex $ v $ . Observe that the analogue is trivially false for odd tournament: in regular tournament $ d^+(v)=d^-(v) $ for every vertex $ v $ , so $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\}=0 $ . For a tournament of even order $ n $ , $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\}\geq n/2 $ . Since a directed path may have up to $ n-1 $ arcs, it might be possible to cover the $ n(n-1)/2 $ arcs of the tournament if $ n $ is even. If the tournament is almost regular (i.e. $ |d^+(v)-d^-(v)|=1 $ for all vertex $ v $ ), the conjecture asserts that it can be decomposed into directed Hamilton paths. This conjecture for almost regular tournaments would imply the following one due to Kelly. Conjecture Every regular tournament of order $ n $ can be decomposed into $ (n-1)/2 $ Hamilton directed cycles. To see this, consider a regular tournament $ T $ and a vertex $ v $ of $ T $ . The tournament $ T-v $ has even order, and in $ T-v $ , $ \max \{0,d^+(v)-d^-(v)\}=0 $ unless $ v $ is an outneighbour of $ v $ in $ T $ in which case $ \max \{0,d^+(v)-d^-(v)\}=0 $ . Hence $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\}=(n-1)/2 $ . Now if Alspach-Mason-Pulman conjecture holds, $ T-v $ can be decomposed into $ (n-1)/2 $ directed paths. These paths must start at distinct outneighbours of $ v $ in $ T $ and ends at distinct inneighbours of $ v $ in $ T $ . Hence, we can complete each directed path in a Hamilton directed cycle in $ T $ to obtain a decomposition of $ T $ into $ (n-1)/2 $ Hamilton cycles. Kelly's conjecture has been proved for tournaments of sufficiently large order by Kühn and Osthus [KO].

=== References listed by OpenProblemGarden ===
- *[AMP] Brian Alspach, David W. Mason, Norman J. Pullman, Path numbers of tournaments, Journal of Combinatorial Theory, Series B, 20 (1976), no. 3, June 1976, 222–228
- [KO] Daniela Kühn and Deryk Osthus, Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments, Advances in Mathematics 237 (2013), 62-146.

=== Catalog page (statement + literature review) ===
Decomposing an even tournament in directed paths. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Alspach–Mason–Pullman conjecture has been proved for all sufficiently large even tournaments by Girão, Granet, Kühn, Lo, and Osthus (2023), who showed any such tournament decomposes into exactly $\mathrm{ex}(T) = \frac{1}{2}\sum_{v}|d^+(v)-d^-(v)|$ directed paths; they also obtained an asymptotically optimal result for odd tournaments. An earlier paper of Lo, Patel, Skokan, and Talbot (2020) had proved many specific cases of the conjecture. The conjecture for all even tournaments (including small orders) remains open.

 Cited literature (2)

 
 
 
partial Decomposing tournaments into paths
 (2020)
 

 
 Allan Lo, Viresh Patel, Jozef Skokan, John Talbot · Proceedings of the London Mathematical Society · arXiv:1902.10775 · doi:10.1112/plms.12328

Proves many previously open cases of the Alspach–Mason–Pullman conjecture on decomposing tournaments of even order into a minimum number of directed paths.
 

 
 
partial Path decompositions of tournaments
 (2023)
 

 
 António Girão, Bertille Granet, Daniela Kühn, Allan Lo, Deryk Osthus · Proceedings of the London Mathematical Society · arXiv:2010.14158 · doi:10.1112/plms.12480

Proves the Alspach–Mason–Pullman conjecture for all sufficiently large even tournaments, and establishes an asymptotically optimal result for odd tournaments.
 

 

 Reviewer notes. The conjecture is proved for all sufficiently large n but the threshold is not made explicit in the abstracts; small even orders may still be open. The PLMS journal pages for both papers returned 403/access errors; verification was done via arXiv abstract pages. No complete proof for all even tournaments has been found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Every tournament $ D $ on an even number of vertices can be decomposed into $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\} $ directed paths.

Discussion

This conjecture is clearly tight, because in a decomposition of a directed graph in directed paths, at least $ \max \{0,d^+(v)-d^-(v)\} $ directed paths must start at vertex $ v $ . Observe that the analogue is trivially false for odd tournament: in regular tournament $ d^+(v)=d^-(v) $ for every vertex $ v $ , so $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\}=0 $ . For a tournament of even order $ n $ , $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\}\geq n/2 $ . Since a directed path may have up to $ n-1 $ arcs, it might be possible to cover the $ n(n-1)/2 $ arcs of the tournament if $ n $ is even. If the tournament is almost regular (i.e. $ |d^+(v)-d^-(v)|=1 $ for all vertex $ v $ ), the conjecture asserts that it can be decomposed into directed Hamilton paths. This conjecture for almost regular tournaments would imply the following one due to Kelly. Conjecture Every regular tournament of order $ n $ can be decomposed into $ (n-1)/2 $ Hamilton directed cycles. To see this, consider a regular tournament $ T $ and a vertex $ v $ of $ T $ . The tournament $ T-v $ has even order, and in $ T-v $ , $ \max \{0,d^+(v)-d^-(v)\}=0 $ unless $ v $ is an outneighbour of $ v $ in $ T $ in which case $ \max \{0,d^+(v)-d^-(v)\}=0 $ . Hence $ \sum_{v\in V}\max\{0,d^+(v)-d^-(v)\}=(n-1)/2 $ . Now if Alspach-Mason-Pulman conjecture holds, $ T-v $ can be decomposed into $ (n-1)/2 $ directed paths. These paths must start at distinct outneighbours of $ v $ in $ T $ and ends at distinct inneighbours of $ v $ in $ T $ . Hence, we can complete each directed path in a Hamilton directed cycle in $ T $ to obtain a decomposition of $ T $ into $ (n-1)/2 $ Hamilton cycles. Kelly's conjecture has been proved for tournaments of sufficiently large order by Kühn and Osthus [KO].

Bibliography

★ [AMP]
 Brian Alspach, David W. Mason, Norman J. Pullman, Path numbers of tournaments , Journal of Combinatorial Theory, Series B, 20 (1976), no. 3, June 1976, 222–228
 Path numbers of tournaments

 [KO]
 Daniela Kühn and Deryk Osthus, Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments, Advances in Mathematics 237 (2013), 62-146.
