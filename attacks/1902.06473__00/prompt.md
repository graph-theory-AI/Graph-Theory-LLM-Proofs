Attack the following open graph-theory problem.

Catalog id: 1902.06473__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1902.06473__00/
Source paper: Information-theoretic lower bounds for quantum sorting (arXiv:1902.06473)

=== Catalog page (statement + literature review) ===
LB and QLB constant-factor equivalence for posets — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The conjecture posits that the classical lower bound LB(P) = n(ln n - H(P)) and the quantum lower bound QLB(P) = n(H_n - QH(P)) for sorting under partial information are within a constant factor of each other for all posets P, where H(P) is the entropy and QH(P) is its averaged variant. The source paper (arXiv:1902.06473) itself proves the conjecture for a wide class of posets (including series-parallel posets), improving on Yao's 2004 result, but the full conjecture for arbitrary posets remains open. No follow-up paper resolving the full conjecture was found in searches covering the period 2019–2026.

 Reviewer notes. The paper itself establishes QLB(P) >= c * LB(P) for series-parallel posets (and more generally for a wide class of posets), which is a partial result toward the full conjecture. The conjecture that LB(P) and QLB(P) are within a constant factor for ALL posets appears to remain open. The PDF source was not machine-readable for full text extraction; the conjecture statement in the input is noted as partially corrupted. No follow-up paper settling the full conjecture was found in four targeted web searches.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. The two lower bounds $\mathrm{LB}(P)$ and $\mathrm{QLB}(P)$ are within a constant factor of each other for all posets $P$.

Context

In the Conclusion, the authors present a table comparing the classical quantity $\mathrm{LB}(P) = n(\ln n - H(P))$ and the quantum quantity $\mathrm{QLB}(P) = n(H_n - QH(P))$, where $H(P) = \min_{z \in C(P)} h(z)$ is the entropy and $QH(P) = \mathbb{E}_{z \in C(P)}[h(z)]$ is its averaged variant. The authors state their findings support a conjecture relating these two bounds, but the remainder of the statement is corrupted in the PDF source.

Notes. PDF source — the statement is truncated after 'QLB(P)' and replaced with garbled content (a list of arXiv IDs). The statement above is inferred from context; the exact formulation cannot be verified.

Source paper

 Information-theoretic lower bounds for quantum sorting
 Jean Cardinal, Gwenaël Joret, Jérémie Roland · 2019-02-18
 https://arxiv.org/abs/1902.06473
 PDF source

=== Source paper abstract / header ===
Abstract:We analyze the quantum query complexity of sorting under partial information. In this problem, we are given a partially ordered set $P$ and are asked to identify a linear extension of $P$ using pairwise comparisons. For the standard sorting problem, in which $P$ is empty, it is known that the quantum query complexity is not asymptotically smaller than the classical information-theoretic lower bound. We prove that this holds for a wide class of partially ordered sets, thereby improving on a result from Yao (STOC'04).
 

 
 
 
 Subjects:
 
 Computational Complexity (cs.CC); Data Structures and Algorithms (cs.DS); Combinatorics (math.CO); Quantum Physics (quant-ph)
 

 Cite as:
 arXiv:1902.06473 [cs.CC]
 

 
  
 (or 
 arXiv:1902.06473v1 [cs.CC] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1902.06473
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Jean Cardinal [view email] 
 [v1]
 Mon, 18 Feb 2019 09:16:43 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Information-theoretic lower bounds for quantum sorting, by Jean Cardinal and 2 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.CC

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2019-02
 

 Change to browse by:
 
 cs
 cs.DS
 math
 math.CO
 quant-ph
 

 

 

 
 References & Citations

 
 
 INSPIRE HEP

 

 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Jean Cardinal
Gwenaël Joret
Jérémie Roland 

 

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
