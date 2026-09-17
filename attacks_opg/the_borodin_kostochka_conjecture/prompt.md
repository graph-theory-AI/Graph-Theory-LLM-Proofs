Attack the following open graph-theory problem.

Catalog id: the_borodin_kostochka_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_borodin_kostochka_conjecture/
Original entry: http://www.openproblemgarden.org/op/the_borodin_kostochka_conjecture
Problem attributed to: Borodin, Oleg V., Kostochka, Alexandr V. (posted 2012-09-10)

=== Problem statement (OpenProblemGarden) ===
Title: The Borodin-Kostochka Conjecture
Conjecture Every graph with maximum degree $ \Delta \geq 9 $ has chromatic number at most $ \max\{\Delta-1, \omega\} $ .

=== Discussion / context (OpenProblemGarden) ===
The Borodin-Kostochka conjecture proposes that for any graph $ G $ with maximum degree $ \Delta $ and clique number $ \omega < \Delta $ , $ G $ is $ \Delta-1 $ colourable so long as $ \Delta $ is sufficiently large (specifically, $ \Delta\geq 9 $ ). The requirement that $ \Delta \geq 9 $ is necessary, as one can see by looking at the strong product of $ C_5 $ and $ K_3 $ . Reed [R] proved that there exists a $ \Delta_0 $ for which the conjecture holds whenever $ \Delta \geq \Delta_0 $ . Specifically he proved that $ \Delta_0 \leq 10^{14} $ , but claims that more careful analysis could reduce $ \Delta_0 $ to 1000. The conjecture was recently proven by Cranston and Rabern for claw-free graphs [CR]. In their paper they mention an unpublished strengthening proposed by Borodin and Kostochka, namely that one can replace the chromatic number in the statement of the conjecture with the list chromatic number.

=== References listed by OpenProblemGarden ===
- [BK] O. V. Borodin and A. V. Kostochka. On an upper bound of a graph's chromatic number, depending on the graph's degree and density. JCTB 23 (1977), 247--250.
- [CR] D. W. Cranston and L. Rabern. Coloring claw-free graphs with colors, arXiv 1206.1269, 2012.
- [R] B. A. Reed. A strengthening of Brooks’ Theorem. J. Comb. Theory Ser. B, 76:136–149, 1999.

=== Catalog page (statement + literature review) ===
The Borodin-Kostochka Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Borodin–Kostochka conjecture remains open for general graphs with $\Delta \ge 9$. Since the problem was posted, the conjecture has been verified for several hereditary graph classes ($(P_5,\text{gem})$-free, $(P_6,\text{apple,torch})$-free, and others), and the unconditional degree threshold has been reduced from Reed's $\Delta_0 \le 10^{14}$ to $\Delta \ge 5.2\times10^9$ in 2026; a companion 2026 paper also establishes the analogue for correspondence (DP) coloring at $\Delta \ge 3\times10^9$.

 Cited literature (8)

 
 
 
partial Coloring $(P_5, \text{gem})$-free graphs with $\Delta-1$ colors
 (2022)
 

 
 Daniel W. Cranston, Hudson Lafayette, Landon Rabern · Journal of Graph Theory · arXiv:2006.02015

Proves the Borodin–Kostochka conjecture for $(P_5,\text{gem})$-free graphs: if $\Delta(G)\ge 9$ and $\omega(G)\le\Delta(G)-1$ then $\chi(G)\le\Delta(G)-1$.
 

 
 
partial Validity of Borodin and Kostochka Conjecture for classes of graphs without a single, forbidden subgraph on 5 vertices
 (2021)
 

 
 Medha Dhurandhar · arXiv preprint · arXiv:2101.01354

Verifies the conjecture for $(P_4\cup K_1)$-free, $P_5$-free, Chair-free, and graphs with dense neighborhoods.
 

 
 
partial Borodin-Kostochka conjecture for a family of $P_6$-free graphs
 (2023)
 

 
 Di Wu, Rong Wu · arXiv preprint · arXiv:2306.12062

Proves the conjecture for $(P_6,\text{apple,torch})$-free graphs, extending the known result for $(P_5,C_4)$-free graphs.
 

 
 
