Attack the following open graph-theory problem.

Catalog id: 1608.07680__00
Catalog status: partial (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1608.07680__00/
Source paper: The crossing number of the cone of a graph (arXiv:1608.07680)

=== Extracted statement (catalog JSON) ===
Title: Problem 1
For each $k \geq 0$, find the smallest integer $f(k)$ for which there is a graph $G$ with crossing number at least $k$ and its cone has $\operatorname{cr}(CG) = f(k)$.

Context:
Motivated by the negative answer to Richter's question for $n=6$, the authors reformulate the problem as finding the minimum possible crossing number of a cone over all graphs of a given crossing number. Equivalently, $f(k)$ is the largest integer such that every graph with $\operatorname{cr}(G) \geq k$ satisfies $\operatorname{cr}(CG) \geq f(k)$. The paper proves $f(k) = k + \Theta(\sqrt{k})$ for multigraphs.

=== Catalog page (statement + literature review) ===
Extremal cone crossing number function — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The problem asks for a general formula for f(k), the smallest crossing number achievable by the cone of any graph with crossing number at least k. The source paper (published as SIAM J. Discrete Math. 32 (2018) 2080–2093) establishes f(k) = k + Θ(√k) for multigraphs and computes the simple-graph version φ_s(3)=3, φ_s(4)=4, φ_s(5)=5. Ding and Huang (Graphs Combin. 2021) extend this table by proving φ_s(6)=5 and φ_s(7)=6. A closed-form formula for all k remains open.

 Cited literature (1)

 
 
 
partial A Note on the Crossing Number of the Cone of a Graph
 (2021)
 

 
 Ding, Z., Huang, Y. · Graphs and Combinatorics · doi:10.1007/s00373-021-02361-2

Proves φ_s(6) = 5 and φ_s(7) = 6 for simple graphs, extending the table of exact values of f(k) from the source paper.
 

 

 Reviewer notes. The Ding-Huang 2021 follow-up paper (Graphs Combin. 37:2351-2363) is behind a paywall; its content was confirmed via multiple consistent search results. No arXiv preprint was found for that paper. The general formula for f(k) (or φ_s(k) in the simple-graph setting) for all k ≥ 0 remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. For each $k \geq 0$, find the smallest integer $f(k)$ for which there is a graph $G$ with crossing number at least $k$ and its cone has $\operatorname{cr}(CG) = f(k)$.

Context

Motivated by the negative answer to Richter's question for $n=6$, the authors reformulate the problem as finding the minimum possible crossing number of a cone over all graphs of a given crossing number. Equivalently, $f(k)$ is the largest integer such that every graph with $\operatorname{cr}(G) \geq k$ satisfies $\operatorname{cr}(CG) \geq f(k)$. The paper proves $f(k) = k + \Theta(\sqrt{k})$ for multigraphs.

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
