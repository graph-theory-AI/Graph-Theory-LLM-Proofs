Attack the following open graph-theory problem.

Catalog id: 2410.23566__06
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2410.23566__06/
Source paper: Blow-ups and extensions of trees in tournaments (arXiv:2410.23566)

=== Catalog page (statement + literature review) ===
Unavoidability rate of k-extensions in tournaments — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 12 asks for the minimum function $f$ such that every $k$-extension of every forest of order $n$ is $(2^{f(k)}\cdot n)$-unavoidable in tournaments. As of the source paper (October 2024), the gap between the quadratic upper bound $f(k)\leq\binom{2k+2}{2}$ (Corollary 25) and the linear lower bound from Proposition 28 remains open. No follow-up paper resolving or narrowing this gap was found in a search of the literature up to May 2026.

 Reviewer notes. No follow-up found. The problem is recent (October 2024) and the wide web search covering author homepages (Lucas Picasarri-Arrieta's site, Clément Rambaud's DBLP) returned no paper addressing the gap between the linear lower bound and the quadratic upper bound on $f$. Status open with high confidence.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the minimum function $f$ such that every $k$-extension of every forest of order $n$ is $(2^{f(k)}\cdot n)$-unavoidable?

Context

This is the analogue of Problem 8 for extensions rather than blow-ups. Corollary 25 gives $f(k)\leqslant\binom{2k+2}{2}$ (quadratic upper bound), while Proposition 28 shows that the unavoidability of some $k$-extensions of the arcless digraph on $n$ vertices is $2^{k}n-o(n)$, giving a linear lower bound on $f$.

Source paper

 Blow-ups and extensions of trees in tournaments
 Pierre Aboulker, Frédéric Havet, William Lochet, Raul Lopes, Lucas Picasarri-Arrieta, Clément Rambaud · 2024-10-31
 https://arxiv.org/abs/2410.23566

=== Source paper abstract / header ===
Abstract:A class of acyclic digraphs $\mathscr{C}$ is linearly unavoidable if there exists a constant $c$ such that every digraph $D\in \mathscr{C}$ is contained in all tournaments of order $c\cdot |V(D)|$. The class of all acyclic digraphs is not linearly avoidable, and Fox, He, and Widgerson recently showed that this is not even the case for acyclic digraphs with bounded maximum degree. On the positive side, Thomason and Häggkvist proved that the class of oriented trees is linearly unavoidable. In this work, we generalize this result to acyclic digraphs obtained from an oriented tree by adding at most $k$ vertices, and $k$-blow-ups of oriented trees, for every fixed integer $k$.
More precisely, we show that if $D$ is obtained from an oriented tree $F$ of order $n$ by adding $k$ universal vertices, then $D$ is contained in every tournament of order $2\cdot 3^{(k+1)(2k+1)} \cdot n$; and if $D$ is obtained from $F$ by replacing each vertex $u$ by an independent set $X_u$ of size $k$ and every arc $uv$ by all possible arcs from $X_u$ to $X_v$, then $D$ is contained in every tournament of order $2^{10+18k}k \cdot n$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2410.23566 [math.CO]
 

 
  
 (or 
 arXiv:2410.23566v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2410.23566
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Lucas Picasarri-Arrieta [view email] 
 [v1]
 Thu, 31 Oct 2024 02:17:56 UTC (175 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Blow-ups and extensions of trees in tournaments, by Pierre Aboulker and 5 other authors
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
 | 2024-10
 

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
