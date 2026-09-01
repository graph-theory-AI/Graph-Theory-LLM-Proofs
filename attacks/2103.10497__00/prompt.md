Attack the following open graph-theory problem.

Catalog id: 2103.10497__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2103.10497__00/
Source paper: Sunflowers in set systems of bounded dimension (arXiv:2103.10497)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.1
For $d \geq 1$ and $r \geq 3$, there is a constant $C = C(d, r)$ such that $f^d_r(k) \leq C^k$.

Context:
The authors note that the Erdős-Rado sunflower conjecture implies this weaker statement about families of bounded VC-dimension $d$, where $f^d_r(k)$ is the minimum family size guaranteeing an $r$-sunflower among $k$-sets with VC-dimension at most $d$. The paper proves the conjecture for $d = 1$ (Theorem 1.2) and establishes the slightly weaker bound $f^d_r(k) \leq 2^{10k(dr)^2 \log^* k}$ for $d \geq 2$ (Theorem 1.3), leaving the full conjecture open for $d \geq 2$.

=== Catalog page (statement + literature review) ===
Exponential sunflower bound for bounded VC-dimension — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture that $f^d_r(k) \leq C^k$ for all $d \geq 1$ and $r \geq 3$ is proven for $d=1$ by the original paper (Theorem 1.2). For $d \geq 2$, Balogh, Bernshteyn, Delcourt, Ferber, and Pham (arXiv:2408.04165, 2024) substantially improved the bound from $2^{10k(dr)^2 \log^* k}$ to $(Cr(\log d + \log^* k))^k$, but the pure exponential $C^k$ with $C = C(d,r)$ independent of $k$ remains open for $d \geq 2$. The $d=1$ case is also resolved sharply in 2408.04165 with the tight bound $(r-1)^k$.

 Cited literature (1)

 
 
 
partial Sunflowers in Set Systems with Small VC-Dimension
 (2024)
 

 
 József Balogh, Anton Bernshteyn, Michelle Delcourt, Asaf Ferber, Huy Tuan Pham · Combinatorica · arXiv:2408.04165 · doi:10.1007/s00493-025-00186-8

Proves that any family of $\ell$-element sets with VC-dimension at most $d$ and size exceeding $(Cr(\log d + \log^* \ell))^\ell$ contains an $r$-sunflower, improving Fox–Pach–Suk's bound; also obtains the sharp bound $(r-1)^k$ for $d=1$, but the conjecture for $d \geq 2$ (pure exponential $C^k$) remains open.
 

 

 Reviewer notes. The paper arXiv:2408.04165 (published in Combinatorica 2025) is the main follow-up; it removes the double-exponential dependence on $\log^* k$ from the exponent but the base still contains a $\log^* k$ factor, so the conjecture for $d \geq 2$ is not yet resolved. No other post-2021 paper resolving the full conjecture was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For $d \geq 1$ and $r \geq 3$, there is a constant $C = C(d, r)$ such that $f^d_r(k) \leq C^k$.

Context

The authors note that the Erdős-Rado sunflower conjecture implies this weaker statement about families of bounded VC-dimension $d$, where $f^d_r(k)$ is the minimum family size guaranteeing an $r$-sunflower among $k$-sets with VC-dimension at most $d$. The paper proves the conjecture for $d = 1$ (Theorem 1.2) and establishes the slightly weaker bound $f^d_r(k) \leq 2^{10k(dr)^2 \log^* k}$ for $d \geq 2$ (Theorem 1.3), leaving the full conjecture open for $d \geq 2$.

Notes. PDF source. Conjecture is explicitly labelled in the paper. The case $d=1$ is resolved by Theorem 1.2; the case $d \geq 2$ remains open.

Source paper

 Sunflowers in set systems of bounded dimension
 Jacob Fox, Janos Pach, Andrew Suk · 2021-03-25
 https://arxiv.org/abs/2103.10497
 PDF source

=== Source paper abstract / header ===
Abstract:Given a family $\mathcal F$ of $k$-element sets, $S_1,\ldots,S_r\in\mathcal F$ form an {\em $r$-sunflower} if $S_i \cap S_j =S_{i'} \cap S_{j'}$ for all $i \neq j$ and $i' \neq j'$. According to a famous conjecture of Erd\H os and Rado (1960), there is a constant $c=c(r)$ such that if $|\mathcal F|\ge c^k$, then $\mathcal F$ contains an $r$-sunflower.
We come close to proving this conjecture for families of bounded {\em Vapnik-Chervonenkis dimension}, VC-dim$(\mathcal F)\le d$. In this case, we show that $r$-sunflowers exist under the slightly stronger assumption $|\mathcal F|\ge2^{10k(dr)^{2\log^{*} k}}$. Here, $\log^*$ denotes the iterated logarithm function.
We also verify the Erd\H os-Rado conjecture for families $\mathcal F$ of bounded {\em Littlestone dimension} and for some geometrically defined set systems.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2103.10497 [math.CO]
 

 
  
 (or 
 arXiv:2103.10497v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2103.10497
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Andrew Suk [view email] 
 [v1]
 Thu, 18 Mar 2021 19:52:28 UTC (14 KB)

 [v2]
 Thu, 25 Mar 2021 23:27:39 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Sunflowers in set systems of bounded dimension, by Jacob Fox and 2 other authors
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
 | 2021-03
 

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
