Attack the following open graph-theory problem.

Catalog id: 2307.02816__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2307.02816__01/
Source paper: The grid-minor theorem revisited (arXiv:2307.02816)

=== Extracted statement (catalog JSON) ===
Title: Question 2
Is there a function $f$ such that for every graph $X$ there exists a function $c$ such that for every positive integer $t$ and for every graph $G$ with $\operatorname{tw}(G)<t$ that does not contain $X$ as a topological minor, there exists a graph $H$ of treewidth at most $f(\operatorname{td}(X))$ such that $G\mathrel{\ooalign{\raise 0.75348pt\hbox{$\subset$}\cr\raise-3.87495pt\hbox{\scalebox{0.9}{$\sim$}}\cr}}H\boxtimes K_{c(t)}$?

Context:
This question asks whether Theorem 2 can be extended from the excluded-minor setting to the excluded-topological-minor setting. Campbell et al. proved a weaker version with $\operatorname{tw}(H)\leqslant|V(X)|$, and that bound is tight for complete graphs.

=== Catalog page (statement + literature review) ===
Topological-minor exclusion product structure — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Question 2 asks whether the main result of arXiv:2307.02816 (which holds in the excluded-minor setting) extends to the excluded-topological-minor setting, with the treewidth of H bounded by f(td(X)) rather than |V(X)|. Campbell et al. (arXiv:2206.02395) proved the weaker version with tw(H) ≤ |V(X)|, and that bound is tight for complete graphs. Subsequent product-structure work (arXiv:2410.20333, Liu–Norin–Wood 2024) addresses odd-minor-free graphs but not the topological-minor setting. No paper resolving Question 2 was found in the indexed literature as of May 2026.

 Reviewer notes. Campbell et al. (arXiv:2206.02395, published in Combinatorics Probability and Computing 2023) proved the topological-minor analogue with tw(H) ≤ |V(X)|; this bound is tight for complete graphs. The source paper's Theorem 2 achieves tw(H) ≤ f(td(X)) in the excluded-minor setting (not topological minor). The gap between |V(X)| and f(td(X)) in the topological-minor setting is the open question. No follow-up resolving this was found; arXiv:2410.20333 (Liu–Norin–Wood 2024) works in the minor and odd-minor settings only.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is there a function $f$ such that for every graph $X$ there exists a function $c$ such that for every positive integer $t$ and for every graph $G$ with $\operatorname{tw}(G)<t$ that does not contain $X$ as a topological minor, there exists a graph $H$ of treewidth at most $f(\operatorname{td}(X))$ such that $G\mathrel{\ooalign{\raise 0.75348pt\hbox{$\subset$}\cr\raise-3.87495pt\hbox{\scalebox{0.9}{$\sim$}}\cr}}H\boxtimes K_{c(t)}$?

Context

This question asks whether Theorem 2 can be extended from the excluded-minor setting to the excluded-topological-minor setting. Campbell et al. proved a weaker version with $\operatorname{tw}(H)\leqslant|V(X)|$, and that bound is tight for complete graphs.

Notes. The subgraph-isomorphism symbol uses \ooalign and is reproduced verbatim from the LaTeX source.

Source paper

 The grid-minor theorem revisited
 Vida Dujmović, Robert Hickingbotham, Jędrzej Hodor, Gweanël Joret, Hoang La, Piotr Micek, Pat Morin, Clément Rambaud, David R. Wood · 2023-07-06
 https://arxiv.org/abs/2307.02816

=== Source paper abstract / header ===
Abstract:We prove that for every planar graph $X$ of treedepth $h$, there exists a positive integer $c$ such that for every $X$-minor-free graph $G$, there exists a graph $H$ of treewidth at most $f(h)$ such that $G$ is isomorphic to a subgraph of $H\boxtimes K_c$. This is a qualitative strengthening of the Grid-Minor Theorem of Robertson and Seymour (JCTB 1986), and treedepth is the optimal parameter in such a result. As an example application, we use this result to improve the upper bound for weak coloring numbers of graphs excluding a fixed graph as a minor.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2307.02816 [math.CO]
 

 
  
 (or 
 arXiv:2307.02816v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2307.02816
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Combinatorica, 45/62, 2025
 

 
 
 Related DOI:
 
 https://doi.org/10.1007/s00493-025-00168-w

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Gwenaël Joret [view email] 
 [v1]
 Thu, 6 Jul 2023 07:20:44 UTC (1,239 KB)

 [v2]
 Mon, 1 Jun 2026 10:50:53 UTC (444 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The grid-minor theorem revisited, by Vida Dujmovi\'c and Robert Hickingbotham and J\k{e}drzej Hodor and Gwena\"el Joret and Hoang La and Piotr Micek and Pat Morin and Cl\'ement Rambaud and David R. Wood
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
 | 2023-07
 

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
