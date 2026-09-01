Attack the following open graph-theory problem.

Catalog id: 2108.02685__01
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2108.02685__01/
Source paper: Irregular Subgraphs (arXiv:2108.02685)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.2
Every graph $G$ with $n$ vertices and minimum degree $\delta$ contains a spanning subgraph $H$ satisfying $m(H) \leq \frac{n}{\delta+1} + 2$.

Context:
This is the second of the two central conjectures introduced by the authors, generalising Conjecture 1.1 from regular graphs to arbitrary graphs with minimum degree $\delta$. Both conjectures remain open; the paper proves asymptotic relaxations showing the bound $(1+o(1))\frac{n}{\delta+1}+2$ is achievable when $n$ is large.

=== Catalog page (statement + literature review) ===
Irregular spanning subgraph with minimum degree bound — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 1.2 from arXiv:2108.02685 remains open in full generality. Fox, Luo, and Pham (2022) proved the asymptotic version for d-regular graphs when d = o(n/(log n)^{12}) via probabilistic methods. Ma and Xie (2024) obtained the first n-independent bound for d-regular graphs (within 2d^2 of the conjectured value) and proved the conjecture in strong form for d=3 regular graphs using deterministic local-adjustment techniques. Luzar, Przybylo, and Sotak (2024) independently resolved the cubic case exactly, showing deviation from n/4 is at most 1/2 (up to three exceptions). The exact bound for general graphs with minimum degree delta is still open.

 Cited literature (3)

 
 
 
partial On random irregular subgraphs
 (2022)
 

 
 Jacob Fox, Sammy Luo, Huy Tuan Pham · Random Structures & Algorithms · arXiv:2207.13651

Proves the asymptotic version of the conjecture for d-regular graphs when d = o(n/(log n)^{12}): with high probability the irregular random subgraph satisfies m(H,k) = (1+o(1))n/(d+1) for all 0 <= k <= d.
 

 
 
partial Finding irregular subgraphs via local adjustments
 (2024)
 

 
 Jie Ma, Shengjie Xie · arXiv preprint · arXiv:2406.05675

Gives the first n-independent bound for d-regular graphs (vertex degree counts within 2d^2 of n/(d+1)) and proves the conjecture in strong form for cubic (d=3) regular graphs via deterministic local-adjustment methods.
 

 
 
partial Degree-balanced decompositions of cubic graphs
 (2024)
 

 
 Borut Luzar, Jakub Przybylo, Roman Sotak · arXiv preprint · arXiv:2408.16121

Resolves the Alon-Wei conjecture for cubic graphs, showing that every cubic graph on n vertices has a spanning subgraph where the number of vertices of each degree deviates from n/4 by at most 1/2, up to three exceptions.
 

 

 Reviewer notes. The conjecture is closely related to Conjecture 1.1 (the regular-graph version). Most follow-up work addresses the regular case; the minimum-degree generalisation of Conjecture 1.2 has seen partial progress only through the special case d=3 and asymptotic results. No paper found that resolves the full conjecture for arbitrary minimum degree delta.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Every graph $G$ with $n$ vertices and minimum degree $\delta$ contains a spanning subgraph $H$ satisfying $m(H) \leq \frac{n}{\delta+1} + 2$.

Context

This is the second of the two central conjectures introduced by the authors, generalising Conjecture 1.1 from regular graphs to arbitrary graphs with minimum degree $\delta$. Both conjectures remain open; the paper proves asymptotic relaxations showing the bound $(1+o(1))\frac{n}{\delta+1}+2$ is achievable when $n$ is large.

Notes. Source is PDF extraction; mathematical notation appears clean for this statement.

Source paper

 Irregular Subgraphs
 Noga Alon, Fan Wei · 2021-08-06
 https://arxiv.org/abs/2108.02685
 PDF source

=== Source paper abstract / header ===
Abstract:We suggest two related conjectures dealing with the existence of spanning irregular subgraphs of graphs. The first asserts that any $d$-regular graph on $n$ vertices contains a spanning subgraph in which the number of vertices of each degree between $0$ and $d$ deviates from $\frac{n}{d+1}$ by at most $2$. The second is that every graph on $n$ vertices with minimum degree $\delta$ contains a spanning subgraph in which the number of vertices of each degree does not exceed $\frac{n}{\delta+1}+2$. Both conjectures remain open, but we prove several asymptotic relaxations for graphs with a large number of vertices $n$. In particular we show that if $d^3 \log n \leq o(n)$ then every $d$-regular graph with $n$ vertices contains a spanning subgraph in which the number of vertices of each degree between $0$ and $d$ is $(1+o(1))\frac{n}{d+1}$. We also prove that any graph with $n$ vertices and minimum degree $\delta$ contains a spanning subgraph in which no degree is repeated more than $(1+o(1))\frac{n}{\delta+1}+2$ times.
 

 
 
 
 Comments:
 The conjectures in the v1 was too strong. We updated the conjectures in this v2
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C35, 05C07
 

 Cite as:
 arXiv:2108.02685 [math.CO]
 

 
  
 (or 
 arXiv:2108.02685v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2108.02685
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Fan Wei [view email] 
 [v1]
 Thu, 5 Aug 2021 15:39:01 UTC (19 KB)

 [v2]
 Fri, 6 Aug 2021 14:57:22 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Irregular Subgraphs, by Noga Alon and Fan Wei
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
 | 2021-08
 

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
