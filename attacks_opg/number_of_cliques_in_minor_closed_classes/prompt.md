Attack the following open graph-theory problem.

Catalog id: number_of_cliques_in_minor_closed_classes
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/number_of_cliques_in_minor_closed_classes/
Original entry: http://www.openproblemgarden.org/op/number_of_cliques_in_minor_closed_classes
Problem attributed to: Wood, David R. (posted 2009-10-12)

=== Problem statement (OpenProblemGarden) ===
Title: Number of Cliques in Minor-Closed Classes
Question Is there a constant $ c $ such that every $ n $ -vertex $ K_t $ -minor-free graph has at most $ c^tn $ cliques?

=== Discussion / context (OpenProblemGarden) ===
Here a clique is a (not neccessarily maximal) set of pairwise adjacent vertices in a graph. See [RW, NSTW] for early bounds on the number of cliques. Wood [W] proved that the number of cliques in an $ n $ -vertex $ K_t $ -minor-free graph is at most $ c^{t\sqrt{\log t}}n\enspace. $ Fomin et al. [FOT] improved this bound to $ c^{t\log\log t}n\enspace. $ These results are based on the fact that every $ n $ -vertex $ K_t $ -minor-free graph has at most $ ct\sqrt{\log t}n $ edges. This bound is tight for certain random graphs. So it is reasonable to expect that random graphs might also provide good lower bounds on the number of cliques. Update 2014: Choongbum Lee and Sang-il Oum [LO] recently answered this question in the affirmative, and even proved it for excluded subdivisions. In particular, they proved that every $ n $ -vertex graph with no $ K_t $ -subdivision has at most $ 2^{474t}n $ cliques and also at most $ 2^{14t+o(t)}n $ cliques. The question now is to determine the minimum constant. Wood [W] proved a lower bound of $ 3^{2t/3-o(t)}n $ using an appropriate sized complete graph minus a perfect matching. The same graph gives a lower bound of $ 3^{s-o(s)}n $ on the number of cliques in a graph with no $ K_s $ subdivision. Update (2019): Fox and Wei [FW] have proved that every graph on $ n $ vertices with no $ K_t $ -minor has at most $ 3^{2t/3+o(t)}n $ cliques. This bound is tight for $ n \geq 4t/3 $ .

