Attack the following open graph-theory problem.

Catalog id: 1810.00058__00
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1810.00058__00/
Source paper: Sparse graphs with no polynomial-sized anticomplete pairs (arXiv:1810.00058)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.4
For every graph $H$ there exists $\varepsilon > 0$ such that in every $H$-free $\varepsilon$-bounded graph $G$ with $|G| > 1$ vertices, there is an anticomplete $(\varepsilon|G|, \varepsilon|G|)$-pair.

Context:
A graph $G$ is $\varepsilon$-bounded if its maximum degree is less than $\varepsilon|G|$. By a theorem of Rödl, $H$ satisfies Conjecture 1.3 if and only if both $H$ and $\bar{H}$ satisfy Conjecture 1.4, so the two conjectures are equivalent over all $H$. For certain graphs $H$, however, 1.4 is more tractable than 1.3.

=== Catalog page (statement + literature review) ===
Linear anticomplete pairs in sparse H-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 1.4 from arXiv:1810.00058 remains open in full generality. Partial progress has been made: Fox, Nguyen, Scott, and Seymour (arXiv:2307.00801) proved the conjecture for H=P4 with the optimal bound δ=ε, and more generally for all graphs H obtainable by vertex-substitution from copies of P4 and its subgraphs, via the stronger 'viral' property. Separately, Bucić, Fox, and Pham (arXiv:2403.08303) proved that the polynomial Rödl conjecture (Conjecture 1.3 in the source paper, which is equivalent to Conjecture 1.4 over all H by Rödl's theorem) is equivalent to the Erdős-Hajnal conjecture, establishing that the full resolution of Conjecture 1.4 is as hard as settling Erdős-Hajnal.

 Cited literature (3)

 
 
 
partial Induced subgraph density. II. Sparse and dense sets in cographs
 (2023)
 

 
 Jacob Fox, Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2307.00801

Proves Conjecture 1.4 for H=P4 with the optimal bound δ=ε, and more generally for all graphs H obtainable by vertex-substitution from P4 and its subgraphs, via the 'viral' property.
 

 
 
reduction Equivalence between Erdős-Hajnal and polynomial Rödl and Nikiforov conjectures
 (2024)
 

 
 Matija Bucić, Jacob Fox, Huy Tuan Pham · arXiv preprint · arXiv:2403.08303

Proves that the polynomial Rödl conjecture (equivalent to Conjecture 1.4 for all H via Rödl's theorem) is equivalent to the Erdős-Hajnal conjecture; deduces that string graphs satisfy the polynomial Rödl conjecture.
 

 
 
partial Induced subgraph density. IV. New graphs with the Erdős-Hajnal property
 (2023)
 

 
 Tung Nguyen, Alex Scott, Paul Seymour · arXiv preprint · arXiv:2307.06455

Establishes the Erdős-Hajnal property for infinitely many new graph classes, implicitly verifying Conjecture 1.4 for those classes via the equivalence proved by Bucić, Fox, and Pham.
 

 

 Reviewer notes. Conjecture 1.4 is equivalent to Conjecture 1.3 (pure pairs) for all H simultaneously, by Rödl's theorem. Conjecture 1.3 in turn is now known to be equivalent to the Erdős-Hajnal conjecture (arXiv:2403.08303), so full resolution of Conjecture 1.4 is tied to one of the most prominent open problems in extremal graph theory. Partial results verified for P4-substitution families. The paper arXiv:2301.10147 takes a different approach via blockades and leaves this conjecture open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every graph $H$ there exists $\varepsilon > 0$ such that in every $H$-free $\varepsilon$-bounded graph $G$ with $|G| > 1$ vertices, there is an anticomplete $(\varepsilon|G|, \varepsilon|G|)$-pair.

Context

A graph $G$ is $\varepsilon$-bounded if its maximum degree is less than $\varepsilon|G|$. By a theorem of Rödl, $H$ satisfies Conjecture 1.3 if and only if both $H$ and $\bar{H}$ satisfy Conjecture 1.4, so the two conjectures are equivalent over all $H$. For certain graphs $H$, however, 1.4 is more tractable than 1.3.

Notes. PDF source — math may be garbled; the paper proves this for all almost-bipartite $H$ as Theorem 1.5

Source paper

 Sparse graphs with no polynomial-sized anticomplete pairs
 Maria Chudnovsky, Jacob Fox, Alex Scott, Paul Seymour, Sophie Spirkl · 2020-12-07
 https://arxiv.org/abs/1810.00058
 PDF source

Related conjectures

 
 implies
 K₃ polynomial anticomplete pair property
 open
 Pure instantiation. Conjecture 1.4 is universally quantified over all graphs H; the target is exactly the instance H = K_3 of that statement (an anticomplete linear pair in every triangle-free epsilon-bounded graph). Truth of the universal statement forces truth of each instance, so source implies target; the converse fails since 1.4 for K_3 says nothing about other H. Direction as claimed is correct. The target's context confirms it is the same Conjecture 1.4 restricted to the triangle (the simplest H not covered by the paper's almost-bipartite theorem).
 

 
 implied by
 Sparse pairs in H-free ε-bounded graphs
 partial
 The source's own context text explicitly states 'The implications 3.3 => 3.4 => 1.4 hold', where 3.4 is the source (c-sparse pairs in H-free epsilon-bounded graphs) and 1.4 is the target (anticomplete linear pairs). The direction matches the claim. Note the implication is not the trivial c=0 instantiation (at c=0 the guaranteed pair size epsilon*c^s*|G| degenerates to 0); it requires the paper's cleaning argument turning sparse pairs into anticomplete pairs, but since the paper itself asserts the implication, this is a literature-stated relation, not just a sketch. Both statements quantify over the same class (H-free epsilon-bounded graphs), so no hypothesis-class mismatch.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:A graph is "$H$-free" if it has no induced subgraph isomorphic to $H$. A conjecture of Conlon, Fox and Sudakov states that for every graph $H$, there exists $s>0$ such that in every $H$-free graph with $n>1$ vertices, either some vertex has degree at least $sn$, or there are two disjoint sets of vertices, of sizes at least $sn^s$ and $sn$, anticomplete to each other. We prove this holds for a large class of graphs $H$, and we prove that something like it holds for all graphs $H$.
Say $H$ is "almost-bipartite" if $H$ is triangle-free and $V(H)$ can be partitioned into a stable set and a set inducing a graph of maximum degree at most one. We prove that the conjecture above holds for when $H$ is almost-bipartite. We also prove a stronger version where instead of excluding $H$ we restrict the number of copies of $H$.
We prove some variations on the conjecture, such as: for every graph $H$, there exists $s >0$ such that in every $H$-free graph with $n>1$ vertices, either some vertex has degree at least $sn$, or there are two disjoint sets $A, B$ of vertices with $|A||B| > s n^{1 + s}$, anticomplete to each other.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1810.00058 [math.CO]
 

 
  
 (or 
 arXiv:1810.00058v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1810.00058
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Paul Seymour [view email] 
 [v1]
 Fri, 28 Sep 2018 19:46:19 UTC (25 KB)

 [v2]
 Mon, 7 Dec 2020 15:15:02 UTC (26 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Sparse graphs with no polynomial-sized anticomplete pairs, by Maria Chudnovsky and 4 other authors
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
 | 2018-10
 

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
