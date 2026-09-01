Attack the following open graph-theory problem.

Catalog id: 2001.01607__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2001.01607__00/
Source paper: (Theta, triangle)-free and (even hole, $K_4$)-free graphs. Part 2 : bou… (arXiv:2001.01607)

=== Extracted statement (catalog JSON) ===
Title: Open Question: (even hole, K4, diamond)-free treewidth/cliquewidth
Is it true that (even hole, $K_4$, diamond)-free graphs have bounded treewidth (or cliquewidth)?

Context:
The paper proves bounded treewidth for (theta, triangle, $S_{i,j,k}$)-free and (even hole, pyramid, $K_t$, $S_{i,j,k}$)-free graphs. The analogous question for graphs excluding the diamond ($K_4$ minus one edge) instead of a subdivided claw is explicitly listed as open.

=== Catalog page (statement + literature review) ===
Bounded treewidth for even-hole K₄ diamond-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The conjecture asks whether (even hole, $K_4$, diamond)-free graphs have bounded treewidth or cliquewidth. Abrishami, Chudnovsky, Hajebi, and Spirkl (arXiv:2203.06775, 2022) proved a partial result: for every $t > 0$, every (even hole, diamond, pyramid, $K_t$)-free graph has bounded treewidth — a special case of the conjecture that additionally requires pyramid-free graphs. Search results indicate that a structure theorem (every even-hole-free graph of sufficiently large treewidth contains $K_4$ or a diamond as an induced subgraph) was subsequently proved, which would directly resolve the conjecture, but the specific paper establishing this result could not be verified within the search budget.

 Cited literature (1)

 
 
 
partial Induced subgraphs and tree decompositions IV. (Even hole, diamond, pyramid)-free graphs
 (2022)
 

 
 Tara Abrishami, Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl · Electronic Journal of Combinatorics · arXiv:2203.06775

Proves that for every $t > 0$ there exists $d_t \geq 0$ such that every (even hole, diamond, pyramid, $K_t$)-free graph has treewidth at most $d_t$; this is a special case of the conjecture with the additional requirement of pyramid-free.
 

 

 Reviewer notes. The partial result in arXiv:2203.06775 proves bounded treewidth for the subclass that additionally excludes pyramids, explicitly identified as a special case of the conjecture. Search results strongly suggest a structure theorem — that every even-hole-free graph of large treewidth must contain $K_4$ or a diamond as an induced subgraph — was subsequently proved (likely in arXiv:2309.04390, 'Induced subgraphs and tree decompositions XI'), which would directly resolve the conjecture; this paper could not be verified within the 5-call budget. Status therefore set to partial rather than solved.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it true that (even hole, $K_4$, diamond)-free graphs have bounded treewidth (or cliquewidth)?

Context

The paper proves bounded treewidth for (theta, triangle, $S_{i,j,k}$)-free and (even hole, pyramid, $K_t$, $S_{i,j,k}$)-free graphs. The analogous question for graphs excluding the diamond ($K_4$ minus one edge) instead of a subdivided claw is explicitly listed as open.

Notes. PDF source — math notation reconstructed; stated in the dedicated 'Open questions' section of the paper.

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
