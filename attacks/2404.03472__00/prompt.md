Attack the following open graph-theory problem.

Catalog id: 2404.03472__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2404.03472__00/
Source paper: Lower bounds for graph reconstruction with maximal independent set quer… (arXiv:2404.03472)

=== Extracted statement (catalog JSON) ===
Title: Problem 5.1 (cover-free families)
Are there $(1,r)$-cover-free families $\mathcal{F}\subseteq\mathcal{P}(t)$ with $t\in\mathcal{O}(r^{2}\log\lvert\mathcal{F}\rvert/\log r)$?

Context:
The paper's lower bound for deterministic non-adaptive reconstruction ($\Omega(\Delta^{3}\log n/\log\Delta)$) is tied to a longstanding gap for cover-free families: $\Omega(r^{w+1}\log n/\log r)\leq t(n,w,r)\leq\mathcal{O}(r^{w+1}\log n)$. Closing this gap for $(1,r)$-cover-free families would directly improve the graph-reconstruction bounds.

=== Catalog page (statement + literature review) ===
Optimal size of (1,r)-cover-free families — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 5.1 from arXiv:2404.03472 asks whether $(1,r)$-cover-free families achieving $t\in\mathcal{O}(r^2\log|\mathcal{F}|/\log r)$ exist, which would close the longstanding gap $\Omega(r^2\log n/\log r)\leq t(n,1,r)\leq\mathcal{O}(r^2\log n)$ that has been open since the 1990s. A related ITCS 2025 follow-up paper on graph reconstruction via MIS queries addresses the algorithmic bounds from the same source paper but does not resolve this combinatorial problem about cover-free families. No post-2024 paper closing the $(\log r)$-factor gap for $(1,r)$-cover-free families was found in the indexed literature.

 Reviewer notes. The gap between the lower bound Omega(r^2 log n / log r) and upper bound O(r^2 log n) for t(n,1,r) has been known since the 1990s (cf. Electronic Journal of Combinatorics v23i2p45 for a survey of lower bounds). The ITCS 2025 paper 'Graph Reconstruction via MIS Queries' (LIPIcs ITCS 2025, doi:10.4230/LIPIcs.ITCS.2025.66) is a direct algorithmic follow-up to the source paper but does not address Problem 5.1. No construction achieving the conjectured O(r^2 log n / log r) bound was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Are there $(1,r)$-cover-free families $\mathcal{F}\subseteq\mathcal{P}(t)$ with $t\in\mathcal{O}(r^{2}\log\lvert\mathcal{F}\rvert/\log r)$?

Context

The paper's lower bound for deterministic non-adaptive reconstruction ($\Omega(\Delta^{3}\log n/\log\Delta)$) is tied to a longstanding gap for cover-free families: $\Omega(r^{w+1}\log n/\log r)\leq t(n,w,r)\leq\mathcal{O}(r^{w+1}\log n)$. Closing this gap for $(1,r)$-cover-free families would directly improve the graph-reconstruction bounds.

Notes. Parser assigned the label 'Problem 5.0' to all three problems in Section 5; this is likely Problem 5.1 or the first of several unnumbered problems.

Source paper

 Lower bounds for graph reconstruction with maximal independent set queries
 Lukas Michel, Alex Scott · 2024-04-04
 https://arxiv.org/abs/2404.03472

=== Source paper abstract / header ===
Abstract:We investigate the number of maximal independent set queries required to reconstruct the edges of a hidden graph. We show that randomised adaptive algorithms need at least $\Omega(\Delta^2 \log(n / \Delta) / \log \Delta)$ queries to reconstruct $n$-vertex graphs of maximum degree $\Delta$ with success probability at least $1/2$, and we further improve this lower bound to $\Omega(\Delta^2 \log(n / \Delta))$ for randomised non-adaptive algorithms. We also prove that deterministic non-adaptive algorithms require at least $\Omega(\Delta^3 \log n / \log \Delta)$ queries.
This improves bounds of Konrad, O'Sullivan, and Traistaru, and answers one of their questions. The proof of the lower bound for deterministic non-adaptive algorithms relies on a connection to cover-free families, for which we also improve known bounds.
 

 
 
 
 Comments:
 12 pages
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2404.03472 [cs.DS]
 

 
  
 (or 
 arXiv:2404.03472v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2404.03472
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Lukas Michel [view email] 
 [v1]
 Thu, 4 Apr 2024 14:25:21 UTC (13 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Lower bounds for graph reconstruction with maximal independent set queries, by Lukas Michel and 1 other authors
View PDF
HTML (experimental)
TeX Source
 

 
 
 view license
 

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2024-04
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
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
