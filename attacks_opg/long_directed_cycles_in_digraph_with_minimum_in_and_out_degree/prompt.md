Attack the following open graph-theory problem.

Catalog id: long_directed_cycles_in_digraph_with_minimum_in_and_out_degree
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/long_directed_cycles_in_digraph_with_minimum_in_and_out_degree/
Original entry: http://www.openproblemgarden.org/op/long_directed_cycles_in_digraph_with_minimum_in_and_out_degree
Problem attributed to: Jackson, Bill (posted 2013-03-01)

=== Problem statement (OpenProblemGarden) ===
Title: Long directed cycles in diregular digraphs
Conjecture Every strong oriented graph in which each vertex has indegree and outdegree at least $ d $ contains a directed cycle of length at least $ 2d+1 $ .

=== Discussion / context (OpenProblemGarden) ===
The disjoint union of two regular tournaments on $ 2d+1 $ vertices shows that this would be best possible. If the oriented graph has order at most $ 4d+1 $ , Jackson conjecture the existence of a longer cycle, namely a Hamilton cycle

=== References listed by OpenProblemGarden ===
- *[J] B. Jackson. Long paths and cycles in oriented graphs. J. Graph Theory 5 (1981), 145--157.

=== Catalog page (statement + literature review) ===
Long directed cycles in diregular digraphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 Jackson's 1981 conjecture that every strong oriented graph with minimum indegree and outdegree at least $d$ contains a directed cycle of length at least $2d+1$ remains open. The 1981 paper established directed paths of length at least $2d$, but the cycle version for strongly connected graphs is unresolved. Related progress has been made on a distinct Jackson conjecture: Lo, Patel, and Yıldız (2023) proved for sufficiently large $n$ that every $d$-regular oriented graph on $n \leq 4d+1$ vertices contains a Hamilton cycle, but this does not settle the general minimum-semidegree conjecture.

 Cited literature (1)

 
 
 
partial Cycle Partitions in Dense Regular Digraphs and Oriented Graphs
 (2025)
 

 
 Allan Lo, Viresh Patel, Mehmet Akif Yıldız · Forum of Mathematics, Sigma · arXiv:2309.11677 · doi:10.1017/fms.2025.28

Proves for sufficiently large $n$ that every $d$-regular oriented graph on $n \leq 4d+1$ vertices has a Hamilton cycle (a related but distinct Jackson conjecture from 1981), and that $d$-regular oriented graphs on $n$ vertices can be covered by at most $n/(2d+1)$ vertex-disjoint cycles; does not address the OPG conjecture for general strong oriented graphs with minimum semidegree $d$.
 

 

 Reviewer notes. The OPG conjecture (cycles of length ≥ 2d+1 in strong oriented graphs with minimum semidegree d) is distinct from the Jackson Hamilton-cycle conjecture (Hamilton cycles in d-regular oriented graphs on n ≤ 4d+1 vertices). Most search results and papers found address the latter or the Caccetta–Häggkvist / Kelly–Kühn–Osthus conjectures. No post-2013 paper directly proving or disproving the OPG conjecture was found after exhausting 6 search queries. The Lo–Patel–Yıldız result is the closest related progress but addresses a different (more restricted) setting.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. Every strong oriented graph in which each vertex has indegree and outdegree at least $ d $ contains a directed cycle of length at least $ 2d+1 $ .

Discussion

The disjoint union of two regular tournaments on $ 2d+1 $ vertices shows that this would be best possible. If the oriented graph has order at most $ 4d+1 $ , Jackson conjecture the existence of a longer cycle, namely a Hamilton cycle

Bibliography

★ [J]
 B. Jackson. Long paths and cycles in oriented graphs. J. Graph Theory 5 (1981), 145--157.
