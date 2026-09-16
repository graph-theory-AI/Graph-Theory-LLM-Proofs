Attack the following open graph-theory problem.

Catalog id: random_stable_roommates
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Matchings
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/random_stable_roommates/
Original entry: http://www.openproblemgarden.org/op/random_stable_roommates
Problem attributed to: Mertens, Stephan (posted 2008-02-26)

=== Problem statement (OpenProblemGarden) ===
Title: Random stable roommates
Conjecture The probability that a random instance of the stable roommates problem on $ n \in 2{\mathbb N} $ people admits a solution is $ \Theta( n ^{-1/4} ) $ .

=== Discussion / context (OpenProblemGarden) ===
A system of preferences for a graph $ G $ is a family $ \{ >_v \}_{v \in V(G)} $ so that every $ >_v $ is a linear ordering of the neighbors of the vertex $ v $ . We say that $ v $ prefers $ u $ to $ u' $ if $ u >_v u' $ . A perfect matching $ M $ in $ G $ is stable if there do not exist $ uv,u'v' \in M $ so that $ u $ prefers $ v' $ to $ v $ and $ v' $ prefers $ u $ to $ u' $ . A famous theorem of Gale-Shapley [GS] proves that every system of preferences on a complete bipartite graph $ K_{n,n} $ admits a stable perfect matching. Indeed, they provide an amusing algorithm to construct one. On complete graphs, this problem is known as either the homosexual stable marriage problem, or more commonly, the stable roommate problem. Here there does not always exist a solution (that is, a stable perfect matching), but Irving [I] constructed an algorithm which runs in polynomial time, and outputs a solution if one exists. Let $ P_n $ denote the probability that a random instance of the stable roommates problem has a solution (so the above conjecture asserts that $ P_n = \Theta( n^{-1/4} $ ). The following are the best known asymptotic bounds for $ P_n $ (with $ n $ even) and hold for $ n $ sufficiently large. The lower bound is due to Pittel [P] and the upper bound to Pittel and Irving [IP] \[ \frac{2 e ^{3/2} }{ \sqrt{\pi n}} \le P_n \le \frac{\sqrt{e}}{2} \] Mertens [M] did an extensive Monte-Carlo simulation to obtain the above conjecture. Indeed, by guessing at the constant he even offers the stronger conjecture $ P_n \simeq e \sqrt{ \frac{2}{\pi} } n ^{-1/4} $ .

=== References listed by OpenProblemGarden ===
- [GS] D. Gale D and L. S. Shapley, College admissions and the stability of marriage, Am. Math. Mon. 69 9-15.
- [I] R. W. Irving, An efficient algorithm for the stable roommates problem, J. Algorithms 6 577-95.
- [IP] B. Pittel and R. W. Irving, An upper bound for the solvability of a random stable roommates instance, Random Struct. Algorithms 5 465-87.
- *[M] S. Mertens, Random stable matchings, J. Stat. Mech. Theory Exp. 2005, no. 10 MathSciNet
- [P] B. Pittel, The 'stable roommates' problem with random preferences, Ann. Probab. 21 1441-77

=== Catalog page (statement + literature review) ===
Random stable roommates — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Chin and Michelen (2026) established the first vanishing upper bound $P_n \leq n^{-1/17}$, proving that random instances are almost surely unsolvable for large $n$ and confirming a 1989 conjecture of Gusfield and Irving. However, the stronger Mertens conjecture $P_n = \Theta(n^{-1/4})$ remains open; the current best bounds are $\Omega(n^{-1/2}) \leq P_n \leq n^{-1/17}$, leaving a gap around the conjectured exponent $1/4$.

 Cited literature (4)

 
 
 
partial Stable Roommates Problem with Random Preferences
 (2015)
 

 
 Stephan Mertens · arXiv preprint · arXiv:1401.5269

Introduces an $O(n^{3/2})$ average-case algorithm and provides large-scale simulation evidence (up to $n=20000$) supporting the conjecture $p_n = \Theta(n^{-1/4})$.
 

 
 
partial On random stable partitions
 (2017)
 

 
 Boris Pittel · arXiv preprint · arXiv:1705.08340

