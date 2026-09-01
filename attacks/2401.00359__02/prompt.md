Attack the following open graph-theory problem.

Catalog id: 2401.00359__02
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2401.00359__02/
Source paper: Ramsey and Turán numbers of sparse hypergraphs (arXiv:2401.00359)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 6.4
Let $L$ be a $d\times d$ Latin square. Define $H_{L}$ to be the 3-uniform 3-partite hypergraph on vertex set $[d]\sqcup[d]\sqcup[d]$ where $(i,j,k)\in E(H_{L})$ if and only if $L(i,j)=k$. Then $\mathrm{ex}(n,H_{L})=n^{3-\Theta(1/d)}$.

Context:
For every $d\times d$ Latin square one has $d_{1}(H_{L}),d_{2}(H_{L})=\Theta(d)$, so $d_{\mathsf{max}}(H_{L})=\Theta(d)$, yet Theorem 1.4 only yields $\mathrm{ex}(n,H_{L})\leq O(n^{3-c/d^{2}})$. The 1-skeleton of $H_{L}$ is $K_{d,d,d}$, the same as that of the complete 3-partite hypergraph $K^{(3)}_{d,d,d}$, so current techniques cannot distinguish $H_{L}$ from $K^{(3)}_{d,d,d}$ at the level of the Turán exponent. Conjecture 6.4 predicts that the exponent is $3-\Theta(1/d)$, matching $d_{\mathsf{max}}(H_{L})=\Theta(d)$ via Conjecture 6.2.

=== Catalog page (statement + literature review) ===
Turán exponent of Latin square hypergraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 6.4 predicts that for any d×d Latin square L, the Turán number satisfies ex(n, H_L) = n^{3-Θ(1/d)}, which would match the bound predicted by the skeletal degeneracy d_max(H_L) = Θ(d) via Conjecture 6.2. The source paper only achieves the weaker upper bound O(n^{3-c/d^2}) via Theorem 1.4. No follow-up work addressing this conjecture was found in a search of the literature through May 2026.

 Reviewer notes. No follow-up found in the indexed literature. The four papers citing arXiv:2401.00359 (per Semantic Scholar) address unrelated topics: hypergraph universality, subhypergraph counting, canonical Ramsey numbers, and blowups of triangle-free graphs. The conjecture is recent (posted 2023-12-31) and the gap between the proven bound O(n^{3-c/d^2}) and the conjectured exponent n^{3-Θ(1/d)} remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $L$ be a $d\times d$ Latin square. Define $H_{L}$ to be the 3-uniform 3-partite hypergraph on vertex set $[d]\sqcup[d]\sqcup[d]$ where $(i,j,k)\in E(H_{L})$ if and only if $L(i,j)=k$. Then $\mathrm{ex}(n,H_{L})=n^{3-\Theta(1/d)}$.

Context

For every $d\times d$ Latin square one has $d_{1}(H_{L}),d_{2}(H_{L})=\Theta(d)$, so $d_{\mathsf{max}}(H_{L})=\Theta(d)$, yet Theorem 1.4 only yields $\mathrm{ex}(n,H_{L})\leq O(n^{3-c/d^{2}})$. The 1-skeleton of $H_{L}$ is $K_{d,d,d}$, the same as that of the complete 3-partite hypergraph $K^{(3)}_{d,d,d}$, so current techniques cannot distinguish $H_{L}$ from $K^{(3)}_{d,d,d}$ at the level of the Turán exponent. Conjecture 6.4 predicts that the exponent is $3-\Theta(1/d)$, matching $d_{\mathsf{max}}(H_{L})=\Theta(d)$ via Conjecture 6.2.

Source paper

 Ramsey and Turán numbers of sparse hypergraphs
 Jacob Fox, Maya Sankar, Michael Simkin, Jonathan Tidor, Yunkun Zhou · 2023-12-31
 https://arxiv.org/abs/2401.00359

=== Source paper abstract / header ===
Abstract:Degeneracy plays an important role in understanding Turán- and Ramsey-type properties of graphs. Unfortunately, the usual hypergraphical generalization of degeneracy fails to capture these properties. We define the skeletal degeneracy of a $k$-uniform hypergraph as the degeneracy of its $1$-skeleton (i.e., the graph formed by replacing every $k$-edge by a $k$-clique). We prove that skeletal degeneracy controls hypergraph Turán and Ramsey numbers in a similar manner to (graphical) degeneracy.
Specifically, we show that $k$-uniform hypergraphs with bounded skeletal degeneracy have linear Ramsey number. This is the hypergraph analogue of the Burr-Erdős conjecture (proved by Lee). In addition, we give upper and lower bounds of the same shape for the Turán number of a $k$-uniform $k$-partite hypergraph in terms of its skeletal degeneracy. The proofs of both results use the technique of dependent random choice. In addition, the proof of our Ramsey result uses the `random greedy process' introduced by Lee in his resolution of the Burr-Erdős conjecture.
 

 
 
 
 Comments:
 33 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2401.00359 [math.CO]
 

 
  
 (or 
 arXiv:2401.00359v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2401.00359
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Michael Simkin [view email] 
 [v1]
 Sun, 31 Dec 2023 00:54:14 UTC (44 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Ramsey and Tur\'an numbers of sparse hypergraphs, by Jacob Fox and 4 other authors
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
 | 2024-01
 

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
