Attack the following open graph-theory problem.

Catalog id: list_chromatic_number_and_maximum_degree_of_bipartite_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_chromatic_number_and_maximum_degree_of_bipartite_graphs/
Original entry: http://www.openproblemgarden.org/op/list_chromatic_number_and_maximum_degree_of_bipartite_graphs
Problem attributed to: Alon, Noga (posted 2013-03-12)

=== Problem statement (OpenProblemGarden) ===
Title: List chromatic number and maximum degree of bipartite graphs
Conjecture There is a constant $ c $ such that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ c \log \Delta $ .

=== Discussion / context (OpenProblemGarden) ===
For definitions and an introduction to list colouring, see the related Wikipedia page . Alon [A] showed that the list chromatic number of a graph (not necessarily bipartite) of maximum degree $ \Delta $ is at least $ \frac{1}{2}(1-o(1))\log_2\Delta $ . Random bipartite graphs show that this is tight up to a multiplicative factor $ (2+o(1)) $ . It is not diffcult to see that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ O(\Delta/\log \Delta) $ . It also follows a more general result of Johansson [J] on triangle-free graphs.

=== References listed by OpenProblemGarden ===
- *[A] N. Alon, Degrees and choice numbers, Random Structures Algorithms, 16 (2000), 364--368.
- [AK] N. Alon and M. Krivelevich, The choice number of random bipartite graphs, Annals of Combi- natorics 2 (1998), 291-297.
- [J] A. Johansson. Asymptotic choice number for triangle free graphs. Technical Report 91–95, DIMACS, 1996.

=== Catalog page (statement + literature review) ===
List chromatic number and maximum degree of bipartite graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Alon's conjecture that the list chromatic number of any bipartite graph of maximum degree $\Delta$ is at most $c\log\Delta$ remains open. The best known upper bound has been improved from $(1+o(1))\Delta/\log\Delta$ (Johansson's triangle-free bound) to $(4/5-\varepsilon)\Delta/\log\Delta$ for bipartite graphs specifically (Bradshaw, Mohar, Stacho 2024), but this is still $\Theta(\Delta/\log\Delta)$ rather than the conjectured $O(\log\Delta)$. Partial asymmetric progress was also made by Alon, Cambie, and Kang (2021), showing that in a bipartite graph with equal maximum degree $\Delta$ on both sides, one side can be coloured from lists of size $\log\Delta$ provided the other side uses lists of size $(1+o(1))\Delta/\log\Delta$.

 Cited literature (4)

 
 
 
partial Asymmetric list sizes in bipartite graphs
 (2021)
 

 
 Noga Alon, Stijn Cambie, Ross J. Kang · Annals of Combinatorics · arXiv:2004.07457 · doi:10.1007/s00026-021-00552-5

Proves that in a bipartite graph with $\Delta_A=\Delta_B=\Delta$, one part can be assigned lists of size $\log\Delta$ and the other $(1+o(1))\Delta/\log\Delta$ and a proper list colouring is guaranteed, giving asymmetric partial progress toward the Alon-Krivelevich conjecture.
 

 
 
partial Bipartite graphs are $(\frac{4}{5}-\varepsilon) \frac{\Delta}{\log \Delta}$-choosable
 (2024)
 

 
 Peter Bradshaw, Bojan Mohar, Ladislav Stacho · arXiv preprint · arXiv:2409.01513

Proves that every bipartite graph of sufficiently large maximum degree $\Delta$ satisfies $\chi_\ell(G) < (4/5-\varepsilon)\Delta/\log\Delta$ for $\varepsilon=10^{-3}$, improving Johansson's triangle-free bound and showing list colouring is fundamentally easier for bipartite graphs, but still far from the conjectured $O(\log\Delta)$.
 

 
 
partial Asymmetric list sizes in bipartite graphs
 (2021)
 

 
 Noga Alon, Stijn Cambie, Ross J. Kang · arXiv preprint · arXiv:2004.07457

Proves Corollary 10: for any $\varepsilon > 0$ and $\Delta$ large enough, every bipartite graph with maximum degree at most $\Delta$ is $((1+\varepsilon)\Delta/\log^4\Delta,\,2)$- and $((1+\varepsilon)\Delta/\log\Delta,\,\log\Delta)$-choosable, constituting the first asymmetric progress toward the conjecture.
 

 
 
partial Bipartite graphs are $(\frac{4}{5}-\varepsilon) \fracΔ{\log Δ}$-choosable
 (2024)
 

 
 Peter Bradshaw, Bojan Mohar, Ladislav Stacho · arXiv preprint · arXiv:2409.01513

Proves that every bipartite graph $G$ of sufficiently large maximum degree $\Delta$ satisfies $\operatorname{ch}(G)<(\frac{4}{5}-\varepsilon)\frac{\Delta}{\log\Delta}$ for $\varepsilon=10^{-3}$, giving the first upper bound with leading constant strictly less than $1$ and showing that list coloring behaves fundamentally differently for bipartite graphs than for general triangle-free graphs.
 

 

 Reviewer notes. The Zhu (2023) paper on 'semi-small list size' for complete bipartite graphs was verified but focuses on asymmetric list sizes in complete bipartite graphs rather than the original conjecture, so it was omitted from since_posted. The conjecture's gap remains very large: the upper bound is $\Theta(\Delta/\log\Delta)$ and the lower bound from random bipartite graphs is $\Omega(\log\Delta)$. The 2024 Bradshaw-Mohar-Stacho paper is an arXiv preprint as of the review date; journal publication status unknown.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. There is a constant $ c $ such that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ c \log \Delta $ .

Discussion

For definitions and an introduction to list colouring, see the related Wikipedia page . Alon [A] showed that the list chromatic number of a graph (not necessarily bipartite) of maximum degree $ \Delta $ is at least $ \frac{1}{2}(1-o(1))\log_2\Delta $ . Random bipartite graphs show that this is tight up to a multiplicative factor $ (2+o(1)) $ . It is not diffcult to see that the list chromatic number of any bipartite graph $ G $ of maximum degree $ \Delta $ is at most $ O(\Delta/\log \Delta) $ . It also follows a more general result of Johansson [J] on triangle-free graphs.

Bibliography

★ [A]
 N. Alon, Degrees and choice numbers , Random Structures Algorithms, 16 (2000), 364--368.
 Degrees and choice numbers

 [AK]
 N. Alon and M. Krivelevich, The choice number of random bipartite graphs, Annals of Combi- natorics 2 (1998), 291-297.

 [J]
 A. Johansson. Asymptotic choice number for triangle free graphs. Technical Report 91–95, DIMACS, 1996.

Related conjectures

 
 implied by
 Asymmetric Krivelevich–Alon choosability for bipartite graphs
 open
 Take any bipartite G with maximum degree Delta; both parts then have maximum degree at most Delta, so apply the source's case (ii) with Delta_A = Delta_B = Delta and k_A = k_B = ceil(C log Delta), which satisfies k_A >= C log Delta_B and k_B >= C log Delta_A. The conclusion is that G is (k, k)-choosable with k = ceil(C log Delta), and (k,k)-choosability (both parts get lists of size k) is exactly k-choosability, so chi_l(G) <= C log Delta + 1 = O(log Delta) — the Alon (Krivelevich–Alon) conjecture. The source's own context confirms the hypothesis-strength ordering: 'conditions (ii) and (iii) are stronger than Conjecture 2' (the symmetric log-Delta conjecture). Direction correct: source is the stronger asymmetric refinement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
