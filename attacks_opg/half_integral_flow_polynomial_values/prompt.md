Attack the following open graph-theory problem.

Catalog id: half_integral_flow_polynomial_values
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Algebraic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/half_integral_flow_polynomial_values/
Original entry: http://www.openproblemgarden.org/op/half_integral_flow_polynomial_values
Problem attributed to: Mohar, Bojan (posted 2007-05-31)

=== Problem statement (OpenProblemGarden) ===
Title: Half-integral flow polynomial values
Let $ \Phi(G,x) $ be the flow polynomial of a graph $ G $ . So for every positive integer $ k $ , the value $ \Phi(G,k) $ equals the number of nowhere-zero $ k $ -flows in $ G $ . Conjecture $ \Phi(G,5.5) > 0 $ for every 2-edge-connected graph $ G $ .

=== Discussion / context (OpenProblemGarden) ===
By Seymour's 6-flow theorem, $ \Phi(G,k) > 0 $ for every 2-edge-connected graph $ G $ and every integer $ k\ge6 $ . It would be interesting to find any non-integer rational number $ x>5 $ so that $ \Phi(G,x) > 0 $ for every 2-edge-connected graph $ G $ . It is known that zeros of flow polynomials are dense in the complex plane.

=== Catalog page (statement + literature review) ===
Half-integral flow polynomial values — Graph-theory open problems

 
 Status
 open
 low confidence
 

 Mohar's conjecture that $\Phi(G, 5.5) > 0$ for every 2-edge-connected graph $G$ appears to remain open. No post-2007 paper resolving the conjecture—either by proving it or finding a counterexample—was found across multiple literature searches. The problem asks for a non-integer rational $x > 5$ with this positivity property, going beyond Seymour's 6-flow theorem which only gives $\Phi(G,k) > 0$ for integer $k \geq 6$.

 Reviewer notes. The canonical OPG page (both openproblemgarden.org and garden.irmacs.sfu.ca) was inaccessible (ECONNREFUSED). The survey arXiv:2007.05195 ('A survey on the study of real zeros of flow polynomials', 2020) is likely the most relevant post-2007 work but its full content was not retrievable to check for discussion of this specific conjecture. The ScienceDirect page for a note on flow polynomials (S0012365X08000721) returned HTTP 403. No paper was found that either proves or disproves the conjecture at x = 5.5. Confidence is low due to inability to access the full text of the most relevant survey.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. $ \Phi(G,5.5) > 0 $ for every 2-edge-connected graph $ G $ .

Keywords:
nowhere-zero flow

Discussion

By Seymour's 6-flow theorem, $ \Phi(G,k) > 0 $ for every 2-edge-connected graph $ G $ and every integer $ k\ge6 $ . It would be interesting to find any non-integer rational number $ x>5 $ so that $ \Phi(G,x) > 0 $ for every 2-edge-connected graph $ G $ . It is known that zeros of flow polynomials are dense in the complex plane.

Related conjectures

 
 implied by
 Real roots of the flow polynomial
 disproved
 Same sign argument at the non-integer point 5.5. For a 2-edge-connected (hence bridgeless) graph G, the flow polynomial Phi(G,t) is nonzero and positive for large t (it is monic of degree |E|-|V|+c; alternatively Phi(G,6)>0 by Seymour's 6-flow theorem). If Phi has no real root greater than 4, it cannot change sign on (4,infinity), so Phi(G,5.5)>0, which is exactly the target conjecture. Self-contained; direction correct.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
