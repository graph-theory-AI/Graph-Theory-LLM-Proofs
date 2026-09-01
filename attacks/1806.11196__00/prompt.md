Attack the following open graph-theory problem.

Catalog id: 1806.11196__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1806.11196__00/
Source paper: List-three-coloring graphs with no induced $P_6+rP_3$ (arXiv:1806.11196)

=== Extracted statement (catalog JSON) ===
Title: Question 1.1
Is it true that for every (fixed) integer $t > 0$, the 3-coloring problem can be solved in polynomial time when restricted to the class of $P_t$-free graphs?

Context:
Theorem 1.1 (from the literature) states that if the $k$-coloring problem is polynomial on $H$-free graphs then every connected component of $H$ must be a path. For $k=3$ the converse may hold — it is known to fail for $k>4$ — so the question of whether $P_t$-free graphs always admit a polynomial-time 3-coloring algorithm remains open. The present paper contributes a positive result for the subclass of $(P_6+rP_3)$-free graphs.

=== Catalog page (statement + literature review) ===
Polynomial 3-coloring for P_t-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Substantial partial progress has been made: the 3-coloring (and list 3-coloring) problem is known to be polynomial for all $P_t$-free graphs with $t \leq 7$, with the $P_7$ case resolved by Bonomo, Chudnovsky, Maceli, Schaudt, Stein, and Zhong around 2018. For $t \geq 8$ the question remains fully open; $P_8$-free graphs are the smallest unsettled case. Since 2018, incremental progress has appeared for specific subclasses of $P_t$-free graphs (e.g., those with restrictions on odd cycle lengths), but no uniform polynomial algorithm for all fixed $t$ is known.

 Cited literature (1)

 
 
 
partial 3-Coloring $P_t$-Free Graphs With Only One Prescribed Induced Odd Cycle Length
 (2025)
 

 
 unverified from abstract page · arXiv preprint · arXiv:2512.06367

Proves a polynomial-time algorithm for 3-coloring $P_{10}$-free graphs whose only induced odd cycles have a single prescribed length (e.g., 7-cycles), a restricted but non-trivial subclass of $P_t$-free graphs.
 

 

 Reviewer notes. The conjecture is proven for $t \leq 7$; the $P_7$ result (Bonomo et al., ~2018) is the furthest general case. For $t \geq 8$ the problem is open and listed as such in recent surveys (e.g., open problems from the 33rd Workshop on Cycles and Colourings, arXiv:2511.02892, 2025). Additional post-2018 partial progress found in search but not fetched: '3-Colouring $P_t$-Free Graphs Without Short Odd Cycles' (Algorithmica 2022, link.springer.com/article/10.1007/s00453-022-01049-0) and 'Three-coloring triangle-free graphs without long forbidden paths' (arXiv:2512.12349, 2025) — these were not WebFetched and are excluded from since_posted per policy.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it true that for every (fixed) integer $t > 0$, the 3-coloring problem can be solved in polynomial time when restricted to the class of $P_t$-free graphs?

Context

Theorem 1.1 (from the literature) states that if the $k$-coloring problem is polynomial on $H$-free graphs then every connected component of $H$ must be a path. For $k=3$ the converse may hold — it is known to fail for $k>4$ — so the question of whether $P_t$-free graphs always admit a polynomial-time 3-coloring algorithm remains open. The present paper contributes a positive result for the subclass of $(P_6+rP_3)$-free graphs.

Notes. The question has no explicit attribution citation in the header; it is recorded as a standing open problem in the field by the paper's authors. Full paper text was truncated in the supplied PDF extraction, so later sections could not be checked for additional conjectural statements.

Source paper

 List-three-coloring graphs with no induced $P_6+rP_3$
 Maria Chudnovsky, Shenwei Huang, Sophie Spirkl, Mingxian Zhong · 2018-07-02
 https://arxiv.org/abs/1806.11196
 PDF source

=== Source paper abstract / header ===
Abstract:For an integer $r$, the graph $P_6+rP_3$ has $r+1$ components, one of which is a path on $6$ vertices, and each of the others is a path on $3$ vertices. In this paper we provide a polynomial-time algorithm to test if a graph with no induced subgraph isomorphic to $P_6+rP_3$ is three-colorable. We also solve the list version of this problem, where each vertex is assigned a list of possible colors, which is a subset of $\{1,2,3\}$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1806.11196 [math.CO]
 

 
  
 (or 
 arXiv:1806.11196v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1806.11196
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Shenwei Huang [view email] 
 [v1]
 Thu, 28 Jun 2018 21:17:04 UTC (33 KB)

 [v2]
 Mon, 2 Jul 2018 12:40:10 UTC (33 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled List-three-coloring graphs with no induced $P_6+rP_3$, by Maria Chudnovsky and Shenwei Huang and Sophie Spirkl and Mingxian Zhong
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
 | 2018-06
 

 Change to browse by:
 
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
