Attack the following open graph-theory problem.

Catalog id: 2502.05289__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2502.05289__00/
Source paper: Induced Disjoint Paths Without an Induced Minor (arXiv:2502.05289)

=== Catalog page (statement + literature review) ===
Subcubic H-ISC planarity dichotomy — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.5 from arXiv:2502.05289 proposes that for any subcubic graph $H$, the $H$-ISC problem (detecting $H$ as an induced subdivision) is in $\mathsf{P}$ if and only if $H$ is planar. The source paper provides the key hardness evidence: it exhibits a specific non-planar subcubic graph $H$ for which $H$-ISC is NP-complete (Theorem 3, also appearing as LIPIcs.ICALP.2025.4). No follow-up paper resolving or substantially advancing the full conjecture was found in the literature indexed as of May 2026.

 Reviewer notes. The conjecture is supported by the paper's own main result (NP-completeness for a specific non-planar subcubic H) and known polynomial algorithms for planar cases (net, K_4). The ICALP 2025 published version (LIPIcs vol. 334) numbers this as Conjecture 5.1 rather than 1.5. No follow-up resolving the full if-and-only-if characterization was found across three targeted searches.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any subcubic graph $H$, $H$-\textsc{ISC} is in $\mathsf{P}$ if and only if $H$ is planar.

Context

The conjecture is proposed by the paper's authors as a natural open question following their proof that a specific non-planar subcubic graph yields NP-complete induced subdivision containment. It complements known polynomial-time algorithms for planar induced subdivision detection (e.g., for the net and $K_{4}$) and the new hardness results of the paper.

Notes. The 'only if' direction (NP-hardness for non-planar subcubic $H$) implicitly assumes $\mathsf{P}\neq\mathsf{NP}$.

Source paper

 Induced Disjoint Paths Without an Induced Minor
 Pierre Aboulker, Édouard Bonnet, Timothé Picavet, Nicolas Trotignon · 2025-02-07
 https://arxiv.org/abs/2502.05289

=== Source paper abstract / header ===
Abstract:We exhibit a new obstacle to the nascent algorithmic theory for classes excluding an induced minor. We indeed show that on the class of string graphs -- which avoids the 1-subdivision of, say, $K_5$ as an induced minor -- Induced 2-Disjoint Paths is NP-complete. So, while $k$-Disjoint Paths, for a fixed $k$, is polynomial-time solvable in general graphs, the absence of a graph as an induced minor does not make its induced variant tractable, even for $k=2$. This answers a question of Korhonen and Lokshtanov [SODA '24], and complements a polynomial-time algorithm for Induced $k$-Disjoint Paths in classes of bounded genus by Kobayashi and Kawarabayashi [SODA '09]. In addition to being string graphs, our produced hard instances are subgraphs of a constant power of bounded-degree planar graphs, hence have bounded twin-width and bounded maximum degree.
We also leverage our new result to show that there is a fixed subcubic graph $H$ such that deciding if an input graph contains $H$ as an induced subdivision is NP-complete. Until now, all the graphs $H$ for which such a statement was known had a vertex of degree at least 4. This answers a question by Chudnovsky, Seymour, and the fourth author [JCTB '13], and by Le [JGT '19]. Finally we resolve another question of Korhonen and Lokshtanov by exhibiting a subcubic graph $H$ without two adjacent degree-3 vertices and such that deciding if an input $n$-vertex graph contains $H$ as an induced minor is NP-complete, and unless the Exponential-Time Hypothesis fails, requires time $2^{\Omega(\sqrt n)}$. This complements an algorithm running in subexponential time $2^{O(n^{2/3} \log n)}$ by these authors [SODA '24] under the same technical condition.
 

 
 
 
 Comments:
 14 pages, 5 figures
 

 Subjects:
 
 Computational Complexity (cs.CC); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 68Q25
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2502.05289 [cs.CC]
 

 
  
 (or 
 arXiv:2502.05289v1 [cs.CC] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2502.05289
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Fri, 7 Feb 2025 19:45:26 UTC (108 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced Disjoint Paths Without an Induced Minor, by Pierre Aboulker and 3 other authors
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
 | 2025-02
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.CO
 

 

 

 
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
