Attack the following open graph-theory problem.

Catalog id: 1907.04585__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1907.04585__00/
Source paper: Quasi-polynomial time approximation schemes for the Maximum Weight Inde… (arXiv:1907.04585)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.3
For every forest $H$ of maximum degree at most three, MWIS admits a QPTAS and a subexponential-time algorithm in the class of graphs that do not contain any subdivision of $H$ as an induced subgraph.

Context:
Following Theorems 1.1 and 1.2, which establish QPTASes and subexponential-time algorithms for MWIS in $H$-free graphs where every component of $H$ is a path or a subdivided claw, the authors conjecture a broader generalization to all forests of maximum degree at most three and graphs excluding any subdivision of $H$ as an induced subgraph. The paper itself proves Conjecture 1.3 for $H$ being a forest with at most three vertices of degree three (with a $2^{O(|V(G)|^{40/41}\log|V(G)|)}$ subexponential bound), but the full generality remains open.

=== Catalog page (statement + literature review) ===
MWIS QPTAS in subdivision-of-forest-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.3 — that MWIS admits a QPTAS and a subexponential-time algorithm in graphs excluding any subdivision of a forest H of maximum degree at most three as an induced subgraph — remains open in full generality. The source paper itself proves the special case where H has at most three vertices of degree three. A 2024 STACS paper (Gartland et al.) extends polynomial-time tractability to sparse graphs (excluding a fixed biclique) with no long subdivided claws, which is a more restrictive setting and does not subsume the conjecture. A 2026 preprint (arXiv:2602.18317) extends QPTAS results to graphs with few independent long induced holes, a structurally different class. No verified follow-up fully resolves the conjecture.

 Reviewer notes. No follow-up paper fully resolving Conjecture 1.3 was found across 7 web calls (4 searches + 3 fetches). The related 2024 STACS paper (Max Weight Independent Set in Sparse Graphs with No Long Claws, LIPIcs STACS 2024:4) achieves polynomial-time results only in the additional presence of biclique-freeness, which is a different and more restrictive setting. The 2026 preprint arXiv:2602.18317 (Bonnet, Czyzewska, Masarik, M. Pilipczuk, Rzazewski) handles graphs with few independent long holes via induced-minor exclusion, not subdivision-of-forest exclusion. The conjecture is recent (effective publication 2023) and the absence of a resolution is consistent with the high difficulty of the problem.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every forest $H$ of maximum degree at most three, MWIS admits a QPTAS and a subexponential-time algorithm in the class of graphs that do not contain any subdivision of $H$ as an induced subgraph.

Context

Following Theorems 1.1 and 1.2, which establish QPTASes and subexponential-time algorithms for MWIS in $H$-free graphs where every component of $H$ is a path or a subdivided claw, the authors conjecture a broader generalization to all forests of maximum degree at most three and graphs excluding any subdivision of $H$ as an induced subgraph. The paper itself proves Conjecture 1.3 for $H$ being a forest with at most three vertices of degree three (with a $2^{O(|V(G)|^{40/41}\log|V(G)|)}$ subexponential bound), but the full generality remains open.

Source paper

 Quasi-polynomial time approximation schemes for the Maximum Weight Independent Set Problem in H-free graphs
 Maria Chudnovsky, Marcin Pilipczuk, Michał Pilipczuk, Stéphan Thomassé · 2023-11-14
 https://arxiv.org/abs/1907.04585
 PDF source

=== Source paper abstract / header ===
Abstract:In the Maximum Independent Set problem we are asked to find a set of pairwise nonadjacent vertices in a given graph with the maximum possible cardinality. In general graphs, this classical problem is known to be NP-hard and hard to approximate within a factor of $n^{1-\varepsilon}$ for any $\varepsilon > 0$. Due to this, investigating the complexity of Maximum Independent Set in various graph classes in hope of finding better tractability results is an active research direction.
In $H$-free graphs, that is, graphs not containing a fixed graph $H$ as an induced subgraph, the problem is known to remain NP-hard and APX-hard whenever $H$ contains a cycle, a vertex of degree at least four, or two vertices of degree at least three in one connected component. For the remaining cases, where every component of $H$ is a path or a subdivided claw, the complexity of Maximum Independent Set remains widely open, with only a handful of polynomial-time solvability results for small graphs $H$ such as $P_5$, $P_6$, the claw, or the fork.
We show that for every graph $H$ for which Maximum Independent Set is not known to be APX-hard and SUBEXP-hard in $H$-free graphs, the problem admits a quasi-polynomial time approximation scheme and a subexponential-time exact algorithm in this graph class. Our algorithm works also in the more general weighted setting, where the input graph is supplied with a weight function on vertices and we are maximizing the total weight of an independent set.
 

 
 
 
 Comments:
 v2: added results on subexponential algorithms, v3: revision after reviewers' remarks, v4: final version accepted at SICOMP
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:1907.04585 [cs.DS]
 

 
  
 (or 
 arXiv:1907.04585v4 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1907.04585
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Marcin Pilipczuk [view email] 
 [v1]
 Wed, 10 Jul 2019 09:21:33 UTC (302 KB)

 [v2]
 Thu, 23 Apr 2020 11:51:57 UTC (312 KB)

 [v3]
 Tue, 17 Oct 2023 12:20:25 UTC (306 KB)

 [v4]
 Tue, 14 Nov 2023 14:24:06 UTC (306 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Quasi-polynomial time approximation schemes for the Maximum Weight Independent Set Problem in H-free graphs, by Maria Chudnovsky and 3 other authors
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
 | 2019-07
 

 Change to browse by:
 
 cs
 cs.DM
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Maria Chudnovsky
Marcin Pilipczuk
Michal Pilipczuk
Stéphan Thomassé 

 

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
