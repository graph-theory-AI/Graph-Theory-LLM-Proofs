Attack the following open graph-theory problem.

Catalog id: 2208.10074__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2208.10074__01/
Source paper: Product structure of graph classes with strongly sublinear separators (arXiv:2208.10074)

=== Extracted statement (catalog JSON) ===
Title: Open Problem 6
For any hereditary graph class $\mathcal{G}$ with separation-number $\operatorname{sep}(\mathcal{G})\in O(n^{1-\epsilon})$, does there exist a constant $c=c(\mathcal{G})$ such that every $n$-vertex graph $G\in\mathcal{G}$ is contained in $H\boxtimes K_m$, where $\operatorname{tw}(H)\leqslant c$ and $m\in O(n^{1-\epsilon})$.

Context:
Open Problem 6 is the only explicitly labeled open-problem environment in the paper (LaTeX environment type [open]). It appears between Theorem 5 and Theorem 7, in the context of product structure theory for graph classes with strongly sublinear separators.

=== Catalog page (statement + literature review) ===
Product structure open problem for sublinear separators — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Open Problem 6 asks whether for any hereditary graph class \mathcal{G} with \operatorname{sep}(\mathcal{G}) \in O(n^{1-\varepsilon}), there exists a constant c = c(\mathcal{G}) such that every n-vertex graph G \in \mathcal{G} is contained in H \boxtimes K_m where \operatorname{tw}(H) \leq c and m \in O(n^{1-\varepsilon}). The source paper itself already confirms the answer affirmatively for graphs excluding a fixed minor (Theorem 7, citing Distel et al. 2022). The 2024 paper by Liu, Norin, and Wood (arXiv:2410.20333) further extends this to graphs excluding a fixed odd minor. The general hereditary case with strongly sublinear separators remains open.

 Cited literature (1)

 
 
 
partial Product Structure and Tree-Decompositions
 (2024)
 

 
 Chun-Hung Liu, Sergey Norin, David R. Wood · arXiv preprint · arXiv:2410.20333

Proves that graphs excluding a fixed odd minor are contained in the strong product of two graphs each with bounded treewidth, extending partial progress on Open Problem 6 to odd-minor-free hereditary classes (which have strongly sublinear separators).
 

 

 Reviewer notes. Open Problem 6 is already partially resolved within the source paper itself for excluded-minor classes (Theorem 7). Post-publication, arXiv:2410.20333 adds partial progress for odd-minor-free classes. No paper was found resolving the general hereditary case. Confidence is medium rather than high because the problem is ~3 years old and there may be further progress not surfaced by these searches.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. For any hereditary graph class $\mathcal{G}$ with separation-number $\operatorname{sep}(\mathcal{G})\in O(n^{1-\epsilon})$, does there exist a constant $c=c(\mathcal{G})$ such that every $n$-vertex graph $G\in\mathcal{G}$ is contained in $H\boxtimes K_m$, where $\operatorname{tw}(H)\leqslant c$ and $m\in O(n^{1-\epsilon})$.

Context

Open Problem 6 is the only explicitly labeled open-problem environment in the paper (LaTeX environment type [open]). It appears between Theorem 5 and Theorem 7, in the context of product structure theory for graph classes with strongly sublinear separators.

Source paper

 Product structure of graph classes with strongly sublinear separators
 Zdeněk Dvořák, David R. Wood · 2023-09-27
 https://arxiv.org/abs/2208.10074

=== Source paper abstract / header ===
Abstract:We investigate the product structure of hereditary graph classes admitting strongly sublinear separators. We characterise such classes as subgraphs of the strong product of a star and a complete graph of strongly sublinear size. In a more precise result, we show that if any hereditary graph class $\mathcal{G}$ admits $O(n^{1-\epsilon})$ separators, then for any fixed $\delta\in(0,\epsilon)$ every $n$-vertex graph in $\mathcal{G}$ is a subgraph of the strong product of a graph $H$ with bounded tree-depth and a complete graph of size $O(n^{1-\epsilon+\delta})$. This result holds with $\delta=0$ if we allow $H$ to have tree-depth $O(\log\log n)$. Moreover, using extensions of classical isoperimetric inequalties for grids graphs, we show the dependence on $\delta$ in our results and the above $\text{td}(H)\in O(\log\log n)$ bound are both best possible. We prove that $n$-vertex graphs of bounded treewidth are subgraphs of the product of a graph with tree-depth $t$ and a complete graph of size $O(n^{1/t})$, which is best possible. Finally, we investigate the conjecture that for any hereditary graph class $\mathcal{G}$ that admits $O(n^{1-\epsilon})$ separators, every $n$-vertex graph in $\mathcal{G}$ is a subgraph of the strong product of a graph $H$ with bounded tree-width and a complete graph of size $O(n^{1-\epsilon})$. We prove this for various classes $\mathcal{G}$ of interest.
 

 
 
 
 Comments:
 v2: added bad news subsection; v3: removed section "Polynomial Expansion Classes" which had an error, added section "Lower Bounds", and added a new author; v4: minor revisions and corrections;
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2208.10074 [math.CO]
 

 
  
 (or 
 arXiv:2208.10074v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2208.10074
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: David Wood [view email] 
 [v1]
 Mon, 22 Aug 2022 06:18:53 UTC (27 KB)

 [v2]
 Thu, 25 Aug 2022 03:43:51 UTC (28 KB)

 [v3]
 Mon, 7 Aug 2023 06:21:38 UTC (41 KB)

 [v4]
 Wed, 27 Sep 2023 23:53:39 UTC (41 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Product structure of graph classes with strongly sublinear separators, by Zden\v{e}k Dvo\v{r}\'ak and David R. Wood
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
 | 2022-08
 

 Change to browse by:
 
 cs
 cs.DM
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
