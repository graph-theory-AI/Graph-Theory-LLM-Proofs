Attack the following open graph-theory problem.

Catalog id: 2603.02786__04
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2603.02786__04/
Source paper: Packing arithmetic progressions (arXiv:2603.02786)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 7
For every fixed $n$ and $k$ tending to infinity, we have $M_{k}(n)=(1+o(1))nk$.

Context:
Concerns packing of $k$ arithmetic progressions of the form $B_d=\{d,2d,\ldots,nd\}$ for $d=1,2,\ldots,k$ with $n$ fixed. The authors suspect the trivial lower bound of $nk$ is asymptotically correct as $k\to\infty$.

=== Catalog page (statement + literature review) ===
Trivial lower bound tight for AP packing — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 7 of arXiv:2603.02786 asserts that for fixed n and k tending to infinity, the minimum interval length M_k(n) needed to pack the arithmetic progressions B_d = {d, 2d, ..., nd} for d = 1, ..., k satisfies M_k(n) = (1+o(1))nk, i.e., the trivial lower bound nk is asymptotically tight. The paper itself establishes Theorem 3, which proves M_k(n) < 3nk for sufficiently large k (beyond a threshold k_0(n)), confirming the right order of magnitude but with a constant factor of 3 instead of 1. No follow-up papers resolving the conjecture were found in the literature, consistent with the paper's very recent publication date of March 2026.

 Reviewer notes. No follow-up papers found. The paper is very recent (March 2026). The authors' own Theorem 3 provides a partial result: M_k(n) < 3nk for k > k_0(n), which establishes the correct order but leaves the asymptotic constant open. Conjecture 7 predicts the constant is 1.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every fixed $n$ and $k$ tending to infinity, we have $M_{k}(n)=(1+o(1))nk$.

Context

Concerns packing of $k$ arithmetic progressions of the form $B_d=\{d,2d,\ldots,nd\}$ for $d=1,2,\ldots,k$ with $n$ fixed. The authors suspect the trivial lower bound of $nk$ is asymptotically correct as $k\to\infty$.

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
