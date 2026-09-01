Attack the following open graph-theory problem.

Catalog id: 2401.00359__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2401.00359__01/
Source paper: Ramsey and Turán numbers of sparse hypergraphs (arXiv:2401.00359)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 6.2
There is a constant $c_{k}>0$ such that for every $k$-uniform $k$-partite hypergraph $H$, $\mathrm{ex}(n,H)\leq O_{H}\left(n^{k-\frac{c_{k}}{d_{\mathsf{max}}(H)}}\right).$

Context:
Theorem 1.4 gives $\Omega_{k}(n^{k-C_{k}/d_{1}(H)})\leq\operatorname{ex}(n,H)\leq O_{H}(n^{k-c_{k}/d_{1}(H)^{k-1}})$. The complete $k$-partite hypergraph $K^{(k)}_{d,\ldots,d}$ shows the upper bound is tight in $d_{1}$, while the bipartite hedgehog $H_{d}^{(k)}$ shows the lower bound is tight in $d_{1}$. This gap motivates replacing $d_{1}(H)$ by the finer quantity $d_{\mathsf{max}}(H)=\max_{1\leq i<k}d_{i}(H)$, and Conjecture 6.2 asserts that the Turán exponent is controlled by $d_{\mathsf{max}}(H)$.

=== Catalog page (statement + literature review) ===
Turán Exponent via d_max for k-partite Hypergraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 6.2 from arXiv:2401.00359 asserts that for every k-uniform k-partite hypergraph H there exists a constant c_k > 0 such that the Turán exponent is controlled by d_max(H) = max_{1 ≤ i < k} d_i(H), refining Theorem 1.4 which gives bounds in terms of the coarser quantity d_1(H). No follow-up paper resolving or substantially advancing this conjecture was found in the indexed literature as of May 2026; the conjecture appears to remain fully open.

 Reviewer notes. No follow-up found after five web queries. The conjecture was posted December 2023 and asks whether d_max(H) = max_{1 ≤ i < k} d_i(H) controls the Turán exponent for k-uniform k-partite hypergraphs; Theorem 1.4 of the same paper establishes matching upper and lower bounds only in terms of the 1-skeleton degeneracy d_1(H), leaving a polynomial gap between the two bounds that motivates the conjecture. The related paper arXiv:2510.07997 on apex partite hypergraphs (2025) addresses a conjecture of Lee rather than Conjecture 6.2.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There is a constant $c_{k}>0$ such that for every $k$-uniform $k$-partite hypergraph $H$, $\mathrm{ex}(n,H)\leq O_{H}\left(n^{k-\frac{c_{k}}{d_{\mathsf{max}}(H)}}\right).$

Context

Theorem 1.4 gives $\Omega_{k}(n^{k-C_{k}/d_{1}(H)})\leq\operatorname{ex}(n,H)\leq O_{H}(n^{k-c_{k}/d_{1}(H)^{k-1}})$. The complete $k$-partite hypergraph $K^{(k)}_{d,\ldots,d}$ shows the upper bound is tight in $d_{1}$, while the bipartite hedgehog $H_{d}^{(k)}$ shows the lower bound is tight in $d_{1}$. This gap motivates replacing $d_{1}(H)$ by the finer quantity $d_{\mathsf{max}}(H)=\max_{1\leq i<k}d_{i}(H)$, and Conjecture 6.2 asserts that the Turán exponent is controlled by $d_{\mathsf{max}}(H)$.

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
