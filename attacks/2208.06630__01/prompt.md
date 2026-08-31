Attack the following open graph-theory problem.

Catalog id: 2208.06630__01
Catalog status: open (triage tier 1, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2208.06630__01/
Source paper: Short reachability networks (arXiv:2208.06630)

=== Catalog page (statement + literature review) ===
Minimum lazy transpositions in 2-uniformity networks — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that the minimum number of lazy transpositions in a 2-uniformity network is 2n-3 was posed in arXiv:2208.06630 (published in DMTCS 2025); the authors supply a matching construction and note an analogy with selection networks. No follow-up paper proving or disproving the conjecture was found in a broad web search. The companion paper arXiv:2208.06629 (same authors, same submission date) studies a related but distinct problem—perfect shuffling by lazy transpositions whose composition is uniform—and does not address the 2-uniformity lower bound.

 Reviewer notes. No follow-up found after searching multiple queries. The paper was first posted August 2022 and published in DMTCS in October 2025. The companion paper arXiv:2208.06629 by the same authors concerns a different notion (lazy transpositions composing to a uniform permutation) and does not resolve Conjecture 1. The conjecture appears to remain open.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For $n\geq 2$, the minimum number of lazy transpositions in a 2-uniformity network is $2n-3$.

Context

The authors construct a 2-uniformity network of length $2n-3$ using the sequence $(1,2,\tfrac{1}{2}),(1,3,\tfrac{2}{n}),(1,2,\tfrac{1}{2}),(1,4,\tfrac{2}{n-1}),\dots,(1,2,\tfrac{1}{2}),(1,n,\tfrac{2}{3}),(1,2,\tfrac{1}{2})$, and conjecture this is optimal. They remark that, if true, it would match nicely with selection networks.

Notes. The paper states that after a preliminary version was posted on arXiv, Conjecture 1 was proven (by unspecified authors in the truncated text); it may no longer be open.

Source paper

 Short reachability networks
 Carla Groenland, Tom Johnston, Jamie Radcliffe, Alex Scott · 2025-10-23
 https://arxiv.org/abs/2208.06630

=== Source paper abstract / header ===
Abstract:We investigate the following generalisation of permutation networks. We say a sequence $T=(T_1,\dots,T_\ell)$ of transpositions in $S_n$ forms a $t$-reachability network if, for every choice of $t$ distinct points $x_1, \dots, x_t\in \{1,\dots,n\}$, there is a subsequence of $T$ whose composition maps $j$ to $x_j$ for every $1\leq j\leq t$. When $t=n$, any permutation in $S_n$ can be created and $T$ is a permutation network. Waksman [JACM, 1968] showed that the shortest permutation networks have length about $n \log_2(n)$. In this paper, we investigate the shortest $t$-reachability networks for other values of $t$. Our main result settles the case of $t=2$: the shortest $2$-reachability network has length $\lceil 3n/2\rceil-2 $. For fixed $t \geq 3$, we give a simple randomised construction which shows that there exist $t$-reachability networks with $(2+o_t(1))n$ transpositions. We also study the effect of restricting to star-transpositions, i.e. restricting all transpositions to have the form $(1, \cdot)$.
 

 
 
 
 Comments:
 12 pages, 1 figure
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2208.06630 [math.CO]
 

 
  
 (or 
 arXiv:2208.06630v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2208.06630
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Mathematics & Theoretical Computer Science, vol. 27:3, Combinatorics (November 4, 2025) dmtcs:12454
 

 
 
 Related DOI:
 
 https://doi.org/10.46298/dmtcs.12454

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tom Johnston [view email] 
 [v1]
 Sat, 13 Aug 2022 11:25:54 UTC (13 KB)

 [v2]
 Thu, 19 Oct 2023 15:07:43 UTC (14 KB)

 [v3]
 Thu, 23 Oct 2025 17:22:21 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Short reachability networks, by Carla Groenland and 3 other authors
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
 | 2022-08
 

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
