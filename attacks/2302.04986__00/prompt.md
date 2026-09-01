Attack the following open graph-theory problem.

Catalog id: 2302.04986__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2302.04986__00/
Source paper: Hitting all maximum stable sets in $P_5$-free graphs (arXiv:2302.04986)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.8
For every forest $H$, there exists a function $f:\mathbb{N}\rightarrow\mathbb{N}$ such that every $H$-free graph $G$ satisfies $\eta(G)\leq f(\omega(G))$.

Context:
Proposed as an analogue of the Gyárfás–Sumner conjecture ($\chi$-boundedness) for $\eta$-boundedness: just as $H$-free graphs are conjectured to be $\chi$-bounded for every forest $H$, the authors conjecture the same for $\eta$-boundedness. The paper proves this conjecture for an assortment of special forests, including stars and paths $P_t$ with $t\leq 5$.

=== Catalog page (statement + literature review) ===
η-boundedness for H-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Conjecture 1.8 proposes that for every forest $H$, the class of $H$-free graphs is $\eta$-bounded (i.e., $\eta(G) \leq f(\omega(G))$), by analogy with the Gyárfás–Sumner conjecture for $\chi$-boundedness. The source paper proves it for stars, subdivided stars, and $P_t$ for $t \leq 5$. A subsequent paper in the Electronic Journal of Combinatorics (2025) extends $\eta$-boundedness to graphs without large induced matchings ($tK_2$-free), resolving a related conjecture from the source paper and adding another family of forests for which the conjecture holds. The full conjecture for all forests $H$ remains open, and the case of $P_t$-free graphs for $t \geq 6$ is explicitly listed as open.

 Cited literature (1)

 
 
 
partial Piercing Independent Sets in Graphs without Large Induced Matching
 (2025)
 

 
 unknown (not retrieved within web-call budget) · Electronic Journal of Combinatorics

Proves that any graph $G$ without induced matching of size $t$ satisfies $\eta(G) \leq \omega(G)^{3t-3+o(1)}$, resolving a conjecture of Hajebi, Li, and Spirkl from the source paper and establishing $\eta$-boundedness for $tK_2$-free graphs, a special case of Conjecture 1.8.
 

 

 Reviewer notes. The EJC paper (v32i1p10, verified via WebFetch) resolves a specific conjecture from the source paper about graphs without large induced matchings ($tK_2$-free), adding a new forest family to the confirmed cases. Author list and arxiv ID for this EJC paper were not retrievable within the 5-call budget. The full Conjecture 1.8 for all forests $H$ remains open; $P_t$-free graphs for $t \geq 6$ are explicitly open per the source paper.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every forest $H$, there exists a function $f:\mathbb{N}\rightarrow\mathbb{N}$ such that every $H$-free graph $G$ satisfies $\eta(G)\leq f(\omega(G))$.

Context

Proposed as an analogue of the Gyárfás–Sumner conjecture ($\chi$-boundedness) for $\eta$-boundedness: just as $H$-free graphs are conjectured to be $\chi$-bounded for every forest $H$, the authors conjecture the same for $\eta$-boundedness. The paper proves this conjecture for an assortment of special forests, including stars and paths $P_t$ with $t\leq 5$.

Source paper

 Hitting all maximum stable sets in $P_5$-free graphs
 Sepehr Hajebi, Yanjia Li, Sophie Spirkl · 2024-01-16
 https://arxiv.org/abs/2302.04986

=== Source paper abstract / header ===
Abstract:We prove that every $P_5$-free graph of bounded clique number contains a small hitting set of all its maximum stable sets.
More generally, let us say a class $\mathcal{C}$ of graphs is $\eta$-bounded if there exists a function $h:\mathbb{N}\rightarrow \mathbb{N}$ such that $\eta(G)\leq h(\omega(G))$ for every graph $G\in \mathcal{C}$, where $\eta(G)$ denotes smallest cardinality of a hitting set of all maximum stable sets in $G$, and $\omega(G)$ is the clique number of $G$. Also, $\mathcal{C}$ is said to be polynomially $\eta$-bounded if in addition $h$ can be chosen to be a polynomial.
We introduce $\eta$-boundedness inspired by a question of Alon and motivated by a number of meaningful similarities to $\chi$-boundedness. In particular, we propose an analogue of the Gyárfás-Sumner conjecture, that the class of all $H$-free graphs is $\eta$-bounded if (and only if) $H$ is a forest. Like $\chi$-boundedness, the case where $H$ is a star is easy to verify, and we prove two non-trivial extensions of this: $H$-free graphs are $\eta$-bounded if (1) $H$ has a vertex incident with all edges of $H$, or (2) $H$ can be obtained from a star by subdividing at most one edge, exactly once.
Unlike $\chi$-boundedness, the case where $H$ is a path is surprisingly hard. Our main result mentioned at the beginning shows that $P_5$-free graphs are $\eta$-bounded. The proof is rather involved compared to the classical ``Gyárfás path'' argument which establishes, for all $t$, the $\chi$-boundedness of $P_t$-free graphs. It remains open whether $P_t$-free graphs are $\eta$-bounded for $t\geq 6$. It also remains open whether $P_5$-free graphs are polynomially $\eta$-bounded, which, if true, would imply the Erdős-Hajnal conjecture for $P_5$-free graphs. But we prove that $H$-free graphs are polynomially $\eta$-bounded if $H$ is a proper induced subgraph of $P_5$.
 

 
 
 
 Comments:
 [v2] Accepted manuscript; see DOI for journal version [v3] Fixed mistake in (16)
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2302.04986 [math.CO]
 

 
  
 (or 
 arXiv:2302.04986v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2302.04986
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Combinatorial Theory, Series B, Volume 165, March 2024, Pages 142-163
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.jctb.2023.11.005

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sophie Spirkl [view email] 
 [v1]
 Fri, 10 Feb 2023 00:15:45 UTC (21 KB)

 [v2]
 Wed, 29 Nov 2023 21:07:50 UTC (21 KB)

 [v3]
 Tue, 16 Jan 2024 19:19:19 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Hitting all maximum stable sets in $P_5$-free graphs, by Sepehr Hajebi and 2 other authors
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
 | 2023-02
 

 Change to browse by:
 
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
