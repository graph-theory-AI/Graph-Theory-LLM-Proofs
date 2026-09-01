Attack the following open graph-theory problem.

Catalog id: 2503.16882__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2503.16882__00/
Source paper: Vertex Partitioning and $p$-Energy of Graphs (arXiv:2503.16882)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2
For every connected graph $G$ of order $n$ and $p\geq 2$, $$\mathcal{E}^{-}_{p}(G)\geq\mathcal{E}^{-}_{p}(P_{n}).$$

Context:
The paper's authors pose this as the natural negative $p$-energy analogue of Conjecture 1 of Tang, Liu, and Wang. Together, Conjectures 1 and 2 generalize Conjecture 3 of Elphick, Farber, Goldberg, and Wocjan, since at $p=2$ both give the bound $n-1$ by symmetry of the path spectrum. The paper settles this conjecture for $p\geq 4$ via Theorem 1.

=== Catalog page (statement + literature review) ===
Minimum negative p-energy at path graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The source paper itself settles the case $p \geq 4$ (Theorem 1), so the conjecture was already partially resolved upon publication. A subsequent paper by Chen, Wang, and Zhang (arXiv:2604.15656, April 2026) extends this to all integers $p \geq 3$ (Corollary 1.7), improving Theorem 1 of the source paper. The case $p = 2$ remains open. Note: the verified HTML of arXiv:2503.16882 shows that Conjecture 2 actually compares to the complete graph $K_n$ (i.e., $\mathcal{E}^{-}_{p}(G) \geq \mathcal{E}^{-}_{p}(K_n)$), not to $P_n$ as stated in the input; the two bounds coincide at $p = 2$ since $\mathcal{E}^{-}_{2}(P_n) = \mathcal{E}^{-}_{2}(K_n) = n-1$.

 Cited literature (1)

 
 
 
partial Positive and negative 3-energies of graphs
 (2026)
 

 
 Zhengbo Chen, Zhouningxin Wang, Xiao-Dong Zhang · arXiv preprint · arXiv:2604.15656

Corollary 1.7 proves Conjecture 2 of the source paper for all integers $p \geq 3$, improving the previously known bound of $p \geq 4$; the case $p = 2$ remains open.
 

 

 Reviewer notes. Discrepancy in conjecture statement: the input states Conjecture 2 as $\mathcal{E}^{-}_{p}(G) \geq \mathcal{E}^{-}_{p}(P_n)$ (path as comparator), but the verified HTML of arXiv:2503.16882 shows the actual Conjecture 2 uses $K_n$ (complete graph) as comparator. The two bounds are equal at $p=2$ (both equal $n-1$), explaining the context remark about 'symmetry of the path spectrum'. The follow-up arXiv:2604.15656 (April 2026) labels the conjecture as 'Conjecture 1.3 (Akbari et al. 2025b)' and confirms the $K_n$ form. Only the $p=2$ case remains unresolved.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every connected graph $G$ of order $n$ and $p\geq 2$, $$\mathcal{E}^{-}_{p}(G)\geq\mathcal{E}^{-}_{p}(P_{n}).$$

Context

The paper's authors pose this as the natural negative $p$-energy analogue of Conjecture 1 of Tang, Liu, and Wang. Together, Conjectures 1 and 2 generalize Conjecture 3 of Elphick, Farber, Goldberg, and Wocjan, since at $p=2$ both give the bound $n-1$ by symmetry of the path spectrum. The paper settles this conjecture for $p\geq 4$ via Theorem 1.

Notes. The theorem-environment text captures only the preamble clause; the displayed formula $\mathcal{E}^{-}_{p}(G)\geq\mathcal{E}^{-}_{p}(P_{n})$ is reconstructed from the stated analogy with Conjecture 1, the generalisation claim for Conjecture 3, and the fact that Theorem 1 (proved bound $\mathcal{E}_{p}^{-}(G)\geq n$ for $p\geq 4$, $G\ncong K_n$) is said to settle this conjecture for $p\geq 4$. The case $2\leq p<4$ remains open.

Source paper

 Vertex Partitioning and $p$-Energy of Graphs
 Saieed Akbari, Hitesh Kumar, Bojan Mohar, Shivaramakrishna Pragada · 2025-06-20
 https://arxiv.org/abs/2503.16882

=== Source paper abstract / header ===
Abstract:For a Hermitian matrix $A$ of order $n$ with eigenvalues $\lambda_1(A)\ge \cdots\ge \lambda_n(A)$, define \[ \mathcal{E}_p^+(A)=\sum_{\lambda_i > 0} \lambda_i^p(A), \quad \mathcal{E}_p^-(A)=\sum_{\lambda_i<0} |\lambda_i(A)|^p,\] to be the positive and the negative $p$-energy of $A$, respectively. In this note, first we show that if $A=[A_{ij}]_{i,j=1}^k$, where $A_{ii}$ are square matrices, then \[ \mathcal{E}_p^+(A)\geq \sum_{i=1}^{k} \mathcal{E}_p^+(A_{ii}), \quad \mathcal{E}_p^-(A)\geq \sum_{i=1}^{k} \mathcal{E}_p^-(A_{ii}),\] for any real number $p\geq 1$. We then apply the previous inequality to establish lower bounds for $p$-energy of the adjacency matrix of graphs.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2503.16882 [math.CO]
 

 
  
 (or 
 arXiv:2503.16882v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2503.16882
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Shivaramakrishna Pragada [view email] 
 [v1]
 Fri, 21 Mar 2025 06:33:17 UTC (11 KB)

 [v2]
 Fri, 20 Jun 2025 21:14:22 UTC (13 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Vertex Partitioning and $p$-Energy of Graphs, by Saieed Akbari and 3 other authors
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
 | 2025-03
 

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
