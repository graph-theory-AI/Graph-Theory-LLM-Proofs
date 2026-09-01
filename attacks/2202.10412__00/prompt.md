Attack the following open graph-theory problem.

Catalog id: 2202.10412__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2202.10412__00/
Source paper: Polynomial bounds for chromatic number VI. Adding a four-vertex path (arXiv:2202.10412)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture (every forest is good)
Perhaps every forest is good (i.e., for every forest $H$, the class of $H$-free graphs is polynomially $\chi$-bounded).

Context:
After recalling that Esperet's conjecture that every $\chi$-bounded hereditary class is polynomially $\chi$-bounded was disproved, the authors ask which hereditary classes are polynomially $\chi$-bounded and raise in particular whether the Gyárfás-Sumner conjecture can be strengthened to polynomial $\chi$-boundedness. They note that among trees, only those not containing $P_5$ are currently known to be good, and that it is not even known whether $P_5$ is good.

=== Catalog page (statement + literature review) ===
Polynomial χ-boundedness for H-free forest classes — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 Graphs with a forbidden induced tree are chi-bounded
 (fuzzy-match score 80).

 
 Status
 partial
 high confidence
 

 The conjecture that every forest H is good (H-free graphs are polynomially χ-bounded) remains open in general, but has seen major progress. At the time of the source paper, P₅ was the smallest forest not known to be good; in December 2025 Tung H. Nguyen (arXiv:2512.24907) proved that P₅-free graphs are polynomially χ-bounded, resolving that open case. The polynomial Gyárfás-Sumner conjecture has also been established for bounded-boxicity graphs (arXiv:2407.16882). Forests requiring longer induced paths (P₆ and beyond) remain open.

 Cited literature (3)

 
 
 
partial Polynomial Gyárfás-Sumner conjecture for graphs of bounded boxicity
 (2024)
 

 
 not retrieved · arXiv preprint · arXiv:2407.16882

Proves that for every positive integer d and every forest F, the class of intersection graphs of axis-aligned boxes in ℝ^d with no induced F is polynomially χ-bounded, establishing the polynomial Gyárfás-Sumner conjecture for bounded-boxicity graphs.
 

 
 
partial On polynomially high-chromatic pure pairs
 (2025)
 

 
 Tung H. Nguyen · arXiv preprint · arXiv:2504.21127

Provides further supporting evidence for the polynomial Gyárfás-Sumner conjecture for P₅ by proving that every P₅-free graph with clique number ω≥2 contains a polynomially high-chromatic complete pair of induced subgraphs.
 

 
 
partial Polynomial χ-boundedness for excluding P₅
 (2025)
 

 
 Tung H. Nguyen · arXiv preprint · arXiv:2512.24907

Proves that chromatic number is polynomially bounded by clique number for graphs with no induced P₅, resolving the P₅ case of the conjecture and a 1985 open problem of Gyárfás; the full conjecture for all forests remains open.
 

 

 Reviewer notes. The P₅ case (the smallest open case noted in the source paper) was resolved by Nguyen in December 2025 (arXiv:2512.24907). However, the full conjecture for every forest remains open: proving P₅-free is polynomially χ-bounded does not directly yield polynomial bounds for P₆-free or other larger-forest-free classes, since P₆-free is a strictly larger class. Authors for arXiv:2407.16882 were not extracted from the fetch.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Perhaps every forest is good (i.e., for every forest $H$, the class of $H$-free graphs is polynomially $\chi$-bounded).

Context

After recalling that Esperet's conjecture that every $\chi$-bounded hereditary class is polynomially $\chi$-bounded was disproved, the authors ask which hereditary classes are polynomially $\chi$-bounded and raise in particular whether the Gyárfás-Sumner conjecture can be strengthened to polynomial $\chi$-boundedness. They note that among trees, only those not containing $P_5$ are currently known to be good, and that it is not even known whether $P_5$ is good.

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
