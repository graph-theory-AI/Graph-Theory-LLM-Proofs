Attack the following open graph-theory problem.

Catalog id: 1803.03588__00
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1803.03588__00/
Source paper: Towards Erdos-Hajnal for graphs with no 5-hole (arXiv:1803.03588)

=== Extracted statement (catalog JSON) ===
Title: Polynomial dependence of $\delta$ on $d$ in Rödl's theorem
A polynomial dependence of $\delta$ on $d$ holds in Theorem 2.2, i.e., the $\delta$ satisfying Rödl's theorem can be taken to be polynomial in $d$; and this would imply the Erdős-Hajnal conjecture itself.

Context:
In the discussion following Rödl's theorem (2.2), the authors note that Rödl's original proof gives a tower-type bound for $1/\delta$ in terms of $1/d$, while Fox and Sudakov [7] improve this to $\delta = 2^{-|V(H)|^{15}(\log(1/d))^2}$. A polynomial dependence is stated as a community conjecture whose truth would imply the full Erdős-Hajnal conjecture.

=== Catalog page (statement + literature review) ===
Polynomial δ Dependence in Rödl's Theorem — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 The Erdös-Hajnal Conjecture
 (fuzzy-match score 75).

 
 Status
 partial
 high confidence
 

 The polynomial bound on $\delta$ in Rödl's theorem remains unproved for general $H$; the best known bound is the loglog improvement $\delta = 2^{-c(\log(1/d))^2/\log\log(1/d)}$ of Bucić–Nguyen–Scott–Seymour (2023), confirming the gap between the exponential status quo and the conjectured polynomial dependence. Notably, Bucić–Fox–Pham (2024) proved that the polynomial Rödl conjecture is in fact *equivalent* to the full Erdős–Hajnal conjecture (strengthening the mere implication stated in the source paper), and also verified the polynomial Rödl property for the special class of string graphs.

 Cited literature (2)

 
 
 
partial Induced subgraph density. I. A loglog step towards Erdos-Hajnal
 (2023)
 

 
 Matija Bucić, Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2301.10147

Improves the exponent in Rödl's bound to $\delta = 2^{-c(\log(1/d))^2/\log\log(1/d)}$, a loglog gain over Fox–Sudakov, but does not achieve the conjectured polynomial dependence.
 

 
 
partial Equivalence between Erdős-Hajnal and polynomial Rödl and Nikiforov conjectures
 (2024)
 

 
 Matija Bucić, Jacob Fox, Huy Tuan Pham · arXiv preprint · arXiv:2403.08303

Proves that the polynomial Rödl conjecture (and the polynomial Nikiforov conjecture) are each equivalent to the Erdős–Hajnal conjecture, upgrading the one-directional implication stated in the source paper to a full equivalence; also verifies the polynomial Rödl property for string graphs as a special case.
 

 

 Reviewer notes. The conjecture as stated in the source paper has two components: (1) that polynomial δ holds in Rödl's theorem, and (2) that this implies Erdős–Hajnal. Component (2) was already known in 2018; arXiv:2403.08303 (2024) strengthens it to a full equivalence. Component (1) — the polynomial bound itself — remains open for general H, with the loglog bound of arXiv:2301.10147 being the current state of the art.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. A polynomial dependence of $\delta$ on $d$ holds in Theorem 2.2, i.e., the $\delta$ satisfying Rödl's theorem can be taken to be polynomial in $d$; and this would imply the Erdős-Hajnal conjecture itself.

Context

In the discussion following Rödl's theorem (2.2), the authors note that Rödl's original proof gives a tower-type bound for $1/\delta$ in terms of $1/d$, while Fox and Sudakov [7] improve this to $\delta = 2^{-|V(H)|^{15}(\log(1/d))^2}$. A polynomial dependence is stated as a community conjecture whose truth would imply the full Erdős-Hajnal conjecture.

Notes. Stated in passive voice ('It is conjectured that…') without a specific citation; appears to be a community/folklore conjecture presented without explicit attribution. For $H = C_5$ the authors note one can achieve the intermediate bound $\delta = 2^{-O((\log(1/d))^2 / \log\log(1/d))}$.

Source paper

 Towards Erdos-Hajnal for graphs with no 5-hole
 Maria Chudnovsky, Jacob Fox, Alex Scott, Paul Seymour, Sophie Spirkl · 2018-03-09
 https://arxiv.org/abs/1803.03588
 PDF source

=== Source paper abstract / header ===
Abstract:The Erdos-Hajnal conjecture says that for every graph $H$ there exists $c>0$ such that $\max(\alpha(G),\omega(G))\ge n^c$ for every $H$-free graph $G$ with $n$ vertices, and this is still open when $H=C_5$. Until now the best bound known on $\max(\alpha(G),\omega(G))$ for $C_5$-free graphs was the general bound of Erdos and Hajnal, that for all $H$, $\max(\alpha(G),\omega(G))\ge 2^{\Omega(\sqrt{\log n })}$ if $G$ is $H$-free. We improve this when $H=C_5$ to $\max(\alpha(G),\omega(G))\ge 2^{\Omega(\sqrt{\log n \log \log n})}.$
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1803.03588 [math.CO]
 

 
  
 (or 
 arXiv:1803.03588v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1803.03588
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Fri, 9 Mar 2018 16:29:58 UTC (8 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Towards Erdos-Hajnal for graphs with no 5-hole, by Maria Chudnovsky and 3 other authors
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
 | 2018-03
 

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
