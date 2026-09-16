Attack the following open graph-theory problem.

Catalog id: fractional_hadwiger
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/fractional_hadwiger/
Original entry: http://www.openproblemgarden.org/op/fractional_hadwiger
Problem attributed to: Harvey, Daniel J., Reed, Bruce A., Seymour, Paul D., Wood, David R. (posted 2014-03-16)

=== Problem statement (OpenProblemGarden) ===
Title: Fractional Hadwiger
Conjecture For every graph $ G $ , (a) $ \chi_f(G)\leq\text{had}(G) $ (b) $ \chi(G)\leq\text{had}_f(G) $ (c) $ \chi_f(G)\leq\text{had}_f(G) $ .

=== Discussion / context (OpenProblemGarden) ===
Here $ \chi $ is the chromatic number, $ \chi_f $ is the fractional chromatic number, $ \text{had} $ is the Hadwiger number, and $ \text{had}_f $ is the fractional Hadwiger number (which was recently introduced independently by Fox [F] and Pedersen [P]). It is well known and easily proved (see [HW]) that $ \chi_f(G)\leq\chi(G)\text{ and }\text{had}(G)\leq\text{had}_f(G)\leq\text{tw}(G)+1, $ where $ \text{tw}(G) $ is the treewidth of $ G $ . Hadwiger's famous conjecture, $ \chi(G)\leq\text{had}(G) $ , bridges the gap in the above inequalities. The above conjectures therefore are weaker than Hadwiger's conjecture. Note that Conjecture (a) implies Conjecture (c), and Conjecture (b) implies Conjecture (c). Note that Reed and Seymour [RS] proved that $ \chi_f(G)\leq2\,\text{had}(G) $ . Conjecture (a) is due to Reed and Seymour [RS]. Conjecture (b) is due to Harvey and Wood [HW]. Conjecture (c) is independently due to Harvey and Wood [HW] and Pedersen [P]. Pedersen [P] presents a natural equivalent formulation of Conjecture (c).

=== References listed by OpenProblemGarden ===
- *[HW] Daniel J. Harvey, David R. Wood, Parameters tied to treewidth. arXiv:1312.3401, 2013.
- [F] Jacob Fox. Constructing dense graphs with sublinear Hadwiger number. J. Combin. Theory Ser. B (to appear).
- *[P] Anders Sune Pedersen. Contributions to the Theory of Colourings, Graph Minors, and Independent Sets, PhD thesis, Department of Mathematics and Computer Science University of Southern Denmark, 2011.
- *[RS] Bruce A. Reed, Paul D. Seymour, Fractional colouring and Hadwiger's conjecture. J. Combin. Theory Ser. B, 74(2), 147-152.

