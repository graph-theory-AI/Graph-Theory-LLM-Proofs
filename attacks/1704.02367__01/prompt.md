Attack the following open graph-theory problem.

Catalog id: 1704.02367__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1704.02367__01/
Source paper: Testing hereditary properties of ordered graphs and matrices (arXiv:1704.02367)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: Better parameter dependence for ordered binary matrix removal
It will be interesting to combine the ideas from the current proof with the binary matrix regularity lemma of Alon, Fischer and Newman to obtain a removal lemma for finite families of ordered binary matrices with better dependence between the parameters $\delta^{-1}$ and $\varepsilon^{-1}$; ideally polynomial dependence, but even exponential dependence would be interesting.

Context:
For ordered binary matrices, Alon, Fischer and Newman obtained an efficient conditional regularity lemma in which $\delta^{-1}$ is polynomial in $\varepsilon^{-1}$. The general ordered removal lemma proved in this paper inherits a wowzer-type dependence from the strong regularity lemma, and improving this for finite families of ordered binary matrices is posed as an open problem.

=== Catalog page (statement + literature review) ===
Polynomial dependence in ordered binary matrix removal — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The open problem asks to improve the wowzer-type parameter dependence in the ordered binary matrix removal lemma (for finite families) to polynomial or at least exponential dependence between \delta^{-1} and \varepsilon^{-1}. Follow-up work has made partial progress: arXiv:2110.03577 characterises exactly when polynomial removal lemmas exist for ordered graphs (only for 2-vertex graphs or one specific 3-vertex configuration, up to symmetry), explicitly building on the Alon--Ben-Eliezer--Fischer framework and suggesting polynomial bounds for general families are rare; arXiv:2307.01652 proves a polynomial removal lemma for ordered matchings, a special subclass of ordered binary matrix patterns. The conjecture for arbitrary finite families of ordered binary matrices appears unresolved.

 Cited literature (2)

 
 
 
partial Polynomial removal lemmas for ordered graphs
 (2021)
 

 
 unknown · arXiv preprint · arXiv:2110.03577

Characterises exactly when \delta_F(\varepsilon) can be chosen polynomially for ordered-graph removal lemmas (only for |V(F)|=2 or one specific 3-vertex case), explicitly citing the Alon--Ben-Eliezer--Fischer result; implies polynomial bounds for general ordered binary matrix families are unlikely.
 

 
 
partial Polynomial removal lemma for ordered matchings
 (2023)
 

 
 unknown · arXiv preprint · arXiv:2307.01652

Proves that for any ordered matching H on t vertices, an ordered n-vertex graph that is \varepsilon-far from H-free contains poly(\varepsilon)\cdot n^t copies of H, establishing a polynomial removal lemma for the ordered matching special case (a subclass of ordered binary matrices).
 

 

 Reviewer notes. The paper arXiv:1609.04235 (Alon--Ben-Eliezer, submitted Sep 2016, journal 'Order' 2019) achieves polynomial dependence for a single forbidden ordered binary matrix; it predates the source paper and is therefore not listed in since_posted, but the source paper likely treats it as the starting point motivating the open problem for finite families. The two since_posted papers address ordered graphs and ordered matchings respectively -- closely related but not identical to ordered binary matrices in general. Author lists for arXiv:2110.03577 and arXiv:2307.01652 could not be confirmed from the abstract pages alone and are marked unknown.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It will be interesting to combine the ideas from the current proof with the binary matrix regularity lemma of Alon, Fischer and Newman to obtain a removal lemma for finite families of ordered binary matrices with better dependence between the parameters $\delta^{-1}$ and $\varepsilon^{-1}$; ideally polynomial dependence, but even exponential dependence would be interesting.

Context

For ordered binary matrices, Alon, Fischer and Newman obtained an efficient conditional regularity lemma in which $\delta^{-1}$ is polynomial in $\varepsilon^{-1}$. The general ordered removal lemma proved in this paper inherits a wowzer-type dependence from the strong regularity lemma, and improving this for finite families of ordered binary matrices is posed as an open problem.

Notes. Stated as a research direction in Section 1.3 without a formal labelled environment.

Source paper

 Testing hereditary properties of ordered graphs and matrices
 Noga Alon, Omri Ben-Eliezer, Eldar Fischer · 2017-04-07
 https://arxiv.org/abs/1704.02367
 PDF source

=== Source paper abstract / header ===
Abstract:We consider properties of edge-colored vertex-ordered graphs, i.e., graphs with a totally ordered vertex set and a finite set of possible edge colors. We show that any hereditary property of such graphs is strongly testable, i.e., testable with a constant number of queries. We also explain how the proof can be adapted to show that any hereditary property of $2$-dimensional matrices over a finite alphabet (where row and column order is not ignored) is strongly testable. The first result generalizes the result of Alon and Shapira [FOCS'05, SICOMP'08], who showed that any hereditary graph property (without vertex order) is strongly testable. The second result answers and generalizes a conjecture of Alon, Fischer and Newman [SICOMP'07] concerning testing of matrix properties.
The testability is proved by establishing a removal lemma for vertex-ordered graphs. It states that for any finite or infinite family $\mathcal{F}$ of forbidden vertex-ordered graphs, and any $\epsilon > 0$, there exist $\delta > 0$ and $k$ so that any vertex-ordered graph which is $\epsilon$-far from being $\mathcal{F}$-free contains at least $\delta n^{|F|}$ copies of some $F\in\mathcal{F}$ (with the correct vertex order) where $|F|\leq k$. The proof bridges the gap between techniques related to the regularity lemma, used in the long chain of papers investigating graph testing, and string testing techniques. Along the way we develop a Ramsey-type lemma for $k$-partite graphs with "undesirable" edges, stating that one can find a Ramsey-type structure in such a graph, in which the density of the undesirable edges is not much higher than the density of those edges in the graph.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1704.02367 [cs.DS]
 

 
  
 (or 
 arXiv:1704.02367v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1704.02367
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Omri Ben-Eliezer [view email] 
 [v1]
 Fri, 7 Apr 2017 20:29:56 UTC (44 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Testing hereditary properties of ordered graphs and matrices, by Noga Alon and 2 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2017-04
 

 Change to browse by:
 
 cs
 cs.CC
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Noga Alon
Omri Ben-Eliezer
Eldar Fischer 

 

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
