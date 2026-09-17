Attack the following open graph-theory problem.

Catalog id: the_crossing_number_of_the_complete_bipartite_graph
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_crossing_number_of_the_complete_bipartite_graph/
Original entry: http://www.openproblemgarden.org/op/the_crossing_number_of_the_complete_bipartite_graph
Problem attributed to: Turan, Paul (posted 2007-05-11)

=== Problem statement (OpenProblemGarden) ===
Title: The Crossing Number of the Complete Bipartite Graph
The crossing number $ cr(G) $ of $ G $ is the minimum number of crossings in all drawings of $ G $ in the plane. Conjecture $ \displaystyle cr(K_{m,n}) = \floor{\frac m2} \floor{\frac {m-1}2} \floor{\frac n2} \floor{\frac {n-1}2} $

=== Discussion / context (OpenProblemGarden) ===
(This discussion appears as [M].) A drawing of a graph $ G $ in the plane has the vertices represented by distinct points and the edges represented by polygonal lines joining their endpoints such that: \item no edge contains a vertex other than its endpoints, \item no two adjacent edges share a point other than their common endpoint, \item two nonadjacent edges share at most one point at which they cross transversally, and \item no three edges cross at the same point. This problem is also known as Turan's Brickyard Problem (since it was formulated by Turan when he was working at a brickyard - the edges of the drawing would correspond to train tracks connecting different shipping depots, and fewer crossings would mean smaller chance for collision of little trains and smaller chance for their derailing). This conjectured value for the crossing number of $ K_{m,n} $ can be realized by the following drawing. Place $ \ceil{n/2} $ vertices on the positive $ x $ -axis and $ \floor{n/2} $ vertices on the negative $ x $ -axis. Similarly, place $ \ceil{m/2} $ and $ \floor{m/2} $ along the positive and negative $ y $ -axis. Now connect each pair of vertices on different axes with straight line segments.

=== References listed by OpenProblemGarden ===
- [G] R. Guy, The decline and fall of Zarankiewicz's theorem, in Proof Techniques in Graph Theory (F. Harary Ed.), Academic Press, New York (1969) 63-69.
- [K] D. Kleitman, The crossing number of K_{5,n} , J. Combin. Theory 9 (1970) 315-32
- [M] B. Mohar, Problem of the Month

=== Catalog page (statement + literature review) ===
The Crossing Number of the Complete Bipartite Graph — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Zarankiewicz conjecture that $\mathrm{cr}(K_{m,n}) = \lfloor m/2 \rfloor \lfloor (m-1)/2 \rfloor \lfloor n/2 \rfloor \lfloor (n-1)/2 \rfloor$ remains open in general; it has been verified for $\min\{m,n\} \le 6$ and a handful of small cases (up to $K_{8,10}$), with the best published asymptotic lower bound at $0.83\,Z(m,n)$ for fixed $m \ge 9$. Since the 2007 posting, Brosch and Polak (2023) have used semidefinite programming to establish new explicit lower bounds for $K_{m,n}$ with $m \in \{10,11,12,13\}$, extending the reach of SDP methods beyond what de Klerk et al. (2006) had achieved.

 Cited literature (2)

 
 
 
partial New lower bounds on crossing numbers of $K_{m,n}$ from semidefinite programming
 (2023)
 

 
 Daniel Brosch, Sven Polak · Mathematical Programming · arXiv:2206.02755 · doi:10.1007/s10107-023-02028-1

Establishes new lower bounds cr(K_{10,n}) >= 4.87057 n^2 - 10n, cr(K_{11,n}) >= 5.99939 n^2 - 12.5n, cr(K_{12,n}) >= 7.25579 n^2 - 15n, cr(K_{13,n}) >= 8.65675 n^2 - 18n via semidefinite programming with full symmetry exploitation.
 

 
 
partial Improved lower bounds for the 2-page crossing numbers of $K_{m,n}$ and $K_n$ via semidefinite programming
 (2012)
 

 
 Etienne de Klerk, Dmitrii V. Pasechnik · SIAM Journal on Optimization · arXiv:1110.4824

Shows that the Zarankiewicz conjecture holds asymptotically for the 2-page crossing number variant with m=7 and m=8 (i.e., lim_{n->inf} cr_2(K_{m,n})/Z(m,n) = 1), and improves bounds for the 2-page crossing number of K_n.
 

 

 Reviewer notes. Christian, Richter, and Salazar (J. Combin. Theory Ser. B, 103:237-247, 2013) proved a key finiteness result: for each fixed m there exists N_0(m) such that verifying the conjecture for all n <= N_0 implies it for all n; this paper was consistently referenced across multiple sources but no accessible URL was found for direct verification, so it is not included in since_posted. Norin and Zwols reportedly showed cr(K_{n,n}) >= 0.9118·Z(n,n) + o(n^4) using flag algebras (BIRS workshop, 2013), which would improve the 0.83 asymptotic bound; this result appears to be unpublished/conference-only and could not be verified via WebFetch. The 2-page crossing number result of de Klerk-Pasechnik concerns a restricted drawing model (vertices on a spine, edges on two half-planes) and is thus about a related but distinct conjecture. The arXiv paper 2605.01120 about 'Zarankiewicz numbers' addresses extremal bipartite graph theory (forbidden submatrix problem), not crossing numbers.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. $ \displaystyle cr(K_{m,n}) = \floor{\frac m2} \floor{\frac {m-1}2} \floor{\frac n2} \floor{\frac {n-1}2} $

Keywords:
complete bipartite graph · crossing number

Discussion

(This discussion appears as [M].) A drawing of a graph $ G $ in the plane has the vertices represented by distinct points and the edges represented by polygonal lines joining their endpoints such that: \item no edge contains a vertex other than its endpoints, \item no two adjacent edges share a point other than their common endpoint, \item two nonadjacent edges share at most one point at which they cross transversally, and \item no three edges cross at the same point. This problem is also known as Turan's Brickyard Problem (since it was formulated by Turan when he was working at a brickyard - the edges of the drawing would correspond to train tracks connecting different shipping depots, and fewer crossings would mean smaller chance for collision of little trains and smaller chance for their derailing). This conjectured value for the crossing number of $ K_{m,n} $ can be realized by the following drawing. Place $ \ceil{n/2} $ vertices on the positive $ x $ -axis and $ \floor{n/2} $ vertices on the negative $ x $ -axis. Similarly, place $ \ceil{m/2} $ and $ \floor{m/2} $ along the positive and negative $ y $ -axis. Now connect each pair of vertices on different axes with straight line segments.

Bibliography

 [G]
 R. Guy, The decline and fall of Zarankiewicz's theorem, in Proof Techniques in Graph Theory (F. Harary Ed.), Academic Press, New York (1969) 63-69.

 [K]
 D. Kleitman, The crossing number of K_{5,n} , J. Combin. Theory 9 (1970) 315-32

 [M]
 B. Mohar, Problem of the Month
 Problem of the Month
