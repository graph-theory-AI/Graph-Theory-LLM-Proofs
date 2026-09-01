Attack the following open graph-theory problem.

Catalog id: 1704.02367__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1704.02367__00/
Source paper: Testing hereditary properties of ordered graphs and matrices (arXiv:1704.02367)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: Regularity-free proof for the ordered removal lemma
It will be interesting to try to obtain a proof for the ordered graph removal lemma that does not go through the strong regularity lemma needed in the current proof.

Context:
The proofs of the ordered removal lemmas rely on strong variants of the graph regularity lemma, which impose a wowzer-type (tower-of-towers) dependence between the parameters $\delta^{-1}$ and $\varepsilon^{-1}$. Fox gave the first regularity-free proof of the unordered graph removal lemma, though still with tower-type dependence; an analogous approach for the ordered setting remains open.

=== Catalog page (statement + literature review) ===
Regularity-free ordered graph removal lemma — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The open problem of finding a regularity-free proof of the ordered graph removal lemma (analogous to Fox's 2011 proof for unordered graphs) remains open in general. Partial progress has been made: the paper arXiv:2110.03577 characterizes exactly which ordered graphs F admit a polynomial bound on delta_F(epsilon) in the induced ordered removal lemma; and arXiv:2307.01652 proves a polynomial removal lemma for ordered matchings via a novel nested-partition technique that avoids the regularity lemma for that special case. A full regularity-free proof for arbitrary ordered graphs has not been found.

 Cited literature (3)

 
 
 
partial Polynomial removal lemmas for ordered graphs
 (2021)
 

 
 unknown · arXiv preprint · arXiv:2110.03577

Characterizes exactly which ordered graphs F admit a polynomial bound delta_F(epsilon) in the induced ordered removal lemma (if and only if |V(F)|=2 or F is a specific three-vertex ordered graph up to symmetry), giving a complete picture of when the wowzer-type dependence can be avoided.
 

 
 
partial Polynomial removal lemma for ordered matchings
 (2023)
 

 
 unknown (includes Tomon) · arXiv preprint · arXiv:2307.01652

Proves a polynomial removal lemma for ordered matchings using a novel nested-partition cleaning argument that avoids the regularity lemma, achieving poly(epsilon) bounds for the special case of ordered matchings.
 

 
 
partial A Removal Lemma for Ordered Hypergraphs
 (2021)
 

 
 Towsner, Henry · Proceedings of the London Mathematical Society · arXiv:2101.09769 · doi:10.1112/plms.70015

Generalizes the Alon-Ben-Eliezer-Fischer ordered graph removal lemma to induced ordered hypergraphs, but does not address the regularity-free question.
 

 

 Reviewer notes. Fox's 2011 regularity-free proof for unordered graphs (arXiv:1006.1300) used entropy/energy-increment ideas. The analogous approach for ordered graphs remains open for general ordered graphs. arXiv:2307.01652 makes partial progress by proving polynomial bounds for ordered matchings via a regularity-free technique (nested partitions), and arXiv:2110.03577 characterizes the polynomial-bound regime for ordered graphs. Authors of 2110.03577 and 2307.01652 were not fully identified from available abstracts.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It will be interesting to try to obtain a proof for the ordered graph removal lemma that does not go through the strong regularity lemma needed in the current proof.

Context

The proofs of the ordered removal lemmas rely on strong variants of the graph regularity lemma, which impose a wowzer-type (tower-of-towers) dependence between the parameters $\delta^{-1}$ and $\varepsilon^{-1}$. Fox gave the first regularity-free proof of the unordered graph removal lemma, though still with tower-type dependence; an analogous approach for the ordered setting remains open.

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
