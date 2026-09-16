Attack the following open graph-theory problem.

Catalog id: 2110.09403__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2110.09403__00/
Source paper: Improved lower bound for the list chromatic number of graphs with no $K… (arXiv:2110.09403)

=== Extracted statement (catalog JSON) ===
Title: Problem 1
Does every $K_t$-minor-free graph $G$ satisfy $\chi_\ell(G) \leq 2t$?

Context:
Having established the lower bound $(2-o(1))t$ for the maximum list chromatic number of $K_t$-minor free graphs, the author asks whether the probabilistic lower-bound construction is essentially optimal up to lower-order terms, or whether the lower bound can be further improved beyond $2t$.

=== Catalog page (statement + literature review) ===
χ_ℓ ≤ 2t for K_t-minor-free graphs — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 List Hadwiger Conjecture
 (fuzzy-match score 76).

 
 Status
 open
 high confidence
 

 The conjecture asks whether the list chromatic number of every $K_t$-minor-free graph is at most $2t$. The source paper itself established the lower bound $(2-o(1))t$, showing that if the conjecture holds the bound $2t$ would be essentially tight. As of 2026, the best known upper bound for $\chi_\ell$ of $K_t$-minor-free graphs remains superlinear in $t$ (of the form $O(t(\log\log t)^6)$), leaving a gap. A follow-up by Fischer and Steiner (2023) generalises the lower bound to all $H$-minor-free graphs but does not resolve the upper bound question.

 Cited literature (1)

 
 
 
partial On the choosability of $H$-minor-free graphs
 (2023)
 

 
 Olivier Fischer, Raphael Steiner · Combinatorics, Probability & Computing · arXiv:2304.04246

Generalises the $(2-o(1))t$ lower bound from $K_t$-minor-free graphs to all $H$-minor-free graphs (showing $f_\ell(H) \ge (1-\varepsilon)(v(H)+\kappa(H))$ for large $H$), strengthening the source paper's result but not establishing the conjectured upper bound $2t$.
 

 

 Reviewer notes. The current best upper bound for the list chromatic number of $K_t$-minor-free graphs is $O(t(\log\log t)^6)$, far above the conjectured $2t$. The conjecture is open with high confidence: the source paper is from 2021, a broad web search and Steiner's own research page confirm no proof of the $2t$ upper bound has appeared. The Fischer–Steiner follow-up (arXiv:2304.04246) only improves the lower-bound side.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Does every $K_t$-minor-free graph $G$ satisfy $\chi_\ell(G) \leq 2t$?

Context

Having established the lower bound $(2-o(1))t$ for the maximum list chromatic number of $K_t$-minor free graphs, the author asks whether the probabilistic lower-bound construction is essentially optimal up to lower-order terms, or whether the lower bound can be further improved beyond $2t$.

Source paper

 Improved lower bound for the list chromatic number of graphs with no $K_t$ minor
 Raphael Steiner · 2021-10-18
 https://arxiv.org/abs/2110.09403
 PDF source

=== Source paper abstract / header ===
Abstract:Hadwiger's conjecture asserts that every graph without a $K_t$-minor is $(t-1)$-colorable. It is known that the exact version of Hadwiger's conjecture does not extend to list coloring, but it has been conjectured by Kawarabayashi and Mohar (2007) that there exists a constant $c$ such that every graph with no $K_t$-minor has list chromatic number at most $ct$. More specifically, they also conjectured that this holds for $c=\frac{3}{2}$.
Refuting the latter conjecture, we show that the maximum list chromatic number of graphs with no $K_t$-minor is at least $(2-o(1))t$, and hence $c \ge 2$ in the above conjecture is necessary. This improves the previous best lower bound by Barát, Joret and Wood (2011), who proved that $c \ge \frac{4}{3}$. Our lower-bound examples are obtained via the probabilistic method.
 

 
 
 
 Comments:
 6 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15, 05C83
 

 Cite as:
 arXiv:2110.09403 [math.CO]
 

 
  
 (or 
 arXiv:2110.09403v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2110.09403
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Mon, 18 Oct 2021 15:33:12 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Improved lower bound for the list chromatic number of graphs with no $K_t$ minor, by Raphael Steiner
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
 | 2021-10
 

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
