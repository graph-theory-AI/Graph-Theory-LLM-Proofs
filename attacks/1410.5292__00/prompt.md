Attack the following open graph-theory problem.

Catalog id: 1410.5292__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1410.5292__00/
Source paper: Ordered Ramsey numbers (arXiv:1410.5292)

=== Extracted statement (catalog JSON) ===
Title: Open problem: ordered Ramsey number of matchings vs triangles
What is the correct order of magnitude of $r_<(M, K_3)$ for an ordered matching $M$ on $n$ vertices? The paper can only prove the trivial upper bound $r_<(M, K_3) \leq r_<(K_n, K_3) = O\!\left(\frac{n^2}{\log n}\right)$, while the lower bound of Theorem 1.8 gives $r_<(M, K_3) \geq c\left(\frac{n}{\log n}\right)^{4/3}$ for some ordered matching $M$ on $n$ vertices.

Context:
The classical off-diagonal Ramsey number $r(K_n, K_3)$ is known up to an asymptotic factor of 4 thanks to Kim's result and improvements via triangle-free processes. For ordered matchings the authors identify the analogous ordered problem but can only close a gap between an exponent of $4/3$ (lower) and $2$ (upper) in the logarithmic scale.

=== Catalog page (statement + literature review) ===
Ordered Ramsey number matching vs triangle magnitude — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture asks for the correct order of magnitude of $r_<(M, K_3)$ for an ordered matching $M$ on $n$ vertices, with the original gap between a lower bound of $\Omega((n/\log n)^{4/3})$ and the trivial upper bound $O(n^2/\log n)$. Balko and Poljak (2024) made significant partial progress: for almost all $n$-vertex ordered matchings with interval chromatic number 2, they establish $r_<(M^<, K^<_3) \in \Omega((n/\log n)^{4/3}) \cap O(n^{7/4})$, improving the upper-bound exponent from 2 to 7/4 for this class. The correct order of magnitude for general ordered matchings remains open.

 Cited literature (1)

 
 
 
partial On ordered Ramsey numbers of matchings versus triangles
 (2024)
 

 
 Balko, Martin; Poljak, Marian · Electronic Journal of Combinatorics · arXiv:2305.17933

For almost all $n$-vertex ordered matchings with interval chromatic number 2, proves $r_<(M^<,K^<_3) \in \Omega((n/\log n)^{4/3}) \cap O(n^{7/4})$, narrowing the exponent gap from $[4/3, 2]$ to $[4/3, 7/4]$ for this class; also shows matchings with interval chromatic number $\geq 3$ attain the general lower bound $\Omega((n/\log n)^{4/3})$; the full question for all ordered matchings remains open.
 

 

 Reviewer notes. Balko and Poljak (arXiv:2305.17933, published in Electronic Journal of Combinatorics 2024, vol. 31(2), P2.23) is the main follow-up directly addressing this problem. An extended abstract appeared at EuroComb 2023. The paper cites an earlier partial result by Rohatgi (2019) as prior art. The correct order of magnitude for all ordered matchings — not just those with bounded interval chromatic number — remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. What is the correct order of magnitude of $r_<(M, K_3)$ for an ordered matching $M$ on $n$ vertices? The paper can only prove the trivial upper bound $r_<(M, K_3) \leq r_<(K_n, K_3) = O\!\left(\frac{n^2}{\log n}\right)$, while the lower bound of Theorem 1.8 gives $r_<(M, K_3) \geq c\left(\frac{n}{\log n}\right)^{4/3}$ for some ordered matching $M$ on $n$ vertices.

Context

The classical off-diagonal Ramsey number $r(K_n, K_3)$ is known up to an asymptotic factor of 4 thanks to Kim's result and improvements via triangle-free processes. For ordered matchings the authors identify the analogous ordered problem but can only close a gap between an exponent of $4/3$ (lower) and $2$ (upper) in the logarithmic scale.

Notes. PDF source — math may be garbled; no explicit Problem/Question label; stated implicitly via 'we could only prove the trivial estimate'.

Source paper

 Ordered Ramsey numbers
 David Conlon, Jacob Fox, Choongbum Lee, Benny Sudakov · 2016-04-25
 https://arxiv.org/abs/1410.5292
 PDF source

=== Source paper abstract / header ===
Abstract:Given a labeled graph $H$ with vertex set $\{1, 2,\ldots,n\}$, the ordered Ramsey number $r_<(H)$ is the minimum $N$ such that every two-coloring of the edges of the complete graph on $\{1, 2, \ldots,N\}$ contains a copy of $H$ with vertices appearing in the same order as in $H$. The ordered Ramsey number of a labeled graph $H$ is at least the Ramsey number $r(H)$ and the two coincide for complete graphs. However, we prove that even for matchings there are labelings where the ordered Ramsey number is superpolynomial in the number of vertices. Among other results, we also prove a general upper bound on ordered Ramsey numbers which implies that there exists a constant $c$ such that $r_<(H) \leq r(H)^{c \log^2 n}$ for any labeled graph $H$ on vertex set $\{1,2, \dots, n\}$.
 

 
 
 
 Comments:
 27 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1410.5292 [math.CO]
 

 
  
 (or 
 arXiv:1410.5292v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1410.5292
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: David Conlon [view email] 
 [v1]
 Mon, 20 Oct 2014 14:34:29 UTC (26 KB)

 [v2]
 Mon, 25 Apr 2016 22:47:24 UTC (27 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Ordered Ramsey numbers, by David Conlon and 3 other authors
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
 | 2014-10
 

 Change to browse by:
 
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 
 
 3 blog links
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
