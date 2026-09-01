Attack the following open graph-theory problem.

Catalog id: 2107.05995__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2107.05995__00/
Source paper: On the Hat Guessing Number of Graphs (arXiv:2107.05995)

=== Extracted statement (catalog JSON) ===
Title: Informal Belief on Degeneracy Bound for Hat Guessing Number
It seems plausible that there exists a function $f : \mathbb{N} \to \mathbb{N}$ such that for every $d$-degenerate graph $G$, $\mathrm{HG}(G) \leq f(d)$.

Context:
The authors remark in the open problems section that such a bounding function seems plausible, noting that it would imply absolute constant bounds on the hat guessing number of planar graphs (which are $5$-degenerate) and a Hadwiger-number bound via degeneracy results.

=== Catalog page (statement + literature review) ===
Hat guessing number bounded by degeneracy — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that there exists f : N → N with HG(G) ≤ f(d) for every d-degenerate graph G remains open. The closest follow-up (arXiv:2112.09619, SIAM JDM 2023) introduces a stronger graph parameter called strong degeneracy and proves HG(G) is bounded above by a function of strong degeneracy—notably reducing the upper bound for outerplanar graphs from ~2^125000 down to 40—but explicitly leaves the question for standard degeneracy open. Prior work (arXiv:2003.04990, E-JC 2020, predating this paper) established doubly-exponential lower bounds HG(G) ≥ 2^(2^(d-1)) for d-degenerate graphs, but this does not preclude a bounding function existing.

 Cited literature (1)

 
 
 
partial Hat guessing numbers of strongly degenerate graphs
 (2023)
 

 
 see arXiv:2112.09619 · SIAM Journal on Discrete Mathematics · arXiv:2112.09619 · doi:10.1137/22M1479154

Proves HG(G) is bounded above by a function of strong degeneracy (a parameter stronger than degeneracy), reducing the outerplanar upper bound to 40, but explicitly leaves open whether HG(G) is bounded by a function of standard degeneracy.
 

 

 Reviewer notes. The conjecture is explicitly discussed as open in arXiv:2112.09619. The doubly-exponential lower bounds from arXiv:2003.04990 (E-JC 2020) predate the source paper. A separate line of work (arXiv:2301.10305) shows the hat guessing number of some planar graph is at least 22, meaning f(5) ≥ 22 if the conjecture holds, but this does not resolve the conjecture. No resolution found in 2022–2026 literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It seems plausible that there exists a function $f : \mathbb{N} \to \mathbb{N}$ such that for every $d$-degenerate graph $G$, $\mathrm{HG}(G) \leq f(d)$.

Context

The authors remark in the open problems section that such a bounding function seems plausible, noting that it would imply absolute constant bounds on the hat guessing number of planar graphs (which are $5$-degenerate) and a Hadwiger-number bound via degeneracy results.

Source paper

 On the Hat Guessing Number of Graphs
 Noga Alon, Jeremy Chizewer · 2021-07-21
 https://arxiv.org/abs/2107.05995
 PDF source

=== Source paper abstract / header ===
Abstract:The hat guessing number $HG(G)$ of a graph $G$ on $n$ vertices is defined in terms of the following game: $n$ players are placed on the $n$ vertices of $G$, each wearing a hat whose color is arbitrarily chosen from a set of $q$ possible colors. Each player can see the hat colors of his neighbors, but not his own hat color. All of the players are asked to guess their own hat colors simultaneously, according to a predetermined guessing strategy and the hat colors they see, where no communication between them is allowed. The hat guessing number $HG(G)$ is the largest integer $q$ such that there exists a guessing strategy guaranteeing at least one correct guess for any hat assignment of $q$ possible colors.
In this note we construct a planar graph $G$ satisfying $HG(G)=12$, settling a problem raised in \cite{BDFGM}. We also improve the known lower bound of $(2-o(1))\log_2 n$ for the typical hat guessing number of the random graph $G=G(n,1/2)$, showing that it is at least $n^{1-o(1)}$ with probability tending to $1$ as $n$ tends to infinity. Finally, we consider the linear hat guessing number of complete multipartite graphs.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C57
 

 Cite as:
 arXiv:2107.05995 [math.CO]
 

 
  
 (or 
 arXiv:2107.05995v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2107.05995
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Jeremy Chizewer [view email] 
 [v1]
 Tue, 13 Jul 2021 11:24:14 UTC (9 KB)

 [v2]
 Wed, 21 Jul 2021 17:28:03 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the Hat Guessing Number of Graphs, by Noga Alon and Jeremy Chizewer
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
 | 2021-07
 

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
