Attack the following open graph-theory problem.

Catalog id: 1612.08698__00
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1612.08698__00/
Source paper: List coloring with requests (arXiv:1612.08698)

=== Extracted statement (catalog JSON) ===
Title: Problem 1
Does there for every integer $d \geq 0$ exist $\varepsilon > 0$ such that every $d$-degenerate graph with an assignment of lists of size $d + 1$ is weighted $\varepsilon$-flexible? Or at least $\varepsilon$-flexible?

Context:
Theorem 2 shows that lists of size $d+2$ suffice for weighted $\varepsilon$-flexibility of $d$-degenerate graphs. The question is whether one extra color (size $d+1$, matching choosability) also guarantees flexibility. For $d=0$ trivial; for $d=1$ (forests with lists of size 2) weighted $1/2$-flexibility is easy; the first open case is $d=2$.

=== Catalog page (statement + literature review) ===
ε-flexibility of d-degenerate graphs with (d+1)-lists — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Problem 1 remains open in full generality: no paper has proved epsilon-flexibility for all d-degenerate graphs with (d+1)-lists for every d >= 2. Substantial partial progress exists: the d=2 case has been confirmed for planar graphs of girth >= 6 (lists of size 3) and for all graphs of maximum average degree < 3; the d=3 case has been confirmed for triangle-free planar graphs (lists of size 4); and epsilon-flexibility has been established for graphs of treewidth 2, treedepth k, and bipartite d-degenerate graphs. The general conjecture for arbitrary d-degenerate graphs with (d+1)-lists remains open for d >= 2.

 Cited literature (5)

 
 
 
partial Flexibility of triangle-free planar graphs
 (2019)
 

 
 Zdeněk Dvořák, Tomáš Masařík, Jan Musílek, Ondřej Pangrác · arXiv preprint · arXiv:1902.02971

Proves that triangle-free planar graphs (which are 3-degenerate) with lists of size at least four are weighted epsilon-flexible for some constant epsilon > 0, resolving the conjecture for this class.
 

 
 
partial Flexibility of planar graphs of girth at least six
 (2019)
 

 
 Zdeněk Dvořák, Tomáš Masařík, Jan Musílek, Ondřej Pangrác · arXiv preprint · arXiv:1902.04069

Proves that planar graphs of girth at least six (which are 2-degenerate) with lists of size three are weighted epsilon-flexible, resolving the d=2 case for this subclass.
 

 
 
partial Flexible List Colorings in Graphs with Special Degeneracy Conditions
 (2020)
 

 
 Peter Bradshaw, Tomáš Masařík, Ladislav Stacho · ISAAC 2020 (LIPIcs) · arXiv:2006.15837 · doi:10.4230/LIPIcs.ISAAC.2020.31

Proves epsilon-flexibility for graphs of treewidth 2 (which are (1/3)-flexibly 3-choosable), treedepth k graphs, and characterizes which maximum-degree-Delta graphs are epsilon-flexibly Delta-choosable.
 

 
 
partial Flexible list colorings: Maximizing the number of requests satisfied
 (2022)
 

 
 Hemanshu Kaul, Rogers Mathew, Jeffrey A. Mudrock, Michael J. Pelsmajer · arXiv preprint · arXiv:2211.09048

Extends flexibility results to bipartite d-degenerate graphs and introduces the list flexibility number, without resolving the full conjecture for arbitrary d-degenerate graphs.
 

 
 
partial Flexible list coloring of graphs with maximum average degree less than 3
 (2023)
 

 
 Richard Bi, Peter Bradshaw · arXiv preprint · arXiv:2310.02979

Proves that every graph with maximum average degree less than 3 is epsilon-flexibly 3-choosable, resolving the d=2 case of the conjecture for a broad class of 2-degenerate graphs (including planar graphs of girth >= 6).
 

 

 Reviewer notes. The conjecture splits into two sub-questions (epsilon-flexible vs. weighted epsilon-flexible); partial results address both variants. The d=1 case (forests with 2-lists) was settled in the original paper. For d=2, several major subclasses are now resolved including maximum average degree < 3 (Bi-Bradshaw 2023). For d=3, triangle-free planar graphs are settled. The full conjecture for arbitrary d-degenerate graphs remains open for d >= 2.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Does there for every integer $d \geq 0$ exist $\varepsilon > 0$ such that every $d$-degenerate graph with an assignment of lists of size $d + 1$ is weighted $\varepsilon$-flexible? Or at least $\varepsilon$-flexible?

Context

Theorem 2 shows that lists of size $d+2$ suffice for weighted $\varepsilon$-flexibility of $d$-degenerate graphs. The question is whether one extra color (size $d+1$, matching choosability) also guarantees flexibility. For $d=0$ trivial; for $d=1$ (forests with lists of size 2) weighted $1/2$-flexibility is easy; the first open case is $d=2$.

Notes. PDF source; math is simple enough to read cleanly.

Source paper

 List coloring with requests
 Zdeněk Dvořák, Sergey Norin, Luke Postle · 2018-11-17
 https://arxiv.org/abs/1612.08698
 PDF source

=== Source paper abstract / header ===
Abstract:Let G be a graph with a list assignment L. Suppose a preferred color is given for some of the vertices; how many of these preferences can be respected when L-coloring G? We explore several natural questions arising in this context, and propose directions for further research.
 

 
 
 
 Comments:
 19 pages, 2 figures; revision according to referee suggestions
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:1612.08698 [math.CO]
 

 
  
 (or 
 arXiv:1612.08698v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1612.08698
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Tue, 27 Dec 2016 18:18:49 UTC (13 KB)

 [v2]
 Sat, 17 Nov 2018 00:59:53 UTC (26 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled List coloring with requests, by Zden\v{e}k Dvo\v{r}\'ak and Sergey Norin and Luke Postle
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
 | 2016-12
 

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
