Attack the following open graph-theory problem.

Catalog id: 2206.10733__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2206.10733__00/
Source paper: Improved bounds for the triangle case of Aharoni's rainbow generalizati… (arXiv:2206.10733)

=== Catalog page (statement + literature review) ===
Happy triples extremal bound for l < k/2 — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 Caccetta-Häggkvist Conjecture
 (fuzzy-match score 100, not yet manually confirmed).

 
 Status
 open
 high confidence
 

 The open problem asks for the best upper bound on the number of happy triples in a graph with $k$ edges and maximum degree at most $l$ in the regime $l < k/2$. Lemma 2 of arXiv:2206.10733 settles the $l \geq k/2$ case with tight extremal graphs, but the authors explicitly note that their dynamic-programming approach gives no insight into the $l < k/2$ regime. A wide web search found no follow-up work addressing this specific open problem.

 Reviewer notes. No follow-up found after 5 web calls. The term 'happy triples' appears to be internal to arXiv:2206.10733 and has not been adopted in subsequent literature indexed by web search. The $l < k/2$ regime remains open as of May 2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It would be interesting to consider the best upper bound on the number of happy triples in a graph with $k$ edges and maximum degree at most $l$, for the regime when $l < k/2$.

Context

Lemma 2 establishes a tight bound on happy triples when $l \geq k/2$, achieved by specific extremal graphs. The authors note that their algorithmic/dynamic-programming approach gives little insight into the $l < k/2$ regime; for example, for $l=3$ and $k=3t$ the extremal graph output is $K_{t,3}$, which does not actually have maximum degree 3 for $t \geq 4$.

Notes. Stated informally in the text as 'It would be interesting to consider…'; PDF source — math may be garbled.

Source paper

 Improved bounds for the triangle case of Aharoni's rainbow generalization of the Caccetta-Häggkvist conjecture
 Patrick Hompe, Zishen Qu, Sophie Spirkl · 2023-09-11
 https://arxiv.org/abs/2206.10733
 PDF source

=== Source paper abstract / header ===
Abstract:For a digraph $G$ and $v \in V(G)$, let $\delta^+(v)$ be the number of out-neighbors of $v$ in $G$. The Caccetta-Häggkvist conjecture states that for all $k \ge 1$, if $G$ is a digraph with $n = |V(G)|$ such that $\delta^+(v) \ge k$ for all $v \in V(G)$, then $G$ contains a directed cycle of length at most $\lceil n/k \rceil$. Aharoni proposed a generalization of this conjecture, that a simple edge-colored graph on $n$ vertices with $n$ color classes, each of size at least $k$, has a rainbow cycle of length at most $\lceil n/k \rceil$. Let us call $(\alpha, \beta)$ \emph{triangular} if every simple edge-colored graph on $n$ vertices with at least $\alpha n$ color classes, each with at least $\beta n$ edges, has a rainbow triangle. Aharoni, Holzman, and DeVos showed the following: $(9/8,1/3)$ is triangular; $(1,2/5)$ is triangular. In this paper, we improve those bounds, showing the following: $(1.1077,1/3)$ is triangular; $(1,0.3988)$ is triangular. Our methods give results for infinitely many pairs $(\alpha, \beta)$, including $\beta < 1/3$; we show that $(1.3481,1/4)$ is triangular.
 

 
 
 
 Comments:
 Accepted manuscript; see DOI for journal version
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2206.10733 [math.CO]
 

 
  
 (or 
 arXiv:2206.10733v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2206.10733
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Mathematics, Volume 347, Issue 1, January 2024, 113691
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.disc.2023.113691

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sophie Spirkl [view email] 
 [v1]
 Tue, 21 Jun 2022 21:15:37 UTC (8 KB)

 [v2]
 Tue, 5 Jul 2022 18:22:43 UTC (18 KB)

 [v3]
 Mon, 11 Sep 2023 14:13:44 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Improved bounds for the triangle case of Aharoni's rainbow generalization of the Caccetta-H\"{a}ggkvist conjecture, by Patrick Hompe and 2 other authors
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
 | 2022-06
 

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
