Attack the following open graph-theory problem.

Catalog id: 2508.14332__00
Catalog status: partial (triage tier 4, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2508.14332__00/
Source paper: Asymptotic structure. IV. A counterexample to the weak coarse Menger co… (arXiv:2508.14332)

=== Extracted statement (catalog JSON) ===
Title: Open case: Coarse Menger Conjecture for c=2
It is unknown whether Conjecture 1.1 holds when $c = 2$: for all integers $k \geq 1$ there exists $\ell > 0$ such that for every graph $G$ and $S, T \subseteq V(G)$, either there are $k$ paths between $S, T$ pairwise at distance at least $2$, or there is a set $X \subseteq V(G)$ with $|X| \leq k-1$ such that every $S$-$T$ path contains a vertex within distance $\ell$ of some member of $X$.

Context:
The authors note that the case $c = 3$ is of special interest because a positive result for $c = 3$ would imply one for all $c \geq 3$ (via taking the $c$-th power of $G$). They explicitly remark that 'the conjecture remains open when $c = 2$, and we have nothing to say about that case in this paper.'

=== Catalog page (statement + literature review) ===
Coarse Menger separation with distance 2 — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The Coarse Menger Conjecture for c=2 was explicitly left open in the source paper, which disproves the weak coarse Menger conjecture for c≥3. Subsequent work (arXiv:2509.08762) proves the coarse Menger conjecture for all graphs of bounded path-width, giving a partial positive result that applies to c=2 in that restricted class. A further paper (arXiv:2605.11112) establishes a coarse Menger theorem for planar and bounded-genus graphs. The c=2 case for general graphs remains open.

 Cited literature (2)

 
 
 
partial Asymptotic structure. V. The coarse Menger conjecture in bounded path-width
 (2025)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2509.08762

Proves the coarse Menger conjecture for all graphs of bounded path-width (across all values of c), providing a partial positive result for the c=2 open case in this restricted graph class.
 

 
 
partial A coarse Menger's Theorem for planar and bounded genus graphs
 (2026)
 

 
 unconfirmed · arXiv preprint · arXiv:2605.11112

Proves a coarse version of Menger's theorem for planar and bounded-genus graphs, giving partial progress on the coarse Menger conjecture (including the c=2 case) for those surface-embeddable graph families.
 

 

 Reviewer notes. The c=2 case of the Coarse Menger Conjecture remains open for general graphs. The source paper's main contribution is a counterexample for c≥3. Partial results exist for bounded path-width (arXiv:2509.08762) and planar/bounded-genus graphs (arXiv:2605.11112). The internal reference arXiv:2412.13893 is a false match and does not concern this conjecture.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Informal. It is unknown whether Conjecture 1.1 holds when $c = 2$: for all integers $k \geq 1$ there exists $\ell > 0$ such that for every graph $G$ and $S, T \subseteq V(G)$, either there are $k$ paths between $S, T$ pairwise at distance at least $2$, or there is a set $X \subseteq V(G)$ with $|X| \leq k-1$ such that every $S$-$T$ path contains a vertex within distance $\ell$ of some member of $X$.

Context

The authors note that the case $c = 3$ is of special interest because a positive result for $c = 3$ would imply one for all $c \geq 3$ (via taking the $c$-th power of $G$). They explicitly remark that 'the conjecture remains open when $c = 2$, and we have nothing to say about that case in this paper.'

Notes. Stated as a passing remark in the introduction; no formal conjecture label. Refers specifically to the strong-form Conjecture 1.1 restricted to c=2.

Source paper

 Asymptotic structure. IV. A counterexample to the weak coarse Menger conjecture
 Tung Nguyen, Alex Scott, Paul Seymour · 2025-08-20
 https://arxiv.org/abs/2508.14332

=== Source paper abstract / header ===
Abstract:Coarse graph theory concerns finding 'coarse' analogues of graph theory theorems, replacing disjointness with being far apart. One of the most interesting open questions is to find a coarse analogue of Menger's theorem, which characterizes when there are $k$ vertex-disjoint paths between two given sets $S,T$ of vertices of a graph. We showed in an earlier paper that the most natural such analogue is false, but a weaker statement remained as a popular open question. Here we show that the weaker statement is also false.
More exactly, suppose that $S,T$ are sets of vertices of a graph $G$, and there do not exist $k$ paths between $S,T$, pairwise at distance at least $c$. To make an analogue of Menger's theorem, one would like to prove that there must be a small set $X\subseteq V(G)$ such that every $S-T$ path of $G$ passes close to a member of $X$: but how small and how close? In view of Menger's theorem, one would hope for $|X|<k$ and 'close' some function of $k,c$ (and indeed, this was conjectured by Georgakopoulos and Papasoglu, and independently, by Albrechtsen, Huynh, Jacobs, Knappe and Wollan); but we showed that this is false, even if $c=3$ and $k=3$.
Here we upgrade the counterexample: we show that, even if $c=k=3$, no pair of constants (for 'small' and 'close') work. For all $\ell, m$, there is a graph $G$ and $S,T\subseteq V(G)$, such that there do not exist three $S-T$ paths pairwise with distance at least three, and yet there is no $X$ with $|X|\le m$ such that every $S-T$ path passes within distance at most $\ell$ of $X$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2508.14332 [math.CO]
 

 
  
 (or 
 arXiv:2508.14332v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2508.14332
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alex Scott [view email] 
 [v1]
 Wed, 20 Aug 2025 01:04:11 UTC (12 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Asymptotic structure. IV. A counterexample to the weak coarse Menger conjecture, by Tung Nguyen and 2 other authors
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
 | 2025-08
 

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
