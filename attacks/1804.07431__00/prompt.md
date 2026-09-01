Attack the following open graph-theory problem.

Catalog id: 1804.07431__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1804.07431__00/
Source paper: Finding Cliques in Social Networks: A New Distribution-Free Model (arXiv:1804.07431)

=== Extracted statement (catalog JSON) ===
Title: Open Problem (exact exponent for maximal cliques in c-closed graphs)
Determine the exact exponent of $n$ (between $3/2$ and $2 - 2^{1-c}$) in the expression for the maximum number of maximal cliques in a $c$-closed graph on $n$ vertices.

Context:
Theorem 1.4 establishes an upper bound of $O(n^{2-2^{1-c}})$ maximal cliques in any $c$-closed graph on $n$ vertices, while Theorem 1.7 gives a matching lower bound of $\Omega(c^{-3/2} 2^{c/2} n^{3/2})$, leaving the exact exponent of $n$ undetermined for intermediate values of $c$. The two bounds coincide at $3/2$ and diverge as $c$ grows.

=== Catalog page (statement + literature review) ===
Exact exponent of maximal cliques in c-closed graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The open problem of determining the exact exponent of n (between 3/2 and 2 − 2^{1−c}) for the maximum number of maximal cliques in a c-closed graph remains unresolved as of 2026. Follow-up work has improved the enumeration algorithm to output-sensitive complexity (arXiv:2303.02390, 2023) and extended the polynomial-bound framework to maximal blow-ups of arbitrary graphs H (arXiv:2506.11437, 2025), but neither paper improves the upper or lower bounds on the exponent for cliques specifically — the 2025 paper explicitly restates the original O(n^{2−2^{1−c}}) bound without improvement.

 Reviewer notes. Two related papers found after 2018: arXiv:2303.02390 (2023) improves maximal clique enumeration in weakly closed graphs to output-sensitive α·O(n·poly(c)) time but does not address the count bounds or exact exponent; arXiv:2506.11437 (2025) extends the framework to maximal blow-ups of arbitrary finite graphs H, explicitly restating the original Fox et al. upper bound O(n^{2−2^{1−c}}) without improvement. No paper resolving the exact exponent gap was found within 5 web calls. Confidence is medium rather than high because the problem is 8 years old (2018) and a wide search found only adjacent work, but the gap between the 3/2 lower bound exponent and the 2−2^{1−c} upper bound exponent is a hard combinatorial question.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the exact exponent of $n$ (between $3/2$ and $2 - 2^{1-c}$) in the expression for the maximum number of maximal cliques in a $c$-closed graph on $n$ vertices.

Context

Theorem 1.4 establishes an upper bound of $O(n^{2-2^{1-c}})$ maximal cliques in any $c$-closed graph on $n$ vertices, while Theorem 1.7 gives a matching lower bound of $\Omega(c^{-3/2} 2^{c/2} n^{3/2})$, leaving the exact exponent of $n$ undetermined for intermediate values of $c$. The two bounds coincide at $3/2$ and diverge as $c$ grows.

Notes. Stated in running prose as 'It is an open problem'; no labelled theorem environment. PDF source — math notation may be garbled.

Source paper

 Finding Cliques in Social Networks: A New Distribution-Free Model
 Jacob Fox, Tim Roughgarden, C. Seshadhri, Fan Wei, Nicole Wein · 2018-04-20
 https://arxiv.org/abs/1804.07431
 PDF source

=== Source paper abstract / header ===
Abstract:We propose a new distribution-free model of social networks. Our definitions are motivated by one of the most universal signatures of social networks, triadic closure---the property that pairs of vertices with common neighbors tend to be adjacent. Our most basic definition is that of a "$c$-closed" graph, where for every pair of vertices $u,v$ with at least $c$ common neighbors, $u$ and $v$ are adjacent. We study the classic problem of enumerating all maximal cliques, an important task in social network analysis. We prove that this problem is fixed-parameter tractable with respect to $c$ on $c$-closed graphs. Our results carry over to "weakly $c$-closed graphs", which only require a vertex deletion ordering that avoids pairs of non-adjacent vertices with $c$ common neighbors. Numerical experiments show that well-studied social networks tend to be weakly $c$-closed for modest values of $c$.
 

 
 
 
 Comments:
 main text 13 pages; 2 figures; appendix 9 pages
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Social and Information Networks (cs.SI)
 
 
 MSC classes:
 68W01, 68R10, 05C85, 05D99
 

 Cite as:
 arXiv:1804.07431 [math.CO]
 

 
  
 (or 
 arXiv:1804.07431v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1804.07431
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Fan Wei [view email] 
 [v1]
 Fri, 20 Apr 2018 02:37:31 UTC (135 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Finding Cliques in Social Networks: A New Distribution-Free Model, by Jacob Fox and 4 other authors
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
 | 2018-04
 

 Change to browse by:
 
 cs
 cs.DM
 cs.DS
 cs.SI
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
