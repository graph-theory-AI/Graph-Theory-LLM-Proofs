Attack the following open graph-theory problem.

Catalog id: real_roots_of_the_flow_polynomial
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/real_roots_of_the_flow_polynomial/
Original entry: http://www.openproblemgarden.org/op/real_roots_of_the_flow_polynomial
Problem attributed to: Welsh, Dominic J. A. (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Real roots of the flow polynomial
Conjecture All real roots of nonzero flow polynomials are at most 4.

=== Discussion / context (OpenProblemGarden) ===
For every graph $ G $ , let $ P_G $ be the chromatic polynomial of $ G $ and let $ Q_G $ be the flow polynomial of $ G $ . If $ G $ is loopless, then $ P_G(k)>0 $ for all sufficiently large integers $ k $ (as $ P_G(k) $ = # of k-colorings of $ G $ ). It follows from Seymour's 6-flow theorem that if $ G $ has no bridge , then $ Q_G(k)>0 $ for all integers $ k>5 $ (as $ Q_G(k) $ = # of nowhere-zero flows in the group of integers modulo $ k $ ). It is natural to ask if all real roots of these polynomials are small. For the chromatic polynomial, $ P_G $ , this is not the case. There exist graphs with chromatic number 3 for which $ P_G $ has arbitrarily large real roots. The above conjecture asserts that the flow polynomial exhibits the opposite behavior. One word of caution, it is known that the set of roots of flow polynomials is dense in the complex plane.

=== References listed by OpenProblemGarden ===
- [S] P.D. Seymour, Nowhere-Zero 6-Flows, J. Combinatorial Theory Ser. B 30 (1981) 130-135. MathSciNet

=== Catalog page (statement + literature review) ===
Real roots of the flow polynomial — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 Welsh's conjecture that all real roots of nonzero flow polynomials are at most $4$ has been disproved: Haggard, Pearce, and Royle found bridgeless graphs whose flow polynomials have real roots exceeding $4$. Subsequently, Jacobsen and Salas proved that real flow roots can even exceed $5$, finding that the generalized Petersen graph $G(119,7)$ has real flow roots at $Q \approx 5.0000198$ and $Q \approx 5.1653$, raising the question of whether real flow roots are bounded above at all.

 Cited literature (2)

 
 
 
counterexample Is the five-flow conjecture almost false?
 (2013)
 

 
 Jesper L. Jacobsen, Jesus Salas · Journal of Combinatorial Theory, Series B · arXiv:1009.4062

Exhibits infinitely many real flow roots exceeding 5 within generalized Petersen graphs G(nk,k), disproving the relaxed Welsh conjecture (bound 5) and showing the original bound-of-4 conjecture was far from tight.
 

 
 
survey A survey on the study of real zeros of flow polynomials
 (2019)
 

 
 Fengming Dong · Journal of Graph Theory · arXiv:2007.05195 · doi:10.1002/jgt.22458

Surveys results on real zeros of flow polynomials, including the disproof of Welsh's conjecture and subsequent developments on zero-free intervals.
 

 

 Reviewer notes. The Haggard-Pearce-Royle paper that first disproved the original Welsh conjecture (bound of 4) could not be located and independently verified by WebFetch; its existence is confirmed by citation in the Jacobsen-Salas arXiv paper and in Gordon Royle's 2010 blog post (symomega). The Dong survey has an unusual timeline: journal publication December 2019 preceded the arXiv posting of July 2020. The supremum of real flow roots of flow polynomials is unknown and remains an open problem.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. All real roots of nonzero flow polynomials are at most 4.

Keywords:
flow polynomial · nowhere-zero flow

Discussion

For every graph $ G $ , let $ P_G $ be the chromatic polynomial of $ G $ and let $ Q_G $ be the flow polynomial of $ G $ . If $ G $ is loopless, then $ P_G(k)>0 $ for all sufficiently large integers $ k $ (as $ P_G(k) $ = # of k-colorings of $ G $ ). It follows from Seymour's 6-flow theorem that if $ G $ has no bridge , then $ Q_G(k)>0 $ for all integers $ k>5 $ (as $ Q_G(k) $ = # of nowhere-zero flows in the group of integers modulo $ k $ ). It is natural to ask if all real roots of these polynomials are small. For the chromatic polynomial, $ P_G $ , this is not the case. There exist graphs with chromatic number 3 for which $ P_G $ has arbitrarily large real roots. The above conjecture asserts that the flow polynomial exhibits the opposite behavior. One word of caution, it is known that the set of roots of flow polynomials is dense in the complex plane.

Bibliography

 [S]
 P.D. Seymour, Nowhere-Zero 6-Flows, J. Combinatorial Theory Ser. B 30 (1981) 130-135. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 5-flow conjecture
 partial
 For a bridgeless graph G the flow polynomial is monic of degree |E|-|V|+c (only the full edge set attains the maximum nullity when there are no bridges), so it is a nonzero polynomial that is positive for large t; alternatively Phi(G,6)>0 by Seymour's 6-flow theorem. If all its real roots are at most 4, it cannot change sign on (4,infinity), hence Phi(G,5)>0. Phi(G,5) counts nowhere-zero Z5-flows, and by Tutte a nowhere-zero Z5-flow exists iff a nowhere-zero integer 5-flow exists. Thus every bridgeless graph would have a nowhere-zero 5-flow. Self-contained; direction correct (root bound is the stronger statement).
 

 
 implies
 Half-integral flow polynomial values
 open
 Same sign argument at the non-integer point 5.5. For a 2-edge-connected (hence bridgeless) graph G, the flow polynomial Phi(G,t) is nonzero and positive for large t (it is monic of degree |E|-|V|+c; alternatively Phi(G,6)>0 by Seymour's 6-flow theorem). If Phi has no real root greater than 4, it cannot change sign on (4,infinity), so Phi(G,5.5)>0, which is exactly the target conjecture. Self-contained; direction correct.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
