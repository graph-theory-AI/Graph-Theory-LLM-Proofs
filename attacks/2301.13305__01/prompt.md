Attack the following open graph-theory problem.

Catalog id: 2301.13305__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2301.13305__01/
Source paper: Graph-codes (arXiv:2301.13305)

=== Catalog page (statement + literature review) ===
K₄ graph-code density vanishing — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The question whether $d_{K_4}(n) = o(1)$ for general graph codes remains open as of May 2026. Versteegen (arXiv:2310.19891, 2023) made partial progress by proving that any linear graph code on $n$ vertices containing no copy of a graph $H$ with an even number of edges has size $O(2^{\binom{n}{2}}/\log n)$, which settles the analogue for linear codes; however, the general (non-linear) case of the question from Conjecture 1.1 / Question 1.1 of arXiv:2301.13305 is not resolved by this work. Several further papers cite arXiv:2301.13305 (including Gishboliner–Jin–Sudakov 2312.06610, Conlon–Lee–Versteegen 2404.17467, and Rancourt–Dodos–Tyros 2602.03298) but none were verified to resolve the full question.

 Cited literature (1)

 
 
 
partial Upper Bounds for Linear Graph Codes
 (2023)
 

 
 Leo Versteegen · arXiv preprint · arXiv:2310.19891

Proves that a linear graph code on $n$ vertices with no copy of $H$ (even number of edges) has size $O(2^{\binom{n}{2}}/\log n)$, settling the linear-code variant of the $d_{K_4}(n)=o(1)$ question but leaving the general non-linear case open.
 

 

 Reviewer notes. The Semantic Scholar citation list for arXiv:2301.13305 returned 20 citing papers (as of May 2026). The most directly relevant verified follow-up is arXiv:2310.19891 (Versteegen), which addresses only linear graph codes. The papers arXiv:2312.06610, arXiv:2404.17467, and arXiv:2602.03298 also cite the source paper but their specific results regarding $d_{K_4}(n)=o(1)$ were not verified within the 5-call budget. The lower bound $d_{K_4}(n) \geq 1/n^{o(1)}$ is established within the source paper itself via Hunter–Mubayi.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Is it true that $d_{K_4}(n) = o(1)$?

Context

In the concluding remarks the authors single this out as an interesting special case of Question 1.1. The companion question of whether $d_{K_4}(n) \geq 1/n^{o(1)}$ is answered affirmatively within the paper by appealing to an edge-coloring construction of Hunter and Mubayi [5] (modifying [11] and [4]); the upper-bound direction $d_{K_4}(n) = o(1)$ remains open.

Notes. The lower bound $d_{K_4}(n) \geq 1/n^{o(1)}$ is established in the paper; only the question of whether $d_{K_4}(n) = o(1)$ remains open.

Source paper

 Graph-codes
 Noga Alon · 2023-02-06
 https://arxiv.org/abs/2301.13305
 PDF source

=== Source paper abstract / header ===
Abstract:The symmetric difference of two graphs $G_1,G_2$ on the same set of vertices $[n]=\{1,2, \ldots ,n\}$ is the graph on $[n]$ whose set of edges are all edges that belong to exactly one of the two graphs $G_1,G_2$. Let $H$ be a fixed graph with an even (positive) number of edges, and let $D_H(n)$ denote the maximum possible cardinality of a family of graphs on $[n]$ containing no two members whose symmetric difference is a copy of $H$. Is it true that $D_H(n)=o(2^{n \choose 2})$ for any such $H$? We discuss this problem, compute the value of $D_H(n)$ up to a constant factor for stars and matchings, and discuss several variants of the problem including ones that have been considered in earlier work.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05D05, 94B25
 

 Cite as:
 arXiv:2301.13305 [math.CO]
 

 
  
 (or 
 arXiv:2301.13305v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2301.13305
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Noga Alon [view email] 
 [v1]
 Mon, 30 Jan 2023 21:54:31 UTC (9 KB)

 [v2]
 Mon, 6 Feb 2023 17:19:26 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Graph-codes, by Noga Alon
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
 | 2023-01
 

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
