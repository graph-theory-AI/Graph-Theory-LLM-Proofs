Attack the following open graph-theory problem.

Catalog id: what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian/
Original entry: http://www.openproblemgarden.org/op/what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian
Problem attributed to: Goldengorin (posted 2007-09-10)

=== Problem statement (OpenProblemGarden) ===
Title: What is the smallest number of disjoint spanning trees made a graph Hamiltonian
We are given a complete simple undirected weighted graph $ G_1=(V,E) $ and its first arbitrary shortest spanning tree $ T_1=(V,E_1) $ . We define the next graph $ G_2=(V,E\setminus E_1) $ and find on $ G_2 $ the second arbitrary shortest spanning tree $ T_2=(V,E_2) $ . We continue similarly by finding $ T_3=(V,E_3) $ on $ G_3=(V,E\setminus \cup_{i=1}^{2}E_i) $ , etc. Let k be the smallest number of disjoint shortest spanning trees as defined above and let $ T^{k}=(V,\cup_{i=1}^{k}E_i) $ be the graph obtained as union of all $ k $ disjoint trees. Question 1 . What is the smallest number of disjoint spanning trees creates a graph $ T^{k} $ containing a Hamiltonian path. Question 2 . What is the smallest number of disjoint spanning trees creates a graph $ T^{k} $ containing a shortest Hamiltonian path? Questions 3 and 4 . Replace in questions 1 and 2 a shortest spanning tree by a 1-tree. What is the smallest number of disjoint 1-trees creates a Hamiltonian graph? What is the smallest number of disjoint 1-trees creates a graph containing a shortest Hamiltonian cycle?

=== Discussion / context (OpenProblemGarden) ===
These questions are induced by the following paper Chrobak and Poljak. On common edges in optimal solutions to travelling salesman and other optimization problems, Discrete Applied Mathematics 20 (1988) 101-111.

=== References listed by OpenProblemGarden ===
- M. Chrobak and S. Poljak. On common edges in optimal solutions to travelling salesman and other optimization problems, Discrete Applied Mathematics 20 (1988) 101-111.

=== Catalog page (statement + literature review) ===
What is the smallest number of disjoint spanning trees made a graph Hamiltonian — Graph-theory open problems

 
 Status
 unclear
 low confidence
 

 No post-2007 literature specifically addressing Goldengorin's questions on the minimum number of disjoint spanning trees (or 1-trees) needed to guarantee a Hamiltonian path or cycle was found across six independent searches. The problem appears to be a niche open question that has not attracted follow-up work in the accessible literature; Goldengorin's own arXiv output contains no papers on this topic, and general graph-theory databases returned no relevant results.

 Cited literature (2)

 
 
 
partial Maximum Independent Set when excluding an induced minor: $K_1 + tK_2$ and $tC_3 \uplus C_4$
 (2025)
 

 
 Édouard Bonnet, Julien Duron, Colin Geniet, Stéphan Thomassé, Alexandra Wesolek · arXiv preprint · arXiv:2302.08182

Proves a polynomial-time algorithm running in $n^{O(t^{5})}$ for MIS in graphs excluding $K_{1}+tK_{2}$ as an induced minor, settling Question 1 for this infinite family of planar graphs.
 

 
 
partial Shallow brambles
 (2025)
 

 
 Nicolas Bousquet, Wouter Cames van Batenburg, Louis Esperet, Gwenaël Joret, Piotr Micek · arXiv preprint · arXiv:2502.04177

Introduces depth-$r$ bramble number, tangle number, linkedness, and well-linkedness, proves they are pairwise polynomially related and all polynomially bounded in $r$ for classes with polynomial expansion, providing potential new tools toward resolving the question positively.
 

 

 Reviewer notes. The OPG problem page (garden.irmacs.sfu.ca) was unreachable (ECONNREFUSED). An arXiv author search confirms Goldengorin's arXiv papers are unrelated to spanning trees or Hamiltonian problems (image processing, scheduling, plant location). Semantic Scholar citation lookup for the Chrobak–Poljak 1988 paper returned empty content. After six searches, no verifiable post-2007 paper addressing any of the four questions in the problem statement was found. The problem most likely remains open and understudied.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

We are given a complete simple undirected weighted graph $ G_1=(V,E) $ and its first arbitrary shortest spanning tree $ T_1=(V,E_1) $ . We define the next graph $ G_2=(V,E\setminus E_1) $ and find on $ G_2 $ the second arbitrary shortest spanning tree $ T_2=(V,E_2) $ . We continue similarly by finding $ T_3=(V,E_3) $ on $ G_3=(V,E\setminus \cup_{i=1}^{2}E_i) $ , etc. Let k be the smallest number of disjoint shortest spanning trees as defined above and let $ T^{k}=(V,\cup_{i=1}^{k}E_i) $ be the graph obtained as union of all $ k $ disjoint trees. Question 1 . What is the smallest number of disjoint spanning trees creates a graph $ T^{k} $ containing a Hamiltonian path. Question 2 . What is the smallest number of disjoint spanning trees creates a graph $ T^{k} $ containing a shortest Hamiltonian path? Questions 3 and 4 . Replace in questions 1 and 2 a shortest spanning tree by a 1-tree. What is the smallest number of disjoint 1-trees creates a Hamiltonian graph? What is the smallest number of disjoint 1-trees creates a graph containing a shortest Hamiltonian cycle?

Keywords:
1-trees · cycle · Hamitonian path · spanning trees

Discussion

These questions are induced by the following paper Chrobak and Poljak. On common edges in optimal solutions to travelling salesman and other optimization problems, Discrete Applied Mathematics 20 (1988) 101-111.

Bibliography

 [?]
 M. Chrobak and S. Poljak. On common edges in optimal solutions to travelling salesman and other optimization problems, Discrete Applied Mathematics 20 (1988) 101-111.
