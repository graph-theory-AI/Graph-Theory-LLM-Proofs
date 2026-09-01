Attack the following open graph-theory problem.

Catalog id: 2105.02383__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2105.02383__00/
Source paper: Ramsey numbers of sparse digraphs (arXiv:2105.02383)

=== Extracted statement (catalog JSON) ===
Title: Open problem on parameters governing $\overrightarrow{r}_1(H)$
What natural parameters (analogous to degeneracy and vertex count for undirected graphs) determine the growth order of $\overrightarrow{r}_1(H)$ for acyclic digraphs? In particular, is $\overrightarrow{r}_1(H)$ polynomial or super-polynomial in $n$ when $H$ has bounded degree?

Context:
For undirected graphs, the Ramsey number is governed by degeneracy and vertex count (Conlon–Fox–Sudakov conjecture, verified up to a $\log^2 d$ factor). The authors introduce the notion of 'multiscale complexity' as a candidate parameter for the directed setting, but stress that the full picture remains unresolved and deserves further research.

=== Catalog page (statement + literature review) ===
Parameters governing acyclic digraph Ramsey growth — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The source paper itself already demonstrates that bounded degree alone does not suffice for polynomial (let alone linear) oriented Ramsey numbers, constructing bounded-degree acyclic digraphs with $\overrightarrow{r}_1(H) \ge n^{\Omega(\Delta^{2/3}/\log^{5/3}\Delta)}$, while the complete characterization via natural parameters remains open. The 2025 follow-up by Bradač, Morawski, Sudakov, and Wigderson extends the linear upper bound regime to acyclic digraphs with 'graded bandwidth' (local edge structure), unifying previous results on bounded height, bounded bandwidth, and tree blowups. However, the full picture is explicitly acknowledged as far from resolved: a complete analogue of the degeneracy-plus-vertex-count framework for undirected graphs has not been found for the directed setting.

 Cited literature (1)

 
 
 
partial Ramsey numbers of digraphs with local edge structure
 (2025)
 

 
 Domagoj Bradač, Patryk Morawski, Benny Sudakov, Yuval Wigderson · arXiv preprint · arXiv:2509.05055

Proves linear oriented Ramsey numbers for bounded-degree acyclic digraphs with graded bandwidth (local edge structure), extending the class of digraphs known to have linear $\overrightarrow{r}_1(H)$ and contributing a structural parameter candidate, while noting the full characterization of which parameters govern the growth order remains far from complete.
 

 

 Reviewer notes. The open problem has two parts: (1) polynomial vs. super-polynomial for bounded-degree digraphs — partially answered, as super-polynomial examples exist in the source paper itself; (2) identifying the right structural parameter — partially addressed by 'multiscale complexity' (source paper) and 'graded bandwidth' (2509.05055), but no complete characterisation is known. The conjecture is best described as open with substantial partial progress.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. What natural parameters (analogous to degeneracy and vertex count for undirected graphs) determine the growth order of $\overrightarrow{r}_1(H)$ for acyclic digraphs? In particular, is $\overrightarrow{r}_1(H)$ polynomial or super-polynomial in $n$ when $H$ has bounded degree?

Context

For undirected graphs, the Ramsey number is governed by degeneracy and vertex count (Conlon–Fox–Sudakov conjecture, verified up to a $\log^2 d$ factor). The authors introduce the notion of 'multiscale complexity' as a candidate parameter for the directed setting, but stress that the full picture remains unresolved and deserves further research.

Notes. Stated as prose in the introduction (no formal theorem environment); also reiterated in the conclusion.

Source paper

 Ramsey numbers of sparse digraphs
 Jacob Fox, Xiaoyu He, Yuval Wigderson · 2022-01-21
 https://arxiv.org/abs/2105.02383
 PDF source

=== Source paper abstract / header ===
Abstract:Burr and Erdős in 1975 conjectured, and Chvátal, Rödl, Szemerédi and Trotter later proved, that the Ramsey number of any bounded degree graph is linear in the number of vertices. In this paper, we disprove the natural directed analogue of the Burr--Erdős conjecture, answering a question of Bucić, Letzter, and Sudakov. If $H$ is an acyclic digraph, the oriented Ramsey number of $H$, denoted $\overrightarrow{r_{1}}(H)$, is the least $N$ such that every tournament on $N$ vertices contains a copy of $H$. We show that for any $\Delta \geq 2$ and any sufficiently large $n$, there exists an acyclic digraph $H$ with $n$ vertices and maximum degree $\Delta$ such that \[ \overrightarrow{r_{1}}(H)\ge n^{\Omega(\Delta^{2/3}/ \log^{5/3} \Delta)}. \] This proves that $\overrightarrow{r_{1}}(H)$ is not always linear in the number of vertices for bounded-degree $H$. On the other hand, we show that $\overrightarrow{r_{1}}(H)$ is nearly linear in the number of vertices for typical bounded-degree acyclic digraphs $H$, and obtain linear or nearly linear bounds for several natural families of bounded-degree acyclic digraphs.
For multiple colors, we prove a quasi-polynomial upper bound $\overrightarrow{r_{k}}(H)=2^{(\log n)^{O_{k}(1)}}$ for all bounded-degree acyclic digraphs $H$ on $n$ vertices, where $\overrightarrow{r_k}(H)$ is the least $N$ such that every $k$-edge-colored tournament on $N$ vertices contains a monochromatic copy of $H$. For $k\geq 2$ and $n\geq 4$, we exhibit an acyclic digraph $H$ with $n$ vertices and maximum degree $3$ such that $\overrightarrow{r_{k}}(H)\ge n^{\Omega(\log n/\log\log n)}$, showing that these Ramsey numbers can grow faster than any polynomial in the number of vertices.
 

 
 
 
 Comments:
 28 pages; revised to reflect referee comments
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2105.02383 [math.CO]
 

 
  
 (or 
 arXiv:2105.02383v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2105.02383
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Yuval Wigderson [view email] 
 [v1]
 Thu, 6 May 2021 00:50:34 UTC (36 KB)

 [v2]
 Fri, 21 Jan 2022 22:14:35 UTC (38 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Ramsey numbers of sparse digraphs, by Jacob Fox and 2 other authors
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
 | 2021-05
 

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
