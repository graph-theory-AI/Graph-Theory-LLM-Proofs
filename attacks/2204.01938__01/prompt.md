Attack the following open graph-theory problem.

Catalog id: 2204.01938__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2204.01938__01/
Source paper: Extremal results on feedback arc sets in digraphs (arXiv:2204.01938)

=== Catalog page (statement + literature review) ===
Directed surplus in random ℬ-free orientations — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No follow-up resolving Remark 1.6 was found in the published or preprint literature. The conjecture, stated informally as a remark rather than a formal conjecture in the paper, asks whether a random orientation of a B-free graph with m = ex(n, B) edges achieves directed surplus Omega(sqrt(mn)) even when the auxiliary condition ex(n, B) = Theta(n^{2-epsilon(B)}) is dropped; the main paper (published 2024 in Random Structures & Algorithms) proves the bound only under that additional density condition. A 2024 preprint (arXiv:2409.16443) on feedback arc sets in random Erdos-Renyi graphs cites the Fox-Himwich-Mani paper but does not address this specific remark.

 Reviewer notes. Remark 1.6 is not labeled a conjecture in the paper — it is a brief informal remark. The main theorem (Theorem 1.5) proves beta(G) = m/2 - Omega(sqrt(mn)) for B-free orientations under the condition ex(n,B) = Theta(n^{2-epsilon(B)}); Remark 1.6 conjectures the same bound holds without that density condition. No paper specifically targeting this remark was found after five web calls. The paper was published in Random Structures & Algorithms 64.2 (2024), pp. 287-308 (doi available via Wiley).

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. A random orientation of a $\mathcal{B}$-free undirected graph on $n$ vertices with $m = \mathrm{ex}(n, \mathcal{B})$ edges likely satisfies $\beta(G) = m/2 - \Omega(\sqrt{mn})$.

Context

In Remark 1.6 the authors note that the proof of Theorem 1.5 uses the auxiliary condition $\mathrm{ex}(n,\mathcal{B}) = \Theta(n^{2-\varepsilon(\mathcal{B})})$ only for convenience, and that without it a random $\mathcal{B}$-free orientation is suspected to already achieve the stated directed-surplus bound.

Notes. Stated with 'we suspect' in Remark 1.6; no labelled theorem environment. PDF math is readable.

Source paper

 Extremal results on feedback arc sets in digraphs
 Jacob Fox, Zoe Himwich, Nitya Mani · 2022-04-19
 https://arxiv.org/abs/2204.01938
 PDF source

=== Source paper abstract / header ===
Abstract:A directed graph is oriented if it can be obtained by orienting the edges of a simple, undirected graph. For an oriented graph $G$, let $\beta(G)$ denote the size of a minimum feedback arc set, a smallest subset of edges whose deletion leaves an acyclic subgraph. A simple consequence of a result of Berger and Shor is that any oriented graph $G$ with $m$ edges satisfies $\beta(G) = m/2 - \Omega(m^{3/4})$.
We observe that if an oriented graph $G$ has a fixed forbidden subgraph $B$, the upper bound of $\beta(G) = m/2 - \Omega(m^{3/4})$ is best possible as a function of the number of edges if $B$ is not bipartite, but the exponent $3/4$ in the lower order term can be improved if $B$ is bipartite. We also show that for every rational number $r$ between $3/4$ and $1$, there is a finite collection of digraphs $\mathcal{B}$ such that every $\mathcal{B}$-free digraph $G$ with $m$ edges satisfies $\beta(G) = m/2 - \Omega(m^r)$, and this bound is best possible up to the implied constant factor. The proof uses a connection to Turán numbers and a result of Bukh and Conlon. Both of our upper bounds come equipped with randomized linear-time algorithms that construct feedback arc sets achieving those bounds. Finally, we give a characterization of quasirandom directed graphs via minimum feedback arc sets.
 

 
 
 
 Comments:
 23 pages
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05D40
 

 Cite as:
 arXiv:2204.01938 [math.CO]
 

 
  
 (or 
 arXiv:2204.01938v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2204.01938
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Nitya Mani [view email] 
 [v1]
 Tue, 5 Apr 2022 02:20:12 UTC (28 KB)

 [v2]
 Tue, 19 Apr 2022 14:03:49 UTC (24 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Extremal results on feedback arc sets in digraphs, by Jacob Fox and 2 other authors
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
 | 2022-04
 

 Change to browse by:
 
 cs
 cs.DM
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
