Attack the following open graph-theory problem.

Catalog id: 1605.07411__00
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1605.07411__00/
Source paper: $χ$-bounded families of oriented graphs (arXiv:1605.07411)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2
$\mathrm{Forb}(H)$ is $\chi$-bounded if and only if $H$ is a forest.

Context:
The paper notes that an easy argument shows this conjecture is equivalent to the Gyárfás–Sumner Conjecture (Conjecture 1). It generalises the 'only if' direction (which follows from Erdős's girth theorem) to a complete characterisation.

=== Catalog page (statement + literature review) ===
Forb(H) χ-bounded iff H is forest — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 2 from arXiv:1605.07411 — that $\mathrm{Forb}(H)$ is $\chi$-bounded if and only if $H$ is a forest in the directed/oriented setting — is explicitly stated in the source paper to be equivalent to the Gyárfás–Sumner conjecture and remains open in full generality. Substantial partial progress has been made: the conjecture is proved for every orientation of $P_4$ (Cook et al., 2022/2023), for $(\overrightarrow{P}_6, \text{triangle})$-free digraphs (Aboulker et al., 2022), and for locally out-transitive oriented graphs, i.e., the $H = S_2^+$ case (Aboulker et al., 2021). No counterexample has been found and the full conjecture remains open.

 Cited literature (3)

 
 
 
partial Decomposing and colouring some locally semicomplete digraphs
 (2021)
 

 
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit · arXiv preprint · arXiv:2103.07886

Proves that oriented graphs in which the out-neighbourhood of every vertex induces a transitive tournament have dichromatic number at most 2, establishing the conjecture for the special case $H = S_2^+$.
 

 
 
partial Proving a directed analogue of the Gyárfás-Sumner conjecture for orientations of $P_4$
 (2023)
 

 
 Linda Cook, Tomáš Masařík, Marcin Pilipczuk, Amadeus Reinald, Uéverton S. Souza · The Electronic Journal of Combinatorics · arXiv:2209.06171

Proves the directed Gyárfás–Sumner conjecture for the case where $H$ is any orientation of a path on four vertices ($P_4$), showing such $H$-free oriented graphs have dichromatic number bounded by a function of $\omega$.
 

 
 
partial (P6, triangle)-free digraphs have bounded dichromatic number
 (2022)
 

 
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit, Stéphan Thomassé · arXiv preprint · arXiv:2212.02272

Proves that oriented graphs with no induced $\overrightarrow{P}_6$ and no triangle have dichromatic number at most 382, establishing the conjecture for the $(\overrightarrow{P}_6, \text{triangle-free})$ special case.
 

 

 Reviewer notes. Conjecture 2 is explicitly equivalent to the Gyárfás–Sumner conjecture (Conjecture 1 of the same paper), so progress is tracked through both the directed (dichromatic number) and undirected (chromatic number) literature. The directed analogue is attributed to Aboulker, Charbit, and Naserasr. The full conjecture is open as of 2026; partial results cover $P_4$ orientations, $P_6$-free triangle-free digraphs, and locally out-transitive graphs.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. $\mathrm{Forb}(H)$ is $\chi$-bounded if and only if $H$ is a forest.

Context

The paper notes that an easy argument shows this conjecture is equivalent to the Gyárfás–Sumner Conjecture (Conjecture 1). It generalises the 'only if' direction (which follows from Erdős's girth theorem) to a complete characterisation.

Notes. PDF source — math may be garbled. Stated by the paper authors as a reformulation equivalent to the Gyárfás–Sumner Conjecture; no separate citation in the header.

Source paper

 $χ$-bounded families of oriented graphs
 Pierre Aboulker, Jørgen Bang-Jensen, Nicolas Bousquet, Pierre Charbit, Frédéric Havet, Frédéric Maffray, Jose Zamora · 2016-05-24
 https://arxiv.org/abs/1605.07411
 PDF source

Related conjectures

 
 equivalent to
 Graphs with a forbidden induced tree are chi-bounded
 partial
 Verified in the paper's text (Conjecture 2, about undirected graphs H): 'an easy argument shows that the conjecture is equivalent to the following one. Conjecture 2. Forb(H) is χ-bounded if and only if H is a forest.' The claimed implication holds immediately: the 'if' direction at H = T (a tree is a forest) is exactly Gyárfás–Sumner. The converse also holds, so the relation is in fact an equivalence: the 'only if' direction follows from Erdős's girth theorem (high-girth high-χ graphs avoid any H with a cycle), and the forest case follows from the tree case since any forest is an induced subgraph of a tree. Note: the finder's sketch misreads H as an oriented forest; Conjecture 2 in the paper is about undirected graphs, which makes the implication direct.
 

 
 equivalent to
 Graphs with a forbidden induced tree are chi-bounded
 partial
 The source's own context explicitly states that an easy argument shows the biconditional 'Forb(H) is chi-bounded iff H is a forest' is equivalent to the Gyarfas-Sumner conjecture (the target). Verification: (target => source) the 'only if' half of the source is Erdos's girth theorem (if H contains a cycle, graphs of girth > |H| and huge chromatic number are H-free with omega = 2), and the 'if' half for a forest H follows from the tree case by a standard easy induction on components (this closure under disjoint union is known for ordinary chi-boundedness, unlike the polynomial version). (source => target) trivial restriction: a tree is a forest. So the two are genuinely equivalent, as claimed.
 

 
 implied by
 Polynomial χ-boundedness for H-free forest classes
 partial
 Self-contained hypothesis-strength argument. Source: for every forest H, the class of H-free graphs is polynomially χ-bounded. Polynomial χ-boundedness trivially implies χ-boundedness, so the source implies the Gyárfás–Sumner conjecture, which is precisely the 'if' direction of the target. The 'only if' direction of the target is a known theorem, not a conjecture: if H contains a cycle, Erdős's construction of graphs with girth > |V(H)| and unbounded chromatic number lies in Forb(H) (these graphs contain no induced H), so Forb(H) is not χ-bounded — the target's own context states this and that the target is equivalent to Gyárfás–Sumner. Hence source ⇒ Gyárfás–Sumner ⇒ target. The converse fails (χ-bounded does not give polynomial bounds), so 'implies' with source strictly stronger is the correct direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:A famous conjecture of Gyárfás and Sumner states for any tree $T$ and integer $k$, if the chromatic number of a graph is large enough, either the graph contains a clique of size $k$ or it contains $T$ as an induced subgraph. We discuss some results and open problems about extensions of this conjecture to oriented graphs. We conjecture that for every oriented star $S$ and integer $k$, if the chromatic number of a digraph is large enough, either the digraph contains a clique of size $k$ or it contains $S$ as an induced subgraph. As an evidence, we prove that for any oriented star $S$, every oriented graph with sufficiently large chromatic number contains either a transitive tournament of order $3$ or $S$ as an induced subdigraph. We then study for which sets ${\cal P}$ of orientations of $P_4$ (the path on four vertices) similar statements hold. We establish some positive and negative results.
 

 
 
 
 Comments:
 27 pages, 4 figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:1605.07411 [cs.DM]
 

 
  
 (or 
 arXiv:1605.07411v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1605.07411
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Pierre Aboulker [view email] 
 [v1]
 Tue, 24 May 2016 12:28:54 UTC (41 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled $\chi$-bounded families of oriented graphs, by Pierre Aboulker and 6 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2016-05
 

 Change to browse by:
 
 cs
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Pierre Aboulker
Jørgen Bang-Jensen
Nicolas Bousquet
Pierre Charbit
Frédéric Havet …

 

 

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
