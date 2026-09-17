Attack the following open graph-theory problem.

Catalog id: chromatic_number_of_random_lifts_of_complete_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Probabilistic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/chromatic_number_of_random_lifts_of_complete_graphs/
Original entry: http://www.openproblemgarden.org/op/chromatic_number_of_random_lifts_of_complete_graphs
Problem attributed to: Amit, Linial, Matousek (posted 2012-09-03)

=== Problem statement (OpenProblemGarden) ===
Title: Chromatic number of random lifts of complete graphs
Question Is the chromatic number of a random lift of $ K_5 $ concentrated on a single value?

=== Discussion / context (OpenProblemGarden) ===
Let $ G $ be a graph with vertex set $ V $ and edge set $ E $ . An $ h $ -lift $ H $ is a graph with vertex set $ V\times\{1,\dots,h\} $ , such that $ (u,k) $ and $ (v,\ell) $ may only be adjacent in $ H $ if $ uv \in E $ , and for each $ uv\in E $ , the edges between $ \{u\}\times\{1,\dots,h\} $ and $ \{v\}\times\{1,\dots,h\} $ form a perfect matching. A random $ h $ -lift of $ G $ is a graph drawn uniformly at random from the set of all $ h $ -lifts of $ G $ . This amounts to choosing, independently at random, a perfect matching for each edge of $ G $ . One is generally interested in properties of random $ h $ -lifts when $ h\to\infty $ . Amit, Linial, and Matousek [ALM02] have studied the chromatic number of random lifts. They ask whether a the chromatic number of a random $ h $ -lift of $ K_5 $ is asymptotically almost surely a single number. It is easy to see that this number may be either 3 or 4. Farzad and Theis [FT12] have shown that random lifts of $ K_5\setminus e $ are asymptotically almost surely 3-colorable. A more general question is this. Question Is the chromatic number of a random lift of $ K_n $ concentrated on a single value? Amit, Linial, and Matousek [ALM02] have shown that the chromatic number of a random lift of $ K_n $ is in $ \Theta(n/\log n) $ .

=== References listed by OpenProblemGarden ===
- *[ALM02] Random Lifts of Graphs III: Independence and Chromatic Number, A. Amit, N. Linial and J. Matousek, Random Structures and Algorithms, 20(2002) 1-22.
- [FT12] Random lifts of are 3-colourable. B. Farzad and D.O. Theis. SIAM J. Discrete Math. 26:1 (2012), 169–179.

=== Catalog page (statement + literature review) ===
Chromatic number of random lifts of complete graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Nir and Pérez Giménez (2021) proved that for fixed $d \geq 3$, the chromatic number of a random $n$-lift of $K_{d+1}$ is a.a.s. either $k$ or $k+1$, where $k$ is the smallest integer satisfying $d < 2k\log k$; moreover, for roughly half of all values of $d$, the chromatic number concentrates on the single value $k$. The specific question of whether the chromatic number of a random lift of $K_5$ ($d=4$, $k=3$) concentrates on a single value (3 or 4) is not definitively resolved by this work and remains open.

 Cited literature (1)

 
 
 
partial The chromatic number of random lifts of complete graphs
 (2021)
 

 
 JD Nir, Xavier Pérez Giménez · arXiv preprint · arXiv:2109.13347

Proves that for fixed $d \geq 3$, the chromatic number of a random $n$-lift of $K_{d+1}$ is a.a.s. $k$ or $k+1$ (where $k$ is the smallest integer with $d < 2k\log k$), and further concentrates on the single value $k$ for roughly half of all values of $d$; the upper bound uses the small subgraph conditioning method and extends to random lifts of arbitrary fixed $d$-regular graphs.
 

 

 Reviewer notes. The paper arXiv:2109.13347 (Nir, Pérez Giménez, submitted September 2021) directly addresses the OPG problem and is the dominant post-2012 result. No journal reference was found; it may still be a preprint. The abstract page confirmed that the paper does not definitively resolve the K_5 question (whether d=4 falls in the 'roughly half' of d values with single-value concentration is unclear from the abstract alone). Attempts to fetch the Semantic Scholar page, arXiv HTML versions, and the PDF all failed or returned empty content; only the plain arXiv abstract page at https://arxiv.org/abs/2109.13347 was successfully verified. No further post-2012 papers specifically on this problem were found in the searches.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 146s.
 

Question. Is the chromatic number of a random lift of $ K_5 $ concentrated on a single value?

Keywords:
random lifts, coloring

Discussion

Let $ G $ be a graph with vertex set $ V $ and edge set $ E $ . An $ h $ -lift $ H $ is a graph with vertex set $ V\times\{1,\dots,h\} $ , such that $ (u,k) $ and $ (v,\ell) $ may only be adjacent in $ H $ if $ uv \in E $ , and for each $ uv\in E $ , the edges between $ \{u\}\times\{1,\dots,h\} $ and $ \{v\}\times\{1,\dots,h\} $ form a perfect matching. A random $ h $ -lift of $ G $ is a graph drawn uniformly at random from the set of all $ h $ -lifts of $ G $ . This amounts to choosing, independently at random, a perfect matching for each edge of $ G $ . One is generally interested in properties of random $ h $ -lifts when $ h\to\infty $ . Amit, Linial, and Matousek [ALM02] have studied the chromatic number of random lifts. They ask whether a the chromatic number of a random $ h $ -lift of $ K_5 $ is asymptotically almost surely a single number. It is easy to see that this number may be either 3 or 4. Farzad and Theis [FT12] have shown that random lifts of $ K_5\setminus e $ are asymptotically almost surely 3-colorable. A more general question is this. Question Is the chromatic number of a random lift of $ K_n $ concentrated on a single value? Amit, Linial, and Matousek [ALM02] have shown that the chromatic number of a random lift of $ K_n $ is in $ \Theta(n/\log n) $ .

Bibliography

★ [ALM02]
 Random Lifts of Graphs III: Independence and Chromatic Number, A. Amit, N. Linial and J. Matousek, Random Structures and Algorithms, 20(2002) 1-22.

 [FT12]
 Random lifts of $ K_5\setminus e $ are 3-colourable. B. Farzad and D.O. Theis. SIAM J. Discrete Math. 26:1 (2012), 169–179.
