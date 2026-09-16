Attack the following open graph-theory problem.

Catalog id: 1907.04066__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1907.04066__00/
Source paper: Coloring count cones of planar graphs (arXiv:1907.04066)

=== Extracted statement (catalog JSON) ===
Title: Problem 1
Does there exist a polynomial-time algorithm which, given a near-triangulation $G$ with the outer face bounded by a 4-cycle $C$ and a 4-coloring $\psi$ of $C$, correctly decides whether $\psi$ extends to a 4-coloring of $G$?

Context:
The authors note that even very basic precoloring extension questions for planar graphs are wide open. There exist infinitely many near-triangulations $G$ whose outer 4-cycle has a precoloring that does not extend to a 4-coloring of $G$, yet no good characterization of such graphs is known.

=== Catalog page (statement + literature review) ===
4-coloring extension for near-triangulations — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Problem 1 asks whether a polynomial-time algorithm exists to decide if a 4-coloring of the outer 4-cycle of a near-triangulation extends to the whole graph; the general question remains open. Dvořák, Moore, Seifrtová, and Šámal (arXiv:2312.13061) provide partial progress by giving linear-time algorithms for the special subclass of planar near-Eulerian-triangulations (all interior vertices have even degree) when the outer face has length at most 5, which covers the 4-cycle case within that restricted class. No resolution of the full statement for arbitrary near-triangulations was found in the literature.

 Cited literature (1)

 
 
 
partial Precoloring extension in planar near-Eulerian-triangulations
 (2023)
 

 
 Dvořák, Moore, Seifrtová, Šámal · arXiv preprint · arXiv:2312.13061

Gives linear-time algorithms for 4-precoloring extension in planar near-Eulerian-triangulations with outer face length at most 5 (including the 4-cycle case), constituting a special-case resolution of Problem 1 restricted to the Eulerian interior-degree setting.
 

 

 Reviewer notes. The paper arXiv:2312.13061 addresses a strictly more restricted class (near-Eulerian-triangulations, where all interior vertices have even degree) rather than arbitrary near-triangulations. Its Conjecture 3 further conjectures a polynomial-time algorithm for all bounded outer-face lengths in the near-Eulerian setting, suggesting the general Problem 1 is still open. A 2025 European Journal of Combinatorics paper (vol. 127, art. 104138) appears related but its content could not be verified via WebFetch.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Does there exist a polynomial-time algorithm which, given a near-triangulation $G$ with the outer face bounded by a 4-cycle $C$ and a 4-coloring $\psi$ of $C$, correctly decides whether $\psi$ extends to a 4-coloring of $G$?

Context

The authors note that even very basic precoloring extension questions for planar graphs are wide open. There exist infinitely many near-triangulations $G$ whose outer 4-cycle has a precoloring that does not extend to a 4-coloring of $G$, yet no good characterization of such graphs is known.

Notes. PDF source — math notation may be garbled

Source paper

 Coloring count cones of planar graphs
 Zdeněk Dvořák, Bernard Lidický · 2021-10-25
 https://arxiv.org/abs/1907.04066
 PDF source

=== Source paper abstract / header ===
Abstract:For a plane near-triangulation $G$ with the outer face bounded by a cycle $C$, let $n^\star_G$ denote the function that to each $4$-coloring $\psi$ of $C$ assigns the number of ways $\psi$ extends to a $4$-coloring of $G$. The block-count reducibility argument (which has been developed in connection with attempted proofs of the Four Color Theorem) is equivalent to the statement that the function $n^\star_G$ belongs to a certain cone in the space of all functions from $4$-colorings of $C$ to real numbers. We investigate the properties of this cone for $|C|=5$, formulate a conjecture strengthening the Four Color Theorem, and present evidence supporting this conjecture.
 

 
 
 
 Comments:
 18 pages, 9 figures
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1907.04066 [math.CO]
 

 
  
 (or 
 arXiv:1907.04066v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1907.04066
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 
 Related DOI:
 
 https://doi.org/10.1002/jgt.22767

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Bernard Lidický [view email] 
 [v1]
 Tue, 9 Jul 2019 10:11:39 UTC (26 KB)

 [v2]
 Mon, 25 Oct 2021 12:15:11 UTC (28 KB)

 

 
 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Coloring count cones of planar graphs, by Zden\v{e}k Dvo\v{r}\'ak and Bernard Lidick\'y
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Ancillary-file links:
 Ancillary files (details):

 proof_verification.cpp
 rays_test.sage

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2019-07
 

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
