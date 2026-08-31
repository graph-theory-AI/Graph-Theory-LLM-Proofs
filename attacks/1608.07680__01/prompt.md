Attack the following open graph-theory problem.

Catalog id: 1608.07680__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1608.07680__01/
Source paper: The crossing number of the cone of a graph (arXiv:1608.07680)

=== Catalog page (statement + literature review) ===
Crossing bound for 2-page extension of 1-page drawing — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Problem 4 from arXiv:1608.07680 asks for a general upper bound on the crossings of an optimal 2-page drawing of G (with fixed spine order) given a 1-page drawing with k crossings; the paper itself provides only a partial answer via the Edwards max-cut bound. A 2021 follow-up note by Ding and Huang (Graphs and Combinatorics) builds on the original work by improving values of the function f(k) for small k, but I could not access its full text to confirm whether it resolves Problem 4. No paper specifically solving the general 1-page-to-2-page bound question was found in the verified literature.

 Reviewer notes. A follow-up paper titled 'A Note on the Crossing Number of the Cone of a Graph' by Ding and Huang was published in Graphs and Combinatorics in 2021 (DOI: 10.1007/s00373-021-02361-2). Search snippets indicate it shows ϕs(6)=5 and ϕs(7)=6 (exact values of f(k) for simple graphs), which concerns the f(k) function rather than the 1-page-to-2-page bound of Problem 4 specifically. The Springer URL was inaccessible (authentication redirect) and no arXiv preprint was found, so this paper is not included in since_posted per the verification requirement. The original paper's partial answer via the Edwards max-cut bound remains the only known published result directly addressing Problem 4.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Given a 1-page drawing of a graph $G$ with $k$ crossings, find an upper bound on the number of crossings of an optimal 2-page drawing of $G$ while having the order of vertices of $G$ on the spine unchanged.

Context

This problem asks: if all vertices of $G$ are incident to the outer face (equivalently, $G$ admits a 1-page drawing), what is the most efficient way to redraw some edges in a new page to reduce crossings? It is intimately related to bounding the crossing number of the cone, and the Edwards max-cut bound (Lemma 5) is applied to answer it partially.

Source paper

 The crossing number of the cone of a graph
 Carlos A. Alfaro, Alan Arroyo, Marek Derunár, Bojan Mohar · 2016-08-27
 https://arxiv.org/abs/1608.07680
 PDF source

=== Source paper abstract / header ===
Abstract:Motivated by a problem asked by Richter and by the long standing Harary-Hill conjecture, we study the relation between the crossing number of a graph $G$ and the crossing number of its cone $CG$, the graph obtained from $G$ by adding a new vertex adjacent to all the vertices in $G$. Simple examples show that the difference $cr(CG)-cr(G)$ can be arbitrarily large for any fixed $k=cr(G)$. In this work, we are interested in finding the smallest possible difference, that is, for each non-negative integer $k$, find the smallest $f(k)$ for which there exists a graph with crossing number at least $k$ and cone with crossing number $f(k)$. For small values of $k$, we give exact values of $f(k)$ when the problem is restricted to simple graphs, and show that $f(k)=k+\Theta (\sqrt {k})$ when multiple edges are allowed.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1608.07680 [math.CO]
 

 
  
 (or 
 arXiv:1608.07680v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1608.07680
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alan Arroyo [view email] 
 [v1]
 Sat, 27 Aug 2016 09:08:33 UTC (43 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The crossing number of the cone of a graph, by Carlos A. Alfaro and 3 other authors
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
 | 2016-08
 

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
