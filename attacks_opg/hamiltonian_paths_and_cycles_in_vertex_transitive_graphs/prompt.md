Attack the following open graph-theory problem.

Catalog id: hamiltonian_paths_and_cycles_in_vertex_transitive_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Algebraic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/hamiltonian_paths_and_cycles_in_vertex_transitive_graphs/
Original entry: http://www.openproblemgarden.org/op/hamiltonian_paths_and_cycles_in_vertex_transitive_graphs
Problem attributed to: Lovasz, Laszlo (posted 2007-03-18)

=== Problem statement (OpenProblemGarden) ===
Title: Hamiltonian paths and cycles in vertex transitive graphs
Problem Does every connected vertex-transitive graph have a Hamiltonian path ?

=== Discussion / context (OpenProblemGarden) ===
The question posed here is due to Lovasz [L], but the general problem of finding Hamiltonian paths and cycles in highly symmetric graphs is much older. Knuth has traced it back to bell ringing , and it appears again in gray codes and in the knight's tour of a chessboard. Vertex-transitive graphs are, of course, very special, very well-behaved graphs, and it seems unsurprising that many of them have Hamiltonian cycles. What is surprising is that there are only five connected ones known which do not have Hamiltonian cycles. This list consists of the complete graph on 2 vertices, the Petersen graph , Coxeter's graph , and the graphs obtained from Petersen and Coxeter by truncating every vertex (inflate each vertex to a triangle). In particular, we do not know of a vertex transitive graph without a Hamiltonian path. Interestingly, there seems to be considerable disagreement among experts as to what the answer will be. On one hand, there does not appear to be any particular reason why vertex-transitive graphs should almost always have Hamiltonian cycles. On the other hand, such graphs have been studied and searched for at great length, and so far every one investigated with the exception of the five listed above has proved to have a Hamiltonian cycle. Babai formulated the following conjecture which is in quite sharp contrast to the problem above. Conjecture (Babai [B96]) There exists $ \epsilon > 0 $ so that there are infinitely many connected vertex-transitive graphs $ G $ with longest cycle of length $ <(1-\epsilon)|V(G)| $ . For general vertex-transitive graphs, very little is known. Babai [B79] has shown that a vertex-transitive graph on $ n $ vertices has a cycle of length $ \ge \sqrt{3n} $ , but (though a very clever arguement) this is obviously quite far from the conjecture. Considerable attention has been given to the special case of Cayley graphs . Here we have the following conjecture. Conjecture Every connected Cayley graph (apart from $ K_2 $ ) has a Hamiltonian cycle. The above conjecture is not difficult to prove for abelian groups. Witte [W] proved it for $ p $ -groups, and it has also been established for certain special types of generating sets. Two other results of note are a theorem of Pak-Radocic [PR] showing that every group $ G $ has a generating set of size $ \le \log_2(|G|) $ for which the corresponding Cayley graph is Hamiltonian, and a theorem of Krivelevich-Sudakov [KS] showing that almost surely taking a random set of $ \log^5(|G|) $ elements of $ G $ as generators yields a Hamiltonian graph.

=== References listed by OpenProblemGarden ===
- [B79] L. Babai, Long cycles in vertex-transitive graphs. J. Graph Theory 3 (1979), no. 3, 301--304. MathSciNet
- [B96] L. Babai, Automorphism groups, isomorphism, reconstruction, in Handbook of Combinatorics, Vol. 2, Elsevier, 1996, 1447-1540. MathSciNet
- [KS] M. Krivelevich and B. Sudakov, Sparse pseudo-random graphs are Hamiltonian. J. Graph Theory 42 (2003), no. 1, 17--33. MathSciNet
- [L] L. Lov\'{a}sz, "Combinatorial structures and their applications", (Proc. Calgary Internat. Conf., Calgary, Alberta, 1969), pp. 243-246, Problem 11, Gordon and Breach, New York, 1970.
- [PR] I. Pak and R. Radocic, Hamiltonian paths in Cayley graphs, preprint
- [W] D. Witte, Cayley digraphs of prime-power order are Hamiltonian. J. Combin. Theory Ser. B 40 (1986), no. 1, 107--112. MathSciNet
- [WG] D. Witte and J.A. Gallian, A survey: Hamiltonian cycles in Cayley graphs. Discrete Math. 51 (1984), no. 3, 293--304. MathSciNet

