Attack the following open graph-theory problem.

Catalog id: approximation_ratio_for_k_outerplanar_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/approximation_ratio_for_k_outerplanar_graphs/
Original entry: http://www.openproblemgarden.org/op/approximation_ratio_for_k_outerplanar_graphs
Problem attributed to: Bentz, Cedric (posted 2010-04-18)

=== Problem statement (OpenProblemGarden) ===
Title: Approximation ratio for k-outerplanar graphs
Conjecture Is the approximation ratio for the Maximum Edge Disjoint Paths (MaxEDP) or the Maximum Integer Multiflow problem (MaxIMF) bounded by a constant in $ k $ -outerplanar graphs or tree-width graphs?

=== Discussion / context (OpenProblemGarden) ===
Assume a flow graph $ G = (V, E) $ with $ n $ vertices and $ m $ edges ( Flow network ). Each edge has a capacity function $ c: E \rightarrow \mathbb{Z}^+ $ . The graph contains a list $ \mathcal{N} $ of terminal vertices called sources ( $ s_i $ ) and sinks ( $ s_i' $ ). Each pair ( $ s_i, s_i' $ ) defines a net or commodity. A Multiflow is a way of routing commodities from their sources to the respective sinks while ensuring that the flow of each commodity is conserved at each non-terminal vertex and that the sum of the flows of all commodities through an edge does not exceed the capacity of the edge. The Maximum Integer Multiflow problem (MaxIMF) seeks to maximize the number of flow units routed between the nets in the graph. The Maximum Edge Disjoint Paths (MaxEDP) problem seeks to find the maximum number of disjoint paths between the sources and sinks. When the capacities for all edges are set to one, MaxIMF simplifies into the MaxEDP problem. Is the approximation ratio ( Approximation and integrality gap ) for MaxEDP or MaxIMF bounded by a constant in $ k $ -outerplanar graphs ( Outerplanar graphs ) or tree-width graphs?

=== References listed by OpenProblemGarden ===
- C. Bentz, “Disjoint paths in sparse graphs,” Discrete Appl. Math., vol. 157, no. 17, pp. 3558–3568, 2009

=== Catalog page (statement + literature review) ===
Approximation ratio for k-outerplanar graphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 Significant partial progress exists. Chekuri, Naves, and Shepherd (ICALP 2013) showed that the integrality gap of the natural multicommodity LP for MaxEDP is bounded by a constant in $k$-sums of bounded-genus graphs (a class that includes bounded-treewidth graphs and in particular $k$-outerplanar graphs for fixed $k$), giving a constant-factor approximation without congestion in these settings. Ene, Mnich, Pilipczuk, and Risteski (SWAT 2016) gave an $O(r^3)$-approximation for MaxEDP on graphs of treewidth at most $r$, which is constant for any fixed treewidth (and hence for fixed $k$ in $k$-outerplanar graphs, since they have treewidth $O(k)$). Naves, Shepherd, and Xia (IPCO 2021 / Math. Programming 2022) further obtained a constant-factor approximation for the weighted edge-disjoint paths problem on outerplanar graphs ($k=1$). However, whether the approximation ratio is bounded by an absolute constant independent of $k$ (or of the treewidth) remains open.

 Cited literature (4)

 
 
 
partial Maximum Edge-Disjoint Paths in k-sums of Graphs
 (2013)
 

 
 Chandra Chekuri, Guyslain Naves, F. Bruce Shepherd · ICALP 2013 (Lecture Notes in Computer Science, vol. 7965) · arXiv:1303.4897 · doi:10.1007/978-3-642-39206-1_28

Provides a polynomial-time algorithm that rounds any fractional MaxEDP solution in a bounded-treewidth (more generally $k$-sum of bounded-genus) graph to an integral routing of a constant fraction of the LP value, with no edge congestion, implying a constant integrality gap and a constant-factor approximation in these classes (including $k$-outerplanar graphs for fixed $k$).
 

 
 
partial On Routing Disjoint Paths in Bounded Treewidth Graphs
 (2016)
 

 
 Alina Ene, Matthias Mnich, Marcin Pilipczuk, Andrej Risteski · SWAT 2016 (LIPIcs vol. 53) · doi:10.4230/LIPIcs.SWAT.2016.15

