Attack the following open graph-theory problem.

Catalog id: list_hadwiger_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_hadwiger_conjecture/
Original entry: http://www.openproblemgarden.org/op/list_hadwiger_conjecture
Problem attributed to: Kawarabayashi, Ken-ichi, Mohar, Bojan (posted 2014-07-07)

=== Problem statement (OpenProblemGarden) ===
Title: List Hadwiger Conjecture
Conjecture Every $ K_t $ -minor-free graph is $ c t $ -list-colourable for some constant $ c\geq1 $ .

=== Discussion / context (OpenProblemGarden) ===
Hadwiger's conjecture asserts that every $ K_t $ - minor -free graph is $ (t − 1) $ -colourable. Robertson, Seymour and Thomas [RST] proved Hadwiger's conjecture for $ t \leq 6 $ . It remains open for $ t \geq 7 $ . In fact, it is open whether every $ K_t $ -minor-free graph is $ ct $ -colourable for some constant $ c\geq 1 $ . It is natural to consider analogous problems for list colourings . First, consider planar graphs. While every planar graph is 4-colourable, Erdös, Rubin and Taylor. [ERT] conjectured that some planar graph is not 4-list-colourable, and that every planar graph is 5-list-colourable. The first conjecture was verified by Voigt [V] and the second by Thomassen [T]. More generally, Borowiecki [B] asked whether every $ K_t $ -minor-free graph is $ (t − 1) $ -list-colourable, which is true for $ t \leq 4 $ but false for $ t = 5 $ by Voigt’s example. Kawarabayashi and Mohar [KM] proposed the stated conjecture, and suggested it might be true with $ c=\frac{3}{2} $ . Barát, Joret and Wood [BJW] proved that $ c\geq\frac{4}{3} $ . In particular, they constructed a $ K_{3t+2} $ -minor-free graph that is not $ 4t $ -list-colourable.

=== References listed by OpenProblemGarden ===
- [B] Mieczyslaw Borowiecki. Research problem 172. Discrete Math., 121:235–236, 1993. .
- [BJW] Janos Barát, Gwenael Joret, David R. Wood. Disproof of the List Hadwiger Conjecture, Electronic J. Combinatorics 18:P232, 2011.
- [ERT] Paul Erdo ̋s, Arthur L. Rubin, and Herbert Taylor. Choosability in graphs. In Proc. West Coast Conference on Combinatorics, Graph Theory and Computing, vol. XXVI of Congress. Numer., pp. 125–157. Utilitas Math., 1980. MathSciNet.
- *[KM] Ken-ichi Kawarabayashi and Bojan Mohar. A relaxed Hadwiger’s conjecture for list colorings. J. Combin. Theory Ser. B, 97(4):647–651, 2007. MathSciNet.
- [RST] Neil Robertson, Paul D. Seymour, and Robin Thomas. Hadwiger’s conjecture for -free graphs. Combinatorica, 13(3):279–361, 1993. MathSciNet.
- [T] Carsten Thomassen. Every planar graph is 5-choosable. J. Combin. Theory Ser. B, 62(1):180–181, 1994. MathSciNet.

=== Catalog page (statement + literature review) ===
List Hadwiger Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that every $K_t$-minor-free graph is $ct$-list-colourable for some absolute constant $c$ remains open. Norin and Postle (2020) established the best current upper bound of $O(t(\log t)^\beta)$-list-colorability for every $\beta > 1/4$, falling short of the conjectured linear bound. Steiner (2022) improved the lower bound to $(2-o(1))t$, refuting the specific sub-conjecture $c = 3/2$ of Kawarabayashi and Mohar and showing $c \geq 2$ is necessary.

 Cited literature (4)

 
 
 
partial Connectivity and choosability of graphs with no $K_t$ minor
 (2020)
 

 
 Sergey Norin, Luke Postle · arXiv preprint · arXiv:2004.10367

Every $K_t$-minor-free graph is $O(t(\log t)^\beta)$-list-colorable for every $\beta > 1/4$, improving the previous $O(t\sqrt{\log t})$ upper bound and providing the best known bound for list coloring.
 

 
 
partial Improved lower bound for the list chromatic number of graphs with no $K_t$ minor
 (2022)
 

 
 Raphael Steiner · Combinatorics, Probability and Computing · arXiv:2110.09403 · doi:10.1017/S0963548322000116

The maximum list chromatic number of $K_t$-minor-free graphs is at least $(2-o(1))t$, showing $c \geq 2$ is necessary and disproving the specific conjecture of Kawarabayashi–Mohar that $c = 3/2$ suffices.
 

 
 
partial Refined list version of Hadwiger's conjecture
 (2022)
 

 
 Yangyan Gu, Yiting Jiang, David R. Wood, Xuding Zhu · SIAM Journal on Discrete Mathematics · arXiv:2209.07013 · doi:10.1137/22M1522413

