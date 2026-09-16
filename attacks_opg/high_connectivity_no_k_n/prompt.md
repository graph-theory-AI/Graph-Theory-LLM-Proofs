Attack the following open graph-theory problem.

Catalog id: high_connectivity_no_k_n
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Minors
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/high_connectivity_no_k_n/
Original entry: http://www.openproblemgarden.org/op/high_connectivity_no_k_n
Problem attributed to: Thomas, Robin (posted 2007-03-10)

=== Problem statement (OpenProblemGarden) ===
Title: Highly connected graphs with no K_n minor
Problem Is it true for all $ n \ge 0 $ , that every sufficiently large $ n $ - connected graph without a $ K_n $ minor has a set of $ n-5 $ vertices whose deletion results in a planar graph ?

=== Discussion / context (OpenProblemGarden) ===
A famous conjecture of Jorgensen asserts that every 6-connected graph without a $ K_6 $ -minor is apex (planar plus one vertex). If true, Jorgensen's conjecture does not generalize (naively) to higher connectivities, since for sufficiently large $ n $ , there do exist $ n $ -connected graphs which are not close to planar in the sense we are considering (many more than $ n-5 $ vertices must be deleted to leave a planar graph). This conjecture of Thomas asserts that all such graphs are small in size. For $ n \le 6 $ this conjecture is true. For $ n \le 4 $ this conjecture is trivial, since any graph without a $ K_4 $ -minor is planar. The $ n=5 $ case follows from a theorem of Wagner which gives a construction for all graphs without $ K_5 $ -minors (and from which it follows that every 4-connected graph with no $ K_5 $ minor is planar). The $ n=6 $ case was recently resolved by DeVos, Hegde, Kawarabayashi, Norine, Thomas, and Wollan. The difficulties associated with finding $ K_n $ minors in graphs make this conjecture appear daunting, but if true, it would yield powerful insight into the structure of graphs.

=== Catalog page (statement + literature review) ===
Highly connected graphs with no K_n minor — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Thomas's question (whether every sufficiently large $n$-connected graph without a $K_n$ minor has $n-5$ vertices whose deletion leaves a planar graph) remains open for $n \ge 7$. The crucial $n=6$ case — Jorgensen's conjecture, that every 6-connected graph with no $K_6$ minor is apex — was verified for *sufficiently large* graphs by Kawarabayashi, Norine, Thomas, and Wollan (2012). It was also proved for graphs of order 12 (Albar–Gonçalves, 2020) and for graphs of girth at least 6, but the full Jorgensen conjecture for all 6-connected graphs is still unresolved.

 Cited literature (2)

 
 
 
partial K_6 minors in large 6-connected graphs
 (2012)
 

 
 Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan · arXiv preprint (later in J. Combin. Theory Ser. B) · arXiv:1203.2192

Proves Jorgensen's conjecture (=$n=6$ case of Thomas's question) for all sufficiently large 6-connected graphs.
 

 
 
partial K_6 minors in 6-connected graphs of bounded tree-width
 (2012)
 

 
 Ken-ichi Kawarabayashi, Serguei Norine, Robin Thomas, Paul Wollan · arXiv preprint (later in J. Combin. Theory Ser. B) · arXiv:1203.2171

Companion paper: verifies the apex conclusion for sufficiently large 6-connected graphs of bounded tree-width.
 

 

 Reviewer notes. The $n \le 6$ cases of Thomas's question (and Jorgensen's conjecture for sufficiently large graphs) are settled; no progress toward $n \ge 7$ surfaced in the searches. Albar–Gonçalves's order-12 result and the girth ≥ 6 result are mentioned in search summaries but were not separately verified.

 
 Auto-reviewed 2026-05-08 with claude (main agent, web search + fetch) (web search enabled).
 

Problem. Is it true for all $ n \ge 0 $ , that every sufficiently large $ n $ - connected graph without a $ K_n $ minor has a set of $ n-5 $ vertices whose deletion results in a planar graph ?

Keywords:
connectivity · minor

Discussion

A famous conjecture of Jorgensen asserts that every 6-connected graph without a $ K_6 $ -minor is apex (planar plus one vertex). If true, Jorgensen's conjecture does not generalize (naively) to higher connectivities, since for sufficiently large $ n $ , there do exist $ n $ -connected graphs which are not close to planar in the sense we are considering (many more than $ n-5 $ vertices must be deleted to leave a planar graph). This conjecture of Thomas asserts that all such graphs are small in size. For $ n \le 6 $ this conjecture is true. For $ n \le 4 $ this conjecture is trivial, since any graph without a $ K_4 $ -minor is planar. The $ n=5 $ case follows from a theorem of Wagner which gives a construction for all graphs without $ K_5 $ -minors (and from which it follows that every 4-connected graph with no $ K_5 $ minor is planar). The $ n=6 $ case was recently resolved by DeVos, Hegde, Kawarabayashi, Norine, Thomas, and Wollan. The difficulties associated with finding $ K_n $ minors in graphs make this conjecture appear daunting, but if true, it would yield powerful insight into the structure of graphs.
