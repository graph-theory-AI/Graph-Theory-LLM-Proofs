Attack the following open graph-theory problem.

Catalog id: 1806.09726__02
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1806.09726__02/
Source paper: Online Ramsey Numbers and the Subgraph Query Problem (arXiv:1806.09726)

=== Extracted statement (catalog JSON) ===
Title: Informal conjecture on generalization of Theorem 4 to all $\tilde{r}(m,n)$
We suspect that Theorem 4 can be generalized to $\tilde{r}(m, n)$ in the same way.

Context:
Theorem 4 establishes $\tilde{r}(3,n) = \Omega(n^3/\log^2 n)$ via a Painter strategy that avoids red triangles, in an argument close in spirit to Erdős's alteration method. The authors note that Krivelevich generalized this alteration method to all $r(m,n)$ and conjecture informally that the same can be done for $\tilde{r}(m,n)$.

=== Catalog page (statement + literature review) ===
Alteration method generalization for r̃(m,n) — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The informal conjecture asks whether Krivelevich's generalization of the alteration method to all $r(m,n)$ can be extended to the online setting for all $\tilde{r}(m,n)$. Guo and Warnke (arXiv:1909.02691, published 2023 in Journal of Graph Theory) apply a refined alteration method specifically to online graph Ramsey games, which is directly in the spirit of the conjecture; however, the abstract does not confirm that bounds for all $m$ are established, so a full resolution cannot be verified from available sources.

 Cited literature (1)

 
 
 
partial Bounds on Ramsey Games via Alterations
 (2019)
 

 
 He Guo, Lutz Warnke · Journal of Graph Theory · arXiv:1909.02691

Refines the classical alteration method and applies it to online graph Ramsey games, extending beyond Krivelevich's single-edge-removal approach and likely addressing the conjecture about $\tilde{r}(m,n)$ for general $m$, though the abstract does not specify the exact range of $m$ covered.
 

 

 Reviewer notes. The conjecture is informal, paralleling Krivelevich's extension of Erdős's alteration method from triangles to general cliques in the classical Ramsey setting. Guo and Warnke (1909.02691) is the most directly relevant follow-up: it refines the alteration method and applies it to online Ramsey games, but the abstract stops short of specifying whether all $m$ are covered. No counterexample or explicit full resolution was found. Xiaoyu He's personal papers page lists no subsequent work on $\tilde{r}(m,n)$.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We suspect that Theorem 4 can be generalized to $\tilde{r}(m, n)$ in the same way.

Context

Theorem 4 establishes $\tilde{r}(3,n) = \Omega(n^3/\log^2 n)$ via a Painter strategy that avoids red triangles, in an argument close in spirit to Erdős's alteration method. The authors note that Krivelevich generalized this alteration method to all $r(m,n)$ and conjecture informally that the same can be done for $\tilde{r}(m,n)$.

Notes. No explicit quantitative bound for general $m$ is stated; only the suspicion of generalizability is expressed.

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
