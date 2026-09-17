Attack the following open graph-theory problem.

Catalog id: 57_regular_moore_graph
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Algebraic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/57_regular_moore_graph/
Original entry: http://www.openproblemgarden.org/op/57_regular_moore_graph
Problem attributed to: Hoffman, Alan J., Singleton, Robert R. (posted 2007-03-18)

=== Problem statement (OpenProblemGarden) ===
Title: 57-regular Moore graph?
Question Does there exist a 57- regular graph with diameter 2 and girth 5?

=== Discussion / context (OpenProblemGarden) ===
A Moore graph is a graph with diameter $ d $ and girth $ 2d+1 $ . It is known that every Moore graph is regular [S] (even distance-regular), and two (rather trivial) families of such graphs are provided by complete graphs and odd cycles. In one of the founding papers in the subject of algebraic graph theory, Hoffman and Singleton [HS] proved that every $ r $ -regular Moore graph with diameter 2 must have $ r \in \{2,3,7,57\} $ . For $ r=2 $ and $ r=3 $ such graphs exist, are unique, and are familiar: the pentagon, and the Petersen graph . For $ r=7 $ Hoffman and Singleton constructed such a graph - now known as the Hoffman-Singleton graph , but for $ r=57 $ we are still uncertain whether such a graph exists. The pentagon, the Petersen graph, and the Hoffman-Singleton graph are all very highly symmetric graphs, and much of the interest in these objects is related to exceptional phenomena in small finite groups. In contrast to this, Higman proved that a 57-regular Moore graph cannot be vertex transitive (see [C]). In some sense, this is indication that even if a 57-regular Moore graph exists, it will be of less interest than its younger siblings. Nevertheless, as a lingering problem left by one of the first papers in algebraic graph theory, this is viewed as an important question. There are some easily established properties of a 57-regular Moore graph. For instance it must have 3250 vertices and independence number at most 400. However it seems not nearly enough is known to narrow the search sufficiently.

=== References listed by OpenProblemGarden ===
- [C] P. J. Cameron, Automorphisms of graphs in: Selected topics in graph theory, Volume 2, eds. L. W. Beineke and R. J. Wilson (Academic Press, London) 1983, pp. 89-127. MathSciNet
- * [HS] A. J. Hoffman and R. R. Singleton, On Moore graphs with diameters 2 and 3. IBM J. Res. Develop. 4 (1960) 497--504. MathSciNet
- [S] R. R. Singleton, There is no irregular Moore graph. American Mathematical Monthly 75, vol 1 (1968) 42–43. MathSciNet

=== Catalog page (statement + literature review) ===
57-regular Moore graph? — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The existence of a 57-regular Moore graph (equivalently, a strongly regular graph with parameters $(3250,57,0,1)$) remains an open problem. A 2020 arXiv preprint by Makhnev claimed to prove non-existence via a case analysis on distance-regular graphs, but Faber and Keegan (2022) identified a critical flaw: the system of equations involved factors into small diagonal blocks, each of which admits solutions. The problem is widely regarded as still open as of 2023.

 Cited literature (2)

 
 
 
partial Moore graph with parameters (3250,57,0,1) does not exist
 (2020)
 

 
 A. A. Makhnev · arXiv preprint · arXiv:2010.13443

Claims to prove non-existence of the Moore graph of degree 57 via a case analysis on distance-regular graphs with intersection array {55,54,2;1,1,54}; subsequently shown to contain a critical error.
 

 
 
partial Existence of a Moore graph of degree 57 is still open
 (2023)
 

 
 Vance Faber, Jonathan Keegan · arXiv preprint · arXiv:2210.09577

Identifies a critical flaw in Makhnev's 2020 claimed non-existence proof (the constraint equations factor into solvable diagonal blocks), and proposes a reformulation in terms of permutation systems, confirming the existence question is still open.
 

 

 Reviewer notes. Several post-2007 papers could not be verified due to HTTP 403 blocks on MDPI (doi:10.3390/axioms15050332, doi:10.3390/sym16121563) and ScienceDirect (doi:10.1016/j.ejco.2023.100078). These reportedly include: a 2024 Symmetry paper (Smith & Montemanni) extending computational subgraph results from 15 to 20, a 2023 EURO J. Computational Optimization paper posing the problem as an optimization problem, and a 2026 Axioms paper proving cyclic-group constructions are impossible. None of these resolve the existence question. The Makhnev 2020 paper (2010.13443) was submitted as arXiv only and its claimed non-existence result is considered invalid. The problem is confidently still open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Question. Does there exist a 57- regular graph with diameter 2 and girth 5?

Keywords:
cage · Moore graph

Discussion

A Moore graph is a graph with diameter $ d $ and girth $ 2d+1 $ . It is known that every Moore graph is regular [S] (even distance-regular), and two (rather trivial) families of such graphs are provided by complete graphs and odd cycles. In one of the founding papers in the subject of algebraic graph theory, Hoffman and Singleton [HS] proved that every $ r $ -regular Moore graph with diameter 2 must have $ r \in \{2,3,7,57\} $ . For $ r=2 $ and $ r=3 $ such graphs exist, are unique, and are familiar: the pentagon, and the Petersen graph . For $ r=7 $ Hoffman and Singleton constructed such a graph - now known as the Hoffman-Singleton graph , but for $ r=57 $ we are still uncertain whether such a graph exists. The pentagon, the Petersen graph, and the Hoffman-Singleton graph are all very highly symmetric graphs, and much of the interest in these objects is related to exceptional phenomena in small finite groups. In contrast to this, Higman proved that a 57-regular Moore graph cannot be vertex transitive (see [C]). In some sense, this is indication that even if a 57-regular Moore graph exists, it will be of less interest than its younger siblings. Nevertheless, as a lingering problem left by one of the first papers in algebraic graph theory, this is viewed as an important question. There are some easily established properties of a 57-regular Moore graph. For instance it must have 3250 vertices and independence number at most 400. However it seems not nearly enough is known to narrow the search sufficiently.

Bibliography

 [C]
 P. J. Cameron, Automorphisms of graphs in: Selected topics in graph theory, Volume 2, eds. L. W. Beineke and R. J. Wilson (Academic Press, London) 1983, pp. 89-127. MathSciNet
 MathSciNet

★ [HS]
 A. J. Hoffman and R. R. Singleton, On Moore graphs with diameters 2 and 3 . IBM J. Res. Develop. 4 (1960) 497--504. MathSciNet
 On Moore graphs with diameters 2 and 3 · MathSciNet

 [S]
 R. R. Singleton, There is no irregular Moore graph . American Mathematical Monthly 75, vol 1 (1968) 42–43. MathSciNet
 There is no irregular Moore graph · MathSciNet

Related conjectures

 
 implies
 Triangle free strongly regular graphs
 open
 A 57-regular Moore graph of diameter 2 and girth 5 has 3250 vertices and is strongly regular with parameters (3250,57,0,1): girth 5 forces lambda=0 (triangle-free) and diameter 2 with girth 5 forces mu=1. None of the seven known triangle-free strongly regular graphs (C5, Petersen, Clebsch, Hoffman-Singleton, Gewirtz, the (77,16,0,4) graph, Higman-Sims) has these parameters, so its existence yields an eighth, answering the target affirmatively. The target's OPG context states this implication verbatim: 'Every Moore Graph of diameter 2 is a triangle-free strongly regular graph, so if there is a 57-regular Moore graph of diameter 2, this would add another to the list.' Direction correct.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