=== Catalog page (statement + literature review) ===
Hamiltonian paths and cycles in vertex transitive graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Lovász problem remains open in general. Since 2007, significant partial results have been established: all Kneser graphs (except the Petersen graph) are Hamiltonian (Merino–Mütze–Namrata, STOC 2023), and the best-known lower bound on cycle length in connected vertex-transitive graphs has been improved to $\Omega(n^{13/21})$ (Groenland et al., 2024). A 2024 preprint claims a proof for the odd-order case, but it has not appeared in a peer-reviewed venue. The full conjecture—does every connected vertex-transitive graph have a Hamiltonian path?—remains open.

 Cited literature (4)

 
 
 
partial Kneser graphs are Hamiltonian
 (2023)
 

 
 Arturo Merino, Torsten Mütze, Namrata · Proceedings of the 55th Annual ACM Symposium on Theory of Computing (STOC 2023) · arXiv:2212.03918 · doi:10.1145/3564246.3585137

Proves that all Kneser graphs $K(n,k)$ admit a Hamilton cycle, with the sole exception of the Petersen graph $K(5,2)$, resolving a special case of the Lovász conjecture for this infinite family of vertex-transitive graphs.
 

 
 
partial Proof of Lovász conjecture for odd order
 (2024)
 

 
 Misa Nakanishi · arXiv preprint · arXiv:2407.00646

Claims to prove that every connected vertex-transitive graph with an odd number of vertices is Hamiltonian (i.e., has a Hamilton cycle), by showing such graphs possess a 2-factor consisting of an odd number of odd cycles of equal length; not yet peer-reviewed.
 

 
 
partial Longest cycles in vertex-transitive and highly connected graphs
 (2024)
 

 
 Carla Groenland, Sean Longbrake, Raphael Steiner, Jérémie Turcotte, Liana Yepremyan · Bulletin of the London Mathematical Society · arXiv:2408.04618 · doi:10.1112/blms.70134

Proves every connected vertex-transitive graph on $n \geq 3$ vertices contains a cycle of length at least $\Omega(n^{13/21})$, improving the longstanding $\Omega(n^{3/5})$ bound due to DeVos.
 

 
 
partial The Lovász conjecture holds for moderately dense Cayley graphs
 (2026)
 

 
 Benjamin Bedert, Nemanja Draganić, Alp Müyesser, Matías Pavez-Signé · arXiv preprint · arXiv:2603.08675

Proves that every large connected $n$-vertex Cayley graph with degree $d \geq n^{1-c}$ (for an absolute constant $c > 0$) has a Hamilton cycle, extending the previously known linear-degree threshold without using Szemerédi's regularity lemma.
 

 

 Reviewer notes. The Nakanishi (2024) preprint (2407.00646) claiming to prove the odd-order case has not appeared in a peer-reviewed journal and is not referenced on the Wikipedia Lovász conjecture page (as of early 2026), suggesting caution. The Groenland et al. BLMS publication was confirmed via arXiv page (journal page returned 403). The STOC 2023 DOI for the Kneser paper (10.1145/3564246.3585137) returned 403 but the arXiv abstract fully confirms the result. The directed analogue (Bucić et al., arXiv:2602.16333, 2026) proves $\Omega(n^{1/3})$ cycles in vertex-transitive digraphs — a related but distinct problem. The original undirected Lovász problem (Hamiltonian path in all connected vertex-transitive graphs) remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Problem. Does every connected vertex-transitive graph have a Hamiltonian path ?

