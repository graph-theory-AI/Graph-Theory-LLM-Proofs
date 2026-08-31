Attack the following open graph-theory problem.

Catalog id: 2506.08810__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2506.08810__01/
Source paper: Infinite induced-saturated graphs (arXiv:2506.08810)

=== Catalog page (statement + literature review) ===
Disconnectedness of H-free graphs adjacency structure — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 22 from arXiv:2506.08810 asks for which finite graphs H the flip graph G_{H,n} (whose vertices are H-free graphs on [n] and whose edges connect graphs differing by exactly one edge) is disconnected for all sufficiently large n. The paper itself establishes that G_{P_4,n} is connected for all n≥1, ruling out universal disconnectedness. No follow-up paper addressing this problem was found in the indexed literature as of May 2026.

 Reviewer notes. No follow-up work found. Semantic Scholar returns zero citations for arXiv:2506.08810 as of May 2026. The paper appeared in the Canadian Journal of Mathematics. The problem is recent (posted June 2025) and is a weaker relaxation of H-induced-saturation: an H-induced-saturated graph on n vertices corresponds to an isolated vertex in G_{H,n}, so disconnectedness of G_{H,n} is strictly weaker. The only known case mentioned in the paper is that G_{P_4,n} is connected for all n≥1.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. For a finite graph $H$ and integer $n$, let $G_{H,n}$ denote the graph with the $H$-free graphs on vertex set $[n]$ as vertices, and with an edge between $G,G^{\prime}\in V(G_{H,n})$ if and only if $|E(G)\triangle E(G^{\prime})|=1$. For which $H$ is $G_{H,n}$ disconnected for all sufficiently large $n$?

Context

An $H$-induced-saturated graph on $n$ vertices corresponds to an isolated vertex in $G_{H,n}$; disconnectedness is a weaker but potentially more tractable property. The authors note that $G_{P_4,n}$ is connected for all $n\geq 1$, so disconnectedness is not universal.

Source paper

 Infinite induced-saturated graphs
 Marthe Bonamy, Carla Groenland, Tom Johnston, Natasha Morrison, Alex Scott · 2025-09-01
 https://arxiv.org/abs/2506.08810

=== Source paper abstract / header ===
Abstract:A graph $G$ is $H$-induced-saturated if $G$ is $H$-free but deleting any edge or adding any edge creates an induced copy of $H$. There are non-trivial graphs $H$, such as $P_4$, for which no finite $H$-induced-saturated graph $G$ exists. We show that for every finite graph $H$ that is not a clique or an independent set, there always exists a countable $H$-induced-saturated graph. In fact, we show that a far stronger property can be achieved: there is a countably infinite $H$-free graph $G$ such that any graph $G'\ne G$ obtained by making a locally finite set of changes to $G$ contains a copy of $H$.
 

 
 
 
 Comments:
 26 pages, 13 figures
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2506.08810 [math.CO]
 

 
  
 (or 
 arXiv:2506.08810v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2506.08810
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Carla Groenland [view email] 
 [v1]
 Tue, 10 Jun 2025 14:00:59 UTC (34 KB)

 [v2]
 Wed, 20 Aug 2025 10:44:56 UTC (36 KB)

 [v3]
 Mon, 1 Sep 2025 10:23:31 UTC (36 KB)

 

 
 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Infinite induced-saturated graphs, by Marthe Bonamy and Carla Groenland and Tom Johnston and Natasha Morrison and Alex Scott
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Ancillary-file links:
 Ancillary files (details):

 small_graphs.py
 theorem_10.py

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2025-06
 

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
