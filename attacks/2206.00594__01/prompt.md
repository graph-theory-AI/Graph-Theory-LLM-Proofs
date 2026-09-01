Attack the following open graph-theory problem.

Catalog id: 2206.00594__01
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2206.00594__01/
Source paper: Sparse graphs with bounded induced cycle packing number have logarithmi… (arXiv:2206.00594)

=== Extracted statement (catalog JSON) ===
Title: Open Question: bounded twin-width for sparse $\mathcal{O}_k$-free graphs
Is there a function $f:\mathbb{N}\times\mathbb{N}\to\mathbb{N}$ such that every $\mathcal{O}_{k}$-free graph that does not contain $K_{t,t}$ as a subgraph has twin-width at most $f(t,k)$?

Context:
The paper shows that sparse $\mathcal{O}_k$-free graphs have logarithmic treewidth, but leaves open whether their twin-width is also bounded as a function of $t$ and $k$. The authors note that $\mathcal{O}_2$-free graphs without $K_{3,3}$ already yield a new family of counterexamples to bounded treewidth from forbidden induced subgraphs alone.

=== Catalog page (statement + literature review) ===
Twin-width bound for K_{t,t}-free O_k-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The open question from arXiv:2206.00594 asks whether $\mathcal{O}_k$-free graphs that exclude $K_{t,t}$ as a subgraph have twin-width bounded by a function of $t$ and $k$. The source paper establishes that such graphs have treewidth at most $O_{t,k}(\log n)$, but the twin-width question is explicitly left open. A related result (arXiv:2307.01732) shows the converse direction for twin-width 2: sparse graphs of twin-width at most 2 have bounded treewidth, but this does not imply bounded twin-width for the $\mathcal{O}_k$-free class. No follow-up resolving the question was found in a wide web search through May 2026.

 Reviewer notes. No follow-up resolving or disproving the conjecture was found. Paper 2307.01732 ('Sparse Graphs of Twin-Width 2 Have Bounded Tree-Width') is tangentially related but addresses the inverse direction and is restricted to twin-width 2. The conjecture remains open with high confidence as of May 2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is there a function $f:\mathbb{N}\times\mathbb{N}\to\mathbb{N}$ such that every $\mathcal{O}_{k}$-free graph that does not contain $K_{t,t}$ as a subgraph has twin-width at most $f(t,k)$?

Context

The paper shows that sparse $\mathcal{O}_k$-free graphs have logarithmic treewidth, but leaves open whether their twin-width is also bounded as a function of $t$ and $k$. The authors note that $\mathcal{O}_2$-free graphs without $K_{3,3}$ already yield a new family of counterexamples to bounded treewidth from forbidden induced subgraphs alone.

Notes. Stated in prose in the introduction without a labelled theorem environment; language is explicit ('we leave as an open question').

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
