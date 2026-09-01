Attack the following open graph-theory problem.

Catalog id: 2312.13965__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2312.13965__00/
Source paper: The growth rate of multicolor Ramsey numbers of $3$-graphs (arXiv:2312.13965)

=== Extracted statement (catalog JSON) ===
Title: Problem 1.1
Given a fixed $k$-uniform hypergraph $G$, determine the integer $h$ (if it exists) such that $r(G;q)$ grows as a tower of height $h$ as $q$ tends to infinity.

Context:
In the graph case, $r(G;q)$ grows as a tower of height $1$ if $G$ is bipartite (with at least two edges) and as a tower of height $2$ otherwise. For 3-uniform hypergraphs, Abbott and Williams showed that $r(K_4^{(3)};q)$ grows as a tower of height $3$. The paper's main theorem (Theorem 1.4) resolves this problem for $k=3$ in full generality.

=== Catalog page (statement + literature review) ===
Tower height for k-uniform Ramsey growth rate — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The source paper's own Theorem 1.4 fully resolves Problem 1.1 for $k=3$: every 3-uniform hypergraph $G$ falls into one of three growth-rate regimes for $r(G;q)$ (polynomial, single-exponential, or double-exponential in $q$), giving tower heights $h\in\{1,2,3\}$ depending on structural properties of $G$. For $k\geq 4$ the general classification remains open; arXiv:2502.20863 (2025) establishes lower bounds on the tower height for $k$-uniform hypergraphs of bounded degree, showing the tower height can reach $k$ for $k\geq 3$, but a complete determination of $h$ for arbitrary $k$-uniform $G$ with $k\geq 4$ has not yet been achieved.

 Cited literature (1)

 
 
 
partial Lower bounds for Ramsey numbers of bounded degree hypergraphs
 (2025)
 

 
 Domagoj Bradač, Matthew Kendall Hunter, Benny Sudakov · arXiv preprint · arXiv:2502.20863

Proves that for all $k\geq 3$ there exist $k$-uniform hypergraphs of bounded degree whose 4-color Ramsey number grows as a tower of height $k$, extending tower-height lower bounds to $k\geq 4$ for specific hypergraphs but not providing a full classification.
 

 

 Reviewer notes. Problem 1.1 is already partially self-resolved: the paper containing it (Theorem 1.4) settles the k=3 case in full generality. The open part is k≥4. arXiv:2502.20863 provides new tower-height lower bounds for bounded-degree k-uniform hypergraphs (k≥3) but stops short of a complete classification for all k-uniform hypergraphs with k≥4.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. Given a fixed $k$-uniform hypergraph $G$, determine the integer $h$ (if it exists) such that $r(G;q)$ grows as a tower of height $h$ as $q$ tends to infinity.

Context

In the graph case, $r(G;q)$ grows as a tower of height $1$ if $G$ is bipartite (with at least two edges) and as a tower of height $2$ otherwise. For 3-uniform hypergraphs, Abbott and Williams showed that $r(K_4^{(3)};q)$ grows as a tower of height $3$. The paper's main theorem (Theorem 1.4) resolves this problem for $k=3$ in full generality.

Source paper

 The growth rate of multicolor Ramsey numbers of $3$-graphs
 Domagoj Bradač, Jacob Fox, Benny Sudakov · 2024-04-29
 https://arxiv.org/abs/2312.13965

=== Source paper abstract / header ===
Abstract:The $q$-color Ramsey number of a $k$-uniform hypergraph $G,$ denoted $r(G;q)$, is the minimum integer $N$ such that any coloring of the edges of the complete $k$-uniform hypergraph on $N$ vertices contains a monochromatic copy of $G$. The study of these numbers is one of the most central topics in combinatorics. One natural question, which for triangles goes back to the work of Schur in 1916, is to determine the behaviour of $r(G;q)$ for fixed $G$ and $q$ tending to infinity. In this paper we study this problem for $3$-uniform hypergraphs and determine the tower height of $r(G;q)$ as a function of $q$. More precisely, given a hypergraph $G$, we determine when $r(G; q)$ behaves polynomially, exponentially or double-exponentially in $q$. This answers a question of Axenovich, Gyárfás, Liu and Mubayi.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2312.13965 [math.CO]
 

 
  
 (or 
 arXiv:2312.13965v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2312.13965
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Domagoj Bradač [view email] 
 [v1]
 Thu, 21 Dec 2023 15:51:41 UTC (19 KB)

 [v2]
 Mon, 29 Apr 2024 09:12:42 UTC (64 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The growth rate of multicolor Ramsey numbers of $3$-graphs, by Domagoj Brada\v{c} and 1 other authors
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
 | 2023-12
 

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
