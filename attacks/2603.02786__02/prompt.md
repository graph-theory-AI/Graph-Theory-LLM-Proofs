Attack the following open graph-theory problem.

Catalog id: 2603.02786__02
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2603.02786__02/
Source paper: Packing arithmetic progressions (arXiv:2603.02786)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 5
For every $k$ satisfying $\Omega(\sqrt{n})=k<\sqrt{n}$, we have $m_{k}(n)\sim\left(1-\frac{k^{2}}{3n}\right)\frac{k}{\ln k}\cdot n$.

Context:
If Conjecture 1 holds, it also resolves $m_k(n)$ asymptotically for $k\geqslant\sqrt{n}$ via Theorem 4. The only remaining open case is $k<\sqrt{n}$ with $k\not=o(\sqrt{n})$, which this conjecture addresses.

=== Catalog page (statement + literature review) ===
AP packing asymptotics for k near √n — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 5 of arXiv:2603.02786 proposes the asymptotic formula $m_k(n) \sim \left(1 - \frac{k^2}{3n}\right) \frac{k}{\ln k} \cdot n$ for every $k$ satisfying $\Omega(\sqrt{n}) = k < \sqrt{n}$. The paper establishes matching upper and lower bounds with this correction factor in Theorem 4 but stops short of closing the gap to a full asymptotic. No follow-up paper resolving or refuting this conjecture was found in the indexed literature as of May 2026, consistent with the paper being only two months old.

 Reviewer notes. No follow-up found. The paper is very recent (March 2026). Conjecture 5 addresses the only remaining open asymptotic regime for m_k(n): the intermediate range Omega(sqrt(n)) = k < sqrt(n). The conjectured formula m_k(n) ~ (1 - k^2/(3n)) * k/ln(k) * n interpolates between the small-k result m_k(n) ~ kn/ln(k) and the large-k regime resolved via Theorem 4 assuming Conjecture 1.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every $k$ satisfying $\Omega(\sqrt{n})=k<\sqrt{n}$, we have $m_{k}(n)\sim\left(1-\frac{k^{2}}{3n}\right)\frac{k}{\ln k}\cdot n$.

Context

If Conjecture 1 holds, it also resolves $m_k(n)$ asymptotically for $k\geqslant\sqrt{n}$ via Theorem 4. The only remaining open case is $k<\sqrt{n}$ with $k\not=o(\sqrt{n})$, which this conjecture addresses.

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
