Attack the following open graph-theory problem.

Catalog id: 1604.07976__01
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1604.07976__01/
Source paper: Smaller Extended Formulations for the Spanning Tree Polytope of Bounded… (arXiv:1604.07976)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2
If $\mathcal{C}$ is a proper minor-closed family of graphs and $G = (V, E)$ is a connected graph in $\mathcal{C}$, then $\mathrm{xc}(P_{\mathrm{sp.trees}}(G)) = O(|V|)$.

Context:
Following Conjecture 1, the authors suggest the linear bound may hold even more generally for all proper minor-closed families. They note the conjecture is known to hold when graphs in $\mathcal{C}$ have bounded treewidth, and they prove it for $k$-apex graphs (Theorem 4) as additional supporting evidence.

=== Catalog page (statement + literature review) ===
Linear extension complexity for minor-closed families — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture that $\mathrm{xc}(P_{\mathrm{sp.trees}}(G)) = O(|V|)$ for every proper minor-closed family $\mathcal{C}$ and connected $G \in \mathcal{C}$ remains open. The main post-2017 progress is due to Aprile, Fiorini, Huynh, Joret, and Wood (2021), who proved an $O(n^{3/2})$ upper bound for any proper minor-closed class (and more generally $O(n^{1+\beta})$ for classes with $O(n^\beta)$-size balanced separators), improving the previously known $O(n^2)$ bounds. The linear $O(n)$ bound has been established for planar graphs and for graphs of bounded treewidth, but the full conjecture for all proper minor-closed families is unresolved.

 Cited literature (1)

 
 
 
partial Smaller Extended Formulations for Spanning Tree Polytopes in Minor-Closed Classes and Beyond
 (2021)
 

 
 Manuel Aprile, Samuel Fiorini, Tony Huynh, Gwenaël Joret, David R. Wood · The Electronic Journal of Combinatorics · arXiv:2106.11945 · doi:10.37236/10522

Proves $\mathrm{xc}(P_{\mathrm{sp.trees}}(G)) = O(n^{3/2})$ for connected $n$-vertex graphs in any proper minor-closed class, improving the $O(n^2)$ bound, but the conjectured $O(n)$ bound remains open.
 

 

 Reviewer notes. The conjecture is open for general proper minor-closed families. The best known upper bound as of 2021 is O(n^{3/2}) by Aprile et al. (arXiv:2106.11945, EJC 2021). No 2022–2026 paper resolving the full conjecture was found in the search.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. If $\mathcal{C}$ is a proper minor-closed family of graphs and $G = (V, E)$ is a connected graph in $\mathcal{C}$, then $\mathrm{xc}(P_{\mathrm{sp.trees}}(G)) = O(|V|)$.

Context

Following Conjecture 1, the authors suggest the linear bound may hold even more generally for all proper minor-closed families. They note the conjecture is known to hold when graphs in $\mathcal{C}$ have bounded treewidth, and they prove it for $k$-apex graphs (Theorem 4) as additional supporting evidence.

Source paper

 Smaller Extended Formulations for the Spanning Tree Polytope of Bounded-genus Graphs
 Samuel Fiorini, Tony Huynh, Gwenaël Joret, Kanstantsin Pashkovich · 2017-01-09
 https://arxiv.org/abs/1604.07976
 PDF source

Related conjectures

 
 implies
 Linear xc bound for bounded-genus spanning trees
 open
 Hypothesis-class containment. For a fixed surface S, the class C_S of graphs embeddable in S is minor-closed (deleting/contracting edges cannot increase genus, i.e. genus is minor-monotone) and proper (K_n for large n does not embed in S, since the genus of K_n grows unboundedly). Hence any connected graph embedded in a fixed surface lies in a proper minor-closed family, and the source conjecture's conclusion xc(P_sp.trees(G)) = O(|V|) applies to it, which is exactly the target's conclusion. Direction is correct: the minor-closed conjecture (Conjecture 2 in the paper) is the stronger, more general statement and restricts to the bounded-genus conjecture (Conjecture 1).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:We give an $O(g^{1/2} n^{3/2} + g^{3/2} n^{1/2})$-size extended formulation for the spanning tree polytope of an $n$-vertex graph embedded on a surface of genus $g$, improving on the known $O(n^2 + g n)$-size extended formulations following from Wong and Martin.
 

 
 
 
 Comments:
 v3: fixed some typos
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05Cxx
 

 Cite as:
 arXiv:1604.07976 [math.CO]
 

 
  
 (or 
 arXiv:1604.07976v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1604.07976
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete & Computational Geometry, 57(3), 757-761 (2017)
 

 
 
 Related DOI:
 
 https://doi.org/10.1007/s00454-016-9852-9

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Gwenaël Joret [view email] 
 [v1]
 Wed, 27 Apr 2016 08:45:52 UTC (7 KB)

 [v2]
 Tue, 20 Dec 2016 15:46:51 UTC (9 KB)

 [v3]
 Mon, 9 Jan 2017 14:22:50 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Smaller Extended Formulations for the Spanning Tree Polytope of Bounded-genus Graphs, by Samuel Fiorini and 3 other authors
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
 | 2016-04
 

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
