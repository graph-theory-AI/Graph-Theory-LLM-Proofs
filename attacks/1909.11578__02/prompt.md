Attack the following open graph-theory problem.

Catalog id: 1909.11578__02
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1909.11578__02/
Source paper: On symmetric intersecting families of vectors (arXiv:1909.11578)

=== Extracted statement (catalog JSON) ===
Title: Polynomial improvement on symmetric intersecting family size bound
Show that there exist constants $c, \delta > 0$ (possibly depending on $k$) such that for any symmetric intersecting $A \subset [k]^n$, we have $\log_k |A| \leq n - cn^{\delta}$.

Context:
This is posed in Section 4 as a concrete and more modest goal, falling short of identifying the exact extremal size: even a polynomial gain over the $o(k^n)$ bound of Theorem 1.1, expressed as $\log_k |A| \leq n - cn^\delta$, would be a significant advance.

=== Catalog page (statement + literature review) ===
Polynomial gain on symmetric intersecting vector families — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The conjecture asks for constants $c, \delta > 0$ (possibly depending on $k$) such that every symmetric intersecting $A \subset [k]^n$ satisfies $\log_k |A| \leq n - cn^{\delta}$, a polynomial improvement over the qualitative $o(k^n)$ bound of Theorem 1.1 for fixed $k \geq 3$. Keller, Lifshitz, and Marcus (arXiv:2307.01356, 2023) prove the first quantitative upper bound in the transitive-symmetric vector-intersecting setting via sharp hypercontractivity, but their result applies only for $k$ growing with $n$ (specifically $2\log n \leq k \leq \sqrt{n}\log n$), leaving the fixed-$k$ case open. No paper resolving the polynomial improvement for fixed $k$ was found in the indexed literature.

 Cited literature (1)

 
 
 
partial Sharp Hypercontractivity for Global Functions
 (2023)
 

 
 Keller, Lifshitz, Marcus · arXiv preprint · arXiv:2307.01356

Proves the first quantitative upper bound on transitive-symmetric vector-intersecting families (Theorem 1.6): for $k \in [2\log n, \sqrt{n}\log n]$, any such family satisfies $|\mathcal{A}|/k^n \leq c_1 \exp(-c_2 k/\log n)$; this is a polynomial improvement in $n$ for $k$ polynomial in $n$, but does not address the fixed-$k$ regime targeted by the conjecture.
 

 

 Reviewer notes. The conjecture targets fixed $k \geq 3$ with $n \to \infty$; arXiv:2307.01356 makes partial progress for $k$ growing with $n$ via sharp hypercontractivity (Theorem 1.6), but this regime does not overlap with fixed $k$. The qualitative $o(k^n)$ bound from the source paper may also follow from earlier work of Dinur, Friedgut, and Regev (as noted in the paper's revised version). Author names for 2307.01356 are from PDF metadata extraction and may need independent verification.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Show that there exist constants $c, \delta > 0$ (possibly depending on $k$) such that for any symmetric intersecting $A \subset [k]^n$, we have $\log_k |A| \leq n - cn^{\delta}$.

Context

This is posed in Section 4 as a concrete and more modest goal, falling short of identifying the exact extremal size: even a polynomial gain over the $o(k^n)$ bound of Theorem 1.1, expressed as $\log_k |A| \leq n - cn^\delta$, would be a significant advance.

Notes. PDF source — math notation may be garbled. No labeled environment; introduced with 'it would be very interesting to at least show' in Section 4.

Source paper

 On symmetric intersecting families of vectors
 Sean Eberhard, Jeff Kahn, Bhargav Narayanan, Sophie Spirkl · 2020-07-31
 https://arxiv.org/abs/1909.11578
 PDF source

=== Source paper abstract / header ===
Abstract:A family of vectors $A \subset [k]^n$ is said to be intersecting if any two elements of $A$ agree on at least one coordinate. We prove, for fixed $k \ge 3$, that the size of a symmetric intersecting subfamily of $[k]^n$ is $o(k^n)$, which is in stark contrast to the case of the Boolean hypercube (where $k =2$). Our main contribution addresses limitations of existing technology: while there is now some spectral machinery, developed by Ellis and the third author, to tackle extremal problems in set theory involving symmetry, this machinery relies crucially on the interplay between up-sets and biased product measures on the Boolean hypercube, features that are notably absent in the problem at hand; here, we describe a method for circumventing these barriers.
 

 
 
 
 Comments:
 6 pages; It has been brought to our attention that our main result (with slightly worse estimates) may be deduced from earlier work of Dinur, Friedgut and Regev, and this revision acknowledges this fact
 

 Subjects:
 
 Combinatorics (math.CO); Classical Analysis and ODEs (math.CA)
 
 
 MSC classes:
 05D05 (Primary), 05E18 (Secondary)
 

 Cite as:
 arXiv:1909.11578 [math.CO]
 

 
  
 (or 
 arXiv:1909.11578v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1909.11578
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 
 Related DOI:
 
 https://doi.org/10.1017/S0963548321000079

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Bhargav Narayanan [view email] 
 [v1]
 Wed, 25 Sep 2019 16:08:44 UTC (9 KB)

 [v2]
 Mon, 28 Oct 2019 14:41:40 UTC (9 KB)

 [v3]
 Tue, 4 Feb 2020 17:44:08 UTC (9 KB)

 [v4]
 Fri, 31 Jul 2020 15:00:17 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On symmetric intersecting families of vectors, by Sean Eberhard and 2 other authors
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
 | 2019-09
 

 Change to browse by:
 
 math
 math.CA
 

 

 

 
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
