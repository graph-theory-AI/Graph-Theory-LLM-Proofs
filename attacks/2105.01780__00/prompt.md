Attack the following open graph-theory problem.

Catalog id: 2105.01780__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2105.01780__00/
Source paper: Approximation schemes for bounded distance problems on fractionally tre… (arXiv:2105.01780)

=== Catalog page (statement + literature review) ===
PTAS for weighted Minimum Vertex Cover in fragile classes — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The open problem asks whether a PTAS exists for weighted Minimum Vertex Cover (and more generally for distance-1 minimization problems) in fractionally treewidth-fragile graphs or hereditary classes with sublinear separators. The main obstruction is that the local-search technique that handles the unweighted case does not extend to weighted instances. A closely related subsequent paper by Dvořák (arXiv:2103.08698, SWAT 2022) gives approximation metatheorems for monotone maximization problems in these classes but explicitly restricts to maximization and does not resolve the minimization question. No paper found in the indexed literature as of May 2026 settles this problem.

 Reviewer notes. No follow-up resolving this open problem was found after an exhaustive 5-call web search. The most related post-2021 work is arXiv:2103.08698 (Dvořák, SWAT 2022) which proves approximation metatheorems for monotone *maximization* problems in fractionally treewidth-fragile classes, but explicitly does not cover minimization problems. The structural paper arXiv:2208.10074 (product structure of classes with strongly sublinear separators) is also related but contains no algorithmic results for vertex cover. The conjecture is recent (2021) and the absence of follow-up in the literature supports an open status with high confidence.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. For the minimization problems, we do not know whether fractional treewidth-fragility is sufficient even for the distance-1 problems. In particular, consider the Minimum Vertex Cover problem in fractionally treewidth-fragile graphs, or more generally in hereditary classes with sublinear separators: while the unweighted version can be dealt with by the local search method, we do not know whether there exists a PTAS for the weighted version of this problem.

Context

The paper's main results (Theorem 2 and its corollaries) apply exclusively to maximization problems; the authors extend fractional treewidth-fragility techniques to handle bounded-distance dependencies for near-monotone maximization. For minimization problems the analogous question is left open, with weighted Minimum Vertex Cover in fractionally treewidth-fragile (or sublinear-separator) classes offered as a concrete test case.

Notes. Stated in running prose without a labelled environment; PDF extraction — surrounding math is clean but statement itself is purely verbal.

Source paper

 Approximation schemes for bounded distance problems on fractionally treewidth-fragile graphs
 Zdeněk Dvořák, Abhiruk Lahiri · 2021-05-04
 https://arxiv.org/abs/2105.01780
 PDF source

=== Source paper abstract / header ===
Abstract:We give polynomial-time approximation schemes for monotone maximization problems expressible in terms of distances (up to a fixed upper bound) and efficiently solvable in graphs of bounded treewidth. These schemes apply in all fractionally treewidth-fragile graph classes, a property that is true for many natural graph classes with sublinear separators. We also provide quasipolynomial-time approximation schemes for these problems in all classes with sublinear separators.
 

 
 
 
 Comments:
 14 pages, no figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2105.01780 [cs.DS]
 

 
  
 (or 
 arXiv:2105.01780v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2105.01780
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Abhiruk Lahiri [view email] 
 [v1]
 Tue, 4 May 2021 22:12:10 UTC (13 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Approximation schemes for bounded distance problems on fractionally treewidth-fragile graphs, by Zden\v{e}k Dvo\v{r}\'ak and 1 other authors
View PDF
HTML (experimental)
TeX Source
 

 
 
 view license
 

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2021-05
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Zdenek Dvorák
Abhiruk Lahiri 

 

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
