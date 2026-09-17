Attack the following open graph-theory problem.

Catalog id: 2202.05557__01
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2202.05557__01/
Source paper: Polynomial bounds for chromatic number. V. Excluding a tree of radius t… (arXiv:2202.05557)

=== Extracted statement (catalog JSON) ===
Title: Question: Extending Theorem 1.6 to paths
Is it true that if $H$ is a path, then for every integer $d \geq 1$, there is a polynomial $f$ such that $\chi(G) \leq f(\tau_d(G))$ for every $H$-free graph $G$?

Context:
This question, suggested by a referee and included by the authors, asks whether the main result (Theorem 1.6 for trees of radius two) can be extended to paths—another prominent family of forests for which polynomial bounds in terms of $\tau_2(G)$ are already known (via results of Bonamy et al. and Scott-Seymour-Spirkl).

=== Catalog page (statement + literature review) ===
Polynomial χ-bound via τ_d for path-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The conjecture asks whether polynomial bounds chi(G) <= f(tau_d(G)) hold for every path-free graph G, extending Theorem 1.6 (proved for trees of radius two) to paths. A direct successor in the series, 'Polynomial bounds for chromatic number VIII. Excluding a path and a complete multipartite graph' by Nguyen (Journal of Graph Theory, 2024, DOI 10.1002/jgt.23129), bears a title that mirrors the structure of the source paper and appears to address exactly this question; however, the full theorem statement could not be verified due to paywall access. The internal corpus references (arXiv:2409.09397, arXiv:2409.09400) concern Gyarfas-Sumner stable-set bounds for forest-free graphs and do not address this specific conjecture about tau_d and chromatic number.

 Cited literature (1)

 
 
 
partial Polynomial bounds for chromatic number VIII. Excluding a path and a complete multipartite graph
 (2024)
 

 
 Nguyen · Journal of Graph Theory · doi:10.1002/jgt.23129

Title mirrors paper V and addresses polynomial chi-bounds for path-free graphs excluding a complete multipartite graph (the structure captured by tau_d); exact theorem scope unverified due to paywall (HTTP 402 on fetch).
 

 

 Reviewer notes. Part VIII of the 'Polynomial bounds for chromatic number' series ('Excluding a path and a complete multipartite graph', Nguyen 2024, JGT, DOI 10.1002/jgt.23129) is the strongest candidate for a resolution of this conjecture: its title exactly parallels paper V's title with 'path' replacing 'tree of radius two', suggesting it proves chi(G) <= poly(tau_d(G)) for path-free graphs. Status is 'partial' rather than 'solved' because the Wiley page returned HTTP 402 (paywall) and the exact theorem statement could not be read. Part VI (arXiv:2202.10412) treats the four-vertex path in the clique-number chi-bounded framework (not tau_d) and remains limited to specific short paths. The three internal corpus references all concern different conjectures (Gyarfas-Sumner stable sets or coarse Menger) and are not relevant here.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it true that if $H$ is a path, then for every integer $d \geq 1$, there is a polynomial $f$ such that $\chi(G) \leq f(\tau_d(G))$ for every $H$-free graph $G$?

Context

This question, suggested by a referee and included by the authors, asks whether the main result (Theorem 1.6 for trees of radius two) can be extended to paths—another prominent family of forests for which polynomial bounds in terms of $\tau_2(G)$ are already known (via results of Bonamy et al. and Scott-Seymour-Spirkl).

Notes. Explicitly labelled as an open question suggested by a referee and incorporated into the paper.

Source paper

 Polynomial bounds for chromatic number. V. Excluding a tree of radius two and a complete multipartite graph
 Alex Scott, Paul Seymour · 2023-01-10
 https://arxiv.org/abs/2202.05557
 PDF source

=== Source paper abstract / header ===
Abstract:The Gyárfás-Sumner conjecture says that for every forest $H$ and every integer $k$, if $G$ is $H$-free and does not contain a clique on $k$ vertices then it has bounded chromatic number. (A graph is $H$-free if it does not contain an induced copy of $H$.) Kierstead and Penrice proved it for trees of radius at most two, but otherwise the conjecture is known only for a few simple types of forest. More is known if we exclude a complete bipartite subgraph instead of a clique: Rödl showed that, for every forest $H$, if $G$ is $H$-free and does not contain $K_{t,t}$ as a subgraph then it has bounded chromatic number. In an earlier paper with Sophie Spirkl, we strengthened Rödl's result, showing that for every forest $H$, the bound on chromatic number can be taken to be polynomial in $t$. In this paper, we prove a related strengthening of the Kierstead-Penrice theorem, showing that for every tree $H$ of radius two and every integer $d\ge 2$, if $G$ is $H$-free and does not contain as a subgraph the complete $d$-partite graph with parts of cardinality $t$, then its chromatic number is at most polynomial in $t$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2202.05557 [math.CO]
 

 
  
 (or 
 arXiv:2202.05557v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2202.05557
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Fri, 11 Feb 2022 11:28:16 UTC (15 KB)

 [v2]
 Tue, 10 Jan 2023 08:39:10 UTC (15 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Polynomial bounds for chromatic number. V. Excluding a tree of radius two and a complete multipartite graph, by Alex Scott and 1 other authors
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
 | 2022-02
 

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
