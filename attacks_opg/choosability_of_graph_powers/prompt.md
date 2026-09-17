Attack the following open graph-theory problem.

Catalog id: choosability_of_graph_powers
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/choosability_of_graph_powers/
Original entry: http://www.openproblemgarden.org/op/choosability_of_graph_powers
Problem attributed to: Noel, Jonathan A. (posted 2013-07-13)

=== Problem statement (OpenProblemGarden) ===
Title: Choosability of Graph Powers
Question (Noel, 2013) Does there exist a function $ f(k)=o(k^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^2\right)\leq f\left(\chi\left(G^2\right)\right)?\]

=== Discussion / context (OpenProblemGarden) ===
For a survey of choosability, including relevant definitions, see [Noe] or click here . The List Square Colouring Conjecture, due to Kostochka and Woodall [KW], states that $ \text{ch}\left(G^2\right) = \chi\left(G^2\right) $ for every graph $ G $ . This was disproved by Kim and Park [KP], who proved that there is a sequence $ \{G_n\}_n $ of graphs and a constant $ c_1 $ such that $ \chi\left(G^2_n\right)\to\infty $ and $ \text{ch}\left(G_n^2\right) \geq c_1 \chi\left(G_n^2\right)\log\left(\chi\left(G_n^2\right)\right) $ for all $ n $ . To obtain this lower bound from the construction of Kim and Park, one can apply the well-known result of Alon [Alo]. It may be the case that the correct upper bound for all graphs is of the same order of magnitude as the example in the result of Kim and Park. Question (Noel, 2013) Does there exist a positive constant $ c_2 $ such that every graph $ G $ satisfies $ \text{ch}\left(G^2\right) \leq c_2\chi\left(G^2\right)\log{\chi\left(G^2\right)} $ ? By calculating the clique number and maximum degree of $ G^2 $ , one can easily show that $ \text{ch}\left(G^2\right)\leq\chi\left(G^2\right)^2 $ (this observation is due to Young Soo Kwon), but it seems that no significantly better bound is known. Proposition If $ G $ contains an edge, then \[\text{ch}\left(G^2\right)< \chi\left(G^2\right)^2.\] Proof We observe the following bounds: \[\chi\left(G^2\right) \geq \omega\left(G^2\right) \geq \Delta(G)+1,\] \[\text{ch}\left(G^2\right) \leq \Delta\left(G^2\right)+1 \leq \Delta(G)\left(\Delta(G)-1\right) + \Delta(G)+1 = \Delta(G)^2+1.\] Therefore, since $ \Delta(G)>0 $ , we have \[\text{ch}\left(G^2\right)\leq \Delta(G)^2+1 < \left(\Delta(G)+1\right)^2 \leq \chi\left(G^2\right)^2.\] This completes the proof. These questions are related to a problem of Zhu (see Doug West's webpage for more info) who asked whether there exists an integer $ k $ such that for every graph $ G $ , we have that $ G^k $ has choice number equal to chromatic number. This conjecture has been disproved independently by Kim, Kwon and Park [KKP] and Kosar, Petrickova, Reigniger and Yeager [KPRY]. The example of [KPRY] also yields, for every $ k $ , a sequence $ \{G_n\}_n $ of graphs and a constant $ c $ such that $ \chi\left(G^k_n\right)\to\infty $ and $ \text{ch}\left(G_n^k\right) \geq c \chi\left(G_n^k\right)\log\left(\chi\left(G_n^k\right)\right) $ for all $ n $ . They ask the following, more general, questions: Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a function $ f_k(x)=o(x^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^k\right)\leq f_k\left(\chi\left(G^k\right)\right)?\] To our knowledge, it is not known whether there exists a function $ f_k(x) = o(x^k) $ such that the same conclusion holds. (Intuitively, it seems that higher values of $ k $ should yield a smaller separation between $ \text{ch}(G^k) $ and $ \chi(G^k) $ ; however, there seems to be no hard evidence to support this.) Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a positive constant $ c_k $ such that every graph $ G $ satisfies $ \text{ch}\left(G^k\right) \leq c_k\chi\left(G^k\right)\log{\chi\left(G^k\right)} $ ? Moreover, can the constant $ c_k $ be made independent of $ k $ ? These questions are also related to the so-called List Total Colouring Conjecture of Borodin, Kostochka and Woodall [BKW], which says that the total graph of a multigraph always satisfies $ \text{ch}=\chi $ . Given a multigraph $ G $ , the total graph of $ G $ can be obtained by subdividing every edge of $ G $ and then taking the square of the resulting graph.

=== References listed by OpenProblemGarden ===
- [Alo] Noga Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.
- [BKW] Oleg V. Borodin, Alexandr V. Kostochka, and Douglas R. Woodall. List edge and list total colourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.
- [KP] Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture, submitted.
- [KKP] Seog-Jin Kim, Young Soo Kwon and Boram Park: Chromatic-choosability of the power of graphs.
- [KPRY] Nicholas Kosar, Sarka Petrickova, Benjamin Reiniger, Elyse Yeager: A note on list-coloring powers of graphs.
- [KW] Alexandr V. Kostochka and Douglas R. Woodall. Choosability conjectures and multicircuits, Discrete Math., 240 (2001), 123--143.
- [Noe] Jonathan A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond, Master's thesis. McGill University (2013). pdf.

=== Catalog page (statement + literature review) ===
Choosability of Graph Powers — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The question of whether $\text{ch}(G^2) \le f(\chi(G^2))$ for some $f = o(k^2)$ remains open. Shortly after the OPG posting, two independent papers (Kim–Kwon–Park and Kosar–Petrickova–Reiniger–Yeager) confirmed that Zhu's related conjecture fails for all powers $k \ge 2$ and that the logarithmic lower bound $\text{ch}(G^k) \ge c\,\chi(G^k)\log\chi(G^k)$ extends to every $k$; KPRY also established $\text{ch}(G^k) < \chi(G^k)^3$ for $k > 1$, but no subquadratic improvement over the quadratic upper bound $\text{ch}(G^2) \le \chi(G^2)^2$ has been established for squares.

 Cited literature (2)

 
 
 
partial Chromatic-choosability of the power of graphs
 (2013)
 

 
 Seog-Jin Kim, Young Soo Kwon, Boram Park · arXiv preprint · arXiv:1309.0888

Independently disproves Zhu's conjecture by showing that for every integer $k \ge 2$ there exists a graph $G$ such that $G^k$ is not chromatic-choosable and the gap $\chi_\ell(G^k)-\chi(G^k)$ can be arbitrarily large.
 

 
 
partial A note on list-coloring powers of graphs
 (2013)
 

 
 Nicholas Kosar, Sarka Petrickova, Benjamin Reiniger, Elyse Yeager · arXiv preprint · arXiv:1309.7705

Extends the logarithmic lower bound to all powers ($\text{ch}(G^k) \ge c\,\chi(G^k)\log\chi(G^k)$ for all $k \ge 2$) and proves the upper bound $\text{ch}(G^k) < \chi(G^k)^3$ for $k > 1$, but does not yield a subquadratic upper bound for squares.
 

 

 Reviewer notes. The Kim–Park arXiv preprint (1305.2566) was submitted May 12 2013, before the OPG posting of July 13 2013, so it is not counted as a post-posting result even though its journal publication (J. Graph Theory, 2015) is later. Both the KKP and KPRY papers appear in the OPG bibliography, indicating the OPG page was updated after initial posting to incorporate them. Six searches were conducted with no evidence of a paper proving a subquadratic upper bound for $\text{ch}(G^2)$; the problem thus appears genuinely open. The 2022 Hasanvand paper (arXiv:2211.00622) addresses the planar/bipartite versions of the List Square Coloring Conjecture but does not establish any bound of the form $\text{ch}(G^2) \le f(\chi(G^2))$ with $f = o(k^2)$.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 269s.
 

Question (Noel, 2013). Does there exist a function $ f(k)=o(k^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^2\right)\leq f\left(\chi\left(G^2\right)\right)?\]

