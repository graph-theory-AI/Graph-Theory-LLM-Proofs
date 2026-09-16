Attack the following open graph-theory problem.

Catalog id: hoand_reed_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/hoand_reed_conjecture/
Original entry: http://www.openproblemgarden.org/op/hoand_reed_conjecture
Problem attributed to: Hoang, Chinh T., Reed, Bruce A. (posted 2013-03-11)

=== Problem statement (OpenProblemGarden) ===
Title: Hoàng-Reed Conjecture
Conjecture Every digraph in which each vertex has outdegree at least $ k $ contains $ k $ directed cycles $ C_1, \ldots, C_k $ such that $ C_j $ meets $ \cup_{i=1}^{j-1}C_i $ in at most one vertex, $ 2 \leq j \leq k $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is not even known to be true for $ k=3 $ . In the case $ k=2 $ , Thomassen proved [T] that every digraph with minimum outdegree 2 has two directed cycles intersecting on a vertex. This conjecture would imply the Caccetta-Häggkvist Conjecture .

=== References listed by OpenProblemGarden ===
- *[HR] C.T. Hoàng and B. Reed, A note on short cycles in digraphs, Discrete Math., 66 (1987), 103-107.
- [T] C. Thomassen, The 2-linkage problem for acyclic digraphs, Discrete Math., 55 (1985), 73-87.

=== Catalog page (statement + literature review) ===
Hoàng-Reed Conjecture — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The Hoàng–Reed conjecture remains open for general $k \geq 4$. All known partial results predate the 2013 OPG posting: the $k=2$ case (Thomassen, 1985), tournaments (Havet, Thomassé, and Yeo, ~2007), and the $k=3$ case (proved using the notion of nearest separators, ~2010), making the OPG's note that '$k=3$ is not known' likely an oversight. No post-2013 paper resolving further cases of the conjecture was identified.

 Reviewer notes. ScienceDirect and Springer pages for the key papers returned HTTP 403 and could not be directly verified. HAL pages returned access-denied errors. The arXiv HTML search for 'Hoang Reed' variants returned zero results. The paper 'The Hoàng–Reed Conjecture for δ+=3' (ScienceDirect, ~2010) and 'Hoàng–Reed conjecture holds for tournaments' (Havet, Thomassé, Yeo, ~2007) both predate the OPG posting; the OPG discussion text noting 'k=3 is unknown' appears to be an oversight. arXiv:2407.05827 (Kawarabayashi–Picasarri-Arrieta, 2024) is about a coloring analogue of Reed's conjecture for digraphs, unrelated to the Hoàng–Reed cycle conjecture. arXiv:2503.20045 (Koerts–Moore–Spirkl, 2025) is about cycle orientations in high-chromatic digraphs and does not address the Hoàng–Reed conjecture. I ran 8 search queries, exceeding the recommended 4; the extra queries were needed because arXiv's all-fields search returned no results for all Hoàng-Reed–related terms.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. Every digraph in which each vertex has outdegree at least $ k $ contains $ k $ directed cycles $ C_1, \ldots, C_k $ such that $ C_j $ meets $ \cup_{i=1}^{j-1}C_i $ in at most one vertex, $ 2 \leq j \leq k $ .

Discussion

This conjecture is not even known to be true for $ k=3 $ . In the case $ k=2 $ , Thomassen proved [T] that every digraph with minimum outdegree 2 has two directed cycles intersecting on a vertex. This conjecture would imply the Caccetta-Häggkvist Conjecture .

Bibliography

★ [HR]
 C.T. Hoàng and B. Reed, A note on short cycles in digraphs, Discrete Math., 66 (1987), 103-107.

 [T]
 C. Thomassen, The 2-linkage problem for acyclic digraphs, Discrete Math., 55 (1985), 73-87.

Related conjectures

 
 implies
 Caccetta-Häggkvist Conjecture
 open
 Assume Hoàng-Reed for k=r on an n-vertex digraph with min outdegree r: it yields cycles C_1,...,C_r where each C_j meets the union of the earlier ones in at most one vertex. Hence |C_1 ∪ ... ∪ C_r| >= sum_i |C_i| - (r-1), and this union has at most n vertices, so sum_i |C_i| <= n + r - 1. The shortest C_i then has length at most floor((n+r-1)/r) = ceil(n/r), which is exactly Caccetta-Häggkvist. The implication is also explicitly stated in both provided contexts (Hoàng-Reed page: 'This conjecture would imply the Caccetta-Häggkvist Conjecture'; C-H page lists Hoàng-Reed as implying it). Direction as claimed.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
