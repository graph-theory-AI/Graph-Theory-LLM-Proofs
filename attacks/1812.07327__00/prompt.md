Attack the following open graph-theory problem.

Catalog id: 1812.07327__00
Catalog status: partial (triage tier 4, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1812.07327__00/
Source paper: 1-subdivisions, fractional chromatic number and Hall ratio (arXiv:1812.07327)

=== Extracted statement (catalog JSON) ===
Title: Problem 4
Determine the smallest function $g : \mathbb{Z}^+ \to \mathbb{R}^+$ such that for every graph $G$, $\chi_f(G) \leq \rho(G)\,g(|V(G)|)$.

Context:
Since $\chi_f(G) = O(\rho(G) \log n)$ follows from a greedy independent-set argument, and the graphs produced by Corollary 3 have doubly exponential size in their fractional chromatic number (giving $g(n) = \Omega(\log\log n)$), the true growth rate of the smallest such $g$ is unknown.

=== Catalog page (statement + literature review) ===
χ_f to Hall ratio gap growth rate — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Problem 4 asks for the exact growth rate of the smallest function $g$ such that $\chi_f(G) \leq \rho(G)\,g(|V(G)|)$ for all graphs $G$; at the time of posting the bounds were $\Omega(\log\log n) \leq g(n) \leq O(\log n)$. Steiner (2024, arXiv:2411.16465, published in Combinatorica) substantially narrows this gap by proving a lower bound of $\Omega(\log n/(\log\log n)^3)$, establishing $g(n) = (\log n)^{1-o(1)}$ and showing the growth rate is essentially logarithmic. The exact smallest $g$ (precise constant factors) remains undetermined, so the problem is partially resolved.

 Cited literature (1)

 
 
 
partial Fractional chromatic number vs. Hall ratio
 (2024)
 

 
 Raphael Steiner · Combinatorica · arXiv:2411.16465 · doi:10.1007/s00493-025-00164-0

Proves $g(n) = (\log n)^{1-o(1)}$ by establishing a lower bound of $\Omega(\log n/(\log\log n)^3)$, reducing the gap from $[\Omega(\log\log n),\, O(\log n)]$ to essentially $\Theta(\log n)$ up to lower-order factors, and additionally constructs graphs with bounded Hall ratio, arbitrarily large fractional chromatic number, and good degree-weighted independence number in every subgraph (Theorem 1.5).
 

 

 Reviewer notes. Steiner's paper (arXiv:2411.16465) is the primary follow-up; it nearly resolves Problem 4 by showing g(n)=(log n)^{1-o(1)}, collapsing an exponential gap to a polylogarithmic one. The exact smallest g (constant factors) is still open. The Dvořák 2007.11853 internal-ref entries appear to be false positives unrelated to Problem 4.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the smallest function $g : \mathbb{Z}^+ \to \mathbb{R}^+$ such that for every graph $G$, $\chi_f(G) \leq \rho(G)\,g(|V(G)|)$.

Context

Since $\chi_f(G) = O(\rho(G) \log n)$ follows from a greedy independent-set argument, and the graphs produced by Corollary 3 have doubly exponential size in their fractional chromatic number (giving $g(n) = \Omega(\log\log n)$), the true growth rate of the smallest such $g$ is unknown.

Source paper

 1-subdivisions, fractional chromatic number and Hall ratio
 Zdeněk Dvořák, Patrice Ossona de Mendez, Hehui Wu · 2020-01-30
 https://arxiv.org/abs/1812.07327
 PDF source

=== Source paper abstract / header ===
Abstract:The Hall ratio of a graph G is the maximum of |V(H)|/alpha(H) over all subgraphs H of G. Clearly, the Hall ratio of a graph is a lower bound for the fractional chromatic number. It has been asked whether conversely, the fractional chromatic number is upper bounded by a function of the Hall ratio. We answer this question in negative, by showing two results of independent interest regarding 1-subdivisions (the 1-subdivision of a graph is obtained by subdividing each edge exactly once).
* For every c > 0, every graph of sufficiently large average degree contains as a subgraph the 1-subdivision of a graph of fractional chromatic number at least c.
* For every d > 0, there exists a graph G of average degree at least d such that every graph whose 1-subdivision appears as a subgraph of G has Hall ratio at most 18.
We also discuss the consequences of these results in the context of graph classes with bounded expansion.
 

 
 
 
 Comments:
 14 pages, no figures; updated for reviewer remarks
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:1812.07327 [math.CO]
 

 
  
 (or 
 arXiv:1812.07327v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1812.07327
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Tue, 18 Dec 2018 12:28:33 UTC (10 KB)

 [v2]
 Thu, 30 Jan 2020 12:21:33 UTC (12 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled 1-subdivisions, fractional chromatic number and Hall ratio, by Zden\v{e}k Dvo\v{r}\'ak and Patrice Ossona de Mendez and Hehui Wu
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
 | 2018-12
 

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
