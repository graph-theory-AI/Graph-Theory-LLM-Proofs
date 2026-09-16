Attack the following open graph-theory problem.

Catalog id: turan_number_of_a_finite_family
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/turan_number_of_a_finite_family/
Original entry: http://www.openproblemgarden.org/op/turan_number_of_a_finite_family
Problem attributed to: Erdos, Paul, Simonovits, Miklos (posted 2013-03-05)

=== Problem statement (OpenProblemGarden) ===
Title: Turán number of a finite family.
Given a finite family $ {\cal F} $ of graphs and an integer $ n $ , the Turán number $ ex(n,{\cal F}) $ of $ {\cal F} $ is the largest integer $ m $ such that there exists a graph on $ n $ vertices with $ m $ edges which contains no member of $ {\cal F} $ as a subgraph. Conjecture For every finite family $ {\cal F} $ of graphs there exists an $ F\in {\cal F} $ such that $ ex(n, F ) = O(ex(n, {\cal F})) $ .

=== Discussion / context (OpenProblemGarden) ===
For the case when $ {\cal F} $ consists of even cycles, this would mean that (up to constants) the Turán number of $ {\cal F} $ is given by that of the longest cycle in $ {\cal F} $ . Verstraëte (see [KO]) conjectured something stronger: Conjecture For all integers $ k < \ell $ there exists a positive c = c(\ell) such that every $ C_{2\ell} $ -free graph $ G $ has a $ C_{2k} $ -free subgraph $ H $ with $ e(H) ≥ e(G)/c $ . This conjecture was motivated by a result of Györi [G] who showed that every bipartite $ C_6 $ -free graph $ G $ has a $ C_4 $ -free subgraph which contains at least half of the edges of $ G $ . The case $ k=2 $ was proved in [KO].

=== References listed by OpenProblemGarden ===
- *[ES] P.Erdös and M. Simonovits, Compactness results in extremal graph theory, Combinatorica 2 (1982), 275–288.
- [KO] D. Kühn and D. Osthus, 4-cycles in graphs without a given even cycle, J. Graph Theory 48 (2005), 147-156.
- [G] E. Györi, -free bipartite graphs and product representation of squares, Discrete Math. 165/166 (1997), 371-375.

=== Catalog page (statement + literature review) ===
Turán number of a finite family. — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture of Erdős and Simonovits — that for every finite family $\mathcal{F}$ some member $F \in \mathcal{F}$ satisfies $\mathrm{ex}(n,F) = O(\mathrm{ex}(n,\mathcal{F}))$ — remains open in general. For the even-cycle case, Grósz, Methuku, and Tompkins (2020) sharpened the Kühn-Osthus bounds on $C_4$-free subgraphs of $C_{2k}$-free graphs. The related stronger conjecture of Verstraëte discussed in the OPG has been partially disproved by Conlon, Mulrenin, and Pohoata (2026), who showed that $C_{10}$-free graphs need not contain $C_8$-free subgraphs with a constant fraction of edges.

 Cited literature (2)

 
 
 
partial On subgraphs of $C_{2k}$-free graphs and a problem of Kühn and Osthus
 (2020)
 

 
 Dániel Grósz, Abhishek Methuku, Casey Tompkins · Combinatorics, Probability and Computing · arXiv:1708.05454

Proves the sharp constant $c = 3/8$ for the $C_6$-free case: every $C_6$-free graph has a bipartite $C_4$-free subgraph with at least $3/8$ of its edges, and gives a new short proof of the general Kühn-Osthus $1/(k-1)$ bound for $C_{2k}$-free bipartite graphs, advancing the even-cycle special case of the conjecture.
 

 
 
counterexample Two counterexamples to a conjecture about even cycles
 (2026)
 

 
 David Conlon, Eion Mulrenin, Cosmin Pohoata · arXiv preprint · arXiv:2603.24515

Disproves Verstraëte's stronger conjecture (explicitly discussed in the OPG) for $\ell=4$, $k=5$: constructs $C_{10}$-free bipartite graphs in which every subgraph containing a constant fraction of edges must contain a $C_8$, using a dense $C_{10}$-free hypercube subgraph and Wenger's construction.
 

 

 Reviewer notes. The Keevash-Sudakov-Verstraete paper (arXiv:1107.4715, July 2011, Combinatorica 2013) proves the Erdős-Simonovits conjecture for families {C_{2ℓ}} combined with odd cycles for ℓ∈{2,3,5}, but the arXiv preprint predates the OPG posting (March 2013) so it was excluded from since_posted. The withdrawn preprint arXiv:2501.13036 (Conlon-Mulrenin-Pohoata, January 2025) was a precursor to 2603.24515 and was superseded. The counterexample to Verstraëte's conjecture (2603.24515) does not directly refute the main Erdős-Simonovits compactness conjecture, which remains open for all finite families.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. For every finite family $ {\cal F} $ of graphs there exists an $ F\in {\cal F} $ such that $ ex(n, F ) = O(ex(n, {\cal F})) $ .

Discussion

For the case when $ {\cal F} $ consists of even cycles, this would mean that (up to constants) the Turán number of $ {\cal F} $ is given by that of the longest cycle in $ {\cal F} $ . Verstraëte (see [KO]) conjectured something stronger: Conjecture For all integers $ k < \ell $ there exists a positive c = c(\ell) such that every $ C_{2\ell} $ -free graph $ G $ has a $ C_{2k} $ -free subgraph $ H $ with $ e(H) ≥ e(G)/c $ . This conjecture was motivated by a result of Györi [G] who showed that every bipartite $ C_6 $ -free graph $ G $ has a $ C_4 $ -free subgraph which contains at least half of the edges of $ G $ . The case $ k=2 $ was proved in [KO].

Bibliography

★ [ES]
 P.Erdös and M. Simonovits, Compactness results in extremal graph theory, Combinatorica 2 (1982), 275–288.

 [KO]
 D. Kühn and D. Osthus, 4-cycles in graphs without a given even cycle, J. Graph Theory 48 (2005), 147-156.

 [G]
 E. Györi, $ C_6 $ -free bipartite graphs and product representation of squares, Discrete Math. 165/166 (1997), 371-375.
