Attack the following open graph-theory problem.

Catalog id: 2404.03472__02
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2404.03472__02/
Source paper: Lower bounds for graph reconstruction with maximal independent set quer… (arXiv:2404.03472)

=== Extracted statement (catalog JSON) ===
Title: Problem 5.3 (adaptive vs non-adaptive gap)
Is there a deterministic adaptive algorithm that uses $o(\Delta^{3}\log(n/\Delta))$ queries to reconstruct any graph of maximum degree $\Delta$?

Context:
For adaptive algorithms the best lower bound drops to $\Omega(\Delta^{2}\log(n/\Delta)/\log\Delta)$ in both the deterministic and randomised settings, while the upper bounds match the non-adaptive case. This gap suggests adaptive algorithms might outperform non-adaptive ones, motivating the question of whether adaptivity yields a provable saving.

=== Catalog page (statement + literature review) ===
Adaptive gap for Δ-degree graph reconstruction — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 5.3 asks whether a deterministic adaptive algorithm can reconstruct any graph of maximum degree $\Delta$ using $o(\Delta^3 \log(n/\Delta))$ MIS queries, potentially exploiting the gap with the adaptive lower bound of $\Omega(\Delta^2 \log(n/\Delta)/\log\Delta)$. The best known deterministic adaptive upper bound remains $O(\Delta^3 \log(n/\Delta))$ (using $O(\log\Delta)$ rounds of adaptivity), matching the non-adaptive case and established in Konrad–O'Sullivan–Traistaru (arXiv:2401.05845, ITCS 2025). No subsequent paper has closed the gap or shown a sub-cubic (in $\Delta$) deterministic adaptive algorithm.

 Reviewer notes. The conjecture is closely related to Konrad, O'Sullivan, Traistaru (arXiv:2401.05845, ITCS 2025), which predates the source paper (v1 January 2024) and already established the $O(\Delta^3 \log(n/\Delta))$ deterministic adaptive bound (Corollary 2 of v4, December 2024). That paper does not reference Problem 5.3 explicitly. No follow-up was found in the indexed literature that beats this bound or proves adaptivity provably helps for deterministic algorithms. The randomised adaptive lower bound $\Omega(\Delta^2 \log(n/\Delta)/\log\Delta)$ from the source paper still leaves a factor-$\Delta\log\Delta$ gap with the upper bound, making this an appealing open problem.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Is there a deterministic adaptive algorithm that uses $o(\Delta^{3}\log(n/\Delta))$ queries to reconstruct any graph of maximum degree $\Delta$?

Context

For adaptive algorithms the best lower bound drops to $\Omega(\Delta^{2}\log(n/\Delta)/\log\Delta)$ in both the deterministic and randomised settings, while the upper bounds match the non-adaptive case. This gap suggests adaptive algorithms might outperform non-adaptive ones, motivating the question of whether adaptivity yields a provable saving.

Notes. Parser assigned the label 'Problem 5.0' to all three problems in Section 5; this is likely Problem 5.3 or the third of several unnumbered problems.

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
