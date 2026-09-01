Attack the following open graph-theory problem.

Catalog id: 2212.02737__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2212.02737__00/
Source paper: Induced subgraphs and tree-decompositions VII. Basic obstructions in $H… (arXiv:2212.02737)

=== Extracted statement (catalog JSON) ===
Title: Question: finite families yielding clean H-free classes
For which finite families $\mathcal{H}$ of graphs is the class of all $\mathcal{H}$-free graphs clean?

Context:
After proving Theorem 1.5 — which characterizes all single graphs $H$ for which the class $\mathcal{F}_H$ of $H$-free graphs is clean (precisely the subdivided star forests) — the authors pose the next natural step. They observe that any finite set $\mathcal{H}$ containing a subdivided star forest yields a clean class, but note that the converse fails (e.g., $\mathcal{H}=\{H, K_3\}$ for the unique double star on six vertices is also clean). A full description is deferred to a companion paper [6] by four of the five authors.

=== Catalog page (statement + literature review) ===
Clean H-free classes from finite families — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The companion paper (arXiv:2311.05066, published in Advances in Combinatorics) by Alecu, Chudnovsky, Hajebi, and Spirkl proves Theorem 1.4: for a finite set $\mathcal{H}$ of graphs, the class of all $\mathcal{H}$-free graphs is clean if and only if there are only finitely many $n \in \mathbb{N}$ for which an $\mathcal{H}$-free $n$-array exists. This provides a complete necessary and sufficient condition in terms of $n$-arrays and reduces the question to understanding when $\mathcal{H}$-free arrays can be constructed for all large $n$. A direct structural characterization of exactly which families $\mathcal{H}$ satisfy this array condition — analogous to the single-graph case where $H$ must be a subdivided star forest — does not appear to follow immediately from these results.

 Cited literature (1)

 
 
 
partial Induced subgraphs and tree decompositions XIII. Basic obstructions in $\mathcal{H}$-free graphs for finite $\mathcal{H}$
 (2024)
 

 
 Bogdan Alecu, Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · Advances in Combinatorics · arXiv:2311.05066

Proves Theorem 1.4: the class of $\mathcal{H}$-free graphs is clean if and only if only finitely many $n$ admit an $\mathcal{H}$-free $n$-array; this is the companion paper [6] promised in arXiv:2212.02737, addressing the finite-family question via an array-based characterization.
 

 

 Reviewer notes. The companion paper [6] referenced in arXiv:2212.02737 is arXiv:2311.05066 (Part XIII of the series), by four of the five original authors (Alecu, Chudnovsky, Hajebi, Spirkl — without Abrishami), submitted to arXiv on November 9, 2023 and published in Advances in Combinatorics. It fully resolves the question in terms of $n$-arrays (Theorem 1.4), but the status is classified 'partial' because the array condition itself may not admit a simple structural description of $\mathcal{H}$; Theorem 1.6 additionally connects the condition to 'tasselled' families. A purely structural characterization of the clean finite families analogous to the single-graph case appears to remain open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. For which finite families $\mathcal{H}$ of graphs is the class of all $\mathcal{H}$-free graphs clean?

Context

After proving Theorem 1.5 — which characterizes all single graphs $H$ for which the class $\mathcal{F}_H$ of $H$-free graphs is clean (precisely the subdivided star forests) — the authors pose the next natural step. They observe that any finite set $\mathcal{H}$ containing a subdivided star forest yields a clean class, but note that the converse fails (e.g., $\mathcal{H}=\{H, K_3\}$ for the unique double star on six vertices is also clean). A full description is deferred to a companion paper [6] by four of the five authors.

Notes. Posed as a natural next step in running prose (no labelled theorem environment). The companion paper [6] is announced to resolve it; PDF source is truncated after Section 2, so later sections may contain additional items not captured here.

Source paper

 Induced subgraphs and tree-decompositions VII. Basic obstructions in $H$-free graphs
 Tara Abrishami, Bogdan Alecu, Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · 2023-11-07
 https://arxiv.org/abs/2212.02737
 PDF source

=== Source paper abstract / header ===
Abstract:We say a class $\mathcal{C}$ of graphs is clean if for every positive integer $t$ there exists a positive integer $w(t)$ such that every graph in $\mathcal{C}$ with treewidth more than $w(t)$ contains an induced subgraph isomorphic to one of the following: the complete graph $K_t$, the complete bipartite graph $K_{t,t}$, a subdivision of the $(t\times t)$-wall or the line graph of a subdivision of the $(t \times t)$-wall. In this paper, we adapt a method due to Lozin and Razgon (building on earlier ideas of Weißauer) to prove that the class of all $H$-free graphs (that is, graphs with no induced subgraph isomorphic to a fixed graph $H$) is clean if and only if $H$ is a forest whose components are subdivided stars.
Their method is readily applied to yield the above characterization. However, our main result is much stronger: for every forest $H$ as above, we show that forbidding certain connected graphs containing $H$ as an induced subgraph (rather than $H$ itself) is enough to obtain a clean class of graphs. Along the proof of the latter strengthening, we build on a result of Davies and produce, for every positive integer $\eta$, a complete description of unavoidable connected induced subgraphs of a connected graph $G$ containing $\eta$ vertices from a suitably large given set of vertices in $G$. This is of independent interest, and will be used in subsequent papers in this series.
 

 
 
 
 Comments:
 Accepted manuscript; see DOI for journal version
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2212.02737 [math.CO]
 

 
  
 (or 
 arXiv:2212.02737v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2212.02737
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Combinatorial Theory, Series B, Volume 164, January 2024, Pages 443-472
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.jctb.2023.10.008

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sophie Spirkl [view email] 
 [v1]
 Tue, 6 Dec 2022 04:02:21 UTC (35 KB)

 [v2]
 Thu, 5 Jan 2023 05:41:17 UTC (36 KB)

 [v3]
 Tue, 7 Nov 2023 16:40:01 UTC (74 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced subgraphs and tree-decompositions VII. Basic obstructions in $H$-free graphs, by Tara Abrishami and 4 other authors
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
 | 2022-12
 

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
