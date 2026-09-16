Attack the following open graph-theory problem.

Catalog id: arc_disjoint_strongly_connected_spanning_subdigraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/arc_disjoint_strongly_connected_spanning_subdigraphs/
Original entry: http://www.openproblemgarden.org/op/arc_disjoint_strongly_connected_spanning_subdigraphs
Problem attributed to: Bang-Jensen, Joergen, Yeo, Anders (posted 2013-03-02)

=== Problem statement (OpenProblemGarden) ===
Title: Arc-disjoint strongly connected spanning subdigraphs
Conjecture There exists an ineteger $ k $ so that every $ k $ -arc-connected digraph contains a pair of arc-disjoint strongly connected spanning subdigraphs?

=== Discussion / context (OpenProblemGarden) ===
Bang-Jensen and Yeo [BY] proved the conjecture for several classes like tournaments. There is stronger conjecture for tournaments . Yeo (See [BG, Theorem 13.10.1]) showed that it is NP-complete to decide whether a 2-regular digraph has two arc-disjoint strongly connected spanning subdigraphs. A similar question can be asked about arc-disjoint out-branching and in-branching . Several related problems are mentioned in the survey of Bang-Jensen and Kriesell [BK].

=== References listed by OpenProblemGarden ===
- [BG] J. Bang-Jensen, G. Gutin, Digraphs: Theory, Algorithms and Applications, 2nd. ed., Springer Verlag (2009).
- [BK] J. Bang-Jensen, M. Kriesell, Disjoint sub(di)graphs in digraphs, Electronic Notes in Discrete Mathematics 34 (2009), 179-183.
- *[BY] J. Bang-Jensen, A. Yeo, Decomposing k-arc-strong tournaments into strong spanning subdigraphs, Combinatorica 24 (2004), 331-349.

=== Catalog page (statement + literature review) ===
Arc-disjoint strongly connected spanning subdigraphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The conjecture — that there exists a fixed $k$ such that every $k$-arc-connected digraph contains two arc-disjoint strongly connected spanning subdigraphs — remains open for general digraphs. Post-2013 work has extended partial results to broader classes: Sun, Gutin, and Ai (2018) handled digraph compositions and products, and Bang-Jensen, Gutin, and Yeo (2019/2020) gave a complete characterization of which semicomplete compositions admit a strong arc decomposition, solving a problem from the 2018 paper but leaving the general conjecture untouched.

 Cited literature (2)

 
 
 
partial Arc-disjoint strong spanning subdigraphs in compositions and products of digraphs
 (2018)
 

 
 Yuefang Sun, Gregory Gutin, Jiangdong Ai · arXiv preprint · arXiv:1812.08809

Establishes sufficient conditions for digraph compositions (with semicomplete base) and certain Cartesian/strong products of strong digraphs to possess a 'good decomposition' (arc set splits into two arc-disjoint strongly connected spanning subdigraphs).
 

 
 
partial Arc-disjoint Strong Spanning Subdigraphs of Semicomplete Compositions
 (2019)
 

 
 Joergen Bang-Jensen, Gregory Gutin, Anders Yeo · arXiv preprint (published Journal of Graph Theory, 2020) · arXiv:1903.12225

Provides a complete characterization of strong semicomplete digraph compositions that have a strong arc decomposition: they must be 2-arc-strong and not isomorphic to four specific exceptional digraphs; this solves the open problem of Sun–Gutin–Ai (2018).
 

 

 Reviewer notes. The Wiley DOI page (10.1002/jgt.22568) and the ScienceDirect paper (pii/S0304397512002204) both returned HTTP 403 and could not be verified; accordingly they are not cited. The published year for arXiv:1903.12225 in J. Graph Theory (2020) is inferred from search result snippets, not from a directly fetched journal page. No paper found in these searches claims to resolve the general k-arc-connected conjecture; all post-2013 progress is confined to structured special classes.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 136s.
 

Conjecture. There exists an ineteger $ k $ so that every $ k $ -arc-connected digraph contains a pair of arc-disjoint strongly connected spanning subdigraphs?

Discussion

Bang-Jensen and Yeo [BY] proved the conjecture for several classes like tournaments. There is stronger conjecture for tournaments . Yeo (See [BG, Theorem 13.10.1]) showed that it is NP-complete to decide whether a 2-regular digraph has two arc-disjoint strongly connected spanning subdigraphs. A similar question can be asked about arc-disjoint out-branching and in-branching . Several related problems are mentioned in the survey of Bang-Jensen and Kriesell [BK].

Bibliography

 [BG]
 J. Bang-Jensen, G. Gutin, Digraphs: Theory, Algorithms and Applications, 2nd. ed., Springer Verlag (2009).

 [BK]
 J. Bang-Jensen, M. Kriesell, Disjoint sub(di)graphs in digraphs, Electronic Notes in Discrete Mathematics 34 (2009), 179-183.

★ [BY]
 J. Bang-Jensen, A. Yeo, Decomposing k-arc-strong tournaments into strong spanning subdigraphs, Combinatorica 24 (2004), 331-349.

Related conjectures

 
 implies
 Arc-disjoint out-branching and in-branching
 partial
 Suppose k witnesses the source conjecture, and let D be a k-arc-strong digraph with specified vertices u, v. Then D contains arc-disjoint strongly connected spanning subdigraphs D1 and D2. Any strong spanning subdigraph contains, for every choice of root, both an out-branching and an in-branching (take a BFS out-tree from the root, resp. an in-tree to the root, which exist by strong connectivity and spanning-ness). Take an out-branching rooted at u inside D1 and an in-branching rooted at v inside D2; they are arc-disjoint because D1 and D2 are. Hence the same k witnesses the target conjecture. Both OPG pages cross-reference each other as similar questions but the implication in this direction is rigorous and self-contained.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
