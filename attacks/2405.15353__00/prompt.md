Attack the following open graph-theory problem.

Catalog id: 2405.15353__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2405.15353__00/
Source paper: Sharing tea on a graph (arXiv:2405.15353)

=== Catalog page (statement + literature review) ===
Exponential bound on optimal tea-sharing sequence length — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Question 6.1 from arXiv:2405.15353 asks whether every finite graph G, weight vector w in R_>=0^{V(G)}, and vertex v in V(G) admit a (w,v)-optimal sequence of length at most 2^{|V(G)|}. The source paper proves that a finite optimal sequence always exists but leaves the sharp exponential upper bound open. Proposition 6.2 of the same paper shows that a natural approach—finding an optimal sequence with no move that is a subset of a later move—fails, indicating the problem is nontrivial. A wide web search covering the arXiv ID, all authors, and the key mathematical terms returned no follow-up paper resolving or making partial progress on this question.

 Reviewer notes. No follow-up found after 5 web calls (4 WebSearch + 1 WebFetch on the arXiv abstract page). The paper appeared on arXiv in May 2024 (v1) and was revised to v2 in September 2025; Question 6.1 is stated in the v2 text. The conjecture is recent (< 2 years from today) and the absence of a follow-up is expected. Status open with high confidence.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. For every finite graph $G$, every ${w\in\mathbb{R}_{\geq 0}^{V(G)}}$, and every ${v\in V(G)}$, is there always a ${(w,v)}$-optimal sequence whose length is at most $2^{{\left\lvert{V(G)}\right\rvert}}$?

Context

The authors prove that for finite graphs the maximum amount of tea at any vertex $v$ can always be achieved after a finite number of sharing moves, but the sharp upper bound on the length of a shortest optimal sequence is unknown. One natural approach—showing that an optimal sequence need not repeat any sharing move—is complicated by Proposition 6.2, which shows that there need not exist an optimal sequence in which no move is a subset of a later move.

Source paper

 Sharing tea on a graph
 J. Pascal Gollin, Kevin Hendrey, Hao Huang, Tony Huynh, Bojan Mohar, Sang-il Oum, Ningyuan Yang, Wei-Hsuan Yu, Xuding Zhu · 2025-09-22
 https://arxiv.org/abs/2405.15353

=== Source paper abstract / header ===
Abstract:Motivated by the analysis of consensus formation in the Deffuant model for social interaction, we consider the following procedure on a graph $G$. Initially, there is one unit of tea at a fixed vertex $r \in V(G)$, and all other vertices have no tea. At any time in the procedure, we can choose a connected subset of vertices $T$ and equalize the amount of tea among vertices in $T$. We prove that if $x \in V(G)$ is at distance $d$ from $r$, then $x$ will have at most $\frac{1}{d+1}$ units of tea during any step of the procedure. This bound is best possible and answers a question of Gantert.
We also consider arbitrary initial weight distributions. For every finite graph $G$ and $w \in \mathbb{R}_{\geq 0}^{V(G)}$, we prove that the set of weight distributions reachable from $w$ is a compact subset of $\mathbb{R}_{\geq 0}^{V(G)}$.
 

 
 
 
 Comments:
 18 pages, 2 figures
 

 Subjects:
 
 Combinatorics (math.CO); Probability (math.PR)
 
 
 MSC classes:
 05C57, 05C90, 05C22, 91D30, 91B32, 05C63
 

 Cite as:
 arXiv:2405.15353 [math.CO]
 

 
  
 (or 
 arXiv:2405.15353v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2405.15353
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Tony Huynh [view email] 
 [v1]
 Fri, 24 May 2024 08:45:02 UTC (22 KB)

 [v2]
 Mon, 22 Sep 2025 08:41:14 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Sharing tea on a graph, by J. Pascal Gollin and 8 other authors
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
 | 2024-05
 

 Change to browse by:
 
 math
 math.PR
 

 

 

 
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
