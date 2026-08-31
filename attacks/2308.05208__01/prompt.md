Attack the following open graph-theory problem.

Catalog id: 2308.05208__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2308.05208__01/
Source paper: Ordering Candidates via Vantage Points (arXiv:2308.05208)

=== Catalog page (statement + literature review) ===
Zero-count gap for sums of square-root polynomials — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture asks to narrow the gap between the linear lower bound of $2r-1$ and the exponential upper bound of $2^{r-1}+1$ for the number of connected components of $\mathbb{R} \setminus V(f)$ when $f$ is a linear combination of $r$ square roots of everywhere-positive quadratic polynomials. A Semantic Scholar citation search found only one paper citing arXiv:2308.05208 (Beker 2023, arXiv:2309.12809), which addresses a different open problem from the same source paper about protrusive orderings. No published or preprint work resolving or partially resolving this gap problem was found.

 Reviewer notes. The only citing paper found (arXiv:2309.12809, Beker 2023) addresses a different open problem from the same source paper. The connected-components gap question appears to be a side remark in the paper (a companion to the main sign-pattern results) and has not attracted dedicated follow-up as of May 2026. Confidence is high given the paper's recency and the breadth of the search.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. For $f : \mathbb{R} \to \mathbb{R}$ a linear combination of $r$ square roots of everywhere-positive quadratic polynomials, the number of connected components of $\mathbb{R} \setminus V(f)$ is at most $2^{r-1}+1$, while at least $2r-1$ components are achievable. It would be interesting to narrow the gap between this linear lower bound and the exponential upper bound.

Context

As a simpler companion question to the sign-pattern gap, the authors fix $N = m = 1$ and $\Delta = s = 2$. The upper bound $2^{r-1}+1$ follows from the same conjugate-multiplication trick as Theorem 2.2; an explicit construction with parameters $0 < a_1 < \cdots < a_{r-1}$ growing extremely quickly achieves $2r - 1$ connected components, giving a linear lower bound versus an exponential upper bound.

Notes. PDF source — mathematical expressions (e.g. $2^{r-1}+1$ vs $2r-1$) may be garbled; values interpreted from the authors' explicit statement 'linear lower bound and exponential upper bound'.

Source paper

 Ordering Candidates via Vantage Points
 Noga Alon, Colin Defant, Noah Kravitz, Daniel G. Zhu · 2023-08-09
 https://arxiv.org/abs/2308.05208
 PDF source

=== Source paper abstract / header ===
Abstract:Given an $n$-element set $C\subseteq\mathbb{R}^d$ and a (sufficiently generic) $k$-element multiset $V\subseteq\mathbb{R}^d$, we can order the points in $C$ by ranking each point $c\in C$ according to the sum of the distances from $c$ to the points of $V$. Let $\Psi_k(C)$ denote the set of orderings of $C$ that can be obtained in this manner as $V$ varies, and let $\psi^{\mathrm{max}}_{d,k}(n)$ be the maximum of $\lvert\Psi_k(C)\rvert$ as $C$ ranges over all $n$-element subsets of $\mathbb{R}^d$. We prove that $\psi^{\mathrm{max}}_{d,k}(n)=\Theta_{d,k}(n^{2dk})$ when $d \geq 2$ and that $\psi^{\mathrm{max}}_{1,k}(n)=\Theta_k(n^{4\lceil k/2\rceil -1})$. As a step toward proving this result, we establish a bound on the number of sign patterns determined by a collection of functions that are sums of radicals of nonnegative polynomials; this can be understood as an analogue of a classical theorem of Warren. We also prove several results about the set $\Psi(C)=\bigcup_{k\geq 1}\Psi_k(C)$; this includes an exact description of $\Psi(C)$ when $d=1$ and when $C$ is the set of vertices of a vertex-transitive polytope.
 

 
 
 
 Comments:
 20 pages, 3 figures
 

 Subjects:
 
 Combinatorics (math.CO); Metric Geometry (math.MG)
 
 
 MSC classes:
 52C10 (Primary) 51M16, 52A40 (Secondary)
 

 Cite as:
 arXiv:2308.05208 [math.CO]
 

 
  
 (or 
 arXiv:2308.05208v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2308.05208
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Zhu [view email] 
 [v1]
 Wed, 9 Aug 2023 20:06:04 UTC (56 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Ordering Candidates via Vantage Points, by Noga Alon and 3 other authors
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
 | 2023-08
 

 Change to browse by:
 
 math
 math.MG
 

 

 

 
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
