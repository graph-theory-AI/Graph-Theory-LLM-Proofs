Attack the following open graph-theory problem.

Catalog id: friendly_partitions
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/friendly_partitions/
Original entry: http://www.openproblemgarden.org/op/friendly_partitions
Problem attributed to: DeVos, Matt (posted 2009-11-08)

=== Problem statement (OpenProblemGarden) ===
Title: Friendly partitions
A friendly partition of a graph is a partition of the vertices into two sets so that every vertex has at least as many neighbours in its own class as in the other. Problem Is it true that for every $ r $ , all but finitely many $ r $ -regular graphs have friendly partitions?

=== Discussion / context (OpenProblemGarden) ===
Let me say at the start, that I (M. DeVos) suspect this problem has been considered previously, so I await a more correct attribution. An unfriendly partition of a graph is a partition of the vertices into two sets so that every vertex has at least as many neighbours in the opposite class as its own. It is an easy fact that every (finite) graph has an unfriendly partition; for instance, any maximum size edge-cut gives a partition with this property. Finding friendly partitions appears to be considerably more difficult. Perhaps one reason why is that there exist graphs without unfriendly partitions. For instance, $ K_{2n} $ and $ K_{2n+1,2n+1} $ have no unfriendly partitions. However, it appears possible that the only graphs which fail to have friendly partitions are fairly dense. When $ r=3 $ , the above problem is fairly easy to solve, as it reduces to the problem of finding two vertex disjoint cycles. Every cubic graph other than $ K_4 $ or $ K_{3,3} $ has two disjoint cycles, and thus has a friendly partition. The case when $ r=4 $ is also not terribly complicated. However, the next step up, $ r=5 $ looks like a tricky problem which requires something new.

=== Catalog page (statement + literature review) ===
Friendly partitions — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 DeVos's question (equivalent to the internal-partition conjecture for $r$-regular graphs) remains open in full generality. Ban and Linial (2013) proved the conjecture for $r=6$ and exhibited new families of regular graphs without internal partitions; the cubic and 4-regular cases were already essentially known. The 5-regular case is still open as a deterministic statement, but Bärnkopf, Nagy and Paulovics (2024) settled it for 5-regular abelian Cayley graphs, and Csóka, Fekete, Nagy and Szemerédi (2025) showed that random 5-regular graphs a.a.s. admit an internal partition.

 Cited literature (4)

 
 
 
partial Internal Partitions of Regular Graphs
 (2013)
 

 
 Amir Ban, Nati Linial · arXiv preprint (later J. Graph Theory) · arXiv:1307.5246

Proves the internal/friendly partition conjecture for $r=6$ (all but finitely many 6-regular graphs have an internal partition), gives improved lower bounds on the threshold $N(d)$, and constructs new families of $d$-regular graphs without internal partitions, including $2k$-regular examples on $3k+2$ vertices.
 

 
 
partial A note on internal partitions: the 5-regular case and beyond
 (2021)
 

 
 Pál Bärnkopf, Zoltán Lóránt Nagy, Zoltán Paulovics · arXiv preprint (Graphs and Combinatorics, 2024) · arXiv:2109.14421 · doi:10.1007/s00373-024-02774-9

Studies the still-open 5-regular case, classifies all 5-regular abelian Cayley graphs without an internal partition, and obtains structural results on subgraphs of minimum degree 3 inside 5-regular graphs.
 

 
 
partial Bisection width, max-cut and internal partitions of 5-regular graphs
 (2025)
 

 
 Endre Csóka, Panna Tímea Fekete, Zoltán Lóránt Nagy, Levente Szemerédi · arXiv preprint · arXiv:2509.08531

Using a local-algorithm based factor with a recoloring phase, proves that random 5-regular graphs asymptotically almost surely admit an internal (friendly) partition, and derives new upper bounds on bisection width and max-cut of random $d$-regular graphs for $d>4$.
 

 
 
partial Majority Dynamics and Internal Partitions of Random Regular Graphs: Experimental Results
 (2024)
 

 
 Pavel Arkhipov · arXiv preprint · arXiv:2406.07026

Investigates majority dynamics on random odd-regular graphs as a heuristic for producing internal partitions, shows the standard dynamics fails to yield parts with the required $\lceil d/2\rceil$-cores, and proposes a modified dynamics that does so with high probability.
 

 

 Reviewer notes. DeVos's 'friendly partition' problem is exactly the internal-partition conjecture studied in the literature (vertex partition into two nonempty parts where every vertex has at least as many neighbours in its own part as in the other). The cases $r\in\{3,4\}$ are folklore/easy (cubic case reduces to two disjoint cycles, excluding $K_4$ and $K_{3,3}$). The Ban-Linial paper resolves $r=6$; $r=5$ and all $r\geq 7$ remain open in the deterministic sense, with progress only for random graphs and special families (Cayley graphs). The DOI 10.1007/s00373-024-02774-9 for the Graphs and Combinatorics version was found via search but the Springer page required authentication; the arXiv abstract page was verified directly.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Problem. Is it true that for every $ r $ , all but finitely many $ r $ -regular graphs have friendly partitions?

Keywords:
edge-cut · partition · regular

Discussion

Let me say at the start, that I (M. DeVos) suspect this problem has been considered previously, so I await a more correct attribution. An unfriendly partition of a graph is a partition of the vertices into two sets so that every vertex has at least as many neighbours in the opposite class as its own. It is an easy fact that every (finite) graph has an unfriendly partition; for instance, any maximum size edge-cut gives a partition with this property. Finding friendly partitions appears to be considerably more difficult. Perhaps one reason why is that there exist graphs without unfriendly partitions. For instance, $ K_{2n} $ and $ K_{2n+1,2n+1} $ have no unfriendly partitions. However, it appears possible that the only graphs which fail to have friendly partitions are fairly dense. When $ r=3 $ , the above problem is fairly easy to solve, as it reduces to the problem of finding two vertex disjoint cycles. Every cubic graph other than $ K_4 $ or $ K_{3,3} $ has two disjoint cycles, and thus has a friendly partition. The case when $ r=4 $ is also not terribly complicated. However, the next step up, $ r=5 $ looks like a tricky problem which requires something new.

Related conjectures

 
 related to
 Unfriendly partitions
 partial
 Dual notions in disjoint settings with no logical link. Friendly partitions (DeVos) asks whether all but finitely many finite r-regular graphs admit a partition where every vertex has at least as many neighbours in its own class; the unfriendly-partition problem (Cowan-Emerson) asks whether every countably infinite graph has a partition where every vertex has at least as many neighbours in the other class. The source page mentions unfriendly partitions only as contrast/motivation ('every finite graph has an unfriendly partition ... finding friendly partitions appears to be considerably more difficult'). One statement is about finite regular graphs with the 'friendly' inequality, the other about countably infinite graphs with the opposite inequality; truth of either has no bearing on the other. Thematically linked, no implication: related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
