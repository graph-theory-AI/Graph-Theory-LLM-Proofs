Attack the following open graph-theory problem.

Catalog id: are_almost_all_graphs_determined_by_their_spectrum
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/are_almost_all_graphs_determined_by_their_spectrum/
Original entry: http://www.openproblemgarden.org/op/are_almost_all_graphs_determined_by_their_spectrum

=== Problem statement (OpenProblemGarden) ===
Title: Are almost all graphs determined by their spectrum?
Problem Are almost all graphs uniquely determined by the spectrum of their adjacency matrix?

=== Discussion / context (OpenProblemGarden) ===
We say that two non-isomorphic graphs are cospectral if their adjacency matrices have the same spectrum (counted with multiplicity). A graph is spectrally determined if no other graphs are cospectral to it. It is unclear to me (M. DeVos) how to attribute this problem, but it was considered already in the 1950's and resonates with the famous problem "Can you hear the shape of a drum?" ([vDH]). A priori, it might seem plausible for all graphs to be spectrally determined.. but this is false. The smallest counterexample is the cospectral pair given by $ K_{1,4} $ and the graph obtained from $ C_4 $ by adding an isolated vertex. Some rich families of cospectral graphs are provided by strongly regular graphs, since any two strongly regular graphs with the same parameters will be cospectral. For the special case of trees, Schwenk proved almost all trees are not spectrally determined. This was sharpened by Godsil and Mckay who showed that almost every tree $ T $ has a cospectral graph $ T' $ so that in addition the complements of $ T $ and $ T' $ are cospectral. Furthermore, an operation called Godsil-Mckay Switching defined by these authors gives a powerful tool to produce general graphs which are cospectral. On the flip side, we seem to have a lack of good tools to prove that a given graph is spectrally determined.

=== References listed by OpenProblemGarden ===
- [vDH] E. R. van Dam and W. H. Haemers, Which graphs are determined by their spectrum?, Linear Algebra and its Applications 373 (2003) 241–272.

=== Catalog page (statement + literature review) ===
Are almost all graphs determined by their spectrum? — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The van Dam–Haemers conjecture that almost all graphs are determined by their adjacency spectrum remains open. The most significant post-posting advance is Koval and Kwan (2024), who proved that at least $e^{cn}$ unlabeled $n$-vertex graphs are determined by their spectrum, breaking the longstanding $e^{c\sqrt{n}}$ barrier but still far short of the conjectured density $\sim 2^{n(n-1)/2}/n!$. A 2026 preprint by Xiang constructs a 'natural' graph matrix (derived from the adjacency matrix) whose spectrum determines random graphs up to isomorphism, resolving a related 2003 question of van Dam and Haemers for a different matrix; and a separate 2026 preprint shows sparse (Erdős–Rényi) graphs are typically NOT determined by their adjacency spectrum, due to pendant-tree obstructions.

 Cited literature (4)

 
 
 
partial Exponentially Many Graphs Are Determined By Their Spectrum
 (2024)
 

 
 Illya Koval, Matthew Kwan · The Quarterly Journal of Mathematics · arXiv:2309.09788 · doi:10.1093/qmath/haae030

Proves that the number of DS $n$-vertex graphs is at least $e^{cn}$ for an absolute constant $c>0$, improving the prior sub-exponential ($e^{c\sqrt{n}}$) bound and answering a question of van Dam and Haemers about exponential lower bounds.
 

 
 
partial Natural graph spectra
 (2026)
 

 
 Ziqing Xiang · arXiv preprint · arXiv:2602.00936

Constructs a natural graph matrix (derived from the adjacency matrix via a double-algebra framework) whose spectrum determines random graphs up to isomorphism, affirmatively answering a 2003 question of van Dam and Haemers — but for a different matrix, not the adjacency matrix itself.
 

 
 
partial Are sparse graphs typically determined by their spectrum?
 (2026)
 

 
 Nils Van de Berg, Alexander Van Werde · arXiv preprint · arXiv:2602.22757

Shows that the giant component of Erdős–Rényi graphs with small average degree is typically cospectral (due to pendant trees), so sparse graphs are generally NOT determined by their adjacency spectrum, while providing evidence that removing pendant trees (passing to the 2-core) restores spectral determination.
 

 
 
survey On Spectral Graph Determination
 (2025)
 

 
 Igal Sason, Noam Krupnik, Suleiman Hamud, Abraham Berman · Mathematics (MDPI) · arXiv:2412.20775

Comprehensive survey of classical and recent advances on spectral characterization of graphs, covering cospectral constructions, DS graph families, and Haemers' conjecture.
 

 

 Reviewer notes. The conjecture (fraction of DS graphs → 1) is not resolved. The Koval–Kwan exponential lower bound is the largest theoretical advance; total DS graphs are still exponentially smaller than all graphs. The Xiang (2026) result resolves a weaker variant (a natural but non-adjacency matrix), so does not close the original problem. The Van de Berg–Van Werde (2026) negative result for sparse graphs does not contradict the conjecture, which is naturally interpreted in the dense/uniform random-graph setting. No paper resolving the full conjecture was found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 115s.
 

Problem. Are almost all graphs uniquely determined by the spectrum of their adjacency matrix?

Keywords:
cospectral · graph invariant · spectrum

Discussion

We say that two non-isomorphic graphs are cospectral if their adjacency matrices have the same spectrum (counted with multiplicity). A graph is spectrally determined if no other graphs are cospectral to it. It is unclear to me (M. DeVos) how to attribute this problem, but it was considered already in the 1950's and resonates with the famous problem "Can you hear the shape of a drum?" ([vDH]). A priori, it might seem plausible for all graphs to be spectrally determined.. but this is false. The smallest counterexample is the cospectral pair given by $ K_{1,4} $ and the graph obtained from $ C_4 $ by adding an isolated vertex. Some rich families of cospectral graphs are provided by strongly regular graphs, since any two strongly regular graphs with the same parameters will be cospectral. For the special case of trees, Schwenk proved almost all trees are not spectrally determined. This was sharpened by Godsil and Mckay who showed that almost every tree $ T $ has a cospectral graph $ T' $ so that in addition the complements of $ T $ and $ T' $ are cospectral. Furthermore, an operation called Godsil-Mckay Switching defined by these authors gives a powerful tool to produce general graphs which are cospectral. On the flip side, we seem to have a lack of good tools to prove that a given graph is spectrally determined.

Bibliography

 [vDH]
 E. R. van Dam and W. H. Haemers, Which graphs are determined by their spectrum?, Linear Algebra and its Applications 373 (2003) 241–272.
