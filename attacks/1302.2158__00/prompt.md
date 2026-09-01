Attack the following open graph-theory problem.

Catalog id: 1302.2158__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1302.2158__00/
Source paper: Three-coloring triangle-free graphs on surfaces II. 4-critical graphs i… (arXiv:1302.2158)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.7
For every integer $k \geq 5$, there exists an integer $K$ with the following property. Let $G$ be a planar graph of girth at least five, let $C_1, C_2$ be two cycles in $G$ of lengths at most $k$, and for every $v \in V(G)$ let $L(v)$ be a set such that $|L(v)| = 1$ if $v \in V(C_1 \cup C_2)$ and $|L(v)| \geq 3$ otherwise. If there exists no proper coloring $\phi$ of $G$ such that $\phi(v) \in L(v)$ for every $v \in V(G)$, then $G$ has a subgraph $H$ on at most $K$ vertices such that $C_1$ and $C_2$ are subgraphs of $H$ and there exists no proper coloring $\psi$ of $H$ such that $\psi(v) \in L(v)$ for every $v \in V(H)$.

Context:
The conjecture is a list-coloring generalisation of the paper's main result (Theorem 1.6). The authors note that an affirmative answer would imply an analogue of Theorem 1.4 for graphs of girth at least five in the list-coloring setting, and that Luke Postle (private communication) believes he has a proof, though it had not yet been written down at the time of submission.

=== Catalog page (statement + literature review) ===
List-coloring bounded obstruction for girth-5 planar graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No paper was found that directly and verifiably proves Conjecture 1.7 from arXiv:1302.2158. Postle's arXiv:1710.06898 (2017) proves a linear isoperimetric bound for 3-list-coloring of graphs of girth at least five on surfaces and finiteness of 4-list-critical graphs of girth at least five on any fixed surface; this machinery is closely related and may imply the conjecture as a corollary for planar graphs, but the direct connection was not confirmed. The three internal references appear to address different conjectures from adjacent papers rather than Conjecture 1.7 specifically.

 Cited literature (1)

 
 
 
partial 3 List Coloring Graphs of Girth at least Five on Surfaces
 (2017)
 

 
 Luke Postle · Journal of Combinatorial Theory, Series B · arXiv:1710.06898

Proves a linear isoperimetric bound for 3-list-coloring of girth-at-least-five graphs on surfaces and finiteness of 4-list-critical graphs of girth at least five on any fixed surface, machinery that may imply the bounded-obstruction conclusion of Conjecture 1.7 as a special case for planar graphs; the explicit connection to Conjecture 1.7 was not verified.
 

 

 Reviewer notes. The source paper notes that Luke Postle (private communication) believed he had a proof at the time of submission. Postle's subsequent arXiv:1710.06898 proves a linear isoperimetric bound for 3-list-coloring of girth-at-least-five graphs, and the published JCTB version appears in ScienceDirect (doi lookup not performed). The conjecture is closely related to the bounded-obstruction / hyperbolic-family framework developed by Postle and Thomas; however, Conjecture 1.7 specifically concerns planar graphs with two precolored cycles of bounded length and 3-element lists elsewhere, and no paper was found that cites or proves it by name within the 5-call budget.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every integer $k \geq 5$, there exists an integer $K$ with the following property. Let $G$ be a planar graph of girth at least five, let $C_1, C_2$ be two cycles in $G$ of lengths at most $k$, and for every $v \in V(G)$ let $L(v)$ be a set such that $|L(v)| = 1$ if $v \in V(C_1 \cup C_2)$ and $|L(v)| \geq 3$ otherwise. If there exists no proper coloring $\phi$ of $G$ such that $\phi(v) \in L(v)$ for every $v \in V(G)$, then $G$ has a subgraph $H$ on at most $K$ vertices such that $C_1$ and $C_2$ are subgraphs of $H$ and there exists no proper coloring $\psi$ of $H$ such that $\psi(v) \in L(v)$ for every $v \in V(H)$.

Context

The conjecture is a list-coloring generalisation of the paper's main result (Theorem 1.6). The authors note that an affirmative answer would imply an analogue of Theorem 1.4 for graphs of girth at least five in the list-coloring setting, and that Luke Postle (private communication) believes he has a proof, though it had not yet been written down at the time of submission.

Notes. The PDF extraction renders the final clause with $\phi$ instead of $\psi$; from context the intended quantifier variable in the conclusion is $\psi$, corrected here.

Source paper

 Three-coloring triangle-free graphs on surfaces II. 4-critical graphs in a disk
 Zdenek Dvorak, Daniel Kral, Robin Thomas · 2017-07-05
 https://arxiv.org/abs/1302.2158
 PDF source

=== Source paper abstract / header ===
Abstract:Let G be a plane graph of girth at least five. We show that if there exists a 3-coloring phi of a cycle C of G that does not extend to a 3-coloring of G, then G has a subgraph H on O(|C|) vertices that also has no 3-coloring extending phi. This is asymptotically best possible and improves a previous bound of Thomassen. In the next paper of the series we will use this result and the attendant theory to prove a generalization to graphs on surfaces with several precolored cycles.
 

 
 
 
 Comments:
 48 pages, 4 figures This version: Revised according to reviewer comments
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C15 (Primary), 05C10 (Secondary)
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:1302.2158 [math.CO]
 

 
  
 (or 
 arXiv:1302.2158v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1302.2158
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Fri, 8 Feb 2013 21:25:22 UTC (67 KB)

 [v2]
 Sat, 25 May 2013 15:28:37 UTC (67 KB)

 [v3]
 Wed, 6 Jan 2016 15:13:42 UTC (67 KB)

 [v4]
 Wed, 5 Jul 2017 19:12:14 UTC (152 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Three-coloring triangle-free graphs on surfaces II. 4-critical graphs in a disk, by Zdenek Dvorak and Daniel Kral and Robin Thomas
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
 | 2013-02
 

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
