Attack the following open graph-theory problem.

Catalog id: 2009.13319__02
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2009.13319__02/
Source paper: Extension of Gyarfas-Sumner conjecture to digraphs (arXiv:2009.13319)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 4.4
Given an oriented forest $F$ and for every integer $k$, $\{\overleftrightarrow{K_2}, K_k, F\}$ is heroic.

Context:
This conjecture is equivalent to the special case of Conjecture 4.2 where $H = TT_k$ is a transitive tournament, since every tournament on at least $2k$ vertices contains $TT_k$ as an induced subdigraph. It generalises the heroic-set result for $\{\overleftrightarrow{K_2}, K_k, P^+(3)\}$ proved in Theorem 4.3, where $K_k$ denotes the digraph on $k$ vertices with no arc.

=== Catalog page (statement + literature review) ===
Heroic triple with oriented forest and K_k — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Conjecture 4.4 — that $\{\overleftrightarrow{K_2}, K_k, F\}$ is heroic for every oriented forest $F$ and every integer $k$ — remains open in full generality. Two follow-up papers from the curated corpus establish special cases: arXiv:2103.07886 handles $F = S_2^+$ (oriented star with two out-edges) and arXiv:2212.02272 handles $F = \overrightarrow{P}_6$ with the clique constraint $\omega \le 2$ (triangle-free). A separate paper (arXiv:2202.13306) is noted to disprove a conjecture of Aboulker, Charbit, and Naserasr in the context of heroes in oriented complete multipartite graphs, but its abstract does not specify which conjecture from the source paper, so it is not attributed to Conjecture 4.4 here.

 Cited literature (2)

 
 
 
partial Decomposing and colouring some locally semicomplete digraphs
 (2022)
 

 
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit · arXiv preprint · arXiv:2103.07886

Proves the conjecture for the special case $F = S_2^+$: every locally out-transitive oriented graph has dichromatic number at most 2 (Theorem 3.2), which corresponds to $\{\overleftrightarrow{K_2}, K_k, S_2^+\}$ being heroic.
 

 
 
partial (P6, triangle)-free digraphs have bounded dichromatic number
 (2023)
 

 
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit, Stéphan Thomassé · arXiv preprint · arXiv:2212.02272

Proves the conjecture for the special case $F = \overrightarrow{P}_6$ with $k = 3$ (triangle-free digraphs): every $\overrightarrow{P}_6$-free digraph with $\omega(D) \le 2$ has dichromatic number at most 382 (Theorem 1.3).
 

 

 Reviewer notes. arXiv:2202.13306 ('Heroes in oriented complete multipartite graphs', Aboulker et al., 2022) was found in search results and its abstract states it disproves a conjecture of Aboulker, Charbit, and Naserasr; however, the abstract specifies the result is about heroes in oriented complete multipartite graphs — likely a different structural conjecture from the same source paper — and the abstract does not name Conjecture 4.4 specifically. It is therefore excluded from since_posted pending full-text verification. The Electronic Journal of Combinatorics paper 'Proving a Directed Analogue of the Gyárfás-Sumner Conjecture for Orientations of P4' appeared in search results and may constitute additional partial progress (F = oriented P4), but could not be verified within the 5-call budget.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Given an oriented forest $F$ and for every integer $k$, $\{\overleftrightarrow{K_2}, K_k, F\}$ is heroic.

Context

This conjecture is equivalent to the special case of Conjecture 4.2 where $H = TT_k$ is a transitive tournament, since every tournament on at least $2k$ vertices contains $TT_k$ as an induced subdigraph. It generalises the heroic-set result for $\{\overleftrightarrow{K_2}, K_k, P^+(3)\}$ proved in Theorem 4.3, where $K_k$ denotes the digraph on $k$ vertices with no arc.

Notes. PDF source — the raw text reads 'for every integer l' but uses $K_k$ in the set; the variable $l$ is likely a PDF extraction artifact for $k$. Here $K_k$ denotes the independent set (edgeless digraph) on $k$ vertices, as per the paper's notation.

Source paper

 Extension of Gyarfas-Sumner conjecture to digraphs
 Pierre Aboulker, Pierre Charbit, Reza Naserasr · 2020-09-28
 https://arxiv.org/abs/2009.13319
 PDF source

Related conjectures

 
 implied by
 Heroic triple characterization via transitive tournaments
 partial
 Instantiate the full characterization (Conjecture 4.2) with H = TT_k: TT_k is itself a transitive tournament, so the second disjunct of the 'if' condition holds trivially and the instance reduces to '{digon, TT_k, F} is heroic for every oriented forest F and every k'. The paper explicitly states (in the target's own context) that this special case is equivalent to the target conjecture about {digon, K_k, F}, via the Ramsey fact that every tournament on 2^k vertices contains TT_k, which makes forbidding the edgeless K_k interchangeable with forbidding TT_k in digon-free digraphs. Full conjecture implies its instance implies the target; direction as claimed (source is the general characterization, target a special case).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:The dichromatic number of a digraph $D$ is the minimum number of colors needed to color its vertices in such a way that each color class induces an acyclic digraph. As it generalizes the notion of the chromatic number of graphs, it has been a recent center of study. In this work we look at possible extensions of Gyárfás-Sumner conjecture. More precisely, we propose as a conjecture a simple characterization of finite sets $\mathcal F$ of digraphs such that every oriented graph with sufficiently large dichromatic number must contain a member of $\mathcal F$ as an induce subdigraph.
Among notable results, we prove that oriented triangle-free graphs without a directed path of length $3$ are $2$-colorable. If condition of "triangle-free" is replaced with "$K_4$-free", then we have an upper bound of $414$. We also show that an orientation of complete multipartite graph with no directed triangle is 2-colorable. To prove these results we introduce the notion of \emph{nice sets} that might be of independent interest.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2009.13319 [math.CO]
 

 
  
 (or 
 arXiv:2009.13319v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2009.13319
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Pierre Aboulker [view email] 
 [v1]
 Mon, 28 Sep 2020 13:41:38 UTC (41 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Extension of Gyarfas-Sumner conjecture to digraphs, by Pierre Aboulker and 2 other authors
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
 | 2020-09
 

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