=== Catalog page (statement + literature review) ===
Fractional Hadwiger — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 No verified post-2014 paper resolves any of the three conjectures (a) $\chi_f(G)\leq\mathrm{had}(G)$, (b) $\chi(G)\leq\mathrm{had}_f(G)$, or (c) $\chi_f(G)\leq\mathrm{had}_f(G)$. The best published upper bound on $\chi_f$ in terms of $\mathrm{had}$ remains Reed and Seymour's 1998 result $\chi_f(G)\leq 2\,\mathrm{had}(G)$; recent improvements toward Hadwiger's conjecture by Norin, Postle and Song concern $\chi(G)$ versus $\mathrm{had}(G)$ rather than the fractional variants.

 Reviewer notes. Searches surfaced recent work on the (integer) Hadwiger conjecture (Norin-Postle-Song, Steiner 2023 on topological bounds, Postle's improved bounds) and on related variants (odd Hadwiger, balanced chromatic number, strong chromatic index), but none of the verified items prove or disprove any of conjectures (a), (b), (c). The Fox 2011 paper (arXiv:1108.4953) introducing $\mathrm{had}_f$ predates the OPG posting date of 2014-03-16, so it cannot count as 'since posted'. I did not exhaustively search for unpublished theses or short notes, so a small probability remains that incremental progress exists in less indexed venues; status reported as 'open' rather than 'unclear' because the OPG-listed Reed-Seymour bound $\chi_f\leq 2\,\mathrm{had}$ from 1998 is still the state of the art quoted in surveys.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. For every graph $ G $ , (a) $ \chi_f(G)\leq\text{had}(G) $ (b) $ \chi(G)\leq\text{had}_f(G) $ (c) $ \chi_f(G)\leq\text{had}_f(G) $ .

Keywords:
fractional coloring, minors

Discussion

Here $ \chi $ is the chromatic number, $ \chi_f $ is the fractional chromatic number, $ \text{had} $ is the Hadwiger number, and $ \text{had}_f $ is the fractional Hadwiger number (which was recently introduced independently by Fox [F] and Pedersen [P]). It is well known and easily proved (see [HW]) that $ \chi_f(G)\leq\chi(G)\text{ and }\text{had}(G)\leq\text{had}_f(G)\leq\text{tw}(G)+1, $ where $ \text{tw}(G) $ is the treewidth of $ G $ . Hadwiger's famous conjecture, $ \chi(G)\leq\text{had}(G) $ , bridges the gap in the above inequalities. The above conjectures therefore are weaker than Hadwiger's conjecture. Note that Conjecture (a) implies Conjecture (c), and Conjecture (b) implies Conjecture (c). Note that Reed and Seymour [RS] proved that $ \chi_f(G)\leq2\,\text{had}(G) $ . Conjecture (a) is due to Reed and Seymour [RS]. Conjecture (b) is due to Harvey and Wood [HW]. Conjecture (c) is independently due to Harvey and Wood [HW] and Pedersen [P]. Pedersen [P] presents a natural equivalent formulation of Conjecture (c).

Bibliography

★ [HW]
 Daniel J. Harvey, David R. Wood, Parameters tied to treewidth. arXiv:1312.3401 , 2013.
 arXiv:1312.3401

 [F]
 Jacob Fox. Constructing dense graphs with sublinear Hadwiger number . J. Combin. Theory Ser. B (to appear).
 Constructing dense graphs with sublinear Hadwiger number

★ [P]
 Anders Sune Pedersen. Contributions to the Theory of Colourings, Graph Minors, and Independent Sets , PhD thesis, Department of Mathematics and Computer Science University of Southern Denmark, 2011.
 Contributions to the Theory of Colourings, Graph Minors, and Independent Sets

★ [RS]
 Bruce A. Reed, Paul D. Seymour, Fractional colouring and Hadwiger's conjecture. J. Combin. Theory Ser. B, 74(2), 147-152.

Related conjectures

 
 implies
 Independence number lower bound in K_{t+1}-minor-free graphs
 open
 If G is K_{t+1}-minor-free then its Hadwiger number satisfies had(G) ≤ t. Part (a) of the Fractional Hadwiger conjecture gives χ_f(G) ≤ had(G) ≤ t. The standard inequality χ_f(G) ≥ n/α(G) (every fractional coloring covers each vertex by independent sets of size ≤ α, LP duality) then gives α(G) ≥ n/χ_f(G) ≥ n/t, which is exactly the target. Only part (a) of the source is needed, and the source conjecture asserts (a), (b), (c) jointly, so truth of the source forces the target. The target's own context confirms this is a weakening along exactly this chain (via Hadwiger). Direction correct.
 

 
 implies
 Seagull problem
 partial
 Part (a) of Fractional Hadwiger states chi_f(G) <= had(G). By LP duality (fractional covering by independent sets), chi_f(G) >= n/alpha(G) for every n-vertex G. If G has no independent set of size 3 then alpha(G) <= 2, so chi_f(G) >= n/2, whence had(G) >= n/2; since had(G) is an integer, G has a K_{ceil(n/2)} minor, i.e. a complete minor on >= n/2 vertices — exactly the Seagull problem. The source conjecture is the conjunction of (a),(b),(c), and (a) alone suffices, so the conjecture implies Seagull. (Part (b) alone would not obviously suffice, since had_f >= had; but the edge is from the full conjecture.) Direction correct: Fractional Hadwiger is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
