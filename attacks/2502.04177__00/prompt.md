Attack the following open graph-theory problem.

Catalog id: 2502.04177__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2502.04177__00/
Source paper: Shallow brambles (arXiv:2502.04177)

=== Catalog page (statement + literature review) ===
Scol bounded by bramble number in polynomial expansion — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 What is the smallest number of disjoint spanning trees made a graph Hamiltonian
 (fuzzy-match score 100, not yet manually confirmed).

 
 Status
 open
 high confidence
 

 Question 2 of arXiv:2502.04177 asks whether, for every graph class with polynomial expansion, the strong r-coloring number scol_r(G) is polynomially bounded by the depth-r bramble number bn_r(G). The paper itself establishes that the depth-r bramble number and several related parameters (depth-r tangle number, linkedness, well-linkedness) are pairwise polynomially related in polynomial-expansion classes, but the connection to scol_r(G) is left open. No follow-up paper resolving this question was found in the indexed literature as of May 2026.

 Reviewer notes. No follow-up paper addressing Question 2 was found after three targeted web searches and two direct fetches of the source paper. The paper was published in DMTCS (September 2025) shortly after the arXiv preprint (February 2025). The conjecture is recent (less than 1 year at time of review), and absence of follow-up is expected. The polynomial expansion assumption is noted in the paper as essential: without it scol_r cannot be bounded by any function of r and bn_{g(r)}(G).

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it true that for every graph class $\mathcal{C}$ with polynomial expansion, there exists a polynomial function $f$ such that for every integer $r\geqslant 0$ and every graph $G\in\mathcal{C}$, $$\mathrm{scol}_{r}(G)\leqslant f(r,\mathrm{bn}_{r}(G))?$$

Context

A positive answer to this question would be sufficient to answer Question 1 positively. The polynomial expansion assumption on $\mathcal{C}$ is essential: without it, $\mathrm{scol}_r(G)$ cannot be bounded by any function of $r$ and the depth-$r$ bramble number $\mathrm{bn}_r(G)$, even if the bramble number is replaced by $\mathrm{bn}_{g(r)}(G)$ for an arbitrary function $g$.

Also stated in

 
Shallow brambles (2025-09-15) 

Source paper

 Shallow brambles
 Nicolas Bousquet, Wouter Cames van Batenburg, Louis Esperet, Gwenaël Joret, Piotr Micek · 2025-09-15
 https://arxiv.org/abs/2502.04177

=== Source paper abstract / header ===
Abstract:A graph class $\mathcal{C}$ has polynomial expansion if there is a polynomial function $f$ such that for every graph $G\in \mathcal{C}$, each of the depth-$r$ minors of $G$ has average degree at most $f(r)$. In this note, we study bounded-radius variants of some classical graph parameters such as bramble number, linkedness and well-linkedness, and we show that they are pairwise polynomially related. Furthermore, in a monotone graph class with polynomial expansion they are all uniformly bounded by a polynomial in $r$.
 

 
 
 
 Comments:
 12 pages, final version
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2502.04177 [math.CO]
 

 
  
 (or 
 arXiv:2502.04177v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2502.04177
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Mathematics & Theoretical Computer Science, vol. 27:3, Graph Theory (September 17, 2025) dmtcs:15257
 

 
 
 Related DOI:
 
 https://doi.org/10.46298/dmtcs.15257

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Louis Esperet [view email] 
 [v1]
 Thu, 6 Feb 2025 16:08:08 UTC (18 KB)

 [v2]
 Tue, 18 Feb 2025 07:31:31 UTC (19 KB)

 [v3]
 Tue, 17 Jun 2025 07:28:10 UTC (14 KB)

 [v4]
 Mon, 15 Sep 2025 15:20:41 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Shallow brambles, by Nicolas Bousquet and Wouter Cames van Batenburg and Louis Esperet and Gwena\"el Joret and Piotr Micek
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
 | 2025-02
 

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
