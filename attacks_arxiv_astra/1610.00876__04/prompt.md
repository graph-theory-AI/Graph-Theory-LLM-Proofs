Attack the following open graph-theory problem.

Catalog id: 1610.00876__04
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1610.00876__04/
Source paper: Subdivisions in digraphs of large out-degree or large dichromatic number (arXiv:1610.00876)

=== Extracted statement (catalog JSON) ===
Title: Problem 12
What is $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n)$?

Context:
The paper proves in Section 3 that every digraph is $\vec{\chi}$-maderian. Since every digraph of order $n$ is a subdigraph of $\vec{K}_n$, bounding $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n)$ controls all cases. The paper establishes $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n) \leq 4^{n^2-2n+1}(n-1)+1$ (Corollary 36), but the exact value is unknown.

=== Catalog page (statement + literature review) ===
Exact value of mader_χ̄(K̄ₙ) — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 Subdivision of a transitive tournament in digraphs with large outdegree.
 (fuzzy-match score 74).

 
 Status
 open
 high confidence
 

 Problem 12 asks for the exact value of $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n)$; the source paper only establishes the doubly-exponential upper bound $4^{n^2-2n+1}(n-1)+1$. The most relevant follow-up, Gishboliner–Steiner–Szabó (2020, arXiv:2008.09888), proves $\mathrm{mader}_{\vec{\chi}}(F)=v(F)$ for octus digraphs and orientations of cactus graphs, but the complete digraph $\vec{K}_n$ falls outside these classes and the exact value remains unknown. No paper resolving Problem 12 was found in the indexed literature.

 Cited literature (2)

 
 
 
partial Dichromatic number and forced subdivisions
 (2020)
 

 
 Lior Gishboliner, Raphael Steiner, Tibor Szabó · Journal of Combinatorial Theory, Series B · arXiv:2008.09888 · doi:10.1016/j.jctb.2021.06.003

Proves $\mathrm{mader}_{\vec{\chi}}(F)=v(F)$ for every octus digraph $F$ and for every orientation of a cactus graph; $\vec{K}_n$ is not in these classes, so the exact value of $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n)$ is not settled.
 

 
 
partial Oriented cycles in digraphs of large outdegree
 (2020)
 

 
 Lior Gishboliner, Raphael Steiner, Tibor Szabó · arXiv preprint · arXiv:2008.13224

Proves that every digraph with minimum out-degree at least $K(\ell)$ contains a subdivision of every orientation of a cycle of length $\ell$; addresses $\mathrm{mader}_{\delta^+}$ for oriented cycles rather than $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n)$.
 

 

 Reviewer notes. The search also surfaced arXiv:2101.04590 (Mészáros–Steiner, 2021, 'Complete minors in digraphs with given dichromatic number'), which improves bounds on forced complete *minors* under dichromatic number; minors are weaker than subdivisions and this paper does not resolve Problem 12. No paper giving the exact value of mader_chi(K_n) was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n)$?

Context

The paper proves in Section 3 that every digraph is $\vec{\chi}$-maderian. Since every digraph of order $n$ is a subdigraph of $\vec{K}_n$, bounding $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n)$ controls all cases. The paper establishes $\mathrm{mader}_{\vec{\chi}}(\vec{K}_n) \leq 4^{n^2-2n+1}(n-1)+1$ (Corollary 36), but the exact value is unknown.

Notes. PDF source — dichromatic number denoted $\vec{\chi}$; upper bound exponent reconstructed from context as $n^2-2n+1 = n(n-1)-n+1$ for $\vec{K}_n$ with $n(n-1)$ arcs and 1 component.

Source paper

 Subdivisions in digraphs of large out-degree or large dichromatic number
 Pierre Aboulker, Nathann Cohen, Fréderic Havet, William Lochet, Phablo F. S. Moura, Stéphan Thomassé · 2016-10-04
 https://arxiv.org/abs/1610.00876
 PDF source

=== Source paper abstract / header ===
Abstract:In 1985, Mader conjectured the existence of a function $f$ such that every digraph with minimum out-degree at least $f(k)$ contains a subdivision of the transitive tournament of order $k$. This conjecture is still completely open, as the existence of $f(5)$ remains unknown. In this paper, we show that if $D$ is an oriented path, or an in-arborescence (i.e., a tree with all edges oriented towards the root) or the union of two directed paths from $x$ to $y$ and a directed path from $y$ to $x$, then every digraph with minimum out-degree large enough contains a subdivision of $D$. Additionally, we study Mader's conjecture considering another graph parameter. The dichromatic number of a digraph $D$ is the smallest integer $k$ such that $D$ can be partitioned into $k$ acyclic subdigraphs. We show that any digraph with dichromatic number greater than $4^m (n-1)$ contains every digraph with $n$ vertices and $m$ arcs as a subdivision.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1610.00876 [math.CO]
 

 
  
 (or 
 arXiv:1610.00876v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1610.00876
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: William Lochet [view email] 
 [v1]
 Tue, 4 Oct 2016 07:25:24 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Subdivisions in digraphs of large out-degree or large dichromatic number, by Pierre Aboulker and 4 other authors
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
 | 2016-10
 

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
