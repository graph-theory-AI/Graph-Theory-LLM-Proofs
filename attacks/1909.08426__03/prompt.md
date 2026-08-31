Attack the following open graph-theory problem.

Catalog id: 1909.08426__03
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1909.08426__03/
Source paper: When Maximum Stable Set can be solved in FPT time (arXiv:1909.08426)

=== Catalog page (statement + literature review) ===
MIS FPT in Pℓ(t)-free Graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 2 from arXiv:1909.08426 asserts that MIS is FPT in $P_\ell(t)$-free graphs for all integers $t$ and $\ell$; as of May 2026 it remains open. The source paper itself establishes the $\ell=4$, first-coordinate-1 case (MIS FPT in $P(1,t,t,t)$-free graphs for every fixed $t\geq 1$). The smallest explicitly open instance, P$_7$-free graphs ($t=1$, $\ell=7$), is still not known to be FPT; a 2025 ISAAC paper proves polynomial-time tractability of CMSO$_2$-definable problems (including MIS) in P$_7$-free graphs of bounded clique number, which is a weaker and structurally different result from FPT on all P$_7$-free graphs.

 Cited literature (1)

 
 
 
partial Sparse Induced Subgraphs in P₇-Free Graphs of Bounded Clique Number
 (2025)
 

 
 authors not retrieved · ISAAC 2025 (LIPIcs) · doi:10.4230/LIPIcs.ISAAC.2025.20

Proves polynomial-time algorithms for CMSO₂-definable problems including MIS on P₇-free graphs of bounded clique number, extending prior quasipolynomial and polynomial results to this restricted subclass but not resolving FPT for general P₇-free graphs.
 

 

 Reviewer notes. No follow-up paper resolving the full conjecture or proving FPT for general P₇-free graphs was found across five web searches. The 2025 ISAAC paper (verified via WebFetch) makes progress on P₇-free graphs of bounded clique number in polynomial time, but does not cite 1909.08426 explicitly and addresses a different complexity notion than FPT. Authors of the ISAAC 2025 paper were not retrieved. The conjecture is relatively recent (~6 years) and the absence of resolution in the literature supports high-confidence open status.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any integers $t$ and $\ell$, MIS is FPT in $P_\ell(t)$-free graphs, where $P_\ell(t) = P(t, t, \ldots, t)$ with the sequence $t, t, \ldots, t$ of length $\ell$.

Context

This is described as a far more distant milestone than Conjecture 1, extending the FPT claim to clique-substituted paths of arbitrary length. The authors remark that even the parameterized complexity of MIS in $P_7$-free graphs (the $t=1$, $\ell=7$ case) is currently open.

Notes. PDF source.

Source paper

 When Maximum Stable Set can be solved in FPT time
 Édouard Bonnet, Nicolas Bousquet, Stéphan Thomassé, Rémi Watrigant · 2019-09-18
 https://arxiv.org/abs/1909.08426
 PDF source

=== Source paper abstract / header ===
Abstract:Maximum Independent Set (MIS for short) is in general graphs the paradigmatic $W[1]$-hard problem. In stark contrast, polynomial-time algorithms are known when the inputs are restricted to structured graph classes such as, for instance, perfect graphs (which includes bipartite graphs, chordal graphs, co-graphs, etc.) or claw-free graphs. In this paper, we introduce some variants of co-graphs with parameterized noise, that is, graphs that can be made into disjoint unions or complete sums by the removal of a certain number of vertices and the addition/deletion of a certain number of edges per incident vertex, both controlled by the parameter. We give a series of FPT Turing-reductions on these classes and use them to make some progress on the parameterized complexity of MIS in $H$-free graphs. We show that for every fixed $t \geqslant 1$, MIS is FPT in $P(1,t,t,t)$-free graphs, where $P(1,t,t,t)$ is the graph obtained by substituting all the vertices of a four-vertex path but one end of the path by cliques of size $t$. We also provide randomized FPT algorithms in dart-free graphs and in cricket-free graphs. This settles the FPT/W[1]-hard dichotomy for five-vertex graphs $H$.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Discrete Mathematics (cs.DM)
 
 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:1909.08426 [cs.DS]
 

 
  
 (or 
 arXiv:1909.08426v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1909.08426
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Wed, 18 Sep 2019 13:04:39 UTC (115 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled When Maximum Stable Set can be solved in FPT time, by \'Edouard Bonnet and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2019-09
 

 Change to browse by:
 
 cs
 cs.CC
 cs.DM
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Nicolas Bousquet
Stéphan Thomassé
Rémi Watrigant 

 

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
