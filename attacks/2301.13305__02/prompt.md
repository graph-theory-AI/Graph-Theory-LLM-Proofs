Attack the following open graph-theory problem.

Catalog id: 2301.13305__02
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2301.13305__02/
Source paper: Graph-codes (arXiv:2301.13305)

=== Extracted statement (catalog JSON) ===
Title: Open problem: tighter bounds for linear graph-codes
Establish tighter bounds for the maximum possible cardinality of a linear family of graphs on $[n]$ in which no symmetric difference is a copy of a fixed graph $H$ with an even number of edges.

Context:
The paper notes that for any fixed graph $H$ with an even number of edges the maximum size of a linear $H$-code is $o\bigl(2^{\binom{n}{2}}\bigr)$, but the proof via Ramsey's Theorem yields very weak quantitative bounds. Theorem 1.6 gives a tight result for the family $\mathcal{K}$ of all cliques as a model for what such tight results could look like.

=== Catalog page (statement + literature review) ===
Linear graph-code cardinality bounds for even H — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Versteegen (2023, arXiv:2310.19891) made significant progress on this problem: for any fixed graph H with an even number of edges, the maximum size of a linear H-code is O(2^{\binom{n}{2}} / \log n), and for almost all such H there exists \varepsilon_H > 0 giving the stronger bound 2^{\binom{n}{2}/n^{\varepsilon_H}}. These are substantially tighter than the original Ramsey-based bounds from the source paper. However, tight bounds matching a lower construction are not yet established in general, so the full problem remains open.

 Cited literature (1)

 
 
 
partial Upper bounds for linear graph codes
 (2023)
 

 
 Leo Versteegen · Random Structures & Algorithms · arXiv:2310.19891 · doi:10.1002/rsa.21263

Proves that for any fixed graph H with an even number of edges the maximum size of a linear H-code is O(2^{\binom{n}{2}}/\log n), and for almost all such H obtains the stronger polynomial-suppression bound 2^{\binom{n}{2}/n^{\varepsilon_H}}, directly addressing the open problem from Alon (2301.13305).
 

 

 Reviewer notes. The open problem asks for tight (matching upper and lower) bounds; Versteegen's paper gives substantially improved upper bounds but full tightness for general H is still open. The published version appeared in Random Structures & Algorithms (2025).

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Establish tighter bounds for the maximum possible cardinality of a linear family of graphs on $[n]$ in which no symmetric difference is a copy of a fixed graph $H$ with an even number of edges.

Context

The paper notes that for any fixed graph $H$ with an even number of edges the maximum size of a linear $H$-code is $o\bigl(2^{\binom{n}{2}}\bigr)$, but the proof via Ramsey's Theorem yields very weak quantitative bounds. Theorem 1.6 gives a tight result for the family $\mathcal{K}$ of all cliques as a model for what such tight results could look like.

Source paper

 Graph-codes
 Noga Alon · 2023-02-06
 https://arxiv.org/abs/2301.13305
 PDF source

=== Source paper abstract / header ===
Abstract:The symmetric difference of two graphs $G_1,G_2$ on the same set of vertices $[n]=\{1,2, \ldots ,n\}$ is the graph on $[n]$ whose set of edges are all edges that belong to exactly one of the two graphs $G_1,G_2$. Let $H$ be a fixed graph with an even (positive) number of edges, and let $D_H(n)$ denote the maximum possible cardinality of a family of graphs on $[n]$ containing no two members whose symmetric difference is a copy of $H$. Is it true that $D_H(n)=o(2^{n \choose 2})$ for any such $H$? We discuss this problem, compute the value of $D_H(n)$ up to a constant factor for stars and matchings, and discuss several variants of the problem including ones that have been considered in earlier work.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05D05, 94B25
 

 Cite as:
 arXiv:2301.13305 [math.CO]
 

 
  
 (or 
 arXiv:2301.13305v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2301.13305
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Noga Alon [view email] 
 [v1]
 Mon, 30 Jan 2023 21:54:31 UTC (9 KB)

 [v2]
 Mon, 6 Feb 2023 17:19:26 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Graph-codes, by Noga Alon
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
 | 2023-01
 

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
