Attack the following open graph-theory problem.

Catalog id: crossing_sequences
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/crossing_sequences/
Original entry: http://www.openproblemgarden.org/op/crossing_sequences
Problem attributed to: Archdeacon, Dan, Bonnington, C. Paul, Siran, Jozef (posted 2008-07-30)

=== Problem statement (OpenProblemGarden) ===
Title: Crossing sequences
Conjecture Let $ (a_0,a_1,a_2,\ldots,0) $ be a sequence of nonnegative integers which strictly decreases until $ 0 $ . Then there exists a graph that be drawn on a surface with orientable (nonorientable, resp.) genus $ i $ with $ a_i $ crossings, but not with less crossings.

=== Discussion / context (OpenProblemGarden) ===
This actually are two conjectures, one for the orientable case and another for nonorientable one. For sequences $ (a_0,a_1,0) $ the nonorientable case was resolved in [ABS] and the orientable one in [DMS]. The conclusion also holds (for the orientable case) whenever the sequence $ (a_i) $ is convex [S], that is whenever $ a_i - a_{i-1} $ is nonincreasing. It might seem that this condition is also necessary: For the most extreme sequence $ (N,N-1,0) $ (suggested by Salazar) one needs to construct a graph for which adding one handle saves just one crossing, while adding another saves many -- but then why not add the second handle first? Somewhat surprisingly, graphs with this counterintuitive property exist, at least for sequences $ (a_0,a_1,0) $ . An interesting open case is to consider sequences for which $$ a_0 - a_s < \varepsilon (a_s - a_{s+1}) $$ for some $ s $ and small $ \varepsilon $ .

=== References listed by OpenProblemGarden ===
- *[ABS] Dan Archdeacon, C. Paul Bonnington, and Jozef Siran, Trading crossings for handles and crosscaps, J.Graph Theory 38 (2001), 230--243.
- [DMS] Matt DeVos, Bojan Mohar, Robert Samal, Unexpected behaviour of crossing sequences, in preparation
- [S] Jozef Siran, The crossing function of a graph, Abh. Math. Sem. Univ. Hamburg 53 (1983), 131--133.

=== Catalog page (statement + literature review) ===
Crossing sequences — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture asks whether every strictly decreasing sequence of nonneg integers ending in 0 is realizable as a crossing sequence of some graph. DeVos, Mohar, and Samal (2011) resolved the orientable case for length-3 sequences $(a, b, 0)$, proving that for any $a > b > 0$ there exists a graph with $\mathrm{cr}_0(G) = a$, $\mathrm{cr}_1(G) = b$, $\mathrm{cr}_2(G) = 0$; together with the pre-posting ABS (2001) nonorientable length-3 result and the known convex-sequence case, this constitutes meaningful partial progress, but the full conjecture for arbitrary-length strictly decreasing sequences remains open.

 Cited literature (1)

 
 
 
partial Unexpected behaviour of crossing sequences
 (2011)
 

 
 Matt DeVos, Bojan Mohar, Robert Samal · Journal of Combinatorial Theory, Series B

Proves the orientable case for length-3 crossing sequences: for any integers $a > b > 0$ there exists a graph $G$ with $\mathrm{cr}_0(G) = a$, $\mathrm{cr}_1(G) = b$, $\mathrm{cr}_2(G) = 0$, resolving a problem of Salazar and confirming the conjecture for this special case.
 

 

 Reviewer notes. The DMS paper was explicitly listed as 'in preparation' in the OPG posting (2008) and appeared in J. Combin. Theory Ser. B 101 (2011) 448–463; the citation was confirmed via Mohar's publication list since the ScienceDirect page returned HTTP 403 and the SFU PDF returned unreadable binary. No post-2011 paper directly advancing the general crossing-sequences conjecture for longer sequences was found; the conjecture for sequences of length ≥ 4 appears open. The arXiv:2405.06118 paper by Timothy Sun addresses Kainen's (different) conjectures on surface crossing numbers and is not directly relevant.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Let $ (a_0,a_1,a_2,\ldots,0) $ be a sequence of nonnegative integers which strictly decreases until $ 0 $ . Then there exists a graph that be drawn on a surface with orientable (nonorientable, resp.) genus $ i $ with $ a_i $ crossings, but not with less crossings.

Keywords:
crossing number · crossing sequence

Discussion

This actually are two conjectures, one for the orientable case and another for nonorientable one. For sequences $ (a_0,a_1,0) $ the nonorientable case was resolved in [ABS] and the orientable one in [DMS]. The conclusion also holds (for the orientable case) whenever the sequence $ (a_i) $ is convex [S], that is whenever $ a_i - a_{i-1} $ is nonincreasing. It might seem that this condition is also necessary: For the most extreme sequence $ (N,N-1,0) $ (suggested by Salazar) one needs to construct a graph for which adding one handle saves just one crossing, while adding another saves many -- but then why not add the second handle first? Somewhat surprisingly, graphs with this counterintuitive property exist, at least for sequences $ (a_0,a_1,0) $ . An interesting open case is to consider sequences for which $$ a_0 - a_s < \varepsilon (a_s - a_{s+1}) $$ for some $ s $ and small $ \varepsilon $ .

Bibliography

★ [ABS]
 Dan Archdeacon, C. Paul Bonnington, and Jozef Siran, Trading crossings for handles and crosscaps, J.Graph Theory 38 (2001), 230--243.

 [DMS]
 Matt DeVos, Bojan Mohar, Robert Samal, Unexpected behaviour of crossing sequences, in preparation

 [S]
 Jozef Siran, The crossing function of a graph, Abh. Math. Sem. Univ. Hamburg 53 (1983), 131--133.
