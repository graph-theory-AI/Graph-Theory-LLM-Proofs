Attack the following open graph-theory problem.

Catalog id: infinite_uniquely_hamiltonian_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/infinite_uniquely_hamiltonian_graphs/
Original entry: http://www.openproblemgarden.org/op/infinite_uniquely_hamiltonian_graphs
Problem attributed to: Mohar, Bojan (posted 2007-07-24)

=== Problem statement (OpenProblemGarden) ===
Title: Infinite uniquely hamiltonian graphs
Problem Are there any uniquely hamiltonian locally finite 1-ended graphs which are regular of degree $ r > 2 $ ?

=== Discussion / context (OpenProblemGarden) ===
(Originally appeared as [M].) Let $ G $ be a locally finite infinite graph and let $ I(G) $ be the set of ends of~ $ G $ . The Freudenthal compactification of $ G $ is the topological space $ |G| $ which is obtained from the usual topological space of the graph, when viewed as a 1-dimensional cell complex, by adding all points of $ I(G) $ and setting, for each end $ t \in I(G) $ , the basic set of neighborhoods of $ t $ to consist of sets of the form $ C(S, t) \cup I(S,t) \cup E'(S,t) $ , where $ S $ ranges over the finite subsets of $ V(G) $ , $ C(S, t) $ is the component of $ G - S $ containing all rays in $ t $ , the set $ I(S,t) $ contains all ends in $ I(G) $ having rays in $ C(S, t) $ , and $ E'(S,t) $ is the union of half-edges $ (z,y] $ , one for every edge $ xy $ joining $ S $ and $ C(S,t) $ . We define a hamilton circle in $ |G| $ as a homeomorphic image $ C $ of the unit circle $ S^1 $ into $ |G| $ such that every vertex (and hence every end) of $ G $ appears in $ C $ . More details about these notions can be found in [D]. A graph $ G $ (finite or infinite) is said to be uniquely hamiltonian if it contains precisely one hamilton circle. For finite graphs, the celebrated Sheehan's conjecture states that there are no $ r $ -regular uniquely hamiltonian graphs for $ r>2 $ ; this is known for all odd $ r $ and even $ r > 23 $ . For infinite graphs this is false even for odd $ r $ (e.g. for the two-way infinite ladder), but each of the known counterexamples has at least 2 ends, leading to the problem stated. Another way to extend Sheehan's conjecture to infinite graphs is to define degree of an end $ t \in I(G) $ to be the maximal number of disjoint rays in $ t $ and ask the following: Problem Are there any uniquely hamiltonian locally finite graphs where every vertex and every end has the same degree $ r > 2 $ ?

=== References listed by OpenProblemGarden ===
- [D] R. Diestel, Graph Theory, Third Edition, Springer, 2005.
- *[M] Bojan Mohar, Problem of the Month

=== Catalog page (statement + literature review) ===
Infinite uniquely hamiltonian graphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The problem remains open in general, but significant partial results have been obtained. Pitz (2018) proved that every one-ended Hamiltonian cubic graph with end degree 3 contains a second Hamilton circle, ruling out uniquely Hamiltonian 1-ended cubic regular graphs (with end degree 3). Miraftab and Morris (2023, JGT 2025) characterized all uniquely Hamiltonian vertex-transitive graphs with finitely many ends, finding that no one-ended vertex-transitive regular graph of degree $r > 2$ is uniquely Hamiltonian; meanwhile Heuer (2018) showed that regular infinite graphs with a unique Hamilton circle do exist, but only with infinitely many ends, leaving Mohar's original 1-ended question open for non-vertex-transitive regular graphs of degree $r > 2$.

 Cited literature (3)

 
 
 
partial Hamiltonicity in locally finite graphs: two extensions and a counterexample
 (2018)
 

 
 Karl Heuer · arXiv preprint · arXiv:1701.06029

Constructs a regular locally finite infinite graph with a unique Hamilton circle (answering positively whether such graphs exist), but the construction has infinitely many ends, so it does not resolve the 1-ended variant of Mohar's problem.
 

 
 
