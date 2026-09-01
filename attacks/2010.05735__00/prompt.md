Attack the following open graph-theory problem.

Catalog id: 2010.05735__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2010.05735__00/
Source paper: Powers of paths in tournaments (arXiv:2010.05735)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: exact constant in the exponent
It would be interesting to find the exact value of the constant factor in the exponent. Optimizing our proof can yield a lower bound of $n/2^{ck+o(k)}$ with $c \approx 3.9$, but is unlikely to give the correct bound.

Context:
Theorem 1 and Yuster's construction together show that the optimal guaranteed length of the $k$-th power of a directed path in any $n$-vertex tournament has the form $n/2^{\Theta(k)}$. The paper provides a lower bound $n/2^{4k+6k}$ and an upper bound $k(k+1)n/2^k$, leaving a gap in the constant in the exponent.

=== Catalog page (statement + literature review) ===
Exact exponent constant for tournament path powers — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The open problem asks for the exact constant $c$ in the exponent such that every $n$-vertex tournament contains the $k$-th power of a directed path of length $n/2^{ck}$; the source paper establishes the form is $n/2^{\Theta(k)}$ with lower bound constant optimisable to $c \approx 3.9$ and upper bound constant $c = 1$ (from Yuster's construction). A follow-up paper (arXiv:2105.12484, Gir\~ao and Kor\'{a}ndi, 2021) studies the related problem of partitioning tournaments into at most $2^{ck}$ $k$-th powers of paths (tight up to the exponential constant) but does not address the exact constant for containment. No subsequent work resolving the exact value of $c$ was found in a thorough web search.

 Cited literature (1)

 
 
 
partial Powers of paths and cycles in tournaments
 (2021)
 

 
 António Girão, Dániel Korándi · arXiv preprint · arXiv:2105.12484

Shows any tournament can be partitioned into at most $2^{ck}$ $k$-th powers of directed paths (tight up to the exponential constant), a related but distinct result that does not determine the exact constant for the containment problem.
 

 

 Reviewer notes. The specific open problem is to find the exact value of $c$ in $n/2^{ck}$, where the current gap is $c \in [1, \approx 3.9]$. The follow-up arXiv:2105.12484 is verified and relevant to the broader topic but addresses tournament decomposition, not containment. No paper resolving the exact constant was found after an exhaustive 5-call web search spanning 2021–2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It would be interesting to find the exact value of the constant factor in the exponent. Optimizing our proof can yield a lower bound of $n/2^{ck+o(k)}$ with $c \approx 3.9$, but is unlikely to give the correct bound.

Context

Theorem 1 and Yuster's construction together show that the optimal guaranteed length of the $k$-th power of a directed path in any $n$-vertex tournament has the form $n/2^{\Theta(k)}$. The paper provides a lower bound $n/2^{4k+6k}$ and an upper bound $k(k+1)n/2^k$, leaving a gap in the constant in the exponent.

Notes. Stated in prose without a labelled environment; verbatim phrasing 'It would be interesting to find the exact value of the constant factor in the exponent.'

Source paper

 Powers of paths in tournaments
 Nemanja Draganić, François Dross, Jacob Fox, António Girão, Frédéric Havet, Dániel Korándi, William Lochet, David Munhá Correia, Alex Scott, Benny Sudakov · 2021-02-16
 https://arxiv.org/abs/2010.05735
 PDF source

=== Source paper abstract / header ===
Abstract:In this short note we prove that every tournament contains the $k$-th power of a directed path of linear length. This improves upon recent results of Yuster and of Girão. We also give a complete solution for this problem when $k=2$, showing that there is always a square of a directed path of length $\lceil 2n/3 \rceil-1$, which is best possible.
 

 
 
 
 Comments:
 6 pages; updated affiliations; accepted at CPC
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2010.05735 [math.CO]
 

 
  
 (or 
 arXiv:2010.05735v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2010.05735
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Dániel Korándi [view email] 
 [v1]
 Mon, 12 Oct 2020 14:27:41 UTC (4 KB)

 [v2]
 Thu, 15 Oct 2020 16:37:57 UTC (5 KB)

 [v3]
 Tue, 10 Nov 2020 15:50:25 UTC (8 KB)

 [v4]
 Tue, 16 Feb 2021 18:08:02 UTC (8 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Powers of paths in tournaments, by Nemanja Dragani\'c and 9 other authors
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
 | 2020-10
 

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
