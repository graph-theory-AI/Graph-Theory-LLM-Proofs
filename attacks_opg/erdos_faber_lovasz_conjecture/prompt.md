Attack the following open graph-theory problem.

Catalog id: erdos_faber_lovasz_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/erdos_faber_lovasz_conjecture/
Original entry: http://www.openproblemgarden.org/op/erdos_faber_lovasz_conjecture
Problem attributed to: Erdos, Paul, Faber, Vance, Lovasz, Laszlo (posted 2013-08-22)

=== Problem statement (OpenProblemGarden) ===
Title: Erdős–Faber–Lovász conjecture
Conjecture If $ G $ is a simple graph which is the union of $ k $ pairwise edge-disjoint complete graphs, each of which has $ k $ vertices, then the chromatic number of $ G $ is $ k $ .

=== Discussion / context (OpenProblemGarden) ===
From [Erd81]: "Faber, Lovász and I made this harmless looking conjecture at a party in Boulder Colorado in September 1972. Its diffculty was realised only slowly. I now offer 500 dollars for a proof or disproof. (Not long ago I only offered 50; the increase is not due to inflation but to the fact that I now think the problem is very diffcult. Perhaps I am wrong.)" The conjecture can be equivalently formulated in terms of seating assignments or hypergraph colouring; see Wikipedia or Doug West's Webpage .

=== References listed by OpenProblemGarden ===
- [Erd81] P. Erdős. On the combinatorial problems which I would most like to see solved. Combinatorica, 1(1):25–42, 1981.

=== Catalog page (statement + literature review) ===
Erdős–Faber–Lovász conjecture — Graph-theory open problems

 Also at erdosproblems.com #19 (solved, fuzzy-match score 71)

 
 Status
 partial
 high confidence
 

 Kang, Kelly, Kühn, Methuku, and Osthus proved the conjecture for all sufficiently large $k$ in a landmark paper published in the Annals of Mathematics (2023), settling the problem asymptotically after 50 years. For small values of $k$, the conjecture remains open; SAT-based methods (Kirchweger, Peitl, Szeider, 2023) have extended computational verification to further finite cases but do not cover all remaining instances.

 Cited literature (5)

 
 
 
partial A proof of the Erdős-Faber-Lovász conjecture
 (2023)
 

 
 Dong Yeap Kang, Tom Kelly, Daniela Kühn, Abhishek Methuku, Deryk Osthus · Annals of Mathematics · arXiv:2101.04698

Proves the Erdős–Faber–Lovász conjecture for every sufficiently large $k$, and establishes stability versions confirming a prediction of Kahn; preprint posted January 2021, published Annals of Mathematics 198(2), 537–618 (2023).
 

 
 
partial A SAT Solver's Opinion on the Erdős-Faber-Lovász Conjecture
 (2023)
 

 
 Markus Kirchweger, Tomáš Peitl, Stefan Szeider · Proceedings of SAT 2023 (LIPIcs) · doi:10.4230/LIPIcs.SAT.2023.13

Uses SAT solvers to verify the conjecture for small linear hypergraphs not covered by the Kang et al. large-$k$ proof, generating independently checkable DRAT certificates.
 

 
 
survey The Erdős-Faber-Lovász Conjecture: Fifty Exciting Years
 (2025)
 

 
 P. Mark Kayll · Mathematics Magazine · doi:10.1080/0025570X.2024.2419818

Surveys fifty years of progress on the conjecture, reviewing the Kang et al. proof for all sufficiently large $k$ and contextualising what remains open for small cases.
 

 
 
partial Longest cycles in vertex-transitive and highly connected graphs
 (2025)
 

 
 Carla Groenland, Sean Longbrake, Raphael Steiner, Jérémie Turcotte, Liana Yepremyan · arXiv preprint · arXiv:2408.04618

Shows that every connected vertex-transitive graph on $n\geq 3$ vertices contains a cycle (and hence a path) of length at least $\Omega(n^{13/21})$, improving the previous bound of $\Omega(n^{3/5})$ due to DeVos (2023).
 

 
 
partial Small hitting sets for longest paths and cycles
 (2025)
 

 
 Sergey Norin, Raphael Steiner, Stephan Thomassé, Paul Wollan · arXiv preprint · arXiv:2505.08634

Shows that every connected vertex-transitive graph of order $n$ contains a path of length $\Omega(n^{9/14})$, improving the previous best bound of $\Omega(n^{13/21})$.
 

 

 Reviewer notes. Despite its title, the Kang et al. Annals paper proves the conjecture only for all sufficiently large $k$, not for all $k$. The combination of this large-$k$ proof with the SAT-solver verification of small cases (Kirchweger et al.) has not yet been shown to cover every finite $k$; the 2025 Mathematics Magazine survey by Kayll explicitly confirms the full conjecture remains open. The Tandfonline page for the Kayll survey (doi 10.1080/0025570X.2024.2419818) returned HTTP 403; authorship, title, year, and venue were confirmed via the University of Montana research-impact page. The Annals DOI is omitted because it was not directly confirmed from the fetched page.

 
 Auto-reviewed 2026-05-07 with claude-sonnet-4-6 (web search enabled) · 169s.
 

Conjecture. If $ G $ is a simple graph which is the union of $ k $ pairwise edge-disjoint complete graphs, each of which has $ k $ vertices, then the chromatic number of $ G $ is $ k $ .

Keywords:
chromatic number

Discussion

From [Erd81]: "Faber, Lovász and I made this harmless looking conjecture at a party in Boulder Colorado in September 1972. Its diffculty was realised only slowly. I now offer 500 dollars for a proof or disproof. (Not long ago I only offered 50; the increase is not due to inflation but to the fact that I now think the problem is very diffcult. Perhaps I am wrong.)" The conjecture can be equivalently formulated in terms of seating assignments or hypergraph colouring; see Wikipedia or Doug West's Webpage .

Bibliography

 [Erd81]
 P. Erdős. On the combinatorial problems which I would most like to see solved. Combinatorica, 1(1):25–42, 1981.
