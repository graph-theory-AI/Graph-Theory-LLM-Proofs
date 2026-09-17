Attack the following open graph-theory problem.

Catalog id: behzads_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/behzads_conjecture/
Original entry: http://www.openproblemgarden.org/op/behzads_conjecture
Problem attributed to: Behzad, M. (posted 2008-06-04)

=== Problem statement (OpenProblemGarden) ===
Title: Total Colouring Conjecture
Conjecture A total coloring of a graph $ G = (V,E) $ is an assignment of colors to the vertices and the edges of $ G $ such that every pair of adjacent vertices, every pair of adjacent edges and every vertex and incident edge pair, receive different colors. The total chromatic number of a graph $ G $ , $ \chi''(G) $ , equals the minimum number of colors needed in a total coloring of $ G $ . It is an old conjecture of Behzad that for every graph $ G $ , the total chromatic number equals the maximum degree of a vertex in $ G $ , $ \Delta(G) $ plus one or two. In other words, \[\chi''(G)=\Delta(G)+1\ \ or \ \ \Delta(G)+2.\]

=== Discussion / context (OpenProblemGarden) ===
The lower bound $ \Delta(G)+1 $ is trivial by looking at the number of colours required on a vertex of maximum degree and its incident edges. It is easy to prove $ \chi''(G)\leq 2\Delta(G)+2 $ . Molloy and Reed [MR] showed that there exists a constant $ C $ such that $ \chi''(G)\leq Delta(G)+C $ for every graph $ G $ . The Edge list coloring conjecture would imply that $ \chi''(G)\leq \Delta(G)+3 $ . The Total Colouring Conjecture was proved for $ \Delta(G)=3 $ by Rosenfeld [R] and also by Vijayaditya [V], and for $ \Delta(G)\in\{4,5\} $ by Kostochka [K1,K2,K3]; in fact the proof for $ \Delta(G)=5 $ holds for multigraphs. The Conjecture has also been established for many graph classes. For every planar graph G with $ \Delta(G) \geq 7 $ , the following clever argument proves it. By the 4 Color Theorem, we can color the vertices with the colors 1, 2, 3, 4. By a result of Sanders and Zhao [SZ], we can color the edges of the graph with the colors $ 3, 4, \ldots, \Delta(G) + 1, \Delta(G) + 2 $ . Uncolor each edge that was colored 3 or 4. Note that each uncolored edge has exactly two colors from $ \{1,2,3,4\} $ forbidden. Hence, each uncolored edge has at least two colors available. Note that the uncolored edges induce a disjoint union of paths and even cycles. Thus, by a special case of a theorem of Erdos, Rubin, and Taylor [ERT], we can color the edges from their lists of two available colors each.

=== References listed by OpenProblemGarden ===
- *[B] M. Behzad, Graphs and their chromatic numbers, Ph.D. Thesis, Michigan State University, 1965.
- [ERT] P. Erdos, A.L. Rubin, and H. Taylor, Choosability in graph, Cong. Numer. 26, 125-157, 1979.
- [K1] A.V. Kostochka, The total coloring of a multigraph with maximal degree 4. Discrete Math. 17, 161-163, 1977.
- [K2] A.V. Kostochka, Upper bounds of chromatic functions of graph (in Russian). Ph.D. Thesis, Novosibirsk, 1978.
- [K3] A.V. Kostochka, Exact upper bound for the total chromatic number of a graph (in Russian). In: Proc. 24th Int. Wiss. Koll., Tech Hochsch. Ilmenau, 1979, pages 33-36, 1979.
- [MR] M. Molloy and B.Reed. A bound on the total chromatic number. Combinatorica, 18(2), 241-280, 1998.
- [R] M. Rosenfeld, On the total coloring of certain graphs. Israel J. Math. 9, 396-402, 1971.
- [SZ] D.P. Sanders and Y. Zhao, Planar Graphs of Maximum Degree Seven are Class 1. J. Comb. Theory B. 83, 201-212, 2001.
- [V] N. Vijayaditya, On total chormatic number of a graph. J. London Math. Soc. (2) 3, 405-408, 1971.

=== Catalog page (statement + literature review) ===
Total Colouring Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Total Colouring Conjecture remains open in general. For planar graphs, all cases except $\Delta(G)=6$ are resolved; a sequence of papers has narrowed the $\Delta=6$ planar case by imposing forbidden-subgraph conditions. For general graphs, Dalal, McDonald, and Shan (2024) confirmed the conjecture for $r$-regular graphs with $r \geq \tfrac{1}{2}(1+\varepsilon)n$ and $n$ sufficiently large, and improved Hind's 1992 general upper bound by one color. An unreviewed arXiv preprint (Murthy, 2020) claims a full proof via the Combinatorial Nullstellensatz, but this has not been accepted by the community and the conjecture is still listed as open.

 Cited literature (5)

 
 
 
