Attack the following open graph-theory problem.

Catalog id: 1806.09726__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1806.09726__00/
Source paper: Online Ramsey Numbers and the Subgraph Query Problem (arXiv:1806.09726)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 7
(a) The diagonal online random Ramsey numbers satisfy $$\tilde{r}_{rand}(n, n) = 2^{(1+o(1)) \frac{2}{3} n}.$$ (b) The off-diagonal online random Ramsey numbers ($m \geq 3$ fixed and $n \to \infty$) satisfy $$\tilde{r}_{rand}(m, n) = n^{(1+o(1)) \frac{2}{3} m}.$$

Context:
The authors define the online random Ramsey number $\tilde{r}_{rand}(m,n)$ as the maximum over $p \in (0,1)$ of $\tilde{r}(m,n;p)$, where Painter independently colors each edge red with probability $p$. These conjectures on the growth rate are motivated by a connection with the Subgraph Query Problem; Theorem 10 and Conjecture 9 together imply both parts of this conjecture.

=== Catalog page (statement + literature review) ===
Diagonal and off-diagonal online random Ramsey growth rates — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 7 from arXiv:1806.09726 posits that the diagonal online random Ramsey numbers grow as $2^{(1+o(1))\frac{2}{3}n}$ and the off-diagonal as $n^{(1+o(1))\frac{2}{3}m}$. The conjecture is tied to the Subgraph Query Problem via Theorem 10 and Conjecture 9 of the same paper. A 2019 follow-up (arXiv:1911.04413) makes progress on the Subgraph Query Problem itself, but a web search through 2026 found no paper that directly resolves either part of Conjecture 7. The conjecture remains open as far as indexed literature reveals.

 Cited literature (1)

 
 
 
partial On the subgraph query problem
 (2019)
 

 
 Ryan Alweiss, Chady Ben Hamida, Xiaoyu He, Alexander Moreira · arXiv preprint · arXiv:1911.04413

Improves bounds on the Subgraph Query Problem for cliques and degenerate graphs, directly related to the mechanism through which Conjecture 7 is expected to follow, but does not resolve the conjecture's stated growth-rate claims.
 

 

 Reviewer notes. Semantic Scholar citation list for arXiv:1806.09726 shows no citing paper that directly resolves Conjecture 7. The related paper arXiv:1911.04413 (with Xiaoyu He as co-author of both) works on the subgraph query problem but does not establish the conjectured exponents for r_rand. The conjecture is 8 years old; medium confidence rather than high is assigned because the conjecture's age and its tight connection to an active research topic leave room for a resolution in the literature that was not surfaced by the search.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. (a) The diagonal online random Ramsey numbers satisfy $$\tilde{r}_{rand}(n, n) = 2^{(1+o(1)) \frac{2}{3} n}.$$ (b) The off-diagonal online random Ramsey numbers ($m \geq 3$ fixed and $n \to \infty$) satisfy $$\tilde{r}_{rand}(m, n) = n^{(1+o(1)) \frac{2}{3} m}.$$

Context

The authors define the online random Ramsey number $\tilde{r}_{rand}(m,n)$ as the maximum over $p \in (0,1)$ of $\tilde{r}(m,n;p)$, where Painter independently colors each edge red with probability $p$. These conjectures on the growth rate are motivated by a connection with the Subgraph Query Problem; Theorem 10 and Conjecture 9 together imply both parts of this conjecture.

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
