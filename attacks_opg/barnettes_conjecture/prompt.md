Attack the following open graph-theory problem.

Catalog id: barnettes_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/barnettes_conjecture/
Original entry: http://www.openproblemgarden.org/op/barnettes_conjecture
Problem attributed to: Barnette, David W. (posted 2007-06-12)

=== Problem statement (OpenProblemGarden) ===
Title: Barnette's Conjecture
Conjecture Every 3-connected cubic planar bipartite graph is Hamiltonian.

=== Discussion / context (OpenProblemGarden) ===
(Originally appeared in [B], this discussion appears as [M].) \item It is known that this is not true if you remove the "bipartite" condition, but the smallest 3-connected cubic planar graph which is not Hamiltonian has 38 vertices. \item Holton, Manvel, and McKay [HMM] proved (using computers) that all graphs having fewer than 66 vertices satisfy the conjecture. \item [A communication by Robert Aldred, Gunnar Brinkmann, and Brendan McKay (December 2002):] A paper of Holton, Manvel and McKay [HMM] proved Barnette's conjecture for up to 64 vertices, inclusive. This is to announce that the conjecture remains true up to 84 vertices, inclusive. The method used was the same as in the 1985 paper, but took advantage of two developments. One was the new program plantri (Brinkmann and McKay, to be published) which can generate the required graphs without isomorphs at more than $ 100\,000 $ per second. The other was the advance in computers. Total cpu time was about 3 years, almost all of it taken in finding hamiltonian cycles. Specifically, for all 3-connected cubic planar bipartite graphs up to 60 vertices, and those up to 64 vertices not having a 4-face adjacent to two others, we found a hamiltonian cycle using $ x $ and avoiding $ y $ for each pair of edges $ x $ and $ y $ . There are over $ 10^{10} $ such graphs. By a theorem of Kelman's, one can build a counterexample to Barnette's conjecture when one has a 3-connected cubic planar bipartite graph with this property: for some two edges $ x $ and $ y $ on the same face, there is no hamiltonian cycle that uses $ x $ and avoids $ y $ . We did not find any such graph even where $ x $ and $ y $ are not required to be on the same face. Perhaps the path to finding a counterexample is to strengthen Kelman's method to some more complicated condition involving 3 or more edges, as then it is more likely to fail on a smaller size. There is another conjecture of Barnette (checked by Brendan McKay and Gunnar Brinkmann up to 250 vertices). Conjecture Every planar cubic 3-connected graph with faces only of sizes 3, 4, 5, and 6 is Hamiltonian.

=== References listed by OpenProblemGarden ===
- *[B] David W. Barnette, Conjecture 5, Recent progress in combinatorics (ed. W. T. Tutte), Academic Press, New York (1969) 343, MathSciNet
- [HMM] Derek A.Holton, Bennet Manvel, Brendan D. McKay, Hamiltonian cycles in cubic 3-connected bipartite planar graphs, J. Combin. Theory Ser. B 38 (1985) 279-297. MathSciNet
- [M] B. Mohar, Problem of the Month

=== Catalog page (statement + literature review) ===
Barnette's Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Barnette's conjecture—that every 3-connected cubic planar bipartite graph is Hamiltonian—remains open. Since the OPG posting date, several partial results have been established: Bagheri et al. (2021) proved Hamiltonicity for the leapfrog extension of any cyclically 4-edge-connected bipartite cubic planar graph; Gorsky et al. (2022) reformulated the conjecture via matching theory, reducing it to cubic planar braces; Florek (2023) found a sufficient neighborhood condition on big faces; Schnieders (2025) proved every Barnette graph with all faces of size at most 8 is Hamiltonian; and Bekos et al. (2025) showed every $n$-vertex Barnette graph contains a subhamiltonian cycle using at least $5n/6$ edges.

 Cited literature (5)

 
 
 
partial Hamiltonian cycles in planar cubic graphs with facial 2‐factors, and a new partial solution of Barnette's Conjecture
 (2021)
 

 
 Behrooz Bagheri Gh, Tomas Feder, Herbert Fleischner, Carlos Subi · Journal of Graph Theory · doi:10.1002/jgt.22612

Proves that the leapfrog extension of any cyclically 4-edge-connected bipartite cubic planar graph is Hamiltonian, extending Goodey's earlier result and providing new best partial solutions to Barnette's conjecture.
 

 
 
reduction Matching Theory and Barnette's Conjecture
 (2022)
 

 
 Maximilian Gorsky, Raphael Steiner, Sebastian Wiederrecht · arXiv preprint · arXiv:2202.11641

