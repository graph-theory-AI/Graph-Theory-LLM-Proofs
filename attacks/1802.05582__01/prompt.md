Attack the following open graph-theory problem.

Catalog id: 1802.05582__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1802.05582__01/
Source paper: Distributed coloring in sparse graphs with fewer colors (arXiv:1802.05582)

=== Extracted statement (catalog JSON) ===
Title: Question on randomized list-coloring round complexity
Is it possible to avoid the multiplicative factor polynomial in $\Delta$ in a randomized version of the distributed $\Delta$-list-coloring algorithm (Corollary 2.1)?

Context:
Panconesi and Srinivasan gave a randomized $\Delta$-coloring algorithm running in $O(\log^3 n / \log \Delta)$ rounds. The paper's list-coloring extension (Corollary 2.1) achieves $O(\Delta^2 \log^3 n)$ rounds deterministically, but it is noted to be unclear whether a randomized variant can similarly remove the polynomial dependence on $\Delta$.

=== Catalog page (statement + literature review) ===
Randomized round complexity of Δ-list-coloring — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The question asks whether a randomized distributed algorithm for Delta-list-coloring can achieve round complexity without a polynomial factor in Delta, analogously to the O(log^3 n / log Delta)-round randomized algorithm of Panconesi and Srinivasan for Delta-coloring. Subsequent work has made substantial progress on randomized Delta-coloring (Ghaffari et al. 2018 reduced to O(log Delta) + 2^{O(sqrt{log log n})} rounds; a 2025 preprint further improved deterministic bounds), and a 2024 paper achieves poly-log log n rounds for Delta-coloring in CONGEST, but none of these works specifically address Delta-list-coloring (with exactly Delta colors per vertex from individual lists). The question, which concerns a strictly harder list variant, appears to remain open as of 2026.

 Reviewer notes. Web searches found significant follow-up on randomized distributed Delta-coloring (not list-coloring): Ghaffari-Hirvonen 2018 (arXiv:1803.03248) achieves O(log Delta) + 2^{O(sqrt{log log n})} rounds for Delta-coloring; arXiv:2504.03080 (2025) improves deterministic bounds further; arXiv:2405.09975 (2024) achieves poly-log-log n randomized rounds for Delta-coloring in CONGEST. None of these papers address the specific question about Delta-LIST-coloring (Corollary 2.1 of the source paper). The distinction matters: standard Delta-coloring exploits graph structure globally, while Delta-list-coloring with arbitrary per-vertex palettes of size exactly Delta is strictly harder and different techniques apply. No resolution of this specific open question was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it possible to avoid the multiplicative factor polynomial in $\Delta$ in a randomized version of the distributed $\Delta$-list-coloring algorithm (Corollary 2.1)?

Context

Panconesi and Srinivasan gave a randomized $\Delta$-coloring algorithm running in $O(\log^3 n / \log \Delta)$ rounds. The paper's list-coloring extension (Corollary 2.1) achieves $O(\Delta^2 \log^3 n)$ rounds deterministically, but it is noted to be unclear whether a randomized variant can similarly remove the polynomial dependence on $\Delta$.

Notes. Implicit question in prose: "it is not clear whether we can similarly avoid the multiplicative factor polynomial in $\Delta$ in a randomized version of our algorithm"; PDF source.

Source paper

 Distributed coloring in sparse graphs with fewer colors
 Pierre Aboulker, Marthe Bonamy, Nicolas Bousquet, Louis Esperet · 2018-12-19
 https://arxiv.org/abs/1802.05582
 PDF source

=== Source paper abstract / header ===
Abstract:This paper is concerned with efficiently coloring sparse graphs in the distributed setting with as few colors as possible. According to the celebrated Four Color Theorem, planar graphs can be colored with at most 4 colors, and the proof gives a (sequential) quadratic algorithm finding such a coloring. A natural problem is to improve this complexity in the distributed setting. Using the fact that planar graphs contain linearly many vertices of degree at most 6, Goldberg, Plotkin, and Shannon obtained a deterministic distributed algorithm coloring $n$-vertex planar graphs with 7 colors in $O(\log n)$ rounds. Here, we show how to color planar graphs with 6 colors in $\mbox{polylog}(n)$ rounds. Our algorithm indeed works more generally in the list-coloring setting and for sparse graphs (for such graphs we improve by at least one the number of colors resulting from an efficient algorithm of Barenboim and Elkin, at the expense of a slightly worst complexity). Our bounds on the number of colors turn out to be quite sharp in general. Among other results, we show that no distributed algorithm can color every $n$-vertex planar graph with 4 colors in $o(n)$ rounds.
 

 
 
 
 Comments:
 16 pages, 4 figures - An extended abstract of this work was presented at PODC'18 (ACM Symposium on Principles of Distributed Computing)
 

 Subjects:
 
 Combinatorics (math.CO); Distributed, Parallel, and Cluster Computing (cs.DC); Data Structures and Algorithms (cs.DS)
 

 Cite as:
 arXiv:1802.05582 [math.CO]
 

 
  
 (or 
 arXiv:1802.05582v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1802.05582
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Electronic Journal of Combinatorics 26(4) (2019), P4.20
 

 

 

 
 Submission history
 From: Louis Esperet [view email] 
 [v1]
 Thu, 15 Feb 2018 14:49:19 UTC (94 KB)

 [v2]
 Fri, 11 May 2018 08:38:31 UTC (95 KB)

 [v3]
 Fri, 7 Sep 2018 10:46:05 UTC (95 KB)

 [v4]
 Wed, 19 Dec 2018 11:57:13 UTC (96 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Distributed coloring in sparse graphs with fewer colors, by Pierre Aboulker and 3 other authors
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
 | 2018-02
 

 Change to browse by:
 
 cs
 cs.DC
 cs.DS
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 
 
 1 blog link
 (what is this?)
 

 

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
