Attack the following open graph-theory problem.

Catalog id: 2209.12023__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2209.12023__00/
Source paper: Twin-width V: linear minors, modular counting, and matrix multiplication (arXiv:2209.12023)

=== Catalog page (statement + literature review) ===
Twin-width of matrices over infinite fields — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The open question asks whether bounded twin-width for matrix classes over infinite fields (starting with Q) can be characterized via linear-minor closure: a class of matrices over Q has bounded twin-width if and only if its closure under linear minors is not the set of all matrices. The paper's main results on FPT matrix multiplication and linear-minor characterization are proved only for finite fields F_q, and no definition of twin-width via contraction sequences is given for matrices over Q. A wide web search (5 calls) found no published or preprint follow-up that addresses this specific question about infinite fields.

 Reviewer notes. No follow-up found addressing twin-width over infinite fields specifically. The STACS 2023 published version of the paper also confines all results to finite alphabets and finite fields. The open question remains unresolved as of May 2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. An intriguing question concerns the existence of such results over infinite fields (starting with $\mathbb{Q}$). We do not have a direct definition of twin-width of matrices over $\mathbb{Q}$ based on contraction sequences. However linear-minor freeness naturally carries to infinite fields, and thus, it is natural to consider that a class of matrices over $\mathbb{Q}$ has bounded twin-width if its closure under linear minors is not the set of all matrices.

Context

After establishing FPT matrix multiplication algorithms for matrices over finite fields $\mathbb{F}_q$ with bounded twin-width (Theorems 5–7), the authors raise the question of whether analogous results hold for matrices over infinite fields such as $\mathbb{Q}$. The text is truncated at this point, so the precise formulation of the question (likely involving the grid rank of a matrix) is not fully visible.

Notes. PDF source — the statement is cut off mid-sentence after the introduction of grid rank; full question not visible in the extracted text.

Source paper

 Twin-width V: linear minors, modular counting, and matrix multiplication
 Édouard Bonnet, Ugo Giocanti, Patrice Ossona de Mendez, Stéphan Thomassé · 2022-09-24
 https://arxiv.org/abs/2209.12023
 PDF source

=== Source paper abstract / header ===
Abstract:We continue developing the theory around the twin-width of totally ordered binary structures, initiated in the previous paper of the series. We first introduce the notion of parity and linear minors of a matrix, which consists of iteratively replacing consecutive rows or consecutive columns with a linear combination of them. We show that a matrix class has bounded twin-width if and only if its linear-minor closure does not contain all matrices. We observe that the fixed-parameter tractable algorithm for first-order model checking on structures given with an $O(1)$-sequence (certificate of bounded twin-width) and the fact that first-order transductions of bounded twin-width classes have bounded twin-width, both established in Twin-width I, extend to first-order logic with modular counting quantifiers. We make explicit a win-win argument obtained as a by-product of Twin-width IV, and somewhat similar to bidimensionality, that we call rank-bidimensionality. Armed with the above-mentioned extension to modular counting, we show that the twin-width of the product of two conformal matrices $A, B$ over a finite field is bounded by a function of the twin-width of $A$, of $B$, and of the size of the field. Furthermore, if $A$ and $B$ are $n \times n$ matrices of twin-width $d$ over $\mathbb F_q$, we show that $AB$ can be computed in time $O_{d,q}(n^2 \log n)$. We finally present an ad hoc algorithm to efficiently multiply two matrices of bounded twin-width, with a single-exponential dependence in the twin-width bound: If the inputs are given in a compact tree-like form, called twin-decomposition (of width $d$), then two $n \times n$ matrices $A, B$ over $\mathbb F_2$, a twin-decomposition of $AB$ with width $2^{d+o(d)}$ can be computed in time $4^{d+o(d)}n$ (resp. $4^{d+o(d)}n^{1+\varepsilon}$), and entries queried in doubly-logarithmic (resp. constant) time.
 

 
 
 
 Comments:
 45 pages, 9 figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Logic in Computer Science (cs.LO); Combinatorics (math.CO)
 
 
 MSC classes:
 68W01
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2209.12023 [cs.DS]
 

 
  
 (or 
 arXiv:2209.12023v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2209.12023
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Sat, 24 Sep 2022 14:41:54 UTC (176 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width V: linear minors, modular counting, and matrix multiplication, by \'Edouard Bonnet and 3 other authors
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
 | 2022-09
 

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

 
 

 

 
 
 1 blog link
 (what is this?)
 

 

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
