Attack the following open graph-theory problem.

Catalog id: good_edge_labelings
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Labeling
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/good_edge_labelings/
Original entry: http://www.openproblemgarden.org/op/good_edge_labelings
Problem attributed to: Araújo, Julio, Cohen, Nathann, Giroire, Frédéric, Havet, Frédéric (posted 2011-06-30)

=== Problem statement (OpenProblemGarden) ===
Title: Good Edge Labelings
Question What is the maximum edge density of a graph which has a good edge labeling? We say that a graph is good-edge-labeling critical , if it has no good edge labeling, but every proper subgraph has a good edge labeling. Conjecture For every $ c<4 $ , there is only a finite number of good-edge-labeling critical graphs with average degree less than $ c $ .

=== Discussion / context (OpenProblemGarden) ===
Let $ G $ be a finite undirected simple graph. A good edge labeling of $ G $ is an assignment of distinct numbers to the edges such that every cycle has at least two local maxima. (The distinctness of the labels is required only to make the term `local maximum' unambiguous.) Equivalently, a labeling of the edges is good, if for every pair of distinct vertices $ u,v $ , there is at most one increasing path from $ u $ to $ v $ . Having a good edge labeling is inherited by subgraphs. It is easy to verify that the graphs $ K_3 $ and $ K_{2,3} $ have no good edge labeling. In [ACGH2] an infinite class of graphs without good edge labelings is given, none of whom is a subgraph of the other. In [BFT] contains an example of a minimal graph without good edge labeling which as average degree < 3 (thus refuting an earlier conjecture saying that a good-edge-labeling critical graph with average degree less than three is either $ K_3 $ or $ K_{2,3} $ ). In that same paper it is shown that every such graph must have girth at most 4. Good edge labeling of graphs was introduced in [BCP] in the context of the so-called Routing and Wavelength Assignment (RWA) problem. The problems above are proposed in [ACGH1] and [ACGH2]. There the algorithmic problem of determining whether a graph has a good edge labeling is shown to be NP-hard. Moreover, the authors also prove that every planar graph with girth at least six has a good edge labeling.

=== References listed by OpenProblemGarden ===
- [BCP] J-C. Bermond, M. Cosnard, and S. Pérennes. Directed acyclic graphs with unique path property. Technical report 6932, INRIA, May 2009
- [ACGH1] J. Araújo, N. Cohen, F. Giroire, F. Havet. Good edge-labelling of graphs. (English summary) LAGOS'09—V Latin-American Algorithms, Graphs and Optimization Symposium, 275–280, Electron. Notes Discrete Math., 35, Elsevier Sci. B. V., Amsterdam, 2009. MathSciNet
- [ACGH2*] J. Araujo, N. Cohen, F. Giroire, and F. Havet. Good edge-labelling of graphs. Research Report 6934, INRIA, 2009.
- [BFT] M. Bode, B. Farzad, D.O. Theis. Good edge-labelings and graphs of girth at least 5. (arXiv:1109.1125)

=== Catalog page (statement + literature review) ===
Good Edge Labelings — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The two open problems — characterising the maximum edge density of good-edge-labelable graphs and the conjecture on finitely many critical graphs with average degree below $c < 4$ — remain unresolved. Mehrabian (2012) established that bad graphs with arbitrarily large girth exist (disproving a naive girth-threshold hope), and showed that any good nearly-regular $n$-vertex graph has at most $n^{1+o(1)}$ edges, giving a partial answer to the density question. A 2024 paper initiates a parameterized-complexity study of the decision problem but does not address the extremal conjectures.

 Cited literature (2)

 
 
 
partial On the density of nearly regular graphs with a good edge-labelling
 (2012)
 

 
 Abbas Mehrabian · SIAM Journal on Discrete Mathematics · arXiv:1110.2391

Proves that bad graphs with arbitrarily large girth exist, and that any good nearly-regular $n$-vertex graph has at most $n^{1+o(1)}$ edges; also shows that for fixed maximum degree $\Delta$, sufficiently large girth forces good labelability.
 

 
 
partial On the parameterized complexity of computing good edge-labelings
 (2024)
 

 
 Davi de Andrade, Júlio Araújo, Laure Morelle, Ignasi Sau, Ana Silva · arXiv preprint · arXiv:2408.15181 · doi:10.48550/arXiv.2408.15181

Initiates a parameterized-complexity study of good edge-labelings, proving NP-completeness of the $c$-GEL variant for all $c\geq 2$ and giving FPT algorithms and polynomial kernels under structural parameters; does not address the density or critical-graph conjectures.
 

 

 Reviewer notes. The [BFT] paper (arXiv:1109.1125, Bode-Farzad-Theis, submitted September 2011 hence after the OPG posting date of 2011-06-30) is already listed in the OPG bibliography and so is not re-listed here. The exact DOI for the Mehrabian SIAM paper was not retrieved and is left null. A systematic search of journals post-2015 was not possible within the 4-query limit; additional results may exist.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Question. What is the maximum edge density of a graph which has a good edge labeling?

Conjecture. For every $ c<4 $ , there is only a finite number of good-edge-labeling critical graphs with average degree less than $ c $ .

Keywords:
good edge labeling, edge labeling

Discussion

Let $ G $ be a finite undirected simple graph. A good edge labeling of $ G $ is an assignment of distinct numbers to the edges such that every cycle has at least two local maxima. (The distinctness of the labels is required only to make the term `local maximum' unambiguous.) Equivalently, a labeling of the edges is good, if for every pair of distinct vertices $ u,v $ , there is at most one increasing path from $ u $ to $ v $ . Having a good edge labeling is inherited by subgraphs. It is easy to verify that the graphs $ K_3 $ and $ K_{2,3} $ have no good edge labeling. In [ACGH2] an infinite class of graphs without good edge labelings is given, none of whom is a subgraph of the other. In [BFT] contains an example of a minimal graph without good edge labeling which as average degree < 3 (thus refuting an earlier conjecture saying that a good-edge-labeling critical graph with average degree less than three is either $ K_3 $ or $ K_{2,3} $ ). In that same paper it is shown that every such graph must have girth at most 4. Good edge labeling of graphs was introduced in [BCP] in the context of the so-called Routing and Wavelength Assignment (RWA) problem. The problems above are proposed in [ACGH1] and [ACGH2]. There the algorithmic problem of determining whether a graph has a good edge labeling is shown to be NP-hard. Moreover, the authors also prove that every planar graph with girth at least six has a good edge labeling.

Bibliography

 [BCP]
 J-C. Bermond, M. Cosnard, and S. Pérennes. Directed acyclic graphs with unique path property. Technical report 6932, INRIA, May 2009

 [ACGH1]
 J. Araújo, N. Cohen, F. Giroire, F. Havet. Good edge-labelling of graphs. (English summary) LAGOS'09—V Latin-American Algorithms, Graphs and Optimization Symposium, 275–280, Electron. Notes Discrete Math., 35, Elsevier Sci. B. V., Amsterdam, 2009. MathSciNet
 MathSciNet

 [ACGH2*]
 J. Araujo, N. Cohen, F. Giroire, and F. Havet. Good edge-labelling of graphs. Research Report 6934, INRIA, 2009.

 [BFT]
 M. Bode, B. Farzad, D.O. Theis. Good edge-labelings and graphs of girth at least 5. (arXiv:1109.1125)
