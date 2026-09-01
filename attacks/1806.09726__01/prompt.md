Attack the following open graph-theory problem.

Catalog id: 1806.09726__01
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1806.09726__01/
Source paper: Online Ramsey Numbers and the Subgraph Query Problem (arXiv:1806.09726)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 9
For any $m \geq 4$, $$f(K_m, p) = 2^{o(m)} p^{-\frac{2}{3}m + c_m},$$ where $c_m$ is a constant depending on $m \bmod 3$ (exact case formula garbled in PDF extraction).

Context:
Here $f(K_m, p)$ is the minimum number of queries needed to find a copy of $K_m$ with probability at least $1/2$ in the Subgraph Query Game on $G(\mathbb{Z}, p)$. The upper bound in this conjecture is proved in Section 5.2, and together with Theorem 12 (the matching lower bound) it is fully verified for $m = 4$ and $m = 5$.

=== Catalog page (statement + literature review) ===
Subgraph query complexity for K_m — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Conjecture 9 asserts $f(K_m, p) = 2^{o(m)} p^{-\frac{2}{3}m + c_m}$ for all $m \geq 4$; the source paper itself proves the upper bound (Section 5.2) and verifies the full conjecture (upper and matching lower bounds) for $m = 4$ and $m = 5$. A direct follow-up, arXiv:1911.04413 by Alweiss, Ben Hamida, He, and Moreira (2019, published in Combinatorics, Probability and Computing 2021), further studies $f(H, p)$ and improves upper bounds for all graphs $H$, but resolution of Conjecture 9 for all $m \geq 6$ could not be confirmed from the publicly accessible abstract. No paper fully resolving the conjecture for general $m$ was found.

 Cited literature (1)

 
 
 
partial On the subgraph query problem
 (2019)
 

 
 Ryan Alweiss, Chady Ben Hamida, Xiaoyu He, Alexander Moreira · Combinatorics, Probability and Computing · arXiv:1911.04413

Improves upper bounds on f(H, p) for every fixed graph H beyond the trivial O(p^{-d}) (where d is the degeneracy of H) and establishes superpolynomial lower bounds for certain 2-degenerate graphs, directly extending the subgraph query research program of arXiv:1806.09726; whether it resolves Conjecture 9 for all K_m (m >= 6) could not be confirmed from the abstract alone.
 

 

 Reviewer notes. The source paper itself already proves the upper bound in Conjecture 9 for all m >= 4 (Section 5.2) and verifies the complete conjecture (matching upper and lower bounds) for m=4 and m=5 via Theorem 12. The follow-up arXiv:1911.04413 is a direct continuation of this research line (shared author Xiaoyu He) but its abstract does not explicitly mention Conjecture 9 or give bounds for K_m with m >= 6. No paper fully resolving Conjecture 9 for general m was found within the cap of 5 web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any $m \geq 4$, $$f(K_m, p) = 2^{o(m)} p^{-\frac{2}{3}m + c_m},$$ where $c_m$ is a constant depending on $m \bmod 3$ (exact case formula garbled in PDF extraction).

Context

Here $f(K_m, p)$ is the minimum number of queries needed to find a copy of $K_m$ with probability at least $1/2$ in the Subgraph Query Game on $G(\mathbb{Z}, p)$. The upper bound in this conjecture is proved in Section 5.2, and together with Theorem 12 (the matching lower bound) it is fully verified for $m = 4$ and $m = 5$.

Notes. PDF source — the piecewise formula defining $c_m$ for $m \equiv 0, 1, 2 \pmod{3}$ is garbled in the extraction and cannot be read cleanly.

Source paper

 Online Ramsey Numbers and the Subgraph Query Problem
 David Conlon, Jacob Fox, Andrey Grinshpun, Xiaoyu He · 2018-11-04
 https://arxiv.org/abs/1806.09726
 PDF source

=== Source paper abstract / header ===
Abstract:The $(m,n)$-online Ramsey game is a combinatorial game between two players, Builder and Painter. Starting from an infinite set of isolated vertices, Builder draws an edge on each turn and Painter immediately paints it red or blue. Builder's goal is to force Painter to create either a red $K_m$ or a blue $K_n$ using as few turns as possible. The online Ramsey number $\tilde{r}(m,n)$ is the minimum number of edges Builder needs to guarantee a win in the $(m,n)$-online Ramsey game. By analyzing the special case where Painter plays randomly, we obtain an exponential improvement \[ \tilde{r}(n,n) \ge 2^{(2-\sqrt{2})n + O(1)} \] for the lower bound on the diagonal online Ramsey number, as well as a corresponding improvement \[ \tilde{r}(m,n) \ge n^{(2-\sqrt{2})m + O(1)} \] for the off-diagonal case, where $m\ge 3$ is fixed and $n\rightarrow\infty$. Using a different randomized Painter strategy, we prove that $\tilde{r}(3,n)=\tilde{\Theta}(n^3)$, determining this function up to a polylogarithmic factor. We also improve the upper bound in the off-diagonal case for $m \geq 4$.
In connection with the online Ramsey game with a random Painter, we study the problem of finding a copy of a target graph $H$ in a sufficiently large unknown Erdős--Rényi random graph $G(N,p)$ using as few queries as possible, where each query reveals whether or not a particular pair of vertices are adjacent. We call this problem the Subgraph Query Problem. We determine the order of the number of queries needed for complete graphs up to five vertices and prove general bounds for this problem.
 

 
 
 
 Comments:
 Corrected substantial error in the proof of Theorem 4
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1806.09726 [math.CO]
 

 
  
 (or 
 arXiv:1806.09726v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1806.09726
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Xiaoyu He [view email] 
 [v1]
 Mon, 25 Jun 2018 23:26:16 UTC (25 KB)

 [v2]
 Sun, 4 Nov 2018 16:35:54 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Online Ramsey Numbers and the Subgraph Query Problem, by David Conlon and 3 other authors
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
 | 2018-06
 

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
