Attack the following open graph-theory problem.

Catalog id: 2307.06455__00
Catalog status: open (triage tier 4, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2307.06455__00/
Source paper: Induced subgraph density. IV. New graphs with the Erdős-Hajnal property (arXiv:2307.06455)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.8
For every graph $H$, there exists $d>0$ such that for every $\varepsilon\in(0,\frac{1}{2})$ and every graph $G$ with $\mathrm{ind}_{H}(G)\leq(\varepsilon^{d}\lvert G\rvert)^{\lvert H\rvert}$, there is an $\varepsilon$-restricted subset of $V(G)$ with size at least $\varepsilon^{d}\lvert G\rvert$.

Context:
This 'polynomial Nikiforov' statement, introduced without external attribution, unifies Theorem 1.6 and Conjecture 1.7. A graph $H$ satisfying it is called viral; Bucić, Fox, and Pham [4] proved that having the Erdős-Hajnal property is equivalent to being viral.

=== Catalog page (statement + literature review) ===
Polynomial Nikiforov universality for graphs — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 The Erdös-Hajnal Conjecture
 (fuzzy-match score 75).

 
 Status
 open
 high confidence
 

 Conjecture 1.8 (the 'polynomial Nikiforov' conjecture) asserts that every graph H is viral, i.e., satisfies a polynomial-bound version of Nikiforov's theorem via ε-restricted subsets. Bucić, Fox, and Pham (arXiv:2403.08303, 2024) proved that the Erdős-Hajnal property is equivalent to being viral, establishing that Conjecture 1.8 is in turn equivalent to the full Erdős-Hajnal conjecture; since the latter remains open, so does Conjecture 1.8. No direct proof or counterexample for Conjecture 1.8 was found in the 2025–2026 literature.

 Cited literature (1)

 
 
 
reduction Equivalence between Erdős-Hajnal and polynomial Rödl and Nikiforov conjectures
 (2024)
 

 
 Matija Bucić, Jacob Fox, Huy Tuan Pham · arXiv preprint · arXiv:2403.08303

Proves that having the Erdős-Hajnal property is equivalent to being viral (i.e., satisfying Conjecture 1.8), thereby reducing the conjecture to the full Erdős-Hajnal conjecture.
 

 

 Reviewer notes. Conjecture 1.8 is equivalent to the full Erdős-Hajnal conjecture via the Bucić-Fox-Pham equivalence (arXiv:2403.08303). The source paper was first posted in July 2023; the 2026-04-18 date is the journal publication, which already cites Bucić-Fox-Pham as reference [4]. No further resolution found in the literature.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every graph $H$, there exists $d>0$ such that for every $\varepsilon\in(0,\frac{1}{2})$ and every graph $G$ with $\mathrm{ind}_{H}(G)\leq(\varepsilon^{d}\lvert G\rvert)^{\lvert H\rvert}$, there is an $\varepsilon$-restricted subset of $V(G)$ with size at least $\varepsilon^{d}\lvert G\rvert$.

Context

This 'polynomial Nikiforov' statement, introduced without external attribution, unifies Theorem 1.6 and Conjecture 1.7. A graph $H$ satisfying it is called viral; Bucić, Fox, and Pham [4] proved that having the Erdős-Hajnal property is equivalent to being viral.

Source paper

 Induced subgraph density. IV. New graphs with the Erdős-Hajnal property
 Tung Nguyen, Alex Scott, Paul Seymour · 2026-04-18
 https://arxiv.org/abs/2307.06455

=== Source paper abstract / header ===
Abstract:Erdős and Hajnal conjectured that for every graph $H$, there exists $c>0$ such that every $H$-free graph $G$ has a clique or a stable set of size at least $|G|^c$ (a graph is $H$-free if it has no induced subgraph isomorphic to $H$). Alon, Pach, and Solymosi reduced the Erdős-Hajnal conjecture to the case when $H$ is {\em prime} (that is, $H$ cannot be obtained by vertex-substitution from smaller graphs); but until now, it was not shown for any prime graph with more than five vertices.
We will provide infinitely many prime graphs that satisfy the conjecture. Let $H$ be a graph with the property that for every prime induced subgraph $G'$ with $|G'|\ge 3$, $G'$ has a vertex of degree one and a vertex of degree $|G'|-2$. We will prove that every graph $H$ with this property satisfies the Erdős-Hajnal conjecture, and infinitely many graphs with this property are prime. More generally, say a graph is {\em buildable} if every prime induced subgraph with at least three vertices has a vertex of degree one. We prove that if $H_1$ and $\overline{H_2}$ are buildable, there exists $c>0$ such that every graph $G$ that is both $H_1$-free and $H_2$-free has a clique or a stable set of size at least $|G|^c$.
Our proof uses a new technique of ``iterative sparsification'', where we pass to a sequence of successively more restricted induced subgraphs. This approach also extends to ordered graphs and to tournaments. For ordered graphs, we obtain a theorem which significantly extends a recent result of Pach and Tomon about excluding monotone paths; and for tournaments, we obtain infinitely many new prime tournaments that satisfy the Erdős-Hajnal conjecture (in tournament form).
 

 
 
 
 Comments:
 24 pages, accepted version
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C20, 05C35, 05C55, 05C69, 05C75
 

 Cite as:
 arXiv:2307.06455 [math.CO]
 

 
  
 (or 
 arXiv:2307.06455v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2307.06455
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Tung H. Nguyen [view email] 
 [v1]
 Wed, 12 Jul 2023 21:14:01 UTC (23 KB)

 [v2]
 Sun, 23 Jul 2023 15:48:21 UTC (24 KB)

 [v3]
 Sun, 3 Mar 2024 09:30:18 UTC (27 KB)

 [v4]
 Sat, 18 Apr 2026 12:06:07 UTC (31 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced subgraph density. IV. New graphs with the Erd\H{o}s-Hajnal property, by Tung Nguyen and 2 other authors
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
 | 2023-07
 

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
