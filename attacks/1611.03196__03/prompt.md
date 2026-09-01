Attack the following open graph-theory problem.

Catalog id: 1611.03196__03
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1611.03196__03/
Source paper: Fair representation by independent sets (arXiv:1611.03196)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.15
For every $m$ there exists a number $c(m)$ for which the following is true: if $G$ is a bipartite graph and $E_1, \ldots, E_m$ are any sets of edges, then there exists a matching $S$ in $G$ of size at least $\frac{|E(G)|}{\Delta(G)} - c(m)$ such that $|S \cap E_i| \leq \left\lceil \frac{|E_i|}{\Delta(G)} \right\rceil$ for all $i \leq m$.

Context:
An under-representation formulation of the fair representation theme, motivated by the observation that over-representation fails when the sets do not form a partition. The authors suggest $c(m) = m/2$ may suffice. When the $E_i$ form a partition, condition (2) implies all but $c(m)$ sets are fairly represented.

=== Catalog page (statement + literature review) ===
Fair representation matching in bipartite graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 1.15 from arXiv:1611.03196 asks for an additive constant c(m) guaranteeing that any bipartite graph G with m edge-sets E_1,...,E_m admits a large matching (of size at least |E(G)|/Delta(G) - c(m)) in which no E_i is over-represented beyond the ceiling of |E_i|/Delta(G). No verified resolution of this conjecture was found in the literature after an exhaustive web search. The conjecture is from 2016 and appears to remain open as of May 2026.

 Reviewer notes. No verified follow-up paper addressing Conjecture 1.15 was found after 5 web calls. A ScienceDirect paper titled 'Almost fair perfect matchings in complete bipartite graphs' appeared in search results but returned HTTP 403 and could not be verified; it is not included in since_posted. The internal reference arXiv:2212.11969 is a false positive from the corpus fuzzy-matching step. Confidence is medium rather than high because the conjecture is approximately 9 years old, making the absence of indexed follow-up somewhat less conclusive.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every $m$ there exists a number $c(m)$ for which the following is true: if $G$ is a bipartite graph and $E_1, \ldots, E_m$ are any sets of edges, then there exists a matching $S$ in $G$ of size at least $\frac{|E(G)|}{\Delta(G)} - c(m)$ such that $|S \cap E_i| \leq \left\lceil \frac{|E_i|}{\Delta(G)} \right\rceil$ for all $i \leq m$.

Context

An under-representation formulation of the fair representation theme, motivated by the observation that over-representation fails when the sets do not form a partition. The authors suggest $c(m) = m/2$ may suffice. When the $E_i$ form a partition, condition (2) implies all but $c(m)$ sets are fairly represented.

Notes. PDF source — ceiling bracket symbols garbled as (cid:100)(cid:101); LaTeX reconstructed from context.

Source paper

 Fair representation by independent sets
 Ron Aharoni, Noga Alon, Eli Berger, Maria Chudnovsky, Dani Kotlar, Martin Loebl, Ran Ziv · 2016-11-10
 https://arxiv.org/abs/1611.03196
 PDF source

=== Source paper abstract / header ===
Abstract:For a hypergraph $H$ let $\beta(H)$ denote the minimal number of edges from $H$ covering $V(H)$. An edge $S$ of $H$ is said to represent {\em fairly} (resp. {\em almost fairly}) a partition $(V_1,V_2, \ldots, V_m)$ of $V(H)$ if $|S\cap V_i|\ge \lfloor\frac{|V_i|}{\beta(H)}\rfloor$ (resp. $|S\cap V_i|\ge \lfloor\frac{|V_i|}{\beta(H)}\rfloor-1$) for all $i \le m$.
In matroids any partition of $V(H)$ can be represented fairly by some independent set. We look for classes of hypergraphs $H$ in which any partition of $V(H)$ can be represented almost fairly by some edge.
We show that this is true when $H$ is the set of independent sets in a path, and conjecture that it is true when $H$ is the set of matchings in $K_{n,n}$. We prove that partitions of $E(K_{n,n})$ into three sets can be represented almost fairly. The methods of proofs are topological.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1611.03196 [math.CO]
 

 
  
 (or 
 arXiv:1611.03196v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1611.03196
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Kotlar [view email] 
 [v1]
 Thu, 10 Nov 2016 06:31:33 UTC (276 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Fair representation by independent sets, by Ron Aharoni and 6 other authors
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
 | 2016-11
 

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
