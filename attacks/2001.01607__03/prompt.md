Attack the following open graph-theory problem.

Catalog id: 2001.01607__03
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2001.01607__03/
Source paper: (Theta, triangle)-free and (even hole, $K_4$)-free graphs. Part 2 : bou… (arXiv:2001.01607)

=== Extracted statement (catalog JSON) ===
Title: Maximum Independent Set complexity for (even hole, K4)-free and (theta, triangle)-free graphs
Determine the computational complexity of the Maximum Independent Set problem for (even hole, $K_4$)-free graphs and for (theta, triangle)-free graphs.

Context:
Maximum Independent Set is polynomial for (even hole, triangle)-free and (even hole, pyramid)-free graphs. The paper gives polynomial algorithms for (theta, triangle, $S_{i,j,k}$)-free and (even hole, pyramid, $K_t$, $S_{i,j,k}$)-free graphs via bounded treewidth, but the complexity for the larger classes (even hole, $K_4$)-free and (theta, triangle)-free is stated as unknown.

=== Catalog page (statement + literature review) ===
MIS complexity for (even hole, K₄)-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The computational complexity of Maximum Independent Set for (even hole, $K_4$)-free graphs and for (theta, triangle)-free graphs remains open. Partial progress exists for subclasses: the source paper gives polynomial algorithms for (theta, triangle, $S_{i,j,k}$)-free and (even hole, pyramid, $K_t$, $S_{i,j,k}$)-free graphs via bounded treewidth, and arXiv:2203.06775 (2022) extends this by proving bounded treewidth for (even hole, diamond, pyramid, $K_t$)-free graphs, implying polynomial MIS for that subclass. Web searches through 2026 confirm that the full complexity question for the stated classes is unresolved.

 Cited literature (1)

 
 
 
partial Induced subgraphs and tree decompositions IV. (Even hole, diamond, pyramid)-free graphs
 (2022)
 

 
 Tara Abrishami, Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · arXiv preprint · arXiv:2203.06775

Proves that for all $t > 0$ there exists $d_t \geq 0$ such that every (even hole, diamond, pyramid, $K_t$)-free graph has treewidth at most $d_t$ (Theorem 1.4), establishing a special case of Conjecture 1.5 from the source paper and implying polynomial-time MIS for this subclass of (even hole, $K_4$)-free graphs.
 

 

 Reviewer notes. No paper resolving the full complexity question for (even hole, $K_4$)-free or (theta, triangle)-free graphs was found within the 5-call web search budget. A 2026 paper arXiv:2604.01816 '(Even hole, triangle)-free graphs revisited' appeared in search results and may be relevant (the (even hole, triangle)-free class is a proper subclass of (even hole, $K_4$)-free), but could not be verified within the call cap. The $O(\log n)$ treewidth bound for (theta, triangle)-free graphs from the source paper yields only quasi-polynomial MIS; polynomial-time complexity remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the computational complexity of the Maximum Independent Set problem for (even hole, $K_4$)-free graphs and for (theta, triangle)-free graphs.

Context

Maximum Independent Set is polynomial for (even hole, triangle)-free and (even hole, pyramid)-free graphs. The paper gives polynomial algorithms for (theta, triangle, $S_{i,j,k}$)-free and (even hole, pyramid, $K_t$, $S_{i,j,k}$)-free graphs via bounded treewidth, but the complexity for the larger classes (even hole, $K_4$)-free and (theta, triangle)-free is stated as unknown.

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
