Attack the following open graph-theory problem.

Catalog id: 1707.03747__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1707.03747__00/
Source paper: Colouring perfect graphs with bounded clique number (arXiv:1707.03747)

=== Extracted statement (catalog JSON) ===
Title: Open Question on Number of Tight Skew Partitions
We do not know how many tight skew partitions there can really be; the authors do not know of a graph with more than linearly many tight skew partitions.

Context:
The paper shows there are at most $n^3 \log n$ tight skew partitions in an $n$-vertex graph (improving the $n^4$ bound from the Kennedy–Reed list), because for every tight skew partition $(A,B)$ the set $B$ appears at least $k_2^2$ times in the Kennedy–Reed output, where $k_2$ is the size of the second-largest anticomponent of $G[B]$. The true maximum is unknown.

=== Catalog page (statement + literature review) ===
Maximum tight skew partitions in perfect graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The paper establishes an upper bound of $n^3 \log n$ tight skew partitions in any $n$-vertex graph (improving the prior $n^4$ Kennedy--Reed bound), but the true maximum remains unknown. The authors observe they know of no graph with more than linearly many tight skew partitions, leaving open whether the correct order is $\Theta(n)$ or something between linear and $n^3 \log n$. A broad literature search spanning 2017--2026 found no follow-up paper resolving or improving this bound.

 Reviewer notes. No follow-up found after five web calls. The open question asks for the true order of the maximum number of tight skew partitions in an $n$-vertex graph; the gap is between $\Omega(n)$ (no known super-linear example) and $O(n^3 \log n)$ (the paper's upper bound). The conjecture is closely related to the algorithmic complexity of finding balanced skew partitions in perfect graphs.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We do not know how many tight skew partitions there can really be; the authors do not know of a graph with more than linearly many tight skew partitions.

Context

The paper shows there are at most $n^3 \log n$ tight skew partitions in an $n$-vertex graph (improving the $n^4$ bound from the Kennedy–Reed list), because for every tight skew partition $(A,B)$ the set $B$ appears at least $k_2^2$ times in the Kennedy–Reed output, where $k_2$ is the size of the second-largest anticomponent of $G[B]$. The true maximum is unknown.

Notes. Stated as prose without a labelled theorem environment. PDF source.

Source paper

 Colouring perfect graphs with bounded clique number
 Maria Chudnovsky, Aurélie Lagoutte, Paul Seymour, Sophie Spirkl · 2017-07-12
 https://arxiv.org/abs/1707.03747
 PDF source

=== Source paper abstract / header ===
Abstract:A graph is perfect if the chromatic number of every induced subgraph equals the size of its largest clique, and an algorithm of Grötschel, Lovász, and Schrijver from 1988 finds an optimal colouring of a perfect graph in polynomial time. But this algorithm uses the ellipsoid method, and it is a well-known open question to construct a "combinatorial" polynomial-time algorithm that yields an optimal colouring of a perfect graph.
A skew partition in $G$ is a partition $(A,B)$ of $V(G)$ such that $G[A]$ is not connected and $\bar{G}[B]$ is not connected, where $\bar{G}$ denotes the complement graph ; and it is balanced if an additional parity condition of paths in $G$ and $\bar{G}$ is satisfied.
In this paper we first give a polynomial-time algorithm that, with input a perfect graph, outputs a balanced skew partition if there is one. Then we use this to obtain a combinatorial algorithm that finds an optimal colouring of a perfect graph with clique number $k$, in time that is polynomial for fixed $k$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:1707.03747 [math.CO]
 

 
  
 (or 
 arXiv:1707.03747v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1707.03747
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Combinatorial Theory, Series B, 122:757-775, 2017
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.jctb.2016.09.006

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Aurélie Lagoutte [view email] 
 [v1]
 Wed, 12 Jul 2017 14:56:22 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Colouring perfect graphs with bounded clique number, by Maria Chudnovsky and 2 other authors
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
 | 2017-07
 

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