Introduces a λ-choosability framework and proves that for any $\varepsilon > 0$ and sufficiently large $t$, for any partition $\lambda$ of $\lfloor(2-\varepsilon)t\rfloor$, there exists a $K_t$-minor-free graph that is not λ-choosable, showing fundamental limitations on list colorability below the $2t$ threshold.
 

 
 
partial Improved lower bound for the list chromatic number of graphs with no $K_t$ minor
 (2021)
 

 
 Raphael Steiner · arXiv preprint · arXiv:2110.09403

Disproves this conjecture by showing that the maximum list chromatic number of $K_t$-minor free graphs is at least $(2-o(1))t$, which strictly exceeds $\frac{3}{2}t$ for all sufficiently large $t$.
 

 

 Reviewer notes. The SIAM page for the Gu–Jiang–Wood–Zhu paper returned 403 Forbidden; verified via the arXiv preprint 2209.07013 instead, using DOI from earlier confirmed search results. The Norin–Postle arXiv preprint (2004.10367) may not yet have a published journal version; cited as arXiv. The Delcourt–Postle O(t log log t) result (arXiv:2108.01633) addresses standard chromatic number only, not list coloring. The gap between the upper bound O(t(log t)^beta) and the linear conjectured bound remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. Every $ K_t $ -minor-free graph is $ c t $ -list-colourable for some constant $ c\geq1 $ .

Keywords:
Hadwiger conjecture · list colouring · minors

Discussion

Hadwiger's conjecture asserts that every $ K_t $ - minor -free graph is $ (t − 1) $ -colourable. Robertson, Seymour and Thomas [RST] proved Hadwiger's conjecture for $ t \leq 6 $ . It remains open for $ t \geq 7 $ . In fact, it is open whether every $ K_t $ -minor-free graph is $ ct $ -colourable for some constant $ c\geq 1 $ . It is natural to consider analogous problems for list colourings . First, consider planar graphs. While every planar graph is 4-colourable, Erdös, Rubin and Taylor. [ERT] conjectured that some planar graph is not 4-list-colourable, and that every planar graph is 5-list-colourable. The first conjecture was verified by Voigt [V] and the second by Thomassen [T]. More generally, Borowiecki [B] asked whether every $ K_t $ -minor-free graph is $ (t − 1) $ -list-colourable, which is true for $ t \leq 4 $ but false for $ t = 5 $ by Voigt’s example. Kawarabayashi and Mohar [KM] proposed the stated conjecture, and suggested it might be true with $ c=\frac{3}{2} $ . Barát, Joret and Wood [BJW] proved that $ c\geq\frac{4}{3} $ . In particular, they constructed a $ K_{3t+2} $ -minor-free graph that is not $ 4t $ -list-colourable.

Bibliography

 [B]
 Mieczyslaw Borowiecki. Research problem 172 . Discrete Math., 121:235–236, 1993. .
 Research problem 172

 [BJW]
 Janos Barát, Gwenael Joret, David R. Wood. Disproof of the List Hadwiger Conjecture , Electronic J. Combinatorics 18:P232, 2011.
 Disproof of the List Hadwiger Conjecture

 [ERT]
 Paul Erdo ̋s, Arthur L. Rubin, and Herbert Taylor. Choosability in graphs . In Proc. West Coast Conference on Combinatorics, Graph Theory and Computing, vol. XXVI of Congress. Numer., pp. 125–157. Utilitas Math., 1980. MathSciNet .
 Choosability in graphs · MathSciNet

★ [KM]
 Ken-ichi Kawarabayashi and Bojan Mohar. A relaxed Hadwiger’s conjecture for list colorings . J. Combin. Theory Ser. B, 97(4):647–651, 2007. MathSciNet .
 A relaxed Hadwiger’s conjecture for list colorings · MathSciNet

 [RST]
 Neil Robertson, Paul D. Seymour, and Robin Thomas. Hadwiger’s conjecture for $ K_6 $ -free graphs . Combinatorica, 13(3):279–361, 1993. MathSciNet .
 Hadwiger’s conjecture for -free graphs · MathSciNet

 [T]
 Carsten Thomassen. Every planar graph is 5-choosable . J. Combin. Theory Ser. B, 62(1):180–181, 1994. MathSciNet .
 Every planar graph is 5-choosable · MathSciNet

Related conjectures

 
 implied by
 List chromatic number bound for K_{s,t}-minor-free graphs
 open
 K_{t-1,t-1} contains a K_t minor: fix a perfect matching a_i b_i and contract the edges a_i b_i for i=1..t-2. The t-2 contracted vertices are pairwise adjacent (a_i is adjacent to b_j for i != j), and the two leftover vertices a_{t-1}, b_{t-1} are adjacent to each other and to every contracted vertex. Hence any K_t-minor-free graph is K_{t-1,t-1}-minor-free, and a positive answer to the source question with s = t' = t-1 gives chi_l(G) <= 2(t-1)+(t-1) = 3t-3 <= 3t for every K_t-minor-free G, which is exactly the List Hadwiger Conjecture with c = 3. Direction is correct: truth of the source forces truth of the target.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
