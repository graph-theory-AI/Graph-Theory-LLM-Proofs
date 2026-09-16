Attack the following open graph-theory problem.

Catalog id: kriesells_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Connectivity
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/kriesells_conjecture/
Original entry: http://www.openproblemgarden.org/op/kriesells_conjecture
Problem attributed to: Kriesell, Matthias (posted 2013-08-25)

=== Problem statement (OpenProblemGarden) ===
Title: Kriesell's Conjecture
Conjecture Let $ G $ be a graph and let $ T\subseteq V(G) $ such that for any pair $ u,v\in T $ there are $ 2k $ edge-disjoint paths from $ u $ to $ v $ in $ G $ . Then $ G $ contains $ k $ edge-disjoint trees, each of which contains $ T $ .

=== Discussion / context (OpenProblemGarden) ===
This problem was featured as unsolved problem #22 in Bondy and Murty's book "Graph Theory" [BM]. See also a posting on the open problem forum of the Egerváry Research Group on Combinatorial Optimization.

=== References listed by OpenProblemGarden ===
- [BM] J. A. Bondy and U. S. R. Murty. Graph theory, volume 244 of Graduate Texts in Mathematics. Springer, New York, 2008.

=== Catalog page (statement + literature review) ===
Kriesell's Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Kriesell's conjecture that 2k-edge-connectivity of $T$ in $G$ guarantees $k$ edge-disjoint $T$-Steiner trees remains open in full generality. The best known result (DeVos, McDonald, Pivotto, 2016) shows that edge-cuts separating $T$ of size at least $5k+4$ suffice, improving earlier bounds of $6.5k$ (West–Wu) and $24k$ (Lau). Special cases are settled: the conjecture holds when $|T| \leq 5$, when $V\setminus T$ is a stable set in a $3k$-edge-connected graph, and when every vertex in $V\setminus T$ has even degree.

 Cited literature (1)

 
 
 
partial Packing Steiner Trees
 (2016)
 

 
 Matt DeVos, Jessica McDonald, Irene Pivotto · Journal of Combinatorial Theory, Series B · arXiv:1307.7621

Proves that $k$ edge-disjoint $T$-Steiner trees exist when every edge-cut separating $T$ has size at least $5k+4$, giving the best known constant-factor relaxation of Kriesell's conjecture and improving earlier bounds of $6.5k$ and $24k$.
 

 

 Reviewer notes. The DeVos–McDonald–Pivotto arXiv preprint (1307.7621) was submitted July 29, 2013, slightly before the OPG posting date of August 25, 2013; it is included here by its journal publication year of 2016. A 2023 paper in Graphs and Combinatorics (DOI: 10.1007/s00373-023-02621-3) titled 'Edge-Disjoint Steiner Trees and Connectors in Graphs' appeared in search results but could not be verified due to Springer paywall restrictions; it may contain further progress. The West–Wu 6.5k result was cited in multiple sources but no specific verified arXiv URL was found. Lau's 24k bound dates from around 2004, predating the OPG posting.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. Let $ G $ be a graph and let $ T\subseteq V(G) $ such that for any pair $ u,v\in T $ there are $ 2k $ edge-disjoint paths from $ u $ to $ v $ in $ G $ . Then $ G $ contains $ k $ edge-disjoint trees, each of which contains $ T $ .

Keywords:
Disjoint paths · edge-connectivity · spanning trees

Discussion

This problem was featured as unsolved problem #22 in Bondy and Murty's book "Graph Theory" [BM]. See also a posting on the open problem forum of the Egerváry Research Group on Combinatorial Optimization.

Bibliography

 [BM]
 J. A. Bondy and U. S. R. Murty. Graph theory, volume 244 of Graduate Texts in Mathematics. Springer, New York, 2008.
