Attack the following open graph-theory problem.

Catalog id: 2112.02378__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2112.02378__00/
Source paper: Quasiplanar Graphs, String Graphs, and the Erdos-Gallai Problem (arXiv:2112.02378)

=== Catalog page (statement + literature review) ===
Linear K_{r-1}-free subgraph in K_r-free segment graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 1.2 asks whether every K_r-free segment graph on n vertices contains an induced K_{r-1}-free subgraph on \Omega_r(n) vertices. The source paper (Fox–Pach–Suk 2022) establishes analogous results for string graphs with a log^2(n) factor loss (Theorems 1.5–1.6), but the segment-graph case with a linear guarantee remains explicitly unresolved. A wide search of the post-2022 literature found no paper resolving the segment-graph case; the conjecture is open with high confidence.

 Reviewer notes. The closest post-2022 work found is arXiv:2409.06650 ('Induced Subgraphs of K_r-Free Graphs and the Erdős–Rogers Problem', Combinatorica 2025), which studies the Erdős–Rogers problem for general (non-geometric) K_r-free graphs; it does not address segment graphs and does not cite 2112.02378. No paper specifically resolving Problem 1.2 for segment graphs was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Fix an integer $r \geq 4$. Is it true that every $K_r$-free segment graph on $n$ vertices has an induced subgraph on $\Omega_r(n)$ vertices which is $K_{r-1}$-free?

Context

Motivated by the approach of coloring $K_r$-free string graphs to prove Conjecture 1.1: if each color class could be made $K_4$-free, Ackerman's result would bound the edges per class by $O(n)$. Although Krawczyk–Walczak showed $K_r$-free string graphs can require $\Omega_r(\log\log n)$ colors with $K_{r-1}$-free classes, the question of finding a linearly large $K_{r-1}$-free induced subgraph in a $K_r$-free segment graph remains open. The paper's Theorems 1.5 and 1.6 address analogous questions for string graphs (with a $\log^2 n$ loss), but the segment-graph case with a linear guarantee is unresolved.

Source paper

 Quasiplanar Graphs, String Graphs, and the Erdos-Gallai Problem
 Jacob Fox, Janos Pach, Andrew Suk · 2022-10-25
 https://arxiv.org/abs/2112.02378
 PDF source

=== Source paper abstract / header ===
Abstract:An $r$-quasiplanar graph is a graph drawn in the plane with no $r$ pairwise crossing edges. Let $s \geq 3$ be an integer and $r=2^s$. We prove that there is a constant $C$ such that every $r$-quasiplanar graph with $n \geq r$ vertices has at most $n\left(Cs^{-1}\log n\right)^{2s-4}$ edges.
A graph whose vertices are continuous curves in the plane, two being connected by an edge if and only if they intersect, is called a string graph. We show that for every $\epsilon>0$, there exists $\delta>0$ such that every string graph with $n$ vertices, whose chromatic number is at least $n^{\epsilon}$ contains a clique of size at least $n^{\delta}$. A clique of this size or a coloring using fewer than $n^{\epsilon}$ colors can be found by a polynomial time algorithm in terms of the size of the geometric representation of the set of strings.
In the process, we use, generalize, and strengthen previous results of Lee, Tomon, and others. All of our theorems are related to geometric variants of the following classical graph-theoretic problem of Erdos, Gallai, and Rogers. Given a $K_r$-free graph on $n$ vertices and an integer $s<r$, at least how many vertices can we find such that the subgraph induced by them is $K_s$-free?
 

 
 
 
 Comments:
 Appears in the Proceedings of the 30th International Symposium on Graph Drawing and Network Visualization (GD 2022)
 

 Subjects:
 
 Combinatorics (math.CO); Computational Geometry (cs.CG)
 

 Cite as:
 arXiv:2112.02378 [math.CO]
 

 
  
 (or 
 arXiv:2112.02378v6 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2112.02378
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Andrew Suk [view email] 
 [v1]
 Sat, 4 Dec 2021 16:41:28 UTC (19 KB)

 [v2]
 Tue, 7 Dec 2021 02:54:48 UTC (19 KB)

 [v3]
 Mon, 13 Dec 2021 17:18:27 UTC (14 KB)

 [v4]
 Sat, 3 Sep 2022 01:56:20 UTC (14 KB)

 [v5]
 Fri, 9 Sep 2022 14:33:48 UTC (37 KB)

 [v6]
 Tue, 25 Oct 2022 13:54:32 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Quasiplanar Graphs, String Graphs, and the Erdos-Gallai Problem, by Jacob Fox and 2 other authors
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
 cs.CG
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
