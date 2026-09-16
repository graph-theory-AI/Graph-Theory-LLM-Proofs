Attack the following open graph-theory problem.

Catalog id: 1608.03040__00
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1608.03040__00/
Source paper: Majority Colourings of Digraphs (arXiv:1608.03040)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2
Every digraph has a majority 3-colouring.

Context:
This conjecture naturally arises from Theorem 1, which shows every digraph has a majority 4-colouring. It would be best possible: odd directed cycles require 3 colours (since each vertex has outdegree 1, a majority colouring is a proper colouring), and circulant digraphs with large odd outdegree also witness this lower bound.

=== Catalog page (statement + literature review) ===
Majority 3-coloring of digraphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture that every digraph has a majority 3-colouring remains open in full generality as of 2026. Anastos, Lamaison, Steiner, and Szabó (arXiv:1911.01954, EJC 2021) proved it for digraphs with chromatic number at most 6 or dichromatic number at most 3 (covering all planar digraphs), and proved the stronger majority 3-choosability for digraphs with maximum out-degree at most 4 or maximum degree at most 7. Their probabilistic argument achieves a fractional bound of K ≤ 3.9602, approaching but not reaching the conjectured value of 3. A 2025 paper in Acta Mathematicae Applicatae Sinica reports further new partial results, and the conjecture is still described as 'far from being resolved' in recent literature.

 Cited literature (1)

 
 
 
partial Majority Colorings of Sparse Digraphs
 (2021)
 

 
 Michael Anastos, Ander Lamaison, Raphael Steiner, Tibor Szabó · Electronic Journal of Combinatorics · arXiv:1911.01954

Proves the conjecture for digraphs with chromatic number at most 6 or dichromatic number at most 3, and proves the stronger majority 3-choosability for digraphs with maximum out-degree at most 4 or maximum degree at most 7; also establishes a fractional majority coloring bound of K ≤ 3.9602.
 

 

 Reviewer notes. Conjecture confirmed open as of 2025 by multiple sources. Additional unverified leads found within cap: Haselgrave (2020) 'Countable graphs are majority 3-choosable' (Warwick eprint 144155, PDF timed out); Acta Mathematicae Applicatae Sinica 2025 paper (doi:10.1007/s10255-025-0002-0) reporting new partial results (Springer auth-wall, not fetched); an IJMTT paper showing every digraph D with minimum out-degree ≥ 28·ln|D| has a majority 3-colouring (arxiv ID not found). These could not be verified within the 5-call cap.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Every digraph has a majority 3-colouring.

Context

This conjecture naturally arises from Theorem 1, which shows every digraph has a majority 4-colouring. It would be best possible: odd directed cycles require 3 colours (since each vertex has outdegree 1, a majority colouring is a proper colouring), and circulant digraphs with large odd outdegree also witness this lower bound.

Source paper

 Majority Colourings of Digraphs
 Stephan Kreutzer, Sang-il Oum, Paul Seymour, Dominic van der Zypen, David R. Wood · 2016-08-10
 https://arxiv.org/abs/1608.03040
 PDF source

Related conjectures

 
 implied by
 Majority 1/k out-neighbour colouring digraphs
 disproved
 The source is universally quantified over k >= 2. Instantiating k = 2 gives: every digraph has a 3-colouring in which each vertex v has at most (1/2)deg+(v) out-neighbours of its own colour — verbatim the definition of a majority 3-colouring. So the general 1/k conjecture implies the majority 3-colouring conjecture as its k = 2 case; the paper itself presents the source as the natural generalisation of the target. That the general conjecture was later disproved for some k does not affect the validity of the implication. Direction correct: the general-k statement is stronger.
 

 
 implies
 Majority 3-coloring of Eulerian digraphs
 open
 Eulerian digraphs are a subclass of digraphs, so the universal majority 3-colouring conjecture instantiates to them. The only subtlety is whether the Eulerian problem asks the genuine majority condition (at most (1/2)deg+(v) same-coloured out-neighbours) rather than the weaker (2/3)deg in-or-out variant already proved; the target statement and its context explicitly say the open question is the full majority 3-colouring with (1/2)deg+(v), matching the source's definition exactly. Direction correct.
 

 
 implies
 Majority 3-coloring of tournaments
 open
 Tournaments are a subclass of digraphs, and both statements use the identical definition of majority 3-colouring (each vertex has at most half of its out-neighbours in its own colour) from the same paper. Truth of the universal statement for all digraphs instantiates directly to every tournament, so the source implies the target. Direction is correct: the all-digraphs conjecture is the stronger statement.
 

 
 implies
 Sublinear majority 3-coloring of digraphs
 solved
 A majority 3-colouring is by definition a 3-colouring in which every vertex v has at most (1/2)deg+(v) out-neighbours of its own colour. Hence if every digraph has a majority 3-colouring (source), then beta = 1/2 < 1 witnesses an affirmative answer to the target question. Parameter monotonicity is trivial (1/2 < 1) and the same colouring object is used, so the implication is immediate. The converse does not follow (some beta in (1/2, 1) could work while beta = 1/2 fails), so 'implies' rather than 'equivalent_to' is the right relation, and the claimed direction (source stronger) is correct.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:We prove that every digraph has a vertex 4-colouring such that for each vertex $v$, at most half the out-neighbours of $v$ receive the same colour as $v$. We then obtain several results related to the conjecture obtained by replacing 4 by 3.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1608.03040 [math.CO]
 

 
  
 (or 
 arXiv:1608.03040v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1608.03040
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Electronic J. Combinatorics 24:2.25, 2017
 

 
 
 Related DOI:
 
 https://doi.org/10.37236/6410

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: David Wood [view email] 
 [v1]
 Wed, 10 Aug 2016 04:29:08 UTC (43 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Majority Colourings of Digraphs, by Stephan Kreutzer and Sang-il Oum and Paul Seymour and Dominic van der Zypen and David R. Wood
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
 | 2016-08
 

 Change to browse by:
 
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 
 
 1 blog link
 (what is this?)
 

 

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