survey Total Colourings - A survey
 (2018)
 

 
 Geetha Jayabalan, Narayanan N, K. Somasundaram · arXiv preprint · arXiv:1812.05833

Comprehensive survey of total coloring results confirming that the conjecture remains open even for planar graphs as of 2018.
 

 
 
partial On a Sufficient Condition for Planar Graphs of Maximum Degree 6 to be Totally 7-Colorable
 (2018)
 

 
 Enqiang Zhu, Chanjuan Liu, Yongsheng Rao · arXiv preprint · arXiv:1812.00133

Proves that every diamond-free and house-free planar graph of maximum degree 6 satisfying certain local cycle conditions is totally 7-colorable, extending the $\Delta=6$ planar case beyond the earlier cycle-free restriction.
 

 
 
partial Total coloring graphs with large maximum degree
 (2024)
 

 
 Aseem Dalal, Jessica McDonald, Songling Shan · arXiv preprint · arXiv:2405.07382

Proves TCC for $r$-regular graphs on $n$ vertices with $r \geq \tfrac{1}{2}(1+\varepsilon)n$ and $n$ sufficiently large, and improves Hind's 1992 general upper bound by one color to $\Delta(G)+2\lceil|V(G)|/(\Delta(G)+1)\rceil$.
 

 
 
partial The Total Coloring Conjecture holds for planar graphs without three special subgraphs
 (2025)
 

 
 Rongjin Su, Gang Fang, Enqiang Zhu · arXiv preprint · arXiv:2507.12737

Establishes TCC for planar graphs with $\Delta=6$ that exclude the mushroom, tent, and cone subgraphs, extending the range of planar graphs for which the $\Delta=6$ case is confirmed.
 

 
 
partial The Parameterised Complexity of List Problems on Graphs of Bounded Treewidth
 (2016)
 

 
 Kitty Meeks, Alexander Scott · arXiv preprint · arXiv:1110.4077

Proves a special case as Theorem 2.8: for any graph $G$ of treewidth at most $k$ with $\Delta(G) \geq (k+2)^{2k+2}$, $\mathrm{ch}_T(G) = \chi_T(G) = \Delta(G)+1$, yielding a stronger form of the conjecture for this class.
 

 

 Reviewer notes. A claimed full proof (arXiv:2003.09658, T.S. Murthy, 2020, using Combinatorial Nullstellensatz over $\mathbb{Z}_p$) is not accepted by the community: Wikipedia still lists TCC as an open problem, the 2024 Dalal et al. paper treats it as open, and no peer-reviewed publication of the Murthy proof was found. The planar $\Delta=6$ case is the main remaining open subcase for planar graphs; all $\Delta\geq 7$ planar cases are settled. The best general bound remains $\Delta(G)+O(1)$ from Molloy–Reed (1998).

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 111s.
 

Conjecture. A total coloring of a graph $ G = (V,E) $ is an assignment of colors to the vertices and the edges of $ G $ such that every pair of adjacent vertices, every pair of adjacent edges and every vertex and incident edge pair, receive different colors. The total chromatic number of a graph $ G $ , $ \chi''(G) $ , equals the minimum number of colors needed in a total coloring of $ G $ . It is an old conjecture of Behzad that for every graph $ G $ , the total chromatic number equals the maximum degree of a vertex in $ G $ , $ \Delta(G) $ plus one or two. In other words, \[\chi''(G)=\Delta(G)+1\ \ or \ \ \Delta(G)+2.\]

Keywords:
Total coloring

Discussion

The lower bound $ \Delta(G)+1 $ is trivial by looking at the number of colours required on a vertex of maximum degree and its incident edges. It is easy to prove $ \chi''(G)\leq 2\Delta(G)+2 $ . Molloy and Reed [MR] showed that there exists a constant $ C $ such that $ \chi''(G)\leq Delta(G)+C $ for every graph $ G $ . The Edge list coloring conjecture would imply that $ \chi''(G)\leq \Delta(G)+3 $ . The Total Colouring Conjecture was proved for $ \Delta(G)=3 $ by Rosenfeld [R] and also by Vijayaditya [V], and for $ \Delta(G)\in\{4,5\} $ by Kostochka [K1,K2,K3]; in fact the proof for $ \Delta(G)=5 $ holds for multigraphs. The Conjecture has also been established for many graph classes. For every planar graph G with $ \Delta(G) \geq 7 $ , the following clever argument proves it. By the 4 Color Theorem, we can color the vertices with the colors 1, 2, 3, 4. By a result of Sanders and Zhao [SZ], we can color the edges of the graph with the colors $ 3, 4, \ldots, \Delta(G) + 1, \Delta(G) + 2 $ . Uncolor each edge that was colored 3 or 4. Note that each uncolored edge has exactly two colors from $ \{1,2,3,4\} $ forbidden. Hence, each uncolored edge has at least two colors available. Note that the uncolored edges induce a disjoint union of paths and even cycles. Thus, by a special case of a theorem of Erdos, Rubin, and Taylor [ERT], we can color the edges from their lists of two available colors each.

