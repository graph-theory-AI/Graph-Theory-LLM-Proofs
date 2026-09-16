Attack the following open graph-theory problem.

Catalog id: circular_colouring_the_orthogonality_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/circular_colouring_the_orthogonality_graph/
Original entry: http://www.openproblemgarden.org/op/circular_colouring_the_orthogonality_graph
Problem attributed to: DeVos, Matt, Ghebleh, Mohammad, Goddyn, Luis A., Mohar, Bojan, Naserasr, Reza (posted 2008-09-23)

=== Problem statement (OpenProblemGarden) ===
Title: Circular colouring the orthogonality graph
Let $ {\mathcal O} $ denote the graph with vertex set consisting of all lines through the origin in $ {\mathbb R}^3 $ and two vertices adjacent in $ {\mathcal O} $ if they are perpendicular. Problem Is $ \chi_c({\mathcal O}) = 4 $ ?

=== Discussion / context (OpenProblemGarden) ===
In the problem statement, $ \chi_c $ denotes the circular chromatic number . Coloring properties of $ {\mathcal O} $ are, rather surprisingly, of interest in quantum mechanics. If the spins of certain particles are measured in three orthogonal directions, then these measurements always return one $ 0 $ and two values which are $ \pm 1 $ . If such a particle has "decided" in advance how it will respond to any possible measurement, then the set of directions in which it will respond $ 0 $ must be an independent set in the orthogonality graph $ {\mathcal O} $ which meets every triangle. Kochen and Specker have shown that $ {\mathcal O} $ (even certain finite subgraphs of it) does not have any independent set meeting every triangle, thus exhibiting a rather mysterious property of these particles. In some sense, if the person doing the measurement has the free will to decide in which directions to measure, then the particle must have some free will to decide how it will respond. The property that $ {\mathcal O} $ has no independent set which meets every triangle shows that $ \chi({\mathcal O}) \ge 4 $ . On the other hand, if we center a regular octahedron at the origin, and assign a color to each line $ L $ depending on which pair of opposite faces it passes through (if $ L $ meets more than one pair of opposite faces, just choose one) we get a proper 4-coloring of $ {\mathcal O} $ . Therefore, $ \chi({\mathcal O}) = 4 $ . These bounds prove that $ 3 \le \chi_c({\mathcal O}) \le 4 $ . By investigating certain finite subgraphs of $ {\mathcal O} $ , DeVos, Ghebleh, Goddyn, Mohar, and Naserasr have shown that $ \chi_c({\mathcal O}) \ge 3.5 $ .

=== Catalog page (statement + literature review) ===
Circular colouring the orthogonality graph — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem asks whether the circular chromatic number of the orthogonality graph $\mathcal{O}$ (vertices = lines through the origin in $\mathbb{R}^3$, edges = orthogonal pairs) equals 4. The bounds $3.5 \le \chi_c(\mathcal{O}) \le 4$ established by DeVos, Ghebleh, Goddyn, Mohar, and Naserasr remain the state of the art; no subsequent paper improving either bound was found in any of the searched sources.

 Reviewer notes. The SIAM Journal paper 'Coloring an Orthogonality Graph' (DOI: 10.1137/050639715) appears to be the source of the lower bound χ_c(O) ≥ 3.5, but the SIAM server returned HTTP 403 on both direct and DOI-redirect fetches, so its full content could not be verified. An arXiv full-text search for 'circular chromatic orthogonality graph' returned zero results. Naserasr's DBLP bibliography (post-2008) contains no paper on this specific problem. The 2025 arXiv paper (2512.01195) on 'Quantum Chromatic Number of Subgraphs of Orthogonality Graphs' concerns quantum chromatic number, not circular chromatic number, and is thus unrelated. The problem remains open as of the search date.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 168s.
 

Problem. Is $ \chi_c({\mathcal O}) = 4 $ ?

Keywords:
circular coloring · geometric graph · orthogonality

Discussion

In the problem statement, $ \chi_c $ denotes the circular chromatic number . Coloring properties of $ {\mathcal O} $ are, rather surprisingly, of interest in quantum mechanics. If the spins of certain particles are measured in three orthogonal directions, then these measurements always return one $ 0 $ and two values which are $ \pm 1 $ . If such a particle has "decided" in advance how it will respond to any possible measurement, then the set of directions in which it will respond $ 0 $ must be an independent set in the orthogonality graph $ {\mathcal O} $ which meets every triangle. Kochen and Specker have shown that $ {\mathcal O} $ (even certain finite subgraphs of it) does not have any independent set meeting every triangle, thus exhibiting a rather mysterious property of these particles. In some sense, if the person doing the measurement has the free will to decide in which directions to measure, then the particle must have some free will to decide how it will respond. The property that $ {\mathcal O} $ has no independent set which meets every triangle shows that $ \chi({\mathcal O}) \ge 4 $ . On the other hand, if we center a regular octahedron at the origin, and assign a color to each line $ L $ depending on which pair of opposite faces it passes through (if $ L $ meets more than one pair of opposite faces, just choose one) we get a proper 4-coloring of $ {\mathcal O} $ . Therefore, $ \chi({\mathcal O}) = 4 $ . These bounds prove that $ 3 \le \chi_c({\mathcal O}) \le 4 $ . By investigating certain finite subgraphs of $ {\mathcal O} $ , DeVos, Ghebleh, Goddyn, Mohar, and Naserasr have shown that $ \chi_c({\mathcal O}) \ge 3.5 $ .
