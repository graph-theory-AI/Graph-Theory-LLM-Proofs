Attack the following open graph-theory problem.

Catalog id: 2204.00722__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2204.00722__00/
Source paper: Twin-width VIII: delineation and win-wins (arXiv:2204.00722)

=== Extracted statement (catalog JSON) ===
Title: Open Question (unit segment graphs delineation)
Are unit segment graphs delineated (by twin-width)?

Context:
The paper establishes that axis-parallel $H_t$-free unit segment graphs have bounded twin-width, while axis-parallel $H_4$-free two-lengthed segment graphs have unbounded twin-width, and that (triangle-free) pure axis-parallel unit segment graphs have unbounded twin-width. This places unit segment graphs at the frontier between delineated and non-delineated intersection graph classes, and the authors explicitly leave their delineation status as an open question.

=== Catalog page (statement + literature review) ===
Delineation of unit segment graphs by twin-width — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The open question of whether unit segment graphs are delineated (by twin-width) remains unresolved for the general class, but significant partial progress has been made. Geniet, Kim, and Meijer (arXiv:2512.21896, 2025) prove that delineation holds for intersection graphs of non-degenerate axis-parallel unit segment graphs, while also showing that delineation fails for visibility graphs of 1.5D terrains; additionally the paper's body discusses non-delineation for more general unit segment variants (degenerate axis-parallel and arbitrary-slope unit segments). The non-degenerate axis-parallel subcase is thus settled positively, but the status of the full class of unit segment graphs — as posed in arXiv:2204.00722 — remains unresolved or at best partially answered negatively for broader subclasses.

 Cited literature (1)

 
 
 
partial First-Order Logic and Twin-Width for Some Geometric Graphs
 (2025)
 

 
 Colin Geniet, Gunwoo Kim, Lucas Meijer · arXiv preprint · arXiv:2512.21896

Proves that delineation holds for non-degenerate axis-parallel unit segment graphs, and that delineation fails for visibility graphs of 1.5D terrains; the paper also establishes non-delineation for degenerate axis-parallel and arbitrary-slope unit segment variants, leaving the general unit segment graph question in a nuanced state.
 

 

 Reviewer notes. The 2025 paper arXiv:2512.21896 makes the most direct progress on this question: it settles the non-degenerate axis-parallel case positively (delineated) but the body of the paper reportedly shows non-delineation for general/degenerate unit segment graphs. Bonnet's open problems page (perso.ens-lyon.fr/edouard.bonnet/openQuestions.html) still lists the question as open. Confidence is medium because the full-paper content was accessed via HTML rendering which may not capture all nuance; the abstract clearly establishes only the positive partial result for non-degenerate axis-parallel unit segment graphs.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Are unit segment graphs delineated (by twin-width)?

Context

The paper establishes that axis-parallel $H_t$-free unit segment graphs have bounded twin-width, while axis-parallel $H_4$-free two-lengthed segment graphs have unbounded twin-width, and that (triangle-free) pure axis-parallel unit segment graphs have unbounded twin-width. This places unit segment graphs at the frontier between delineated and non-delineated intersection graph classes, and the authors explicitly leave their delineation status as an open question.

Notes. Stated verbatim in the abstract: 'We leave as an open question whether unit segment graphs are delineated.'

Source paper

 Twin-width VIII: delineation and win-wins
 Édouard Bonnet, Dibyayan Chakraborty, Eun Jung Kim, Noleen Köhler, Raul Lopes, Stéphan Thomassé · 2022-04-01
 https://arxiv.org/abs/2204.00722
 PDF source

=== Source paper abstract / header ===
Abstract:We introduce the notion of delineation. A graph class $\mathcal C$ is said delineated if for every hereditary closure $\mathcal D$ of a subclass of $\mathcal C$, it holds that $\mathcal D$ has bounded twin-width if and only if $\mathcal D$ is monadically dependent. An effective strengthening of delineation for a class $\mathcal C$ implies that tractable FO model checking on $\mathcal C$ is perfectly understood: On hereditary closures $\mathcal D$ of subclasses of $\mathcal C$, FO model checking is fixed-parameter tractable (FPT) exactly when $\mathcal D$ has bounded twin-width. Ordered graphs [BGOdMSTT, STOC '22] and permutation graphs [BKTW, JACM '22] are effectively delineated, while subcubic graphs are not. On the one hand, we prove that interval graphs, and even, rooted directed path graphs are delineated. On the other hand, we show that segment graphs, directed path graphs, and visibility graphs of simple polygons are not delineated. In an effort to draw the delineation frontier between interval graphs (that are delineated) and axis-parallel two-lengthed segment graphs (that are not), we investigate the twin-width of restricted segment intersection classes. It was known that (triangle-free) pure axis-parallel unit segment graphs have unbounded twin-width [BGKTW, SODA '21]. We show that $K_{t,t}$-free segment graphs, and axis-parallel $H_t$-free unit segment graphs have bounded twin-width, where $H_t$ is the half-graph or ladder of height $t$. In contrast, axis-parallel $H_4$-free two-lengthed segment graphs have unbounded twin-width. Our new results, combined with the known FPT algorithm for FO model checking on graphs given with $O(1)$-sequences, lead to win-win arguments. For instance, we derive FPT algorithms for $k$-Ladder on visibility graphs of 1.5D terrains, and $k$-Independent Set on visibility graphs of simple polygons.
 

 
 
 
 Comments:
 51 pages, 19 figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Logic in Computer Science (cs.LO); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85, 05C75
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2204.00722 [cs.DS]
 

 
  
 (or 
 arXiv:2204.00722v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2204.00722
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Fri, 1 Apr 2022 23:49:17 UTC (185 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width VIII: delineation and win-wins, by \'Edouard Bonnet and 5 other authors
View PDF
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
 | 2022-04
 

 Change to browse by:
 
 cs
 cs.DM
 cs.LO
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
