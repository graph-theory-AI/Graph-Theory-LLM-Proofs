Attack the following open graph-theory problem.

Catalog id: seymours_second_neighbourhood_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/seymours_second_neighbourhood_conjecture/
Original entry: http://www.openproblemgarden.org/op/seymours_second_neighbourhood_conjecture
Problem attributed to: Seymour, Paul D. (posted 2007-10-09)

=== Problem statement (OpenProblemGarden) ===
Title: Seymour's Second Neighbourhood Conjecture
Conjecture Any oriented graph has a vertex whose outdegree is at most its second outdegree.

=== Discussion / context (OpenProblemGarden) ===
By the $ n $ th outdegree of $ v $ , we mean the number of vertices for which the minimal outward-directed path from $ v $ to them is of length $ n $ . Chen, Shen, and Yuster [CSY] proved that in any oriented graph there is a vertex whose second outdegree is at least $ \gamma $ times its outdegree, where $ \gamma=0.657298... $ is the unique real root of $ 2x^3+x^2 -1=0 $ . This conjecture implies a special case of the \Oprefnum[Caccetta-Häggkvist Conjecture]{46385}.

=== References listed by OpenProblemGarden ===
- [ASY] Chen, G.; Shen, J.; Yuster, R. Second neighborhood via first neighborhood in digraphs, Annals of Combinatorics, 7 (2003), 15--20.
- [F] Fisher, David C. Squaring a tournament: a proof of Dean's conjecture. J. Graph Theory 23 (1996), no. 1, 43--48.
- [KL] Kaneko, Yoshihiro; Locke, Stephen C. The minimum degree approach for Paul Seymour's distance 2 conjecture. Proceedings of the Thirty-second Southeastern International Conference on Combinatorics, Graph Theory and Computing (Baton Rouge, LA, 2001). Congr. Numer. 148 (2001), 201--206.

=== Catalog page (statement + literature review) ===
Seymour's Second Neighbourhood Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Seymour's Second Neighbourhood Conjecture remains open in general. Meaningful partial progress since 2007 includes confirmation for almost all orientations of random graphs $G(n,p)$ with fixed $p < 1/2$, for tournaments missing two stars, and via exhaustive computation for all oriented graphs of order at most seven. Structural reductions show that any minimum counterexample must be strongly connected with bounded minimum outdegree.

 Cited literature (4)

 
 
 
partial Seymour's Second Neighborhood Conjecture for orientations of (pseudo)random graphs
 (2022)
 

 
 Fábio Botler, Phablo F. S. Moura, Tássio Naia · arXiv preprint · arXiv:2211.06540

Proves the conjecture holds asymptotically almost surely for all orientations of G(n,p) when lim sup p < 1/4, and for random orientations of pseudorandom graphs satisfying certain density conditions.
 

 
 
partial Seymour's second neighbourhood conjecture: random graphs and reductions
 (2024)
 

 
 Alberto Espuny Díaz, António Girão, Bertille Granet, Gal Kronenberg · arXiv preprint · arXiv:2403.02842 · doi:10.1002/rsa.21251

Proves the conjecture for almost all orientations of G(n,p) for any fixed p in [0, 1/2), and shows any minimum counterexample must be strongly connected with bounded minimum outdegree.
 

 
 
partial About the second neighborhood conjecture for tournaments missing two stars or disjoint paths
 (2024)
 

 
 Moussa Daamouch, Salman Ghazal, Darine Al-Mniny · arXiv preprint · arXiv:2406.03635

Proves Seymour's Second Neighbourhood Conjecture for tournaments missing two stars, and investigates the conjecture for tournaments missing disjoint paths of length 2.
 

 
 
partial Seymour's Second Neighbourhood Conjecture for Oriented Graphs of Order at Most Seven and Split-Twin Extensions
 (2026)
 

 
 Stanisław M. S. Halkiewicz · arXiv preprint · arXiv:2601.21563

Computationally verifies the conjecture for all oriented graphs of order at most 7, and introduces a split-twin extension operation preserving Seymour vertices, generating infinite inductively-defined families satisfying the conjecture.
 

 

 Reviewer notes. A preprint (arXiv:2501.00614, 13 revisions as of Feb 2026) by Charles N. Glover claims a complete proof via the 'Graph Level Order' framework but is not peer-reviewed and should not be treated as a confirmed proof. The published journal version of arXiv:2403.02842 appears in Random Structures & Algorithms (2025, DOI 10.1002/rsa.21251) per search results, but that Wiley page returned HTTP 403 so is not in verified_urls. A 2026 Graphs and Combinatorics paper by Wang and Lu (DOI 10.1007/s00373-026-03014-y) on 'Seymour's second neighborhood conjecture for some oriented graphs' could not be fully verified due to an authentication redirect and is therefore excluded from since_posted.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. Any oriented graph has a vertex whose outdegree is at most its second outdegree.

Keywords:
Caccetta-Häggkvist · neighbourhood · second · Seymour

Discussion

By the $ n $ th outdegree of $ v $ , we mean the number of vertices for which the minimal outward-directed path from $ v $ to them is of length $ n $ . Chen, Shen, and Yuster [CSY] proved that in any oriented graph there is a vertex whose second outdegree is at least $ \gamma $ times its outdegree, where $ \gamma=0.657298... $ is the unique real root of $ 2x^3+x^2 -1=0 $ . This conjecture implies a special case of the \Oprefnum[Caccetta-Häggkvist Conjecture]{46385}.

Bibliography

 [ASY]
 Chen, G.; Shen, J.; Yuster, R. Second neighborhood via first neighborhood in digraphs, Annals of Combinatorics, 7 (2003), 15--20.

 [F]
 Fisher, David C. Squaring a tournament: a proof of Dean's conjecture. J. Graph Theory 23 (1996), no. 1, 43--48.

 [KL]
 Kaneko, Yoshihiro; Locke, Stephen C. The minimum degree approach for Paul Seymour's distance 2 conjecture. Proceedings of the Thirty-second Southeastern International Conference on Combinatorics, Graph Theory and Computing (Baton Rouge, LA, 2001). Congr. Numer. 148 (2001), 201--206.

Related conjectures

 
 related to
 Caccetta-Häggkvist Conjecture
 open
 Both OPG pages state the connection explicitly, but it is only a partial implication: Seymour's Second Neighbourhood Conjecture implies the Behzad-Chartrand-Wall / triangle case of Caccetta-Haggkvist (min in- and out-degree >= n/3 forces a directed cycle of length <= 3), via the standard argument that a vertex with second outneighbourhood at least as large as its outneighbourhood in a triangle-free digraph would force more than n vertices. SSNC does not imply the full Caccetta-Haggkvist conjecture (general r, cycles of length ceil(n/r)), so 'implies' would overstate it; the correct classification is a well-documented partial-implication link, i.e. related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
