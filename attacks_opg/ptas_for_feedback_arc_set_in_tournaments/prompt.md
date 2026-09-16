Attack the following open graph-theory problem.

Catalog id: ptas_for_feedback_arc_set_in_tournaments
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Graph Algorithms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/ptas_for_feedback_arc_set_in_tournaments/
Original entry: http://www.openproblemgarden.org/op/ptas_for_feedback_arc_set_in_tournaments
Problem attributed to: Ailon, Nir, Alon, Noga (posted 2013-03-15)

=== Problem statement (OpenProblemGarden) ===
Title: PTAS for feedback arc set in tournaments
Question Is there a polynomial time approximation scheme for the feedback arc set problem for the class of tournaments?

=== Discussion / context (OpenProblemGarden) ===
A tournament is an orientation of a complete graph. A feedback arc set is a set of arcs in a digraph whose removal leave the digraph acyclic. The feedback arc set problem consists in finding a feedback arc set of minimum size. A polynomial time approximation scheme is an algorithm which takes an instance of an optimization problem and a parameter $ \epsilon > 0 $ and, in polynomial time, produces a solution that is within a factor $ 1+\epsilon $ of being optimal. The feedback arc set problem has been proved NP-hard. See [ACM, A, CTY, C]. It was shown in [RS] that the feedback arc set problem is fixed parameter tractable for tournaments.

=== References listed by OpenProblemGarden ===
- *[AA] N. Ailon, N. Alon, link, Inform. and Comput. 205 (8) (2007) 1117–1129.
- [ACM] N. Alion, M. Charikar, A. Newman, Aggregating inconsistent information: Ranking and clustering, in: Proceedings of the 37th Symposium on the Theory of Computing, STOC, ACM Press, 2005, pp. 684–693.
- [A] N. Alon, Ranking tournaments, SIAM J. Discrete Math. 20 (2006) 137–142.
- [CTY] P. Charbit, P. Thomassé, A. Yeo, The minimum Feedback arc set problem is NP-hard for tournaments, Combin. Probab. Comput. 16 (1) (2007) 1–4.
- [C] V. Conitzer, Computing Slater rankings using similarities among candidates, in: Proceedings, The Twenty-First National Conference on Artificial Intelligence and the Eighteenth Innovative Applications of Artificial Intelligence Conference, July 16–20, AAAI Press, Boston, Massachusetts, USA, 2006.
- [RS] V. Raman, S. Saurabh, Parameterized complexity of directed feedback arc set problems in tournaments, in: Algorithms and Data Structures, in: Lecture Notes in Computer Science, vol. 2748, Springer, Berlin, 2003, pp. 484–492.

=== Catalog page (statement + literature review) ===
PTAS for feedback arc set in tournaments — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 The problem of whether a PTAS exists for feedback arc set in tournaments was answered affirmatively by Kenyon-Mathieu and Schudy at STOC 2007 (before the OPG posting), who gave a PTAS for weighted feedback arc set in tournaments. Post-posting, Baweja, Jia, and Woodruff (ITCS 2022) further extended this by giving the first semi-streaming PTAS, achieving a $(1+\varepsilon)$-approximation in $p$ passes using $n^{1+1/p}\cdot\mathrm{poly}((\log n)/\varepsilon)$ space.

 Cited literature (1)

 
 
 
partial An Efficient Semi-Streaming PTAS for Tournament Feedback ArcSet with Few Passes
 (2022)
 

 
 Anubhav Baweja, Justin Jia, David P. Woodruff · 13th Innovations in Theoretical Computer Science Conference (ITCS 2022) · arXiv:2107.07141 · doi:10.4230/LIPIcs.ITCS.2022.16

Gives the first semi-streaming PTAS for minimum feedback arc set on tournaments, achieving a (1+ε)-approximation in polynomial time with p passes in n^{1+1/p}·poly((log n)/ε) space, extending the classical PTAS to the streaming setting.
 

 

 Reviewer notes. The OPG problem appears to have been posted in 2013 despite already being solved: Kenyon-Mathieu and Schudy gave a PTAS for weighted feedback arc set in tournaments at STOC 2007 ('How to rank with few errors'). That 2007 paper cannot appear in since_posted (predates the posting) but is the primary solution; its bibliographic record is verified via DBLP and the PTAS claim is verified via an accessible paper mirror. The ACM DL page (doi:10.1145/1250790.1250806) is closed-access. The status 'solved' reflects that the question 'Is there a PTAS?' has a definitive yes answer.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Question. Is there a polynomial time approximation scheme for the feedback arc set problem for the class of tournaments?

Keywords:
feedback arc set · PTAS · tournament

Discussion

A tournament is an orientation of a complete graph. A feedback arc set is a set of arcs in a digraph whose removal leave the digraph acyclic. The feedback arc set problem consists in finding a feedback arc set of minimum size. A polynomial time approximation scheme is an algorithm which takes an instance of an optimization problem and a parameter $ \epsilon > 0 $ and, in polynomial time, produces a solution that is within a factor $ 1+\epsilon $ of being optimal. The feedback arc set problem has been proved NP-hard. See [ACM, A, CTY, C]. It was shown in [RS] that the feedback arc set problem is fixed parameter tractable for tournaments.

Bibliography

★ [AA]
 N. Ailon, N. Alon, link , Inform. and Comput. 205 (8) (2007) 1117–1129.
 link

 [ACM]
 N. Alion, M. Charikar, A. Newman, Aggregating inconsistent information: Ranking and clustering, in: Proceedings of the 37th Symposium on the Theory of Computing, STOC, ACM Press, 2005, pp. 684–693.

 [A]
 N. Alon, Ranking tournaments, SIAM J. Discrete Math. 20 (2006) 137–142.

 [CTY]
 P. Charbit, P. Thomassé, A. Yeo, The minimum Feedback arc set problem is NP-hard for tournaments, Combin. Probab. Comput. 16 (1) (2007) 1–4.

 [C]
 V. Conitzer, Computing Slater rankings using similarities among candidates, in: Proceedings, The Twenty-First National Conference on Artificial Intelligence and the Eighteenth Innovative Applications of Artificial Intelligence Conference, July 16–20, AAAI Press, Boston, Massachusetts, USA, 2006.

 [RS]
 V. Raman, S. Saurabh, Parameterized complexity of directed feedback arc set problems in tournaments, in: Algorithms and Data Structures, in: Lecture Notes in Computer Science, vol. 2748, Springer, Berlin, 2003, pp. 484–492.
