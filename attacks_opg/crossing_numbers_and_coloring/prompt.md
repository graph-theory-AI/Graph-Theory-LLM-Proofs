Attack the following open graph-theory problem.

Catalog id: crossing_numbers_and_coloring
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/crossing_numbers_and_coloring/
Original entry: http://www.openproblemgarden.org/op/crossing_numbers_and_coloring
Problem attributed to: Albertson, Michael O. (posted 2009-09-04)

=== Problem statement (OpenProblemGarden) ===
Title: Crossing numbers and coloring
We let $ cr(G) $ denote the crossing number of a graph $ G $ . Conjecture Every graph $ G $ with $ \chi(G) \ge t $ satisfies $ cr(G) \ge cr(K_t) $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is an interesting weakening of the disproved Hajos Conjecture which asserted that $ \chi(G) \ge t $ implies that $ G $ contains a subdivision of $ K_t $ . A minimal counterexample to Albertson's conjecture is critical, with minimum degree $ \ge t $ . Using this and the crossing lemma, Albertson, Cranston and Fox showed that a minimum counterexample has at most $ 4t $ vertices. They then analyzed small cases to show that the conjecture holds for $ t \le 12 $ . More recently, Barat and Toth [BT] sharpened these arguments to show that the conjecture holds for $ t \le 16 $ .

=== References listed by OpenProblemGarden ===
- [BT] J. Barat and G. Toth, Towards the Albertson Conjecture

=== Catalog page (statement + literature review) ===
Crossing numbers and coloring — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Albertson's conjecture remains open in general, but substantial progress has been made since it was posted in 2009. Ackerman (2019) extended the verified range from $t \le 16$ to $t \le 18$; Cranston (2025) further pushed this to $t \le 24$ and greatly restricts possible counterexamples for $t \in \{25, 26\}$; Fox, Pach, and Suk (SoCG 2025) proved the conjecture for all graphs with chromatic number $k$ having at most $1.4(k-1)$ vertices (for sufficiently large $k$), via the Lescure–Meyniel weak immersion conjecture.

 Cited literature (3)

 
 
 
partial On topological graphs with at most four crossings per edge
 (2019)
 

 
 Eyal Ackerman · Computational Geometry · arXiv:1509.01932

As a corollary of results on topological graphs with at most four crossings per edge, proves Albertson's conjecture for $r \le 18$, extending the prior bound of $r \le 16$.
 

 
 
partial Immersions and Albertson's Conjecture
 (2025)
 

 
 Jacob Fox, János Pach, Andrew Suk · 41st International Symposium on Computational Geometry (SoCG 2025) · arXiv:2510.05893 · doi:10.4230/LIPIcs.SoCG.2025.50

Proves Albertson's conjecture for all graphs with chromatic number $k$ having at most $1.4(k-1)$ vertices (for sufficiently large $k$), via a proof of the Lescure–Meyniel weak immersion conjecture in that range.
 

 
 
partial Progress on Albertson's Conjecture
 (2025)
 

 
 Daniel W. Cranston · arXiv preprint · arXiv:2512.08020

Extends verification of Albertson's conjecture to $r \le 24$ (from $r \le 18$) and greatly restricts the possible counterexamples for $r \in \{25, 26\}$, also improving bounds on the order of a minimum counterexample.
 

 

 Reviewer notes. The Ackerman paper (arXiv:1509.01932) was submitted in 2015 and revised/published in 2019; Wikipedia identifies the venue as Computational Geometry but I did not independently verify the journal DOI. The Fox–Pach–Suk arXiv preprint (2510.05893) appeared October 2025 after the SoCG 2025 conference; the published DROPS version cites the 1.4(k-1) vertex bound. The Cranston 2025 paper (arXiv:2512.08020) is a preprint as of December 2025; journal publication status unknown. The conjecture remains wide open for general graphs.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. Every graph $ G $ with $ \chi(G) \ge t $ satisfies $ cr(G) \ge cr(K_t) $ .

Keywords:
coloring · complete graph · crossing number

Discussion

This conjecture is an interesting weakening of the disproved Hajos Conjecture which asserted that $ \chi(G) \ge t $ implies that $ G $ contains a subdivision of $ K_t $ . A minimal counterexample to Albertson's conjecture is critical, with minimum degree $ \ge t $ . Using this and the crossing lemma, Albertson, Cranston and Fox showed that a minimum counterexample has at most $ 4t $ vertices. They then analyzed small cases to show that the conjecture holds for $ t \le 12 $ . More recently, Barat and Toth [BT] sharpened these arguments to show that the conjecture holds for $ t \le 16 $ .

Bibliography

 [BT]
 J. Barat and G. Toth, Towards the Albertson Conjecture
 Towards the Albertson Conjecture
