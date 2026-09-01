Attack the following open graph-theory problem.

Catalog id: 2603.02786__03
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2603.02786__03/
Source paper: Packing arithmetic progressions (arXiv:2603.02786)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 6
If $k\ll n$, then $M_{k}(n)\sim\frac{k^{2}}{2\ln k}\cdot n$, while otherwise, $M_{k}(n)\sim\frac{k^{2}}{2\ln k}\cdot n-\frac{k^{3}}{3\ln k}$.

Context:
Conjectured asymptotic behaviour of $M_k(n)$ for $k<n$ in view of Theorem 5, splitting into two regimes according to whether $k\ll n$ or not.

=== Catalog page (statement + literature review) ===
Asymptotic regimes of Mₖ(n) packing progressions — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 6 of arXiv:2603.02786 proposes the precise asymptotic of M_k(n) (the minimum interval length needed to pack the arithmetic progressions B_d = {d, 2d, ..., nd} for d = 1,...,k) in two regimes: M_k(n) ~ k^2 n / (2 ln k) when k << n, and M_k(n) ~ k^2 n / (2 ln k) - k^3 / (3 ln k) otherwise. Theorem 5 of the same paper establishes matching bounds up to a (1/2 - o_k(1)) vs (zeta(2)/2 + o_k(1)) gap in the leading constant, so the conjecture refines those bounds to exact asymptotics. No follow-up paper resolving the conjecture was found in a broad web search conducted approximately 10 weeks after the paper's submission.

 Reviewer notes. No follow-up found. The paper was posted March 3, 2026; this review was conducted May 14, 2026, only ~10 weeks later, so absence of follow-up is expected and consistent with high confidence open status. The conjecture proposes exact asymptotics sharpening Theorem 5 of the same paper; both regimes hinge on the leading constant k^2/(2 ln k).

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. If $k\ll n$, then $M_{k}(n)\sim\frac{k^{2}}{2\ln k}\cdot n$, while otherwise, $M_{k}(n)\sim\frac{k^{2}}{2\ln k}\cdot n-\frac{k^{3}}{3\ln k}$.

Context

Conjectured asymptotic behaviour of $M_k(n)$ for $k<n$ in view of Theorem 5, splitting into two regimes according to whether $k\ll n$ or not.

Source paper

 Packing arithmetic progressions
 Noga Alon, Michał Dębski, Jarosław Grytczuk, Jakub Przybyło · 2026-03-03
 https://arxiv.org/abs/2603.02786

=== Source paper abstract / header ===
Abstract:Let $\mathcal{F}=\{A_1,A_2,\ldots,A_k\}$ be a collection of finite arithmetic progressions, where each $A_d$ is an initial segment of the set $D_d=\{d,2d,3d,\ldots\}$ of consecutive multiples of a positive integer $d$. Let $m(\mathcal{F})$ denote the minimum length of an interval containing pairwise disjoint \emph{shifted} copies of all members of the family $\mathcal{F}$.
We study this parameter in the following two cases: for a fixed positive integer $n$, (1) each progression in $\mathcal{F}$ has the form $A_d=D_d\cap\{1,2,\ldots,n\}$, and (2) all progressions $A_d$ of $\mathcal{F}$ have the same size $n$, that is, $A_d=D_d\cap \{1,2,\ldots, nd\}$. We in particular derive the following asymptotic estimates. In case (1), when $k=n$, we get $m(\mathcal{F})=\Theta(n^{3/2}/\ln n)$. In case (2), when $k=n$, we get $m(\mathcal{F})=\Theta(n^3/\ln n)$, while if $k>k_0(n)$, then $m(\mathcal{F}) < 3kn$. In both cases we additionally determine $m(\mathcal{F})$ asymptotically or settle its order of magnitude for all $k<n$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2603.02786 [math.CO]
 

 
  
 (or 
 arXiv:2603.02786v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2603.02786
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Jarosław Grytczuk [view email] 
 [v1]
 Tue, 3 Mar 2026 09:25:43 UTC (18 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Packing arithmetic progressions, by Noga Alon and 3 other authors
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
 | 2026-03
 

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
