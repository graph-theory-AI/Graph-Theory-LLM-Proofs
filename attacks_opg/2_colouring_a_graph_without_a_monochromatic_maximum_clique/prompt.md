Attack the following open graph-theory problem.

Catalog id: 2_colouring_a_graph_without_a_monochromatic_maximum_clique
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/2_colouring_a_graph_without_a_monochromatic_maximum_clique/
Original entry: http://www.openproblemgarden.org/op/2_colouring_a_graph_without_a_monochromatic_maximum_clique
Problem attributed to: Hoang, Chinh T., McDiarmid, Colin (posted 2013-08-25)

=== Problem statement (OpenProblemGarden) ===
Title: 2-colouring a graph without a monochromatic maximum clique
Conjecture If $ G $ is a non-empty graph containing no induced odd cycle of length at least $ 5 $ , then there is a $ 2 $ -vertex colouring of $ G $ in which no maximum clique is monochromatic.

=== Discussion / context (OpenProblemGarden) ===
A $ 2 $ -division of a graph $ G $ is a partitioning of $ G $ into two subgraphs, neither of which contains a maximum clique. It is known that every perfect graph admits a $ 2 $ -division. Thus, by the Strong Perfect Graph Theorem [CRS], a graph which does not contain an induced copy of an odd cycle of length at least $ 5 $ or its complement has a $ 2 $ -division. Hoàng and McDiarmid [HMcD] also prove that a claw-free graph admits a 2-division if and only if it does not contain an induced odd cycle of length at least $ 5 $ . The conjecture says that this holds for all graphs. This problem was featured as unsolved problem #49 in Bondy and Murty's book "Graph Theory" [BM]. See also a posting on the American Institute of Mathematics website, contributed by Bruce Reed.

=== References listed by OpenProblemGarden ===
- [CRS] Maria Chudnovsky, Neil Robertson, Paul Seymour, Robin Thomas: The strong perfect graph theorem, Ann. of Math. (2) 164 (2006), no. 1, 51--229. MathSciNet
- [HMcD] C.T. Hoàng, C. McDiarmid, On the divisibility of graphs, Discrete Math. 242 (1–3) (2002) 145–156.
- [BM] J. A. Bondy and U. S. R. Murty. Graph theory, volume 244 of Graduate Texts in Mathematics. Springer, New York, 2008.

=== Catalog page (statement + literature review) ===
2-colouring a graph without a monochromatic maximum clique — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Hoàng–McDiarmid conjecture that every odd-hole-free graph admits a 2-division (a vertex partition into two parts each missing a maximum clique) remains open in full generality. Since 2013, several restricted classes of odd-hole-free graphs have been proved to be 2-divisible (the hereditary strengthening): notably (banner, odd hole)-free graphs (Hoàng, 2018), (P₅, C₅)-free graphs (Chudnovsky–Sivaraman, 2019), and graphs forbidding an odd hole together with a dart, racket, or bull (Dong–Song–Xu, 2022). All of these are partial results; no proof covering all odd-hole-free graphs has appeared.

 Cited literature (4)

 
 
 
partial On the structure of (banner, odd hole)-free graphs
 (2018)
 

 
 Chính T. Hoàng · Journal of Graph Theory · arXiv:1510.02324 · doi:10.1002/jgt.22258

Proves that (banner, odd hole)-free graphs are perfectly divisible (a property stronger than 2-divisibility), verifying the conjecture for this class.
 

 
 
partial Perfect divisibility and 2-divisibility
 (2019)
 

 
 Maria Chudnovsky, Vaidy Sivaraman · Journal of Graph Theory · arXiv:1704.06667 · doi:10.1002/jgt.22367

Proves that (P₅, C₅)-free graphs are 2-divisible, and that bull-free graphs that are also odd-hole-free or P₅-free are perfectly divisible, advancing the conjecture for these classes.
 

 
 
partial 2-divisibility of Some Odd Hole Free Graphs
 (2022)
 

 
 Wei Dong, Jia-lei Song, Bao-gang Xu · Acta Mathematicae Applicatae Sinica, English Series · doi:10.1007/s10255-022-1110-8

Proves that {odd hole, H}-free graphs are 2-divisible where H is a dart, a racket, or a bull, verifying the conjecture for three new families of odd-hole-free graphs.
 

 
 
partial On the structure of (dart, odd hole)-free graphs
 (2025)
 

 
 Chính T. Hoàng · arXiv preprint · arXiv:2504.20422

Gives a structural decomposition of (dart, odd hole)-free graphs and a new proof that they are 2-divisible, and further proves they are perfectly divisible.
 

 

 Reviewer notes. The full abstract of Dong–Song–Xu (2022) was not retrievable (Springer paywall; Chinese journal page returned only metadata); the specific claim about dart/racket/bull is supported by search-result summaries and by an explicit attribution in Hoàng (arXiv:2504.20422), which cites Dong–Song–Xu for the (dart, odd hole) result. The Barbados 2025 open-problems PDF was binary-encoded and unreadable by WebFetch, so I could not confirm whether the conjecture is listed there as still open, but all other evidence is consistent with it remaining open. The He–Shi–Wu–Yao preprint (arXiv:2603.09549, 2026) proves (odd hole, hammer, K₂,₃)-free graphs are perfectly divisible, representing yet another incremental special case; it was verified but not included in since_posted as it adds marginal new information beyond the other entries.

 
 Auto-reviewed 2026-05-07 with claude-sonnet-4-6 (web search enabled) · 273s.
 

Conjecture. If $ G $ is a non-empty graph containing no induced odd cycle of length at least $ 5 $ , then there is a $ 2 $ -vertex colouring of $ G $ in which no maximum clique is monochromatic.

Keywords:
maximum clique · Partitioning

Discussion

A $ 2 $ -division of a graph $ G $ is a partitioning of $ G $ into two subgraphs, neither of which contains a maximum clique. It is known that every perfect graph admits a $ 2 $ -division. Thus, by the Strong Perfect Graph Theorem [CRS], a graph which does not contain an induced copy of an odd cycle of length at least $ 5 $ or its complement has a $ 2 $ -division. Hoàng and McDiarmid [HMcD] also prove that a claw-free graph admits a 2-division if and only if it does not contain an induced odd cycle of length at least $ 5 $ . The conjecture says that this holds for all graphs. This problem was featured as unsolved problem #49 in Bondy and Murty's book "Graph Theory" [BM]. See also a posting on the American Institute of Mathematics website, contributed by Bruce Reed.

Bibliography

 [CRS]
 Maria Chudnovsky, Neil Robertson, Paul Seymour, Robin Thomas: The strong perfect graph theorem , Ann. of Math. (2) 164 (2006), no. 1, 51--229. MathSciNet
 The strong perfect graph theorem · MathSciNet

 [HMcD]
 C.T. Hoàng, C. McDiarmid, On the divisibility of graphs, Discrete Math. 242 (1–3) (2002) 145–156.

 [BM]
 J. A. Bondy and U. S. R. Murty. Graph theory, volume 244 of Graduate Texts in Mathematics. Springer, New York, 2008.
