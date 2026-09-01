Attack the following open graph-theory problem.

Catalog id: 1907.01083__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1907.01083__00/
Source paper: The independent set problem is FPT for even-hole-free graphs (arXiv:1907.01083)

=== Extracted statement (catalog JSON) ===
Title: Open problem: Combinatorial algorithm for MIS on perfect graphs
It remains an open question to find a combinatorial algorithm for the maximum independent set problem on perfect graphs. In fact, we do not even have a combinatorial FPT algorithm for the maximum independent set problem on perfect graphs.

Context:
The maximum independent set problem on perfect graphs is solvable in polynomial time via the ellipsoid method, but a combinatorial algorithm (i.e., one not relying on the ellipsoid method) is unknown. This is mentioned as a side remark motivating the study of related graph classes.

=== Catalog page (statement + literature review) ===
Combinatorial MIS algorithm on perfect graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The problem of finding a combinatorial algorithm for maximum independent set on perfect graphs — avoiding the ellipsoid method of Grötschel-Lovász-Schrijver — has been open since the early 1980s and remains unresolved as of 2026. The source paper raises this as a side remark noting that not even a combinatorial FPT algorithm for MIS on perfect graphs is known. A wide web search covering publications through 2026 found no paper that resolves either the polynomial or FPT combinatorial question for the full class of perfect graphs; recent algorithmic progress has focused on subclasses such as even-hole-free graphs and H-free graphs, leaving the perfect-graph case open.

 Reviewer notes. No follow-up paper resolving this open problem was found. The problem is long-standing (open since Grötschel-Lovász-Schrijver 1981) and is mentioned only as a motivating side remark in the source paper. Recent work (e.g., quasi-polynomial-time algorithms for H-free graphs, polynomial algorithms for graphs excluding subdivided claws) addresses related but strictly different questions. The conjecture is closely related to the broader open question of de-linearizing the Lovász theta function machinery for graph optimization.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It remains an open question to find a combinatorial algorithm for the maximum independent set problem on perfect graphs. In fact, we do not even have a combinatorial FPT algorithm for the maximum independent set problem on perfect graphs.

Context

The maximum independent set problem on perfect graphs is solvable in polynomial time via the ellipsoid method, but a combinatorial algorithm (i.e., one not relying on the ellipsoid method) is unknown. This is mentioned as a side remark motivating the study of related graph classes.

Notes. Stated as a known open problem in the community without a specific attribution cite; no labeled theorem environment.

Source paper

 The independent set problem is FPT for even-hole-free graphs
 Edin Husic, Stephan Thomasse, Nicolas Trotignon · 2019-10-06
 https://arxiv.org/abs/1907.01083
 PDF source

=== Source paper abstract / header ===
Abstract:The class of even-hole-free graphs is very similar to the class of perfect graphs, and was indeed a cornerstone in the tools leading to the proof of the Strong Perfect Graph Theorem. However, the complexity of computing a maximum independent set (MIS) is a long-standing open question in even-hole-free graphs. From the hardness point of view, MIS is W[1]-hard in the class of graphs without induced 4-cycle (when parameterized by the solution size). Halfway of these, we show in this paper that MIS is FPT when parameterized by the solution size in the class of even-hole-free graphs. The main idea is to apply twice the well-known technique of augmenting graphs to extend some initial independent set.
 

 
 
 
 Comments:
 12 pages, 2 figures
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1907.01083 [math.CO]
 

 
  
 (or 
 arXiv:1907.01083v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1907.01083
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Edin Husic [view email] 
 [v1]
 Mon, 1 Jul 2019 21:45:20 UTC (113 KB)

 [v2]
 Sun, 6 Oct 2019 18:57:34 UTC (140 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The independent set problem is FPT for even-hole-free graphs, by Edin Husic and 1 other authors
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
 | 2019-07
 

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
