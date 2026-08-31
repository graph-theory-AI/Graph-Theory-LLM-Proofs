Attack the following open graph-theory problem.

Catalog id: 2603.17630__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2603.17630__01/
Source paper: Anticoncentration of random spanning trees in graphs with large minimum… (arXiv:2603.17630)

=== Catalog page (statement + literature review) ===
Non-isomorphic spanning trees count lower bound — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 4.2 from arXiv:2603.17630 (March 2026) asserts that Ω(n^{d-1}) is the correct lower bound for the number of non-isomorphic spanning trees in connected n-vertex graphs with minimum degree at least d, with K_{d,n-d} as the conjectured extremal example. The same paper establishes the weaker bound n^{Ω(d)} (tight only up to the constant in the exponent), which proves Lee's conjecture in strong form but falls short of the d-1 exponent claimed in Conjecture 4.2. No follow-up paper resolving or making partial progress on this specific conjecture was found in the indexed literature as of May 2026.

 Reviewer notes. The conjecture is very recent (March 2026). The source paper itself proves n^{Omega(d)} non-isomorphic spanning trees for graphs of minimum degree d, which is tight only up to the constant in the exponent; Conjecture 4.2 asks for the sharp exponent d-1, achieved by K_{d,n-d}. The predecessor paper arXiv:2601.07740 (Anticoncentration of random spanning trees in almost regular graphs) established a similar result for almost regular graphs and predates the source paper. No follow-up addressing Conjecture 4.2 was found after 5 web calls.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $d$ be sufficiently large, and let $n$ be sufficiently large relative to $d$. Suppose that $G$ is a connected graph with $n$ vertices and minimum degree at least $d$. Then, the number of non-isomorphic spanning trees of $G$ is at least $\Omega(n^{d-1})$.

Context

The anticoncentration property of Conjecture 4.1 would imply only $n^{(1/2-o_n(1))(d-1)}$ non-isomorphic spanning trees, but $K_{d,n-d}$ has $\Omega(n^{d-1})$ non-isomorphic spanning trees. The authors conjecture that this larger quantity gives an essentially optimal lower bound, with $K_{d,n-d}$ being an extremal example.

Source paper

 Anticoncentration of random spanning trees in graphs with large minimum degree
 Veronica Bitonti, Lukas Michel, Alex Scott · 2026-03-18
 https://arxiv.org/abs/2603.17630

=== Source paper abstract / header ===
Abstract:A classical result by Otter shows that the complete graph has an exponential number of non-isomorphic spanning trees. This was recently extended by Lee to every almost regular graph of sufficiently large degree.
In this paper, we consider graphs of large minimum degree. We show that every connected graph $G$ with $n$ vertices and minimum degree $d$ has at least $n^{\Omega(d)}$ non-isomorphic spanning trees. This is tight up to the constant factor in the exponent. In fact, we prove the following anticoncentration result: if $\mathcal{T}$ is a uniformly random spanning tree of $G$, then for every tree $T$, the probability that $\mathcal{T}$ is isomorphic to $T$ is at most $n^{-\Omega(d)}$. This proves a conjecture of Lee in a strong form.
 

 
 
 
 Comments:
 16 pages
 

 Subjects:
 
 Combinatorics (math.CO); Probability (math.PR)
 

 Cite as:
 arXiv:2603.17630 [math.CO]
 

 
  
 (or 
 arXiv:2603.17630v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2603.17630
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Lukas Michel [view email] 
 [v1]
 Wed, 18 Mar 2026 11:51:31 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Anticoncentration of random spanning trees in graphs with large minimum degree, by Veronica Bitonti and 2 other authors
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
 math.PR
 

 

 

 
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
