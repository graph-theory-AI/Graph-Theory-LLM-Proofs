Attack the following open graph-theory problem.

Catalog id: 2004.07214__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.07214__00/
Source paper: Enumerating minimal dominating sets in the (in)comparability graphs of … (arXiv:2004.07214)

=== Catalog page (statement + literature review) ===
Dom-Enum polynomial in Sₜ-free incomparability graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 7.1 from arXiv:2004.07214 asks for an output-polynomial time algorithm for Dom-Enum in incomparability graphs of $S_t$-free posets, as the natural counterpart to the paper's Corollary 5.3 (which covers comparability graphs of $S_t$-free posets) and Theorem 1.1 (incomparability graphs of bounded-dimension posets). The paper, originally posted in April 2020 and published in Discrete Mathematics in 2025, leaves this as an open problem. No follow-up paper resolving the conjecture was found in the indexed literature; a related 2025 WADS paper (chordal bipartite graphs) cites the source paper but addresses a different graph class.

 Reviewer notes. The conjecture has been open since April 2020. The paper proves the comparability-graph analogue (Corollary 5.3) and the bounded-dimension case for incomparability graphs (Theorem 1.1), but the S_t-free incomparability case resists the same techniques because comparability graphs of S_t-free posets are not of bounded LMIM-width. A WADS 2025 paper on chordal bipartite graphs cites arXiv:2004.07214 but does not address this conjecture. Confidence is medium rather than high because the arXiv preprint is from 2020 (~6 years old), making the absence of a resolution somewhat surprising.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every $t$, there is an output-polynomial time algorithm for Dom-Enum in incomparability graphs of $S_{t}$-free posets.

Context

The algorithm of Corollary 5.3 already covers all comparability graphs of $S_{t}$-free posets. The paper asks what can be said about Dom-Enum in $H$-free incomparability graphs; since co-bipartite graphs are incomparability graphs, the question is only interesting for co-bipartite $H$. This conjecture is proposed as the natural counterpart of Theorem 1.2 for the $S_t$-free setting.

Also stated in

 
Enumerating minimal dominating sets in the (in)comparability graphs of bounded dimension posets (2025-11-26) 

Source paper

 Enumerating minimal dominating sets in the (in)comparability graphs of bounded dimension posets
 Marthe Bonamy, Oscar Defrain, Piotr Micek, Lhouari Nourine · 2025-11-26
 https://arxiv.org/abs/2004.07214

=== Source paper abstract / header ===
Abstract:Enumerating minimal transversals in a hypergraph is a notoriously hard problem. It can be reduced to enumerating minimal dominating sets in a graph, in fact even to enumerating minimal dominating sets in an incomparability graph. We provide an output-polynomial time algorithm for incomparability graphs whose underlying posets have bounded dimension. Through a different proof technique, we also provide an output-polynomial algorithm for their complements, i.e., for comparability graphs of bounded dimension posets.
Our algorithm for incomparability graphs is based on flashlight search and relies on the geometrical representation of incomparability graphs with bounded dimension, as given by Golumbic et al. in 1983. It runs with polynomial delay and only needs polynomial space. Our algorithm for comparability graphs is based on the flipping method introduced by Golovach et al. in 2015. It performs in incremental-polynomial time and requires exponential space.
In addition, we show how to improve the flipping method so that it requires only polynomial space. Since the flipping method is a key tool for the best known algorithms enumerating minimal dominating sets in a number of graph classes, this yields direct improvements on the state of the art.
 

 
 
 
 Comments:
 23 pages, 5 figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2004.07214 [cs.DM]
 

 
  
 (or 
 arXiv:2004.07214v2 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2004.07214
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Oscar Defrain [view email] 
 [v1]
 Wed, 15 Apr 2020 17:15:46 UTC (175 KB)

 [v2]
 Wed, 26 Nov 2025 10:58:30 UTC (180 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Enumerating minimal dominating sets in the (in)comparability graphs of bounded dimension posets, by Marthe Bonamy and 3 other authors
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
 | 2020-04
 

 Change to browse by:
 
 cs
 cs.DS
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Marthe Bonamy
Oscar Defrain
Piotr Micek
Lhouari Nourine 

 

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
