Attack the following open graph-theory problem.

Catalog id: 2004.07214__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.07214__01/
Source paper: Enumerating minimal dominating sets in the (in)comparability graphs of … (arXiv:2004.07214)

=== Catalog page (statement + literature review) ===
Dom-Enum in co-bipartite H-free incomparability graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No paper resolving Conjecture 7.3 was found. The closest related follow-up is a 2025 WADS paper (arXiv:2502.14611, Castelo–Defrain–Gomes) giving polynomial-delay algorithms for minimal dominating sets in chordal bipartite graphs, which cites 2004.07214 but does not address the co-bipartite H-free incomparability setting of Conjecture 7.3. The broader problem of Dom-Enum in H-free incomparability graphs for co-bipartite H remains open, with the conjecture having been present in the arXiv preprint since April 2020.

 Reviewer notes. Confidence is medium rather than high because the arXiv preprint has been available since April 2020 (over five years), making the absence of follow-up more notable. A related WADS 2025 paper (arXiv:2502.14611, Castelo–Defrain–Gomes) proves polynomial delay for chordal bipartite graphs and cites the source paper, but does not address Conjecture 7.3. The conjecture is the broadest of three open problems in the concluding section, subsuming Conjecture 7.2, and the paper notes that the incomparability condition may not even be necessary. Source paper published in Discrete Mathematics (ScienceDirect, November 2025, doi link found at sciencedirect.com/science/article/abs/pii/S0012365X25005126).

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any co-bipartite $H$, there is an output-polynomial time algorithm for Dom-Enum in $H$-free incomparability graphs.

Context

This is the broadest of the three conjectures in the concluding section, subsuming Conjecture 7.2. The authors note there is no blatant reason why the incomparability condition should be necessary, leaving open whether the result might hold for all $H$-free graphs with co-bipartite $H$.

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