Gives an $O(r^3)$-approximation for MaxEDP on graphs of treewidth at most $r$, improving over the previous $O(r \cdot 3^r)$ bound and yielding a constant-factor approximation for any fixed treewidth (and thus for $k$-outerplanar graphs with $k$ fixed).
 

 
 
partial Maximum Weight Disjoint Paths in Outerplanar Graphs via Single-Tree Cut Approximators
 (2020)
 

 
 Guyslain Naves, F. Bruce Shepherd, Henry Xia · arXiv preprint (later IPCO 2021 / Math. Programming 2022) · arXiv:2007.10537 · doi:10.1007/978-3-030-73879-2_23

Constructs a single-tree $O(1)$ cut approximator for outerplanar graphs and uses it to give a constant-factor approximation for the maximum-weight (capacitated) edge-disjoint paths / all-or-nothing flow problem in outerplanar graphs, settling the case $k=1$.
 

 
 
partial New algorithms for maximum disjoint paths based on tree-likeness
 (2018)
 

 
 Krzysztof Fleszar, Matthias Mnich, Joachim Spoerhase · Mathematical Programming, vol. 171 · doi:10.1007/s10107-017-1199-3

Gives an $O(\sqrt{r}\,\mathrm{polylog}(kr))$-approximation for MaxEDP parametrized by the feedback vertex set number $r$ (a parameter stronger than treewidth), and shows how to route $\Omega(\mathrm{OPT}^*)$ pairs with $O(\log(kr)/\log\log(kr))$ congestion.
 

 

 Reviewer notes. The original conjecture asks whether the approximation ratio is bounded by an absolute constant in $k$-outerplanar graphs (or in bounded-treewidth graphs). All known results either (i) give constants that depend on $k$ / treewidth $r$ (e.g. the $O(r^3)$ bound of Ene-Mnich-Pilipczuk-Risteski), or (ii) achieve a true constant only for restricted classes such as outerplanar graphs ($k=1$, Naves-Shepherd-Xia) or via constant-congestion / LP-rounding statements (Chekuri-Naves-Shepherd 2013 for $k$-sums of bounded-genus graphs). It is plausible that the Chekuri-Naves-Shepherd result yields a constant approximation ratio for $k$-outerplanar graphs uniformly in $k$, but this could not be confirmed from the abstracts alone within the time budget. EDP is also known to be NP-hard already at treewidth 2 (series-parallel), so improvements must come from approximation, not exact algorithms.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Is the approximation ratio for the Maximum Edge Disjoint Paths (MaxEDP) or the Maximum Integer Multiflow problem (MaxIMF) bounded by a constant in $ k $ -outerplanar graphs or tree-width graphs?

Keywords:
approximation algorithms · planar graph · polynomial algorithm

Discussion

Assume a flow graph $ G = (V, E) $ with $ n $ vertices and $ m $ edges ( Flow network ). Each edge has a capacity function $ c: E \rightarrow \mathbb{Z}^+ $ . The graph contains a list $ \mathcal{N} $ of terminal vertices called sources ( $ s_i $ ) and sinks ( $ s_i' $ ). Each pair ( $ s_i, s_i' $ ) defines a net or commodity. A Multiflow is a way of routing commodities from their sources to the respective sinks while ensuring that the flow of each commodity is conserved at each non-terminal vertex and that the sum of the flows of all commodities through an edge does not exceed the capacity of the edge. The Maximum Integer Multiflow problem (MaxIMF) seeks to maximize the number of flow units routed between the nets in the graph. The Maximum Edge Disjoint Paths (MaxEDP) problem seeks to find the maximum number of disjoint paths between the sources and sinks. When the capacities for all edges are set to one, MaxIMF simplifies into the MaxEDP problem. Is the approximation ratio ( Approximation and integrality gap ) for MaxEDP or MaxIMF bounded by a constant in $ k $ -outerplanar graphs ( Outerplanar graphs ) or tree-width graphs?

Bibliography

 [?]
 C. Bentz, “Disjoint paths in sparse graphs,” Discrete Appl. Math., vol. 157, no. 17, pp. 3558–3568, 2009
