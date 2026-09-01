Attack the following open graph-theory problem.

Catalog id: 2311.05713__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2311.05713__00/
Source paper: List-$k$-Coloring $H$-free graphs for all $k>4$ (arXiv:2311.05713)

=== Extracted statement (catalog JSON) ===
Title: Converse to Theorem 1.1 (3-Coloring dichotomy for $H$-free graphs)
If every component of $H$ is a path, then the $3$-Coloring Problem restricted to $H$-free graphs can be solved in polynomial time.

Context:
Theorem 1.1 (Holyer; Kamiński and Lozin) establishes that if $H$ has at least one component which is not a path then the $3$-Coloring Problem on $H$-free graphs is NP-hard. Immediately after stating this theorem the paper notes: 'The converse to Theorem 1.1 is wide open.'

=== Catalog page (statement + literature review) ===
Polynomial 3-coloring for path-component-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that 3-Coloring is polynomial-time solvable on $H$-free graphs whenever every component of $H$ is a path is explicitly called 'wide open' in the source paper. The complexity of 3-Coloring on $H$-free graphs has been settled for all $H$ on at most seven vertices, with the two remaining open cases being $H = P_8$ and $H = 2P_4$; no follow-up paper resolving the full conjecture was found in the literature through May 2026.

 Reviewer notes. The source paper (arXiv:2311.05713) proves a full dichotomy for List-k-Coloring with k>4 but explicitly leaves the k=3 case open. The main bottleneck cases identified in the literature are P8-free graphs and 2P4-free graphs. A 2025 paper (arXiv:2509.02423) studies 4-coloring of (Pt,C3)-free graphs (NP-hardness direction) but does not touch the 3-coloring/path conjecture. The STACS 2026 paper on list coloring ordered graphs addresses k=4 in a different setting and does not resolve this conjecture.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. If every component of $H$ is a path, then the $3$-Coloring Problem restricted to $H$-free graphs can be solved in polynomial time.

Context

Theorem 1.1 (Holyer; Kamiński and Lozin) establishes that if $H$ has at least one component which is not a path then the $3$-Coloring Problem on $H$-free graphs is NP-hard. Immediately after stating this theorem the paper notes: 'The converse to Theorem 1.1 is wide open.'

Notes. Not a labelled environment; the open problem is identified by the remark 'The converse to Theorem 1.1 is wide open.' The statement of the converse is implicit and reconstructed from Theorem 1.1.

Source paper

 List-$k$-Coloring $H$-free graphs for all $k>4$
 Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · 2023-11-09
 https://arxiv.org/abs/2311.05713
 PDF source

=== Source paper abstract / header ===
Abstract:Given an integer $k>4$ and a graph $H$, we prove that, assuming P$\neq$NP, the List-$k$-Coloring Problem restricted to $H$-free graphs can be solved in polynomial time if and only if either every component of $H$ is a path on at most three vertices, or removing the isolated vertices of $H$ leaves an induced subgraph of the five-vertex path. In fact, the "if" implication holds for all $k\geq 1$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2311.05713 [math.CO]
 

 
  
 (or 
 arXiv:2311.05713v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2311.05713
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Combinatorica 44 (2024). 1063-1068
 

 
 
 Related DOI:
 
 https://doi.org/10.1007/s00493-024-00106-2

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sepehr Hajebi [view email] 
 [v1]
 Thu, 9 Nov 2023 19:48:23 UTC (107 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled List-$k$-Coloring $H$-free graphs for all $k>4$, by Maria Chudnovsky and 2 other authors
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
 | 2023-11
 

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
