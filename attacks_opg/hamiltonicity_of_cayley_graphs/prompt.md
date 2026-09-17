Attack the following open graph-theory problem.

Catalog id: hamiltonicity_of_cayley_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/hamiltonicity_of_cayley_graphs/
Original entry: http://www.openproblemgarden.org/op/hamiltonicity_of_cayley_graphs
Problem attributed to: Rapaport-Strasser, E. (posted 2008-09-25)

=== Problem statement (OpenProblemGarden) ===
Title: Hamiltonicity of Cayley graphs
Question Is every Cayley graph Hamiltonian?

=== Discussion / context (OpenProblemGarden) ===
This problem seems to have been first considered by Rapaport-Strasser [R]. Lovasz [L] conjectured more generally that every vertex-transitive graph is Hamiltonian. For a survey of results up to 1996, see [CG]. Although many specific Cayley graphs have been shown to be Hamiltonian, there are few general results. One exception is the theorem by Pak and Radoičić [PR] that every finite group $ G $ with at least three elements has a generating set $ S $ of size $ |S| \le \log_2|G| $ , such that the corresponding Cayley graph is Hamiltonian.

=== References listed by OpenProblemGarden ===
- [CG] S. J. Curran, J. A. Gallian, Hamiltonian cycles and paths in Cayley graphs and digraphs—a survey, Discrete Math. 156 (1996), 1–18.
- [L] L. Lovasz, Problem 11, in “Combinatorial structures and their applications,” University of Calgary, Calgary, Alberta, Canada (1970), Gordon and Breach, New York.
- [PR] I. Pak and R. Radoičić, Hamiltonian paths in Cayley graphs, preprint.
- *[R] E. Rapaport-Strasser, Cayley color groups and Hamilton lines, Scripta Math. 24 (1959), 51–58.

=== Catalog page (statement + literature review) ===
Hamiltonicity of Cayley graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The question of whether every Cayley graph is Hamiltonian remains open in general. Since the problem was posted, Groenland et al. proved that every connected vertex-transitive graph on $n$ vertices contains a cycle of length $\Omega(n^{13/21})$; a 2024 preprint by Nakanishi claims to prove Hamiltonicity for all odd-order connected vertex-transitive graphs (hence all Cayley graphs of odd-order groups), though the preprint remains unreviewed; and Bedert et al. (2026) established the conjecture for all Cayley graphs of degree $d \ge n^{1-c}$.

 Cited literature (3)

 
 
 
partial Longest cycles in vertex-transitive and highly connected graphs
 (2024)
 

 
 Carla Groenland, Sean Longbrake, Raphael Steiner, Jérémie Turcotte, Liana Yepremyan · Bulletin of the London Mathematical Society · arXiv:2408.04618

Improves the lower bound on the longest cycle in a connected vertex-transitive graph on $n$ vertices from $\Omega(n^{3/5})$ to $\Omega(n^{13/21})$.
 

 
 
partial Proof of Lovász conjecture for odd order
 (2024)
 

 
 Misa Nakanishi · arXiv preprint · arXiv:2407.00646

Claims to prove that every connected vertex-transitive graph with an odd number of vertices (in particular every Cayley graph of a group of odd order) is Hamiltonian; unreviewed preprint as of May 2026.
 

 
 
partial The Lovász conjecture holds for moderately dense Cayley graphs
 (2026)
 

 
 Benjamin Bedert, Nemanja Draganić, Alp Müyesser, Matías Pavez-Signé · arXiv preprint · arXiv:2603.08675

Proves that every large connected $n$-vertex Cayley graph of degree $d \ge n^{1-c}$ (for an absolute constant $c \ge 1/200$) has a Hamilton cycle, improving the previously required linear-degree threshold.
 

 

 Reviewer notes. The Nakanishi preprint (2407.00646) is unreviewed as of May 2026; if correct it resolves the odd-order case for the strictly stronger Hamiltonicity question (cycle, not just path). The OPG problem asks for a Hamiltonian cycle, which is stronger than the Lovász conjecture (Hamiltonian path); partial results here are cited for vertex-transitive graphs since every Cayley graph is vertex-transitive. Groenland et al. appeared in Bulletin of the London Mathematical Society (October 2025, DOI 10.1112/blms.70134 per search result) but only the arXiv URL was directly verified. The Pak–Radoičić paper was published as Discrete Math. 309(17):5501–5508 (2009) but the result was already cited as a known preprint in the OPG problem statement and is excluded from since_posted.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Question. Is every Cayley graph Hamiltonian?

Discussion

This problem seems to have been first considered by Rapaport-Strasser [R]. Lovasz [L] conjectured more generally that every vertex-transitive graph is Hamiltonian. For a survey of results up to 1996, see [CG]. Although many specific Cayley graphs have been shown to be Hamiltonian, there are few general results. One exception is the theorem by Pak and Radoičić [PR] that every finite group $ G $ with at least three elements has a generating set $ S $ of size $ |S| \le \log_2|G| $ , such that the corresponding Cayley graph is Hamiltonian.

Bibliography

 [CG]
 S. J. Curran, J. A. Gallian, Hamiltonian cycles and paths in Cayley graphs and digraphs—a survey, Discrete Math. 156 (1996), 1–18.

 [L]
 L. Lovasz, Problem 11, in “Combinatorial structures and their applications,” University of Calgary, Calgary, Alberta, Canada (1970), Gordon and Breach, New York.

 [PR]
 I. Pak and R. Radoičić, Hamiltonian paths in Cayley graphs , preprint.
 Hamiltonian paths in Cayley graphs

★ [R]
 E. Rapaport-Strasser, Cayley color groups and Hamilton lines, Scripta Math. 24 (1959), 51–58.
