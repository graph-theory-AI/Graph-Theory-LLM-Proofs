Attack the following open graph-theory problem.

Catalog id: intersecting_two_perfect_matchings
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Matchings
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/intersecting_two_perfect_matchings/
Original entry: http://www.openproblemgarden.org/op/intersecting_two_perfect_matchings
Problem attributed to: Macajova, Edita, Skoviera, Martin (posted 2007-08-30)

=== Problem statement (OpenProblemGarden) ===
Title: The intersection of two perfect matchings
Conjecture Every bridgeless cubic graph has two perfect matchings $ M_1 $ , $ M_2 $ so that $ M_1 \cap M_2 $ does not contain an odd edge-cut.

=== Discussion / context (OpenProblemGarden) ===
Let $ G = (V,E) $ be a bridgeless cubic graph. A binary cycle (henceforth called cycle ) is a set $ C \subseteq E $ so that every vertex of $ (V,C) $ has even degree (equivalently, a cycle is any member of the binary cycle space). A postman join is a set $ J \subseteq E $ so that $ E \setminus J $ is a cycle. Note that since $ G $ is cubic, every perfect matching is a postman join. Next we state a well-known theorem of Jaeger in three equivalent forms. Theorem (Jaeger's 8-flow theorem) \item $ G $ has a nowhere-zero flow in the group $ {\mathbb Z}_2^3 $ . \item $ G $ has three cycles $ C_1,C_2,C_3 $ so that $ C_1 \cup C_2 \cup C_3 = E $ . \item $ G $ has three postman joins $ J_1,J_2,J_3 $ so that $ J_1 \cap J_2 \cap J_3 = \emptyset $ . The last of these statements is interesting, since The Berge Fulkerson Conjecture (if true) implies the following: Conjecture $ G $ has three perfect matchings $ M_1,M_2,M_3 $ so that $ M_1 \cap M_2 \cap M_3= \emptyset $ . So, we know that $ G $ has three postman joins $ J_1,J_2,J_3 $ with empty intersection, and it is conjectured that $ J_1,J_2,J_3 $ may be chosen so that each is a perfect matching, but now we see two statements in between the theorem and the conjecture. Namely, is it true that $ J_1,J_2,J_3 $ may be chosen so that one is a perfect matching? or two? The first of these was solved recently. Theorem (Macajova, Skoviera) $ G $ has two postman sets $ J_1,J_2 $ and one perfect matching $ M $ so that $ M \cap J_1 \cap J_2 = \emptyset $ The second of these asks for two perfect matchings $ M_1,M_2 $ and one postman join $ J $ so that $ M_1 \cap M_2 \cap J = \emptyset $ . It is an easy exercise to show that a set $ S \subseteq E $ contains a postman join if an only if $ S $ has nonempty intersection with every odd edge-cut. Therefore, finding two perfect matchings and one postman join with empty common intersection is precisely equivalent to the conjecture at the start of this page - find two perfect matchings whose intersection contains no odd edge-cut.

=== References listed by OpenProblemGarden ===
- * Edita Macajova, Martin Skoviera, Fano colourings of cubic graphs and the Fulkerson conjecture. Theoret. Comput. Sci. 349 (2005), no. 1, 112--120. MathSciNet

=== Catalog page (statement + literature review) ===
The intersection of two perfect matchings — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The Mácajová–Škoviera conjecture — that every bridgeless cubic graph has two perfect matchings $M_1, M_2$ with $M_1 \cap M_2$ containing no odd edge-cut — remains open. Fouquet and Vanherpe (2010) proved it for cubic graphs with few vertices and for traceable graphs. Related conjectures in the same research programme (notably Mazzuoccolo's conjecture that two perfect matchings whose deletion yields a bipartite subgraph, proved by Kardoš, Máčajová, and Zerafa in 2023) have since been resolved, but the original conjecture as stated is unresolved.

 Cited literature (2)

 
 
 
partial Mácajová and Škoviera Conjecture on Cubic Graphs
 (2010)
 

 
 Jean-Luc Fouquet, Jean-Marie Vanherpe · Discussiones Mathematicae Graph Theory · arXiv:0809.4839

Proves the conjecture for cubic graphs with a bounded number of vertices and gives a stronger result for traceable cubic graphs.
 

 
 
partial Disjoint odd circuits in a bridgeless cubic graph can be quelled by a single perfect matching
 (2023)
 

 
 František Kardoš, Edita Máčajová, Jean Paul Zerafa · Journal of Combinatorial Theory, Series B · arXiv:2204.10021

Proves Mazzuoccolo's conjecture that every bridgeless cubic graph admits two perfect matchings whose deletion yields a bipartite subgraph — a related result in the same research programme between Jaeger's 8-flow theorem and the Berge–Fulkerson conjecture, but distinct from the Mácajová–Škoviera conjecture about the intersection avoiding an odd edge-cut.
 

 

 Reviewer notes. The OPG page (openproblemgarden.org) was unreachable (ECONNREFUSED). The DMGT journal page for the Fouquet–Vanherpe article (dmgt.uz.zgora.pl) returned an SSL error and could not be verified. The Kardoš–Máčajová–Zerafa 2023 paper proves Mazzuoccolo's bipartite conjecture (G − M1 − M2 bipartite), which is at a different level in the hierarchy than the Mácajová–Škoviera conjecture (M1 ∩ M2 has no odd edge-cut). No post-2010 paper specifically resolving the Mácajová–Škoviera conjecture was found in 5 searches; it is assessed as still open with partial results.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. Every bridgeless cubic graph has two perfect matchings $ M_1 $ , $ M_2 $ so that $ M_1 \cap M_2 $ does not contain an odd edge-cut.

Keywords:
cubic · nowhere-zero flow · perfect matching

Discussion

Let $ G = (V,E) $ be a bridgeless cubic graph. A binary cycle (henceforth called cycle ) is a set $ C \subseteq E $ so that every vertex of $ (V,C) $ has even degree (equivalently, a cycle is any member of the binary cycle space). A postman join is a set $ J \subseteq E $ so that $ E \setminus J $ is a cycle. Note that since $ G $ is cubic, every perfect matching is a postman join. Next we state a well-known theorem of Jaeger in three equivalent forms. Theorem (Jaeger's 8-flow theorem) \item $ G $ has a nowhere-zero flow in the group $ {\mathbb Z}_2^3 $ . \item $ G $ has three cycles $ C_1,C_2,C_3 $ so that $ C_1 \cup C_2 \cup C_3 = E $ . \item $ G $ has three postman joins $ J_1,J_2,J_3 $ so that $ J_1 \cap J_2 \cap J_3 = \emptyset $ . The last of these statements is interesting, since The Berge Fulkerson Conjecture (if true) implies the following: Conjecture $ G $ has three perfect matchings $ M_1,M_2,M_3 $ so that $ M_1 \cap M_2 \cap M_3= \emptyset $ . So, we know that $ G $ has three postman joins $ J_1,J_2,J_3 $ with empty intersection, and it is conjectured that $ J_1,J_2,J_3 $ may be chosen so that each is a perfect matching, but now we see two statements in between the theorem and the conjecture. Namely, is it true that $ J_1,J_2,J_3 $ may be chosen so that one is a perfect matching? or two? The first of these was solved recently. Theorem (Macajova, Skoviera) $ G $ has two postman sets $ J_1,J_2 $ and one perfect matching $ M $ so that $ M \cap J_1 \cap J_2 = \emptyset $ The second of these asks for two perfect matchings $ M_1,M_2 $ and one postman join $ J $ so that $ M_1 \cap M_2 \cap J = \emptyset $ . It is an easy exercise to show that a set $ S \subseteq E $ contains a postman join if an only if $ S $ has nonempty intersection with every odd edge-cut. Therefore, finding two perfect matchings and one postman join with empty common intersection is precisely equivalent to the conjecture at the start of this page - find two perfect matchings whose intersection contains no odd edge-cut.

Bibliography

★ [?]
 Edita Macajova, Martin Skoviera, Fano colourings of cubic graphs and the Fulkerson conjecture. Theoret. Comput. Sci. 349 (2005), no. 1, 112--120. MathSciNet
 MathSciNet

Related conjectures

 
 implied by
 The Berge-Fulkerson conjecture
 partial
 Rigorous: any perfect matching meets every odd edge-cut delta(X) in an odd (hence >=1) number of edges, since the odd set X cannot be perfectly matched internally. Given a Fulkerson cover M1..M6 with every edge in exactly two matchings, if an odd cut C were contained in M1 cap M2, every edge of C would already have both its memberships used by M1 and M2, forcing M3 cap C to be empty -- contradicting that the perfect matching M3 meets C. So M1 cap M2 contains no odd edge-cut, which is exactly the target. Direction correct: Berge-Fulkerson is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
