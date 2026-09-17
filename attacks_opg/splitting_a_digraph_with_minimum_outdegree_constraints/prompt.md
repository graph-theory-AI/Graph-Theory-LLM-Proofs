Attack the following open graph-theory problem.

Catalog id: splitting_a_digraph_with_minimum_outdegree_constraints
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/splitting_a_digraph_with_minimum_outdegree_constraints/
Original entry: http://www.openproblemgarden.org/op/splitting_a_digraph_with_minimum_outdegree_constraints
Problem attributed to: Alon, Noga (posted 2013-03-01)

=== Problem statement (OpenProblemGarden) ===
Title: Splitting a digraph with minimum outdegree constraints
Problem Is there a minimum integer $ f(d) $ such that the vertices of any digraph with minimum outdegree $ d $ can be partitioned into two classes so that the minimum outdegree of the subgraph induced by each class is at least $ d $ ?

=== Discussion / context (OpenProblemGarden) ===
Thomassen [T] proved the conjecture when $ d=1 $ and showed $ f(1)=3 $ . In fact, this case is equivalent to the case $ k=2 $ of the Bermond-Thomassen Conjecture . The existence of the corresponding function $ f $ for the undirected analogue is easy and has been observed by many authors. Stiebitz [S] even proved the following tight result: if the minimum degree of an undirected graph $ G $ is $ d_1+d_2+ \cdots + d_k $ , where each $ d_i $ is a non-negative integer, then the vertex set of $ G $ can be partitioned into $ k $ pairwise disjoint sets $ V_1,\dots , V_k $ , so that for all $ i $ , the induced subgraph on $ V_i $ has minimum degree at least $ d_i $ . This is clearly tight, as shown by an appropriate complete graph.

=== References listed by OpenProblemGarden ===
- *[A] Noga Alon, Disjoint Directed Cycles, Journal of Combinatorial Theory, Series B, 68 (1996), no. 2, 167-178.
- [S] M. Stiebitz, Decomposing graphs under degree constraints, J. Graph Theory 23 (1996), 31-324.
- [T] C. Thomassen, Disjoint cycles in digraphs, Combinatorica 3 (1983), 393 - 396.

=== Catalog page (statement + literature review) ===
Splitting a digraph with minimum outdegree constraints — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The problem, posed by Alon in 2006, asks whether a finite function $F(s,t)$ exists guaranteeing that every digraph with minimum out-degree at least $F(s,t)$ admits a vertex partition into parts $A$ and $B$ with induced minimum out-degrees at least $s$ and $t$, respectively; it remains open for all $s,t \geq 2$. Christoph, Petrova, and Steiner (2023) proved a key reduction: if $F(2,2)$ is finite, then $F(s,t) = \Theta(s+t)$ for all $s,t \geq 1$, thereby reducing the entire conjecture to the single base case $F(2,2) < \infty$.

 Cited literature (1)

 
 
 
partial A note on digraph splitting
 (2025)
 

 
 Micha Christoph, Kalina Petrova, Raphael Steiner · Combinatorics, Probability and Computing · arXiv:2310.08449

Proves that if $F(2,2) < \infty$ then $F(s,t) = \Theta(s+t)$ for all $s,t \geq 1$, reducing Alon's conjecture to the single case $s=t=2$.
 

 

 Reviewer notes. The Springer paper 'Partition and Disjoint Cycles in Digraphs' by Song and Yan (Graphs and Combinatorics 2023, DOI 10.1007/s00373-023-02631-1) appeared in search result summaries as proving F(d₁,...,dₖ) ≤ 2(d₁+⋯+dₖ) under bounded in-degree conditions, but the Springer page is paywalled and no arXiv preprint was found, so it was excluded from since_posted. The Cambridge Core 'Splitting digraphs' entry is Alon's 2006 problem-posing article (predates the 2013 OPG posting). The arXiv:2310.08449 paper was submitted October 2023 and published online March 2025.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Problem. Is there a minimum integer $ f(d) $ such that the vertices of any digraph with minimum outdegree $ d $ can be partitioned into two classes so that the minimum outdegree of the subgraph induced by each class is at least $ d $ ?

Discussion

Thomassen [T] proved the conjecture when $ d=1 $ and showed $ f(1)=3 $ . In fact, this case is equivalent to the case $ k=2 $ of the Bermond-Thomassen Conjecture . The existence of the corresponding function $ f $ for the undirected analogue is easy and has been observed by many authors. Stiebitz [S] even proved the following tight result: if the minimum degree of an undirected graph $ G $ is $ d_1+d_2+ \cdots + d_k $ , where each $ d_i $ is a non-negative integer, then the vertex set of $ G $ can be partitioned into $ k $ pairwise disjoint sets $ V_1,\dots , V_k $ , so that for all $ i $ , the induced subgraph on $ V_i $ has minimum degree at least $ d_i $ . This is clearly tight, as shown by an appropriate complete graph.

Bibliography

★ [A]
 Noga Alon, Disjoint Directed Cycles, Journal of Combinatorial Theory, Series B, 68 (1996), no. 2, 167-178.

 [S]
 M. Stiebitz, Decomposing graphs under degree constraints, J. Graph Theory 23 (1996), 31-324.

 [T]
 C. Thomassen, Disjoint cycles in digraphs, Combinatorica 3 (1983), 393 - 396.

Related conjectures

 
 related to
 The Bermond-Thomassen Conjecture
 partial
 The OPG context explicitly states only a case-level equivalence: the d=1 case of the splitting problem (Thomassen's f(1)=3) is equivalent to the k=2 case of Bermond-Thomassen (min outdegree 3 gives 2 disjoint cycles); indeed a bipartition with both parts of min outdegree >=1 yields two disjoint cycles, and conversely per Thomassen. But the full statements do not imply each other: for general d, splitting into two parts of min outdegree d says nothing about packing k disjoint cycles under the specific 2k-1 bound, and k disjoint cycles do not yield an outdegree-preserving bipartition. The problems are thematically linked with one coinciding special case, so related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
