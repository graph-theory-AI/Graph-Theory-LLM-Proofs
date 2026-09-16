Attack the following open graph-theory problem.

Catalog id: the_crossing_number_of_the_complete_graph
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_crossing_number_of_the_complete_graph/
Original entry: http://www.openproblemgarden.org/op/the_crossing_number_of_the_complete_graph

=== Problem statement (OpenProblemGarden) ===
Title: The Crossing Number of the Complete Graph
The crossing number $ cr(G) $ of $ G $ is the minimum number of crossings in all drawings of $ G $ in the plane. Conjecture $ \displaystyle cr(K_n) = \frac 14 \floor{\frac n2} \floor{\frac{n-1}2} \floor{\frac{n-2}2} \floor{\frac{n-3}2} $

=== Discussion / context (OpenProblemGarden) ===
(This discussion appears as [M].) A drawing of a graph $ G $ in the plane has the vertices represented by distinct points and the edges represented by polygonal lines joining their endpoints such that: \item no edge contains a vertex other than its endpoints, \item no two adjacent edges share a point other than their common endpoint, \item two nonadjacent edges share at most one point at which they cross transversally, and \item no three edges cross at the same point. The conjectured value for the crossing number of $ K_n $ is known to be an upper bound. This is shown by exhibiting a drawing with that number of crossings. If $ n = 2m $ , place $ m $ vertices regularly spaced along two circles of radii 1 and 2, respectively. Two vertices on the inner circle are connected by a straight line; two vertices on the outer circle are connected by a polygonal line outside the circle. A vertex on the inner circle is connected to one on the outer circle with a polygonal line segment of minimum possible positive winding angle around the cylinder. A simple count shows that the number of crossings in such a drawing achieves the conjectured minimum. For $ n = 2m-1 $ we delete one vertex from the drawing described and achieve the conjectured minimum. The conjecture is known to be true for $ n $ at most 10 [G]. If the conjecture is true for $ n = 2m $ , then it is also true for $ n-1 $ . This follows from an argument counting the number of crossings in drawings of all $ K_{n-1} $ 's contained in an optimal drawing of $ K_n $ . It would also be interesting to prove that the conjectured upper bound is asymptotically correct, that is, that $ \lim \frac{cr(K_n)}{\binom{n}4} = \frac38 $ . The best known lower bound is due to Kleitman [K], who showed that this limit is at least $ 3/10 $ .

=== References listed by OpenProblemGarden ===
- [G] R. Guy, The decline and fall of Zarankiewicz's theorem, in Proof Techniques in Graph Theory (F. Harary Ed.), Academic Press, New York (1969) 63-69.
- [K] D. Kleitman, The crossing number of , J. Combin. Theory 9 (1970) 315-323.
- [M] B. Mohar, Problem of the Month

=== Catalog page (statement + literature review) ===
The Crossing Number of the Complete Graph — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Hill's conjecture that $\mathrm{cr}(K_n) = \frac{1}{4}\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor\lfloor(n-2)/2\rfloor\lfloor(n-3)/2\rfloor$ remains open in general. Since 2007, the conjecture has been proved for all 2-page, cylindrical, and shellable drawings by Ábrego et al., and Balogh, Lidický, and Salazar established via flag algebras that $\mathrm{cr}(K_n) > 0.985\,H(n)$ for all sufficiently large $n$, substantially improving the previously known $0.83\,H(n)$ lower bound. The exact value of $\mathrm{cr}(K_{13})$ remains unknown, narrowed to $\{219, 221, 223, 225\}$.

 Cited literature (5)

 
 
 
partial The 2-page crossing number of $K_n$
 (2012)
 

 
 Bernardo M. Abrego, Oswin Aichholzer, Silvia Fernandez-Merchant, Pedro Ramos, Gelasio Salazar · arXiv preprint · arXiv:1206.5669

Proves that the 2-page crossing number of $K_n$ equals $Z(n)$, confirming Hill's conjecture for the 2-page drawing model.
 

 
 
partial Shellable drawings and the cylindrical crossing number of $K_n$
 (2013)
 

 
 Bernardo M. Ábrego, Oswin Aichholzer, Silvia Fernández-Merchant, Pedro Ramos, Gelasio Salazar · arXiv preprint · arXiv:1309.3665

Proves the Harary-Hill conjecture for all shellable drawings (including cylindrical, x-bounded, monotone, and 2-page drawings), settling the conjecture for these drawing classes.
 

 
 
partial On the crossing number of $K_{13}$
 (2013)
 

 
 Dan McQuillan, Shengjun Pan, R. Bruce Richter · arXiv preprint · arXiv:1307.3297

Rules out $\mathrm{cr}(K_{13}) = 217$, narrowing the possible values to $\{219, 221, 223, 225\}$ and advancing the verification program toward $n = 13$.
 

 
 
