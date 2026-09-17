Attack the following open graph-theory problem.

Catalog id: 2002.05383__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2002.05383__00/
Source paper: An update on reconfiguring $10$-colorings of planar graphs (arXiv:2002.05383)

=== Extracted statement (catalog JSON) ===
Title: Problem 3
What is the minimum integer $\kappa$ such that for every planar graph $G$ with $n$ vertices, $R_{\kappa}(G)$ has diameter $O(n)$?

Context:
Planar graphs are 5-degenerate and have maximum average degree less than 6; prior results give $R_8(G)$ diameter $O(n(\log n)^7)$ and $R_{12}(G)$ diameter at most $6n$ for planar $G$. The paper improves the upper bound to $\kappa \leq 10$ via Theorem 4, and an isolated 6-coloring of the icosahedron shows $\kappa \geq 7$; the authors note that $\kappa = 7$ cannot be excluded.

=== Catalog page (statement + literature review) ===
Linear diameter of planar graph reconfigurations — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Problem 3 asks for the minimum $\kappa$ such that $R_\kappa(G)$ has diameter $O(n)$ for every $n$-vertex planar graph $G$. The source paper establishes $7 \leq \kappa \leq 10$. A 2024 paper (arXiv:2411.00679, EJC 2025) proves a conjecture of Dvo\v{r}\'ak and Feghali in the list-coloring setting, showing that any two 10-list-colorings of a planar graph can be connected by a recoloring sequence of length linear in the number of vertices. The exact minimum $\kappa$ for uniform $k$-colorings of general planar graphs remains open.

 Cited literature (1)

 
 
 
partial 10-list Recoloring of Planar Graphs
 (2024)
 

 
 unverified · European Journal of Combinatorics · arXiv:2411.00679

Confirms a conjecture of Dvo\v{r}\'ak and Feghali: for any 10-list assignment of a planar graph, any two list-colorings can be connected by a recoloring sequence of length linear in the number of vertices, published in EJC December 2025.
 

 

 Reviewer notes. The gap 7 \leq \kappa \leq 10 established in the source paper has not been fully closed for general planar graphs. arXiv:2006.09269 ('A Thomassen-type method for planar graph recoloring', June 2020) gives related bounds via a different technique but falls within the same calendar year as the source paper and was not included in since_posted. arXiv:2411.00679 resolves the generalized list-coloring variant. Author names for since_posted entries could not be confirmed within the web-call cap.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the minimum integer $\kappa$ such that for every planar graph $G$ with $n$ vertices, $R_{\kappa}(G)$ has diameter $O(n)$?

Context

Planar graphs are 5-degenerate and have maximum average degree less than 6; prior results give $R_8(G)$ diameter $O(n(\log n)^7)$ and $R_{12}(G)$ diameter at most $6n$ for planar $G$. The paper improves the upper bound to $\kappa \leq 10$ via Theorem 4, and an isolated 6-coloring of the icosahedron shows $\kappa \geq 7$; the authors note that $\kappa = 7$ cannot be excluded.

Source paper

 An update on reconfiguring $10$-colorings of planar graphs
 Zdeněk Dvořák, Carl Feghali · 2020-02-13
 https://arxiv.org/abs/2002.05383
 PDF source

=== Source paper abstract / header ===
Abstract:The reconfiguration graph $R_k(G)$ for the $k$-colorings of a graph $G$ has as vertex set the set of all possible proper $k$-colorings of $G$ and two colorings are adjacent if they differ in the color of exactly one vertex. A result of Bousquet and Perarnau (2016) regarding graphs of bounded degeneracy implies that if $G$ is a planar graph with $n$ vertices, then $R_{12}(G)$ has diameter at most $6n$. We improve on the number of colors, showing that $R_{10}(G)$ has diameter at most $8n$ for every planar graph $G$ with $n$ vertices.
 

 
 
 
 Comments:
 25 pages, 1 figure
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15
 

 Cite as:
 arXiv:2002.05383 [math.CO]
 

 
  
 (or 
 arXiv:2002.05383v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2002.05383
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Carl Feghali [view email] 
 [v1]
 Thu, 13 Feb 2020 08:06:21 UTC (48 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled An update on reconfiguring $10$-colorings of planar graphs, by Zden\v{e}k Dvo\v{r}\'ak and Carl Feghali
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
 | 2020-02
 

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
