Attack the following open graph-theory problem.

Catalog id: caccetta_haggkvist_conjecture
Source: OpenProblemGarden (importance: Outstanding ✭✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/caccetta_haggkvist_conjecture/
Original entry: http://www.openproblemgarden.org/op/caccetta_haggkvist_conjecture
Problem attributed to: Caccetta, L., Häggkvist, Roland (posted 2013-02-28)

=== Problem statement (OpenProblemGarden) ===
Title: Caccetta-Häggkvist Conjecture
Conjecture Every simple digraph of order $ n $ with minimum outdegree at least $ r $ has a cycle with length at most $ \lceil n/r\rceil $

=== Discussion / context (OpenProblemGarden) ===
It is one of the most famous conjectures in graph theory. It has many alternative formulations and lots of work have been done around it. Many interesting conjectures are related to it. See [Sul]. It is in particular implied by a conjecture of Thomassé and Hoàng-Reed Conjecture . The Caccetta-Häggkvist Conjecture is a generalization of an earlier conjecture of Behzad, Chartrand, and Wall, who conjectured it only for diregular digraphs. Caccetta-H äggkvist Conjecture has been proved for $ r\leq \sqrt{n/2} $ by Shen [She1]. For $ r\geq n/2 $ it is trivial. But already for $ r=n/3 $ , it is still open as well as Behzad-Chartrand-Wall Conjecture Conjecture Every simple $ n $ -vertex digraph with minimum outdegree at least $ r/3 $ and minimum indegree at least $ r/3 $ has a cycle with length at most $ 3 $ . This conjecture would be implied by Seymour's Second Neighbourhood Conjecure . Shen [She2] also proved the following approximate version. Theorem Every simple digraph of order $ n $ with minimum outdegree at least $ r $ has a cycle with length at most $ n/r + 73 $ . Bollobás and Scott [BS] proposed a weighted version of the Caccetta-Häggkvist Conjecture. Conjecture Let $ w:E(D) \rightarrow [0,1] $ be a weight function on the arcs of a digraph $ D $ . If $ \sum_{u\in N^-(v)} w(uv) \geq 1 $ and $ \sum_{u\in N^+(v)} w(vu) \geq 1 $ for all $ v\in V(D) $ , then there is a directed cycle in $ D $ of total weight at least 1. They gave a nice proof that there is a directed path of total weight at least 1.

=== References listed by OpenProblemGarden ===
- [BCW] M. Behzad, G. Chartrand, and C. Wall. On minimal regular digraphs with given girth. Fundamenta Mathematicae, 69:227–231, 1970.
- [BS] B. Bollobás and A. D. Scott, A proof of a conjecture of {B}ondy concerning paths in weighted digraphs. J. Combin. Theory Ser. B, 66:283-292, 1996.
- *[CH] L. Caccetta and R. Häggkvist. On minimal digraphs with given girth. Congressus Numerantium, XXI, 1978
- [She1J. Shen. On the girth of digraphs. Discrete Math, 211(1-3):167–181, 2000.
- [She2] J. Shen. On the Caccetta-Häggkvist conjecture. Graphs and Combinatorics, 18(3):645–654, 2002.
- [Sul] Blair D. Sullivan: A Summary of Problems and Results related to the Caccetta-Häggkvist Conjecture

=== Catalog page (statement + literature review) ===
Caccetta-Häggkvist Conjecture — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The Caccetta-Häggkvist conjecture remains open in its full generality, including the well-known case $r = n/3$ (existence of a directed triangle). Post-2013 work has produced only partial results: improvements on the digraph triangle bound, proofs for restricted classes (e.g., small independence number, forbidden subgraphs), counterexamples to a stronger conjecture of Thomassé, and progress on Aharoni's rainbow generalization (now resolved up to a constant factor and up to an additive constant).

 Cited literature (9)

 
 
 
partial On the length of directed paths in digraphs
 (2024)
 

 
 Yangyang Cheng, Peter Keevash · arXiv preprint · arXiv:2402.16776

Disproves Thomassé's strengthening of the Caccetta-Häggkvist conjecture for all girth $g \geq 4$ and proves new lower bounds on directed path lengths in digraphs of given minimum out-degree and girth.
 

 
 
partial Improved bounds for the triangle case of Aharoni's rainbow generalization of the Caccetta-Häggkvist conjecture
 (2022)
 

 
 Patrick Hompe, Zishen Qu, Sophie Spirkl · arXiv preprint · arXiv:2206.10733

Establishes improved triangle-existence bounds in Aharoni's rainbow generalization of the Caccetta-Häggkvist conjecture, e.g. that $(1.1077, 1/3)$ is triangular and $(1, 0.3988)$ is triangular.
 

 
 
partial Further approximations for Aharoni's rainbow generalization of the Caccetta-Häggkvist conjecture
 (2021)
 

 
 Patrick Hompe, Sophie Spirkl · arXiv preprint · arXiv:2105.03373

Proves Aharoni's rainbow version of the Caccetta-Häggkvist conjecture holds when each color class has size $\Omega(k)$, improving the previous $\Omega(k \log k)$ requirement and bringing the result to within a constant factor of the conjecture.
 

 
 
partial Aharoni's rainbow cycle conjecture holds up to an additive constant
 (2022)
 

 
 Patrick Hompe, Tony Huynh · arXiv preprint · arXiv:2212.05697

Shows that Aharoni's rainbow generalization of the Caccetta-Häggkvist conjecture holds up to an additive constant: edge-colored graphs with $n$ vertices and $n$ color classes of size at least $r$ contain a rainbow cycle of length at most $n/r + \alpha_r$.
 

 
 
partial Short rainbow cycles in edge-colored graphs
 (2023)
 

 
 Xiaozheng Chen, Shanshan Guo, Fei Huang · arXiv preprint · arXiv:2311.12302

Proves that for edge-colored graphs on $n$ vertices with $n$ color classes (each a matching of size 2 or a triangle) of which at least $\alpha n$ have a given form for $\alpha > 1/2$, the graph contains a rainbow cycle of length $O(\log n)$, contributing to Aharoni's rainbow version of the Caccetta-Häggkvist conjecture.
 

 
 
partial Decomposing and colouring some locally semicomplete digraphs
 (2022)
 

 
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit · arXiv preprint · arXiv:2103.07886

Proves that every locally in-tournament digraph satisfies the Caccetta-Häggkvist conjecture, deducing it from the structural decomposition theorem (Theorem 2.3).
 

 
 
partial Improved bounds for the triangle case of Aharoni's rainbow generalization of the Caccetta-Häggkvist conjecture
 (2023)
 

 
 Patrick Hompe, Zishen Qu, Sophie Spirkl · arXiv preprint · arXiv:2206.10733

Does not prove new bounds for the conjecture directly; instead uses existing approximations for the triangle case as a tool to establish improved triangularity bounds for Aharoni's rainbow generalization, and notes that improvements to those approximations would yield improvements to Theorem 3.
 

 
 
partial Short rainbow cycles in graphs and matroids
 (2020)
 

 
 Matt DeVos, Matthew Drescher, Daryl Funk, Sebastián González Hermosillo de la Maza, Krystal Guo, Tony Huynh, Bojan Mohar, Amanda Montejano · arXiv preprint · arXiv:1806.00825

Proves the $r=2$ case of Aharoni's rainbow strengthening of this conjecture (Theorem 5), which implies the $r=2$ case of Caccetta-Häggkvist. Also introduces Conjecture 4, a weaker rainbow properly-coloured-cycle condition shown to imply the full Caccetta-Häggkvist conjecture.
 

 
 
partial Short directed cycles in bipartite digraphs
 (2019)
 

 
 Paul Seymour, Sophie Spirkl · arXiv preprint · arXiv:1809.08324

Shows that the Caccetta-Häggkvist conjecture implies the bipartite analogue Conjecture 1.2; uses CH-approximations to prove 1.2 for $k = 1, 2, 3, 4, 6$, and all $k \geq 224{,}539$.
 

 

 Reviewer notes. The original Caccetta-Häggkvist conjecture is unresolved, including the central r = n/3 (triangle) case. Most recent activity post-2013 concerns either Aharoni's rainbow generalization or strengthenings/restrictions (small independence number, forbidden subgraphs). The 2024 Cheng-Keevash paper disproves a strictly stronger conjecture of Thomassé but does not affect the original Caccetta-Häggkvist statement. The SIAM page for Devlin/Aharoni-style 'Nonuniform Degrees' rainbow paper returned 403 and was not directly verified, so it is not cited.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. Every simple digraph of order $ n $ with minimum outdegree at least $ r $ has a cycle with length at most $ \lceil n/r\rceil $

Discussion

It is one of the most famous conjectures in graph theory. It has many alternative formulations and lots of work have been done around it. Many interesting conjectures are related to it. See [Sul]. It is in particular implied by a conjecture of Thomassé and Hoàng-Reed Conjecture . The Caccetta-Häggkvist Conjecture is a generalization of an earlier conjecture of Behzad, Chartrand, and Wall, who conjectured it only for diregular digraphs. Caccetta-H äggkvist Conjecture has been proved for $ r\leq \sqrt{n/2} $ by Shen [She1]. For $ r\geq n/2 $ it is trivial. But already for $ r=n/3 $ , it is still open as well as Behzad-Chartrand-Wall Conjecture Conjecture Every simple $ n $ -vertex digraph with minimum outdegree at least $ r/3 $ and minimum indegree at least $ r/3 $ has a cycle with length at most $ 3 $ . This conjecture would be implied by Seymour's Second Neighbourhood Conjecure . Shen [She2] also proved the following approximate version. Theorem Every simple digraph of order $ n $ with minimum outdegree at least $ r $ has a cycle with length at most $ n/r + 73 $ . Bollobás and Scott [BS] proposed a weighted version of the Caccetta-Häggkvist Conjecture. Conjecture Let $ w:E(D) \rightarrow [0,1] $ be a weight function on the arcs of a digraph $ D $ . If $ \sum_{u\in N^-(v)} w(uv) \geq 1 $ and $ \sum_{u\in N^+(v)} w(vu) \geq 1 $ for all $ v\in V(D) $ , then there is a directed cycle in $ D $ of total weight at least 1. They gave a nice proof that there is a directed path of total weight at least 1.

Bibliography

 [BCW]
 M. Behzad, G. Chartrand, and C. Wall. On minimal regular digraphs with given girth. Fundamenta Mathematicae, 69:227–231, 1970.

 [BS]
 B. Bollobás and A. D. Scott, A proof of a conjecture of {B}ondy concerning paths in weighted digraphs. J. Combin. Theory Ser. B, 66:283-292, 1996.

★ [CH]
 L. Caccetta and R. Häggkvist. On minimal digraphs with given girth. Congressus Numerantium, XXI, 1978

 [?]
 [She1J. Shen. On the girth of digraphs. Discrete Math, 211(1-3):167–181, 2000.

 [She2]
 J. Shen. On the Caccetta-Häggkvist conjecture. Graphs and Combinatorics, 18(3):645–654, 2002.

 [Sul]
 Blair D. Sullivan: A Summary of Problems and Results related to the Caccetta-Häggkvist Conjecture
 A Summary of Problems and Results related to the Caccetta-Häggkvist Conjecture

Related conjectures

 
 implied by
 Asymmetric out-degree girth bound for bipartite digraphs
 open
 Stated in the paper's abstract (the asymmetric conjecture "implies the Caccetta-Häggkvist conjecture (set beta>0 and very small)"), and verifiable directly: given a digraph D on n vertices with min out-degree r, build a bipartite digraph with parts A, B both copies of V(D), arcs v_A -> v_B for every vertex v and u_B -> v_A for every arc uv of D. Vertices of A have out-degree 1 = beta|B| with beta = 1/n; vertices of B have out-degree >= r = alpha|A| with alpha = r/n. Take k = ceil(n/r): then k*alpha + beta = ceil(n/r)*r/n + 1/n >= 1 + 1/n > 1, so the asymmetric conjecture gives a directed cycle of length <= 2k, which projects to a closed walk of length <= k in D, hence a cycle of length <= ceil(n/r). Direction as claimed.
 

 
 implies
 Bipartite Caccetta–Häggkvist short cycle
 partial
 Explicitly stated in the source paper's abstract: "The Caccetta-Häggkvist conjecture implies that for every integer k>=1, if G is a bipartite digraph, with n vertices in each part, and every vertex has out-degree more than n/(k+1), then G has a directed cycle of length at most 2k." The target's own context also records this. Note the implication is not a trivial application of CH to the 2n-vertex bipartite digraph (that only yields girth <= 2k+2 after rounding to even length); the paper derives it via an auxiliary digraph, so the confirmation rests on the paper's explicit statement rather than a one-line reduction. Direction is as claimed: CH is the stronger statement here.
 

 
 implied by
 Hoàng-Reed Conjecture
 open
 Assume Hoàng-Reed for k=r on an n-vertex digraph with min outdegree r: it yields cycles C_1,...,C_r where each C_j meets the union of the earlier ones in at most one vertex. Hence |C_1 ∪ ... ∪ C_r| >= sum_i |C_i| - (r-1), and this union has at most n vertices, so sum_i |C_i| <= n + r - 1. The shortest C_i then has length at most floor((n+r-1)/r) = ceil(n/r), which is exactly Caccetta-Häggkvist. The implication is also explicitly stated in both provided contexts (Hoàng-Reed page: 'This conjecture would imply the Caccetta-Häggkvist Conjecture'; C-H page lists Hoàng-Reed as implying it). Direction as claimed.
 

 
 implied by
 Proper-incident short rainbow cycle bound
 open
 Stated in the source's context ('the authors prove that Conjecture 4 implies the Caccetta-Häggkvist conjecture') and the reduction verifies directly. Given a simple digraph D on n vertices with minimum out-degree ≥ r: if D has a digon there is a directed 2-cycle and ⌈n/r⌉ ≥ 2 whenever r < n (r ≥ n is vacuous). Otherwise colour each edge of the underlying simple graph by its tail in D: n colour classes, each of size ≥ r. The source gives a cycle C of length k ≤ ⌈n/r⌉ with no two incident edges of the same colour; since each edge is coloured by one of its endpoints and no vertex of C is the tail of both its incident cycle edges, the edge→tail map is a bijection onto V(C), so C is consistently oriented — a directed cycle of length ≤ ⌈n/r⌉.
 

 
 related to
 Seymour's Second Neighbourhood Conjecture
 partial
 Both OPG pages state the connection explicitly, but it is only a partial implication: Seymour's Second Neighbourhood Conjecture implies the Behzad-Chartrand-Wall / triangle case of Caccetta-Haggkvist (min in- and out-degree >= n/3 forces a directed cycle of length <= 3), via the standard argument that a vertex with second outneighbourhood at least as large as its outneighbourhood in a triangle-free digraph would force more than n vertices. SSNC does not imply the full Caccetta-Haggkvist conjecture (general r, cycles of length ceil(n/r)), so 'implies' would overstate it; the correct classification is a well-documented partial-implication link, i.e. related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
