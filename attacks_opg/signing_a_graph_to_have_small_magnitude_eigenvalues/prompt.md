Attack the following open graph-theory problem.

Catalog id: signing_a_graph_to_have_small_magnitude_eigenvalues
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/signing_a_graph_to_have_small_magnitude_eigenvalues/
Original entry: http://www.openproblemgarden.org/op/signing_a_graph_to_have_small_magnitude_eigenvalues
Problem attributed to: Bilu, Yonatan, Linial, Nathan (posted 2013-03-24)

=== Problem statement (OpenProblemGarden) ===
Title: Signing a graph to have small magnitude eigenvalues
Conjecture If $ A $ is the adjacency matrix of a $ d $ -regular graph, then there is a symmetric signing of $ A $ (i.e. replace some $ +1 $ entries by $ -1 $ ) so that the resulting matrix has all eigenvalues of magnitude at most $ 2 \sqrt{d-1} $ .

=== Discussion / context (OpenProblemGarden) ===
A graph $ H $ is a $ k $ - lift of a graph $ G $ if there is a $ k $ -to- $ 1 $ map $ f : V(H) \rightarrow V(G) $ which is locally injective in the sense that the restriction of $ f $ to the neighbourhood of every vertex is an injection. We can construct a random $ k $ -lift of $ G $ with vertex set $ V(G) \times \{1,\ldots,k\} $ by adding a (uniformly chosen) random matching between $ \{v\} \times \{1,\ldots,k\} $ and $ \{w\} \times \{1,\ldots,k\} $ whenever $ vw \in E(G) $ . If $ H $ is a $ k $ -lift of $ G $ , then every eigenvalue of $ G $ will also be an eigenvalue of $ H $ , but in addition $ H $ will have $ (k-1) |V(G)| $ new eigenvalues. There has been considerable interest and investigation into the behaviour of these new eigenvalues for a random $ k $ -lift, since it is expected that they should generally be small in magnitude. In particular, if $ G $ is a Ramanujan graph (a $ d $ -regular graph for which all nontrivial eigenvalues are at most $ 2 \sqrt{d-1} $ ) it may be possible to construct a new Ramanujan graph by taking a suitable $ k $ -lift of $ G $ . A series of increasingly strong results have shown that a random $ k $ -lift of a $ d $ -regular Ramanujan graph will have all new eigenvalues at most $ O(d^{3/4}) $ (Friedman [F]), $ O(d^{2/3}) $ (Linial and Pruder [LP]) and $ O(\sqrt{d} \log d) $ (Lubetzky, Sudakov, and Vu [LSV]). An interesting paper of Bilu and Linial [BL] investigates 2-lifts of graphs. Let $ G $ be a graph and let $ H $ be a 2-lift of $ G $ with vertex set $ V(G) \times \{1,2\} $ as above. Every eigenvector of $ G $ extends naturally to an eigenvector of $ H $ which is constant on each fiber (set of the form $ \{u\} \times \{1,2\} $ ). Thus, we may assume that all of the new eigenvalues are associated with eigenvectors which sum to zero on each fiber. So, each of these new eigenvectors is completely determined by its behaviour on $ V(G) \times \{1\} $ . Now we assign a signature $ \pm 1 $ to each edge of $ G $ to form a signed graph $ G^* $ by assigning each edge $ uv \in E(G) $ for which $ (u,1)(v,1) \in E(H) $ a sign of $ 1 $ and every other edge of $ G $ sign $ -1 $ . It is straightforward to verify that the restriction of any new eigenvector of $ H $ to $ V(G) \times \{1\} $ will then be an eigenvector of $ G^* $ . Thus, the above conjecture is equivalent to the conjecture that every $ d $ -regular graph has a $ 2 $ -lift so that all new eigenvalues have magnitude at most $ 2 \sqrt{d-1} $ . Furthermore, a positive solution to this conjecture for $ d $ -regular Ramanujan graphs would yield families of $ d $ -regular expanders.

=== References listed by OpenProblemGarden ===
- *[BL] Y. Bilu, N. Linial, Lifts, discrepancy and nearly optimal spectral gap, Combinatorica 26 (5) (2006) 495–519. MathSciNet
- [F] J. Friedman, Relative expanders or weakly relatively Ramanujan graphs, Duke Math. J. 118 (1) (2003) 19–35. MathSciNet
- [LP] N. Linial, D. Puder, Word maps and spectra of random graph lifts, Random Structures Algorithms 37 (1) (2010) 100–135. MathSciNet
- [LSV] E. Lubetzky, B. Sudakov, V Vu, Spectra of lifted Ramanujan graphs. Adv. Math. 227 (2011), no. 4, 1612–1645. MathSciNet

=== Catalog page (statement + literature review) ===
Signing a graph to have small magnitude eigenvalues — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Marcus, Spielman, and Srivastava (2015) resolved the conjecture for bipartite $d$-regular graphs: using the method of interlacing polynomials, they proved that every bipartite $d$-regular graph has a 2-lift with all new eigenvalues of magnitude at most $2\sqrt{d-1}$, yielding infinite families of bipartite Ramanujan graphs of every degree $> 2$. Hall, Puder, and Sawin (2018) further extended this to $r$-sheeted coverings for bipartite Ramanujan graphs. However, the original Bilu–Linial conjecture for general (non-bipartite) $d$-regular graphs remains open.

 Cited literature (2)

 
 
 
