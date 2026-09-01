Attack the following open graph-theory problem.

Catalog id: 1904.12273__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1904.12273__00/
Source paper: Detecting a long odd hole (arXiv:1904.12273)

=== Extracted statement (catalog JSON) ===
Title: Open Problem (induced st-path of excess length three)
Is there a polynomial-time algorithm to test whether a graph contains an induced path between specified vertices $s, t$ of length at least three more than the shortest $st$-path?

Context:
Berger, Spirkl, and Seymour (including a co-author of the present paper) have a poly-time algorithm to detect an induced $st$-path longer than the shortest $st$-path. Whether a poly-time algorithm exists to detect one that is at least three longer remains open, as noted in the introduction.

=== Catalog page (statement + literature review) ===
Poly-time excess-3 induced st-path detection — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No polynomial-time algorithm and no NP-hardness proof is known for detecting an induced st-path of length at least three more than the shortest st-path. The related and strictly easier problem of excess ≥ 1 was solved in polynomial time by Berger, Spirkl, and Seymour (arXiv:2005.12861, 2020), with the running time subsequently improved from O(n^{18}) to O(n^{4.75}) by Chiu and Lu (arXiv:2109.15268, 2021); neither work addresses excess ≥ 3 or the intermediate case of excess ≥ 2.

 Cited literature (1)

 
 
 
partial Blazing a Trail via Matrix Multiplications: A Faster Algorithm for Non-shortest Induced Paths
 (2021)
 

 
 Jia-Hao Chiu, Hsueh-I Lu · arXiv preprint · arXiv:2109.15268

Improves the polynomial algorithm for detecting an induced st-path longer than the shortest (excess ≥ 1) from O(n^{18}) to O(n^{4.75}) via Boolean matrix multiplications, but does not address the open problem of excess ≥ 3.
 

 

 Reviewer notes. No follow-up resolving the excess ≥ 3 case was found. The contemporaneous paper arXiv:2005.12861 (Berger, Spirkl, Seymour; arXiv 2020, journal Discrete Mathematics 2021) solved the easier excess ≥ 1 problem polynomially. The intermediate cases (excess = 2 or excess = 3) remain open with no complexity determination in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Is there a polynomial-time algorithm to test whether a graph contains an induced path between specified vertices $s, t$ of length at least three more than the shortest $st$-path?

Context

Berger, Spirkl, and Seymour (including a co-author of the present paper) have a poly-time algorithm to detect an induced $st$-path longer than the shortest $st$-path. Whether a poly-time algorithm exists to detect one that is at least three longer remains open, as noted in the introduction.

Notes. Stated in passing as 'It is open whether...' with no formal label. Arises from related work by Berger, Spirkl, and Seymour; one of the present paper's authors (Seymour) is involved in the related work.

Source paper

 Detecting a long odd hole
 Maria Chudnovsky, Alex Scott, Paul Seymour · 2020-09-06
 https://arxiv.org/abs/1904.12273
 PDF source

=== Source paper abstract / header ===
Abstract:For each integer $t\ge 5$, we give a polynomial-time algorithm to test whether a graph contains an induced cycle with length at least $t$ and odd.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1904.12273 [math.CO]
 

 
  
 (or 
 arXiv:1904.12273v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1904.12273
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Sun, 28 Apr 2019 07:58:02 UTC (21 KB)

 [v2]
 Sun, 6 Sep 2020 18:22:39 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Detecting a long odd hole, by Maria Chudnovsky and 2 other authors
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
 | 2019-04
 

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
