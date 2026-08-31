Attack the following open graph-theory problem.

Catalog id: 2206.12335__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2206.12335__01/
Source paper: Improved bounds for 1-independent percolation on $\mathbb{Z}^n$ (arXiv:2206.12335)

=== Catalog page (statement + literature review) ===
Giant component threshold in hypercube percolation — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 6.4 asks for the exact value of $p_{\mathrm{giant}}$, the critical probability for a 1-independent percolation model on the hypercube $Q_n$ to contain a giant component with high probability. The source paper establishes $p_{\mathrm{giant}} \leq 0.5847$ while the best known lower bound remains $1/2$; Falgas-Ravry and Pfenninger (arXiv:2106.08674, RSA 2023) conjectured $p_{\mathrm{giant}} = 1/2$. No follow-up paper resolving the exact value was found in the literature as of May 2026.

 Reviewer notes. No follow-up paper resolving Problem 6.4 was found. The conjecture p_giant = 1/2 is due to Falgas-Ravry and Pfenninger (arXiv:2106.08674; published in Random Structures & Algorithms 2023), predating the source paper. The source paper was published in the Electronic Journal of Probability (2025, doi:10.1214/25-EJP1341). Standard (bond/site) percolation results on the hypercube found in recent literature are unrelated to the 1-independent setting of this problem.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the value of $p_{\mathrm{giant}}$?

Context

The paper establishes $p_{\mathrm{giant}}\leq 0.5847$ (when each edge of the hypercube $Q_n$ is open with probability at least $0.5847$ and $n$ is large, a giant component exists with high probability). The best lower bound remains $1/2$. Falgas-Ravry and Pfenninger conjectured $p_{\mathrm{giant}}=1/2$, but the exact value is unknown.

Source paper

 Improved bounds for 1-independent percolation on $\mathbb{Z}^n$
 Paul Balister, Tom Johnston, Michael Savery, Alex Scott · 2025-06-23
 https://arxiv.org/abs/2206.12335

=== Source paper abstract / header ===
Abstract:A 1-independent bond percolation model on a graph $G$ is a probability distribution on the spanning subgraphs of $G$ in which, for all vertex-disjoint sets of edges $S_1$ and $S_2$, the states of the edges in $S_1$ are independent of the states of the edges in $S_2$. Such a model is said to percolate if the random subgraph has an infinite component with positive probability. In 2012 the first author and Bollobás defined $p_{\max}(G)$ to be the supremum of those $p$ for which there exists a 1-independent bond percolation model on $G$ in which each edge is present in the random subgraph with probability at least $p$ but which does not percolate.
A fundamental and challenging problem in this area is to determine the value of $p_{\max}(G)$ when $G$ is the lattice graph $\mathbb{Z}^2$. Since $p_{\max}(\mathbb{Z}^n)\leq p_{\max}(\mathbb{Z}^{n-1})$, it is also of interest to establish the value of $\lim_{n\to\infty} p_{\max}(\mathbb{Z}^n)$. In this paper we significantly improve the best known upper bound on this limit and obtain better upper and lower bounds on $p_{\max}(\mathbb{Z}^2)$. In proving these results, we also give an upper bound on the critical probability for a 1-independent model on the hypercube graph to contain a giant component asymptotically almost surely.
 

 
 
 
 Comments:
 31 pages, 3 figures
 

 Subjects:
 
 Probability (math.PR); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2206.12335 [math.PR]
 

 
  
 (or 
 arXiv:2206.12335v2 [math.PR] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2206.12335
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 
 Related DOI:
 
 https://doi.org/10.1214/25-EJP1341

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tom Johnston [view email] 
 [v1]
 Fri, 24 Jun 2022 15:13:41 UTC (30 KB)

 [v2]
 Mon, 23 Jun 2025 09:02:21 UTC (43 KB)

 

 
 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Improved bounds for 1-independent percolation on $\mathbb{Z}^n$, by Paul Balister and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Ancillary-file links:
 Ancillary files (details):

 README.txt
 perctest.c
 perctestRC4.c

 

 
 Current browse context:

 math.PR

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2022-06
 

 Change to browse by:
 
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
