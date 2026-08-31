Attack the following open graph-theory problem.

Catalog id: 2308.02981__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2308.02981__01/
Source paper: Factoring Pattern-Free Permutations into Separable ones (arXiv:2308.02981)

=== Catalog page (statement + literature review) ===
Parameterized complexity of separable index — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Question 1.3 asks for the parameterised complexity of computing the separable index sep(σ) — the smallest k such that a permutation σ factors as a product of k separable permutations — and of approximating it within a constant factor. The paper's main theorem (Theorem 1.1) yields an FPT approximation algorithm, but the approximation ratio is a triple-exponential function of the parameter k, which the authors note is very far from constant. No follow-up work addressing the exact complexity or a constant-factor approximation of sep(σ) has been found in the literature as of May 2026.

 Reviewer notes. No follow-up found after three targeted searches and direct PDF inspection. The conjecture is recent (2023, published SODA 2024) and quite specific; open with high confidence. The arxiv:2507.07606 paper on Ramsey-like theorems for separable permutations was inspected but its abstract does not address the complexity of sep(σ).

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. What is the parameterised complexity of computing $\mathrm{sep}(\sigma)$, and of approximating it within a constant factor?

Context

The paper's main result implies an FPT approximation for the separable index $\mathrm{sep}(\sigma)$ via pattern recognition, but the approximation function is triple exponential in $k$. The authors ask whether the complexity of computing or approximating $\mathrm{sep}(\sigma)$ exactly can be improved, possibly to an exact algorithm.

Source paper

 Factoring Pattern-Free Permutations into Separable ones
 Édouard Bonnet, Romain Bourneuf, Colin Geniet, Stéphan Thomassé · 2023-08-06
 https://arxiv.org/abs/2308.02981
 PDF source

=== Source paper abstract / header ===
Abstract:We show that for any permutation $\pi$ there exists an integer $k_{\pi}$ such that every permutation avoiding $\pi$ as a pattern is a product of at most $k_{\pi}$ separable permutations. In other words, every strict class $\mathcal C$ of permutations is contained in a bounded power of the class of separable permutations. This factorisation can be computed in linear time, for any fixed $\pi$. The central tool for our result is a notion of width of permutations, introduced by Guillemot and Marx [SODA '14] to efficiently detect patterns, and later generalised to graphs and matrices under the name of twin-width. Specifically, our factorisation is inspired by the decomposition used in the recent result that graphs with bounded twin-width are polynomially $\chi$-bounded. As an application, we show that there is a fixed class $\mathcal C$ of graphs of bounded twin-width such that every class of bounded twin-width is a first-order transduction of $\mathcal C$.
 

 
 
 
 Comments:
 34 pages, 8 figures
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Logic in Computer Science (cs.LO)
 
 
 MSC classes:
 05A05
 

 
 ACM classes:
 G.2.1
 

 Cite as:
 arXiv:2308.02981 [math.CO]
 

 
  
 (or 
 arXiv:2308.02981v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2308.02981
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Sun, 6 Aug 2023 01:09:16 UTC (44 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Factoring Pattern-Free Permutations into Separable ones, by \'Edouard Bonnet and 3 other authors
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
 | 2023-08
 

 Change to browse by:
 
 cs
 cs.DM
 cs.DS
 cs.LO
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
