Attack the following open graph-theory problem.

Catalog id: 2206.00594__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2206.00594__00/
Source paper: Sparse graphs with bounded induced cycle packing number have logarithmi… (arXiv:2206.00594)

=== Catalog page (statement + literature review) ===
Polynomial MIS in 𝒪_k-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 1.3 states that Maximum Independent Set is solvable in polynomial time in all $\mathcal{O}_k$-free graphs. The source paper itself proves the result for sparse $\mathcal{O}_k$-free graphs (Corollary 1.2) and gives a quasi-polynomial algorithm ($n^{O(k^2 \log n)}$) for the general case, stopping short of resolving the full conjecture. A November 2025 preprint (arXiv:2511.10019) introduces Odd-Cycle-Packing-treewidth (OCP-tw) and proves MIS polynomial for bounded OCP-tw in odd-minor-free graph classes, which is thematically related but does not directly establish the polynomial-time result for general $\mathcal{O}_k$-free graphs. No paper resolving the full conjecture was found.

 Cited literature (1)

 
 
 
partial Odd-Cycle-Packing-treewidth: On the Maximum Independent Set problem in odd-minor-free graph classes
 (2025)
 

 
 authors not retrieved from abstract · arXiv preprint · arXiv:2511.10019

Introduces OCP-treewidth and proves MIS solvable in polynomial time on graphs of bounded OCP-tw in odd-minor-free graph classes; whether $\mathcal{O}_k$-free graphs have bounded OCP-tw is not established, so the conjecture is not directly resolved.
 

 

 Reviewer notes. The source paper's own Corollary 1.2 already settles the sparse case and gives a quasi-polynomial algorithm for the general case; Conjecture 1.3 asks for the remaining step to full polynomial time. Paper arXiv:2511.10019 (Nov 2025) is the closest related post-paper work found, proving MIS polynomial for bounded OCP-treewidth, but the relationship between OCP-treewidth and the $\mathcal{O}_k$-free property could not be confirmed within the search budget. No direct resolution of Conjecture 1.3 was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Maximum Independent Set is solvable in polynomial time in $\mathcal{O}_{k}$-free graphs.

Context

The paper proves that sparse $\mathcal{O}_k$-free graphs have logarithmic treewidth, making Maximum Independent Set polynomial in the sparse case (Corollary 1.2). A quasipolynomial algorithm is also given for general $\mathcal{O}_k$-free graphs, stopping just short of resolving this conjecture in full generality.

Source paper

 Sparse graphs with bounded induced cycle packing number have logarithmic treewidth
 Marthe Bonamy, Édouard Bonnet, Hugues Déprés, Louis Esperet, Colin Geniet, Claire Hilaire, Stéphan Thomassé, Alexandra Wesolek · 2024-02-16
 https://arxiv.org/abs/2206.00594

=== Source paper abstract / header ===
Abstract:A graph is $\mathcal{O}_k$-free if it does not contain $k$ pairwise vertex-disjoint and non-adjacent cycles. We prove that "sparse" (here, not containing large complete bipartite graphs as subgraphs) $\mathcal{O}_k$-free graphs have treewidth (even, feedback vertex set number) at most logarithmic in the number of vertices. This is optimal, as there is an infinite family of $\mathcal{O}_2$-free graphs without $K_{2,3}$ as a subgraph and whose treewidth is (at least) logarithmic.
Using our result, we show that Maximum Independent Set and 3-Coloring in $\mathcal{O}_k$-free graphs can be solved in quasi-polynomial time. Other consequences include that most of the central NP-complete problems (such as Maximum Independent Set, Minimum Vertex Cover, Minimum Dominating Set, Minimum Coloring) can be solved in polynomial time in sparse $\mathcal{O}_k$-free graphs, and that deciding the $\mathcal{O}_k$-freeness of sparse graphs is polynomial time solvable.
 

 
 
 
 Comments:
 30 pages, 6 figures. v5: revised version
 

 Subjects:
 
 Combinatorics (math.CO); Data Structures and Algorithms (cs.DS)
 

 Cite as:
 arXiv:2206.00594 [math.CO]
 

 
  
 (or 
 arXiv:2206.00594v5 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2206.00594
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Combinatorial Theory, Series B 167 (2024), 215-249
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.jctb.2024.03.003

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Louis Esperet [view email] 
 [v1]
 Wed, 1 Jun 2022 16:06:38 UTC (138 KB)

 [v2]
 Tue, 14 Jun 2022 10:57:46 UTC (138 KB)

 [v3]
 Mon, 18 Jul 2022 08:18:18 UTC (140 KB)

 [v4]
 Tue, 11 Apr 2023 12:12:39 UTC (141 KB)

 [v5]
 Fri, 16 Feb 2024 09:36:29 UTC (143 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Sparse graphs with bounded induced cycle packing number have logarithmic treewidth, by Marthe Bonamy and 7 other authors
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
 | 2022-06
 

 Change to browse by:
 
 cs
 cs.DS
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 
 
 1 blog link
 (what is this?)
 

 

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
