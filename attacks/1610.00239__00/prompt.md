Attack the following open graph-theory problem.

Catalog id: 1610.00239__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1610.00239__00/
Source paper: Optimal compression of approximate inner products and dimension reducti… (arXiv:1610.00239)

=== Catalog page (statement + literature review) ===
Bounded-norm bipartite Johnson-Lindenstrauss reduction — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 2.4 from arXiv:1610.00239 asserts that the bipartite Johnson-Lindenstrauss reduction to dimension $t = \lfloor C\log(2+\varepsilon^2 n)/\varepsilon^2 \rfloor$ can be achieved with the additional guarantee that all output vectors have Euclidean norm at most $O(1)$. No resolution or significant partial progress has been found in the literature as of May 2026. The conjecture has been open since 2017; if proved it would close the gap in the space complexity bounds of Theorem 2.2 for $\varepsilon \geq 2/\sqrt{n}$.

 Reviewer notes. No follow-up paper addressing Conjecture 2.4 was found across three targeted searches. The conjecture is roughly 9 years old; the medium confidence reflects that this age makes pure absence of indexed results somewhat less conclusive than for a very recent paper.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Under the assumptions of Theorem 1.2, the conclusion holds together with the further requirement that $\|x_i\| \leq O(1)$ and $\|y_i\| \leq O(1)$ for all $1 \leq i \leq n$.

Context

Theorem 1.2 establishes a bipartite Johnson-Lindenstrauss reduction to dimension $t = \lfloor C\log(2+\varepsilon^2 n)/\varepsilon^2 \rfloor$ that approximates inner products up to additive error $\varepsilon$, but does not control the norms of the output vectors. The authors conjecture that the output vectors can simultaneously be taken to have bounded Euclidean norm $O(1)$. If true, this would close the gap between the upper and lower bounds in the first bullet of Theorem 2.2 for all $\varepsilon \geq 2/\sqrt{n}$.

Notes. PDF source — norm notation $\|\cdot\|$ appears as bare vertical bars in the raw extract; reconstructed from context. The paper proves two partial results supporting the conjecture: the case $t = \Omega(n)$ (i.e., $\varepsilon = \Theta(1/\sqrt{n})$) is established as Theorem 2.5, and a matching bit-count estimate is proved for the column-query variant.

Source paper

 Optimal compression of approximate inner products and dimension reduction
 Noga Alon, Bo'az Klartag · 2017-04-02
 https://arxiv.org/abs/1610.00239
 PDF source

=== Source paper abstract / header ===
Abstract:Let $X$ be a set of $n$ points of norm at most $1$ in the Euclidean space $R^k$, and suppose $\varepsilon>0$. An $\varepsilon$-distance sketch for $X$ is a data structure that, given any two points of $X$ enables one to recover the square of the (Euclidean) distance between them up to an {\em additive} error of $\varepsilon$. Let $f(n,k,\varepsilon)$ denote the minimum possible number of bits of such a sketch. Here we determine $f(n,k,\varepsilon)$ up to a constant factor for all $n \geq k \geq 1$ and all $\varepsilon \geq \frac{1}{n^{0.49}}$. Our proof is algorithmic, and provides an efficient algorithm for computing a sketch of size $O(f(n,k,\varepsilon)/n)$ for each point, so that the square of the distance between any two points can be computed from their sketches up to an additive error of $\varepsilon$ in time linear in the length of the sketches. We also discuss the case of smaller $\varepsilon>2/\sqrt n$ and obtain some new results about dimension reduction in this range. In particular, we show that for any such $\varepsilon$ and any $k \leq t=\frac{\log (2+\varepsilon^2 n)}{\varepsilon^2}$ there are configurations of $n$ points in $R^k$ that cannot be embedded in $R^{\ell}$ for $\ell < ck$ with $c$ a small absolute positive constant, without distorting some inner products (and distances) by more than $\varepsilon$. On the positive side, we provide a randomized polynomial time algorithm for a bipartite variant of the Johnson-Lindenstrauss lemma in which scalar products are approximated up to an additive error of at most $\varepsilon$. This variant allows a reduction of the dimension down to $O(\frac{\log (2+\varepsilon^2 n)}{\varepsilon^2})$, where $n$ is the number of points.
 

 
 
 
 Comments:
 29 pages
 

 Subjects:
 
 Metric Geometry (math.MG); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1610.00239 [math.MG]
 

 
  
 (or 
 arXiv:1610.00239v4 [math.MG] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1610.00239
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Bo'az Klartag [view email] 
 [v1]
 Sun, 2 Oct 2016 08:24:06 UTC (10 KB)

 [v2]
 Thu, 15 Dec 2016 09:35:32 UTC (10 KB)

 [v3]
 Thu, 16 Mar 2017 06:26:20 UTC (19 KB)

 [v4]
 Sun, 2 Apr 2017 11:44:42 UTC (25 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Optimal compression of approximate inner products and dimension reduction, by Noga Alon and Bo'az Klartag
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 math.MG

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2016-10
 

 Change to browse by:
 
 math
 math.CO
 

 

 

 
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
