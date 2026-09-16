Attack the following open graph-theory problem.

Catalog id: turans_problem_for_hypergraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Hypergraphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/turans_problem_for_hypergraphs/
Original entry: http://www.openproblemgarden.org/op/turans_problem_for_hypergraphs
Problem attributed to: Turan, Paul (posted 2013-03-12)

=== Problem statement (OpenProblemGarden) ===
Title: Turán's problem for hypergraphs
Conjecture Every simple $ 3 $ -uniform hypergraph on $ 3n $ vertices which contains no complete $ 3 $ -uniform hypergraph on four vertices has at most $ \frac12 n^2(5n-3) $ hyperedges. Conjecture Every simple $ 3 $ -uniform hypergraph on $ 2n $ vertices which contains no complete $ 3 $ -uniform hypergraph on five vertices has at most $ n^2(n-1) $ hyperedges.

=== Discussion / context (OpenProblemGarden) ===
Let $ V $ be an $ n $ -set. A $ k $ -uniform hypergraph $ (V,{\cal F}) $ is complete if $ {\cal F}={V \choose k} $ , the set of all $ {n\choose{k}} $ $ k $ -subsets of $ V $ . Let $ \{X,Y,Z\} $ be a partition of $ V $ into three sets which are as nearly equal in size as possible, and let $ {\cal F} $ be the union of $ \{\{x,y,z\}:x\in X, y\in Y, z\in Z\} $ , $ \{\{x_1,x_2,y\}:x_1\in X, x_2\in X, y\in Y\} $ , $ \{\{y_1,y_2,z\}:y_1\in Y, y_2\in Y, z\in Z\} $ , and $ \{\{z_1,z_2,x\}:z_1\in Z, z_2\in Z, x\in X\} $ . This $ 3 $ -uniform hypergraph has $ \frac12 n^2(5n-3) $ hyperedges and contains no complete $ 3 $ -uniform hypergraph on four vertices. Hence the first conjecture asserts that this hypergraph is extremal with this prpoerty. Let $ \{X,Y\} $ be a partition of $ V $ into two sets which are as nearly equal in size as possible, and let $ {\cal F} $ be the set of all $ 3 $ -subsets of $ V $ which intersect both $ X $ and $ Y $ . This $ 3 $ -uniform hypergraph has $ n^2(n-1) $ hyperedges and contains no complete $ 3 $ -uniform hypergraph on five vertices. Hence the second conjecture asserts that this hypergraph is extremal with this property.

=== References listed by OpenProblemGarden ===
- *[T] P. Turán, Eine Extremalaufgabe aus der Graphentheorie. Mat. Fiz. Lapok 48 (1941), 436--452.

=== Catalog page (statement + literature review) ===
Turán's problem for hypergraphs — Graph-theory open problems

 
 Status
 open
 high confidence
 

 Both of Turán's conjectures for 3-uniform hypergraphs remain unresolved as of 2026. The conjecture that the Turán density of $K_4^{(3)}$ equals $5/9$ is particularly celebrated; the best known upper bound $\pi(K_4^{(3)}) \leq 0.561666$ was established via Razborov's flag-algebra computations before the OPG posting date and has not been improved. Recent work in extremal hypergraph theory (tight-cycle densities, entropy-based approaches, expanded hypergraphs) has advanced surrounding machinery but has not touched these specific conjectures.

 Reviewer notes. Both the PDF of Keevash's survey (Oxford) and the AIM problem-list page were unreachable for readable content (binary PDF, expired certificate). The IMRN 2024 paper on tight-cycle Turán densities explicitly states that the K4^(3) conjecture remains open; the 2024/2026 entropy-meets-Turán paper addresses 'tent' hypergraphs, not K4^(3) or K5^(3). No post-2013 paper with verifiable complete bibliographic details was found that makes direct partial progress on either stated conjecture, so since_posted is empty. The Razborov flag-algebra bound (0.561666) pre-dates the posting and is not included.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Every simple $ 3 $ -uniform hypergraph on $ 3n $ vertices which contains no complete $ 3 $ -uniform hypergraph on four vertices has at most $ \frac12 n^2(5n-3) $ hyperedges.

Conjecture. Every simple $ 3 $ -uniform hypergraph on $ 2n $ vertices which contains no complete $ 3 $ -uniform hypergraph on five vertices has at most $ n^2(n-1) $ hyperedges.

Discussion

Let $ V $ be an $ n $ -set. A $ k $ -uniform hypergraph $ (V,{\cal F}) $ is complete if $ {\cal F}={V \choose k} $ , the set of all $ {n\choose{k}} $ $ k $ -subsets of $ V $ . Let $ \{X,Y,Z\} $ be a partition of $ V $ into three sets which are as nearly equal in size as possible, and let $ {\cal F} $ be the union of $ \{\{x,y,z\}:x\in X, y\in Y, z\in Z\} $ , $ \{\{x_1,x_2,y\}:x_1\in X, x_2\in X, y\in Y\} $ , $ \{\{y_1,y_2,z\}:y_1\in Y, y_2\in Y, z\in Z\} $ , and $ \{\{z_1,z_2,x\}:z_1\in Z, z_2\in Z, x\in X\} $ . This $ 3 $ -uniform hypergraph has $ \frac12 n^2(5n-3) $ hyperedges and contains no complete $ 3 $ -uniform hypergraph on four vertices. Hence the first conjecture asserts that this hypergraph is extremal with this prpoerty. Let $ \{X,Y\} $ be a partition of $ V $ into two sets which are as nearly equal in size as possible, and let $ {\cal F} $ be the set of all $ 3 $ -subsets of $ V $ which intersect both $ X $ and $ Y $ . This $ 3 $ -uniform hypergraph has $ n^2(n-1) $ hyperedges and contains no complete $ 3 $ -uniform hypergraph on five vertices. Hence the second conjecture asserts that this hypergraph is extremal with this property.

Bibliography

★ [T]
 P. Turán, Eine Extremalaufgabe aus der Graphentheorie. Mat. Fiz. Lapok 48 (1941), 436--452.
