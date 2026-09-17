Attack the following open graph-theory problem.

Catalog id: forcing_a_2_regular_minor
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Minors
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/forcing_a_2_regular_minor/
Original entry: http://www.openproblemgarden.org/op/forcing_a_2_regular_minor
Problem attributed to: Reed, Bruce A., Wood, David R. (posted 2014-03-16)

=== Problem statement (OpenProblemGarden) ===
Title: Forcing a 2-regular minor
Conjecture Every graph with average degree at least $ \frac{4}{3}t-2 $ contains every 2-regular graph on $ t $ vertices as a minor.

=== Discussion / context (OpenProblemGarden) ===
Reed and Wood [RW] explained that a result of Corradi and Hajnal [CH] implies that if $ H $ is the graph consisting of $ k $ disjoint triangles, then every graph with average degree at least $ 4k-2 $ contains $ H $ as a minor. Moreover, the bound of $ 4k-2 $ is best possible since the complete bipartite graph $ K_{2k-1,n} $ contains no $ H $ -minor, but has average degree tending to $ 4k-2 $ (as $ n\rightarrow\infty $ ). Thus the conjecture would generalise this result. Update: There has been a lot of recent progress on this conjecture [HW,CNLWY].

=== References listed by OpenProblemGarden ===
- [CH] Keresztely Corradi and Andras Hajnal. On the maximal number of independent circuits of a graph. Acta Math. Acad. Sci. Hungar., 14:423–443, 1963.
- *[RW] Bruce Reed and David R. Wood. Forcing a sparse minor, arXiv:1402.0272, 2013.
- [HW] Daniel J. Harvey and David R. Wood. Cycles of given size in a dense graph. SIAM J. Discrete Math. 29.4:2336–2349, 2015.
- [CNLWY] E. Csóka, S. Norin, I. Lo, H. Wu and L. Yepremyan. The extremal function for disconnected minors. J. Comb. Theory B 126 (2017), 162-174.

=== Catalog page (statement + literature review) ===
Forcing a 2-regular minor — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 The Reed-Wood conjecture was proved by Csoka, Lo, Norin, Wu, and Yepremyan (2015 arXiv; published JCTB 2017). Their paper 'The extremal function for disconnected minors' establishes that every graph with average degree at least $\frac{4}{3}t-2$ contains every 2-regular graph on $t$ vertices as a minor, verifying the Reed-Wood (and Harvey-Wood) conjectures for unions of cycles. The bound is tight by the $K_{2k-1,n}$ examples noted in the OPG discussion.

 Cited literature (2)

 
 
 
proof The extremal function for disconnected minors
 (2015)
 

 
 Endre Csoka, Irene Lo, Sergey Norin, Hehui Wu, Liana Yepremyan · arXiv preprint · arXiv:1509.01185 · doi:10.1016/j.jctb.2017.04.005

Proves that every graph with average degree at least 4t/3 - 2 contains every 2-regular graph on t vertices as a minor, settling the Reed-Wood conjecture (and the related Harvey-Wood conjecture for unions of cycles).
 

 
 
partial Average degree conditions forcing a minor
 (2016)
 

 
 Daniel J. Harvey, David R. Wood · Electronic Journal of Combinatorics · arXiv:1506.01775

Strengthens Reed-Wood bounds for sparse graphs with many high-degree vertices and provides earlier partial progress toward the 2-regular minor conjecture, motivating the Csoka et al. resolution.
 

 

 Reviewer notes. The OPG record itself flags [CNLWY] as recent progress; verification of the arXiv PDF confirms Theorem 1 of Csoka-Lo-Norin-Wu-Yepremyan explicitly states and proves the Reed-Wood conjecture (every graph with average degree at least 4t/3 - 2 contains every 2-regular graph on t vertices as a minor). The journal version appeared in J. Combin. Theory Ser. B 126 (2017), 162-174, doi:10.1016/j.jctb.2017.04.005. Sciencedirect/Elsevier abstract page returned 403 to WebFetch but the DOI redirect resolved to the same article and the arXiv preprint was directly verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Every graph with average degree at least $ \frac{4}{3}t-2 $ contains every 2-regular graph on $ t $ vertices as a minor.

Keywords:
minors

Discussion

Reed and Wood [RW] explained that a result of Corradi and Hajnal [CH] implies that if $ H $ is the graph consisting of $ k $ disjoint triangles, then every graph with average degree at least $ 4k-2 $ contains $ H $ as a minor. Moreover, the bound of $ 4k-2 $ is best possible since the complete bipartite graph $ K_{2k-1,n} $ contains no $ H $ -minor, but has average degree tending to $ 4k-2 $ (as $ n\rightarrow\infty $ ). Thus the conjecture would generalise this result. Update: There has been a lot of recent progress on this conjecture [HW,CNLWY].

Bibliography

 [CH]
 Keresztely Corradi and Andras Hajnal. On the maximal number of independent circuits of a graph. Acta Math. Acad. Sci. Hungar. , 14:423–443, 1963.

★ [RW]
 Bruce Reed and David R. Wood. Forcing a sparse minor, arXiv: 1402.0272 , 2013.
 1402.0272

 [HW]
 Daniel J. Harvey and David R. Wood. Cycles of given size in a dense graph . SIAM J. Discrete Math. 29.4:2336–2349, 2015.
 Cycles of given size in a dense graph

 [CNLWY]
 E. Csóka, S. Norin, I. Lo, H. Wu and L. Yepremyan. The extremal function for disconnected minors. J. Comb. Theory B 126 (2017), 162-174.
