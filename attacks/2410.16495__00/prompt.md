Attack the following open graph-theory problem.

Catalog id: 2410.16495__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2410.16495__00/
Source paper: Induced subgraphs and tree decompositions XVI. Complete bipartite induc… (arXiv:2410.16495)

=== Extracted statement (catalog JSON) ===
Title: Question 1.1
What are the unavoidable induced subgraphs of graphs with large treewidth?

Context:
This question is the central goal of the series of papers on induced subgraphs and tree decompositions. The answer is known when 'induced subgraphs' is replaced by 'subgraphs' or 'minors' via Robertson and Seymour's grid theorem, but the induced setting is more complex, requiring all basic obstructions (complete graphs, complete bipartite graphs, subdivided walls, and their line graphs) as well as non-basic ones such as Pohoata-Davies graphs, occultations, and layered wheels.

=== Catalog page (statement + literature review) ===
Unavoidable induced subgraphs of large treewidth — Graph-theory open problems (arXiv)

 
 Status
 disproved
 high confidence
 

 What the 'disproved' badge means here: the question is not being declared meaningless or trivially closed — rather, the clean answer it hoped for is now proven impossible. Question 1.1 asks for the unavoidable induced subgraphs of graphs with large treewidth: the induced-subgraph analogue of the Robertson–Seymour Grid Minor theorem (where subdivided walls are the unavoidable subgraphs) and the central programmatic goal of the Chudnovsky–Hajebi–Spirkl 'Induced subgraphs and tree decompositions' series. The hope was a single 'holy grail' family F* of unavoidable induced subgraphs that works for every hereditary class of unbounded treewidth. That hope is refuted by Alecu, Bonnet, Bureo Villafana and Trotignon, 'Every Graph is Essential to Large Treewidth' (arXiv:2502.14775, Feb 2025): their Theorem 1.1 shows that for every single graph H there is a hereditary (weakly sparse) class of unbounded treewidth whose H-free subclass has bounded treewidth — so every graph H is 'essential', and no F* can work except the class of all graphs. There is therefore no clean induced analogue of the Grid Minor theorem, and several explicit conjectures fall with it (Hajebi's Conjectures 1.14/1.15 and a conjecture of Trotignon). What remains alive is the restricted programme: for specific excluded-obstruction classes the CHS series still proves treewidth characterizations (e.g. paper XIX, arXiv:2506.05602). So: general clean characterization — provably does not exist; structure theory for restricted hereditary classes — ongoing.

 Cited literature (3)

 
 
 
disproved Every Graph is Essential to Large Treewidth
 (2025)
 

 
 Bogdan Alecu, Édouard Bonnet, Pedro Bureo Villafana, Nicolas Trotignon · arXiv preprint (v3, 1 Apr 2025) · arXiv:2502.14775

Refutes the existence of an induced-subgraph analogue of the Grid Minor theorem. Theorem 1.1: for every graph H there is a hereditary weakly sparse class C_H of unbounded treewidth whose H-free subclass has bounded treewidth (strengthened in Thm 1.2 to: for every t, a class where H-free graphs of treewidth ≤ t have bounded treewidth, for every H). Consequence: no family F* of unavoidable induced subgraphs works except the class of all graphs — 'every graph is essential' — so Question 1.1 has no clean characterization in general. Built from a generalized 'abstract layered wheel' construction; also refutes Hajebi's Conjectures 1.14/1.15 and a conjecture of Trotignon.
 

 
 
partial Induced subgraphs and tree decompositions XIX. Thetas and forests
 (2025)
 

 
 Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · arXiv preprint · arXiv:2506.05602

Proves treewidth is polynomially bounded by clique number in hereditary classes that are theta-free and exclude line graphs of subdivisions of some wall, making partial progress toward the full characterization sought by Question 1.1.
 

 
 
partial A simple layered-wheel-like construction
 (2025)
 

 
 Authors unconfirmed from fetch · arXiv preprint · arXiv:2507.06169

Constructs layered-wheel-like graphs achieving high girth with bounded outerstring treewidth, providing a simpler approach to the obstruction class identified as the last barrier to a complete induced-subgraph/treewidth characterization; also disproves a conjecture of Trotignon.
 

 

 Reviewer notes. Status changed open -> disproved on 2026-05-29 after arXiv:2502.14775 (Alecu, Bonnet, Bureo Villafana, Trotignon) was identified as refuting the strongest form of Question 1.1. The 'disproved' label refers to the implicit conjecture that a clean induced analogue of the Grid Minor theorem (a unavoidable-induced-subgraph family F*) exists; the broad question itself remains a live research programme for restricted classes, where characterizations are still being proved (CHS series papers XVI–XIX). Caveat: Question 1.1 is worded as an open-ended question rather than a yes/no conjecture, so 'disproved' is a curatorial judgement that the hoped-for clean characterization provably fails. Paper XVIII (arXiv:2412.17756, Dec 2024) fully resolves the analogous question for pathwidth. Earlier framing treated the question as fully open as of 2026.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. What are the unavoidable induced subgraphs of graphs with large treewidth?

Context

This question is the central goal of the series of papers on induced subgraphs and tree decompositions. The answer is known when 'induced subgraphs' is replaced by 'subgraphs' or 'minors' via Robertson and Seymour's grid theorem, but the induced setting is more complex, requiring all basic obstructions (complete graphs, complete bipartite graphs, subdivided walls, and their line graphs) as well as non-basic ones such as Pohoata-Davies graphs, occultations, and layered wheels.

Source paper

 Induced subgraphs and tree decompositions XVI. Complete bipartite induced minors
 Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · 2026-02-18
 https://arxiv.org/abs/2410.16495

=== Source paper abstract / header ===
Abstract:We prove that for every graph $G$ with a sufficiently large complete bipartite induced minor, either $G$ has an induced minor isomorphic to a large wall, or $G$ contains a large constellation; that is, a complete bipartite induced minor model such that on one side of the bipartition, each branch set is a singleton, and on the other side, each branch set induces a path.
We further refine this theorem by characterizing the unavoidable induced subgraphs of large constellations as two types of highly structured constellations. These results will be key ingredients in several forthcoming papers of this series.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2410.16495 [math.CO]
 

 
  
 (or 
 arXiv:2410.16495v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2410.16495
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Combinatorial Theory, Series B 176, 2026, 287-318
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.jctb.2025.09.005

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sepehr Hajebi [view email] 
 [v1]
 Mon, 21 Oct 2024 20:35:47 UTC (168 KB)

 [v2]
 Wed, 23 Oct 2024 17:09:18 UTC (168 KB)

 [v3]
 Wed, 13 Nov 2024 21:39:28 UTC (172 KB)

 [v4]
 Wed, 18 Feb 2026 20:50:40 UTC (171 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced subgraphs and tree decompositions XVI. Complete bipartite induced minors, by Maria Chudnovsky and 2 other authors
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
 | 2024-10
 

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
