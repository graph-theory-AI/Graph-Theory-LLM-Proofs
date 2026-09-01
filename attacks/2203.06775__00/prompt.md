Attack the following open graph-theory problem.

Catalog id: 2203.06775__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2203.06775__00/
Source paper: Induced subgraphs and tree decompositions IV. (Even hole, diamond, pyra… (arXiv:2203.06775)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.6
For all $t > 0$ there exists $c_t \geq 0$ such that $\mathrm{tw}(G) \leq c_t$ for every $G \in \mathcal{C}^*_t$.

Context:
Here $\mathcal{C}^*_t$ denotes the class of $(C_4, \text{diamond}, \text{theta}, \text{prism}, \text{even wheel}, K_t)$-free graphs — a relaxation of $\mathcal{C}_t$ in which pyramids are no longer excluded. The authors pose this as a slight generalization of Sintiari–Trotignon's Conjecture 1.5, noting that Theorem 1.4 (the main result of the paper) would serve as the base case if the conjecture could be proved by the same techniques.

=== Catalog page (statement + literature review) ===
Bounded treewidth for (C₄, diamond, theta, prism)-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 1.6 posits a constant treewidth bound $\mathrm{tw}(G) \leq c_t$ for all $G \in \mathcal{C}^*_t$ ($(C_4$, diamond, theta, prism, even wheel, $K_t)$-free graphs). No verified proof or counterexample of the full conjecture was found. The closely related Sintiari–Trotignon conjecture (Conjecture 1.5 in the source paper) on even-hole-free $K_t$-free graphs was resolved in 2024 by arXiv:2402.14211 with a logarithmic bound $c_t \log n$ shown to be asymptotically tight, which does not settle Conjecture 1.6 since $\mathcal{C}^*_t$ is a more restricted class and the conjecture asks for a constant bound. Web searches suggest possible counterexamples to related bounded-treewidth conjectures by Hajebi (a co-author) appearing in 2025, but these could not be verified within the search budget.

 Cited literature (1)

 
 
 
partial Induced subgraphs and tree decompositions XV. Even-hole-free graphs with bounded clique number
 (2024)
 

 
 Maria Chudnovsky, Peter Gartland, Sepehr Hajebi, Daniel Lokshtanov, Sophie Spirkl · arXiv preprint · arXiv:2402.14211

Proves every $n$-vertex even-hole-free graph with no $K_t$ satisfies $\mathrm{tw}(G) \leq c_t \log n$ and shows this logarithmic bound is tight, resolving Conjecture 1.5 (Sintiari–Trotignon) but leaving Conjecture 1.6's constant bound for the more restricted class $\mathcal{C}^*_t$ open.
 

 

 Reviewer notes. Conjecture 1.6 asks for a CONSTANT bound $c_t$ on $\mathrm{tw}$ for $\mathcal{C}^*_t$, which is a harder question than the logarithmic bound proved for the strictly larger even-hole-free $K_t$-free class by arXiv:2402.14211. Web searches surfaced a 2025 Journal of Graph Theory paper by Hajebi ('Chordal Graphs, Even-Hole-Free Graphs and Sparse Obstructions to Bounded Treewidth') and a mention of counterexamples to a Hajebi-attributed bounded-treewidth conjecture, but these could not be verified within the 5-call budget; confidence is set to medium rather than high for this reason.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For all $t > 0$ there exists $c_t \geq 0$ such that $\mathrm{tw}(G) \leq c_t$ for every $G \in \mathcal{C}^*_t$.

Context

Here $\mathcal{C}^*_t$ denotes the class of $(C_4, \text{diamond}, \text{theta}, \text{prism}, \text{even wheel}, K_t)$-free graphs — a relaxation of $\mathcal{C}_t$ in which pyramids are no longer excluded. The authors pose this as a slight generalization of Sintiari–Trotignon's Conjecture 1.5, noting that Theorem 1.4 (the main result of the paper) would serve as the base case if the conjecture could be proved by the same techniques.

Source paper

 Induced subgraphs and tree decompositions IV. (Even hole, diamond, pyramid)-free graphs
 Tara Abrishami, Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · 2022-10-21
 https://arxiv.org/abs/2203.06775
 PDF source

=== Source paper abstract / header ===
Abstract:A hole in a graph $G$ is an induced cycle of length at least four, and an even hole is a hole of even length. The diamond is the graph obtained from the complete graph $K_4$ by removing an edge. A pyramid is a graph consisting of a triangle called the base, a vertex called the apex, and three internally disjoint paths starting at the apex and disjoint otherwise, each joining the apex to a vertex of the base. For a family $\mathcal{H}$ of graphs, we say a graph $G$ is $\mathcal{H}$-free if no induced subgraph of $G$ is isomorphic to a member of $\mathcal{H}$. Cameron, da Silva, Huang, and Vušković proved that (even hole, triangle)-free graphs have treewidth at most five, which motivates studying the treewidth of even-hole-free graphs of larger clique number. Sintiari and Trotignon provided a construction of (even hole, pyramid, $K_4$)-free graphs of arbitrarily large treewidth.
Here, we show that for every $t$, (even hole, pyramid, diamond, $K_t$)-free graphs have bounded treewidth. The graphs constructed by Sintiari and Trotignon contain diamonds, so our result is sharp in the sense that it is false if we do not exclude diamonds. Our main result is in fact more general, that treewidth is bounded in graphs excluding certain wheels and three-path-configurations, diamonds, and a fixed complete graph. The proof uses "non-crossing decompositions" methods similar to those in previous papers in this series. In previous papers, however, bounded degree was a necessary condition to prove bounded treewidth. The result of this paper is the first to use the method of "non-crossing decompositions" to prove bounded treewidth in a graph class of unbounded maximum degree.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2203.06775 [math.CO]
 

 
  
 (or 
 arXiv:2203.06775v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2203.06775
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Electron. J. Combin. 30 (2023), no. 2, Paper No. 2.42, 19 pp
 

 
 
 Related DOI:
 
 https://doi.org/10.37236/11623

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tara Abrishami [view email] 
 [v1]
 Sun, 13 Mar 2022 22:01:16 UTC (18 KB)

 [v2]
 Fri, 21 Oct 2022 03:56:48 UTC (18 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced subgraphs and tree decompositions IV. (Even hole, diamond, pyramid)-free graphs, by Tara Abrishami and 3 other authors
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
 | 2022-03
 

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
