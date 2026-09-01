Attack the following open graph-theory problem.

Catalog id: 2201.00328__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2201.00328__00/
Source paper: Implicit representation of sparse hereditary families (arXiv:2201.00328)

=== Extracted statement (catalog JSON) ===
Title: Question (Section 3, implicit representation for speed $2^{O(n\log n)}$)
Is it possible that hereditary families with speed $f(n) \leq 2^{O(n \log n)}$ always admit an implicit representation of size $O(n^{1/2} \log n)$?

Context:
Hatami and Hatami [13] showed that for every $\delta > 0$ there are hereditary families with speed $f(n) \leq 2^{O(n \log n)}$ for which any implicit representation requires labels of size at least $\Omega(n^{1/2-\delta})$, and they raise the question of whether the exponent $1/2$ can be improved. Alon here asks the complementary upper-bound question: whether $O(n^{1/2} \log n)$ always suffices in this speed range.

=== Catalog page (statement + literature review) ===
√n log n implicit labels for hereditary families — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The question of whether every hereditary family with speed $f(n) \leq 2^{O(n\log n)}$ admits an implicit representation of size $O(n^{1/2}\log n)$ remains open as of May 2026. The matching lower bound $\Omega(n^{1/2-\delta})$ for every $\delta>0$ (Hatami–Hatami, 2022, cited in the source paper) shows that the exponent $1/2$ cannot be improved. Partial progress within the same speed regime was made in 2026 by Cardinal and Sharir, who proved $O(n^{1-2/(d+1)+\varepsilon})$-bit labels for $d$-dimensional semialgebraic families (which have speed $2^{\Theta(n\log n)}$), beating the $n^{1/2}$ threshold for $d=1$, but the question for all hereditary families of this speed remains unresolved.

 Cited literature (1)

 
 
 
partial Implicit representations via the polynomial method
 (2026)
 

 
 Jean Cardinal, Micha Sharir · arXiv preprint · arXiv:2602.10922

Proves O(n^{1-2/(d+1)+ε})-bit adjacency labeling schemes for d-dimensional semialgebraic hereditary families, which lie in the speed-2^{Θ(n log n)} regime; for d=1 this gives sub-n^{1/2} labels, providing partial evidence for the upper-bound question, but does not resolve it for all hereditary families of this speed.
 

 

 Reviewer notes. No direct resolution found. Hatami–Hatami (arXiv:2111.13198, 2022) established the lower bound Ω(n^{1/2−δ}) for every δ>0, which was already known at the time Alon posed the question. Cardinal and Sharir (arXiv:2602.10922, 2026) give better-than-n^{1/2} bounds for semialgebraic families specifically (a subfamily of speed-2^{O(n log n)} hereditary families) but the general upper-bound question is unresolved. A separate line of work by Bonnet–Duron–Sylvester–Zamaraev (arXiv:2409.04821, ITCS 2025) proves O(log³n) for structurally defined 'small classes', which may not coincide with the full speed-2^{O(n log n)} regime.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it possible that hereditary families with speed $f(n) \leq 2^{O(n \log n)}$ always admit an implicit representation of size $O(n^{1/2} \log n)$?

Context

Hatami and Hatami [13] showed that for every $\delta > 0$ there are hereditary families with speed $f(n) \leq 2^{O(n \log n)}$ for which any implicit representation requires labels of size at least $\Omega(n^{1/2-\delta})$, and they raise the question of whether the exponent $1/2$ can be improved. Alon here asks the complementary upper-bound question: whether $O(n^{1/2} \log n)$ always suffices in this speed range.

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
