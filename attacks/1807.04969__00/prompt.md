Attack the following open graph-theory problem.

Catalog id: 1807.04969__00
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1807.04969__00/
Source paper: H\\ (arXiv:1807.04969)

=== Catalog page (statement + literature review) ===
Erdős–Pósa constant dependence on |H| — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The open problem asks for good bounds on the constant $c = c(H)$ in the Erdős-Pósa bounding function $f(k) = ck\log(k+1)$ for planar minors, and in particular whether $c$ can be made to depend only polynomially on $|H|$. The original paper's proof yields an enormous (possibly non-computable) constant $c$, while Chekuri–Chuzhoy achieve polynomial dependence on $|H|$ at the cost of extra poly-logarithmic factors. No subsequent work resolving this specific quantitative question was found in a thorough search of the literature as of May 2026.

 Reviewer notes. No follow-up paper specifically addressing the quantitative dependence of $c$ on $|H|$ was found. The related 2020 paper 'Erdős-Pósa from ball packing' (Cames van Batenburg, Joret, Ulmer; SIDMA) provides an alternative proof framework for edge variants but does not resolve the constant-vs-|H| question. The paper arXiv:2407.09671 ('Obstructions to Erdős-Pósa Dualities for Minors') addresses half-integrality and characterisation of EP-counterexamples, not the quantitative bound on $c$. The open problem remains unresolved with high confidence.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Find good bounds on $c$ as a function of $|H|$ in the bounding function $f(k) = ck\log(k+1)$; in particular, determine whether $c$ could depend polynomially on $|H|$.

Context

The constant $c = c(H)$ obtained in the proof of Theorem 1.1 is enormous and not even known to be computable, whereas Chekuri and Chuzhoy's earlier result achieves $c$ depending polynomially on $|H|$ (at the cost of a poly-logarithmic factor $\log^d k$). The authors explicitly leave the question of good bounds on $c$ as a function of $|H|$ as an open problem.

Notes. Stated in prose in the introduction without a labelled environment: "Finding good bounds on c as a function of |H| is left as an open problem, in particular it would be interesting to determine whether c could depend polynomially on |H|."

Source paper

 A tight Erdős-Pósa function for planar minors
 Wouter Cames van Batenburg, Tony Huynh, Gwenaël Joret, Jean-Florent Raymond · 2019-10-23
 https://arxiv.org/abs/1807.04969
 PDF source

=== Source paper abstract / header ===
Abstract:Let $H$ be a planar graph. By a classical result of Robertson and Seymour, there is a function $f:\mathbb{N} \to \mathbb{R}$ such that for all $k \in \mathbb{N}$ and all graphs $G$, either $G$ contains $k$ vertex-disjoint subgraphs each containing $H$ as a minor, or there is a subset $X$ of at most $f(k)$ vertices such that $G-X$ has no $H$-minor. We prove that this remains true with $f(k) = c k \log k$ for some constant $c=c(H)$. This bound is best possible, up to the value of $c$, and improves upon a recent result of Chekuri and Chuzhoy [STOC 2013], who established this with $f(k) = c k \log^d k$ for some universal constant $d$. The proof is constructive and yields a polynomial-time $O(\log \mathsf{OPT})$-approximation algorithm for packing subgraphs containing an $H$-minor.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C75
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:1807.04969 [math.CO]
 

 
  
 (or 
 arXiv:1807.04969v5 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1807.04969
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Advances in Combinatorics, 2019:2, 33 pp
 

 
 
 Related DOI:
 
 https://doi.org/10.19086/aic.10807

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Gwenaël Joret [view email] 
 [v1]
 Fri, 13 Jul 2018 08:24:29 UTC (29 KB)

 [v2]
 Wed, 14 Nov 2018 13:12:03 UTC (30 KB)

 [v3]
 Wed, 17 Apr 2019 17:47:46 UTC (37 KB)

 [v4]
 Thu, 18 Apr 2019 17:42:15 UTC (37 KB)

 [v5]
 Wed, 23 Oct 2019 19:40:26 UTC (50 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A tight Erd\H{o}s-P\'osa function for planar minors, by Wouter Cames van Batenburg and 3 other authors
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
 | 2018-07
 

 Change to browse by:
 
 cs
 cs.DM
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