partial Coloring some $(P_6,C_4)$-free graphs with $\Delta-1$ colors
 (2024)
 

 
 Ran Chen, Di Wu, Xiaowen Zhang · arXiv preprint · arXiv:2405.18455

Proves the conjecture for $(P_6,C_4,H)$-free graphs where $H\in\{K_7,C_5^+\}$.
 

 
 
partial On graphs with chromatic number and maximum degree both equal to nine
 (2024)
 

 
 Rachel Galindo, Jessica McDonald · arXiv preprint · arXiv:2408.12693

Proves structural results in support of the $\Delta=9$ base case of the conjecture, showing that vertex-critical graphs satisfying certain conditions must contain $K_3\vee\overline{K_6}$.
 

 
 
partial On the Borodin–Kostochka conjecture for graphs with large maximum degree
 (2026)
 

 
 Feng Liu, Shuang Sun, Yan Wang · arXiv preprint · arXiv:2603.16670

Reduces the unconditional threshold: every graph with $\Delta\ge 5.2\times10^9$ and $\omega(G)<\Delta$ satisfies $\chi(G)\le\Delta-1$, improving Reed's 1999 bound of $\Delta_0\le 10^{14}$.
 

 
 
partial On Borodin-Kostochka conjecture for correspondence coloring
 (2026)
 

 
 Zděněk Dvořák, Ross J. Kang, David Mikšaník · arXiv preprint · arXiv:2603.14427

Proves that for $\Delta\ge 3\times10^9$, every graph satisfies $\chi_{\mathrm{DP}}(G)\le\max(\omega(G),\Delta-1)$, establishing the correspondence-coloring analogue of the conjecture for large degree.
 

 
 
partial On Borodin-Kostochka conjecture for correspondence coloring
 (2026)
 

 
 Zdeněk Dvořák, Ross J. Kang, David Mikšaník · arXiv preprint · arXiv:2603.14427

Proves the conjecture for the stronger correspondence chromatic number $\chi_{DP}$, showing that for every graph $G$ with $\Delta(G)\geq 3\cdot 10^9$, $\chi_{DP}(G)\leq\max(\omega(G),\Delta(G)-1)$.
 

 

 Reviewer notes. The conjecture is definitively still open in general. A ScienceDirect paper on the list-chromatic version (S0012365X22005064) and a paper on K_{1,3}-bar-free graphs (S0166218X2400266X) returned HTTP 403 and could not be verified; they are not cited. The arXiv paper 2101.01354 by Dhurandhar is not peer-reviewed and should be treated with appropriate caution. The 2026 papers (2603.16670 and 2603.14427) are preprints not yet journal-published as of this review date.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. Every graph with maximum degree $ \Delta \geq 9 $ has chromatic number at most $ \max\{\Delta-1, \omega\} $ .

Discussion

The Borodin-Kostochka conjecture proposes that for any graph $ G $ with maximum degree $ \Delta $ and clique number $ \omega < \Delta $ , $ G $ is $ \Delta-1 $ colourable so long as $ \Delta $ is sufficiently large (specifically, $ \Delta\geq 9 $ ). The requirement that $ \Delta \geq 9 $ is necessary, as one can see by looking at the strong product of $ C_5 $ and $ K_3 $ . Reed [R] proved that there exists a $ \Delta_0 $ for which the conjecture holds whenever $ \Delta \geq \Delta_0 $ . Specifically he proved that $ \Delta_0 \leq 10^{14} $ , but claims that more careful analysis could reduce $ \Delta_0 $ to 1000. The conjecture was recently proven by Cranston and Rabern for claw-free graphs [CR]. In their paper they mention an unpublished strengthening proposed by Borodin and Kostochka, namely that one can replace the chromatic number in the statement of the conjecture with the list chromatic number.

Bibliography

 [BK]
 O. V. Borodin and A. V. Kostochka. On an upper bound of a graph's chromatic number, depending on the graph's degree and density. JCTB 23 (1977), 247--250.

 [CR]
 D. W. Cranston and L. Rabern. Coloring claw-free graphs with $ \Delta-1 $ colors , arXiv 1206.1269, 2012.
 Coloring claw-free graphs with colors

 [R]
 B. A. Reed. A strengthening of Brooks’ Theorem. J. Comb. Theory Ser. B, 76:136–149, 1999.
