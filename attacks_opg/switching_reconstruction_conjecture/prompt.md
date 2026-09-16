Attack the following open graph-theory problem.

Catalog id: switching_reconstruction_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/switching_reconstruction_conjecture/
Original entry: http://www.openproblemgarden.org/op/switching_reconstruction_conjecture
Problem attributed to: Stanley, Richard P. (posted 2013-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Switching reconstruction conjecture
Conjecture Every simple graph on five or more vertices is switching-reconstructible.

=== Discussion / context (OpenProblemGarden) ===
To switch a vertex of a simple graph is to exchange its sets of neighbours and non-neighbours. The graph so obtained is called a switching of the graph. The collection of switchings of a graph G is called the switching deck of $ G $ . A graph is switching-reconstructible if every graph with the same deck as $ G $ is isomorphic to $ G $ . There are four pairs of non-isomorphic graphs of order $ 4 $ with the same switching deck. One of them consists of the empty graph and the $ 4 $ -cycle. Stanley [S] proved that a graph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . An analogous problem was posed for digraphs. Instead of complementing the edges at a vertex, one reverses each of its incident arc.

=== References listed by OpenProblemGarden ===
- *[S] R. P. Stanley Reconstruction from vertex-switching. J. Combin. Theory Ser. B, 38 (1985), 132--138.

=== Catalog page (statement + literature review) ===
Switching reconstruction conjecture — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 Stanley proved in 1985 that every simple graph on $n$ vertices is switching-reconstructible when $n \not\equiv 0 \pmod{4}$, and this remains the best known result. The conjecture is still open for $n \equiv 0 \pmod{4}$, $n \geq 8$ (the case $n = 4$ is known to fail). No post-2013 papers establishing progress on this remaining open case were found.

 Reviewer notes. arxiv:2401.01582 ('The Stanley Conjecture Revisited') and arxiv:2309.13870 ('New cases of the Strong Stanley Conjecture') are both about Jack symmetric functions / Littlewood-Richardson coefficients, completely unrelated to graph reconstruction. arxiv:2601.04530 ('On identity Seidel switches', 2026) studies which vertex subsets yield automorphisms under Seidel switching, tangentially related but not addressing reconstruction. arxiv:2403.04263 ('Switching Classes: Characterization and Computation', 2024) studies hereditary class properties under switching, not reconstruction. arxiv:2604.16567 ('Shuffling the Deck', 2026) concerns the classical vertex-deletion reconstruction conjecture, not vertex-switching reconstruction. The OPG page was unreachable (ECONNREFUSED). The core open case—n ≡ 0 (mod 4), n ≥ 8—appears not to have attracted published resolution since Stanley's foundational 1985 paper.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Every simple graph on five or more vertices is switching-reconstructible.

Keywords:
reconstruction

Discussion

To switch a vertex of a simple graph is to exchange its sets of neighbours and non-neighbours. The graph so obtained is called a switching of the graph. The collection of switchings of a graph G is called the switching deck of $ G $ . A graph is switching-reconstructible if every graph with the same deck as $ G $ is isomorphic to $ G $ . There are four pairs of non-isomorphic graphs of order $ 4 $ with the same switching deck. One of them consists of the empty graph and the $ 4 $ -cycle. Stanley [S] proved that a graph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . An analogous problem was posed for digraphs. Instead of complementing the edges at a vertex, one reverses each of its incident arc.

Bibliography

★ [S]
 R. P. Stanley Reconstruction from vertex-switching. J. Combin. Theory Ser. B, 38 (1985), 132--138.
