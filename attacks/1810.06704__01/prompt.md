Attack the following open graph-theory problem.

Catalog id: 1810.06704__01
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1810.06704__01/
Source paper: Colouring Graphs with Sparse Neighbourhoods: Bounds and Applications (arXiv:1810.06704)

=== Extracted statement (catalog JSON) ===
Title: Question 1.4
Let $G$ be a $\delta$-sparse graph. What is the largest $\varepsilon = \varepsilon(\delta)$ such that $\chi(G) \leq (1-\varepsilon)(\Delta+1)$?

Context:
This isolates the second step in the King–Reed proof: given neighbourhood sparsity, bound the chromatic number below $\Delta+1$. Molloy–Reed obtained $\varepsilon(\delta)\approx 0.0238\delta$ and Bruhn–Joos improved to $\approx 0.1827\delta - 0.0778\delta^{3/2}$; the paper further improves this using an iterative naive colouring procedure.

=== Catalog page (statement + literature review) ===
Optimal ε for sparse-neighbourhood chromatic bound — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The exact optimal function ε(δ) characterising the best chromatic bound for δ-sparse graphs remains unknown. Hurley, de Joannis de Verclos, and Kang (arXiv:2007.07874, Advances in Combinatorics 2022) directly improved the lower bound on ε(δ) via an iterated colouring procedure for graphs of bounded local density (the same σ-sparse setting), claiming their leading term is asymptotically optimal as σ→0 and surpassing the Bonamy–Perrett–Postle bound. No paper has determined the exact value of ε(δ) for any specific δ > 0.

 Cited literature (1)

 
 
 
partial An improved procedure for colouring graphs of bounded local density
 (2022)
 

 
 Eoin Hurley, Rémi de Joannis de Verclos, Ross J. Kang · Advances in Combinatorics · arXiv:2007.07874

Improves the lower bound on ε(σ) for σ-sparse (equivalently δ-sparse) graphs, obtaining a leading term claimed asymptotically optimal as σ→0, and simultaneously improving Reed's conjecture ε from 1/26 to 0.119 and the strong chromatic index bound from 1.835Δ² to 1.772Δ².
 

 

 Reviewer notes. Question 1.4 is a quantitative optimisation question (find the exact ε(δ)), not a yes/no conjecture; it cannot be 'solved' until the exact function is determined. The Hurley–de Joannis de Verclos–Kang paper (2007.07874) is the clearest post-2018 follow-up on the same sparse-neighbourhood colouring framework and improves the bound, but leaves the exact ε(δ) open. The Dhawan paper (2403.03054) studies (k,r)-locally-sparse graphs, a different sparsity notion not directly relevant to this question.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Let $G$ be a $\delta$-sparse graph. What is the largest $\varepsilon = \varepsilon(\delta)$ such that $\chi(G) \leq (1-\varepsilon)(\Delta+1)$?

Context

This isolates the second step in the King–Reed proof: given neighbourhood sparsity, bound the chromatic number below $\Delta+1$. Molloy–Reed obtained $\varepsilon(\delta)\approx 0.0238\delta$ and Bruhn–Joos improved to $\approx 0.1827\delta - 0.0778\delta^{3/2}$; the paper further improves this using an iterative naive colouring procedure.

Notes. PDF source; statement is clearly readable.

Source paper

 Colouring Graphs with Sparse Neighbourhoods: Bounds and Applications
 Marthe Bonamy, Thomas Perrett, Luke Postle · 2018-10-15
 https://arxiv.org/abs/1810.06704
 PDF source

=== Source paper abstract / header ===
Abstract:Let $G$ be a graph with chromatic number $\chi$, maximum degree $\Delta$ and clique number $\omega$. Reed's conjecture states that $\chi \leq \lceil (1-\varepsilon)(\Delta + 1) + \varepsilon\omega \rceil$ for all $\varepsilon \leq 1/2$. It was shown by King and Reed that, provided $\Delta$ is large enough, the conjecture holds for $\varepsilon \leq 1/130,000$. In this article, we show that the same statement holds for $\varepsilon \leq 1/26$, thus making a significant step towards Reed's conjecture. We derive this result from a general technique to bound the chromatic number of a graph where no vertex has many edges in its neighbourhood. Our improvements to this method also lead to improved bounds on the strong chromatic index of general graphs. We prove that $\chi'_s(G)\leq 1.835 \Delta(G)^2$ provided $\Delta(G)$ is large enough.
 

 
 
 
 Comments:
 Submitted for publication in July 2016
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:1810.06704 [math.CO]
 

 
  
 (or 
 arXiv:1810.06704v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1810.06704
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Marthe Bonamy [view email] 
 [v1]
 Mon, 15 Oct 2018 21:27:19 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Colouring Graphs with Sparse Neighbourhoods: Bounds and Applications, by Marthe Bonamy and 2 other authors
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
 | 2018-10
 

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
