Attack the following open graph-theory problem.

Catalog id: 1505.01616__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1505.01616__00/
Source paper: Colouring graphs with constraints on connectivity (arXiv:1505.01616)

=== Catalog page (statement + literature review) ===
k-coloring complexity for maximally locally connected graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Question 1.7 asks whether, for fixed k ≥ 4, there is a polynomial-time algorithm for k-colouring k-connected graphs with maximal local (vertex) connectivity k. The source paper settles the k=3 case with a polynomial-time algorithm (the class Ĉ^k_2), but explicitly leaves the case k ≥ 4 open. No subsequent paper resolving or substantially advancing this question was found across five targeted searches covering 2016–2026.

 Reviewer notes. No follow-up work found addressing Question 1.7 for k ≥ 4. The question has been open since 2016 (~10 years). Confidence is medium rather than high because the conjecture is old enough that absence of evidence in web search is less conclusive than for a recent paper. The complexity of k-colouring k-connected graphs with maximal local vertex connectivity k for k ≥ 4 remains a natural open problem in structural and algorithmic graph theory.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. For fixed $k \geq 4$, is there a polynomial-time algorithm that, given a $k$-connected graph $G$ with maximal local connectivity $k$, finds a $k$-colouring of $G$, or determines that none exists?

Context

Theorem 1.2 gives a polynomial-time algorithm for $k$-colouring when restricted to $\hat{\mathcal{C}}^k_1$ (k-connected graphs with maximal local edge-connectivity $k$). The complexity for the more general class $\hat{\mathcal{C}}^k_2$ (k-connected graphs with maximal local connectivity $k$) remains open for $k \geq 4$.

Also stated in

 
Colouring graphs with constraints on connectivity (2016-10-14) 

Source paper

 Colouring graphs with constraints on connectivity
 Pierre Aboulker, Nick Brettell, Frédéric Havet, Dániel Marx, Nicolas Trotignon · 2016-10-14
 https://arxiv.org/abs/1505.01616
 PDF source

=== Source paper abstract / header ===
Abstract:A graph $G$ has maximal local edge-connectivity $k$ if the maximum number of edge-disjoint paths between every pair of distinct vertices $x$ and $y$ is at most $k$. We prove Brooks-type theorems for $k$-connected graphs with maximal local edge-connectivity $k$, and for any graph with maximal local edge-connectivity 3. We also consider several related graph classes defined by constraints on connectivity. In particular, we show that there is a polynomial-time algorithm that, given a 3-connected graph $G$ with maximal local connectivity 3, outputs an optimal colouring for $G$. On the other hand, we prove, for $k \ge 3$, that $k$-colourability is NP-complete when restricted to minimally $k$-connected graphs, and 3-colourability is NP-complete when restricted to $(k-1)$-connected graphs with maximal local connectivity $k$. Finally, we consider a parameterization of $k$-colourability based on the number of vertices of degree at least $k+1$, and prove that, even when $k$ is part of the input, the corresponding parameterized problem is FPT.
 

 
 
 
 Comments:
 The latest version has minor corrections and clarifications
 

 Subjects:
 
 Combinatorics (math.CO); Computational Complexity (cs.CC)
 

 Cite as:
 arXiv:1505.01616 [math.CO]
 

 
  
 (or 
 arXiv:1505.01616v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1505.01616
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Graph Theory 85 (2017), 814-838
 

 
 
 Related DOI:
 
 https://doi.org/10.1002/jgt.22109

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Nick Brettell [view email] 
 [v1]
 Thu, 7 May 2015 08:11:23 UTC (30 KB)

 [v2]
 Fri, 14 Oct 2016 01:01:19 UTC (35 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Colouring graphs with constraints on connectivity, by Pierre Aboulker and 4 other authors
View PDF
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
 | 2015-05
 

 Change to browse by:
 
 cs
 cs.CC
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
