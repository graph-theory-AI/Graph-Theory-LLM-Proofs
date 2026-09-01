Attack the following open graph-theory problem.

Catalog id: 2206.11371__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2206.11371__00/
Source paper: Set-coloring Ramsey numbers via codes (arXiv:2206.11371)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture on R(n;r,s) vs R'(n;r,s) near Turán density
We clearly have $R(n; r, s) \geq R'(n; r, s)$ and we believe that this estimate should be close to an equality when $s/r$ is close to the Turán density $1 - \frac{1}{n-1}$.

Context:
The authors introduce the variant $R'(n;r,s)$, defined as the minimum $N$ such that every $(r,s)$-coloring of $K_N$ yields a color class with chromatic number at least $n$. They observe that $R(n;r,s) \geq R'(n;r,s)$ always holds, and that for the special case $s = r-1$ near-equality is confirmed by prior work of Alon et al. [1]. The informal belief is stated in Section 4 while studying the fixed-$n$ regime.

=== Catalog page (statement + literature review) ===
R(n;r,s) vs R'(n;r,s) near Turán density equality — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The informal conjecture that R(n;r,s) ≈ R'(n;r,s) when s/r is near the Turán density 1−1/(n−1) has not been explicitly resolved, but the same group of authors published a follow-up (arXiv:2305.14132) that studies R(n;r,s) precisely in the intermediate range where s/r is close to 1−1/(n−1) by connecting it to the maximum size of error-correcting codes near the zero-rate threshold — the same coding-theoretic quantity that defines R'. This provides partial progress towards the belief, but a precise comparison R(n;r,s) ≈ R'(n;r,s) has not been confirmed in the verified literature.

 Cited literature (1)

 
 
 
partial Set-coloring Ramsey numbers and error-correcting codes near the zero-rate threshold
 (2023)
 

 
 David Conlon, Jacob Fox, Xiaoyu He, Dhruv Mubayi, Andrew Suk, Jacques Verstraete · arXiv preprint · arXiv:2305.14132

Proves bounds on R(n;r,s) when s/r is close to the Turán density 1−1/(n−1) by establishing a connection to the maximum size of error-correcting codes near the zero-rate threshold, directly relevant to the regime where R and R' are conjectured to be close.
 

 

 Reviewer notes. R'(n;r,s) is defined in the source paper as the minimum N such that every (r,s)-coloring of K_N yields a color class with chromatic number at least n; it equals A_{n-1}(r,s)+1 where A_{n-1}(r,s) is the maximum size of an (n−1)-ary error-correcting code of length r and distance r−s. The follow-up arXiv:2305.14132 connects R(n;r,s) to this same coding quantity in the Turán-density regime, constituting indirect partial evidence for the conjecture, but does not explicitly prove R≈R'. No paper was found that directly states and resolves this informal conjecture.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We clearly have $R(n; r, s) \geq R'(n; r, s)$ and we believe that this estimate should be close to an equality when $s/r$ is close to the Turán density $1 - \frac{1}{n-1}$.

Context

The authors introduce the variant $R'(n;r,s)$, defined as the minimum $N$ such that every $(r,s)$-coloring of $K_N$ yields a color class with chromatic number at least $n$. They observe that $R(n;r,s) \geq R'(n;r,s)$ always holds, and that for the special case $s = r-1$ near-equality is confirmed by prior work of Alon et al. [1]. The informal belief is stated in Section 4 while studying the fixed-$n$ regime.

Notes. PDF source — math may be garbled. Statement reconstructed from prose; no labelled conjecture environment. The problems/further-remarks section mentioned at the end of the introduction is not present in the extracted text, so additional posed problems from that section may be missing.

Source paper

 Set-coloring Ramsey numbers via codes
 David Conlon, Jacob Fox, Xiaoyu He, Dhruv Mubayi, Andrew Suk, Jacques Verstraete · 2022-06-22
 https://arxiv.org/abs/2206.11371
 PDF source

=== Source paper abstract / header ===
Abstract:For positive integers $n,r,s$ with $r > s$, the set-coloring Ramsey number $R(n;r,s)$ is the minimum $N$ such that if every edge of the complete graph $K_N$ receives a set of $s$ colors from a palette of $r$ colors, then there is guaranteed to be a monochromatic clique on $n$ vertices, that is, a subset of $n$ vertices where all of the edges between them receive a common color. In particular, the case $s=1$ corresponds to the classical multicolor Ramsey number. We prove general upper and lower bounds on $R(n;r,s)$ which imply that $R(n;r,s) = 2^{\Theta(nr)}$ if $s/r$ is bounded away from $0$ and $1$. The upper bound extends an old result of Erdős and Szemerédi, who treated the case $s = r-1$, while the lower bound exploits a connection to error-correcting codes. We also study the analogous problem for hypergraphs.
 

 
 
 
 Comments:
 11 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2206.11371 [math.CO]
 

 
  
 (or 
 arXiv:2206.11371v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2206.11371
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Xiaoyu He [view email] 
 [v1]
 Wed, 22 Jun 2022 20:37:50 UTC (15 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Set-coloring Ramsey numbers via codes, by David Conlon and 5 other authors
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
 | 2022-06
 

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
