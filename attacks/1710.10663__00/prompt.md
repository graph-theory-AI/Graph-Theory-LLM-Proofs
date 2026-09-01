Attack the following open graph-theory problem.

Catalog id: 1710.10663__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1710.10663__00/
Source paper: List-decodable zero-rate codes (arXiv:1710.10663)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture on exact asymptotics of maxcode_L for even L
We believe that in fact $\mathrm{maxcode}_L(\varepsilon) = c_L \varepsilon^{-1} + O(1)$ for even $L$.

Context:
Theorem 2 establishes the two-sided bound $c_L \varepsilon^{-1} + O(1) \leq \mathrm{maxcode}_L(\varepsilon) = O(\varepsilon^{-1})$ for every even $L \geq 2$, where $c_L = 2^{-\lfloor L/2 \rfloor}\binom{L}{\lfloor L/2 \rfloor}$ comes from Theorem 1. The authors conjecture that the lower bound is tight up to an additive constant, i.e., that the exact leading coefficient is $c_L$.

=== Catalog page (statement + literature review) ===
Exact leading coefficient of maxcode_L even L — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The source paper (Theorem 2) already established the lower bound $\mathrm{maxcode}_L(\varepsilon) \geq c_L\varepsilon^{-1}+O(1)$ for even $L$; the conjecture asks whether the matching upper bound also has leading constant $c_L$. A 2023/2025 follow-up by Resch, Yuan, and Zhang (arXiv:2309.01800, ITCS 2025) proves tight $\Theta(1/\varepsilon)$ bounds for list-decodable and list-recoverable zero-rate codes over general alphabets with unspecified constants, extending the Alon--Bukh--Polyanskiy framework but not addressing the exact leading constant $c_L$ for the binary even-$L$ case. No paper in the indexed literature appears to resolve the exact-constant question.

 Cited literature (1)

 
 
 
partial Tight Bounds on List-Decodable and List-Recoverable Zero-Rate Codes
 (2025)
 

 
 Nicolas Resch, Chen Yuan, Yihan Zhang · ITCS 2025 (LIPIcs vol. 325, article 82) · arXiv:2309.01800 · doi:10.4230/LIPIcs.ITCS.2025.82

Proves matching upper and lower bounds of $\Theta_{q,\ell,L}(1/\varepsilon)$ for zero-rate list-decodable and list-recoverable codes over general alphabets, generalising Alon--Bukh--Polyanskiy to $q\geq 3$ and arbitrary list sizes, but the constants absorbed in $\Theta_{q,\ell,L}$ are not identified as $c_L$ for the binary even-$L$ case.
 

 

 Reviewer notes. The closest follow-up, Resch--Yuan--Zhang (arXiv:2309.01800), proves tight-order bounds for general alphabets but does not pin down the exact binary constant $c_L=2^{-\lfloor L/2\rfloor}\binom{L}{\lfloor L/2\rfloor}$ for even $L$. The specific conjecture on the exact leading coefficient appears to remain open in the published literature as of May 2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We believe that in fact $\mathrm{maxcode}_L(\varepsilon) = c_L \varepsilon^{-1} + O(1)$ for even $L$.

Context

Theorem 2 establishes the two-sided bound $c_L \varepsilon^{-1} + O(1) \leq \mathrm{maxcode}_L(\varepsilon) = O(\varepsilon^{-1})$ for every even $L \geq 2$, where $c_L = 2^{-\lfloor L/2 \rfloor}\binom{L}{\lfloor L/2 \rfloor}$ comes from Theorem 1. The authors conjecture that the lower bound is tight up to an additive constant, i.e., that the exact leading coefficient is $c_L$.

Notes. Stated as 'We believe that in fact …' in prose immediately after Theorem 2; no labelled theorem environment. PDF source — math notation may be garbled.

Source paper

 List-decodable zero-rate codes
 Noga Alon, Boris Bukh, Yury Polyanskiy · 2018-05-14
 https://arxiv.org/abs/1710.10663
 PDF source

=== Source paper abstract / header ===
Abstract:We consider list-decoding in the zero-rate regime for two cases: the binary alphabet and the spherical codes in Euclidean space. Specifically, we study the maximal $\tau \in [0,1]$ for which there exists an arrangement of $M$ balls of relative Hamming radius $\tau$ in the binary hypercube (of arbitrary dimension) with the property that no point of the latter is covered by $L$ or more of them. As $M\to \infty$ the maximal $\tau$ decreases to a well-known critical value $\tau_L$. In this work, we prove several results on the rate of this convergence.
For the binary case, we show that the rate is $\Theta(M^{-1})$ when $L$ is even, thus extending the classical results of Plotkin and Levenshtein for $L=2$. For $L=3$ the rate is shown to be $\Theta(M^{-\tfrac{2}{3}})$.
For the similar question about spherical codes, we prove the rate is $\Omega(M^{-1})$ and $O(M^{-\tfrac{2L}{L^2-L+2}})$.
 

 
 
 
 Comments:
 20 pages, improved exposition
 

 Subjects:
 
 Information Theory (cs.IT); Combinatorics (math.CO)
 
 
 MSC classes:
 68P30, 05D99, 52C35
 

 Cite as:
 arXiv:1710.10663 [cs.IT]
 

 
  
 (or 
 arXiv:1710.10663v2 [cs.IT] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1710.10663
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Boris Bukh [view email] 
 [v1]
 Sun, 29 Oct 2017 18:29:47 UTC (26 KB)

 [v2]
 Mon, 14 May 2018 16:18:43 UTC (27 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled List-decodable zero-rate codes, by Noga Alon and 2 other authors
View PDF
HTML (experimental)
TeX Source
 

 
 
 view license
 

 

 
 Current browse context:

 cs.IT

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2017-10
 

 Change to browse by:
 
 cs
 math
 math.CO
 math.IT
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Noga Alon
Boris Bukh
Yury Polyanskiy 

 

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
