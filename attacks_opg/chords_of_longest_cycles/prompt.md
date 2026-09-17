Attack the following open graph-theory problem.

Catalog id: chords_of_longest_cycles
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/chords_of_longest_cycles/
Original entry: http://www.openproblemgarden.org/op/chords_of_longest_cycles
Problem attributed to: Thomassen, Carsten (posted 2007-11-12)

=== Problem statement (OpenProblemGarden) ===
Title: Chords of longest cycles
Conjecture If $ G $ is a 3-connected graph, every longest cycle in $ G $ has a chord.

=== Discussion / context (OpenProblemGarden) ===
A chord of a cycle $ C $ is an edge $ e $ so that $ e \not\in E(C) $ , but both ends of $ e $ are in $ V(C) $ . Longest cycles are of great interest in basic graph theory, and this appealing conjecture suggests a very simple property they should share - at least in 3-connected graphs. In dense graphs, this conjecture is easy to verify - for instance, if $ G $ is Hamiltonian, it is trivially true. More interestingly, Thomassen [T] proved that his conjecture is true for cubic graphs using a clever sufficient condition for Hamiltonicity (based on Thomason's lollipop method) combined with a pretty theorem of Fleischner and Steibitz (cycle plus triangles graphs are 3-colorable). Other work on this conjecture has focused on graphs embedded in surfaces. Zhang [Z] has proved the conjecture for planar graphs of minimum degree four, Li and Zhang have proved the conjecture for graphs in the projective plane of minimum degree four [LZ1] and for 4-connected graphs in the klein bottle or torus [LZ2]. Finally, Kawarabayashi, Niu, and Zhang [KNZ] have shown the conjecture for 4-connected graphs on a fixed surface with sufficiently high face-width.

=== References listed by OpenProblemGarden ===
- [KNZ] K. Kawarabayashi, J. Niu, C. Q. Zhang, Chords of longest circuits in locally planar graphs. European J. Combin. 28 (2007), no. 1, 315--321. MathSciNet
- [LZ1] X. Li, C. Q. Zhang, Chords of longest circuits in 3-connected graphs. Discrete Math. 268 (2003), no. 1-3, 199--206. MathSciNet
- [LZ2] X. Li, C. Q. Zhang, Chords of longest circuits of graphs embedded in torus and Klein bottle. J. Graph Theory 43 (2003), no. 1, 1--23. MathSciNet.
- [T2] C. Thomassen, Chords of longest cycles in cubic graphs. J. Combin. Theory Ser. B 71 (1997), no. 2, 211--214. MathSciNet.
- [Z] C. Q. Zhang, Longest cycles and their chords. J. Graph Theory 11 (1987), no. 4, 521--529. MathSciNet.

=== Catalog page (statement + literature review) ===
Chords of longest cycles — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Thomassen's 1976 conjecture that every longest cycle in a 3-connected graph has a chord remains open in full generality. Post-2007 partial results include: Harvey's 2017 proof for graphs with sufficiently high minimum degree (without requiring 3-connectivity); Wu and Zhang's 2025 proof of both Thomassen's and Harvey's conjectures for graphs whose circumference is at least $n - O(\sqrt{n})$; and additional work on chords passing through specified small vertex/edge sets. Significant results by Birmelé (2008, for $K_{3,3}$-minor-free 3-connected graphs) and Thomassen himself (2018, for 2-connected cubic graphs and the existence of at least one chorded longest cycle when $\delta\ge 4$) were found via search but could not be directly verified through web fetches due to paywalls.

 Cited literature (4)

 
 
 
partial A Cycle of Maximum Order in a Graph of High Minimum Degree has a Chord
 (2017)
 

 
 Daniel J. Harvey · The Electronic Journal of Combinatorics

Proves that every longest cycle in a graph with sufficiently high minimum degree contains a chord (no 3-connectivity hypothesis needed), and introduces the stronger Harvey conjecture for 2-connected graphs with $\delta(G)\ge 3$.
 

 
 
partial Longest cycles and longest chordless cycles in 2-connected graphs
 (2024)
 

 
 Yanan Hu, Chengli Li, Feng Liu · arXiv preprint · arXiv:2410.19005

Proves Harvey's conjecture (which implies Thomassen's) for $\ell$-holed graphs and graphs with small induced circumference, thereby establishing Thomassen's conjecture for these classes.
 

 
 
