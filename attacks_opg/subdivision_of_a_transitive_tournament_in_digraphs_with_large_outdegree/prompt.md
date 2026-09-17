Attack the following open graph-theory problem.

Catalog id: subdivision_of_a_transitive_tournament_in_digraphs_with_large_outdegree
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/subdivision_of_a_transitive_tournament_in_digraphs_with_large_outdegree/
Original entry: http://www.openproblemgarden.org/op/subdivision_of_a_transitive_tournament_in_digraphs_with_large_outdegree
Problem attributed to: Mader, W. (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Subdivision of a transitive tournament in digraphs with large outdegree.
Conjecture For all $ k $ there is an integer  $ f(k) $ such that every digraph of minimum outdegree at least  $ f(k) $ contains a subdivision of a transitive tournament of order $ k $ .

=== Discussion / context (OpenProblemGarden) ===
A fundamental result of Mader [M1] states that for every integer $ k $ there is a smallest $ g(k) $ so that every graph of average degree at least $ g(k) $ contains a subdivision of a complete graph on $ k $ vertices. Bollobás and Thomason [BT] as well as Komlós and Szemerédi [KS] showed that $ g $ is quadratic in $ k $ . The above conjecture is a digraph analogue of this result. However one cannot replace the minimum outdegree in this conjecture by the average degree as in Mader's analogue for graphs: consider the complete bipartite graph $ K_{n,n} $ and orient all edges from the first to the second class. The resulting digraph has average degree $ n $ but not even a transitive tournament on 3 vertices. One might be tempted to conjecture that large minimum outdegree would even force the existence of a subdivision of a large complete digraph. However, for all $ n $ Thomassen [T] constructed a digraph on $ n $ vertices whose minimum outdegree is at least $ \frac{1}{2} \log_2 n $ but which does not contain an even directed cycle (and thus no complete digraph on 3 vertices). A simpler construction was found by DeVos et al. [DMMS]. It is easy to see that  $ f(1)=0 $ and $ f(2)=1 $ . Mader [M3] showed that $ f(4) = 3 $ . Even the existence of  $ f(5) $ is not known.

=== References listed by OpenProblemGarden ===
- [BT] B. Bollobás and A. Thomason, Proof of a conjecture of Mader, Erdös and Hajnal on topological complete subgraphs, European Journal of Combinatorics 19 (1998), 883–887.
- [DMMS] M. DeVos, J. McDonald, B. Mohar, and D. Scheide, Immersing complete digraphs, European Journal of Combinatorics, 33 (2012), no 6, 1294-1302.
- [KS] J. Komlós and E. Szemerédi, Topological Cliques in Graphs II, Combinatorics, Probability and Computing 5 (1996), 70–90.
- [M1] W. Mader, Homomorphieeigenschaften und mittlere Kantendichte von Graphen, Math. Annalen 174 (1967), 265–268.
- * [M2] W. Mader, Degree and Local Connectivity in Digraphs, Combinatorica 5 (1985), 161–165.
- [M3] W. Mader, On Topological Tournaments of order 4 in Digraphs of Outdegree 3, Journal of Graph Theory 21 (1996), 371–376.
- [T] C. Thomassen, Even Cycles in Directed Graphs, European Journal of Combinatorics 6 (1985), 85–89.

=== Catalog page (statement + literature review) ===
Subdivision of a transitive tournament in digraphs with large outdegree. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Mader's conjecture remains open in full generality — even the existence of $f(5)$ is unknown as of the most recent sources found. Meaningful partial progress has been made: Lochet (2017) proved the immersion analogue of the conjecture (immersion being a weaker embedding notion than subdivision), and Aboulker et al. (2019) proved the conjecture for special sub-structures (oriented paths, in-arborescences) and connected it to the dichromatic number. Kim, Lee, and Seo (2022) established Ramsey-type bounds $O(k^2 \log\log k)$ for 1-subdivisions of transitive tournaments inside arbitrary tournaments.

 Cited literature (4)

 
 
 
partial Subdivisions in Digraphs of Large Out-Degree or Large Dichromatic Number
 (2019)
 

 
 Pierre Aboulker, Nathann Cohen, Frédéric Havet, William Lochet, Phablo F. S. Moura, Stéphan Thomassé · The Electronic Journal of Combinatorics · arXiv:1610.00876

Proves Mader's conjecture for special cases including oriented paths and in-arborescences, and shows digraphs with dichromatic number greater than $4^m(n-1)$ contain every $n$-vertex $m$-arc digraph as a subdivision; the general conjecture remains open with $f(5)$ still unknown.
 

 
 
partial Immersion of transitive tournaments in digraphs with large minimum outdegree
 (2017)
 

 
 William Lochet · arXiv preprint · arXiv:1710.11482

Proves the immersion analogue of Mader's conjecture: every simple digraph with minimum outdegree greater than $h(k)$ contains an immersion of the transitive tournament on $k$ vertices, resolving a conjecture of DeVos–McDonald–Mohar–Scheide.
 

 
 
partial On 1-subdivisions of transitive tournaments
 (2022)
 

 
 Jaehoon Kim, Hyunwoo Lee, Jaehyeon Seo · The Electronic Journal of Combinatorics · arXiv:2110.05002

Proves the oriented Ramsey number for the 1-subdivision of the $k$-vertex transitive tournament is $O(k^2 \log\log k)$, tight up to the logarithmic factor, and gives structural results for tournaments with bounded outdegree variation; applies to tournaments, not general digraphs.
 

 
 
partial Subdivisions in digraphs of large out-degree or large dichromatic number
 (2016)
 

 
 Pierre Aboulker, Nathann Cohen, Fréderic Havet, William Lochet, Phablo F. S. Moura, Stéphan Thomassé · arXiv preprint · arXiv:1610.00876

Proves the conjecture for all oriented paths (Corollary 20, with $\mathrm{mader}_{\delta^+}(P)=|V(P)|-1$), for all in-arborescences (Theorem 23), and for the union of two directed paths from $x$ to $y$ and one from $y$ to $x$ (Theorem 24); also studies an analogue via the dichromatic number parameter.
 

 

 Reviewer notes. The Lochet immersion paper (arXiv:1710.11482, 2017) resolves a related but weaker conjecture; its journal publication status was not fully confirmed but its content and authorship were verified. The Kim–Lee–Seo result applies to 1-subdivisions inside tournaments (not general digraphs with large minimum outdegree), so it does not directly resolve Mader's conjecture. No paper was found proving f(5) exists or resolving the general Mader conjecture. A 2023 survey (arXiv:2306.02364) was found but did not address this specific conjecture in its accessible content.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. For all $ k $ there is an integer  $ f(k) $ such that every digraph of minimum outdegree at least  $ f(k) $ contains a subdivision of a transitive tournament of order $ k $ .

Discussion

A fundamental result of Mader [M1] states that for every integer $ k $ there is a smallest $ g(k) $ so that every graph of average degree at least $ g(k) $ contains a subdivision of a complete graph on $ k $ vertices. Bollobás and Thomason [BT] as well as Komlós and Szemerédi [KS] showed that $ g $ is quadratic in $ k $ . The above conjecture is a digraph analogue of this result. However one cannot replace the minimum outdegree in this conjecture by the average degree as in Mader's analogue for graphs: consider the complete bipartite graph $ K_{n,n} $ and orient all edges from the first to the second class. The resulting digraph has average degree $ n $ but not even a transitive tournament on 3 vertices. One might be tempted to conjecture that large minimum outdegree would even force the existence of a subdivision of a large complete digraph. However, for all $ n $ Thomassen [T] constructed a digraph on $ n $ vertices whose minimum outdegree is at least $ \frac{1}{2} \log_2 n $ but which does not contain an even directed cycle (and thus no complete digraph on 3 vertices). A simpler construction was found by DeVos et al. [DMMS]. It is easy to see that  $ f(1)=0 $ and $ f(2)=1 $ . Mader [M3] showed that $ f(4) = 3 $ . Even the existence of  $ f(5) $ is not known.

Bibliography

 [BT]
 B. Bollobás and A. Thomason, Proof of a conjecture of Mader, Erdös and Hajnal on topological complete subgraphs, European Journal of Combinatorics 19 (1998), 883–887.

 [DMMS]
 M. DeVos, J. McDonald, B. Mohar, and D. Scheide, Immersing complete digraphs, European Journal of Combinatorics, 33 (2012), no 6, 1294-1302.

 [KS]
 J. Komlós and E. Szemerédi, Topological Cliques in Graphs II, Combinatorics, Probability and Computing 5 (1996), 70–90.

 [M1]
 W. Mader, Homomorphieeigenschaften und mittlere Kantendichte von Graphen, Math. Annalen 174 (1967), 265–268.

★ [M2]
 W. Mader, Degree and Local Connectivity in Digraphs, Combinatorica 5 (1985), 161–165.

 [M3]
 W. Mader, On Topological Tournaments of order 4 in Digraphs of Outdegree 3, Journal of Graph Theory 21 (1996), 371–376.

 [T]
 C. Thomassen, Even Cycles in Directed Graphs, European Journal of Combinatorics 6 (1985), 85–89.

Related conjectures

 
 equivalent to
 TT_k Subdivision via Minimum Semidegree
 open
 One direction is hypothesis-class containment: delta^0(D)=min(delta^+,delta^-)>=f forces delta^+(D)>=f, so any digraph satisfying the semidegree hypothesis satisfies the outdegree hypothesis, hence Mader's outdegree conjecture implies the semidegree version. The converse is proved in the source paper: it shows that if transitive tournaments are delta^0-maderian then mader_{delta^+}(TT_k) <= mader_{delta^0}(TT_{2k}) for all k, and the provided context explicitly states 'Conjecture 3 is equivalent to Mader's Conjecture 2', which is the OPG statement. Equivalence is thus both partly self-contained and explicitly asserted in the source text.
 

 
 implies
 TT_k Subdivision via Minimum Semidegree
 open
 Hypothesis-class containment: delta^0(D) = min(min-outdegree, min-indegree), so any digraph with delta^0(D) >= f(k) in particular has minimum outdegree >= f(k). If Mader's outdegree conjecture holds with f(k), every such digraph contains a TT_k subdivision, so mader_{delta^0}(TT_k) exists and is <= f(k). The semidegree hypothesis is the stronger assumption, making the outdegree conjecture the stronger statement; direction as claimed. The target's own context notes the paper proves the two are in fact equivalent (via mader_{delta^+}(TT_k) <= mader_{delta^0}(TT_{2k})), but the claimed one-way implication is immediate from the statements alone.
 

 
 implies
 δ⁺-Maderian property for oriented trees
 open
 Every oriented tree T on k vertices is an acyclic digraph, so ordering its vertices along a topological order embeds T as a subdigraph of the transitive tournament TT_k (TT_k contains all forward arcs). A subdivision of TT_k contains a subdivision of every subdigraph H of TT_k: keep the branch vertices of H and the directed paths corresponding to H's arcs. Hence if min out-degree >= f(k) forces a TT_k-subdivision (source), it forces a subdivision of every oriented tree of order k, i.e., every oriented tree is delta+-maderian with mader_{delta+}(T) <= f(|T|) (target). Direction is correct: source is the stronger statement, and the target's context confirms it is 'posed as a natural weaker step towards Mader's Conjecture'.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