Shows the expected number of stable partitions with odd cycles grows as $n^{1/4}$ (consistent with the conjecture), but with standard deviation of order $n^{3/8}$, too large to conclude odd cycles exist with high probability, leaving the conjecture unresolved.
 

 
 
partial The random stable roommates problem typically has no solution
 (2026)
 

 
 Byron Chin, Marcus Michelen · arXiv preprint · arXiv:2601.07612

Proves the first vanishing upper bound $P_n \leq n^{-1/17}$ for sufficiently large $n$, confirming the Gusfield–Irving (1989) conjecture that $P_n \to 0$, but the Mertens conjecture $P_n = \Theta(n^{-1/4})$ remains open.
 

 
 
survey Perspectives on Unsolvability in the Roommates Problem
 (2025)
 

 
 Frederik Glitzner, David Manlove · arXiv preprint · arXiv:2505.06717

Empirical study of solvability probability across multiple preference distributions (instances up to $n=5001$) and structural analysis of unstable configurations, finding solution sets are typically small.
 

 

 Reviewer notes. The Mertens conjecture $P_n = \Theta(n^{-1/4})$ posted to OPG in 2008 remains open. The Chin–Michelen 2026 result ($P_n \leq n^{-1/17}$) is a landmark improvement over the previous constant upper bound $\sqrt{e}/2$, but does not yet achieve the conjectured exponent. The Pittel (2017) result on expected number of stable partitions is suggestive but not conclusive. The lower bound $P_n \geq C n^{-1/2}$ (Pittel 1993, predating OPG posting) has not been improved.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. The probability that a random instance of the stable roommates problem on $ n \in 2{\mathbb N} $ people admits a solution is $ \Theta( n ^{-1/4} ) $ .

Keywords:
stable marriage · stable roommates

Discussion

A system of preferences for a graph $ G $ is a family $ \{ >_v \}_{v \in V(G)} $ so that every $ >_v $ is a linear ordering of the neighbors of the vertex $ v $ . We say that $ v $ prefers $ u $ to $ u' $ if $ u >_v u' $ . A perfect matching $ M $ in $ G $ is stable if there do not exist $ uv,u'v' \in M $ so that $ u $ prefers $ v' $ to $ v $ and $ v' $ prefers $ u $ to $ u' $ . A famous theorem of Gale-Shapley [GS] proves that every system of preferences on a complete bipartite graph $ K_{n,n} $ admits a stable perfect matching. Indeed, they provide an amusing algorithm to construct one. On complete graphs, this problem is known as either the homosexual stable marriage problem, or more commonly, the stable roommate problem. Here there does not always exist a solution (that is, a stable perfect matching), but Irving [I] constructed an algorithm which runs in polynomial time, and outputs a solution if one exists. Let $ P_n $ denote the probability that a random instance of the stable roommates problem has a solution (so the above conjecture asserts that $ P_n = \Theta( n^{-1/4} $ ). The following are the best known asymptotic bounds for $ P_n $ (with $ n $ even) and hold for $ n $ sufficiently large. The lower bound is due to Pittel [P] and the upper bound to Pittel and Irving [IP] \[ \frac{2 e ^{3/2} }{ \sqrt{\pi n}} \le P_n \le \frac{\sqrt{e}}{2} \] Mertens [M] did an extensive Monte-Carlo simulation to obtain the above conjecture. Indeed, by guessing at the constant he even offers the stronger conjecture $ P_n \simeq e \sqrt{ \frac{2}{\pi} } n ^{-1/4} $ .

Bibliography

 [GS]
 D. Gale D and L. S. Shapley, College admissions and the stability of marriage, Am. Math. Mon. 69 9-15.

 [I]
 R. W. Irving, An efficient algorithm for the stable roommates problem, J. Algorithms 6 577-95.

 [IP]
 B. Pittel and R. W. Irving, An upper bound for the solvability of a random stable roommates instance, Random Struct. Algorithms 5 465-87.

★ [M]
 S. Mertens, Random stable matchings , J. Stat. Mech. Theory Exp. 2005, no. 10 MathSciNet
 Random stable matchings · MathSciNet

 [P]
 B. Pittel, The 'stable roommates' problem with random preferences, Ann. Probab. 21 1441-77