Keywords:
choosability · chromatic number · list coloring · square of a graph

Discussion

For a survey of choosability, including relevant definitions, see [Noe] or click here . The List Square Colouring Conjecture, due to Kostochka and Woodall [KW], states that $ \text{ch}\left(G^2\right) = \chi\left(G^2\right) $ for every graph $ G $ . This was disproved by Kim and Park [KP], who proved that there is a sequence $ \{G_n\}_n $ of graphs and a constant $ c_1 $ such that $ \chi\left(G^2_n\right)\to\infty $ and $ \text{ch}\left(G_n^2\right) \geq c_1 \chi\left(G_n^2\right)\log\left(\chi\left(G_n^2\right)\right) $ for all $ n $ . To obtain this lower bound from the construction of Kim and Park, one can apply the well-known result of Alon [Alo]. It may be the case that the correct upper bound for all graphs is of the same order of magnitude as the example in the result of Kim and Park. Question (Noel, 2013) Does there exist a positive constant $ c_2 $ such that every graph $ G $ satisfies $ \text{ch}\left(G^2\right) \leq c_2\chi\left(G^2\right)\log{\chi\left(G^2\right)} $ ? By calculating the clique number and maximum degree of $ G^2 $ , one can easily show that $ \text{ch}\left(G^2\right)\leq\chi\left(G^2\right)^2 $ (this observation is due to Young Soo Kwon), but it seems that no significantly better bound is known. Proposition If $ G $ contains an edge, then \[\text{ch}\left(G^2\right)< \chi\left(G^2\right)^2.\] Proof We observe the following bounds: \[\chi\left(G^2\right) \geq \omega\left(G^2\right) \geq \Delta(G)+1,\] \[\text{ch}\left(G^2\right) \leq \Delta\left(G^2\right)+1 \leq \Delta(G)\left(\Delta(G)-1\right) + \Delta(G)+1 = \Delta(G)^2+1.\] Therefore, since $ \Delta(G)>0 $ , we have \[\text{ch}\left(G^2\right)\leq \Delta(G)^2+1 < \left(\Delta(G)+1\right)^2 \leq \chi\left(G^2\right)^2.\] This completes the proof. These questions are related to a problem of Zhu (see Doug West's webpage for more info) who asked whether there exists an integer $ k $ such that for every graph $ G $ , we have that $ G^k $ has choice number equal to chromatic number. This conjecture has been disproved independently by Kim, Kwon and Park [KKP] and Kosar, Petrickova, Reigniger and Yeager [KPRY]. The example of [KPRY] also yields, for every $ k $ , a sequence $ \{G_n\}_n $ of graphs and a constant $ c $ such that $ \chi\left(G^k_n\right)\to\infty $ and $ \text{ch}\left(G_n^k\right) \geq c \chi\left(G_n^k\right)\log\left(\chi\left(G_n^k\right)\right) $ for all $ n $ . They ask the following, more general, questions: Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a function $ f_k(x)=o(x^2) $ such that for every graph $ G $ , \[\text{ch}\left(G^k\right)\leq f_k\left(\chi\left(G^k\right)\right)?\] To our knowledge, it is not known whether there exists a function $ f_k(x) = o(x^k) $ such that the same conclusion holds. (Intuitively, it seems that higher values of $ k $ should yield a smaller separation between $ \text{ch}(G^k) $ and $ \chi(G^k) $ ; however, there seems to be no hard evidence to support this.) Question (Kosar et al., 2013) Given $ k\geq2 $ , does there exist a positive constant $ c_k $ such that every graph $ G $ satisfies $ \text{ch}\left(G^k\right) \leq c_k\chi\left(G^k\right)\log{\chi\left(G^k\right)} $ ? Moreover, can the constant $ c_k $ be made independent of $ k $ ? These questions are also related to the so-called List Total Colouring Conjecture of Borodin, Kostochka and Woodall [BKW], which says that the total graph of a multigraph always satisfies $ \text{ch}=\chi $ . Given a multigraph $ G $ , the total graph of $ G $ can be obtained by subdividing every edge of $ G $ and then taking the square of the resulting graph.

Bibliography

 [Alo]
 Noga Alon. Choice numbers of graphs: a probabilistic approach. Combin. Probab. Comput., 1(2):107–114, 1992.

 [BKW]
 Oleg V. Borodin, Alexandr V. Kostochka, and Douglas R. Woodall. List edge and list total colourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.

 [KP]
 Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture , submitted.
 Counterexamples to the List Square Coloring Conjecture

 [KKP]
 Seog-Jin Kim, Young Soo Kwon and Boram Park: Chromatic-choosability of the power of graphs .
 Chromatic-choosability of the power of graphs

 [KPRY]
 Nicholas Kosar, Sarka Petrickova, Benjamin Reiniger, Elyse Yeager: A note on list-coloring powers of graphs .
 A note on list-coloring powers of graphs

 [KW]
 Alexandr V. Kostochka and Douglas R. Woodall. Choosability conjectures and multicircuits, Discrete Math., 240 (2001), 123--143.

 [Noe]
 Jonathan A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond, Master's thesis. McGill University (2013). pdf .
 pdf

Related conjectures

 
 related to
 List Total Colouring Conjecture
 open
 The source page explicitly says these questions 'are also related to the so-called List Total Colouring Conjecture'. Both descend from the disproved List Square Colouring Conjecture ch(G^2)=chi(G^2): LTCC is its special case on squares of subdivisions (total graphs), Noel's question is a weakened o(k^2)-bound version for all graphs. No implication either way: a positive answer to Noel's question allows a superlinear gap, far weaker than the exact equality LTCC demands on total graphs; and LTCC, restricted to total graphs, cannot bound ch(G^2) for general G. Explicitly stated relatedness, no derivable implication: related_only.
 

 
 related to
 Total Colouring Conjecture
 partial
 The mention in the source page is actually to the List Total Colouring Conjecture of Borodin, Kostochka and Woodall, not to Behzad's Total Colouring Conjecture; the match to Behzad's page is a name near-miss. A thematic link survives (total graphs are squares of subdivided graphs, so choosability-of-squares questions bear on total colouring), but there is no implication either way: Noel's question asks for an o(k^2) bound on ch(G^2) in terms of chi(G^2), while Behzad's conjecture bounds the chromatic number (not choosability) of total graphs by Delta+2. Neither statement's truth forces the other's.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
