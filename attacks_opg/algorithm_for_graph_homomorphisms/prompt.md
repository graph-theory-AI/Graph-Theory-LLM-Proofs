Attack the following open graph-theory problem.

Catalog id: algorithm_for_graph_homomorphisms
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Homomorphisms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/algorithm_for_graph_homomorphisms/
Original entry: http://www.openproblemgarden.org/op/algorithm_for_graph_homomorphisms
Problem attributed to: Fomin, Fedor V., Heggernes, Pinar, Kratsch, Dieter (posted 2010-07-08)

=== Problem statement (OpenProblemGarden) ===
Title: Algorithm for graph homomorphisms
Question Is there an algorithm that decides, for input graphs $ G $ and $ H $ , whether there exists a homomorphism from $ G $ to $ H $ in time $ O(c^{|V(G)|+|V(H)|}) $ for some constant $ c $ ?

=== Discussion / context (OpenProblemGarden) ===
An affirmative answer is known in several cases: if $ H=K_k $ (graph coloring) [L], [BH], [K]; if $ H $ has bounded treewidth [FHK]; if $ H $ has bounded cliquewidth [W].

=== References listed by OpenProblemGarden ===
- [BH] Andreas Björklund, Thore Husfeldt: Inclusion--Exclusion Algorithms for Counting Set Partitions, Proc. FOCS'06 (2006).
- *[FHK] Fedor V. Fomin, Pinar Heggernes, Dieter Kratsch: Exact Algorithms for Graph Homomorphisms, Theory Comput. Syst. 41 (2007), no. 2, 381--393. MathSciNet
- [K] Mikko Koivisto: An Algorithm for Graph Coloring and Other Partitioning Problems via Inclusion--Exclusion, Proc. FOCS'06 (2006).
- [L] Eugene L. Lawler: A note on the complexity of the chromatic number problem, Information Processing Lett. 5 (1976), no. 3, 66--67. MathSciNet
- [W] Magnus Wahlström: New Plain-Exponential Time Classs for Graph Homomorphism, CSR2009, LNCS5675 (2009), 346--355.

=== Catalog page (statement + literature review) ===
Algorithm for graph homomorphisms — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The original question of whether there is an algorithm deciding the existence of a homomorphism from $G$ to $H$ in time $O(c^{|V(G)|+|V(H)|})$ for some absolute constant $c$ remains open in full generality. Since 2010, several works have extended the list of graph classes admitting such plain-exponential algorithms (e.g., Wahlstrom-type results were generalized by Dadsetan and Bulatov to further classes for the counting version, and Rzazewski gave an $O^{*}((b+2)^{|V(G)|})$ algorithm parametrized by the bandwidth of the complement of $H$), and Fomin, Golovnev, Kulikov, and Mihajlin proved an ETH lower bound of $2^{\Omega(n \log h / \log\log h)}$ for the general problem, which however does not rule out a $c^{n+h}$ algorithm.

 Cited literature (4)

 
 
 
partial Lower Bounds for the Graph Homomorphism Problem
 (2015)
 

 
 Fedor V. Fomin, Alexander Golovnev, Alexander S. Kulikov, Ivan Mihajlin · ICALP 2015 / arXiv preprint · arXiv:1502.05447 · doi:10.1007/978-3-662-47672-7_39

Proves an ETH-based lower bound of $2^{\Omega(n \log h / \log\log h)}$ for deciding graph homomorphism, ruling out single-exponential-in-$n\log h$ algorithms but not a $c^{|V(G)|+|V(H)|}$ algorithm.
 

 
 
partial Exact Algorithm for Graph Homomorphism and Locally Injective Graph Homomorphism
 (2014)
 

 
 Pawel Rzazewski · Information Processing Letters / arXiv preprint · arXiv:1310.3341 · doi:10.1016/j.ipl.2014.02.012

Gives an exact algorithm for graph homomorphism running in time $O^{*}((b+2)^{|V(G)|})$, where $b$ is the bandwidth of the complement of $H$, expanding the list of classes for which the problem is solvable in plain-exponential time.
 

 
 
partial Counting homomorphisms in plain exponential time
 (2018)
 

 
 Amineh Dadsetan, Andrei A. Bulatov · arXiv preprint · arXiv:1810.03087

Generalizes Wahlstrom's result for counting graph homomorphisms in time $k^{|V(G)|+|V(H)|}\cdot\mathrm{poly}$ from bounded clique-width to additional classes of target graphs $H$, enlarging the known cases of plain-exponential algorithms.
 

 
 
partial The Fine-Grained Complexity of Graph Homomorphism Parameterized by Clique-Width
 (2022)
 

 
 Robert Ganian, Thekla Hamm, Viktoriia Korchemna, Karolina Okrasa, Kirill Simonov · ICALP 2022 / arXiv preprint · arXiv:2210.06845 · doi:10.4230/LIPIcs.ICALP.2022.66

Provides a fine-grained classification of the homomorphism problem in time $O^{*}(s(H)^{cw})$ with matching SETH-based lower bounds, refining the picture for restricted target graphs $H$ (clique-width-parametrized) but leaving the general $c^{|V(G)|+|V(H)|}$ question open.
 

 

 Reviewer notes. The original question concerns the decision version with constant base $c$ independent of $G,H$. The 2015 ETH lower bound of $2^{\Omega(n \log h / \log\log h)}$ does NOT rule out a $c^{|V(G)|+|V(H)|}$ algorithm (e.g., when $h \gg n$, $c^{n+h}$ can exceed the lower bound). All cited papers extend the known classes of $H$ for which plain-exponential algorithms exist, or give lower bounds for restricted parameterizations, but none affirmatively or negatively resolves the original FHK question. The exact published year/venue of arXiv:1810.03087 was not verified beyond the preprint.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Question. Is there an algorithm that decides, for input graphs $ G $ and $ H $ , whether there exists a homomorphism from $ G $ to $ H $ in time $ O(c^{|V(G)|+|V(H)|}) $ for some constant $ c $ ?

Keywords:
algorithm · Exponential-time algorithm · homomorphism

Discussion

An affirmative answer is known in several cases: if $ H=K_k $ (graph coloring) [L], [BH], [K]; if $ H $ has bounded treewidth [FHK]; if $ H $ has bounded cliquewidth [W].

Bibliography

 [BH]
 Andreas Björklund, Thore Husfeldt: Inclusion--Exclusion Algorithms for Counting Set Partitions, Proc. FOCS'06 (2006).

★ [FHK]
 Fedor V. Fomin, Pinar Heggernes, Dieter Kratsch: Exact Algorithms for Graph Homomorphisms, Theory Comput. Syst. 41 (2007), no. 2, 381--393. MathSciNet
 MathSciNet

 [K]
 Mikko Koivisto: An $ O^\ast(2^n) $ Algorithm for Graph Coloring and Other Partitioning Problems via Inclusion--Exclusion, Proc. FOCS'06 (2006).

 [L]
 Eugene L. Lawler: A note on the complexity of the chromatic number problem, Information Processing Lett. 5 (1976), no. 3, 66--67. MathSciNet
 MathSciNet

 [W]
 Magnus Wahlström: New Plain-Exponential Time Classs for Graph Homomorphism, CSR2009, LNCS5675 (2009), 346--355.
