Attack the following open graph-theory problem.

Catalog id: 1608.07028__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1608.07028__00/
Source paper: Random subgraphs of properly edge-coloured complete graphs and long rai… (arXiv:1608.07028)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: error term for longest rainbow cycle
Determine the correct order of the error term in the maximum length of a rainbow cycle guaranteed in every properly edge-coloured $K_n$; currently the deficit is known to lie between $-1$ and $-O(n^{3/4})$.

Context:
Theorem 1.2 establishes a rainbow cycle of length at least $n - 24n^{3/4}$, while Andersen's Conjecture 1.1 posits a rainbow path of length $n-2$. The authors note that the constant $24$ in front of $n^{3/4}$ is not optimised, and leave as an open problem the task of pinning down the true order of the error term.

=== Catalog page (statement + literature review) ===
Rainbow cycle error term in K_n — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The open problem asks for the exact order of the error term $n - \ell^*(n)$, where $\ell^*(n)$ is the length of the longest rainbow cycle guaranteed in every properly edge-coloured $K_n$. Alon, Pokrovskiy, and Sudakov (2016, arXiv:1608.07028) established $\ell^*(n) \ge n - O(n^{3/4})$. Balogh and Molla (arXiv:1706.04950, published 2019) subsequently improved this to $\ell^*(n) \ge n - O(\log n \cdot \sqrt{n})$, so the deficit now lies between $\Omega(1)$ and $O(\log n \cdot \sqrt{n})$; the exact order remains open.

 Cited literature (1)

 
 
 
partial Long rainbow cycles and Hamiltonian cycles using many colors in properly edge-colored complete graphs
 (2019)
 

 
 J\u00f3zsef Balogh, Theodore Molla · European Journal of Combinatorics · arXiv:1706.04950

Improves the error term for the longest rainbow cycle in any properly edge-coloured $K_n$ from $O(n^{3/4})$ to $O(\log n \cdot \sqrt{n})$.
 

 

 Reviewer notes. Balogh-Molla 2019 (arXiv:1706.04950) improved the upper bound on the error term from $O(n^{3/4})$ to $O(\log n \cdot \sqrt{n})$, but the exact order remains unknown. A 2023 paper (arXiv:2309.04460, Alon-Buc\u0301ic\u0301-Sauermann-Zakharov-Zamir) achieves essentially tight bounds for rainbow cycles in sparse properly edge-coloured graphs, but does not directly resolve the deficit question for $K_n$. Andersen's Conjecture (rainbow path of length $n-2$) remains open and would imply a deficit of $O(1)$.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the correct order of the error term in the maximum length of a rainbow cycle guaranteed in every properly edge-coloured $K_n$; currently the deficit is known to lie between $-1$ and $-O(n^{3/4})$.

Context

Theorem 1.2 establishes a rainbow cycle of length at least $n - 24n^{3/4}$, while Andersen's Conjecture 1.1 posits a rainbow path of length $n-2$. The authors note that the constant $24$ in front of $n^{3/4}$ is not optimised, and leave as an open problem the task of pinning down the true order of the error term.

Notes. Stated in prose immediately after Theorem 1.2: 'leaving as an open problem to pin down the correct order of the error term (currently between −1 and −O(n^{3/4}))'.

Source paper

 Random subgraphs of properly edge-coloured complete graphs and long rainbow cycles
 Noga Alon, Alexey Pokrovskiy, Benny Sudakov · 2016-08-25
 https://arxiv.org/abs/1608.07028
 PDF source

=== Source paper abstract / header ===
Abstract:A subgraph of an edge-coloured complete graph is called rainbow if all its edges have different colours. In 1980 Hahn conjectured that every properly edge-coloured complete graph $K_n$ has a rainbow Hamiltonian path. Although this conjecture turned out to be false, it was widely believed that such a colouring always contains a rainbow cycle of length almost $n$. In this paper, improving on several earlier results, we confirm this by proving that every properly edge-coloured $K_n$ has a rainbow cycle of length $n-O(n^{3/4})$. One of the main ingredients of our proof, which is of independent interest, shows that a random subgraph of a properly edge-coloured $K_n$ formed by the edges of a random set of colours has a similar edge distribution as a truly random graph with the same edge density. In particular it has very good expansion properties.
 

 
 
 
 Comments:
 9 pages, 1 figure
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C38, 05C45, 05B15
 

 Cite as:
 arXiv:1608.07028 [math.CO]
 

 
  
 (or 
 arXiv:1608.07028v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1608.07028
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexey Pokrovskiy [view email] 
 [v1]
 Thu, 25 Aug 2016 06:39:53 UTC (41 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Random subgraphs of properly edge-coloured complete graphs and long rainbow cycles, by Noga Alon and 2 other authors
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
 | 2016-08
 

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