partial Chords of longest cycles passing through a specified small set
 (2025)
 

 
 Haidong Wu, Shunzhe Zhang · arXiv preprint · arXiv:2502.10657

Proves that in 3-connected planar graphs with $\delta\ge 4$, every longest cycle containing a specified set of three vertices or an edge plus a vertex has a chord; analogous results for 2-connected cubic graphs.
 

 
 
partial Chords of longest cycles in graphs with large circumferences
 (2025)
 

 
 Haidong Wu, Shunzhe Zhang · arXiv preprint · arXiv:2511.03422

Proves both Thomassen's and Harvey's conjectures for graphs whose circumference is at least $n - \frac{1+\sqrt{4n-3}}{2}$ (i.e., close to $n$), without needing the connectivity assumption.
 

 

 Reviewer notes. Two important post-2007 papers appeared in every search but could not be directly verified via WebFetch due to publisher paywalls: (1) Étienne Birmelé, 'Every longest circuit of a 3-connected, K_{3,3}-minor free graph has a chord,' J. Graph Theory 58 (2008) 293–298 (DOI 10.1002/jgt.20312) — this significantly extends Zhang's 1987 planar result by removing the minimum-degree-4 condition; (2) Carsten Thomassen, 'Chords in longest cycles,' J. Combin. Theory Ser. B 129 (2018) 148–157 (DOI 10.1016/j.jctb.2017.09.008) — proves every longest cycle in a 2-connected cubic graph has a chord, and that some longest cycle has a chord in 3-connected graphs with $\delta\ge 4$. Both are widely cited in the verified 2025 arXiv papers and appear consistent across multiple independent search results. A Wang–Yue paper (Discrete Appl. Math. 377 (2025) 541–551) on 3-connected graphs with circumference $\ge n-5$ was also identified but not directly verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 301s.
 

Conjecture. If $ G $ is a 3-connected graph, every longest cycle in $ G $ has a chord.

Keywords:
chord · connectivity · cycle

Discussion

A chord of a cycle $ C $ is an edge $ e $ so that $ e \not\in E(C) $ , but both ends of $ e $ are in $ V(C) $ . Longest cycles are of great interest in basic graph theory, and this appealing conjecture suggests a very simple property they should share - at least in 3-connected graphs. In dense graphs, this conjecture is easy to verify - for instance, if $ G $ is Hamiltonian, it is trivially true. More interestingly, Thomassen [T] proved that his conjecture is true for cubic graphs using a clever sufficient condition for Hamiltonicity (based on Thomason's lollipop method) combined with a pretty theorem of Fleischner and Steibitz (cycle plus triangles graphs are 3-colorable). Other work on this conjecture has focused on graphs embedded in surfaces. Zhang [Z] has proved the conjecture for planar graphs of minimum degree four, Li and Zhang have proved the conjecture for graphs in the projective plane of minimum degree four [LZ1] and for 4-connected graphs in the klein bottle or torus [LZ2]. Finally, Kawarabayashi, Niu, and Zhang [KNZ] have shown the conjecture for 4-connected graphs on a fixed surface with sufficiently high face-width.

Bibliography

 [KNZ]
 K. Kawarabayashi, J. Niu, C. Q. Zhang, Chords of longest circuits in locally planar graphs. European J. Combin. 28 (2007), no. 1, 315--321. MathSciNet
 MathSciNet

 [LZ1]
 X. Li, C. Q. Zhang, Chords of longest circuits in 3-connected graphs. Discrete Math. 268 (2003), no. 1-3, 199--206. MathSciNet
 MathSciNet

 [LZ2]
 X. Li, C. Q. Zhang, Chords of longest circuits of graphs embedded in torus and Klein bottle. J. Graph Theory 43 (2003), no. 1, 1--23. MathSciNet .
 MathSciNet

 [T2]
 C. Thomassen, Chords of longest cycles in cubic graphs. J. Combin. Theory Ser. B 71 (1997), no. 2, 211--214. MathSciNet .
 MathSciNet

 [Z]
 C. Q. Zhang, Longest cycles and their chords. J. Graph Theory 11 (1987), no. 4, 521--529. MathSciNet .
 MathSciNet
