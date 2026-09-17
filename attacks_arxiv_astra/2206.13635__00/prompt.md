Attack the following open graph-theory problem.

Catalog id: 2206.13635__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2206.13635__00/
Source paper: Coloring hypergraphs with excluded minors (arXiv:2206.13635)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2
For every integer $t\geq 2$ we have $h(t)=\left\lceil\frac{3}{2}(t-1)\right\rceil$. In other words, if a hypergraph $H$ does not contain $K_{t}$ as a minor, then $\chi(H)\leq\left\lceil\frac{3}{2}(t-1)\right\rceil$.

Context:
The function $h(t)$ is the smallest integer such that every $K_t$-minor-free hypergraph is $h(t)$-colorable. The paper proves the lower bound $h(t)\geq\left\lceil\frac{3}{2}(t-1)\right\rceil$ by an explicit construction, and conjectures this lower bound is tight. The conjecture remains open even for $t=3$, where the best known upper bound is $4$.

=== Catalog page (statement + literature review) ===
Chromatic number of Kₜ-minor-free hypergraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 2 of Steiner (arXiv:2206.13635) — that h(t) = ⌈3/2(t-1)⌉ for all t ≥ 2 — remains open as of 2026. The paper establishes the matching lower bound by construction and proves the conjecture for hypergraphs with independence number at most 2; the best general upper bound is h(t) = O(t log log t) via Delcourt–Postle. Even the t=3 case (asking whether every K_3-minor-free hypergraph is 3-colorable) is open, with a gap between the lower bound of 3 and the best known upper bound of 4. No follow-up paper resolving the full conjecture was found in a wide literature search.

 Reviewer notes. The paper was first posted June 2022 and published in European Journal of Combinatorics in 2024 (ScienceDirect doi:10.1016/j.ejc.2024.…). The conjecture is proven for the special case of hypergraphs with independence number ≤ 2, and for t ∈ {2,3,4,5,6} the bound χ(H) ≤ 2t-2 holds. The t=3 case (Problem 1 in the paper) is the most immediate open question. No citing paper resolving the conjecture was found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every integer $t\geq 2$ we have $h(t)=\left\lceil\frac{3}{2}(t-1)\right\rceil$. In other words, if a hypergraph $H$ does not contain $K_{t}$ as a minor, then $\chi(H)\leq\left\lceil\frac{3}{2}(t-1)\right\rceil$.

Context

The function $h(t)$ is the smallest integer such that every $K_t$-minor-free hypergraph is $h(t)$-colorable. The paper proves the lower bound $h(t)\geq\left\lceil\frac{3}{2}(t-1)\right\rceil$ by an explicit construction, and conjectures this lower bound is tight. The conjecture remains open even for $t=3$, where the best known upper bound is $4$.

Source paper

 Coloring hypergraphs with excluded minors
 Raphael Steiner · 2024-04-19
 https://arxiv.org/abs/2206.13635

Related conjectures

 
 implies
 3-colorability of K₃-minor-free hypergraphs
 open
 Pure restriction: setting t = 3 in the conjecture h(t) = ceil(3(t-1)/2) gives h(3) = ceil(3) = 3, i.e. every K_3-minor-free hypergraph is 3-colorable, which is verbatim the target problem. The relation is also explicitly stated in the provided context of the target: 'Problem 1 isolates the smallest open case of Conjecture 2' (both from the same paper, arXiv:2206.13635). The converse fails (t = 3 says nothing about larger t), so the relation is a strict implication, source stronger than target.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:Hadwiger's conjecture, among the most famous open problems in graph theory, states that every graph that does not contain $K_t$ as a minor is properly $(t-1)$-colorable. The purpose of this work is to demonstrate that a natural extension of Hadwiger's problem to hypergraph coloring exists, and to derive some first partial results and applications. Generalizing ordinary graph minors to hypergraphs, we say that a hypergraph $H_1$ is a minor of a hypergraph $H_2$, if a hypergraph isomorphic to $H_1$ can be obtained from $H_2$ via a finite sequence of vertex- and hyperedge-deletions, and hyperedge contractions. We first show that a weak extension of Hadwiger's conjecture to hypergraphs holds true: For every $t \ge 1$, there exists a finite (smallest) integer $h(t)$ such that every hypergraph with no $K_t$-minor is $h(t)$-colorable, and we prove $$\left\lceil\frac{3}{2}(t-1)\right\rceil \le h(t) \le 2g(t)$$ where $g(t)$ denotes the maximum chromatic number of graphs with no $K_t$-minor. Using the recent result by Delcourt and Postle that $g(t)=O(t \log \log t)$, this yields $h(t)=O(t \log \log t)$. We further conjecture that $h(t)=\left\lceil\frac{3}{2}(t-1)\right\rceil$, i.e., that every hypergraph with no $K_t$-minor is $\left\lceil\frac{3}{2}(t-1)\right\rceil$-colorable for all $t \ge 1$, and prove this conjecture for all hypergraphs with independence number at most $2$. By considering special classes of hypergraphs, the above additionally has some interesting applications for ordinary graph coloring, such as:
-graphs of chromatic number $C k t \log \log t$ contain $K_t$-minors with $k$-edge-connected branch-sets,
-graphs of chromatic number $C q t \log \log t$ contain $K_t$-minors with modulo-$q$-connected branch sets,
-by considering cycle hypergraphs of digraphs we recover known results on strong minors in digraphs of large dichromatic number as special cases.
 

 
 
 
 Comments:
 15 pages, Final version, revised according to the reviewer's comments
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15, 05C20, 05C65, 05C83
 

 Cite as:
 arXiv:2206.13635 [math.CO]
 

 
  
 (or 
 arXiv:2206.13635v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2206.13635
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Mon, 27 Jun 2022 21:22:34 UTC (19 KB)

 [v2]
 Mon, 18 Jul 2022 08:58:41 UTC (19 KB)

 [v3]
 Fri, 19 Apr 2024 07:40:44 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Coloring hypergraphs with excluded minors, by Raphael Steiner
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
