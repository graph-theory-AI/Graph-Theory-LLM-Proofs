Attack the following open graph-theory problem.

Catalog id: 2112.02313__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2112.02313__00/
Source paper: Kempe changes in degenerate graphs (arXiv:2112.02313)

=== Extracted statement (catalog JSON) ===
Title: Polynomial Kempe sequences for degenerate graphs
Can any two $k$-colorings of a $(k-1)$-degenerate graph on $n$ vertices always be connected by a sequence of Kempe changes whose length is polynomial in $n$?

Context:
Las Vergnas and Meyniel proved in 1981 that all $k$-colorings of a $d$-degenerate graph are Kempe equivalent when $k > d+1$, but their proof yields a sequence that may be exponential in the number of vertices. Whether a polynomial bound can be achieved is posed as an intriguing open question and is the central motivation for all three main results of the paper.

=== Catalog page (statement + literature review) ===
Polynomial Kempe connectivity in degenerate graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question of whether any two $k$-colorings of a $(k-1)$-degenerate graph on $n$ vertices can always be connected by a Kempe sequence of polynomial length remains open. The source paper (arXiv:2112.02313, published in European Journal of Combinatorics 2023) proves polynomial bounds only under stronger assumptions: $O(kn^2)$ Kempe changes when the graph has treewidth at most $k-1$, and $O(n^2)$ changes when the number of colors equals the maximum degree $\Delta$. No follow-up paper resolving the general $(k-1)$-degenerate case was found in the indexed literature.

 Reviewer notes. The source paper partially resolves the question: it proves polynomial bounds for the special cases of bounded treewidth (treewidth at most k-1 gives O(kn^2)) and maximum-degree colorings (O(n^2) for Delta-colorings, with one exception). The open question is specifically about general (k-1)-degenerate graphs with exactly k colors, which subsumes the treewidth case. A related 2025 paper (arXiv:2512.00695) studies Kempe changes in H-free graphs but focuses on Kempe connectivity (existence of a sequence), not polynomial length bounds. No resolution of the full conjecture was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Can any two $k$-colorings of a $(k-1)$-degenerate graph on $n$ vertices always be connected by a sequence of Kempe changes whose length is polynomial in $n$?

Context

Las Vergnas and Meyniel proved in 1981 that all $k$-colorings of a $d$-degenerate graph are Kempe equivalent when $k > d+1$, but their proof yields a sequence that may be exponential in the number of vertices. Whether a polynomial bound can be achieved is posed as an intriguing open question and is the central motivation for all three main results of the paper.

Notes. PDF source — stated as an open question in the abstract and introduction without a labeled environment; no explicit attribution to prior authors.

Source paper

 Kempe changes in degenerate graphs
 Marthe Bonamy, Vincent Delecroix, Clément Legrand-Duchesne · 2021-12-04
 https://arxiv.org/abs/2112.02313
 PDF source

=== Source paper abstract / header ===
Abstract:We consider Kempe changes on the $k$-colorings of a graph on $n$ vertices. If the graph is $(k-1)$-degenerate, then all its $k$-colorings are equivalent up to Kempe changes. However, the sequence between two $k$-colorings that arises from the proof may be exponential in the number of vertices. An intriguing open question is whether it can be turned polynomial. We prove this to be possible under the stronger assumption that the graph has treewidth at most $k-1$. Namely, any two $k$-colorings are equivalent up to $O(kn^2)$ Kempe changes. We investigate other restrictions (list coloring, bounded maximum average degree, degree bounds). As a main result, we derive that given an $n$-vertex graph with maximum degree $\Delta$, the $\Delta$-colorings are all equivalent up to $O(n^2)$ Kempe changes, unless $\Delta = 3$ and some connected component is a 3-prism.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2112.02313 [math.CO]
 

 
  
 (or 
 arXiv:2112.02313v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2112.02313
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Clément Legrand-Duchesne [view email] 
 [v1]
 Sat, 4 Dec 2021 11:34:38 UTC (27 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Kempe changes in degenerate graphs, by Marthe Bonamy and Vincent Delecroix and Cl\'ement Legrand-Duchesne
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
 | 2021-12
 

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