partial Closing in on Hill's conjecture
 (2017)
 

 
 József Balogh, Bernard Lidický, Gelasio Salazar · arXiv preprint · arXiv:1711.08958

Using flag algebras, proves that $\mathrm{cr}(K_n) > 0.985\,H(n)$ for all sufficiently large $n$, substantially improving the prior best asymptotic lower bound of $0.83\,H(n)$.
 

 
 
survey On a conjecture by Anthony Hill
 (2020)
 

 
 Bojan Mohar · arXiv preprint · arXiv:2009.03418

Provides a very general construction (including random configurations on a sphere) showing that many distinct drawing families achieve the Hill upper bound $H(n)$, without establishing it as a lower bound.
 

 

 Reviewer notes. The Pan-Richter 2007 paper 'The crossing number of K11 is 100' (J. Graph Theory 56(2):128-134), which extends the verified range to n <= 12, could not be cited because neither the Wiley nor ResearchGate page was accessible (HTTP 403). The OPG posting (2007-05-11) states only n <= 10 was known, suggesting Pan-Richter appeared around the same time or just after. The 'Closing in on Hill's conjecture' paper was published in SIAM J. Discrete Math. 2019 (DOI 10.1137/17M1158859) but is cited here via its verified arXiv preprint. The problem remains fully open for general n >= 13.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. $ \displaystyle cr(K_n) = \frac 14 \floor{\frac n2} \floor{\frac{n-1}2} \floor{\frac{n-2}2} \floor{\frac{n-3}2} $

Keywords:
complete graph · crossing number

Discussion

(This discussion appears as [M].) A drawing of a graph $ G $ in the plane has the vertices represented by distinct points and the edges represented by polygonal lines joining their endpoints such that: \item no edge contains a vertex other than its endpoints, \item no two adjacent edges share a point other than their common endpoint, \item two nonadjacent edges share at most one point at which they cross transversally, and \item no three edges cross at the same point. The conjectured value for the crossing number of $ K_n $ is known to be an upper bound. This is shown by exhibiting a drawing with that number of crossings. If $ n = 2m $ , place $ m $ vertices regularly spaced along two circles of radii 1 and 2, respectively. Two vertices on the inner circle are connected by a straight line; two vertices on the outer circle are connected by a polygonal line outside the circle. A vertex on the inner circle is connected to one on the outer circle with a polygonal line segment of minimum possible positive winding angle around the cylinder. A simple count shows that the number of crossings in such a drawing achieves the conjectured minimum. For $ n = 2m-1 $ we delete one vertex from the drawing described and achieve the conjectured minimum. The conjecture is known to be true for $ n $ at most 10 [G]. If the conjecture is true for $ n = 2m $ , then it is also true for $ n-1 $ . This follows from an argument counting the number of crossings in drawings of all $ K_{n-1} $ 's contained in an optimal drawing of $ K_n $ . It would also be interesting to prove that the conjectured upper bound is asymptotically correct, that is, that $ \lim \frac{cr(K_n)}{\binom{n}4} = \frac38 $ . The best known lower bound is due to Kleitman [K], who showed that this limit is at least $ 3/10 $ .

Bibliography

 [G]
 R. Guy, The decline and fall of Zarankiewicz's theorem, in Proof Techniques in Graph Theory (F. Harary Ed.), Academic Press, New York (1969) 63-69.

 [K]
 D. Kleitman, The crossing number of $ K_{5,n} $ , J. Combin. Theory 9 (1970) 315-323.

 [M]
 B. Mohar, Problem of the Month
 Problem of the Month

Related conjectures

 
 implied by
 Crossing number of Kₙ minus t-matching
 open
 The full text of arXiv:2009.03418 (Conjecture 5) states cr(M_{n,t}) = H(n) - (1/2)t(k-1)(k-2) for n >= 5 and 0 <= t <= n/2, explicitly including t = 0. Since M_{n,0} = K_n and the correction term vanishes at t = 0, the conjecture's t = 0 instance reads cr(K_n) = H(n), which is exactly the Harary-Hill conjecture (the cases n < 5 are trivially known, cr = 0). So truth of the M_{n,t} conjecture for all admissible (n,t) forces the Harary-Hill value for all n: a clean instance-restriction implication in the claimed direction.
 

 
 related to
 Drawing disconnected graphs on surfaces
 partial
 The mention is purely definitional: the source page says 'We insist on the usual restrictions for drawings (as in The Crossing Number of the Complete Graph)', importing the standard good-drawing conditions and nothing more. There is no logical dependence: the truth of the exact formula for cr(K_n) in the plane neither forces nor follows from the statement that optimal drawings of a disconnected graph on an arbitrary surface keep the components disjoint (the latter is about arbitrary graphs G_1, G_2 and arbitrary surfaces, the former about one specific family in the plane). They share only the theme of crossing-minimal drawings.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
