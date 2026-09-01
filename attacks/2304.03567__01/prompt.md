Attack the following open graph-theory problem.

Catalog id: 2304.03567__01
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2304.03567__01/
Source paper: Temporalizing digraphs via linear-size balanced bi-trees (arXiv:2304.03567)

=== Extracted statement (catalog JSON) ===
Title: Problem 2
What is the maximum $c_{b}$ for which every strongly connected directed graph on $n$ vertices has a balanced bi-tree of size at least $c_{b}.n$?

Context:
The paper proves $c_{b}\geq 1/3$ (Theorem 4), where both the out-tree $|T^{+}|$ and in-tree $|T^{-}|$ of the bi-tree each have size at least $n/6$. The exact optimal constant $c_{b}$ is unknown.

=== Catalog page (statement + literature review) ===
Optimal balanced bi-tree size constant — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 2 of arXiv:2304.03567 asks for the maximum constant $c_b$ such that every strongly connected directed graph on $n$ vertices has a balanced bi-tree of size at least $c_b \cdot n$. The source paper establishes $c_b \geq 1/3$ (Theorem 4), with both the out-tree and in-tree of size at least $n/6$ each. No subsequent work improving this bound or determining the exact value of $c_b$ was found in a thorough web search.

 Reviewer notes. No follow-up work found after 5 web calls. The conjecture was published at STACS 2024 and remains open. The internal references supplied (arXiv:2206.12335, twice) are false matches from the fuzzy-matching pipeline — they concern 1-independent percolation on Z^n and have no connection to this problem.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the maximum $c_{b}$ for which every strongly connected directed graph on $n$ vertices has a balanced bi-tree of size at least $c_{b}.n$?

Context

The paper proves $c_{b}\geq 1/3$ (Theorem 4), where both the out-tree $|T^{+}|$ and in-tree $|T^{-}|$ of the bi-tree each have size at least $n/6$. The exact optimal constant $c_{b}$ is unknown.

Source paper

 Temporalizing digraphs via linear-size balanced bi-trees
 Stéphane Bessy, Stéphan Thomassé, Laurent Viennot · 2024-01-11
 https://arxiv.org/abs/2304.03567

=== Source paper abstract / header ===
Abstract:In a directed graph $D$ on vertex set $v_1,\dots ,v_n$, a \emph{forward arc} is an arc $v_iv_j$ where $i<j$. A pair $v_i,v_j$ is \emph{forward connected} if there is a directed path from $v_i$ to $v_j$ consisting of forward arcs. In the {\tt Forward Connected Pairs Problem} ({\tt FCPP}), the input is a strongly connected digraph $D$, and the output is the maximum number of forward connected pairs in some vertex enumeration of $D$. We show that {\tt FCPP} is in APX, as one can efficiently enumerate the vertices of $D$ in order to achieve a quadratic number of forward connected pairs. For this, we construct a linear size balanced bi-tree $T$ (an out-tree and an in-tree with same size which roots are identified). The existence of such a $T$ was left as an open problem motivated by the study of temporal paths in temporal networks. More precisely, $T$ can be constructed in quadratic time (in the number of vertices) and has size at least $n/3$. The algorithm involves a particular depth-first search tree (Left-DFS) of independent interest, and shows that every strongly connected directed graph has a balanced separator which is a circuit. Remarkably, in the request version {\tt RFCPP} of {\tt FCPP}, where the input is a strong digraph $D$ and a set of requests $R$ consisting of pairs $\{x_i,y_i\}$, there is no constant $c>0$ such that one can always find an enumeration realizing $c.|R|$ forward connected pairs $\{x_i,y_i\}$ (in either direction).
 

 
 
 
 Comments:
 11 pages, 2 figure
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS)
 
 
 MSC classes:
 05C20, 05C85, 68R10
 

 
 ACM classes:
 F.2.2; G.2.2
 

 Cite as:
 arXiv:2304.03567 [math.CO]
 

 
  
 (or 
 arXiv:2304.03567v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2304.03567
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Stéphane Bessy [view email] 
 [v1]
 Fri, 7 Apr 2023 10:02:30 UTC (361 KB)

 [v2]
 Thu, 11 Jan 2024 09:30:34 UTC (48 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Temporalizing digraphs via linear-size balanced bi-trees, by St\'ephane Bessy and 1 other authors
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
 | 2023-04
 

 Change to browse by:
 
 cs
 cs.DM
 cs.DS
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
