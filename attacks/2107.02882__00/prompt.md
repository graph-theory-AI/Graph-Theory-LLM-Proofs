Attack the following open graph-theory problem.

Catalog id: 2107.02882__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2107.02882__00/
Source paper: Twin-width and polynomial kernels (arXiv:2107.02882)

=== Catalog page (statement + literature review) ===
Connected k-domination no-kernel at twin-width 4 — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The source paper (arXiv:2107.02882) establishes that Connected k-Dominating Set and Total k-Dominating Set have no polynomial kernel on graphs of bounded twin-width via local gadget modifications of their main reduction, but with a worse upper bound on the twin-width than 4. The open problem asks whether the twin-width bound can be brought down to exactly 4 (matching the result for plain k-Dominating Set in Theorem 1). No follow-up paper resolving this specific question was found in five targeted web searches covering the period 2021–2026.

 Reviewer notes. No follow-up paper resolving or partially addressing this open problem was found. The MFCS 2025 paper on dominating set variants and twin-width (LIPIcs.MFCS.2025.13) addresses FPT algorithms rather than kernelization lower bounds and is unrelated. The conjecture is open with high confidence.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Can one show that Connected $k$-Dominating Set and Total $k$-Dominating Set on graphs of twin-width at most $4$ do not admit a polynomial kernel (unless $\mathrm{coNP} \subseteq \mathrm{NP/poly}$), even when a $4$-sequence of the graph is given?

Context

The authors establish via local gadget modifications of their main reduction (Theorem 1) that Connected $k$-Dominating Set and Total $k$-Dominating Set have no polynomial kernel on graphs of bounded twin-width, but with a worse upper bound on the twin-width than 4. Bringing the twin-width bound down to 4—as achieved for plain $k$-Dominating Set in Theorem 1—would require additional work.

Notes. Implicit open problem stated in prose: 'More work would be necessary to get the lower bound for twin-width at most 4.' Confirmed by Table 1, which lists no 'no PK' entry for Connected k-Dominating Set at twin-width at most 4. PDF source — math notation may be partially garbled.

Source paper

 Twin-width and polynomial kernels
 Édouard Bonnet, Eun Jung Kim, Amadeus Reinald, Stéphan Thomassé, Rémi Watrigant · 2021-09-14
 https://arxiv.org/abs/2107.02882
 PDF source

=== Source paper abstract / header ===
Abstract:We study the existence of polynomial kernels, for parameterized problems without a polynomial kernel on general graphs, when restricted to graphs of bounded twin-width. Our main result is that a polynomial kernel for $k$-Dominating Set on graphs of twin-width at most 4 would contradict a standard complexity-theoretic assumption. The reduction is quite involved, especially to get the twin-width upper bound down to 4, and can be tweaked to work for Connected $k$-Dominating Set and Total $k$-Dominating Set (albeit with a worse upper bound on the twin-width). The $k$-Independent Set problem admits the same lower bound by a much simpler argument, previously observed [ICALP '21], which extends to $k$-Independent Dominating Set, $k$-Path, $k$-Induced Path, $k$-Induced Matching, etc. On the positive side, we obtain a simple quadratic vertex kernel for Connected $k$-Vertex Cover and Capacitated $k$-Vertex Cover on graphs of bounded twin-width. Interestingly the kernel applies to graphs of Vapnik-Chervonenkis density 1, and does not require a witness sequence. We also present a more intricate $O(k^{1.5})$ vertex kernel for Connected $k$-Vertex Cover. Finally we show that deciding if a graph has twin-width at most 1 can be done in polynomial time, and observe that most optimization/decision graph problems can be solved in polynomial time on graphs of twin-width at most 1.
 

 
 
 
 Comments:
 32 pages, 11 figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2107.02882 [cs.DS]
 

 
  
 (or 
 arXiv:2107.02882v2 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2107.02882
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Tue, 6 Jul 2021 20:46:27 UTC (208 KB)

 [v2]
 Tue, 14 Sep 2021 15:08:21 UTC (208 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width and polynomial kernels, by \'Edouard Bonnet and 4 other authors
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
 | 2021-07
 

 Change to browse by:
 
 cs
 cs.CC
 cs.DM
 math
 math.CO
 

 

 

 
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
