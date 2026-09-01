Attack the following open graph-theory problem.

Catalog id: 1407.5833__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1407.5833__00/
Source paper: Identifying codes in hereditary classes of graphs and VC-dimension (arXiv:1407.5833)

=== Extracted statement (catalog JSON) ===
Title: VC-Dimension Dichotomy for Identifying Codes (Approximation)
For any hereditary class of graphs $\mathcal{C}$, either (1) the minimum identifying code size has a logarithmic lower bound and Min Id Code is log-APX-hard in $\mathcal{C}$, or (2) the minimum identifying code size has a polynomial lower bound and Min Id Code admits a constant factor approximation algorithm in $\mathcal{C}$.

Context:
Surveying known results in Table 1, the authors observe that hereditary graph classes appear to split into two regimes according to their VC-dimension: infinite VC-dimension corresponds to a logarithmic lower bound and log-APX-hardness, while finite VC-dimension corresponds to a polynomial lower bound and (conjecturally) constant-factor approximability. The paper aims to shed light on the validity of this dichotomy for all hereditary classes.

=== Catalog page (statement + literature review) ===
VC-dimension dichotomy for identifying codes approximation — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The source paper (arXiv:1407.5833, published SIAM Journal on Discrete Mathematics 29(4):2047–2064, 2015) proves both halves of the size dichotomy: infinite VC-dimension forces a logarithmic lower bound and log-APX-hardness, while finite VC-dimension forces a polynomial lower bound. The conjectured complementary algorithmic half — that finite VC-dimension also entails constant-factor approximability of Min Identifying Code — remains open; four targeted web searches found no follow-up paper proving or disproving this claim as of May 2026.

 Reviewer notes. No follow-up paper was found that resolves the conjectured constant-factor approximability of Min Identifying Code in finite VC-dimension hereditary classes. The paper itself (confirmed via WebFetch of the arXiv abstract page) notes that C₄-free bipartite graphs (finite VC-dimension) exhibit non-trivial intermediate behavior, illustrating the difficulty of the algorithmic half of the dichotomy. The conjecture is at least 9 years old; absence of a resolution in indexed literature suggests it is a hard open problem. Confidence is medium rather than high because the paper is old enough that a resolution in a journal paper not prominently indexed on arXiv could have been missed.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. For any hereditary class of graphs $\mathcal{C}$, either (1) the minimum identifying code size has a logarithmic lower bound and Min Id Code is log-APX-hard in $\mathcal{C}$, or (2) the minimum identifying code size has a polynomial lower bound and Min Id Code admits a constant factor approximation algorithm in $\mathcal{C}$.

Context

Surveying known results in Table 1, the authors observe that hereditary graph classes appear to split into two regimes according to their VC-dimension: infinite VC-dimension corresponds to a logarithmic lower bound and log-APX-hardness, while finite VC-dimension corresponds to a polynomial lower bound and (conjecturally) constant-factor approximability. The paper aims to shed light on the validity of this dichotomy for all hereditary classes.

Notes. The lower-bound half of the dichotomy is fully proved as Theorem 2.2. The approximation half is shown to fail in general: C4-free bipartite graphs have finite VC-dimension but Min Id Code cannot be approximated within a factor of c log|V| for some c > 0 (Thm 4.3). The question of which finite VC-dimension classes admit constant-factor approximations remains open (Table 2 lists Girth ≥ 5, Chordal bipartite, Unit disk, and Undirected path graphs as open). PDF source — math notation may be garbled; full paper text is truncated so later explicit problem statements may be missing.

Source paper

 Identifying codes in hereditary classes of graphs and VC-dimension
 Nicolas Bousquet, Aurélie Lagoutte, Zhentao Li, Aline Parreau, Stéphan Thomassé · 2017-04-14
 https://arxiv.org/abs/1407.5833
 PDF source

=== Source paper abstract / header ===
Abstract:An identifying code of a graph is a subset of its vertices such that every vertex of the graph is uniquely identified by the set of its neighbours within the code. We show a dichotomy for the size of the smallest identifying code in classes of graphs closed under induced subgraphs. Our dichotomy is derived from the VC-dimension of the considered class C, that is the maximum VC-dimension over the hypergraphs formed by the closed neighbourhoods of elements of C. We show that hereditary classes with infinite VC-dimension have infinitely many graphs with an identifying code of size logarithmic in the number of vertices while classes with finite VC-dimension have a polynomial lower bound.
We then turn to approximation algorithms. We show that the problem of finding a smallest identifying code in a given graph from some class is log-APX-hard for any hereditary class of infinite VC-dimension. For hereditary classes of finite VC-dimension, the only known previous results show that we can approximate the identifying code problem within a constant factor in some particular classes, e.g. line graphs, planar graphs and unit interval graphs. We prove that it can be approximate within a factor 6 for interval graphs. In contrast, we show that on C_4-free bipartite graphs (a class of finite VC-dimension) it cannot be approximated to within a factor of this http URL(|V|) for some c>0.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1407.5833 [cs.DM]
 

 
  
 (or 
 arXiv:1407.5833v3 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1407.5833
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 SIAM Journal of Discrete Mathematics, 29(4):2047-2064, 2015
 

 
 
 Related DOI:
 
 https://doi.org/10.1137/14097879X

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Aurélie Lagoutte [view email] 
 [v1]
 Tue, 22 Jul 2014 12:12:57 UTC (135 KB)

 [v2]
 Wed, 22 Apr 2015 10:12:22 UTC (135 KB)

 [v3]
 Fri, 14 Apr 2017 12:39:02 UTC (152 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Identifying codes in hereditary classes of graphs and VC-dimension, by Nicolas Bousquet and 4 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2014-07
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Nicolas Bousquet
Aurélie Lagoutte
Zhentao Li
Aline Parreau
Stéphan Thomassé 

 

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
