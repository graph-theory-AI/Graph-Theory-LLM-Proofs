Attack the following open graph-theory problem.

Catalog id: 2202.06810__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2202.06810__00/
Source paper: Structured Codes of Graphs (arXiv:2202.06810)

=== Catalog page (statement + literature review) ===
M_{F_{2c}}(n) gap for odd n — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question of determining $M_{F_{2c}}(n)$ for odd $n \geq 5$ remains open. The upper bound $M_{F_{2c}}(n) \leq 2^{n-2}$ is established in the source paper, but the best-known construction for odd $n$ gives only $2^{n-2} - \binom{n-2}{(n-3)/2}$, leaving a gap. A 2023 follow-up by Bai, Gao, Ma, and Wu (arXiv:2307.08266, SIAM J. Discrete Math.) studies related phase-transition problems for $M_{\mathcal{F}}(n)$ and announces a partial solution to a problem from the source paper, but this refers to Problem 3 about spanning trees with many leaves, not to the 2-connected code problem; no paper found closes the odd-$n$ gap for $M_{F_{2c}}$.

 Reviewer notes. The Semantic Scholar citation list for arXiv:2202.06810 contains 17 citing papers (as of May 2026); the most topically adjacent is arXiv:2307.08266 (Bai–Gao–Ma–Wu, SIAM JDM 2024), whose 'partial solution to a recent problem posed by Alon et al.' addresses Problem 3 (spanning-tree leaf sequences), not the 2-connected code problem. Alon's 'Connectivity graph-codes' (arXiv:2308.07653, Random Struct. Algorithms 2024) and Versteegen's 'Upper Bounds for Linear Graph Codes' (arXiv:2310.19891) were identified as citing papers but do not appear to address $M_{F_{2c}}$ for odd $n$ specifically. No follow-up resolving the odd-$n$ gap was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine $M_{F_{2c}}(n)$ for odd $n \geq 5$. The upper bound $M_{F_{2c}}(n) \leq 2^{n-2}$ holds for all $n$, but the best construction for odd $n$ yields only $2^{n-2} - \binom{n-2}{(n-3)/2}$ graphs.

Context

Theorem 3 establishes $M_{F_{2c}}(n) = 2^{n-2}$ for all even $n$ via matching upper and lower bounds. For odd $n$ the upper bound still holds, but the construction from the even case fails; the best the authors could achieve gives $2^{n-2} - \binom{n-2}{(n-3)/2}$, leaving a gap. For $n = 3$ the upper bound is attained (a triangle and the empty graph), but no general matching construction is known.

Notes. Stated as Remark 2 without a formal Problem/Conjecture environment; the authors do not explicitly conjecture the true value for odd $n$ but clearly identify it as an open case.

Source paper

 Structured Codes of Graphs
 Noga Alon, Anna Gujgiczer, János Körner, Aleksa Milojević, Gábor Simonyi · 2022-04-01
 https://arxiv.org/abs/2202.06810
 PDF source

=== Source paper abstract / header ===
Abstract:We investigate the maximum size of graph families on a common vertex set of cardinality $n$ such that the symmetric difference of the edge sets of any two members of the family satisfies some prescribed condition. We solve the problem completely for infinitely many values of $n$ when the prescribed condition is connectivity or $2$-connectivity, Hamiltonicity or the containment of a spanning star. We also investigate local conditions that can be certified by looking at only a subset of the vertex set. In these cases a capacity-type asymptotic invariant is defined and when the condition is to contain a certain subgraph this invariant is shown to be a simple function of the chromatic number of this required subgraph. This is proven using classical results from extremal graph theory. Several variants are considered and the paper ends with a collection of open problems.
 

 
 
 
 Comments:
 The paper is significantly revised: there are more authors, more results, in particular, some of the open problems of the earlier version are solved, and even the title has been changed. 29 pages
 

 Subjects:
 
 Combinatorics (math.CO); Information Theory (cs.IT)
 
 
 MSC classes:
 05C35, 05C51, 05C70, 94B25
 

 Cite as:
 arXiv:2202.06810 [math.CO]
 

 
  
 (or 
 arXiv:2202.06810v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2202.06810
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Gábor Simonyi [view email] 
 [v1]
 Mon, 14 Feb 2022 15:52:46 UTC (22 KB)

 [v2]
 Fri, 25 Feb 2022 17:46:31 UTC (22 KB)

 [v3]
 Fri, 1 Apr 2022 20:31:00 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Structured Codes of Graphs, by Noga Alon and 4 other authors
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
 | 2022-02
 

 Change to browse by:
 
 cs
 cs.IT
 math
 math.IT
 

 

 

 
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