partial Interlacing families I: Bipartite Ramanujan graphs of all degrees
 (2015)
 

 
 Adam W. Marcus, Daniel A. Spielman, Nikhil Srivastava · Annals of Mathematics · arXiv:1304.4132

Proves the bipartite case of the Bilu–Linial conjecture: every bipartite $d$-regular graph has a 2-lift with all new eigenvalues of magnitude at most $2\sqrt{d-1}$, establishing bipartite Ramanujan graphs of every degree via a new method of interlacing polynomials.
 

 
 
partial Ramanujan Coverings of Graphs
 (2018)
 

 
 Chris Hall, Doron Puder, William F. Sawin · Advances in Mathematics · arXiv:1506.02335

Generalises the MSS bipartite 2-lift result to $r$-sheeted coverings: for every $r \geq 2$ and every bipartite Ramanujan graph $G$, there exists an $r$-covering of $G$ in which all new eigenvalues are bounded by the spectral radius of the universal cover.
 

 

 Reviewer notes. The MSS paper (arXiv April 2013) resolves only the bipartite case of the Bilu–Linial conjecture; the conjecture for general non-bipartite d-regular graphs appears to remain open as of the latest searches. The Hall–Puder–Sawin paper (arXiv June 2015, Advances in Mathematics 2018) extends to r-coverings but still works within the bipartite framework. No post-2018 resolution of the non-bipartite case was found in up to 5 queries.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. If $ A $ is the adjacency matrix of a $ d $ -regular graph, then there is a symmetric signing of $ A $ (i.e. replace some $ +1 $ entries by $ -1 $ ) so that the resulting matrix has all eigenvalues of magnitude at most $ 2 \sqrt{d-1} $ .

Keywords:
eigenvalue · expander · Ramanujan graph · signed graph · signing

Discussion

A graph $ H $ is a $ k $ - lift of a graph $ G $ if there is a $ k $ -to- $ 1 $ map $ f : V(H) \rightarrow V(G) $ which is locally injective in the sense that the restriction of $ f $ to the neighbourhood of every vertex is an injection. We can construct a random $ k $ -lift of $ G $ with vertex set $ V(G) \times \{1,\ldots,k\} $ by adding a (uniformly chosen) random matching between $ \{v\} \times \{1,\ldots,k\} $ and $ \{w\} \times \{1,\ldots,k\} $ whenever $ vw \in E(G) $ . If $ H $ is a $ k $ -lift of $ G $ , then every eigenvalue of $ G $ will also be an eigenvalue of $ H $ , but in addition $ H $ will have $ (k-1) |V(G)| $ new eigenvalues. There has been considerable interest and investigation into the behaviour of these new eigenvalues for a random $ k $ -lift, since it is expected that they should generally be small in magnitude. In particular, if $ G $ is a Ramanujan graph (a $ d $ -regular graph for which all nontrivial eigenvalues are at most $ 2 \sqrt{d-1} $ ) it may be possible to construct a new Ramanujan graph by taking a suitable $ k $ -lift of $ G $ . A series of increasingly strong results have shown that a random $ k $ -lift of a $ d $ -regular Ramanujan graph will have all new eigenvalues at most $ O(d^{3/4}) $ (Friedman [F]), $ O(d^{2/3}) $ (Linial and Pruder [LP]) and $ O(\sqrt{d} \log d) $ (Lubetzky, Sudakov, and Vu [LSV]). An interesting paper of Bilu and Linial [BL] investigates 2-lifts of graphs. Let $ G $ be a graph and let $ H $ be a 2-lift of $ G $ with vertex set $ V(G) \times \{1,2\} $ as above. Every eigenvector of $ G $ extends naturally to an eigenvector of $ H $ which is constant on each fiber (set of the form $ \{u\} \times \{1,2\} $ ). Thus, we may assume that all of the new eigenvalues are associated with eigenvectors which sum to zero on each fiber. So, each of these new eigenvectors is completely determined by its behaviour on $ V(G) \times \{1\} $ . Now we assign a signature $ \pm 1 $ to each edge of $ G $ to form a signed graph $ G^* $ by assigning each edge $ uv \in E(G) $ for which $ (u,1)(v,1) \in E(H) $ a sign of $ 1 $ and every other edge of $ G $ sign $ -1 $ . It is straightforward to verify that the restriction of any new eigenvector of $ H $ to $ V(G) \times \{1\} $ will then be an eigenvector of $ G^* $ . Thus, the above conjecture is equivalent to the conjecture that every $ d $ -regular graph has a $ 2 $ -lift so that all new eigenvalues have magnitude at most $ 2 \sqrt{d-1} $ . Furthermore, a positive solution to this conjecture for $ d $ -regular Ramanujan graphs would yield families of $ d $ -regular expanders.

Bibliography

★ [BL]
 Y. Bilu, N. Linial, Lifts, discrepancy and nearly optimal spectral gap, Combinatorica 26 (5) (2006) 495–519. MathSciNet
 MathSciNet

 [F]
 J. Friedman, Relative expanders or weakly relatively Ramanujan graphs, Duke Math. J. 118 (1) (2003) 19–35. MathSciNet
 MathSciNet

 [LP]
 N. Linial, D. Puder, Word maps and spectra of random graph lifts, Random Structures Algorithms 37 (1) (2010) 100–135. MathSciNet
 MathSciNet

 [LSV]
 E. Lubetzky, B. Sudakov, V Vu, Spectra of lifted Ramanujan graphs. Adv. Math. 227 (2011), no. 4, 1612–1645. MathSciNet
 MathSciNet
