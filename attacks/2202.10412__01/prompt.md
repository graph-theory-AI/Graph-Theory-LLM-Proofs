Attack the following open graph-theory problem.

Catalog id: 2202.10412__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2202.10412__01/
Source paper: Polynomial bounds for chromatic number VI. Adding a four-vertex path (arXiv:2202.10412)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2.3
Let $\psi, \sigma : \mathbb{N} \to \mathbb{N}$ be non-decreasing polynomials, let $q \geq 0$ an integer, and let $H$ be a broom. Then there is a non-decreasing polynomial $\phi : \mathbb{N} \to \mathbb{N}$ such that if $G$ is a graph, and $\chi(G) > \phi(\omega(G))$, and $G$ contains no $(\psi, q)$-scattering, then $G$ [contains] a $\sigma$-nondominating copy of $H$.

Context:
The authors remark that Conjecture 2.3 is 'an appealing possible strengthening of 2.2 that we could not prove.' Theorem 2.2 (which is proved) requires $H$ to be a broom and $J$ a path, finding both; Conjecture 2.3 would give a $\sigma$-nondominating copy of a broom alone without needing a path. This would extend the self-isolating property (proved for paths as Corollary 2.4) to brooms.

=== Catalog page (statement + literature review) ===
Nondominating broom copy in χ-bounded graphs — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 Graphs with a forbidden induced tree are chi-bounded
 (fuzzy-match score 80).

 
 Status
 open
 high confidence
 

 Conjecture 2.3 from arXiv:2202.10412 would extend the self-isolating property (proved for paths as Corollary 2.4 of the same paper) to brooms, asserting that a graph of sufficiently large chromatic number relative to its clique number and containing no (ψ,q)-scattering must contain a σ-nondominating copy of any given broom H. The authors themselves described it as 'an appealing possible strengthening of 2.2 that we could not prove.' No subsequent paper resolving or substantially advancing this conjecture was found in the literature through May 2026.

 Reviewer notes. No follow-up found. Sophie Spirkl's arXiv listing (arxiv.org/a/spirkl_s_1.html) and Paul Seymour's publication page show no paper specifically addressing sigma-nondominating broom copies or (psi,q)-scattering after 2023. The related 2025 preprint arXiv:2504.21127 (Nguyen, 'On Polynomially High-Chromatic Pure Pairs') extends broom-related poly-chi-bounding results but does not reference Conjecture 2.3 or the scattering/nondominating framework.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $\psi, \sigma : \mathbb{N} \to \mathbb{N}$ be non-decreasing polynomials, let $q \geq 0$ an integer, and let $H$ be a broom. Then there is a non-decreasing polynomial $\phi : \mathbb{N} \to \mathbb{N}$ such that if $G$ is a graph, and $\chi(G) > \phi(\omega(G))$, and $G$ contains no $(\psi, q)$-scattering, then $G$ [contains] a $\sigma$-nondominating copy of $H$.

Context

The authors remark that Conjecture 2.3 is 'an appealing possible strengthening of 2.2 that we could not prove.' Theorem 2.2 (which is proved) requires $H$ to be a broom and $J$ a path, finding both; Conjecture 2.3 would give a $\sigma$-nondominating copy of a broom alone without needing a path. This would extend the self-isolating property (proved for paths as Corollary 2.4) to brooms.

Notes. PDF extraction: the phrase 'then G a σ-nondominating copy of H' is missing the word 'contains'; reconstructed in brackets. Statement otherwise clear.

Source paper

 Polynomial bounds for chromatic number VI. Adding a four-vertex path
 Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl · 2023-03-22
 https://arxiv.org/abs/2202.10412
 PDF source

=== Source paper abstract / header ===
Abstract:A class of graphs is $\chi$-bounded if there is a function $f$ such that every graph $G$ in the class has chromatic number at most $f(\omega(G))$, where $\omega(G)$ is the clique number of $G$; the class is polynomially $\chi$-bounded if $f$ can be taken to be a polynomial. The Gyárfás-Sumner conjecture asserts that, for every forest $H$, the class of $H$-free graphs (graphs with no induced copy of $H$) is $\chi$-bounded. Let us say a forest $H$ is good if it satisfies the stronger property that the class of $H$-free graphs is polynomially $\chi$-bounded.
Very few forests are known to be good: for example, it is open for the five-vertex path. Indeed, it is not even known that if every component of a forest $H$ is good then $H$ is good, and in particular, it was not known that the disjoint union of two four-vertex paths is good. Here we show the latter, and more generally, that if $H$ is good then so is the disjoint union of $H$ and a four-vertex path. We also prove a more general result: if every component of $H_1$ is good, and $H_2$ is any path (or broom) then the class of graphs that are both $H_1$-free and $H_2$-free is polynomially $\chi$-bounded.
 

 
 
 
 Comments:
 Accepted manuscript; see DOI for journal version
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2202.10412 [math.CO]
 

 
  
 (or 
 arXiv:2202.10412v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2202.10412
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 European Journal of Combinatorics, Volume 110, May 2023, 103710
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.ejc.2023.103710

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sophie Spirkl [view email] 
 [v1]
 Mon, 21 Feb 2022 18:19:43 UTC (12 KB)

 [v2]
 Wed, 22 Mar 2023 18:23:52 UTC (12 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Polynomial bounds for chromatic number VI. Adding a four-vertex path, by Maria Chudnovsky and 3 other authors
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