Translates Barnette's conjecture into matching-theoretic terms and reduces it to the equivalent statement that all cubic 3-connected planar bipartite braces are Hamiltonian, relaxing planarity to Pfaffianness for a broader reformulation.
 

 
 
partial A sufficient condition for cubic 3-connected plane bipartite graphs to be hamiltonian
 (2023)
 

 
 Jan Florek · arXiv preprint · arXiv:2309.09578

Proves Hamiltonicity when no face has more than four neighboring big faces (faces with at least 6 edges), and shows such graphs contain exponentially many Hamilton cycles; extends Goodey's result.
 

 
 
partial Barnette Graphs with Faces up to Size 8 are Hamiltonian
 (2025)
 

 
 Tobias Schnieders · arXiv preprint · arXiv:2508.03531

Proves that every cubic bipartite planar 3-connected graph whose faces all have size at most 8 is Hamiltonian, substantially strengthening Goodey's classical result (faces of size at most 6).
 

 
 
partial Approximating Barnette's Conjecture
 (2025)
 

 
 Michael A. Bekos, Michael Kaufmann, Maximilian Pfister · 33rd International Symposium on Graph Drawing and Network Visualization (GD 2025), LIPIcs · doi:10.4230/LIPIcs.GD.2025.6

Shows every $n$-vertex Barnette graph admits a subhamiltonian cycle containing at least $5n/6$ edges, improving the previously known bound of $2n/3$.
 

 

 Reviewer notes. The ScienceDirect page for Florek (2010) 'On Barnette's conjecture' (Discrete Mathematics) returned HTTP 403 and could not be verified; it was excluded despite being post-2007. The arXiv PDF for Gorsky et al. (2202.11641) returned binary data; the abstract page was used instead. No journal publication venue for Gorsky et al. could be confirmed. The Wikipedia article also mentions Alt et al. (2016) as establishing partial results via dual-graph coloring conditions, but this paper was not independently verified via WebFetch and is therefore excluded. The related Barnette conjecture about faces of sizes 3–6 was fully proved by Kardoš (2020), but that is a distinct conjecture.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 1315s.
 

Conjecture. Every 3-connected cubic planar bipartite graph is Hamiltonian.

Keywords:
bipartite · cubic · hamiltonian

Discussion

(Originally appeared in [B], this discussion appears as [M].) \item It is known that this is not true if you remove the "bipartite" condition, but the smallest 3-connected cubic planar graph which is not Hamiltonian has 38 vertices. \item Holton, Manvel, and McKay [HMM] proved (using computers) that all graphs having fewer than 66 vertices satisfy the conjecture. \item [A communication by Robert Aldred, Gunnar Brinkmann, and Brendan McKay (December 2002):] A paper of Holton, Manvel and McKay [HMM] proved Barnette's conjecture for up to 64 vertices, inclusive. This is to announce that the conjecture remains true up to 84 vertices, inclusive. The method used was the same as in the 1985 paper, but took advantage of two developments. One was the new program plantri (Brinkmann and McKay, to be published) which can generate the required graphs without isomorphs at more than $ 100\,000 $ per second. The other was the advance in computers. Total cpu time was about 3 years, almost all of it taken in finding hamiltonian cycles. Specifically, for all 3-connected cubic planar bipartite graphs up to 60 vertices, and those up to 64 vertices not having a 4-face adjacent to two others, we found a hamiltonian cycle using $ x $ and avoiding $ y $ for each pair of edges $ x $ and $ y $ . There are over $ 10^{10} $ such graphs. By a theorem of Kelman's, one can build a counterexample to Barnette's conjecture when one has a 3-connected cubic planar bipartite graph with this property: for some two edges $ x $ and $ y $ on the same face, there is no hamiltonian cycle that uses $ x $ and avoids $ y $ . We did not find any such graph even where $ x $ and $ y $ are not required to be on the same face. Perhaps the path to finding a counterexample is to strengthen Kelman's method to some more complicated condition involving 3 or more edges, as then it is more likely to fail on a smaller size. There is another conjecture of Barnette (checked by Brendan McKay and Gunnar Brinkmann up to 250 vertices). Conjecture Every planar cubic 3-connected graph with faces only of sizes 3, 4, 5, and 6 is Hamiltonian.

Bibliography

★ [B]
 David W. Barnette, Conjecture 5, Recent progress in combinatorics (ed. W. T. Tutte), Academic Press, New York (1969) 343, MathSciNet
 MathSciNet

 [HMM]
 Derek A.Holton, Bennet Manvel, Brendan D. McKay, Hamiltonian cycles in cubic 3-connected bipartite planar graphs, J. Combin. Theory Ser. B 38 (1985) 279-297. MathSciNet
 MathSciNet

 [M]
 B. Mohar, Problem of the Month
 Problem of the Month
