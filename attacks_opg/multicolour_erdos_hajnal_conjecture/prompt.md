Attack the following open graph-theory problem.

Catalog id: multicolour_erdos_hajnal_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/multicolour_erdos_hajnal_conjecture/
Original entry: http://www.openproblemgarden.org/op/multicolour_erdos_hajnal_conjecture
Problem attributed to: Erdos, Paul, Hajnal, Andras (posted 2019-10-10)

=== Problem statement (OpenProblemGarden) ===
Title: Multicolour Erdős--Hajnal Conjecture
Conjecture For every fixed $ k\geq2 $ and fixed colouring $ \chi $ of $ E(K_k) $ with $ m $ colours, there exists $ \varepsilon>0 $ such that every colouring of the edges of $ K_n $ contains either $ k $ vertices whose edges are coloured according to $ \chi $ or $ n^\varepsilon $ vertices whose edges are coloured with at most $ m-1 $ colours.

=== Discussion / context (OpenProblemGarden) ===
See [FGP].

=== References listed by OpenProblemGarden ===
- [FGP] Jacob Fox, Andrey Grinshpun and János Pach: The Erdős–Hajnal conjecture for rainbow triangles, J. Combin. Theory, Series B. 111 (2016), 75--125.

=== Catalog page (statement + literature review) ===
Multicolour Erdős--Hajnal Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The multicolour Erdős–Hajnal conjecture remains open in general, even for two colours. Since the problem was posted (2019), Axenovich, Snyder, and Weber confirmed the conjecture for three-colour edge-colorings of $K_n$ that avoid any family of at most three coloured triangle patterns; separately, Axenovich and Weber reduced the full conjecture to the case where the host clique uses at most one more colour than the forbidden pattern, and exhibited surprising non-monotone behaviour in homogeneous-set sizes.

 Cited literature (3)

 
 
 
partial The Erdős-Hajnal conjecture for three colors and multiple forbidden patterns
 (2020)
 

 
 Maria Axenovich, Richard Snyder, Lea Weber · arXiv preprint · arXiv:2005.09269

Confirms the multicolour Erdős–Hajnal conjecture for three-colour edge-colorings of $K_n$ that avoid any family of at most three coloured triangle patterns, providing asymptotically tight bounds.
 

 
 
reduction A note on multicolour Erdős-Hajnal conjecture
 (2023)
 

 
 Maria Axenovich, Lea Weber · arXiv preprint · arXiv:2311.03249

Reduces the multicolour EH-conjecture to the case where the host-clique colour count is equal to or exactly one more than that of the forbidden pattern, and demonstrates that allowing an extra colour can non-monotonically decrease the size of the largest homogeneous set.
 

 
 
partial Rainbow triangles and the Erdős-Hajnal problem in projective geometries
 (2025)
 

 
 Carolyn Chun, James Dylan Douthitt, Wayne Ge, Tony Huynh, Matthew E. Kroeker, Peter Nelson · arXiv preprint · arXiv:2505.13781

Formulates and partially resolves a geometric analogue of the multicolour EH-conjecture for finite projective geometries, proving a Gallai-type decomposition for rainbow-triangle-free three-colourings of PG(n-1,2).
 

 

 Reviewer notes. The two ScienceDirect URLs returned HTTP 403; they appear to be the journal-published versions of arXiv:2005.09269 (Discrete Math. 2021) and arXiv:2311.03249 (Discrete Math. 2025) respectively, but could not be confirmed — both papers are cited via their verified arXiv pages only. The 2025 projective-geometry paper (2505.13781) addresses a geometric analogue rather than the original graph-theoretic statement. The original conjecture remains open for all k≥2 and all colourings χ, including the two-colour case.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. For every fixed $ k\geq2 $ and fixed colouring $ \chi $ of $ E(K_k) $ with $ m $ colours, there exists $ \varepsilon>0 $ such that every colouring of the edges of $ K_n $ contains either $ k $ vertices whose edges are coloured according to $ \chi $ or $ n^\varepsilon $ vertices whose edges are coloured with at most $ m-1 $ colours.

Keywords:
ramsey theory

Discussion

See [FGP].

Bibliography

 [FGP]
 Jacob Fox, Andrey Grinshpun and János Pach: The Erdős–Hajnal conjecture for rainbow triangles, J. Combin. Theory, Series B. 111 (2016), 75--125.

Related conjectures

 
 implies
 The Erdös-Hajnal Conjecture
 partial
 Standard specialization to m=2. Given a graph H on k >= 2 vertices, let chi be the 2-colouring of E(K_k) with colour 1 on edges of H and colour 2 on non-edges. A 2-colouring of E(K_n) is exactly a graph G on n vertices (colour 1 = edge). The multicolour conjecture for (k, chi, m=2) gives epsilon > 0 such that G contains either k vertices whose pairs are coloured according to chi -- an induced copy of H -- or n^epsilon vertices whose pairs use at most m-1 = 1 colour -- a clique or an independent set of size n^epsilon. So every H-free G has a clique or independent set of size n^epsilon, which is Erdos-Hajnal with delta(H) = epsilon. Quantifying over all k and chi covers every fixed H (H with <= 1 vertex is trivial). Direction correct: multicolour is the stronger statement; its m=2 instance is classical EH.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
