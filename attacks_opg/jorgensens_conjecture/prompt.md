Attack the following open graph-theory problem.

Catalog id: jorgensens_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Minors
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/jorgensens_conjecture/
Original entry: http://www.openproblemgarden.org/op/jorgensens_conjecture
Problem attributed to: Jorgensen, Leif K. (posted 2007-03-10)

=== Problem statement (OpenProblemGarden) ===
Title: Jorgensen's Conjecture
Conjecture Every 6- connected graph without a $ K_6 $ minor is apex (planar plus one vertex).

=== Discussion / context (OpenProblemGarden) ===
For $ n \le 5 $ , the class of graphs with no $ K_n $ minor is very well understood. Simple graphs without $ K_3 $ minors are forests. Graphs without $ K_4 $ minors are called series-parallel graphs , and have a simple construction. Finally, Wagner [W] obtained a construction for all graphs without $ K_5 $ minors. For $ n \ge 6 $ , an explicit characterization of those graphs without $ K_n $ minors appears hopeless. The graph minors project of Robertson and Seymour give a rough structure theorem for such classes, but much remains unknown. In particular, this conjecture and Thomas' conjecture highly connected graphs with no $ K_n $ -minor suggest interesting properties of highly connected graphs without $ K_n $ minors which appear quite difficult to resolve. Part of the interest in graphs without $ K_n $ minors stems from Hadwiger's conjecture (every loopless graph without a $ K_{n+1} $ minor is $ n $ -colorable). Indeed, Wagner's work on graphs with no $ K_5 $ minor was done while studying the $ n=4 $ case of Hadwiger. More recently, Robertson, Seymour, and Thomas [RST] proved Hadwiger's conjecture for $ n=5 $ , and in doing so came somewhat close to proving Jorgensoen's conjecture. The thrust of their argument is to prove that any minimal counterexample to Hadwiger for $ n=5 $ is apex. However, in doing so, they exploit both connectivity and coloring properties of a minimal counterexample. It would appear to be difficult to modify their argument to prove Jorgensen's conjecture. DeVos, Hegde, Kawarabayashi, Norine, Thomas, and Wollan proved this conjecture true for all sufficiently large graphs [KNTWa,KNTWb].

=== References listed by OpenProblemGarden ===
- [RST] N. Robertson, P. D. Seymour, R. Thomas, Hadwiger's conjecture for -free graphs. Combinatorica 13 (1993), no. 3, 279-361. MathSciNet
- [W] K. Wagner Uber eine Eigenschaft der ebenen Komplexe, Math. Ann 114 (1937) 570-590. MathSciNet
- [KNTWa] Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan. minors in 6-connected graphs of bounded tree-width. J. Combinatorial Theory, Series B, 136:1--32, 2019
- [KNTWb] Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan. minors in large 6-connected graphs. J. Combinatorial Theory, Series B, 129:158-203, 2019.

=== Catalog page (statement + literature review) ===
Jorgensen's Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Jørgensen's conjecture has been proved for all *sufficiently large* 6-connected graphs by Kawarabayashi, Norine, Thomas, and Wollan (2019), with a companion paper handling the bounded tree-width case, but the full conjecture for all 6-connected graphs (including small ones) remains open. A 2020 paper by Odeneal and Pavelescu verified the conjecture for the specific case of graphs of order 12.

 Cited literature (3)

 
 
 
partial K6 minors in 6-connected graphs of bounded tree-width
 (2019)
 

 
 Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan · Journal of Combinatorial Theory, Series B · arXiv:1203.2171 · doi:10.1016/j.jctb.2017.09.009

Proves Jørgensen's conjecture for all sufficiently large 6-connected graphs of bounded tree-width, a key step toward the full result.
 

 
 
partial K6 minors in large 6-connected graphs
 (2019)
 

 
 Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan · Journal of Combinatorial Theory, Series B · arXiv:1203.2192 · doi:10.1016/j.jctb.2017.09.010

Proves Jørgensen's conjecture for all sufficiently large 6-connected graphs, establishing that every such graph with no K6 minor is apex.
 

 
 
