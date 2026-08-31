Attack the following open graph-theory problem.

Catalog id: 1707.09402__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1707.09402__00/
Source paper: Independent Feedback Vertex Set for $P_5$-free Graphs (arXiv:1707.09402)

=== Catalog page (statement + literature review) ===
Independent Feedback Vertex Set linear forest complexity — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No follow-up paper resolving the complexity of Independent Feedback Vertex Set for P_h-free graphs (h ≥ 6) or for general linear forests has been identified. Related problems—standard Feedback Vertex Set and Even Cycle Transversal on linear-forest-free graphs—have seen progress (polynomial time for sP₃-free and (sP₁+P₅)-free graphs, arXiv:2105.02736), but those results do not carry over to the independent variant. The classification for linear-forest cases of Independent Feedback Vertex Set therefore appears to remain open as of 2026.

 Reviewer notes. The conjecture is from 2017; no resolution found after ~9 years in the indexed literature, which warrants medium rather than high confidence. The related (non-independent) Feedback Vertex Set and Even Cycle Transversal problems have been extended to broader linear-forest classes (arXiv:2105.02736), but techniques there rely on block-graph structure and do not obviously extend to the independent setting. Absence of visible progress over this timescale may indicate the problem is genuinely hard.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Only the cases where $H$ is a linear forest, that is, a disjoint union of paths, remain open for the complexity classification of \textsc{Independent Feedback Vertex Set} on $H$-free graphs. In particular, the case where $H$ is a single path $P_h$ with $h \geq 6$ has not yet been resolved.

Context

The authors prove NP-completeness when $H$ contains a claw or cycle, and polynomial-time solvability for $P_4$-free and $P_5$-free graphs, completing those cases. This leaves all linear-forest cases open toward a full complexity dichotomy for $H$-free graphs.

Notes. PDF source — stated in prose without a labelled environment. The provided text is truncated after Section 3; Section 6 is described in the introduction as explicitly surveying related open problems but its content was not included in the extraction, so additional formal conjectures/questions from that section may be missing.

Source paper

 Independent Feedback Vertex Set for $P_5$-free Graphs
 Marthe Bonamy, Konrad K. Dabrowski, Carl Feghali, Matthew Johnson, Daniel Paulusma · 2017-07-28
 https://arxiv.org/abs/1707.09402
 PDF source

=== Source paper abstract / header ===
Abstract:The NP-complete problem Feedback Vertex Set is that of deciding whether or not it is possible, for a given integer $k\geq 0$, to delete at most $k$ vertices from a given graph so that what remains is a forest. The variant in which the deleted vertices must form an independent set is called Independent Feedback Vertex Set and is also NP-complete. In fact, even deciding if an independent feedback vertex set exists is NP-complete and this problem is closely related to the $3$-Colouring problem, or equivalently, to the problem of deciding whether or not a graph has an independent odd cycle transversal, that is, an independent set of vertices whose deletion makes the graph bipartite. We initiate a systematic study of the complexity of Independent Feedback Vertex Set for $H$-free graphs. We prove that it is NP-complete if $H$ contains a claw or cycle. Tamura, Ito and Zhou proved that it is polynomial-time solvable for $P_4$-free graphs. We show that it remains polynomial-time solvable for $P_5$-free graphs. We prove analogous results for the Independent Odd Cycle Transversal problem, which asks whether or not a graph has an independent odd cycle transversal of size at most $k$ for a given integer $k\geq 0$. Finally, in line with our underlying research aim, we compare the complexity of Independent Feedback Vertex Set for $H$-free graphs with the complexity of $3$-Colouring, Independent Odd Cycle Transversal and other related problems.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1707.09402 [cs.DS]
 

 
  
 (or 
 arXiv:1707.09402v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1707.09402
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Matthew Johnson [view email] 
 [v1]
 Fri, 28 Jul 2017 20:17:45 UTC (27 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Independent Feedback Vertex Set for $P_5$-free Graphs, by Marthe Bonamy and 4 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2017-07
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Marthe Bonamy
Konrad K. Dabrowski
Carl Feghali
Matthew Johnson
Daniël Paulusma 

 

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
