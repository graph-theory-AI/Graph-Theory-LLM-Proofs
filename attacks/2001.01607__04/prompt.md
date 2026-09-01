Attack the following open graph-theory problem.

Catalog id: 2001.01607__04
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2001.01607__04/
Source paper: (Theta, triangle)-free and (even hole, $K_4$)-free graphs. Part 2 : bou… (arXiv:2001.01607)

=== Extracted statement (catalog JSON) ===
Title: Maximum Independent Set complexity for H-free graphs when H contains P7, S1,1,3, or S1,2,2
Determine the computational complexity of the Maximum Independent Set problem for $H$-free graphs whenever $H$ is some $S_{i,j,k}$ that contains either $P_7$, $S_{1,1,3}$, or $S_{1,2,2}$.

Context:
The problem is polynomial for $H \subseteq P_k$ with $k \leq 6$ and for $H \subseteq S_{i,j,k}$ with $(i,j,k) \leq (1,1,2)$, and is NP-hard when $H$ is not an induced subgraph of any $S_{i,j,k}$. The boundary region where $H$ contains $P_7$, $S_{1,1,3}$, or $S_{1,2,2}$ is listed as completely open.

=== Catalog page (statement + literature review) ===
MIS complexity for S_{i,j,k}-free graphs with P₇ — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The computational complexity of Maximum Independent Set for $H$-free graphs when $H$ contains $P_7$, $S_{1,1,3}$, or $S_{1,2,2}$ remains unresolved as a full polynomial/NP-hard dichotomy. Partial progress exists: quasi-polynomial-time algorithms apply to all $P_k$-free graphs (hence $P_7$-free), and polynomial-time algorithms have been obtained for bounded-degree graphs excluding any fixed subdivided claw as an induced subgraph, covering $S_{1,1,3}$- and $S_{1,2,2}$-free cases under bounded degree. No polynomial-time algorithm or NP-hardness result for the general unbounded-degree cases has been found.

 Cited literature (1)

 
 
 
partial Polynomial-time algorithm for Maximum Independent Set in bounded-degree graphs with no long induced claws
 (2022)
 

 
 Tara Abrishami, Maria Chudnovsky, Cemil Dibek, Paweł Rzążewski · arXiv preprint · arXiv:2107.05434

Gives a polynomial-time algorithm for Maximum Independent Set in $H$-free graphs of bounded degree for any fixed subdivided claw $H$, resolving the bounded-degree special cases of $S_{1,1,3}$- and $S_{1,2,2}$-free graphs but not the general (unbounded-degree) question.
 

 

 Reviewer notes. Quasi-polynomial-time algorithms for Independent Set in P_k-free graphs (Gartland–Lokshtanov 2020, arXiv:2005.00690; Pilipczuk et al. 2021, arXiv:2009.13494) provide sub-exponential progress for P_7-free graphs but fall short of polynomial time. The bounded-degree result (arXiv:2107.05434) makes partial inroads on the S_{i,j,k} cases. The full dichotomy determining which S_{i,j,k} yield polynomial-time solvability vs NP-hardness remains open. The internal reference 2203.06775 was verified to be about a different conjecture in the same source paper (treewidth of (even hole, K_4)-free graphs, Conjecture 1.5), not the MIS complexity problem.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the computational complexity of the Maximum Independent Set problem for $H$-free graphs whenever $H$ is some $S_{i,j,k}$ that contains either $P_7$, $S_{1,1,3}$, or $S_{1,2,2}$.

Context

The problem is polynomial for $H \subseteq P_k$ with $k \leq 6$ and for $H \subseteq S_{i,j,k}$ with $(i,j,k) \leq (1,1,2)$, and is NP-hard when $H$ is not an induced subgraph of any $S_{i,j,k}$. The boundary region where $H$ contains $P_7$, $S_{1,1,3}$, or $S_{1,2,2}$ is listed as completely open.

Notes. PDF source — math notation reconstructed; stated in the 'Algorithmic consequences' section.

Source paper

 (Theta, triangle)-free and (even hole, $K_4$)-free graphs. Part 2 : bounds on treewidth
 Marcin Pilipczuk, Ni Luh Dewi Sintiari, Stéphan Thomassé, Nicolas Trotignon · 2020-10-27
 https://arxiv.org/abs/2001.01607
 PDF source

=== Source paper abstract / header ===
Abstract:A {\em theta} is a graph made of three internally vertex-disjoint chordless paths $P_1 = a \dots b$, $P_2 = a \dots b$, $P_3 = a \dots b$ of length at least~2 and such that no edges exist between the paths except the three edges incident to $a$ and the three edges incident to $b$. A {\em pyramid} is a graph made of three chordless paths $P_1 = a \dots b_1$, $P_2 = a \dots b_2$, $P_3 = a \dots b_3$ of length at least~1, two of which have length at least 2, vertex-disjoint except at $a$, and such that $b_1b_2b_3$ is a triangle and no edges exist between the paths except those of the triangle and the three edges incident to~$a$. An \emph{even hole} is a chordless cycle of even length. For three non-negative integers $i\leq j\leq k$, let $S_{i,j,k}$ be the tree with a vertex $v$, from which start three paths with $i$, $j$, and $k$ edges respectively. We denote by $K_t$ the complete graph on $t$ vertices.
We prove that for all non-negative integers $i, j, k$, the class of graphs that contain no theta, no $K_3$, and no $S_{i, j, k}$ as induced subgraphs have bounded treewidth. We prove that for all non-negative integers $i, j, k, t$, the class of graphs that contain no even hole, no pyramid, no $K_t$, and no $S_{i, j, k}$ as induced subgraphs have bounded treewidth. To bound the treewidth, we prove that every graph of large treewidth must contain a large clique or a minimal separator of large cardinality.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2001.01607 [cs.DM]
 

 
  
 (or 
 arXiv:2001.01607v3 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2001.01607
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 J Graph Theory. 2021; 97: 624-641
 

 
 
 Related DOI:
 
 https://doi.org/10.1002/jgt.22675

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Nicolas Trotignon [view email] 
 [v1]
 Mon, 6 Jan 2020 14:43:25 UTC (48 KB)

 [v2]
 Mon, 13 Jan 2020 16:27:29 UTC (48 KB)

 [v3]
 Tue, 27 Oct 2020 05:20:22 UTC (50 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled (Theta, triangle)-free and (even hole, $K_4$)-free graphs. Part 2 : bounds on treewidth, by Marcin Pilipczuk and 2 other authors
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
 | 2020-01
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Marcin Pilipczuk
Ni Luh Dewi Sintiari
Stéphan Thomassé
Nicolas Trotignon 

 

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