=== References listed by OpenProblemGarden ===
- [FOT] Fedor V. Fomin, Sang il Oum, and Dimitrios M. Thilikos. Rank-width and tree-width of -minor-free graphs, European J. Combin. 31 (7), 1617–1628, 2010.
- [NSTW] Serguei Norine, Paul Seymour, Robin Thomas, Paul Wollan. Proper minor-closed families are small. J. Combin. Theory Ser. B, 96(5):754--757, 2006.
- [RW] Bruce Reed and David R. Wood. Fast separation in a graph with an excluded minor. In 2005 European Conf. on Combinatorics, Graph Theory and Applications (EuroComb '05), vol. AE of Discrete Math. Theor. Comput. Sci. Proceedings, pp. 45--50. 2005.
- * [W] David R. Wood. On the maximum number of cliques in a graph. Graphs Combin., 23(3):337--352, 2007.
- [LO] Choongbum Lee and Sang-il Oum. Number of cliques in graphs with forbidden minor, 2014.
- [FW] Jacob Fox, Fan Wei. On the number of cliques in graphs with a forbidden minor

=== Catalog page (statement + literature review) ===
Number of Cliques in Minor-Closed Classes — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 The original question was answered affirmatively by Lee and Oum (2014), who showed every $n$-vertex $K_t$-minor-free graph has at most $c^t n$ cliques for some absolute constant $c$. Fox and Wei (arXiv 2016) sharpened this to the asymptotically tight bound $3^{2t/3+o(t)}n$, matching Wood's lower-bound construction for $n \geq 4t/3$. Shi and Wei (2024) further determined essentially sharp bounds on the number of $k$-cliques in $K_t$-minor-free graphs for each fixed order $k$.

 Cited literature (2)

 
 
 
proof On the number of cliques in graphs with a forbidden minor
 (2017)
 

 
 Jacob Fox, Fan Wei · Journal of Combinatorial Theory, Series B · arXiv:1603.07056 · doi:10.1016/j.jctb.2017.04.004

Proves the asymptotically tight bound $3^{2t/3+o(t)}n$ on the total number of cliques in $K_t$-minor-free graphs on $n$ vertices, showing it is tight for $n \geq 4t/3$, thereby resolving the question of the exponential constant.
 

 
 
partial Extremal number of cliques of given orders in graphs with a forbidden clique minor
 (2024)
 

 
 Ruilin Shi, Fan Wei · arXiv preprint · arXiv:2408.12082

Determines essentially sharp bounds (up to $o_t(1)$ in the exponent) on the maximum number of cliques of each fixed order $k$ in $K_t$-minor-free graphs, answering a refinement of Wood's and Fox–Wei's questions and partially disproving a conjecture of Wood.
 

 

 Reviewer notes. The Lee–Oum 2014 paper (OPG reference [LO]) first resolved the original question affirmatively, but its KAIST PDF URL returned unreadable binary content and no arXiv ID was found; it is therefore not cited in since_posted despite being a key result. The Fox–Wei paper was published in J. Combin. Theory Ser. B 126 (2017) 175–197, DOI 10.1016/j.jctb.2017.04.004; the ScienceDirect abstract explicitly says Lee–Oum answered Wood's original question affirmatively and that Fox–Wei determine the exponential constant. The Shi–Wei 2024 paper (arXiv:2408.12082) was found on a Wiley page suggesting publication in J. London Math. Soc., but that page also returned HTTP 403. The o(t) term in the Fox–Wei exponent means the exact minimum constant remains open as a follow-on question.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Question. Is there a constant $ c $ such that every $ n $ -vertex $ K_t $ -minor-free graph has at most $ c^tn $ cliques?

Keywords:
clique · graph · minor

Discussion

Here a clique is a (not neccessarily maximal) set of pairwise adjacent vertices in a graph. See [RW, NSTW] for early bounds on the number of cliques. Wood [W] proved that the number of cliques in an $ n $ -vertex $ K_t $ -minor-free graph is at most $ c^{t\sqrt{\log t}}n\enspace. $ Fomin et al. [FOT] improved this bound to $ c^{t\log\log t}n\enspace. $ These results are based on the fact that every $ n $ -vertex $ K_t $ -minor-free graph has at most $ ct\sqrt{\log t}n $ edges. This bound is tight for certain random graphs. So it is reasonable to expect that random graphs might also provide good lower bounds on the number of cliques. Update 2014: Choongbum Lee and Sang-il Oum [LO] recently answered this question in the affirmative, and even proved it for excluded subdivisions. In particular, they proved that every $ n $ -vertex graph with no $ K_t $ -subdivision has at most $ 2^{474t}n $ cliques and also at most $ 2^{14t+o(t)}n $ cliques. The question now is to determine the minimum constant. Wood [W] proved a lower bound of $ 3^{2t/3-o(t)}n $ using an appropriate sized complete graph minus a perfect matching. The same graph gives a lower bound of $ 3^{s-o(s)}n $ on the number of cliques in a graph with no $ K_s $ subdivision. Update (2019): Fox and Wei [FW] have proved that every graph on $ n $ vertices with no $ K_t $ -minor has at most $ 3^{2t/3+o(t)}n $ cliques. This bound is tight for $ n \geq 4t/3 $ .

Bibliography

 [FOT]
 Fedor V. Fomin, Sang il Oum, and Dimitrios M. Thilikos. Rank-width and tree-width of $ H $ -minor-free graphs , European J. Combin. 31 (7), 1617–1628, 2010.
 Rank-width and tree-width of -minor-free graphs

 [NSTW]
 Serguei Norine, Paul Seymour, Robin Thomas, Paul Wollan. Proper minor-closed families are small. J. Combin. Theory Ser. B , 96(5):754--757, 2006.

 [RW]
 Bruce Reed and David R. Wood. Fast separation in a graph with an excluded minor. In 2005 European Conf. on Combinatorics, Graph Theory and Applications (EuroComb '05), vol. AE of Discrete Math. Theor. Comput. Sci. Proceedings , pp. 45--50. 2005.

★ [W]
 David R. Wood. On the maximum number of cliques in a graph . Graphs Combin. , 23(3):337--352, 2007.
 On the maximum number of cliques in a graph

 [LO]
 Choongbum Lee and Sang-il Oum. Number of cliques in graphs with forbidden minor , 2014.
 Number of cliques in graphs with forbidden minor

 [FW]
 Jacob Fox, Fan Wei. On the number of cliques in graphs with a forbidden minor
 On the number of cliques in graphs with a forbidden minor

Related conjectures

 
 implied by
 Optimal clique count exponent for K_t-subdivisions
 open
 A K_t-subdivision yields a K_t-minor, so every K_t-minor-free graph is K_t-subdivision-free; the containment goes the right way for the claimed direction. The source's conjectured bound 3^{2t/3+o(t)} n on cliques in K_t-subdivision-free graphs is at most c^t n for a fixed constant c (3^{2t/3} = (3^{2/3})^t and the 3^{o(t)} factor is absorbed by slightly enlarging c, with finitely many small t handled by a constant), which answers the OPG question affirmatively. The target was independently resolved (Lee-Oum 2014, Fox-Wei 2019, as noted on the OPG page), which is consistent with but not needed for the implication.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
