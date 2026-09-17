Attack the following open graph-theory problem.

Catalog id: monochromatic_reachability_vs_rainbow_triangles
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs » Tournaments
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/monochromatic_reachability_vs_rainbow_triangles/
Original entry: http://www.openproblemgarden.org/op/monochromatic_reachability_vs_rainbow_triangles
Problem attributed to: Sands, Bill, Sauer, Norbert W., Woodrow, Robert E. (posted 2008-07-15)

=== Problem statement (OpenProblemGarden) ===
Title: Monochromatic reachability or rainbow triangles
In an edge-colored digraph, we say that a subgraph is rainbow if all its edges have distinct colors, and monochromatic if all its edges have the same color. Problem Let $ G $ be a tournament with edges colored from a set of three colors. Is it true that $ G $ must have either a rainbow directed cycle of length three or a vertex $ v $ so that every other vertex can be reached from $ v $ by a monochromatic (directed) path?

=== Discussion / context (OpenProblemGarden) ===
This problem was raised in a paper by Sands, Sauer, and Woodrow [SSW] where they prove that every tournament with 2-colored edges has a vertex $ v $ so that every other vertex can be reached from $ v $ by a monochromatic path. Galeana-Sanchez and Rojas-Monroy found a tournament on 6 vertices with 4-colored edges which has no rainbow triangle and does not have a vertex $ v $ which has monochromatic paths to all remaining vertices. However, the following generalization of the above conjecture looks plausible. Problem Does every edge-colored tournament have either a rainbow directed cycle or a vertex $ v $ so that every other vertex can be reached from $ v $ by a monochromatic path?

=== References listed by OpenProblemGarden ===
- *[SSW] B. Sands, N. Sauer, R. Woodrow, On monochromatic paths in edge-coloured digraphs. J. Combin. Theory Ser. B 33 (1982), no. 3, 271--275. MathSciNet.

=== Catalog page (statement + literature review) ===
Monochromatic reachability or rainbow triangles — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture that every 3-edge-colored tournament has either a rainbow directed triangle or a vertex from which all others are reachable by a monochromatic path remains open. Georgakopoulos and Sprüssel (2009) established a partial case: the conclusion holds for every 3-edge-colored tournament in which no vertex is incident with all three colors. The generalized conjecture (arbitrary number of colors) is also open, with the 4-color case shown to be false by a counterexample that predates the OPG posting.

 Cited literature (1)

 
 
 
partial On 3-coloured tournaments
 (2009)
 

 
 Agelos Georgakopoulos, Philipp Sprüssel · arXiv preprint · arXiv:0904.1967

Proves that every 3-edge-colored tournament in which no vertex is incident with all three colors contains either a rainbow directed triangle or a vertex with monochromatic paths to all other vertices, establishing the conjecture under this additional assumption.
 

 

 Reviewer notes. The Douglas West problem page (dwest.web.illinois.edu/regs/msourcyc.html, citations through 2010) confirms the 3-color conjecture is still open. The Georgakopoulos-Sprüssel arXiv preprint notes their main result 'had appeared before' in another work, meaning the partial result under extra conditions may predate the OPG posting; nonetheless the paper itself is from 2009. The 'Monochromatic Sinks in k-Arc Colored Tournaments' (Springer 2015) and related journal papers could not be fully accessed due to paywalls and may contain further partial progress. No paper found that resolves the main conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Problem. Let $ G $ be a tournament with edges colored from a set of three colors. Is it true that $ G $ must have either a rainbow directed cycle of length three or a vertex $ v $ so that every other vertex can be reached from $ v $ by a monochromatic (directed) path?

Keywords:
digraph · edge-coloring · tournament

Discussion

This problem was raised in a paper by Sands, Sauer, and Woodrow [SSW] where they prove that every tournament with 2-colored edges has a vertex $ v $ so that every other vertex can be reached from $ v $ by a monochromatic path. Galeana-Sanchez and Rojas-Monroy found a tournament on 6 vertices with 4-colored edges which has no rainbow triangle and does not have a vertex $ v $ which has monochromatic paths to all remaining vertices. However, the following generalization of the above conjecture looks plausible. Problem Does every edge-colored tournament have either a rainbow directed cycle or a vertex $ v $ so that every other vertex can be reached from $ v $ by a monochromatic path?

Bibliography

★ [SSW]
 B. Sands, N. Sauer, R. Woodrow, On monochromatic paths in edge-coloured digraphs . J. Combin. Theory Ser. B 33 (1982), no. 3, 271--275. MathSciNet .
 On monochromatic paths in edge-coloured digraphs · MathSciNet
