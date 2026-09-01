Attack the following open graph-theory problem.

Catalog id: 1803.05396__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1803.05396__00/
Source paper: $H$-colouring $P_t$-free graphs in subexponential time (arXiv:1803.05396)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: Complexity of 3-colourability of $P_t$-free graphs
Determine the complexity of $3$-colourability of $P_t$-free graphs for $t \geq 8$.

Context:
Polynomial-time algorithms for 3-colourability of $P_t$-free graphs are known for $t \leq 7$ (combining results for $t \leq 5$, $(k,t)=(3,7)$, and hardness for $P_7$-free graphs). The paper notes this problem remains open for $t \geq 8$, and provides a subexponential-time algorithm as partial progress.

=== Catalog page (statement + literature review) ===
3-colourability complexity of P_t-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The open problem asks to determine whether 3-colourability of $P_t$-free graphs (for $t \geq 8$) can be decided in polynomial time or is NP-hard; the question is not settled. The subexponential-time algorithm of the source paper was significantly improved to quasi-polynomial time $n^{\mathcal{O}(\log^2 n)}$ by Pilipczuk, Pilipczuk, and Rz\k{a}\.zewski (2020), using techniques from Independent Set in $P_t$-free graphs. A 2025 paper by Zhou, Zhong, and Huang establishes a polynomial-time algorithm for the restricted class $\mathcal{G}_{10,7}$ ($P_{10}$-free graphs with all induced odd cycles of the same length 7), but the full complexity boundary for $t \geq 8$ remains open.

 Cited literature (2)

 
 
 
partial Quasi-polynomial-time algorithm for Independent Set in $P_t$-free graphs via shrinking the space of induced paths
 (2020)
 

 
 Marcin Pilipczuk, Michał Pilipczuk, Paweł Rzążewski · arXiv preprint · arXiv:2009.13494

Extends the quasi-polynomial-time Independent Set framework to 3-Coloring of $P_t$-free graphs, achieving runtime $n^{\mathcal{O}(\log^2 n)}$, a major improvement over the subexponential bound of the source paper.
 

 
 
partial 3-Coloring $P_t$-Free Graphs With Only One Prescribed Induced Odd Cycle Length
 (2025)
 

 
 Yidong Zhou, Mingxian Zhong, Shenwei Huang · arXiv preprint · arXiv:2512.06367

Gives a polynomial-time algorithm for 3-coloring graphs in $\mathcal{G}_{10,7}$ (the class of $P_{10}$-free graphs whose induced odd cycles all have length exactly 7), extending polynomial tractability to a new subclass.
 

 

 Reviewer notes. Polynomial-time solvability vs.~NP-hardness for 3-colourability of $P_t$-free graphs with $t \geq 8$ remains open. The strongest known upper bound is quasi-polynomial time $n^{\mathcal{O}(\log^2 n)}$ (Pilipczuk et al., 2020), improving the subexponential bound of Conjecture 1803.05396. Polynomial-time results exist only for restricted subclasses (e.g., $\mathcal{G}_{10,7}$). No NP-hardness result for any fixed $t \geq 8$ is known.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the complexity of $3$-colourability of $P_t$-free graphs for $t \geq 8$.

Context

Polynomial-time algorithms for 3-colourability of $P_t$-free graphs are known for $t \leq 7$ (combining results for $t \leq 5$, $(k,t)=(3,7)$, and hardness for $P_7$-free graphs). The paper notes this problem remains open for $t \geq 8$, and provides a subexponential-time algorithm as partial progress.

Notes. Stated as background open problem in prose without a labelled environment and without an explicit citation; PDF source — the inequality sign $\geq$ was dropped in extraction and has been reconstructed from context.

Source paper

 $H$-colouring $P_t$-free graphs in subexponential time
 Carla Groenland, Karolina Okrasa, Pawel Rzążewski, Alex Scott, Paul Seymour, Sophie Spirkl · 2019-03-22
 https://arxiv.org/abs/1803.05396
 PDF source

=== Source paper abstract / header ===
Abstract:A graph is called $P_t$-free if it does not contain the path on $t$ vertices as an induced subgraph. Let $H$ be a multigraph with the property that any two distinct vertices share at most one common neighbour. We show that the generating function for (list) graph homomorphisms from $G$ to $H$ can be calculated in subexponential time $2^{O\left(\sqrt{tn\log(n)}\right)}$ for $n=|V(G)|$ in the class of $P_t$-free graphs $G$. As a corollary, we show that the number of 3-colourings of a $P_t$-free graph $G$ can be found in subexponential time. On the other hand, no subexponential time algorithm exists for 4-colourability of $P_t$-free graphs assuming the Exponential Time Hypothesis. Along the way, we prove that $P_t$-free graphs have pathwidth that is linear in their maximum degree.
 

 
 
 
 Comments:
 Fixed some typo's
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1803.05396 [cs.DM]
 

 
  
 (or 
 arXiv:1803.05396v3 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1803.05396
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Carla Groenland [view email] 
 [v1]
 Wed, 14 Mar 2018 16:45:27 UTC (10 KB)

 [v2]
 Thu, 10 May 2018 07:18:57 UTC (13 KB)

 [v3]
 Fri, 22 Mar 2019 15:33:04 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled $H$-colouring $P_t$-free graphs in subexponential time, by Carla Groenland and Karolina Okrasa and Pawel Rz\k{a}\.zewski and Alex Scott and Paul Seymour and Sophie Spirkl
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2018-03
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Carla Groenland
Alex Scott 

 

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
