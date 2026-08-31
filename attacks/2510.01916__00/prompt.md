Attack the following open graph-theory problem.

Catalog id: 2510.01916__00
Catalog status: open (triage tier 1, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2510.01916__00/
Source paper: Short circuit walks in fixed dimension (arXiv:2510.01916)

=== Catalog page (statement + literature review) ===
NP-hardness of Circuit Distance for polytopes — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 21 from arXiv:2510.01916 posits that Circuit Distance (the non-monotone variant) is NP-hard for polygons. The paper's main result (Theorem 1) already establishes NP-hardness for the monotone variant, and the authors remark that their proof techniques seem likely to extend to the non-monotone setting. No follow-up paper resolving this conjecture was found in a wide web search; the conjecture is very recent (October 2025) and remains open.

 Reviewer notes. The paper proves NP-hardness of Monotone Circuit Distance for polygons (Theorem 1) and conjectures the same holds for the non-monotone Circuit Distance problem (Conjecture 21). The conjecture is recent (≤ 1 year) and a wide search found no resolution; open with high confidence. A related ScienceDirect paper 'On the hardness of short and sign-compatible circuit walks' (pii/S0166218X25000678) may be relevant background work but returned HTTP 403 and could not be verified.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Circuit Distance is $\mathsf{NP}$-hard for polygons.

Context

The authors focus on monotone circuit walks as most directly relevant to circuit augmentation schemes, but note the non-monotone variant is natural too. The Circuit Distance problem asks whether there is a circuit walk from $\mathbf{s}$ to $\mathbf{t}$ of length at most $k$ in a polytope $P=\{\mathbf{x}\in\mathbb{R}^{n}\colon Ax\leq\mathbf{b}\}$. The authors remark that their proof techniques seem likely to extend to this non-monotone setting.

Notes. Polygons are 2-dimensional polytopes; in this case circuit directions coincide with edge directions (as noted in Observation 9 of the paper).

Source paper

 Short circuit walks in fixed dimension
 Alexander E. Black, Christian Nöbel, Raphael Steiner · 2025-10-02
 https://arxiv.org/abs/2510.01916

=== Source paper abstract / header ===
Abstract:Circuit augmentation schemes are a family of combinatorial algorithms for linear programming that generalize the simplex method. To solve the linear program, they construct a so-called monotone circuit walk: They start at an initial vertex of the feasible region and traverse a discrete sequence of points on the boundary, while moving along certain allowed directions (circuits) and improving the objective function at each step until reaching an optimum. Since the existence of short circuit walks has been conjectured (Circuit Diameter Conjecture), several works have investigated how well one can efficiently approximate shortest monotone circuit walks towards an optimum. A first result addressing this question was given by De Loera, Kafer, and Sanità [SIAM J. Opt., 2022], who showed that given as input an LP and the starting vertex, finding a $2$-approximation for this problem is NP-hard. Cardinal and the third author [Math. Prog. 2023] gave a stronger lower bound assuming the exponential time hypothesis, showing that even an approximation factor of $O(\frac{\log m}{\log \log m})$ is intractable for LPs defined by $m$ inequalities. Both of these results were based on reductions from highly degenerate polytopes in combinatorial optimization with high dimension.
In this paper, we significantly strengthen the aforementioned hardness results by showing that for every fixed $\varepsilon>0$ approximating the problem on polygons with $m$ edges to within a factor of $O(m^{1-\varepsilon})$ is NP-hard. This result is essentially best-possible, as it cannot be improved beyond $o(m)$. In particular, this implies hardness for simple polytopes and in fixed dimension.
 

 
 
 
 Comments:
 27 pages
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2510.01916 [cs.DS]
 

 
  
 (or 
 arXiv:2510.01916v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2510.01916
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Christian Nöbel [view email] 
 [v1]
 Thu, 2 Oct 2025 11:33:52 UTC (44 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Short circuit walks in fixed dimension, by Alexander E. Black and 2 other authors
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
 | 2025-10
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
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
