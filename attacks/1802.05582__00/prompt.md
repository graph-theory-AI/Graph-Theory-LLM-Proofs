Attack the following open graph-theory problem.

Catalog id: 1802.05582__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1802.05582__00/
Source paper: Distributed coloring in sparse graphs with fewer colors (arXiv:1802.05582)

=== Extracted statement (catalog JSON) ===
Title: Open problem on sublinear round complexity
It remains interesting to obtain a bound on the round complexity that is sublinear in $n$ regardless of the value of $d$.

Context:
After noting that network decompositions can replace the $O(d^4 \log^3 n)$ round complexity of Theorem 1.3 by $d^3 2^{O(\sqrt{\log n})}$, the authors remark that these alternative bounds are unsatisfying. The problem of achieving a round complexity that is sublinear in $n$ independent of $d$ remains open.

=== Catalog page (statement + literature review) ===
Sublinear round complexity for distributed coloring — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The open problem asks for a distributed algorithm coloring $d$-degenerate graphs with $(1+\varepsilon)d$ colors in a number of rounds that is sublinear in $n$ for every fixed $d$, without the round bound growing with $d$. The source paper achieves $O(d^4\log^3 n)$ rounds, improvable to $d^3 \cdot 2^{O(\sqrt{\log n})}$ via the Panconesi--Srinivasan network decomposition. The 2020 breakthrough of Rozhoň and Ghaffari (STOC 2020) provides a poly$(\log n)$-time deterministic network decomposition and resolves the $2^{O(\sqrt{\log n})}$ factor, but the resulting bound on $d$-degenerate coloring still carries a $d$-dependent multiplicative factor, leaving the requirement of independence from $d$ unmet. No paper directly resolving the conjecture was found in the indexed literature.

 Reviewer notes. The conjecture is closely related to the Rozhoň--Ghaffari (STOC 2020) polylogarithmic network decomposition breakthrough (arXiv:1907.05254, STOC proceedings DOI 10.1145/3357713.3384298), which eliminates $2^{O(\sqrt{\log n})}$ factors for many distributed problems. However, for this specific problem the resulting algorithms still carry a polynomial dependence on $d$, so the full requirement of being sublinear in $n$ independently of $d$ remains unresolved. A PODC 2024 paper on adaptive MPC coloring in sparse graphs also appeared in search results but could not be fetched (HTTP 403). No verified citation resolving the conjecture was found after 5 web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. It remains interesting to obtain a bound on the round complexity that is sublinear in $n$ regardless of the value of $d$.

Context

After noting that network decompositions can replace the $O(d^4 \log^3 n)$ round complexity of Theorem 1.3 by $d^3 2^{O(\sqrt{\log n})}$, the authors remark that these alternative bounds are unsatisfying. The problem of achieving a round complexity that is sublinear in $n$ independent of $d$ remains open.

Notes. Stated as an open direction in prose, no labelled environment; PDF source.

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
