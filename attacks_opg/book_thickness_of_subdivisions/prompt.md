Attack the following open graph-theory problem.

Catalog id: book_thickness_of_subdivisions
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/book_thickness_of_subdivisions/
Original entry: http://www.openproblemgarden.org/op/book_thickness_of_subdivisions
Problem attributed to: Blankenship, Robin, Oporowski, Bogdan (posted 2009-01-19)

=== Problem statement (OpenProblemGarden) ===
Title: Book Thickness of Subdivisions
Let $ G $ be a finite undirected simple graph. A $ k $ -page book embedding of $ G $ consists of a linear order $ \preceq $ of $ V(G) $ and a (non-proper) $ k $ -colouring of $ E(G) $ such that edges with the same colour do not cross with respect to $ \preceq $ . That is, if $ v\prec x\prec w\prec y $ for some edges $ vw,xy\in E(G) $ , then $ vw $ and $ xy $ receive distinct colours. One can think that the vertices are placed along the spine of a book, and the edges are drawn without crossings on the pages of the book. The book thickness of $ G $ , denoted by bt $ (G) $ is the minimum integer $ k $ for which there is a $ k $ -page book embedding of $ G $ . Let $ G' $ be the graph obtained by subdividing each edge of $ G $ exactly once. Conjecture There is a function $ f $ such that for every graph $ G $ , $$ \text{bt}(G) \leq f( \text{bt}(G') )\enspace. $$

=== Discussion / context (OpenProblemGarden) ===
The conjecture is due to [B099]. The conjecture is true for complete graphs [BO99,EM99,E02]. The conjecture is discussed in depth in [DW05].

=== References listed by OpenProblemGarden ===
- *[BO99] Robin Blankenship and Bogdan Oporowski. Drawing Subdivisions Of Complete And Complete Bipartite Graphs On Books, Technical Report 1999-4, Department of Mathematics, Louisiana State University, 1999.
- [DW05] Vida Dujmovic and David Wood. Stacks, queues and tracks: Layouts of graph subdivisions. Discrete Mathematics & Theoretical Computer Science 7:155-202, 2005.
- [EM99] Hikoe Enomoto and Miki Shimabara Miyauchi. Embedding graphs into a three page book with crossings of edges over the spine. SIAM J. Discrete Math., 12(3):337–341, 1999.
- [E02] David Eppstein. Separating thickness from geometric thickness. In Proc. 10th International Symp. on Graph Drawing (GD ’02), pp. 150–161. vol. 2528 of Lecture Notes in Comput. Sci. Springer, 2002.

=== Catalog page (statement + literature review) ===
Book Thickness of Subdivisions — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 The Blankenship–Oporowski conjecture has been disproved. Dujmović, Eppstein, Hickingbotham, Morin, and Wood (2022) exhibited a family of graphs whose Cartesian products of stars and triangular tilings have unbounded stack-number (= book thickness), yet subdividing each edge into six-edge paths reduces the book thickness to three. Consequently, no function $f$ can satisfy $\text{bt}(G) \leq f(\text{bt}(G'))$ for all graphs $G$ and subdivisions $G'$.

 Cited literature (1)

 
 
 
counterexample Stack-number is not bounded by queue-number
 (2022)
 

 
 Vida Dujmović, David Eppstein, Robert Hickingbotham, Pat Morin, David R. Wood · Combinatorica · arXiv:2011.04195 · doi:10.1007/s00493-021-4585-7

Constructs graphs with queue-number at most 4 but unbounded stack-number; since bounded queue-number implies bounded stack-number for constant subdivisions (by Dujmović–Wood 2005), these graphs have unbounded book thickness while their constant-subdivision has book thickness 3, directly disproving the Blankenship–Oporowski conjecture.
 

 

 Reviewer notes. The arXiv preprint appeared in November 2020 (arXiv:2011.04195); the journal version appeared in Combinatorica 42:151–164, 2022. Wikipedia's dedicated 'Blankenship–Oporowski conjecture' page and the blog post by Eppstein both confirm the disproof. The Springer/DOI page for the Combinatorica article was inaccessible (authentication redirect), so the arXiv abstract page was used as the primary verified URL. The paper also resolves the Heath–Leighton–Rosenberg (1992) open problem as a corollary.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 1165s.
 

Conjecture. There is a function $ f $ such that for every graph $ G $ , $$ \text{bt}(G) \leq f( \text{bt}(G') )\enspace. $$

Keywords:
book embedding · book thickness

Discussion

The conjecture is due to [B099]. The conjecture is true for complete graphs [BO99,EM99,E02]. The conjecture is discussed in depth in [DW05].

Bibliography

★ [BO99]
 Robin Blankenship and Bogdan Oporowski. Drawing Subdivisions Of Complete And Complete Bipartite Graphs On Books , Technical Report 1999-4, Department of Mathematics, Louisiana State University, 1999.

 [DW05]
 Vida Dujmovic and David Wood. Stacks, queues and tracks: Layouts of graph subdivisions . Discrete Mathematics & Theoretical Computer Science 7:155-202, 2005.
 Stacks, queues and tracks: Layouts of graph subdivisions

 [EM99]
 Hikoe Enomoto and Miki Shimabara Miyauchi. Embedding graphs into a three page book with $ O(M \log N) $ crossings of edges over the spine . SIAM J. Discrete Math., 12(3):337–341, 1999.
 Embedding graphs into a three page book with crossings of edges over the spine

 [E02]
 David Eppstein. Separating thickness from geometric thickness . In Proc. 10th International Symp. on Graph Drawing (GD ’02), pp. 150–161. vol. 2528 of Lecture Notes in Comput. Sci. Springer, 2002.
