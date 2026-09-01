Attack the following open graph-theory problem.

Catalog id: 2407.08927__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2407.08927__00/
Source paper: Tree Independence Number IV. Even-hole-free Graphs (arXiv:2407.08927)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: Polynomial-time MWIS on even-hole-free graphs
Does there exist a polynomial-time algorithm for the Maximum Weight Independent Set problem on even-hole-free graphs?

Context:
On even-hole-free graphs, Maximum Weight Clique is known to be polynomial-time solvable, but the question of whether a polynomial-time algorithm exists for Maximum Weight Independent Set remains open. This is in stark contrast to perfect graphs, for which polynomial-time algorithms have been known since 1981. The present paper gives a quasi-polynomial-time algorithm via a polylogarithmic tree independence number bound, but the polynomial-time question is not resolved.

=== Catalog page (statement + literature review) ===
MWIS polynomial-time on even-hole-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The source paper (arXiv:2407.08927, published at SODA 2025) establishes a quasi-polynomial-time algorithm for MWIS on even-hole-free graphs by proving that every n-vertex even-hole-free graph has a tree decomposition with each bag having independence number at most c log^{10} n; the polynomial-time question is explicitly left open. A 2026 preprint (arXiv:2604.01816) proves bounded treewidth (≤ 4) for the more restricted class of (even-hole, triangle)-free graphs, implying polynomial-time MWIS for that proper subclass, but the general even-hole-free case remains unresolved. No paper has been found that settles the polynomial-time question for all even-hole-free graphs.

 Cited literature (1)

 
 
 
partial (Even hole, triangle)-free graphs revisited
 (2026)
 

 
 Unknown (not extracted from abstract) · arXiv preprint · arXiv:2604.01816

Proves treewidth ≤ 4 for (theta, triangle, wac)-free graphs (a proper subclass of even-hole-free graphs also excluding triangles), implying polynomial-time MWIS for that restricted subclass but not for general even-hole-free graphs.
 

 

 Reviewer notes. The source paper itself (SODA 2025) is the strongest known positive result: quasi-polynomial time via tree independence number O(log^10 n). The paper explicitly notes that the quasi-polynomial bound is consistent with NP-hardness, so the complexity of MWIS on even-hole-free graphs remains open. The 2026 paper arXiv:2604.01816 about (even hole, triangle)-free graphs achieves treewidth ≤ 4 for a more restricted subclass; authors were not extractable from the abstract page within the 5-call cap.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. Does there exist a polynomial-time algorithm for the Maximum Weight Independent Set problem on even-hole-free graphs?

Context

On even-hole-free graphs, Maximum Weight Clique is known to be polynomial-time solvable, but the question of whether a polynomial-time algorithm exists for Maximum Weight Independent Set remains open. This is in stark contrast to perfect graphs, for which polynomial-time algorithms have been known since 1981. The present paper gives a quasi-polynomial-time algorithm via a polylogarithmic tree independence number bound, but the polynomial-time question is not resolved.

Notes. Stated in prose in the introduction without a labelled theorem environment; the paper provides quasi-polynomial-time progress but leaves polynomial-time open.

Source paper

 Tree Independence Number IV. Even-hole-free Graphs
 Maria Chudnovsky, Peter Gartland, Sepehr Hajebi, Daniel Lokshtanov, Sophie Spirkl · 2024-07-12
 https://arxiv.org/abs/2407.08927

=== Source paper abstract / header ===
Abstract:We prove that the tree independence number of every even-hole-free graph is at most polylogarithmic in its number of vertices. More explicitly, we prove that there exists a constant c>0 such that for every integer n>1 every n-vertex even-hole-free graph has a tree decomposition where each bag has stability (independence) number at most c log^10 n. This implies that the Maximum Weight Independent Set problem, as well as several other natural algorithmic problems that are known to be NP-hard in general, can be solved in quasi-polynomial time if the input graph is even-hole-free.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS)
 

 Cite as:
 arXiv:2407.08927 [math.CO]
 

 
  
 (or 
 arXiv:2407.08927v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2407.08927
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Lokshtanov [view email] 
 [v1]
 Fri, 12 Jul 2024 02:21:08 UTC (130 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Tree Independence Number IV. Even-hole-free Graphs, by Maria Chudnovsky and 4 other authors
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
 | 2024-07
 

 Change to browse by:
 
 cs
 cs.DM
 cs.DS
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
