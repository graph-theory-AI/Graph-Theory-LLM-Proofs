Attack the following open graph-theory problem.

Catalog id: 2404.03472__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2404.03472__01/
Source paper: Lower bounds for graph reconstruction with maximal independent set quer… (arXiv:2404.03472)

=== Extracted statement (catalog JSON) ===
Title: Problem 5.2 (randomised non-adaptive optimality)
Is there a randomised non-adaptive algorithm which uses $\mathcal{O}(\Delta^{2}\log(n/\Delta))$ queries to reconstruct any graph of maximum degree $\Delta$ with high probability?

Context:
The paper proves an $\Omega(\Delta^{2}\log(n/\Delta))$ lower bound for randomised non-adaptive algorithms, while the existing upper bound of Konrad, O'Sullivan, and Traistaru is $\mathcal{O}(\Delta^{2}\log n)$. The question asks whether the new lower bound is tight, i.e., whether the $\log\Delta$ gap in the $n$-dependence can be closed.

=== Catalog page (statement + literature review) ===
Optimal randomised non-adaptive MIS reconstruction — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 5.2 asks whether the Ω(Δ²log(n/Δ)) lower bound for randomised non-adaptive MIS-query reconstruction algorithms is tight, i.e., whether an O(Δ²log(n/Δ)) algorithm exists. The current best upper bound remains O(Δ²log n) due to Konrad, O'Sullivan, and Traistaru (ITCS 2025), leaving a log Δ gap in the n-dependence. No follow-up paper closing this gap has been found as of May 2026.

 Reviewer notes. The conjecture is posed against the backdrop of two contemporaneous papers: arXiv:2404.03472 (Michel–Scott, April 2024) proving the Ω(Δ²log(n/Δ)) lower bound, and arXiv:2401.05845 (Konrad–O'Sullivan–Traistaru, January 2024, published as ITCS 2025 LIPIcs proceedings) providing the O(Δ²log n) randomised non-adaptive upper bound. The ITCS 2025 proceedings version of arXiv:2401.05845 explicitly cites arXiv:2404.03472 (as reference [23]), confirming mutual awareness, but does not improve the upper bound. No subsequent paper achieving O(Δ²log(n/Δ)) was found across multiple searches covering 2024–2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Is there a randomised non-adaptive algorithm which uses $\mathcal{O}(\Delta^{2}\log(n/\Delta))$ queries to reconstruct any graph of maximum degree $\Delta$ with high probability?

Context

The paper proves an $\Omega(\Delta^{2}\log(n/\Delta))$ lower bound for randomised non-adaptive algorithms, while the existing upper bound of Konrad, O'Sullivan, and Traistaru is $\mathcal{O}(\Delta^{2}\log n)$. The question asks whether the new lower bound is tight, i.e., whether the $\log\Delta$ gap in the $n$-dependence can be closed.

Notes. Parser assigned the label 'Problem 5.0' to all three problems in Section 5; this is likely Problem 5.2 or the second of several unnumbered problems.

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
