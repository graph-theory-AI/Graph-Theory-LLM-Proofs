Attack the following open graph-theory problem.

Catalog id: 2111.00282__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2111.00282__00/
Source paper: Twin-width VI: the lens of contraction sequences (arXiv:2111.00282)

=== Extracted statement (catalog JSON) ===
Title: Open Challenge: Efficient Approximation of Twin-Width for Unordered Graphs
Efficiently approximating twin-width (that is, returning an $f(d)$-sequence when the twin-width of the input is at most $d$) remains an open challenge for unordered graphs.

Context:
The authors note that efficient approximation of twin-width has been achieved for classes of totally ordered binary structures and for all mentioned classes of bounded twin-width (bounded tree-width, proper minor-closed, hereditary subclasses of permutation graphs, etc.), but the problem is unresolved for general unordered graphs. This open challenge is stated in the introduction as a key missing piece in the twin-width landscape.

=== Catalog page (statement + literature review) ===
Twin-width approximation for unordered graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The open challenge of efficiently approximating twin-width for unordered graphs remains unresolved for general graphs, as confirmed by Bonnet's own open-questions page (updated 2025). Partial progress exists: an FPT approximation algorithm has been found for graphs with small feedback edge number (Balabán, Ganian, Rocton 2023), but no XP or FPT approximation is known for the general unordered case. Exact computation of twin-width is NP-hard—deciding whether twin-width is at most 4 is NP-complete.

 Cited literature (1)

 
 
 
partial Computing Twin-Width Parameterized by the Feedback Edge Number
 (2023)
 

 
 Jakub Balabán, Robert Ganian, Mathis Rocton · arXiv preprint · arXiv:2310.08243

Provides an FPT approximation algorithm for twin-width on graphs parameterized by feedback edge number, computing an ℓ-contraction sequence or certifying twin-width ≥ ℓ; does not address the general unordered graph case.
 

 

 Reviewer notes. Bonnet's open questions page (https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html) explicitly lists FPT approximation for general unordered graphs as still the missing piece; the challenge is open with high confidence. Partial progress exists only for restricted parameterizations such as feedback edge number.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Efficiently approximating twin-width (that is, returning an $f(d)$-sequence when the twin-width of the input is at most $d$) remains an open challenge for unordered graphs.

Context

The authors note that efficient approximation of twin-width has been achieved for classes of totally ordered binary structures and for all mentioned classes of bounded twin-width (bounded tree-width, proper minor-closed, hereditary subclasses of permutation graphs, etc.), but the problem is unresolved for general unordered graphs. This open challenge is stated in the introduction as a key missing piece in the twin-width landscape.

Notes. Stated in running prose in the introduction without a labelled theorem environment. The PDF extraction is incomplete — the paper content cuts off mid-sentence in Section 2.1 (before the bulk of the technical sections), so additional labelled conjectures/problems/questions in later sections of the paper are not captured here.

Source paper

 Twin-width VI: the lens of contraction sequences
 Édouard Bonnet, Eun Jung Kim, Amadeus Reinald, Stéphan Thomassé · 2022-05-31
 https://arxiv.org/abs/2111.00282
 PDF source

=== Source paper abstract / header ===
Abstract:A contraction sequence of a graph consists of iteratively merging two of its vertices until only one vertex remains. The recently introduced twin-width graph invariant is based on contraction sequences. More precisely, if one puts red edges between two vertices representing non-homogeneous subsets, the twin-width is the minimum integer $d$ such that a contraction sequence keeps red degree at most $d$. By changing the condition imposed on the trigraphs (i.e., graphs with some edges being red) and possibly slightly tweaking the notion of contractions, we show how to characterize the well-established bounded rank-width, tree-width, linear rank-width, path-width, and proper minor-closed classes by means of contraction sequences. As an application we give a transparent alternative proof of the celebrated Courcelle's theorem (actually of its generalization by Courcelle, Makowsky, and Rotics), that MSO$_2$ (resp. MSO$_1$) model checking on graphs with bounded tree-width (resp. bounded rank-width) is fixed-parameter tractable in the size of the input sentence.
We then explore new avenues along the general theme of contraction sequences both in order to refine the landscape between bounded tree-width and bounded twin-width (via spanning twin-width) and to capture more general classes than bounded twin-width. To this end, we define an oriented version of twin-width, where appearing red edges are oriented away from the newly contracted vertex, and the mere red out-degree should remain bounded. Surprisingly, classes of bounded oriented twin-width coincide with those of bounded twin-width. Finally we examine, from an algorithmic standpoint, the concept of partial contraction sequences, where, instead of terminating on a single-vertex graph, the sequence ends when reaching a particular target class.
 

 
 
 
 Comments:
 27 pages, 3 figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Logic in Computer Science (cs.LO); Combinatorics (math.CO)
 
 
 MSC classes:
 68R10, 05C85
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2111.00282 [cs.DS]
 

 
  
 (or 
 arXiv:2111.00282v2 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2111.00282
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Sat, 30 Oct 2021 16:28:03 UTC (202 KB)

 [v2]
 Tue, 31 May 2022 21:49:10 UTC (204 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width VI: the lens of contraction sequences, by \'Edouard Bonnet and 3 other authors
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
 | 2021-11
 

 Change to browse by:
 
 cs
 cs.DM
 cs.LO
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Eun Jung Kim
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
