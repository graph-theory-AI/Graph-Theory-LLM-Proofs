Attack the following open graph-theory problem.

Catalog id: 1604.02317__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1604.02317__00/
Source paper: Disjoint paths in unions of tournaments (arXiv:1604.02317)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture (vertex-disjoint paths, stability number two)
We suspect the $k$ vertex-disjoint paths problem might be NP-complete for digraphs with stability number two.

Context:
The authors discuss whether their polynomial-time result for semicomplete digraphs (Theorem 1.2) can be extended to digraphs with bounded stability number. The edge-disjoint version is known to be polynomial-time solvable in this setting, but the vertex-disjoint version remains out of reach. The authors remark that they suspect NP-completeness already at stability number two.

=== Catalog page (statement + literature review) ===
NP-completeness of vertex-disjoint paths, stability two — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No paper resolving the conjecture has been found in five web searches. The source paper proves a polynomial-time algorithm for fixed k in semicomplete digraphs (stability number 1) and for digraphs partitioned into a bounded number of semicomplete parts, but leaves the fixed-k, stability-number-two case open with a suspicion of NP-completeness. A 2025 ICALP paper (Gomes, Lopes, Sau) revisits directed disjoint paths on tournaments and corrects a historical NP-completeness proof for unbounded k, but does not address the fixed-k question at stability number two.

 Reviewer notes. The conjecture is stated informally in arXiv:1604.02317 (published 2018-12-23). The ICALP 2025 paper 'Revisiting Directed Disjoint Paths on Tournaments (And Relatives)' by Gomes, Lopes, and Sau (https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.90) corrects a 1992 NP-completeness proof for the unbounded-k case on tournaments and provides new FPT algorithms with vertex congestion, but does not resolve the fixed-k stability-number-two conjecture. No follow-up settling the conjecture was found after 5 web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We suspect the $k$ vertex-disjoint paths problem might be NP-complete for digraphs with stability number two.

Context

The authors discuss whether their polynomial-time result for semicomplete digraphs (Theorem 1.2) can be extended to digraphs with bounded stability number. The edge-disjoint version is known to be polynomial-time solvable in this setting, but the vertex-disjoint version remains out of reach. The authors remark that they suspect NP-completeness already at stability number two.

Notes. Stated as 'we suspect' in running prose with no labelled theorem environment. The full paper text appears truncated after Section 3; additional conjectures or open problems in later sections may have been missed.

Source paper

 Disjoint paths in unions of tournaments
 Maria Chudnovsky, Alex Scott, Paul Seymour · 2018-12-23
 https://arxiv.org/abs/1604.02317
 PDF source

=== Source paper abstract / header ===
Abstract:Given $k$ pairs of vertices $(s_i,t_i)\;(1\le i\le k)$ of a digraph $G$, how can we test whether there exist vertex-disjoint directed paths from $s_i$ to $t_i$ for $1\le i\le k$? This is NP-complete in general digraphs, even for $k = 2$, but in an earlier paper we proved that for all fixed $k$, there is a polynomial-time algorithm to solve the problem if $G$ is a tournament (or more generally, a semicomplete digraph). Here we prove that for all fixed $k$ there is a polynomial-time algorithm to solve the problem when $V(G)$ is partitioned into a bounded number of sets each inducing a semicomplete digraph (and we are given the partition).
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1604.02317 [math.CO]
 

 
  
 (or 
 arXiv:1604.02317v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1604.02317
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Fri, 8 Apr 2016 11:55:23 UTC (17 KB)

 [v2]
 Sun, 23 Dec 2018 18:10:46 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Disjoint paths in unions of tournaments, by Maria Chudnovsky and 2 other authors
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
 | 2016-04
 

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
