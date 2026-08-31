Attack the following open graph-theory problem.

Catalog id: 1908.06300__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1908.06300__01/
Source paper: The stable set problem in graphs with bounded genus and bounded odd cyc… (arXiv:1908.06300)

=== Catalog page (statement + literature review) ===
Stable set for bounded ocp, unbounded genus — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The source paper (arXiv:1908.06300, SODA 2020) establishes a polynomial-time algorithm for the stable set problem when both ocp(G) \leq k and the Euler genus are fixed constants, but leaves open whether the genus restriction can be dropped for k \geq 2. A closely related follow-up by the same authors (arXiv:1911.12179, Mathematical Programming 2022) gives polynomial-size extended formulations for the case ocp(G) \leq 1 without any genus constraint, but that case was already polynomial-time via the bimodular algorithm before the source paper. No paper resolving the general question (bounded ocp, arbitrary Euler genus, k \geq 2) was found in the literature through May 2026.

 Reviewer notes. The open question for arbitrary Euler genus with ocp(G) \leq k (k \geq 2) remains unresolved as of May 2026. The k=1 case (no two disjoint odd cycles) was already tractable before the source paper via the bimodular algorithm; arXiv:1911.12179 (Conforti, Fiorini, Huynh, Weltge, Math. Programming 2022) further gives an O(n^2)-size extended formulation for k=1 without genus restriction, but this does not directly resolve the open question for larger k. No counterexample or general algorithm dropping the genus constraint was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Is the stable set problem polynomial-time solvable for graphs $G$ with $\mathrm{ocp}(G) \leq k$ (for fixed $k$) embedded in a surface of arbitrary Euler genus?

Context

The paper's main result (Theorem 2) gives a polynomial-time algorithm when both the odd cycle packing number and the Euler genus are fixed constants. Immediately after stating this result the authors note they do not know whether the genus bound can be dropped while retaining polynomial-time solvability.

Notes. Stated as 'we do not know whether'; no labelled theorem environment.

Source paper

 The stable set problem in graphs with bounded genus and bounded odd cycle packing number
 Michele Conforti, Samuel Fiorin, Tony Huynh, Gwenaël Joret, Stefan Weltge · 2019-08-17
 https://arxiv.org/abs/1908.06300
 PDF source

=== Source paper abstract / header ===
Abstract:Consider the family of graphs without $ k $ node-disjoint odd cycles, where $ k $ is a constant. Determining the complexity of the stable set problem for such graphs $ G $ is a long-standing problem. We give a polynomial-time algorithm for the case that $ G $ can be further embedded in a (possibly non-orientable) surface of bounded genus. Moreover, we obtain polynomial-size extended formulations for the respective stable set polytopes.
To this end, we show that $2$-sided odd cycles satisfy the Erdős-Pósa property in graphs embedded in a fixed surface. This extends the fact that odd cycles satisfy the Erdős-Pósa property in graphs embedded in a fixed orientable surface (Kawarabayashi & Nakamoto, 2007).
Eventually, our findings allow us to reduce the original problem to the problem of finding a minimum-cost non-negative integer circulation of a certain homology class, which turns out to be efficiently solvable in our case.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Combinatorics (math.CO); Optimization and Control (math.OC)
 

 Cite as:
 arXiv:1908.06300 [cs.DM]
 

 
  
 (or 
 arXiv:1908.06300v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1908.06300
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Stefan Weltge [view email] 
 [v1]
 Sat, 17 Aug 2019 13:10:18 UTC (46 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The stable set problem in graphs with bounded genus and bounded odd cycle packing number, by Michele Conforti and 4 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2019-08
 

 Change to browse by:
 
 cs
 cs.DS
 math
 math.CO
 math.OC
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Michele Conforti
Samuel Fiorini
Tony Huynh
Gwenaël Joret
Stefan Weltge 

 

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
