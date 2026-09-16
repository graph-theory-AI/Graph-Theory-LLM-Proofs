Attack the following open graph-theory problem.

Catalog id: lovasz_path_removal_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/lovasz_path_removal_conjecture/
Original entry: http://www.openproblemgarden.org/op/lovasz_path_removal_conjecture
Problem attributed to: Lovasz, Laszlo (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Lovász Path Removal Conjecture
Conjecture There is an integer-valued function $ f(k) $ such that if $ G $ is any $ f(k) $ -connected graph and $ x $ and $ y $ are any two vertices of $ G $ , then there exists an induced path $ P $ with ends $ x $ and $ y $ such that $ G-V(P) $ is $ k $ -connected.

=== Discussion / context (OpenProblemGarden) ===
It follows from a theorem of Tutte that any 3-connected graph contains a non-separating path connecting any two vertices, and consequently, $ f(1)=3 $ . When $ k=2 $ , it was independently shown by Chen, Gould, and Yu [CGY] and Kriesell [K] that $ f(2) = 5 $ . Anwering a conjecture of Kriesell, Kawarabayashi et al. [KLRW] proved the following weaker statement, in which one only removes the edges of the path. Theorem There exists a function $ f(k) $ such that for every $ f(k) $ -connected graph $ G $ and any two vertices $ x $ and $ y $ of $ G $ , there exists an induced path $ P $ with ends $ x $ and $ y $ such that $ G\setminus E(P) $ is $ k $ -connected.

=== References listed by OpenProblemGarden ===
- [CGY] G. Chen, R. Gould, X. Yu, Graph connectivity after path removal, Combinatorica 23 (2003) 185--203.
- [KLRW] K. Kawarabayashi, O. Lee, B. Reed, and P. Wollan, A weaker version of Lovasz's path removal conjecture, Journal of Combinatorial Theory, Series B 98 (2008) 972--979.
- [K] M. Kriesell, Induced paths in 5-connected graphs, J. of Graph Theory, 36 (2001), 52--58.
- *[T] C. Thomassen, Graph decompositions with applications to subdivisions and path systems modulo k, J. of Graph Theory, 7 (1983), 261--271.

=== Catalog page (statement + literature review) ===
Lovász Path Removal Conjecture — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The conjecture is established for $k=1$ ($f(1)=3$, via Tutte) and $k=2$ ($f(2)=5$, by Chen–Gould–Yu and independently Kriesell), but remains wide open for all $k \geq 3$. The weaker edge-removal version was proved by Kawarabayashi, Lee, Reed, and Wollan (2008), before the OPG posting. No post-2013 paper verified by this review establishes $f(k)$ for any new value of $k$ or proves the existence of $f(k)$ in general.

 Reviewer notes. The arXiv paper 2402.12639 (Qi and Yan, 2024, 'Removal paths avoiding vertices') was verified but addresses a different (though related) problem: finding k internally disjoint s-t paths avoiding specified vertices such that their combined vertex deletion leaves a 2-connected graph; the paths need not be induced, so this does not directly prove new cases of the Lovász conjecture. A note titled 'A note on Lovász removable path conjecture' hosted at staff.ustc.edu.cn could not be fetched (network timeout) and therefore could not be cited. The ResearchGate page for 'Non-Separating Paths in 4-Connected Graphs' returned 403 Forbidden. All search results confirm the conjecture for k≥3 remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. There is an integer-valued function $ f(k) $ such that if $ G $ is any $ f(k) $ -connected graph and $ x $ and $ y $ are any two vertices of $ G $ , then there exists an induced path $ P $ with ends $ x $ and $ y $ such that $ G-V(P) $ is $ k $ -connected.

Discussion

It follows from a theorem of Tutte that any 3-connected graph contains a non-separating path connecting any two vertices, and consequently, $ f(1)=3 $ . When $ k=2 $ , it was independently shown by Chen, Gould, and Yu [CGY] and Kriesell [K] that $ f(2) = 5 $ . Anwering a conjecture of Kriesell, Kawarabayashi et al. [KLRW] proved the following weaker statement, in which one only removes the edges of the path. Theorem There exists a function $ f(k) $ such that for every $ f(k) $ -connected graph $ G $ and any two vertices $ x $ and $ y $ of $ G $ , there exists an induced path $ P $ with ends $ x $ and $ y $ such that $ G\setminus E(P) $ is $ k $ -connected.

Bibliography

 [CGY]
 G. Chen, R. Gould, X. Yu, Graph connectivity after path removal, Combinatorica 23 (2003) 185--203.

 [KLRW]
 K. Kawarabayashi, O. Lee, B. Reed, and P. Wollan, A weaker version of Lovasz's path removal conjecture, Journal of Combinatorial Theory, Series B 98 (2008) 972--979.

 [K]
 M. Kriesell, Induced paths in 5-connected graphs, J. of Graph Theory, 36 (2001), 52--58.

★ [T]
 C. Thomassen, Graph decompositions with applications to subdivisions and path systems modulo k, J. of Graph Theory, 7 (1983), 261--271.
