Attack the following open graph-theory problem.

Catalog id: the_crossing_number_of_the_hypercube
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Topological Graph Theory » Crossing numbers
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_crossing_number_of_the_hypercube/
Original entry: http://www.openproblemgarden.org/op/the_crossing_number_of_the_hypercube
Problem attributed to: Erdos, Paul, Guy, Richard K. (posted 2007-05-11)

=== Problem statement (OpenProblemGarden) ===
Title: The Crossing Number of the Hypercube
The crossing number $ cr(G) $ of $ G $ is the minimum number of crossings in all drawings of $ G $ in the plane. The $ d $ -dimensional (hyper)cube $ Q_d $ is the graph whose vertices are all binary sequences of length $ d $ , and two of the sequences are adjacent in $ Q_d $ if they differ in precisely one coordinate. Conjecture $ \displaystyle \lim \frac{cr(Q_d)}{4^d} = \frac{5}{32} $

=== Discussion / context (OpenProblemGarden) ===
It is known that $ cr(Q_d) = 0 $ for $ d = 1,2,3 $ and that $ cr(Q_4) = 8 $ . No other exact values are known. Madej [M] proved that $ cr(Q_d) \le 4^d/6 + o(4^d/6) $ . Faria and de Figueiredo [FF] improved the upper bound to $ (165/1024) 4^d $ . Sykora and Vrto [SV] proved that $ 4^d/20 + o(4^d/20) $ is a lower bound on $ cr(Q_d) $ .

=== References listed by OpenProblemGarden ===
- *[EG] P. Erdős and R.K. Guy, Crossing number problems, Amer. Math. Monthly 80 (1973) 52-58.
- [FF] L. Faria, C.M.H. de Figueiredo, On Eggleton and Guy's conjectured upper bound for the crossing number of the -cube, Math. Slovaca 50 (2000) 271-287.
- [M] T. Madej, Bounds for the crossing number of the -cube, J. Graph Theory 15 (1991) 81-97.
- [SV] O. Sykora and I. Vrto, On crossing numbers of hypercubes and cube connected cycles, BIT 33 (1993) 232-237.

=== Catalog page (statement + literature review) ===
The Crossing Number of the Hypercube — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Yang, Wang, Wang, and Zhou (arXiv 2012, published J. Graph Theory 2022) disproved the exact Erdős-Guy formula $\mathrm{cr}(Q_n) = \frac{5}{32}4^n - \lfloor\frac{n^2+1}{2}\rfloor 2^{n-2}$ by constructing drawings of $Q_n$ with strictly fewer crossings for $n > 6$. The OPG limit conjecture $\lim \mathrm{cr}(Q_d)/4^d = 5/32$ is not directly resolved by this disproof, and the asymptotic question remains open with bounds roughly in $[1/20,\, 5/32]$. Separately, Faria, de Figueiredo, Sýkora, and Vrťo (J. Graph Theory 2008) improved the upper bound beyond the 2000 result cited at OPG, matching the EG formula's leading term before Yang et al. showed even that was not tight.

 Cited literature (1)

 
 
 
counterexample Disproof of a conjecture by Erdős and Guy on the crossing number of hypercubes
 (2012)
 

 
 Yuansheng Yang, Guoqing Wang, Haoli Wang, Yan Zhou · arXiv preprint · arXiv:1201.4700 · doi:10.1002/jgt.22787

Constructs drawings of $Q_n$ with strictly fewer crossings than the Erdős-Guy formula predicts for $n > 6$, disproving the exact equality $\mathrm{cr}(Q_n) = \frac{5}{32}4^n - \lfloor\frac{n^2+1}{2}\rfloor 2^{n-2}$.
 

 

 Reviewer notes. The OPG states the conjecture as a limit (lim cr(Q_d)/4^d = 5/32), whereas the original 1973 Erdős-Guy paper conjectured the exact formula cr(Q_n) = (5/32)4^n - floor((n²+1)/2)·2^(n-2). Yang et al. disprove the exact formula; the asymptotic limit question is not explicitly addressed and remains open. The Faria, de Figueiredo, Sýkora, Vrťo (2008, J. Graph Theory doi:10.1002/jgt.20330) paper improved the upper bound beyond the 2000 result cited at OPG (achieving exactly the EG formula's leading term), and is a relevant post-posting result, but the Wiley/JGT page returned 403 and the PDF was binary-only, so it could not be verified and is not included in since_posted. The Mohar/SFU problem page was last updated June 2001 and does not reflect post-2007 developments.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Conjecture. $ \displaystyle \lim \frac{cr(Q_d)}{4^d} = \frac{5}{32} $

Keywords:
crossing number · hypercube

Discussion

It is known that $ cr(Q_d) = 0 $ for $ d = 1,2,3 $ and that $ cr(Q_4) = 8 $ . No other exact values are known. Madej [M] proved that $ cr(Q_d) \le 4^d/6 + o(4^d/6) $ . Faria and de Figueiredo [FF] improved the upper bound to $ (165/1024) 4^d $ . Sykora and Vrto [SV] proved that $ 4^d/20 + o(4^d/20) $ is a lower bound on $ cr(Q_d) $ .

Bibliography

★ [EG]
 P. Erdős and R.K. Guy, Crossing number problems, Amer. Math. Monthly 80 (1973) 52-58.

 [FF]
 L. Faria, C.M.H. de Figueiredo, On Eggleton and Guy's conjectured upper bound for the crossing number of the $ n $ -cube, Math. Slovaca 50 (2000) 271-287.

 [M]
 T. Madej, Bounds for the crossing number of the $ n $ -cube, J. Graph Theory 15 (1991) 81-97.

 [SV]
 O. Sykora and I. Vrto, On crossing numbers of hypercubes and cube connected cycles, BIT 33 (1993) 232-237.
