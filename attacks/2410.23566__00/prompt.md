Attack the following open graph-theory problem.

Catalog id: 2410.23566__00
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2410.23566__00/
Source paper: Blow-ups and extensions of trees in tournaments (arXiv:2410.23566)

=== Catalog page (statement + literature review) ===
Polynomial unavoidability in bounded average degree digraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 6 from arXiv:2410.23566 asks whether for each positive real α there exists a polynomial P_α bounding unvd(D) for every digraph with maximum average degree at most α. The question is motivated by Fox, He, and Wigderson's result (arXiv:2105.02383) establishing that acyclic digraphs with bounded maximum degree are not linearly unavoidable, with unavoidability growing as n^{Ω(Δ^{2/3}/log^{5/3}Δ)}. No paper resolving the polynomial question or providing a counterexample was found in the literature as of May 2026.

 Reviewer notes. No follow-up found in indexed literature. The Fox–He–Wigderson result (arXiv:2105.02383, 'Ramsey numbers of sparse digraphs', Israel J. Math. 2024) rules out linear unavoidability for bounded-degree acyclic digraphs but leaves the polynomial question open; Problem 6 asks about bounded maximum average degree, a condition weaker than bounded maximum degree, so the Fox–He–Wigderson lower bounds do not directly answer it.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. Let $\alpha$ be a positive real number. Does there exist a polynomial $P_{\alpha}$ such that $\operatorname{unvd}(D)\leqslant P_{\alpha}(|V(D)|)$ for every digraph with maximum average degree at most $\alpha$?

Context

Fox, He, and Wigderson showed that acyclic digraphs with bounded maximum degree are not linearly unavoidable, ruling out linear bounds. This problem asks whether the weaker polynomial unavoidability still holds for digraphs with bounded maximum average degree, and is complemented by the second question of which families of such digraphs are linearly unavoidable.

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
