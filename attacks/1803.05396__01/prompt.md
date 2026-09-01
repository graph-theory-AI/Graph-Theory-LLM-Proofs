Attack the following open graph-theory problem.

Catalog id: 1803.05396__01
Catalog status: partial (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1803.05396__01/
Source paper: $H$-colouring $P_t$-free graphs in subexponential time (arXiv:1803.05396)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: Polynomial-time maximum independent set on $P_t$-free graphs
Determine whether maximum independent set is decidable in polynomial time for $P_t$-free graphs for $t \geq 7$.

Context:
Subexponential-time algorithms for maximum independent set on $P_t$-free graphs were given by Brause and independently by Bascó, Marx and Tuza; the present paper extends the subexponential approach to a broader class of problems including maximum independent set, but polynomial-time decidability for $t \geq 7$ remains open.

=== Catalog page (statement + literature review) ===
Polynomial-time MIS on Pₜ-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture remains open in its full generality for all $t \geq 7$. The most significant post-2019 advance is the quasi-polynomial-time algorithm of Gartland and Lokshtanov (2020), which shows that Maximum Independent Set on $P_k$-free graphs can be solved in time $n^{O(k^2 \log^3 n)}$ for any fixed $k$, ruling out NP-completeness for any fixed path length. Polynomial-time results have been extended to $P_7$-free graphs with bounded clique number (ISAAC 2025), but polynomial-time solvability for general $P_t$-free graphs with $t \geq 7$ remains open.

 Cited literature (1)

 
 
 
partial Independent Set on $P_k$-Free Graphs in Quasi-Polynomial Time
 (2020)
 

 
 Peter Gartland, Daniel Lokshtanov · arXiv preprint · arXiv:2005.00690

Proves that Maximum Weight Independent Set on $P_k$-free graphs is solvable in quasi-polynomial time $n^{O(k^2 \log^3 n)}$ for any fixed $k$, providing the first conclusive evidence that the problem is not NP-complete for any fixed $k$ and representing the strongest known upper bound for $t \geq 7$.
 

 

 Reviewer notes. The quasi-polynomial-time result of Gartland--Lokshtanov (arxiv:2005.00690) is the main post-2019 advance directly relevant to this problem; it does not achieve polynomial time but establishes a clear barrier to NP-hardness. A 2025 ISAAC paper (DOI 10.4230/LIPIcs.ISAAC.2025.20, 'Sparse Induced Subgraphs in P_7-Free Graphs of Bounded Clique Number') extends polynomial-time solvability to P_7-free graphs with bounded clique number, but this paper's authors and arxiv ID could not be verified within the web-call budget. The polynomial-time open question for unrestricted P_t-free graphs with t >= 7 is thus confirmed open with high confidence.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine whether maximum independent set is decidable in polynomial time for $P_t$-free graphs for $t \geq 7$.

Context

Subexponential-time algorithms for maximum independent set on $P_t$-free graphs were given by Brause and independently by Bascó, Marx and Tuza; the present paper extends the subexponential approach to a broader class of problems including maximum independent set, but polynomial-time decidability for $t \geq 7$ remains open.

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
