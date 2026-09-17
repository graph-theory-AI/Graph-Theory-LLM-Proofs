Attack the following open graph-theory problem.

Catalog id: cycles_in_graphs_of_large_chromatic_number
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/cycles_in_graphs_of_large_chromatic_number/
Original entry: http://www.openproblemgarden.org/op/cycles_in_graphs_of_large_chromatic_number
Problem attributed to: Brewster, Richard C., McGuinness, Sean, Moore, Benjamin, Noel, Jonathan A. (posted 2015-09-20)

=== Problem statement (OpenProblemGarden) ===
Title: Cycles in Graphs of Large Chromatic Number
Conjecture If $ \chi(G)>k $ , then $ G $ contains at least $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ .

=== Discussion / context (OpenProblemGarden) ===
Chudnovsky, Plumettaz, Scott and Seymour [CPSS] proved that every graph with chromatic number at least $ 4 $ contains a cycle of length $ 0\bmod 3 $ . A simpler proof was found by Wrochna [W]. Wrochna's argument was generalised by Brewster, McGuinness, Moore and Noel [BMMN] to the following: if $ \chi(G)>k $ , then $ G $ contains at least TeX Embedding failed! cycles of length $ 0\bmod k $ .} The compete graph on $ k+1 $ vertices has exactly $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ and so the conjecture above, if true, would be best possible.

=== References listed by OpenProblemGarden ===
- [BMMN] R. C. Brewster, S. McGuinness, B. Moore, J. A. Noel, A Dichotomy Theorem for Circular Colouring Reconfiguration, submitted, arXiv:1508.05573v1.
- [CPSS] M. Chudnovsky, M. Plumettaz, A. Scott, and P. Seymour, The Structure of Graphs with no Cycles of Length Divisible by Three, in preparation.
- [Wro] M. Wrochna, unpublished.

=== Catalog page (statement + literature review) ===
Cycles in Graphs of Large Chromatic Number — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The $k=3$ case of the conjecture — every graph with $\chi(G)>3$ contains at least $4$ cycles of length $0\bmod 3$ — was fully resolved by Kim and Picollelli (2024), who proved that every 4-critical graph contains at least 4 such cycles with equality only for $K_4$. They also showed that $(k+1)$-critical graphs with minimum degree $k$ contain at least as many cycles of length $0\bmod r$ as $K_{k+1}$ (provided $k+1\not\equiv 0\pmod{r}$), but the full conjecture for $k\ge 4$ remains open.

 Cited literature (1)

 
 
 
partial 4-Chromatic Graphs Have At Least Four Cycles of Length $0 \bmod 3$
 (2024)
 

 
 Sean Kim, Michael Picollelli · Electronic Journal of Combinatorics · arXiv:2312.05945 · doi:10.37236/12623

Proves the $k=3$ case of the BMMN conjecture in full (every 4-critical graph contains $\ge 4$ cycles of length $0\bmod 3$, uniquely minimised by $K_4$) and also establishes partial results toward the general conjecture for $(k+1)$-critical graphs with minimum degree $k$.
 

 

 Reviewer notes. The Gao–Huo–Ma (2023) result (that $(k+1)$-critical non-complete graphs contain cycles of all lengths mod $k$ for $k\ge 6$) is cited inside the Kim–Picollelli paper but was not independently verified here, so it is not listed in since_posted. The CPSS paper [Chudnovsky–Plumettaz–Scott–Seymour] was originally listed as 'in preparation'; it may have been published but was not found in searches. The 2026 paper arXiv:2605.02731 and arXiv:2601.13552 concern Dean's conjecture (minimum degree, not chromatic number) and are unrelated.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. If $ \chi(G)>k $ , then $ G $ contains at least $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ .

Keywords:
chromatic number · cycles

Discussion

Chudnovsky, Plumettaz, Scott and Seymour [CPSS] proved that every graph with chromatic number at least $ 4 $ contains a cycle of length $ 0\bmod 3 $ . A simpler proof was found by Wrochna [W]. Wrochna's argument was generalised by Brewster, McGuinness, Moore and Noel [BMMN] to the following: if $ \chi(G)>k $ , then $ G $ contains at least TeX Embedding failed! cycles of length $ 0\bmod k $ .} The compete graph on $ k+1 $ vertices has exactly $ \frac{(k+1)(k-1)!}{2} $ cycles of length $ 0\bmod k $ and so the conjecture above, if true, would be best possible.

Bibliography

 [BMMN]
 R. C. Brewster, S. McGuinness, B. Moore, J. A. Noel, A Dichotomy Theorem for Circular Colouring Reconfiguration, submitted, arXiv:1508.05573v1.

 [CPSS]
 M. Chudnovsky, M. Plumettaz, A. Scott, and P. Seymour, The Structure of Graphs with no Cycles of Length Divisible by Three, in preparation.

 [Wro]
 M. Wrochna, unpublished.
