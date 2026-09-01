Attack the following open graph-theory problem.

Catalog id: 1907.07250__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1907.07250__00/
Source paper: Shotgun reconstruction in the hypercube (arXiv:1907.07250)

=== Extracted statement (catalog JSON) ===
Title: Gap problem for 1-ball reconstruction threshold
Determine the correct threshold $q^*(n)$ such that almost every $q$-colouring of the hypercube $Q_n$ is reconstructible from the multiset of its coloured 1-balls, narrowing the gap between the lower bound $q = \Omega(n)$ and the upper bound $q \geq n^{2+\varepsilon}$.

Context:
Theorem 1.2 shows that for $q \geq n^{2+\varepsilon}$ almost every $q$-colouring of $Q_n$ is 1-distinguishable, while a counting argument shows that $\Omega(n)$ colours are necessary for reconstruction from 1-balls. The authors note explicitly that 'it would be interesting to narrow the gap', with further discussion deferred to Section 6 (open questions).

=== Catalog page (statement + literature review) ===
1-ball reconstruction threshold gap in Qₙ — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture asks to narrow the gap between the Omega(n) lower bound and the n^{2+epsilon} upper bound for the threshold number of colours q*(n) at which almost every q-colouring of Q_n becomes reconstructible from its multiset of coloured 1-balls. The source paper (published in Random Structures & Algorithms 60, 2022) established these two bounds, but no subsequent paper has been found that closes or significantly narrows this gap. Related shotgun assembly work on lattice models and random graphs has appeared, but none addresses the hypercube 1-ball threshold directly.

 Reviewer notes. No follow-up resolving or narrowing the gap was found in five web calls. The source paper appeared in Random Structures & Algorithms 60(1) 117-150 (2022). Nearby literature found includes arXiv:2205.01327 (shotgun threshold for lattice labeling model, Z^d not Q_n) and a 2025 Springer paper on shotgun assembly of random graphs — neither addresses the Q_n 1-ball colour threshold. The arXiv paper 2308.01671 ('Reconstruction of graph colourings') concerns k-deck reconstruction on grids and random graphs, not 1-ball coloring reconstruction on Q_n. The problem remains open with high confidence.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the correct threshold $q^*(n)$ such that almost every $q$-colouring of the hypercube $Q_n$ is reconstructible from the multiset of its coloured 1-balls, narrowing the gap between the lower bound $q = \Omega(n)$ and the upper bound $q \geq n^{2+\varepsilon}$.

Context

Theorem 1.2 shows that for $q \geq n^{2+\varepsilon}$ almost every $q$-colouring of $Q_n$ is 1-distinguishable, while a counting argument shows that $\Omega(n)$ colours are necessary for reconstruction from 1-balls. The authors note explicitly that 'it would be interesting to narrow the gap', with further discussion deferred to Section 6 (open questions).

Notes. Stated informally in the introduction without a labelled environment: 'It is easy to show that Ω(n) colours are required for reconstructability, and it would be interesting to narrow the gap (see Sections 1.1 and 6 for further discussion).' Section 6, which reportedly contains further open questions, was not included in the provided text extract.

Source paper

 Shotgun reconstruction in the hypercube
 Michał Przykucki, Alexander Roberts, Alex Scott · 2019-07-16
 https://arxiv.org/abs/1907.07250
 PDF source

=== Source paper abstract / header ===
Abstract:Mossel and Ross raised the question of when a random colouring of a graph can be reconstructed from local information, namely the colourings (with multiplicity) of balls of given radius. In this paper, we are concerned with random $2$-colourings of the vertices of the $n$-dimensional hypercube, or equivalently random Boolean functions. In the worst case, balls of diameter $\Omega(n)$ are required to reconstruct. However, the situation for random colourings is dramatically different: we show that almost every $2$-colouring can be reconstructed from the multiset of colourings of balls of radius $2$. Furthermore, we show that for $q \ge n^{2+\epsilon}$, almost every $q$-colouring can be reconstructed from the multiset of colourings of $1$-balls.
 

 
 
 
 Comments:
 36 pages
 

 Subjects:
 
 Combinatorics (math.CO); Probability (math.PR)
 
 
 MSC classes:
 05C60, 60C05 (Primary), 05C15 (Secondary)
 

 Cite as:
 arXiv:1907.07250 [math.CO]
 

 
  
 (or 
 arXiv:1907.07250v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1907.07250
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Michał Przykucki [view email] 
 [v1]
 Tue, 16 Jul 2019 20:32:37 UTC (30 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Shotgun reconstruction in the hypercube, by Micha{\l} Przykucki and 2 other authors
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
 | 2019-07
 

 Change to browse by:
 
 math
 math.PR
 

 

 

 
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
