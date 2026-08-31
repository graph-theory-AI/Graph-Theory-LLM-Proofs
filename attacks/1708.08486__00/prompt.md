Attack the following open graph-theory problem.

Catalog id: 1708.08486__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1708.08486__00/
Source paper: Popular progression differences in vector spaces II (arXiv:1708.08486)

=== Catalog page (statement + literature review) ===
Exponential constant in r(n,m) for 𝔽₃ⁿ subspaces — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question asks whether the exponential base in the exponent of r(n,m) (the maximum size of a subset of F_3^n containing no affine m-dimensional subspace) is 3 (as in the random lower bound r(n,m) >= N^{1-(m+1)3^{-m}}) rather than C≈13.901 (as in the cap-set-supersaturation upper bound). Fox and Pham's paper itself provides evidence that the popular-differences approach cannot close this gap, and no subsequent work resolving or substantially narrowing it was found in the literature search.

 Reviewer notes. No follow-up paper resolving or substantially advancing the question was found in five web searches. The paper itself proves that the popular-differences/density-increment approach via Green's arithmetic regularity lemma cannot settle the correct exponential base, leaving the gap between 3 and C≈13.901 open. The question is closely tied to sharp bounds on n_3(alpha,beta) for beta=alpha^{3+o(1)}, which also remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Is $3$, the lower bound on $r(n,m)$ given by considering a random set, the right exponential constant? That is, does $r(n,m) = N^{1-\varepsilon_m}$ hold with the same exponential base $3$ as in the random lower bound $r(n,m) \geq N^{1-(m+1)3^{-m}}$, rather than the base $C \approx 13.901$ appearing in the upper bound $r(n,m) \leq (1+o(1))N^{1-C^{-m}}$?

Context

The lower and upper bounds for $r(n,m)$ (the maximum size of a subset of $\mathbb{F}_3^n$ containing no affine $m$-dimensional subspace) both have the form $N^{1-\varepsilon_m}$ with $\varepsilon_m \to 0$ exponentially fast in $m$, but with different exponential constants: $3$ in the random lower bound and $C \approx 13.901$ in the upper bound derived from the cap set supersaturation result. The authors note that resolving this question is closely tied to whether $n_3(\alpha,\beta)$ is small enough for $\beta = \alpha^{3+o(1)}$, and their main result provides evidence that the approach via popular differences likely cannot resolve it.

Notes. Stated as an open question in running prose in the introduction without a formal labelled environment. PDF source — exponent notation in r(n,m) bounds may be garbled.

Source paper

 Popular progression differences in vector spaces II
 Jacob Fox, Huy Tuan Pham · 2019-11-21
 https://arxiv.org/abs/1708.08486
 PDF source

=== Source paper abstract / header ===
Abstract:Green used an arithmetic analogue of Szemerédi's celebrated regularity lemma to prove the following strengthening of Roth's theorem in vector spaces. For every $\alpha>0$, $\beta<\alpha^3$, and prime number $p$, there is a least positive integer $n_p(\alpha,\beta)$ such that if $n \geq n_p(\alpha,\beta)$, then for every subset of $\mathbb{F}_p^n$ of density at least $\alpha$ there is a nonzero $d$ for which the density of three-term arithmetic progressions with common difference $d$ is at least $\beta$. We determine for $p \geq 19$ the tower height of $n_p(\alpha,\beta)$ up to an absolute constant factor and an additive term depending only on $p$. In particular, if we want half the random bound (so $\beta=\alpha^3/2$), then the dimension $n$ required is a tower of twos of height $\Theta \left((\log p) \log \log (1/\alpha)\right)$. It turns out that the tower height in general takes on a different form in several different regions of $\alpha$ and $\beta$, and different arguments are used both in the upper and lower bounds to handle these cases.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Number Theory (math.NT)
 

 Cite as:
 arXiv:1708.08486 [math.CO]
 

 
  
 (or 
 arXiv:1708.08486v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1708.08486
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Analysis, 2019:16, 39 pp
 

 

 

 
 Submission history
 From: Huy Tuan Pham [view email] 
 [v1]
 Mon, 28 Aug 2017 19:01:31 UTC (43 KB)

 [v2]
 Thu, 21 Nov 2019 16:24:15 UTC (75 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Popular progression differences in vector spaces II, by Jacob Fox and Huy Tuan Pham
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
 | 2017-08
 

 Change to browse by:
 
 math
 math.NT
 

 

 

 
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
