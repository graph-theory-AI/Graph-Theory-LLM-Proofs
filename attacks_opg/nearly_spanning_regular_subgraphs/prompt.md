Attack the following open graph-theory problem.

Catalog id: nearly_spanning_regular_subgraphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/nearly_spanning_regular_subgraphs/
Original entry: http://www.openproblemgarden.org/op/nearly_spanning_regular_subgraphs
Problem attributed to: Alon, Noga, Mubayi, Dhruv (posted 2008-05-22)

=== Problem statement (OpenProblemGarden) ===
Title: Nearly spanning regular subgraphs
Conjecture For every $ \epsilon > 0 $ and every positive integer $ k $ , there exists $ r_0 = r_0(\epsilon,k) $ so that every simple $ r $ -regular graph $ G $ with $ r \ge r_0 $ has a $ k $ -regular subgraph $ H $ with $ |V(H)| \ge (1- \epsilon) |V(G)| $ .

=== Discussion / context (OpenProblemGarden) ===
Petersen's theorem asserts that every regular graph of even degree contains a 2-factor (i.e. a spanning 2-regular subgraph). Iterating this easy result we find that for any pair of positive even integers $ k,r $ , every $ r $ -regular graph has a spanning $ k $ -regular subgraph. The cases when either $ k $ or $ r $ is odd are considerably more complicated. There are some nice general results (see [AFK]) which show that every regular graph of sufficiently high degree contains a $ k $ -regular subgraph. However these theorems give no bound on the size of this subgraph. For $ k=1 $ this conjecture is an easy consequence of Vizing's Theorem. Indeed, this theorem implies that every $ d $ -regular graph $ G $ has a 1-regular subgraph $ H $ with $ |V(H)| \ge (1 - \frac{1}{d+1}) |V(G)| $ (just choose a largest color class from a $ (d+1) $ -edge coloring). Alon [A] proved the conjecture for $ k=2 $ with the help of two famous results on permanents: the Minc Conjecture (proved by Bregman), and the van der Waerden conjecture (proved by Falikman and Egorichev). It is open for all $ k \ge 3 $ .

=== References listed by OpenProblemGarden ===
- *[A] N. Alon, Problems and results in extremal combinatorics, J, Discrete Math. 273 (2003), 31-53.
- [AFK] N. Alon, S. Friedland and G. Kalai, Regular subgraphs of almost regular graphs, J. Combinatorial Theory, Ser. B 37(1984), 79-91.

=== Catalog page (statement + literature review) ===
Nearly spanning regular subgraphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The Alon–Mubayi conjecture remains open for all $k \geq 3$. The $k=1$ case follows from Vizing's theorem and $k=2$ was settled by Alon (using the Bregman and Falikman–Egorichev permanents results) before the problem was posted; no post-2008 paper verifiably proving or substantially advancing the conjecture for any $k \geq 3$ was found. Recent progress on closely related regular-subgraph problems (Erdős–Sauer threshold, chromatic-number/regularity relations) does not address the nearly-spanning requirement.

 Reviewer notes. All post-2008 papers found address different regular-subgraph problems: Erdős–Sauer edge-density threshold (Janzer–Sudakov 2022, arXiv:2204.12455; Chakraborti–Janzer–Methuku–Montgomery 2024, arXiv:2411.11785), chromatic-number/regular-subgraph relations (Janzer–Steiner–Sudakov 2024, arXiv:2410.02437), and nearly-regular subgraphs of random subgraphs (Diskin–Erde–Kang–Krivelevich 2026, EJC v33i1p37). None target the Alon–Mubayi nearly-spanning conjecture for fixed k ≥ 3 in deterministic r-regular graphs. Confidence is medium rather than high because a specialised preprint could exist without prominent web presence.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. For every $ \epsilon > 0 $ and every positive integer $ k $ , there exists $ r_0 = r_0(\epsilon,k) $ so that every simple $ r $ -regular graph $ G $ with $ r \ge r_0 $ has a $ k $ -regular subgraph $ H $ with $ |V(H)| \ge (1- \epsilon) |V(G)| $ .

Keywords:
regular · subgraph

Discussion

Petersen's theorem asserts that every regular graph of even degree contains a 2-factor (i.e. a spanning 2-regular subgraph). Iterating this easy result we find that for any pair of positive even integers $ k,r $ , every $ r $ -regular graph has a spanning $ k $ -regular subgraph. The cases when either $ k $ or $ r $ is odd are considerably more complicated. There are some nice general results (see [AFK]) which show that every regular graph of sufficiently high degree contains a $ k $ -regular subgraph. However these theorems give no bound on the size of this subgraph. For $ k=1 $ this conjecture is an easy consequence of Vizing's Theorem. Indeed, this theorem implies that every $ d $ -regular graph $ G $ has a 1-regular subgraph $ H $ with $ |V(H)| \ge (1 - \frac{1}{d+1}) |V(G)| $ (just choose a largest color class from a $ (d+1) $ -edge coloring). Alon [A] proved the conjecture for $ k=2 $ with the help of two famous results on permanents: the Minc Conjecture (proved by Bregman), and the van der Waerden conjecture (proved by Falikman and Egorichev). It is open for all $ k \ge 3 $ .

Bibliography

★ [A]
 N. Alon, Problems and results in extremal combinatorics , J, Discrete Math. 273 (2003), 31-53.
 Problems and results in extremal combinatorics

 [AFK]
 N. Alon, S. Friedland and G. Kalai, Regular subgraphs of almost regular graphs, J. Combinatorial Theory, Ser. B 37(1984), 79-91.
