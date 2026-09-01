Attack the following open graph-theory problem.

Catalog id: 1802.03727__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1802.03727__00/
Source paper: Separation choosability and dense bipartite induced subgraphs (arXiv:1802.03727)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.3
There is a function $x_1(d)$ that satisfies $x_1(d) \to \infty$ as $d \to \infty$ such that $\mathrm{ch}_{\mathrm{sep}}(G) \geq x_1(d)$ for any graph $G$ with minimum degree $d$.

Context:
The authors prove Theorem 1.2 that separation choosability grows logarithmically in minimum degree for bipartite graphs, and ask whether the bipartiteness assumption can be dropped. The difficulty is that a bad list assignment with maximum separation on a graph does not necessarily retain maximum separation when edges are added, so the standard bipartite-subgraph reduction used for ordinary choosability fails.

=== Catalog page (statement + literature review) ===
Separation choosability grows with minimum degree — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 1.3 from arXiv:1802.03727 asks whether separation choosability ch_sep(G) tends to infinity with the minimum degree d for general graphs, dropping the bipartite assumption of Theorem 1.2. No follow-up paper proving or disproving this conjecture for general graphs was found in the indexed literature through 2026. The related 2025 preprint arXiv:2509.13913 on separation choosability does not address this conjecture, focusing instead on comparisons among coloring parameters for sparse graph families. The conjecture has been open since 2018 and remains unresolved.

 Reviewer notes. Theorem 1.2 of the source paper proves ch_sep(G) = Ω(log d / log log d) for bipartite G with minimum degree d; Conjecture 1.3 asks for the same unbounded growth for all graphs. The difficulty noted by the authors is that a bad list assignment with maximum separation does not retain maximum separation when edges are added, so the standard bipartite-reduction argument for ordinary choosability fails. A related Ramsey-type question (does every triangle-free graph of min-degree d contain a bipartite induced subgraph of min-degree Ω(log d)?) was studied by Kwan et al. (arXiv:1810.12144, Combinatorica 2020) but this does not directly resolve Conjecture 1.3. No post-2018 paper resolving the conjecture for general graphs was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There is a function $x_1(d)$ that satisfies $x_1(d) \to \infty$ as $d \to \infty$ such that $\mathrm{ch}_{\mathrm{sep}}(G) \geq x_1(d)$ for any graph $G$ with minimum degree $d$.

Context

The authors prove Theorem 1.2 that separation choosability grows logarithmically in minimum degree for bipartite graphs, and ask whether the bipartiteness assumption can be dropped. The difficulty is that a bad list assignment with maximum separation on a graph does not necessarily retain maximum separation when edges are added, so the standard bipartite-subgraph reduction used for ordinary choosability fails.

Notes. PDF source — math appears cleanly extracted for this statement.

Source paper

 Separation choosability and dense bipartite induced subgraphs
 Louis Esperet, Ross J. Kang, Stéphan Thomassé · 2018-12-04
 https://arxiv.org/abs/1802.03727
 PDF source

=== Source paper abstract / header ===
Abstract:We study a restricted form of list colouring, for which every pair of lists that correspond to adjacent vertices may not share more than one colour. The optimal list size such that a proper list colouring is always possible given this restriction, we call separation choosability. We show for bipartite graphs that separation choosability increases with (the logarithm of) the minimum degree. This strengthens results of Molloy and Thron and, partially, of Alon. One attempt to drop the bipartiteness assumption precipitates a natural class of Ramsey-type questions, of independent interest. For example, does every triangle-free graph of minimum degree $d$ contain a bipartite induced subgraph of minimum degree $\Omega(\log d)$ as $d\to\infty$?
 

 
 
 
 Comments:
 18 pages; v2 accepted to Combinatorics, Probability & Computing
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C15, 05C35
 

 Cite as:
 arXiv:1802.03727 [math.CO]
 

 
  
 (or 
 arXiv:1802.03727v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1802.03727
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Combinator. Probab. Comp. 28 (2019) 720-732
 

 
 
 Related DOI:
 
 https://doi.org/10.1017/S0963548319000026

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Ross J. Kang [view email] 
 [v1]
 Sun, 11 Feb 2018 12:04:09 UTC (16 KB)

 [v2]
 Tue, 4 Dec 2018 19:42:49 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Separation choosability and dense bipartite induced subgraphs, by Louis Esperet and 2 other authors
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
 | 2018-02
 

 Change to browse by:
 
 cs
 cs.DM
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
