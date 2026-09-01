Attack the following open graph-theory problem.

Catalog id: 2301.13305__04
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2301.13305__04/
Source paper: Graph-codes (arXiv:2301.13305)

=== Extracted statement (catalog JSON) ===
Title: Open problem: minimum edge-coloring with odd intersection property
Determine or estimate the smallest number of colors in an edge coloring of $K_n$ in which every copy of a given graph $H$ (or every copy of any member of a prescribed family $\mathcal{H}$ of graphs) intersects at least one color class by an odd number of edges.

Context:
The authors propose this in the concluding remarks as a natural variant of classical Ramsey Theory questions arising from the coloring method used throughout the paper to produce lower bounds on independence numbers of Cayley graphs.

=== Catalog page (statement + literature review) ===
Odd-intersection edge coloring of Kₙ — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Bennett, Heath, and Zerbib (arXiv:2307.01314, July 2023) directly study the quantity g(G,H) — the minimum number of colors to edge-color G so that every copy of H has an odd color class — introduced as a tool for bounding graph-codes. They establish g(K_n, K_5) ≤ n^{o(1)} and g(K_{n,n}, C_4) = n/2 + o(n), providing the first non-trivial estimates for specific choices of H. The general problem for arbitrary H remains open, and subsequent 2025 papers continue developing the odd-Ramsey framework.

 Cited literature (1)

 
 
 
partial Edge-coloring a graph $G$ so that every copy of a graph $H$ has an odd color class
 (2023)
 

 
 Patrick Bennett, Emily Heath, Shira Zerbib · arXiv preprint · arXiv:2307.01314

Defines g(G,H) as the minimum number of colors to edge-color G so every copy of H has an odd color class, and proves g(K_n, K_5) ≤ n^{o(1)} and g(K_{n,n}, C_4) = n/2 + o(n), giving the first estimates for specific graphs H.
 

 

 Reviewer notes. The follow-up paper arXiv:2307.01314 formalises the open problem under the name g(G,H) and solves it for G=K_n with H=K_5 and G=K_{n,n} with H=C_4, but the general problem for arbitrary H in K_n is still open. Search results also surfaced several 2025 papers on odd Ramsey numbers (arXiv:2507.19456, arXiv:2511.10497, arXiv:2605.07322) that extend this line of work further, but those were not individually verified via WebFetch within the 5-call cap.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine or estimate the smallest number of colors in an edge coloring of $K_n$ in which every copy of a given graph $H$ (or every copy of any member of a prescribed family $\mathcal{H}$ of graphs) intersects at least one color class by an odd number of edges.

Context

The authors propose this in the concluding remarks as a natural variant of classical Ramsey Theory questions arising from the coloring method used throughout the paper to produce lower bounds on independence numbers of Cayley graphs.

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
