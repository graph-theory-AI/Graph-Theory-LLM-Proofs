Attack the following open graph-theory problem.

Catalog id: 2301.13305__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2301.13305__00/
Source paper: Graph-codes (arXiv:2301.13305)

=== Extracted statement (catalog JSON) ===
Title: Question 1.1
Let $\mathcal{H}$ be a family of graphs closed under isomorphism. Is it true that $d_{\mathcal{H}}(n)$ tends to $0$ as $n$ tends to infinity if and only if $\mathcal{H}$ contains a graph with an even number of edges? Equivalently: is it true that for any fixed graph $H$ with an even number of edges, $d_H(n)$ tends to $0$ as $n$ tends to infinity?

Context:
The authors define $d_H(n)$ as the maximum fraction of all graphs on $[n]$ forming an $H$-code (a family with no two members whose symmetric difference is a copy of $H$). If every member of $\mathcal{H}$ has an odd number of edges then $d_{\mathcal{H}}(n) \geq 1/2$, motivating the question of whether containing an even-edge graph is exactly the condition that forces $d_{\mathcal{H}}(n) \to 0$. The question is stated as the central open problem and noted in the concluding remarks to remain wide open.

=== Catalog page (statement + literature review) ===
Even-edge graphs and H-code density — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The full Question 1.1 — whether $d_H(n)\to 0$ for every fixed graph $H$ with an even number of edges — remains open for general H-codes. Versteegen (arXiv:2310.19891, 2023) proved the analogous statement for the linear variant: if $H$ has an even number of edges then the density of a linear graph code avoiding $H$ is $O(2^{\binom{n}{2}}/\log n)$, and for almost all such $H$ it is at most $2^{\binom{n}{2}/n^{\varepsilon_H}}$ for some $\varepsilon_H>0$. This constitutes partial progress on Alon's question but does not settle it for non-linear codes.

 Cited literature (1)

 
 
 
partial Upper bounds for linear graph codes
 (2023)
 

 
 Leo Versteegen · Random Structures & Algorithms · arXiv:2310.19891

Proves that linear H-codes with H having an even number of edges have density O(1/log n), and for almost all such H an exponentially smaller density bound; explicitly described as progress on Alon's question.
 

 

 Reviewer notes. Versteegen's partial result is for the linear subproblem (codes closed under symmetric difference); it does not imply the general case since linear codes form a strict subset of all H-codes. The paper was published in Random Structures & Algorithms (Wiley) in 2025. The pre-existing 'Structured Codes of Graphs' by Alon and Gujgiczer (arXiv:2202.06810, SIAM J. Discrete Math. 2023) predates the graph-codes paper and is not a follow-up. The full non-linear question appears to remain open as of May 2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Let $\mathcal{H}$ be a family of graphs closed under isomorphism. Is it true that $d_{\mathcal{H}}(n)$ tends to $0$ as $n$ tends to infinity if and only if $\mathcal{H}$ contains a graph with an even number of edges? Equivalently: is it true that for any fixed graph $H$ with an even number of edges, $d_H(n)$ tends to $0$ as $n$ tends to infinity?

Context

The authors define $d_H(n)$ as the maximum fraction of all graphs on $[n]$ forming an $H$-code (a family with no two members whose symmetric difference is a copy of $H$). If every member of $\mathcal{H}$ has an odd number of edges then $d_{\mathcal{H}}(n) \geq 1/2$, motivating the question of whether containing an even-edge graph is exactly the condition that forces $d_{\mathcal{H}}(n) \to 0$. The question is stated as the central open problem and noted in the concluding remarks to remain wide open.

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
