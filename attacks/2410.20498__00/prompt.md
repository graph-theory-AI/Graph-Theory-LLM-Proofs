Attack the following open graph-theory problem.

Catalog id: 2410.20498__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2410.20498__00/
Source paper: On hypercube statistics (arXiv:2410.20498)

=== Extracted statement (catalog JSON) ===
Title: Conjecture on $\lambda(d,1)$
$\lambda(d,1)=(1+o(1))/e$ where the $o(1)$-term tends to $0$ as $d$ tends to infinity.

Context:
The lower bound in Theorem 2, $(1-2^{-d})^{2^{d}-1}$, approaches $e^{-1}\approx 0.37$ as $d\to\infty$. The authors suspect this lower bound is asymptotically sharp, making $1/e$ the true limit of $\lambda(d,1)$.

=== Catalog page (statement + literature review) ===
λ(d,1) asymptotic limit 1/e hypercube — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No follow-up paper has proven or disproven the conjecture that $\lambda(d,1)=(1+o(1))/e$. A March 2025 paper (arXiv:2503.03408) studies the same $\lambda(d,s)$ statistics framework using flag algebras, proving exact values for $(d,s)\in\{(3,2),(4,2),(4,4)\}$, but explicitly treats $\lambda(2,1)$ as an intriguing open problem without addressing the $d\to\infty$ asymptotic. An April 2026 preprint (arXiv:2604.13402) extends the framework to affine (non-axis-aligned) subspaces of $\mathbb{F}_2^n$, motivated by the source paper, but its results concern a different statistic $\lambda^*(d,s)$ and do not bear on the axis-aligned conjecture.

 Cited literature (1)

 
 
 
partial Some exact values of the inducibility and statistics constants for hypercubes
 (2025)
 

 
 unknown (authors not returned by abstract page fetch) · arXiv preprint · arXiv:2503.03408

Proves exact values $\lambda(3,2)=8/9$, $\lambda(4,2)=264/343$, $\lambda(4,4)=26/27$ via flag algebras, and explicitly identifies $\lambda(2,1)$ as an open problem, but does not address the $d\to\infty$ asymptotic of $\lambda(d,1)$.
 

 

 Reviewer notes. The conjecture is recent (October 2024) and no resolution was found. arXiv:2503.03408 (March 2025) is the closest follow-up in the same research line: it proves exact values for other (d,s) pairs using flag algebras, cites Alon-Axenovich-Goldwasser as the initiating work, and mentions $\lambda(d,1)$ cases as open problems, confirming the conjecture remains unresolved as of early 2025. arXiv:2604.13402 (April 2026) is motivated by the source paper but works with affine subspaces and a different statistic $\lambda^*(d,s)$; for odd $s$ it proves $\lambda^*(d,s)\le 1/2$, which is structurally different from the axis-aligned setting.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Informal. $\lambda(d,1)=(1+o(1))/e$ where the $o(1)$-term tends to $0$ as $d$ tends to infinity.

Context

The lower bound in Theorem 2, $(1-2^{-d})^{2^{d}-1}$, approaches $e^{-1}\approx 0.37$ as $d\to\infty$. The authors suspect this lower bound is asymptotically sharp, making $1/e$ the true limit of $\lambda(d,1)$.

Notes. Stated in the abstract with the words 'We suspect'; no labelled conjecture environment.

Source paper

 On hypercube statistics
 Noga Alon, Maria Axenovich, John Goldwasser · 2024-10-27
 https://arxiv.org/abs/2410.20498

=== Source paper abstract / header ===
Abstract:Let $d \geq 1$ and $s \leq 2^d$ be nonnegative integers. For a subset $A$ of vertices of the hypercube $Q_n$ and $n\geq d$, let $\lambda(n,d,s,A)$ denote the fraction of subcubes $Q_d$ of $Q_n$ that contain exactly $s$ vertices of $A$. Let $\lambda(n,d,s)$ denote the maximum possible value of $\lambda(n,d,s,A)$ as $A$ ranges over all subsets of vertices of $Q_n$, and let $\lambda(d,s)$ denote the limit of this quantity as $n$ tends to infinity. We prove several lower and upper bounds on $\lambda(d,s)$, showing that for all admissible values of $d$ and $s$ it is larger than $0.28$. We also show that the values of $s=s(d)$ such that $\lambda(d,s)=1$ are exactly $\{0,2^{d-1},2^d\}$. In addition we prove that if $0<s< d/8$, then $\lambda(d, s) \leq 1 - \Omega(1/s)$, and that if $s$ is divisible by a power of $2$ which is $\Omega(s)$ then $\lambda(d,s) \geq 1-O(1/s)$. We suspect that $\lambda(d,1)=(1+o(1))/e$ where the $o(1)$-term tends to $0$ as $d$ tends to infinity, but this remains open, as does the problem of obtaining tight bounds for essentially all other quantities $\lambda(d,s)$.
 

 
 
 
 Comments:
 10 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2410.20498 [math.CO]
 

 
  
 (or 
 arXiv:2410.20498v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2410.20498
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Maria Axenovich [view email] 
 [v1]
 Sun, 27 Oct 2024 16:25:40 UTC (11 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On hypercube statistics, by Noga Alon and 2 other authors
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
 | 2024-10
 

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
