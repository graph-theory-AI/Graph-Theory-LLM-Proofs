Attack the following open graph-theory problem.

Catalog id: 1811.12252__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1811.12252__01/
Source paper: Graph Isomorphism for $(H_1,H_2)$-free Graphs: An Almost Complete Dicho… (arXiv:1811.12252)

=== Extracted statement (catalog JSON) ===
Title: Open Question: FPT Algorithm for Graph Isomorphism Parameterized by Clique-Width
Whether an FPT algorithm exists for Graph Isomorphism when parameterized by clique-width is still open.

Context:
Lokshtanov et al. [23] gave an FPT algorithm parameterized by treewidth, and Grohe and Schweitzer [20] proved XP membership parameterized by clique-width (i.e., polynomial-time solvability for each fixed clique-width). The question of whether the parameter clique-width admits an FPT algorithm remains unresolved.

=== Catalog page (statement + literature review) ===
Graph Isomorphism FPT by Clique-Width — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 As of 2026 it remains open whether Graph Isomorphism admits an FPT algorithm parameterized by clique-width; the best known result is XP membership due to Grohe and Schweitzer. A 2025 IPEC paper (Blažej, Jana, Ramanujan, Strulo) proves FPT for the new intermediate parameter cograph-modular-treewidth, which lies strictly between treewidth and clique-width, but explicitly confirms that the FPT status for clique-width itself is still open. No W[1]-hardness evidence for clique-width parameterization has been established.

 Cited literature (1)

 
 
 
partial Bridging Treewidth and Clique-Width via Cograph-Modular-Treewidth
 (2025)
 

 
 Václav Blažej, Satyabrata Jana, M. S. Ramanujan, Peter Strulo · 20th International Symposium on Parameterized and Exact Computation (IPEC 2025), LIPIcs · doi:10.4230/LIPIcs.IPEC.2025.18

Introduces cograph-modular-treewidth (strictly between treewidth and clique-width) and proves Graph Isomorphism is FPT for this parameter, while noting the FPT status for clique-width remains open.
 

 

 Reviewer notes. The FPT status of Graph Isomorphism parameterized by clique-width is one of the central open problems in parameterized complexity. No internal references were supplied. The IPEC 2025 paper by Blažej et al. is the closest recent progress, establishing FPT for a strictly intermediate parameter (cograph-modular-treewidth) that does not subsume the full clique-width case.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Whether an FPT algorithm exists for Graph Isomorphism when parameterized by clique-width is still open.

Context

Lokshtanov et al. [23] gave an FPT algorithm parameterized by treewidth, and Grohe and Schweitzer [20] proved XP membership parameterized by clique-width (i.e., polynomial-time solvability for each fixed clique-width). The question of whether the parameter clique-width admits an FPT algorithm remains unresolved.

Notes. Stated as an existing open problem in the introduction without attribution to specific authors; not a formally labelled environment. PDF source — math notation appears clean for this item.

Source paper

 Graph Isomorphism for $(H_1,H_2)$-free Graphs: An Almost Complete Dichotomy
 Marthe Bonamy, Nicolas Bousquet, Konrad K. Dabrowski, Matthew Johnson, Daniël Paulusma, Théo Pierron · 2019-09-03
 https://arxiv.org/abs/1811.12252
 PDF source

=== Source paper abstract / header ===
Abstract:We resolve the computational complexity of Graph Isomorphism for classes of graphs characterized by two forbidden induced subgraphs $H_1$ and $H_2$ for all but six pairs $(H_1,H_2)$. Schweitzer had previously shown that the number of open cases was finite, but without specifying the open cases. Grohe and Schweitzer proved that Graph Isomorphism is polynomial-time solvable on graph classes of bounded clique-width. Our work combines known results such as these with new results. By exploiting a relationship between Graph Isomorphism and clique-width, we simultaneously reduce the number of open cases for boundedness of clique-width for $(H_1,H_2)$-free graphs to five.
 

 
 
 
 Comments:
 28 pages, 4 figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C60, 05C75
 

 Cite as:
 arXiv:1811.12252 [cs.DM]
 

 
  
 (or 
 arXiv:1811.12252v2 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1811.12252
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Konrad Dabrowski [view email] 
 [v1]
 Thu, 29 Nov 2018 15:34:39 UTC (42 KB)

 [v2]
 Tue, 3 Sep 2019 15:07:51 UTC (40 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Graph Isomorphism for $(H_1,H_2)$-free Graphs: An Almost Complete Dichotomy, by Marthe Bonamy and Nicolas Bousquet and Konrad K. Dabrowski and Matthew Johnson and Dani\"el Paulusma and Th\'eo Pierron
View PDF
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2018-11
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Marthe Bonamy
Konrad K. Dabrowski
Matthew Johnson
Daniël Paulusma 

 

 export BibTeX citation
 Loading...

 
 
 BibTeX formatted citation

 ×
 

 
 loading...
 

 
 Data provided by: 
 
 

 

 Bookmark

 
 
 
 
 

 

 

 
 Bibliographic Tools
 
 Bibliographic and Citation Tools

 
 
 
 
 
 
 Bibliographic Explorer Toggle
 
 

 
 Bibliographic Explorer (What is the Explorer?)
 

 

 
 
 
 
 
 Connected Papers Toggle
 
 

 
 Connected Papers (What is Connected Papers?)
 

 

 
 
 
 
 Litmaps Toggle
 
 

 
 Litmaps (What is Litmaps?)
 

 

 
 
 
 
 
 scite.ai Toggle
 
 

 
 scite Smart Citations (What are Smart Citations?)
 

 

 

 

 

 

 

 

 
 Code, Data, Media
 
 Code, Data and Media Associated with this Article

 
 
 
 
 
 
 alphaXiv Toggle
 
 

 
 alphaXiv (What is alphaXiv?)
 

 

 
 
 
 
 
 Links to Code Toggle
 
 

 
 CatalyzeX Code Finder for Papers (What is CatalyzeX?)
 

 

 
 
 
 
 
 DagsHub Toggle
 
 

 
 DagsHub (What is DagsHub?)
 

 

 
 
 
 
 
 
 GotitPub Toggle
 
 

 
 Gotit.pub (What is GotitPub?)
 

 

 
 
 
 
 
 Huggingface Toggle
 
 

 
 Hugging Face (What is Huggingface?)
 

 

 
 
 
 
 
 ScienceCast Toggle
 
 

 
 ScienceCast (What is ScienceCast?)
 

 

 

 

 

 

 

 

 

 

 
 Demos
 
 Demos

 
 
 
 
 
 
 Replicate Toggle
 
 

 
 Replicate (What is Replicate?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 Hugging Face Spaces (What is Spaces?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 TXYZ.AI (What is TXYZ.AI?)
 

 

 

 

 

 

 

 
 Related Papers
 
 Recommenders and Search Tools

 
 
 
 
 
 
 Link to Influence Flower
 
 

 
 Influence Flower (What are Influence Flowers?)
 

 

 
 
 
 
 
 Core recommender toggle
 
 

 
 CORE Recommender (What is CORE?)
 

 

 

 
 
 Author

 Venue

 Institution

 Topic

 
 
 

 

 

 

 

 

 

 

 

 
 
 About arXivLabs
 
 
 
 
 arXivLabs: experimental projects with community collaborators

 arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

 Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

 Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

 

 
 

 

 

 

 

 
 Which authors of this paper are endorsers? |
 Disable MathJax (What is MathJax?)
