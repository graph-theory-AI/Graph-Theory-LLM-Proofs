Attack the following open graph-theory problem.

Catalog id: hamilton_cycle_in_small_d_diregular_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/hamilton_cycle_in_small_d_diregular_graphs/
Original entry: http://www.openproblemgarden.org/op/hamilton_cycle_in_small_d_diregular_graphs
Problem attributed to: Jackson, Bill (posted 2013-03-08)

=== Problem statement (OpenProblemGarden) ===
Title: Hamilton cycle in small d-diregular graphs
An directed graph is $ k $ -diregular if every vertex has indegree and outdegree at least $ k $ . Conjecture For $ d >2 $ , every $ d $ -diregular oriented graph on at most $ 4d+1 $ vertices has a Hamilton cycle.

=== Discussion / context (OpenProblemGarden) ===
The disjoint union of two regular tournaments on $ 2d+1 $ vertices shows that this would be best possible. For $ d $ -diregular oriented graphs with an arbitrary order of vertices, Jackson conjectured the existence of a long cycle . Kühn and Osthus [KO] conjectured that it may actually be possible to increase the size of the graph even further if we assume that the graph is strongly 2-connected. Problem Is it true that for each $ d >2 $ , every $ d $ -regular strongly $ 2 $ -connected oriented graph $ G $ on at most $ 6d $ vertices has a Hamilton cycle?

=== References listed by OpenProblemGarden ===
- *[J] B. Jackson. Long paths and cycles in oriented graphs, J. Graph Theory 5 (1981), 145-157.
- [KO] D. Osthus and D. Kühn, A survey on Hamilton cycles in directed graphs, European J. Combinatorics 33 (2012), 750-766.

=== Catalog page (statement + literature review) ===
Hamilton cycle in small d-diregular graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Lo, Patel, and Yıldız proved an approximate version of Jackson's conjecture in 2022 (every $d$-regular oriented graph on $n > n_0$ vertices with $d \geq (1/4+\varepsilon)n$ has a Hamilton cycle). Their 2023 follow-up establishes Jackson's conjecture itself for sufficiently large $n$: there exists $n_0$ such that every $d$-regular oriented graph on $n \geq n_0$ vertices with $n \leq 4d+1$ has a Hamilton cycle. The original conjecture for all $d > 2$ (including small values) remains open.

 Cited literature (2)

 
 
 
partial Hamilton Cycles in Dense Regular Digraphs and Oriented Graphs
 (2023)
 

 
 Allan Lo, Viresh Patel, Mehmet Akif Yıldız · Journal of Combinatorial Theory, Series B · arXiv:2203.10112

Proves that for every $\varepsilon > 0$ there exists $n_0$ such that every $d$-regular oriented graph on $n > n_0$ vertices with $d \geq (1/4 + \varepsilon)n$ has a Hamilton cycle, giving an approximate version of Jackson's conjecture.
 

 
 
partial Cycle Partitions in Dense Regular Digraphs and Oriented Graphs
 (2025)
 

 
 Allan Lo, Viresh Patel, Mehmet Akif Yıldız · Forum of Mathematics, Sigma · arXiv:2309.11677

Proves Jackson's conjecture for sufficiently large $n$: there exists $n_0$ such that every $d$-regular oriented graph on $n \geq n_0$ vertices with $n \leq 4d+1$ has a Hamilton cycle, via a cycle-partition result showing at most $n/(2d+1)$ vertex-disjoint cycles suffice.
 

 

 Reviewer notes. arXiv:1907.08479 (Liebenau–Pehova, 2019) addresses a different Jackson conjecture about bipartite tournaments and is excluded from since_posted. The ScienceDirect page for 2203.10112 (JCTB) returned HTTP 403; DOI not confirmed. The 2309.11677 result proves Jackson's conjecture for all sufficiently large n (leaving finitely many small-d cases open); the exact value of n₀ is not specified explicitly. The Kühn–Osthus variant (strongly 2-connected, at most 6d vertices) appears to remain open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. For $ d >2 $ , every $ d $ -diregular oriented graph on at most $ 4d+1 $ vertices has a Hamilton cycle.

Discussion

The disjoint union of two regular tournaments on $ 2d+1 $ vertices shows that this would be best possible. For $ d $ -diregular oriented graphs with an arbitrary order of vertices, Jackson conjectured the existence of a long cycle . Kühn and Osthus [KO] conjectured that it may actually be possible to increase the size of the graph even further if we assume that the graph is strongly 2-connected. Problem Is it true that for each $ d >2 $ , every $ d $ -regular strongly $ 2 $ -connected oriented graph $ G $ on at most $ 6d $ vertices has a Hamilton cycle?

Bibliography

★ [J]
 B. Jackson. Long paths and cycles in oriented graphs, J. Graph Theory 5 (1981), 145-157.

 [KO]
 D. Osthus and D. Kühn, A survey on Hamilton cycles in directed graphs, European J. Combinatorics 33 (2012), 750-766.