Keywords:
cycle · hamiltonian · path · vertex-transitive

Discussion

The question posed here is due to Lovasz [L], but the general problem of finding Hamiltonian paths and cycles in highly symmetric graphs is much older. Knuth has traced it back to bell ringing , and it appears again in gray codes and in the knight's tour of a chessboard. Vertex-transitive graphs are, of course, very special, very well-behaved graphs, and it seems unsurprising that many of them have Hamiltonian cycles. What is surprising is that there are only five connected ones known which do not have Hamiltonian cycles. This list consists of the complete graph on 2 vertices, the Petersen graph , Coxeter's graph , and the graphs obtained from Petersen and Coxeter by truncating every vertex (inflate each vertex to a triangle). In particular, we do not know of a vertex transitive graph without a Hamiltonian path. Interestingly, there seems to be considerable disagreement among experts as to what the answer will be. On one hand, there does not appear to be any particular reason why vertex-transitive graphs should almost always have Hamiltonian cycles. On the other hand, such graphs have been studied and searched for at great length, and so far every one investigated with the exception of the five listed above has proved to have a Hamiltonian cycle. Babai formulated the following conjecture which is in quite sharp contrast to the problem above. Conjecture (Babai [B96]) There exists $ \epsilon > 0 $ so that there are infinitely many connected vertex-transitive graphs $ G $ with longest cycle of length $ <(1-\epsilon)|V(G)| $ . For general vertex-transitive graphs, very little is known. Babai [B79] has shown that a vertex-transitive graph on $ n $ vertices has a cycle of length $ \ge \sqrt{3n} $ , but (though a very clever arguement) this is obviously quite far from the conjecture. Considerable attention has been given to the special case of Cayley graphs . Here we have the following conjecture. Conjecture Every connected Cayley graph (apart from $ K_2 $ ) has a Hamiltonian cycle. The above conjecture is not difficult to prove for abelian groups. Witte [W] proved it for $ p $ -groups, and it has also been established for certain special types of generating sets. Two other results of note are a theorem of Pak-Radocic [PR] showing that every group $ G $ has a generating set of size $ \le \log_2(|G|) $ for which the corresponding Cayley graph is Hamiltonian, and a theorem of Krivelevich-Sudakov [KS] showing that almost surely taking a random set of $ \log^5(|G|) $ elements of $ G $ as generators yields a Hamiltonian graph.

Bibliography

 [B79]
 L. Babai, Long cycles in vertex-transitive graphs. J. Graph Theory 3 (1979), no. 3, 301--304. MathSciNet
 MathSciNet

 [B96]
 L. Babai, Automorphism groups, isomorphism, reconstruction, in Handbook of Combinatorics, Vol. 2, Elsevier, 1996, 1447-1540. MathSciNet
 MathSciNet

 [KS]
 M. Krivelevich and B. Sudakov, Sparse pseudo-random graphs are Hamiltonian . J. Graph Theory 42 (2003), no. 1, 17--33. MathSciNet
 Sparse pseudo-random graphs are Hamiltonian · MathSciNet

 [L]
 L. Lov\'{a}sz, "Combinatorial structures and their applications", (Proc. Calgary Internat. Conf., Calgary, Alberta, 1969), pp. 243-246, Problem 11, Gordon and Breach, New York, 1970.

 [PR]
 I. Pak and R. Radocic, Hamiltonian paths in Cayley graphs , preprint
 Hamiltonian paths in Cayley graphs

 [W]
 D. Witte, Cayley digraphs of prime-power order are Hamiltonian. J. Combin. Theory Ser. B 40 (1986), no. 1, 107--112. MathSciNet
 MathSciNet

 [WG]
 D. Witte and J.A. Gallian, A survey: Hamiltonian cycles in Cayley graphs. Discrete Math. 51 (1984), no. 3, 293--304. MathSciNet
 MathSciNet
