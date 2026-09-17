Attack the following open graph-theory problem.

Catalog id: 1806.00541__00
Catalog status: open (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1806.00541__00/
Source paper: Extension Complexity of the Correlation Polytope (arXiv:1806.00541)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2
For every $n$-vertex graph $G$, the extension complexity of $\mathrm{COR}(G)$ is $2^{\Omega(\mathrm{tw}(G)+\log n)}$.

Context:
The authors prove the matching upper bound $2^{O(\mathrm{tw}(G)+\log n)}$ in Theorem 1 and conjecture that this is tight in general. If true, the conjecture would improve the bound of Göös, Jain and Watson ($2^{\Omega(n/\log n)}$ for the stable set polytope) to $2^{\Omega(n)}$, and would yield explicit 0/1-polytopes with extension complexity exponential in their dimension, as predicted by the counting argument of Rothvoß.

=== Catalog page (statement + literature review) ===
Treewidth-exponential extension complexity for correlation polytopes — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The source paper proves the matching upper bound 2^{O(tw(G)+log n)} for the extension complexity of COR(G) and establishes tightness for minor-closed graph classes, but Conjecture 2 — that 2^{Omega(tw(G)+log n)} holds for every n-vertex graph G — remains open in full generality. Five web searches spanning 2019–2026 found no follow-up paper proving or disproving the conjecture for arbitrary graphs. The conjecture would imply 2^{Omega(n)} extension complexity for the stable set polytope of dense graphs and explicit 0/1-polytopes with extension complexity exponential in their dimension.

 Reviewer notes. No follow-up found resolving Conjecture 2 in full generality. The paper does prove tightness for graphs in minor-closed classes (e.g. planar graphs), but the conjecture asks for all n-vertex graphs. The related Springer paper 'New limits of treewidth-based tractability in optimization' (Math. Program. 2021) could not be accessed but appears to address parameterized complexity limits rather than the exact conjecture. arXiv:2106.11945 (Smaller Extended Formulations for Spanning Tree Polytopes) is unrelated.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every $n$-vertex graph $G$, the extension complexity of $\mathrm{COR}(G)$ is $2^{\Omega(\mathrm{tw}(G)+\log n)}$.

Context

The authors prove the matching upper bound $2^{O(\mathrm{tw}(G)+\log n)}$ in Theorem 1 and conjecture that this is tight in general. If true, the conjecture would improve the bound of Göös, Jain and Watson ($2^{\Omega(n/\log n)}$ for the stable set polytope) to $2^{\Omega(n)}$, and would yield explicit 0/1-polytopes with extension complexity exponential in their dimension, as predicted by the counting argument of Rothvoß.

Notes. The paper proves this conjecture for the special case of proper minor-closed graph classes (Theorem 3), but the general statement remains open.

Source paper

 Extension Complexity of the Correlation Polytope
 Pierre Aboulker, Samuel Fiorini, Tony Huynh, Marco Macchia, Johanna Seif · 2018-10-18
 https://arxiv.org/abs/1806.00541
 PDF source

=== Source paper abstract / header ===
Abstract:We prove that for every $n$-vertex graph $G$, the extension complexity of the correlation polytope of $G$ is $2^{O(\mathrm{tw}(G) + \log n)}$, where $\mathrm{tw}(G)$ is the treewidth of $G$. Our main result is that this bound is tight for graphs contained in minor-closed classes.
 

 
 
 
 Comments:
 7 pages, 7 figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Computational Complexity (cs.CC)
 
 
 MSC classes:
 05C83, 90C27
 

 Cite as:
 arXiv:1806.00541 [cs.DM]
 

 
  
 (or 
 arXiv:1806.00541v2 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1806.00541
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Marco Macchia [view email] 
 [v1]
 Fri, 1 Jun 2018 20:59:09 UTC (13 KB)

 [v2]
 Thu, 18 Oct 2018 12:48:33 UTC (13 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Extension Complexity of the Correlation Polytope, by Pierre Aboulker and 4 other authors
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
 | 2018-06
 

 Change to browse by:
 
 cs
 cs.CC
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Pierre Aboulker
Samuel Fiorini
Tony Huynh
Marco Macchia
Johanna Seif 

 

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
