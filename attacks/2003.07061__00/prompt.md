Attack the following open graph-theory problem.

Catalog id: 2003.07061__00
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2003.07061__00/
Source paper: The $ε$-$t$-Net Problem (arXiv:2003.07061)

=== Extracted statement (catalog JSON) ===
Title: The $\varepsilon$-$t$-Net Problem
How small are the smallest $\varepsilon$-$t$-nets for $H$? Can we compute them efficiently?

Context:
Given a finite hypergraph $H=(V,E)$, a positive integer $t$, and $\varepsilon\in(t/|V|,1)$, an $\varepsilon$-$t$-net is a family $S\subseteq\binom{V}{t}$ of $t$-element subsets of $V$ such that every hyperedge $e\in E$ with $|e|\geq\varepsilon|V|$ contains some $s\in S$. The problem generalises the classical $\varepsilon$-net problem ($t=1$) and the Mnet notion ($t=\Theta(\varepsilon|V|)$), and arises naturally in secret sharing and other combinatorial contexts.

=== Catalog page (statement + literature review) ===
ε-t-net size and computation — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The problem asks how small the smallest $\varepsilon$-$t$-nets for a hypergraph $H$ can be and whether they can be computed efficiently. The source paper proved existence of $\varepsilon$-$t$-nets of size $O((1+\log t)d/\varepsilon \cdot \log(1/\varepsilon))$ for VC-dimension-$d$ hypergraphs and $O(1/\varepsilon)$ for certain geometric classes; whether these bounds are tight and whether efficient algorithms exist in general remains open. A 2024 paper by Keller and Smorodinsky (arXiv:2311.13662, SoCG 2024) applies $\varepsilon$-$t$-nets as a tool to Zarankiewicz’s problem, extending the utility of the framework but not resolving the original minimization or algorithmic questions.

 Cited literature (1)

 
 
 
partial Zarankiewicz's problem via ε-t-nets
 (2024)
 

 
 Chaya Keller, Shakhar Smorodinsky · 40th International Symposium on Computational Geometry (LIPIcs SoCG 2024) · arXiv:2311.13662 · doi:10.4230/LIPIcs.SoCG.2024.66

Applies $\varepsilon$-$t$-nets as a tool to Zarankiewicz’s problem, obtaining a sharp $O(n)$ bound for intersection graphs of two families of pseudo-discs and an $O(n\log n/\log\log n)$ bound for axis-parallel rectangles, demonstrating the power of the $\varepsilon$-$t$-net framework but not resolving the original question on minimum net sizes.
 

 

 Reviewer notes. The ε-t-Net Problem is the core open problem of the paper; the specific questions on tight bounds for general hypergraphs and efficient computation remain unresolved. The journal version appeared in Discrete & Computational Geometry (2022), DOI 10.1007/s00454-022-00376-x. A 2024 SoCG paper by two of the original authors (Keller and Smorodinsky) uses ε-t-nets as a productive combinatorial tool for Zarankiewicz-type problems in geometry. No paper was found that directly proves or disproves optimal bounds for the general ε-t-net minimization problem.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. How small are the smallest $\varepsilon$-$t$-nets for $H$? Can we compute them efficiently?

Context

Given a finite hypergraph $H=(V,E)$, a positive integer $t$, and $\varepsilon\in(t/|V|,1)$, an $\varepsilon$-$t$-net is a family $S\subseteq\binom{V}{t}$ of $t$-element subsets of $V$ such that every hyperedge $e\in E$ with $|e|\geq\varepsilon|V|$ contains some $s\in S$. The problem generalises the classical $\varepsilon$-net problem ($t=1$) and the Mnet notion ($t=\Theta(\varepsilon|V|)$), and arises naturally in secret sharing and other combinatorial contexts.

Notes. Stated as an explicitly labelled Problem environment in Section 1.2. PDF source causes epsilon to render as (cid:15) throughout, but the statement itself is unambiguous.

Source paper

 The $ε$-$t$-Net Problem
 Noga Alon, Bruno Jartoux, Chaya Keller, Shakhar Smorodinsky, Yelena Yuditsky · 2020-03-16
 https://arxiv.org/abs/2003.07061
 PDF source

=== Source paper abstract / header ===
Abstract:We study a natural generalization of the classical $\epsilon$-net problem (Haussler--Welzl 1987), which we call the "$\epsilon$-$t$-net problem": Given a hypergraph on $n$ vertices and parameters $t$ and $\epsilon\geq \frac t n$, find a minimum-sized family $S$ of $t$-element subsets of vertices such that each hyperedge of size at least $\epsilon n$ contains a set in $S$. When $t=1$, this corresponds to the $\epsilon$-net problem.
We prove that any sufficiently large hypergraph with VC-dimension $d$ admits an $\epsilon$-$t$-net of size $O(\frac{ (1+\log t)d}{\epsilon} \log \frac{1}{\epsilon})$. For some families of geometrically-defined hypergraphs (such as the dual hypergraph of regions with linear union complexity), we prove the existence of $O(\frac{1}{\epsilon})$-sized $\epsilon$-$t$-nets.
We also present an explicit construction of $\epsilon$-$t$-nets (including $\epsilon$-nets) for hypergraphs with bounded VC-dimension. In comparison to previous constructions for the special case of $\epsilon$-nets (i.e., for $t=1$), it does not rely on advanced derandomization techniques. To this end we introduce a variant of the notion of VC-dimension which is of independent interest.
 

 
 
 
 Comments:
 This is the full version of the paper to appear in the Proceedings of the 36th International Symposium on Computational Geometry (SoCG 2020)
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Computational Geometry (cs.CG); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2003.07061 [cs.DM]
 

 
  
 (or 
 arXiv:2003.07061v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2003.07061
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 
 Related DOI:
 
 https://doi.org/10.1007/s00454-022-00376-x

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Yelena Yuditsky [view email] 
 [v1]
 Mon, 16 Mar 2020 07:47:15 UTC (108 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The $\epsilon$-$t$-Net Problem, by Noga Alon and 4 other authors
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
 | 2020-03
 

 Change to browse by:
 
 cs
 cs.CG
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Noga Alon
Chaya Keller
Shakhar Smorodinsky
Yelena Yuditsky 

 

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
