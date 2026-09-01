Attack the following open graph-theory problem.

Catalog id: 2011.08049__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2011.08049__00/
Source paper: Efficient polynomial-time approximation scheme for the genus of dense g… (arXiv:2011.08049)

=== Extracted statement (catalog JSON) ===
Title: Open Problem (Spherical Density Regime)
Determine whether efficient constant-factor approximation algorithms exist for the genus of graphs with average degree at most 6 (spherical density regime), or prove that approximating the genus in this regime is hard.

Context:
The authors partition the genus approximation problem into three density regimes. The spherical density regime (average degree $\leq 6$) is described as 'probably most interesting'; no efficient constant-factor approximation algorithm is known for it, and the authors identify resolving this as 'the major open problem'. Conjecture 1.1 (APX-hardness for cubic graphs) is the leading candidate resolution.

=== Catalog page (statement + literature review) ===
Genus approximation hardness in spherical density regime — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No resolution of the spherical density regime open problem has been found in the literature. The source paper (published in J. ACM 71(6), 2024) identifies the genus approximation problem for graphs with average degree at most 6 as the major open problem in its density-regime framework; Conjecture 1.1 of the paper (APX-hardness for cubic graphs) is the authors' leading candidate resolution but remains unproved. A wide search across arXiv, Jing's research page, and general queries on genus approximation hardness returned no follow-up paper addressing either the spherical regime or the APX-hardness conjecture for cubic graphs.

 Reviewer notes. The open problem has two possible resolutions: (a) an efficient constant-factor approximation algorithm for genus in the spherical density regime (average degree ≤ 6), or (b) a proof that approximation is hard in this regime. Conjecture 1.1 of the paper conjectures APX-hardness for cubic graphs as the most likely resolution; this conjecture itself remains open. No follow-up found in indexed literature as of 2026-05-14.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Informal. Determine whether efficient constant-factor approximation algorithms exist for the genus of graphs with average degree at most 6 (spherical density regime), or prove that approximating the genus in this regime is hard.

Context

The authors partition the genus approximation problem into three density regimes. The spherical density regime (average degree $\leq 6$) is described as 'probably most interesting'; no efficient constant-factor approximation algorithm is known for it, and the authors identify resolving this as 'the major open problem'. Conjecture 1.1 (APX-hardness for cubic graphs) is the leading candidate resolution.

Notes. Stated in prose: 'resolving this is the major open problem'; no formal labelled theorem environment.

Source paper

 Efficient polynomial-time approximation scheme for the genus of dense graphs
 Yifan Jing, Bojan Mohar · 2024-08-27
 https://arxiv.org/abs/2011.08049

=== Source paper abstract / header ===
Abstract:The main results of this paper provide an Efficient Polynomial-Time Approximation Scheme (EPTAS) for approximating the genus (and non-orientable genus) of dense graphs. By dense we mean that $|E(G)|\ge \alpha |V(G)|^2$ for some fixed $\alpha>0$. While a constant factor approximation is trivial for this class of graphs, approximations with factor arbitrarily close to 1 need a sophisticated algorithm and complicated mathematical justification. More precisely, we provide an algorithm that for a given (dense) graph $G$ of order $n$ and given $\varepsilon>0$, returns an integer $g$ such that $G$ has an embedding into a surface of genus $g$, and this is $\varepsilon$-close to a minimum genus embedding in the sense that the minimum genus $\mathsf{g}(G)$ of $G$ satisfies: $\mathsf{g}(G)\le g\le (1+\varepsilon)\mathsf{g}(G)$. The running time of the algorithm is $O(f(\varepsilon)\,n^2)$, where $f(\cdot)$ is an explicit function. Next, we extend this algorithm to also output an embedding (rotation system) whose genus is $g$. This second algorithm is an Efficient Polynomial-time Randomized Approximation Scheme (EPRAS) and runs in time $O(f_1(\varepsilon)\,n^2)$.
 

 
 
 
 Comments:
 36 pages. An extended abstract of the preliminary version of this paper appeared in FOCS 2018; to appear in JACM
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2011.08049 [math.CO]
 

 
  
 (or 
 arXiv:2011.08049v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2011.08049
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Yifan Jing [view email] 
 [v1]
 Mon, 16 Nov 2020 16:01:58 UTC (109 KB)

 [v2]
 Tue, 27 Aug 2024 00:11:34 UTC (109 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Efficient polynomial-time approximation scheme for the genus of dense graphs, by Yifan Jing and 1 other authors
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
 | 2020-11
 

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
