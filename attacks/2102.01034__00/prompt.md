Attack the following open graph-theory problem.

Catalog id: 2102.01034__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2102.01034__00/
Source paper: On the dichromatic number of surfaces (arXiv:2102.01034)

=== Catalog page (statement + literature review) ===
Complexity of Σ-k-dicolourability k∈{4,5} — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 4.4 from arXiv:2102.01034 asks for the computational complexity of \Sigma-k-DICOLOURABILITY for k \in {4, 5} and \Sigma different from the sphere; the source paper establishes NP-completeness for k=2 and polynomial-time solvability for k \geq 6, leaving the intermediate cases k=4 and k=5 explicitly open. A wide literature search found no follow-up paper that resolves (or even substantially advances) this complexity question for either value of k on any non-spherical surface. The problem remains open as of May 2026.

 Reviewer notes. No follow-up found. Five web calls were used (2 WebSearch + 3 WebFetch). The paper was published in the Electronic Journal of Combinatorics (2022, v29i1p30). The open problem is sandwiched between the known NP-complete case k=2 and the known polynomial-time case k>=6; resolving k in {4,5} likely requires new structural insight into digraphs on surfaces. The thesis 'Digraph colouring' (HAL tel-04633967, 2024) appeared in the search but was access-denied; it may contain partial progress and warrants manual inspection.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the complexity of $\Sigma$-$k$-\textsc{Dicolourability} for $k \in \{4, 5\}$ and $\Sigma$ different from the sphere?

Context

The paper establishes that Σ-2-DICOLOURABILITY is NP-complete for any surface, and that Σ-k-DICOLOURABILITY is polynomial-time solvable for any surface Σ and any integer k ≥ 6. The complexity for k ∈ {4, 5} on surfaces other than the sphere is explicitly left open.

Notes. Problem 4.4 is referenced in the introduction but the full text of Section 4 was not present in the PDF extraction; the statement is inferred from the surrounding context.

Source paper

 On the dichromatic number of surfaces
 Pierre Aboulker, Frédéric Havet, Kolja Knauer, Clément Rambaud · 2021-11-16
 https://arxiv.org/abs/2102.01034
 PDF source

=== Source paper abstract / header ===
Abstract:In this paper, we give bounds on the dichromatic number $\vec{\chi}(\Sigma)$ of a surface $\Sigma$, which is the maximum dichromatic number of an oriented graph embeddable on $\Sigma$. We determine the asymptotic behaviour of $\vec{\chi}(\Sigma)$ by showing that there exist constants $a_1$ and $a_2$ such that, $a_1\frac{\sqrt{-c}}{\log(-c)} \leq \vec{\chi}(\Sigma) \leq a_2 \frac{\sqrt{-c}}{\log(-c)} $ for every surface $\Sigma$ with Euler characteristic $c\leq -2$. We then give more explicit bounds for some surfaces with high Euler characteristic. In particular, we show that the dichromatic numbers of the projective plane $\mathbb{N}_1$, the Klein bottle $\mathbb{N}_2$, the torus $\mathbb{S}_1$, and Dyck's surface $\mathbb{N}_3$ are all equal to $3$, and that the dichromatic numbers of the $5$-torus $\mathbb{S}_5$ and the $10$-cross surface $\mathbb{N}_{10}$ are equal to $4$. We also consider the complexity of deciding whether a given digraph or oriented graph embeddable on a fixed surface is $k$-dicolourable. In particular, we show that for any fixed surface, deciding whether a digraph embeddable on this surface is $2$-dicolourable is NP-complete, and that deciding whether a planar oriented graph is $2$-dicolourable is NP-complete unless all planar oriented graphs are $2$-dicolourable (which was conjectured by Neumann-Lara).
 

 
 
 
 Comments:
 26 pages, 5 figures, improved asymptotic bounds
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2102.01034 [math.CO]
 

 
  
 (or 
 arXiv:2102.01034v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2102.01034
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Kolja Knauer [view email] 
 [v1]
 Mon, 1 Feb 2021 18:12:13 UTC (59 KB)

 [v2]
 Thu, 4 Feb 2021 11:47:42 UTC (59 KB)

 [v3]
 Tue, 16 Nov 2021 16:33:39 UTC (59 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the dichromatic number of surfaces, by Pierre Aboulker and 3 other authors
View PDF
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
 | 2021-02
 

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
