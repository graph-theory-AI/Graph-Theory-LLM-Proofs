Attack the following open graph-theory problem.

Catalog id: 2110.10530__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2110.10530__00/
Source paper: Improved pyrotechnics : Closer to the burning graph conjecture (arXiv:2110.10530)

=== Catalog page (statement + literature review) ===
R-burnability of trees with bounded growth — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 7 proposes that every tree of growth k and order n is R-burnable whenever R is a finite set containing {0,1,...,k} with sufficient total volume sum_{r in R}(2r+1) >= n. No paper directly addressing this specific conjecture was found in a broad literature search. The broader Burning Number Conjecture has seen significant partial progress since 2022 (proven for trees without degree-2 vertices in arXiv:2312.13972, and for trees with at most floor(sqrt(n-1)) degree-2 vertices in arXiv:2509.03144), but these results target the standard BNC and do not resolve Conjecture 7, which is a strictly stronger generalisation requiring R-burnability for arbitrary valid sets R.

 Reviewer notes. No follow-up paper addressing R-burnability or Conjecture 7 from arXiv:2110.10530 was found. The closest related work is progress on the standard Burning Number Conjecture: arXiv:2312.13972 (trees without degree-2 vertices, published in Graphs and Combinatorics 2024) and arXiv:2509.03144 (trees with at most floor(sqrt(n-1)) degree-2 vertices, 2025). Neither paper addresses the R-burnability framework. The conjecture is likely open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $T$ be a tree of growth $k$ and of order $n$. If $R$ is a finite set of integers such that $\{0, 1, \ldots, k\} \subseteq R$ and $\sum_{r \in R}(2r+1) \geq n$, then $T$ is $R$-burnable.

Context

The authors propose this as a stronger version of the Burning Number Conjecture via a reformulation using $R$-burnability: the BNC states that every connected graph on $n$ vertices is $\{0, 1, \ldots, \lceil\sqrt{n}\rceil - 1\}$-burnable, since $\sum_{r=0}^{\lceil\sqrt{n}\rceil - 1}(2r+1) = \lceil\sqrt{n}\rceil^2 \geq n$. Conjecture 7 generalises this to trees of bounded growth by requiring the set $R$ to contain all radii up to $k$ and have sufficient total volume.

Source paper

 Improved pyrotechnics : Closer to the burning graph conjecture
 Paul Bastide, Marthe Bonamy, Anthony Bonato, Pierre Charbit, Shahin Kamali, Théo Pierron, Mikaël Rabie · 2022-03-04
 https://arxiv.org/abs/2110.10530
 PDF source

=== Source paper abstract / header ===
Abstract:The Burning Number Conjecture claims that for every connected graph $G$ of order $n,$ its burning number satisfies $b(G) \le \lceil \sqrt{n} \rceil.$ While the conjecture remains open, we prove that it is asymptotically true when the order of the graph is much larger than its \emph{growth}, which is the maximal distance of a vertex to a well-chosen path in the graph. We prove that the conjecture for graphs of bounded growth reduces to a finite number of cases. We provide the best-known bound on the burning number of a connected graph $G$ of order $n,$ given by $b(G) \le \sqrt{4n/3} + 1,$ improving on the previously known $\sqrt{3n/2}+O(1)$ bound. Using the improved upper bound, we show that the conjecture almost holds for all graphs with minimum degree at least $3$ and holds for all large enough graphs with minimum degree at least $4$. The previous best-known result was for graphs with minimum degree $23$.
 

 
 
 
 Comments:
 10 pages
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 G.2.2
 

 Cite as:
 arXiv:2110.10530 [math.CO]
 

 
  
 (or 
 arXiv:2110.10530v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2110.10530
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Mikaël Rabie [view email] 
 [v1]
 Wed, 20 Oct 2021 12:35:28 UTC (11 KB)

 [v2]
 Fri, 4 Mar 2022 10:41:09 UTC (57 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Improved pyrotechnics : Closer to the burning graph conjecture, by Paul Bastide and 5 other authors
View PDF
HTML (experimental)
TeX Source
 

 
 
 view license
 

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2021-10
 

 Change to browse by:
 
 cs
 cs.DM
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

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