partial Hamilton cycles in infinite cubic graphs
 (2018)
 

 
 Max Pitz · Electronic Journal of Combinatorics · arXiv:1705.07031

Proves that every one-ended Hamiltonian cubic graph with end degree 3 contains a second Hamilton circle, thereby showing no such graph is uniquely Hamiltonian, which resolves the $r = 3$ case of Mohar's problem under the matching end-degree condition.
 

 
 
partial On vertex-transitive graphs with a unique hamiltonian cycle
 (2023)
 

 
 Babak Miraftab, Dave Witte Morris · Journal of Graph Theory · arXiv:2303.11124 · doi:10.1002/jgt.23166

Characterizes all uniquely Hamiltonian vertex-transitive graphs with finitely many ends, establishing that no one-ended vertex-transitive regular graph of degree $r > 2$ admits a unique Hamilton circle, and that the only two-ended examples are specific known graphs.
 

 

 Reviewer notes. The Miraftab-Morris paper (arXiv:2303.11124) was accessed only via abstract page; the full text could not be retrieved (Wiley page returned 403, PDF not readable), so the specific theorem about 1-ended vertex-transitive graphs is inferred from search-result summaries and should be treated with medium confidence. The Heuer (1701.06029) paper's construction: the number of ends is not stated in the arXiv abstract; search summaries suggest continuum many ends. The Pitz result is the most directly verified partial answer to the 1-ended problem. For general non-vertex-transitive locally finite 1-ended regular graphs of degree r > 3, the problem appears fully open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Problem. Are there any uniquely hamiltonian locally finite 1-ended graphs which are regular of degree $ r > 2 $ ?

Keywords:
hamiltonian · infinite graph · uniquely hamiltonian

Discussion

(Originally appeared as [M].) Let $ G $ be a locally finite infinite graph and let $ I(G) $ be the set of ends of~ $ G $ . The Freudenthal compactification of $ G $ is the topological space $ |G| $ which is obtained from the usual topological space of the graph, when viewed as a 1-dimensional cell complex, by adding all points of $ I(G) $ and setting, for each end $ t \in I(G) $ , the basic set of neighborhoods of $ t $ to consist of sets of the form $ C(S, t) \cup I(S,t) \cup E'(S,t) $ , where $ S $ ranges over the finite subsets of $ V(G) $ , $ C(S, t) $ is the component of $ G - S $ containing all rays in $ t $ , the set $ I(S,t) $ contains all ends in $ I(G) $ having rays in $ C(S, t) $ , and $ E'(S,t) $ is the union of half-edges $ (z,y] $ , one for every edge $ xy $ joining $ S $ and $ C(S,t) $ . We define a hamilton circle in $ |G| $ as a homeomorphic image $ C $ of the unit circle $ S^1 $ into $ |G| $ such that every vertex (and hence every end) of $ G $ appears in $ C $ . More details about these notions can be found in [D]. A graph $ G $ (finite or infinite) is said to be uniquely hamiltonian if it contains precisely one hamilton circle. For finite graphs, the celebrated Sheehan's conjecture states that there are no $ r $ -regular uniquely hamiltonian graphs for $ r>2 $ ; this is known for all odd $ r $ and even $ r > 23 $ . For infinite graphs this is false even for odd $ r $ (e.g. for the two-way infinite ladder), but each of the known counterexamples has at least 2 ends, leading to the problem stated. Another way to extend Sheehan's conjecture to infinite graphs is to define degree of an end $ t \in I(G) $ to be the maximal number of disjoint rays in $ t $ and ask the following: Problem Are there any uniquely hamiltonian locally finite graphs where every vertex and every end has the same degree $ r > 2 $ ?

Bibliography

 [D]
 R. Diestel, Graph Theory, Third Edition, Springer, 2005.

★ [M]
 Bojan Mohar, Problem of the Month
 Problem of the Month
