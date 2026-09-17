Attack the following open graph-theory problem.

Catalog id: list_total_colouring_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_total_colouring_conjecture/
Original entry: http://www.openproblemgarden.org/op/list_total_colouring_conjecture
Problem attributed to: Borodin, Oleg V., Kostochka, Alexandr V., Woodall, Douglas R. (posted 2013-08-29)

=== Problem statement (OpenProblemGarden) ===
Title: List Total Colouring Conjecture
Conjecture If $ G $ is the total graph of a multigraph, then $ \chi_\ell(G)=\chi(G) $ .

=== Discussion / context (OpenProblemGarden) ===
The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is defined here . Given a multigraph $ H $ , the total graph $ T(H) $ of $ H $ is a graph on vertex set $ V(T(H)):=V(H)\cup E(H) $ where \item two elements of $ V(H) $ are adjacent in $ T(H) $ if and only if they are adjacent in $ H $ ; \item two elements of $ E(H) $ are adjacent in $ T(H) $ if and only if they share an endpoint; \item an element of $ V(H) $ is adjacent to an element of $ E(H) $ in $ T(H) $ if it is incident with it. This problem is related to the List (Edge) Colouring Conjecture as well as the Total Colouring Conjecture. Kostochka and Woodall [KW] conjectured that $ \chi_\ell(G^2)=\chi(G^2) $ for every graph $ G $ ; this was known as the List Square Colouring Conjecture. It is stronger than the List Total Colouring Conjecture since, given a multigraph $ H $ , the total graph of $ H $ can be obtained by subdividing each edge of $ H $ and taking the square. Moreover, the graph obtained from $ H $ by subdividing each edge is bipartite and one part of the bipartition consists of vertices of degree $ 2 $ . Thus, the List Total Colouring Conjecture corresponds to this (very) special case of the List Square Colouring Conjecture. However, the List Square Colouring Conjecture is not true in general. For a family of counterexamples, see the paper of Kim and Park [KP].

=== References listed by OpenProblemGarden ===
- *[BKW] O. V. Borodin, A. V. Kostochka, and D. R. Woodall. List edge and list totalcolourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.
- [KW] A. V. Kostochka and D. R. Woodall. Choosability conjectures and multicircuits. Discrete Math., 240(1-3):123–143, 2001.
- [KP] Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture, submitted.

=== Catalog page (statement + literature review) ===
List Total Colouring Conjecture — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The List Total Colouring Conjecture — that $\chi_\ell(G)=\chi(G)$ whenever $G$ is the total graph of a multigraph — remains open. The stronger List Square Colouring Conjecture was already known to be false at the time of posting (Kim–Park 2013, cited in the problem statement itself); subsequent work by Hasanvand (2022) extended those counterexamples to bipartite planar graphs and their line graphs, but neither result bears on the LTCC. No proof or disproof of the LTCC has been identified in the post-2013 literature.

 Cited literature (2)

 
 
 
partial The List Square Coloring Conjecture fails for bipartite planar graphs and their line graphs
 (2022)
 

 
 Morteza Hasanvand · arXiv preprint · arXiv:2211.00622

Extends the failure of the List Square Colouring Conjecture (the strictly stronger conjecture) to bipartite planar graphs and their line graphs; explicitly notes the LTCC remains open and motivates revised restricted versions.
 

 
 
partial On the Alon-Tarsi Number of Some Line and Total graphs
 (2023)
 

 
 S. Prajnanaswaroopa · arXiv preprint · arXiv:2312.09951

Establishes ATN(T(G)) ≤ Δ(G)+3 for any graph G, giving a weak upper bound on the list chromatic number of total graphs; does not prove χ_ℓ(T(H))=χ(T(H)) for multigraph total graphs.
 

 

 Reviewer notes. The Kim–Park counterexamples to the List Square Colouring Conjecture (arXiv:1305.2566, submitted May 2013) predate the OPG posting and are already cited in the problem statement, so they are not counted as post-posting results. The Hasanvand (2022) paper is directly about the LSCC (not LTCC) but is included as it is the most relevant post-2013 development in the surrounding area. The Prajnanaswaroopa (2023) paper provides a bound Δ+3 on the Alon-Tarsi number of total graphs, which is weaker than what would be needed for the LTCC. No special-case proof of the LTCC for specific multigraph families was found in the post-2013 search.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. If $ G $ is the total graph of a multigraph, then $ \chi_\ell(G)=\chi(G) $ .

Keywords:
list coloring · Total coloring · total graphs

Discussion

The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is defined here . Given a multigraph $ H $ , the total graph $ T(H) $ of $ H $ is a graph on vertex set $ V(T(H)):=V(H)\cup E(H) $ where \item two elements of $ V(H) $ are adjacent in $ T(H) $ if and only if they are adjacent in $ H $ ; \item two elements of $ E(H) $ are adjacent in $ T(H) $ if and only if they share an endpoint; \item an element of $ V(H) $ is adjacent to an element of $ E(H) $ in $ T(H) $ if it is incident with it. This problem is related to the List (Edge) Colouring Conjecture as well as the Total Colouring Conjecture. Kostochka and Woodall [KW] conjectured that $ \chi_\ell(G^2)=\chi(G^2) $ for every graph $ G $ ; this was known as the List Square Colouring Conjecture. It is stronger than the List Total Colouring Conjecture since, given a multigraph $ H $ , the total graph of $ H $ can be obtained by subdividing each edge of $ H $ and taking the square. Moreover, the graph obtained from $ H $ by subdividing each edge is bipartite and one part of the bipartition consists of vertices of degree $ 2 $ . Thus, the List Total Colouring Conjecture corresponds to this (very) special case of the List Square Colouring Conjecture. However, the List Square Colouring Conjecture is not true in general. For a family of counterexamples, see the paper of Kim and Park [KP].

Bibliography

★ [BKW]
 O. V. Borodin, A. V. Kostochka, and D. R. Woodall. List edge and list totalcolourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.

 [KW]
 A. V. Kostochka and D. R. Woodall. Choosability conjectures and multicircuits. Discrete Math., 240(1-3):123–143, 2001.

 [KP]
 Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture, submitted.

Related conjectures

 
 related to
 Choosability of Graph Powers
 open
 The source page explicitly says these questions 'are also related to the so-called List Total Colouring Conjecture'. Both descend from the disproved List Square Colouring Conjecture ch(G^2)=chi(G^2): LTCC is its special case on squares of subdivisions (total graphs), Noel's question is a weakened o(k^2)-bound version for all graphs. No implication either way: a positive answer to Noel's question allows a superlinear gap, far weaker than the exact equality LTCC demands on total graphs; and LTCC, restricted to total graphs, cannot bound ch(G^2) for general G. Explicitly stated relatedness, no derivable implication: related_only.
 

 
 related to
 Total Colouring Conjecture
 partial
 Both conjectures concern the same object, since chi''(H) = chi(T(H)). But they assert logically independent things: LTCC says the list chromatic number of a total graph equals its chromatic number (choosability = colorability), while TCC bounds that chromatic number by Delta(H)+2. Truth of LTCC gives no bound on chi(T(H)), and truth of TCC says nothing about list colorings, so neither implies the other. The OPG context itself only says the problem 'is related to ... the Total Colouring Conjecture'. (Note: their conjunction would give chi_ell(T(H)) <= Delta+2, but separately no implication holds.)
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
