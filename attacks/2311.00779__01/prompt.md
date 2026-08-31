Attack the following open graph-theory problem.

Catalog id: 2311.00779__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2311.00779__01/
Source paper: Shortest paths on polymatroids and hypergraphic polytopes (arXiv:2311.00779)

=== Catalog page (statement + literature review) ===
Flip Distance Complexity for Rectangulations — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The computational complexity of computing the flip distance between two rectangulations of a unit square remains open as of May 2026. The source paper (Cardinal–Steiner 2023) proves NP-hardness for shortest paths on polymatroids in general — a framework that subsumes rectangulations as a special case — but this general hardness result does not resolve the specific complexity of the rectangulations instance. A wide search of the 2024–2026 literature found no follow-up paper settling this question; Cardinal’s June 2025 invited talk at CNRS still presents the rectangulations case within the same open context.

 Reviewer notes. No follow-up paper specifically resolving the complexity of flip distance between rectangulations was found. Closely related work in the same area: (1) Ito et al. proved NP-hardness of computing combinatorial shortest paths on graph associahedra (SIAM J. Discrete Math., 2024, DOI:10.1137/24M1720317), and an FPT algorithm for the same graph-associahedra problem appeared at ICALP 2025 (DOI:10.4230/LIPIcs.ICALP.2025.63); both concern elimination-tree flip graphs, not rectangulations. (2) The Rectangulotopes paper (arXiv:2404.17349, 2024) constructs polytopes whose skeleta are flip graphs on rectangulations but does not address computational complexity. The rectangulations case remains a specific open sub-problem within the broader polymatroid shortest-path framework of 2311.00779.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. What is the computational complexity of computing the flip distance between two rectangulations of a unit square?

Context

Rectangulations are tessellations of the unit square by axis-aligned rectangles, whose flip graphs are skeletons of polytopes that are polymatroids (and special cases of quotientopes). Since they fall under Problem 2 (shortest paths on a polymatroid), the authors note explicitly that the complexity of the flip distance problems between rectangulations remains open.

Notes. Stated in prose as 'The complexity of these problems is open.' PDF source — math notation appears clean for this item.

Source paper

 Shortest paths on polymatroids and hypergraphic polytopes
 Jean Cardinal, Raphael Steiner · 2023-11-06
 https://arxiv.org/abs/2311.00779
 PDF source

=== Source paper abstract / header ===
Abstract:Base polytopes of polymatroids, also known as generalized permutohedra, are polytopes whose edges are parallel to a vector of the form $\mathbf{e}_i - \mathbf{e}_j$. We consider the following computational problem: Given two vertices of a generalized permutohedron $P$, find a shortest path between them on the skeleton of $P$. This captures many known flip distance problems, such as computing the minimum number of exchanges between two spanning trees of a graph, the rotation distance between binary search trees, the flip distance between acyclic orientations of a graph, or rectangulations of a square. We prove that this problem is $NP$-hard, even when restricted to very simple polymatroids in $\mathbb{R}^n$ defined by $O(n)$ inequalities. Assuming $P\not= NP$, this rules out the existence of an efficient simplex pivoting rule that performs a minimum number of nondegenerate pivoting steps to an optimal solution of a linear program, even when the latter defines a polymatroid. We also prove that the shortest path problem is inapproximable when the polymatroid is specified via an evaluation oracle for a corresponding submodular function, strengthening a recent result by Ito et al. (ICALP'23). More precisely, we prove the $APX$-hardness of the shortest path problem when the polymatroid is a hypergraphic polytope, whose vertices are in bijection with acyclic orientations of a given hypergraph. The shortest path problem then amounts to computing the flip distance between two acyclic orientations of a hypergraph. On the positive side, we provide a polynomial-time approximation algorithm for the problem of computing the flip distance between two acyclic orientations of a hypergraph, where the approximation factor is the maximum codegree of the hypergraph. Our result implies an exact polynomial-time algorithm for the flip distance between two acyclic orientations of any linear hypergraph.
 

 
 
 
 Comments:
 26 pages, 5 figures, full version
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Combinatorics (math.CO); Optimization and Control (math.OC)
 
 
 MSC classes:
 90C05, 90C08, 90C27, 90C35, 90C49, 90C57, 90C60, 05C50, 05C65, 05B35, 52B40
 

 Cite as:
 arXiv:2311.00779 [cs.DS]
 

 
  
 (or 
 arXiv:2311.00779v2 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2311.00779
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Wed, 1 Nov 2023 18:46:52 UTC (125 KB)

 [v2]
 Mon, 6 Nov 2023 10:42:17 UTC (125 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Shortest paths on polymatroids and hypergraphic polytopes, by Jean Cardinal and 1 other authors
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
 | 2023-11
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.CO
 math.OC
 

 

 

 
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
