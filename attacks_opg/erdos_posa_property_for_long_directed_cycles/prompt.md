Attack the following open graph-theory problem.

Catalog id: erdos_posa_property_for_long_directed_cycles
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/erdos_posa_property_for_long_directed_cycles/
Original entry: http://www.openproblemgarden.org/op/erdos_posa_property_for_long_directed_cycles
Problem attributed to: Havet, Frédéric, Maia, Ana Karolinna (posted 2013-06-25)

=== Problem statement (OpenProblemGarden) ===
Title: Erdős-Posa property for long directed cycles
Conjecture Let $ \ell \geq 2 $ be an integer. For every integer $ n\geq 0 $ , there exists an integer $ t_n=t_n(\ell) $ such that for every digraph $ D $ , either $ D $ has a $ n $ pairwise-disjoint directed cycles of length at least $ \ell $ , or there exists a set $ T $ of at most $ t_n $ vertices such that $ D-T $ has no directed cycles of length at least $ \ell $ .

=== Discussion / context (OpenProblemGarden) ===
The case $ \ell=2 $ has been proved by Reed et al. [RRST], hence solving a conjecture of Gallai [G] and Younger [Y]. The case $ \ell=2 $ and $ n=2 $ has previously been solved by McCuaig [M], who proved that $ t_2(2)=3 $ . Havet and Maia [HM] proved the case $ \ell=3 $ . The analogous statement for undirected graph has been proved by Birmelé, Bondy and Reed [BBR], hence generalizing Erdős-Posa [EP] result for $ \ell =3 $ .

=== References listed by OpenProblemGarden ===
- [BBR] E. Birmelé, J.A. Bondy, and B.A. Reed. The Erdos-Posa property for long circuits, Combinatorica, 27(2), 135–145, 2007.
- [EP] P. Erdős and L. Pósa. On the independent circuits contained in a graph. Canad. J. Math., 17, 347--352, 1965.
- [G] T. Gallai. Problem 6, in Theory of Graphs, Proc. Colloq. Tihany 1966 (New York), Academic Press, p.362, 1968.
- *[HM] F. Havet and A. K. Maia. On disjoint directed cycles with prescribed minimum lengths. INRIA Research Report, RR-8286, 2013.
- [M] W. McCuaig, Intercyclic digraphs. Graph Structure Theory, (Neil Robertson and Paul Seymour, eds.), AMS Contemporary Math., 147:203--245, 1993.
- [RRST] B. Reed, N. Robertson, P.D. Seymour, and R. Thomas. Packing directed circuits. Combinatorica, 16(4):535--554, 1996.
- [Y] D. H. Younger. Graphs with interlinked directed circuits. Proceedings of the Midwest Symposium on Circuit Theory, 2:XVI 2.1 - XVI 2.7, 1973.

=== Catalog page (statement + literature review) ===
Erdős-Posa property for long directed cycles — Graph-theory open problems

 
 Status
 solved
 medium confidence
 

 The conjecture was resolved by Kawarabayashi and Kreutzer as an application of their Directed Grid Theorem (STOC 2015 / arXiv:1411.5681): the abstract explicitly states that the directed grid theorem improves the Reed-Robertson-Seymour-Thomas result on disjoint cycles of length at least $\ell$, establishing the Erdős-Pósa property for long directed cycles for every fixed $\ell$. This result is referenced explicitly as the proof of 'the Erdős-Pósa property for long cycles in directed graphs' by Göke, Marx and Mnich (ICALP 2020).

 Cited literature (2)

 
 
 
proof The Directed Grid Theorem
 (2015)
 

 
 Ken-ichi Kawarabayashi, Stephan Kreutzer · STOC 2015 (arXiv:1411.5681) · arXiv:1411.5681

Proves the directed grid theorem and, as an application, establishes the Erdős-Pósa property for disjoint directed cycles of length at least $\ell$, improving Reed-Robertson-Seymour-Thomas (1996); abstract explicitly cites the Open Problem Garden entry.
 

 
 
partial Hitting Long Directed Cycles Is Fixed-Parameter Tractable
 (2020)
 

 
 Alexander Göke, Dániel Marx, Matthias Mnich · ICALP 2020 (arXiv:2003.05267) · arXiv:2003.05267

Gives an FPT algorithm for the Directed Long Cycle Hitting Set problem, described by the authors as an exact version of the approximation algorithm following from the Erdős-Pósa property for long directed cycles proved by Kreutzer and Kawarabayashi (STOC 2015).
 

 

 Reviewer notes. Confidence is medium rather than high because the Kawarabayashi-Kreutzer abstract phrases the long-cycles result as 'improving' the Reed-Robertson-Seymour-Thomas result on disjoint cycles of length at least $\ell$ rather than spelling out an Erdős-Pósa-style theorem in the abstract; however, the Göke-Marx-Mnich ICALP 2020 paper explicitly attributes the proof of 'the Erdős-Pósa property for long cycles in directed graphs' to Kreutzer-Kawarabayashi (STOC 2015), and the Kawarabayashi-Kreutzer abstract explicitly references the OPG entry, which together strongly support that the conjecture is solved. The exact bound $t_n(\ell)$ from the directed grid theorem is non-elementary in $n$.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Let $ \ell \geq 2 $ be an integer. For every integer $ n\geq 0 $ , there exists an integer $ t_n=t_n(\ell) $ such that for every digraph $ D $ , either $ D $ has a $ n $ pairwise-disjoint directed cycles of length at least $ \ell $ , or there exists a set $ T $ of at most $ t_n $ vertices such that $ D-T $ has no directed cycles of length at least $ \ell $ .

Discussion

The case $ \ell=2 $ has been proved by Reed et al. [RRST], hence solving a conjecture of Gallai [G] and Younger [Y]. The case $ \ell=2 $ and $ n=2 $ has previously been solved by McCuaig [M], who proved that $ t_2(2)=3 $ . Havet and Maia [HM] proved the case $ \ell=3 $ . The analogous statement for undirected graph has been proved by Birmelé, Bondy and Reed [BBR], hence generalizing Erdős-Posa [EP] result for $ \ell =3 $ .

Bibliography

 [BBR]
 E. Birmelé, J.A. Bondy, and B.A. Reed. The Erdos-Posa property for long circuits, Combinatorica, 27(2), 135–145, 2007.

 [EP]
 P. Erdős and L. Pósa. On the independent circuits contained in a graph. Canad. J. Math., 17, 347--352, 1965.

 [G]
 T. Gallai. Problem 6, in Theory of Graphs, Proc. Colloq. Tihany 1966 (New York), Academic Press, p.362, 1968.

★ [HM]
 F. Havet and A. K. Maia. On disjoint directed cycles with prescribed minimum lengths . INRIA Research Report, RR-8286, 2013.
 On disjoint directed cycles with prescribed minimum lengths

 [M]
 W. McCuaig, Intercyclic digraphs. Graph Structure Theory, (Neil Robertson and Paul Seymour, eds.), AMS Contemporary Math., 147:203--245, 1993.

 [RRST]
 B. Reed, N. Robertson, P.D. Seymour, and R. Thomas. Packing directed circuits . Combinatorica, 16(4):535--554, 1996.
 Packing directed circuits

 [Y]
 D. H. Younger. Graphs with interlinked directed circuits. Proceedings of the Midwest Symposium on Circuit Theory, 2:XVI 2.1 - XVI 2.7, 1973.