Bibliography

★ [B]
 M. Behzad, Graphs and their chromatic numbers, Ph.D. Thesis, Michigan State University, 1965.

 [ERT]
 P. Erdos, A.L. Rubin, and H. Taylor, Choosability in graph, Cong. Numer. 26, 125-157, 1979.

 [K1]
 A.V. Kostochka, The total coloring of a multigraph with maximal degree 4. Discrete Math. 17, 161-163, 1977.

 [K2]
 A.V. Kostochka, Upper bounds of chromatic functions of graph (in Russian). Ph.D. Thesis, Novosibirsk, 1978.

 [K3]
 A.V. Kostochka, Exact upper bound for the total chromatic number of a graph (in Russian). In: Proc. 24th Int. Wiss. Koll., Tech Hochsch. Ilmenau, 1979, pages 33-36, 1979.

 [MR]
 M. Molloy and B.Reed. A bound on the total chromatic number. Combinatorica, 18(2), 241-280, 1998.

 [R]
 M. Rosenfeld, On the total coloring of certain graphs. Israel J. Math. 9, 396-402, 1971.

 [SZ]
 D.P. Sanders and Y. Zhao, Planar Graphs of Maximum Degree Seven are Class 1. J. Comb. Theory B. 83, 201-212, 2001.

 [V]
 N. Vijayaditya, On total chormatic number of a graph. J. London Math. Soc. (2) 3, 405-408, 1971.

Related conjectures

 
 implied by
 List Total Coloring χ″ℓ ≤ Δ+2
 open
 Ordinary total coloring is the special case of list total coloring where every vertex and edge receives the same list {1,...,k}, so χ''(G) ≤ χ''_ℓ(G) for every graph. Thus χ''_ℓ(G) ≤ Δ+2 for all simple graphs gives χ''(G) ≤ Δ+2. Combined with the trivial lower bound χ''(G) ≥ Δ+1 (a maximum-degree vertex and its incident edges pairwise conflict), this yields χ''(G) ∈ {Δ+1, Δ+2}, which is exactly Behzad's Total Colouring Conjecture. The source's own context describes it as the list analogue of TCC. Direction correct: the list version is the stronger statement.
 

 
 related to
 Choosability of Graph Powers
 open
 The mention in the source page is actually to the List Total Colouring Conjecture of Borodin, Kostochka and Woodall, not to Behzad's Total Colouring Conjecture; the match to Behzad's page is a name near-miss. A thematic link survives (total graphs are squares of subdivided graphs, so choosability-of-squares questions bear on total colouring), but there is no implication either way: Noel's question asks for an o(k^2) bound on ch(G^2) in terms of chi(G^2), while Behzad's conjecture bounds the chromatic number (not choosability) of total graphs by Delta+2. Neither statement's truth forces the other's.
 

 
 related to
 Edge list coloring conjecture
 open
 The TCC page states only that the Edge List Coloring Conjecture 'would imply chi''(G) <= Delta(G)+3' (via ch'(G)=chi'(G) <= Delta+1 by Vizing and chi'' <= ch'+2). Delta+3 is strictly weaker than TCC's Delta+2 bound, so ELCC does NOT imply TCC. Conversely TCC, a statement about the total chromatic number, says nothing about list edge colorings, so it does not imply ELCC. The connection is a weak-bound consequence only: the correct classification is related_only, with no implication in either direction.
 

 
 related to
 List Total Colouring Conjecture
 open
 Both conjectures concern the same object, since chi''(H) = chi(T(H)). But they assert logically independent things: LTCC says the list chromatic number of a total graph equals its chromatic number (choosability = colorability), while TCC bounds that chromatic number by Delta(H)+2. Truth of LTCC gives no bound on chi(T(H)), and truth of TCC says nothing about list colorings, so neither implies the other. The OPG context itself only says the problem 'is related to ... the Total Colouring Conjecture'. (Note: their conjunction would give chi_ell(T(H)) <= Delta+2, but separately no implication holds.)
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