partial Simple graphs of order 12 and minimum degree 6 contain K6 minors
 (2020)
 

 
 Ryan Odeneal, Andrei Pavelescu · Involve, a Journal of Mathematics · doi:10.2140/involve.2020.13.829

Proves that every simple graph of order 12 with minimum degree 6 contains a K6 minor, verifying Jørgensen's conjecture for graphs of order 12.
 

 

 Reviewer notes. The two Kawarabayashi–Norine–Thomas–Wollan papers (arXiv 2012, journal 2019) are already cited in the OPG problem statement, but are included here as they post-date the 2007 posting. The exact size threshold for 'sufficiently large' is not stated in the abstracts. No post-2020 paper completing the conjecture for all small graphs was found; the conjecture remains open for graphs below the threshold of the KNTW result.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Every 6- connected graph without a $ K_6 $ minor is apex (planar plus one vertex).

Keywords:
connectivity · minor

Discussion

For $ n \le 5 $ , the class of graphs with no $ K_n $ minor is very well understood. Simple graphs without $ K_3 $ minors are forests. Graphs without $ K_4 $ minors are called series-parallel graphs , and have a simple construction. Finally, Wagner [W] obtained a construction for all graphs without $ K_5 $ minors. For $ n \ge 6 $ , an explicit characterization of those graphs without $ K_n $ minors appears hopeless. The graph minors project of Robertson and Seymour give a rough structure theorem for such classes, but much remains unknown. In particular, this conjecture and Thomas' conjecture highly connected graphs with no $ K_n $ -minor suggest interesting properties of highly connected graphs without $ K_n $ minors which appear quite difficult to resolve. Part of the interest in graphs without $ K_n $ minors stems from Hadwiger's conjecture (every loopless graph without a $ K_{n+1} $ minor is $ n $ -colorable). Indeed, Wagner's work on graphs with no $ K_5 $ minor was done while studying the $ n=4 $ case of Hadwiger. More recently, Robertson, Seymour, and Thomas [RST] proved Hadwiger's conjecture for $ n=5 $ , and in doing so came somewhat close to proving Jorgensoen's conjecture. The thrust of their argument is to prove that any minimal counterexample to Hadwiger for $ n=5 $ is apex. However, in doing so, they exploit both connectivity and coloring properties of a minimal counterexample. It would appear to be difficult to modify their argument to prove Jorgensen's conjecture. DeVos, Hegde, Kawarabayashi, Norine, Thomas, and Wollan proved this conjecture true for all sufficiently large graphs [KNTWa,KNTWb].

Bibliography

 [RST]
 N. Robertson, P. D. Seymour, R. Thomas, Hadwiger's conjecture for $ K\sb 6 $ -free graphs . Combinatorica 13 (1993), no. 3, 279-361. MathSciNet
 Hadwiger's conjecture for -free graphs · MathSciNet

 [W]
 K. Wagner Uber eine Eigenschaft der ebenen Komplexe, Math. Ann 114 (1937) 570-590. MathSciNet
 MathSciNet

 [KNTWa]
 Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan. $ K_6 $ minors in 6-connected graphs of bounded tree-width. J. Combinatorial Theory, Series B, 136:1--32, 2019

 [KNTWb]
 Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan. $ K_6 $ minors in large 6-connected graphs. J. Combinatorial Theory, Series B, 129:158-203, 2019.

Related conjectures

 
 implies
 Forcing a $K_6$-minor
 partial
 Scope caveat: the target entry contains two conjectures, and Jorgensen implies only the second one (every 7-connected graph has a K_6 minor), not the first (minimum degree 7 forces a K_6 minor). The implication to the second is rigorous: a 7-connected graph G with no K_6 minor is 6-connected, so by Jorgensen it is apex, i.e. G - v is planar for some vertex v; but G - v is 6-connected (deleting one vertex from a 7-connected graph), and no planar graph is 6-connected since every planar graph has a vertex of degree at most 5. Contradiction. The target's OPG context states this explicitly: 'The second conjecture is implied by Jorgensen's conjecture.' Since the entry's first conjecture implies its second, Jorgensen implies only the weaker half of the entry.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
