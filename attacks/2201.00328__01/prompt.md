Attack the following open graph-theory problem.

Catalog id: 2201.00328__01
Catalog status: open (triage tier 2, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2201.00328__01/
Source paper: Implicit representation of sparse hereditary families (arXiv:2201.00328)

=== Catalog page (statement + literature review) ===
Implicit representation for sub-polynomial speed hereditary families — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No follow-up work resolving this question was found. The source paper (published in Discrete & Computational Geometry, 2024) establishes only the weaker bound O(n^{1-1/d} log n) under the hypothesis f(n) \leq 2^{(1/4-\varepsilon)n^2}; the specific question of whether the intermediate speed regime f(n) < 2^{n^{1+\varepsilon}} forces a label size of O(n^{2/3} log n) appears unresolved in the indexed literature as of May 2026. A 2025 paper on implicit representations via the polynomial method (arXiv:2602.10922) addresses semialgebraic families but does not treat this speed regime or the n^{2/3} exponent.

 Reviewer notes. No follow-up found that addresses this specific question. The paper arXiv:2602.10922 ('Implicit representations via the polynomial method', 2025) is thematically related but focuses on semialgebraic graphs and cites only Alon's main theorem (O(n^{1-1/d} log n)), not this open question. The source paper was published as Discrete Comput. Geom. (2024); the question about the n^{2/3} exponent for the intermediate speed range f(n) < 2^{n^{1+\varepsilon}} remains open with high confidence.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. If the speed of a hereditary family satisfies $f(n) < 2^{n^{1+\varepsilon}}$ for a sufficiently small fixed $\varepsilon > 0$, is there always an implicit representation of size at most $O(n^{2/3} \log n)$?

Context

This is posed as a follow-up to the $O(n^{1/2}\log n)$ question for the slower-speed regime. Theorem 1.1 guarantees only $O(n^{1-1/d}\log n)$ under the weaker bound $f(n) \leq 2^{(1/4-\varepsilon)n^2}$, and the question asks whether the intermediate speed range $f(n) < 2^{n^{1+\varepsilon}}$ forces a sub-polynomial improvement to $n^{2/3}$.

Notes. Posed as an explicit question in Section 3 but without a labelled theorem environment; PDF source.

Source paper

 Implicit representation of sparse hereditary families
 Noga Alon · 2022-01-02
 https://arxiv.org/abs/2201.00328
 PDF source

=== Source paper abstract / header ===
Abstract:For a hereditary family of graphs $\FF$, let $\FF_n$ denote the set of all members of $\FF$ on $n$ vertices. The speed of $\FF$ is the function $f(n)=|\FF_n|$. An implicit representation of size $\ell(n)$ for $\FF_n$ is a function assigning a label of $\ell(n)$ bits to each vertex of any given graph $G \in \FF_n$, so that the adjacency between any pair of vertices can be determined by their labels. Bonamy, Esperet, Groenland and Scott proved that the minimum possible size of an implicit representation of $\FF_n$ for any hereditary family $\FF$ with speed $2^{\Omega(n^2)}$ is $(1+o(1)) \log_2 |\FF_n|/n~(=\Theta(n))$. A recent result of Hatami and Hatami shows that the situation is very different for very sparse hereditary families. They showed that for every $\delta>0$ there are hereditary families of graphs with speed $2^{O(n \log n)}$ that do not admit implicit representations of size smaller than $n^{1/2-\delta}$. In this note we show that even a mild speed bound ensures an implicit representation of size $O(n^c)$ for some $c<1$. Specifically we prove that for every $\eps>0$ there is an integer $d \geq 1$ so that if $\FF$ is a hereditary family with speed $f(n) \leq 2^{(1/4-\eps)n^2}$ then $\FF_n$ admits an implicit representation of size $O(n^{1-1/d} \log n)$. Moreover, for every integer $d>1$ there is a hereditary family for which this is tight up to the logarithmic factor.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C78, 68R10
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:2201.00328 [math.CO]
 

 
  
 (or 
 arXiv:2201.00328v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2201.00328
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Noga Alon [view email] 
 [v1]
 Sun, 2 Jan 2022 09:57:25 UTC (7 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Implicit representation of sparse hereditary families, by Noga Alon
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
 | 2022-01
 

 Change to browse by:
 
 cs
 cs.DM
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
