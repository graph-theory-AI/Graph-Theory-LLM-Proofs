Attack the following open graph-theory problem.

Catalog id: 2004.14789__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.14789__01/
Source paper: Twin-width I: tractable FO model checking (arXiv:2004.14789)

=== Extracted statement (catalog JSON) ===
Title: Question (common superclass for FPT FO model checking)
Do bounded twin-width and nowhere dense classes admit a natural common superclass still admitting an FPT algorithm for FO model checking?

Context:
Figure 3 shows that bounded twin-width and nowhere dense classes together roughly subsume all current knowledge on fixed-parameter tractability of FO model checking. The authors explicitly pose whether a natural common superclass of both still admits an FPT algorithm for FO model checking.

=== Catalog page (statement + literature review) ===
FPT FO model checking superclass of twin-width — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The natural candidate common superclass — monadically NIP (monadically dependent) classes — has been identified in the literature and is known to contain both bounded twin-width and nowhere dense classes. Significant partial progress has been made: FPT FO model checking was proved for all monadically stable graph classes (which strictly contain all nowhere dense classes) in 2023, and for all classes of bounded merge-width (which unify bounded twin-width and bounded expansion) in 2025. The full question of whether all monadically NIP/dependent classes admit FPT FO model checking remains an open conjecture, widely regarded as the central problem in the area.

 Cited literature (2)

 
 
 
partial First-Order Model Checking on Monadically Stable Graph Classes
 (2023)
 

 
 Jan Dreier et al. · arXiv preprint · arXiv:2311.18740

Proves FPT FO model checking for all monadically stable graph classes, a strict superclass of nowhere dense that does not subsume bounded twin-width, extending one half of the question.
 

 
 
partial Merge-width and First-Order Model Checking
 (2025)
 

 
 Jan Dreier, Szymon Toruńczyk · arXiv preprint · arXiv:2502.18065

Introduces merge-width, a parameter whose bounded classes subsume both bounded expansion and bounded twin-width, and proves FPT FO model checking for all classes of bounded merge-width, giving a unified common superclass for the algorithmic part of the question.
 

 

 Reviewer notes. Monadically NIP (= monadically dependent) is the broadly accepted natural candidate for the common superclass asked about: it contains both bounded twin-width and nowhere dense classes, and the conjecture that FPT FO model checking holds exactly on monadically NIP hereditary classes is the central open problem in parameterized model checking. The two papers cited give FPT for important proper sub-cases: monadically stable (⊇ nowhere dense, published as arXiv:2311.18740) and bounded merge-width (⊇ bounded twin-width ∪ bounded expansion, published as arXiv:2502.18065 and appearing at STOC 2025). The question is therefore partially resolved: a natural common superclass with FPT is known (bounded merge-width), and evidence strongly points to monadically NIP as the tight characterisation, but the full statement for all monadically NIP classes is open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Do bounded twin-width and nowhere dense classes admit a natural common superclass still admitting an FPT algorithm for FO model checking?

Context

Figure 3 shows that bounded twin-width and nowhere dense classes together roughly subsume all current knowledge on fixed-parameter tractability of FO model checking. The authors explicitly pose whether a natural common superclass of both still admits an FPT algorithm for FO model checking.

Notes. Posed as a rhetorical question in the caption of Figure 3, not in a labelled theorem environment.

Source paper

 Twin-width I: tractable FO model checking
 Édouard Bonnet, Eun Jung Kim, Stéphan Thomassé, Rémi Watrigant · 2021-10-25
 https://arxiv.org/abs/2004.14789
 PDF source

=== Source paper abstract / header ===
Abstract:Inspired by a width invariant defined on permutations by Guillemot and Marx [SODA '14], we introduce the notion of twin-width on graphs and on matrices. Proper minor-closed classes, bounded rank-width graphs, map graphs, $K_t$-free unit $d$-dimensional ball graphs, posets with antichains of bounded size, and proper subclasses of dimension-2 posets all have bounded twin-width. On all these classes (except map graphs without geometric embedding) we show how to compute in polynomial time a sequence of $d$-contractions, witness that the twin-width is at most $d$. We show that FO model checking, that is deciding if a given first-order formula $\phi$ evaluates to true for a given binary structure $G$ on a domain $D$, is FPT in $|\phi|$ on classes of bounded twin-width, provided the witness is given. More precisely, being given a $d$-contraction sequence for $G$, our algorithm runs in time $f(d,|\phi|) \cdot |D|$ where $f$ is a computable but non-elementary function. We also prove that bounded twin-width is preserved by FO interpretations and transductions (allowing operations such as squaring or complementing a graph). This unifies and significantly extends the knowledge on fixed-parameter tractability of FO model checking on non-monotone classes, such as the FPT algorithm on bounded-width posets by Gajarský et al. [FOCS '15].
 

 
 
 
 Comments:
 49 pages, 9 figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Logic in Computer Science (cs.LO)
 
 
 MSC classes:
 68Q25
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2004.14789 [cs.DS]
 

 
  
 (or 
 arXiv:2004.14789v3 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2004.14789
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Thu, 30 Apr 2020 14:05:41 UTC (89 KB)

 [v2]
 Wed, 23 Sep 2020 13:47:30 UTC (91 KB)

 [v3]
 Mon, 25 Oct 2021 15:10:57 UTC (93 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width I: tractable FO model checking, by \'Edouard Bonnet and 3 other authors
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
 | 2020-04
 

 Change to browse by:
 
 cs
 cs.DM
 cs.LO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Eun Jung Kim
Stéphan Thomassé
Rémi Watrigant 

 

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
