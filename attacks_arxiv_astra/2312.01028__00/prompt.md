Attack the following open graph-theory problem.

Catalog id: 2312.01028__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2312.01028__00/
Source paper: A structure theorem for pseudo-segments and its applications (arXiv:2312.01028)

=== Extracted statement (catalog JSON) ===
Title: Optimal disjoint-edges bound in complete simple topological graphs
Is it true that every complete $n$-vertex simple topological graph contains $\Omega(n)$ pairwise disjoint edges?

Context:
Aichholzer et al. [2] showed that every complete $n$-vertex simple topological graph always contains $\Omega(n^{1/2})$ pairwise disjoint edges. The paper notes that improving this lower bound to $\Omega(n)$ is an open problem, and Corollary 1.3 provides a new nearly-polynomial lower bound under a density assumption.

=== Catalog page (statement + literature review) ===
Linear disjoint edges in complete topological graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The best known lower bound for pairwise disjoint edges in a complete $n$-vertex simple topological graph is $\Omega(n^{1/2})$, established by Aichholzer, García, Tejel, Vogtenhuber, and Weinberger (SoCG 2022, arXiv:2203.06143), improving the earlier $\Omega(n^{1/3})$ bound of Suk (2012). The source paper (Fox–Pach–Suk, 2023) provides a nearly-polynomial improvement under a density assumption via a pseudo-segment regularity lemma, but the full $\Omega(n)$ conjecture remains open. No post-2023 paper resolving the problem was found in a broad web search.

 Reviewer notes. The Omega(n^{1/2}) bound (Aichholzer et al., SoCG 2022, arXiv:2203.06143) is the current state of the art; the source paper improves this to a nearly-polynomial bound only under an edge-density assumption (Corollary 1.3). The paper 2512.04795 (December 2025) addresses plane paths in dense topological graphs but does not resolve the disjoint-edges question. No follow-up resolving the full Omega(n) conjecture was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Is it true that every complete $n$-vertex simple topological graph contains $\Omega(n)$ pairwise disjoint edges?

Context

Aichholzer et al. [2] showed that every complete $n$-vertex simple topological graph always contains $\Omega(n^{1/2})$ pairwise disjoint edges. The paper notes that improving this lower bound to $\Omega(n)$ is an open problem, and Corollary 1.3 provides a new nearly-polynomial lower bound under a density assumption.

Notes. Stated in passing as an open problem without a labelled theorem environment; PDF source.

Source paper

 A structure theorem for pseudo-segments and its applications
 Jacob Fox, Janos Pach, Andrew Suk · 2023-12-02
 https://arxiv.org/abs/2312.01028
 PDF source

=== Source paper abstract / header ===
Abstract:We prove a far-reaching strengthening of Szemerédi's regularity lemma for intersection graphs of pseudo-segments. It shows that the vertex set of such a graph can be partitioned into a bounded number of parts of roughly the same size such that almost all bipartite graphs between different pairs of parts are complete or empty. We use this to get an improved bound on disjoint edges in simple topological graphs, showing that every $n$-vertex simple topological graph with no $k$ pairwise disjoint edges has at most $n(\log n)^{O(\log k)}$ edges.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Computational Geometry (cs.CG)
 

 Cite as:
 arXiv:2312.01028 [math.CO]
 

 
  
 (or 
 arXiv:2312.01028v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2312.01028
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Andrew Suk [view email] 
 [v1]
 Sat, 2 Dec 2023 04:37:15 UTC (62 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A structure theorem for pseudo-segments and its applications, by Jacob Fox and 2 other authors
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
 | 2023-12
 

 Change to browse by:
 
 cs
 cs.CG
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
