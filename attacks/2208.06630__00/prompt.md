Attack the following open graph-theory problem.

Catalog id: 2208.06630__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2208.06630__00/
Source paper: Short reachability networks (arXiv:2208.06630)

=== Catalog page (statement + literature review) ===
Minimum transpositions in t-reachable networks — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 1 from arXiv:2208.06630 asks for the minimum number of transpositions in a t-reachable network, including the special case of star transpositions of the form (1,·). The paper (published in DMTCS, November 2025) settles the t=2 case exactly and gives an upper bound of (2+o_t(1))n transpositions for fixed t>=3, but the true asymptotics for large t remain open; a gap between upper and lower bounds also persists in the star-transposition setting. No follow-up paper resolving either variant was found in the indexed literature.

 Reviewer notes. The paper appeared in Discrete Mathematics & Theoretical Computer Science, vol. 27:3, Combinatorics (DOI: 10.46298/dmtcs.12454), published 4 November 2025. A companion manuscript 'Perfect shuffling with fewer lazy transpositions' by Groenland and Johnston is hosted on Alex Scott's webpage but its arXiv preprint status and exact bearing on Problem 1 could not be confirmed within the 5-call budget. The sole verified citing paper (arXiv:2210.13286, Janzer–Johnson–Leader 2022) concerns lazy random transpositions and uniform mixing, not the deterministic t-reachable network problem. No resolution of the open asymptotics for t>=3 or the star-transposition gap was found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the minimum number of transpositions needed in a $t$-reachable network? What if all transpositions are of the form $(1,\cdot)$?

Context

The authors determine the exact minimum for $t=2$ (Theorem 2) and give an upper bound of $(2+o_t(1))n$ transpositions for fixed $t\geq 3$, but the asymptotics remain open for large $t$. Lower bounds for star-transposition $t$-reachable networks are also given, but a gap between upper and lower bounds remains even in that restricted setting.

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
