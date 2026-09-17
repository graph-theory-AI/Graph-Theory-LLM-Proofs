Attack the following open graph-theory problem.

Catalog id: 1903.04761__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1903.04761__00/
Source paper: On the Maximum Weight Independent Set Problem in graphs without induced… (arXiv:1903.04761)

=== Extracted statement (catalog JSON) ===
Title: Combinatorial Polynomial-Time Algorithm for MIS/MWIS in Perfect Graphs
No combinatorial polynomial-time algorithm is known for any of MIS, MWIS, MC, and MWC in perfect graphs; finding one is a major open problem in the field. At the moment we do not even have a polynomial-time combinatorial algorithm to solve MIS in perfect graphs with no hole of length four.

Context:
The Grötschel–Lovász–Schrijver algorithm solves MWIS on perfect graphs via the ellipsoid method, which the authors distinguish from combinatorial algorithms (roughly, algorithms not using division and operating directly on vertices and edges). Even the restricted case of MIS in perfect graphs with no $C_4$ (hole of length four) lacks a combinatorial polynomial-time algorithm.

=== Catalog page (statement + literature review) ===
Combinatorial MIS algorithm for perfect graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The open problem of finding a combinatorial polynomial-time algorithm for MIS/MWIS in perfect graphs remains largely unresolved. Abrishami and Chudnovsky (arXiv:2110.00108, 2021) made partial progress by giving a combinatorial polynomial-time algorithm for MWIS in perfect graphs of bounded degree that contain no prism and no hole of length four as induced subgraphs—directly addressing the C4-free subcase highlighted in the source paper, but under additional structural restrictions. No combinatorial poly-time algorithm is known for all perfect graphs or even for all C4-free perfect graphs without the bounded-degree and prism-free conditions.

 Cited literature (1)

 
 
 
partial Submodular functions and perfect graphs
 (2021)
 

 
 Tara Abrishami, Maria Chudnovsky · arXiv preprint · arXiv:2110.00108

Gives a combinatorial polynomial-time algorithm for MWIS in perfect graphs of bounded degree with no prism and no hole of length four, making partial progress on the C4-free case of the open problem.
 

 

 Reviewer notes. The full open problem (combinatorial poly-time for all perfect graphs, or even all C4-free perfect graphs) remains open as of 2026. The 2110.00108 result is the closest identified partial progress, but requires both bounded degree and absence of prisms in addition to no C4. No purely combinatorial algorithm for general perfect graphs or even unbounded-degree C4-free perfect graphs has been found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. No combinatorial polynomial-time algorithm is known for any of MIS, MWIS, MC, and MWC in perfect graphs; finding one is a major open problem in the field. At the moment we do not even have a polynomial-time combinatorial algorithm to solve MIS in perfect graphs with no hole of length four.

Context

The Grötschel–Lovász–Schrijver algorithm solves MWIS on perfect graphs via the ellipsoid method, which the authors distinguish from combinatorial algorithms (roughly, algorithms not using division and operating directly on vertices and edges). Even the restricted case of MIS in perfect graphs with no $C_4$ (hole of length four) lacks a combinatorial polynomial-time algorithm.

Notes. A long-standing community open problem cited as motivation in the introduction; not introduced by these authors. PDF source — math may be garbled.

Source paper

 On the Maximum Weight Independent Set Problem in graphs without induced cycles of length at least five
 Maria Chudnovsky, Marcin Pilipczuk, Michał Pilipczuk, Stéphan Thomassé · 2020-01-16
 https://arxiv.org/abs/1903.04761
 PDF source

Related conjectures

 
 same conjecture as
 Combinatorial MIS algorithm on perfect graphs
 open
 Both records pose the identical, standard open problem: find a combinatorial (non-ellipsoid) polynomial-time algorithm for maximum independent set on perfect graphs, each explicitly contrasting with the Grotschel-Lovasz-Schrijver ellipsoid-method algorithm. The extras differ only in framing: 1903.04761 also lists the complementation/weighting-equivalent variants (MWIS, MC, MWC) and the C4-free special case; 1907.01083 also notes that even a combinatorial FPT algorithm is unknown. The core question stated is word-for-word the same problem, so this is a genuine same-conjecture match, not a fuzzy false positive.
 

 
 same conjecture as
 Combinatorial MWIS algorithm for perfect graphs
 partial
 The target's problem (combinatorial polynomial-time algorithm for MWIS in perfect graphs) appears verbatim in the source's list ('no combinatorial polynomial-time algorithm is known for any of MIS, MWIS, MC, and MWC in perfect graphs; finding one is a major open problem'). Both attribute the only known polynomial algorithm to the Grotschel-Lovasz-Schrijver ellipsoid method and ask for a combinatorial replacement. The extra variants in the source are equivalent forms (perfect graphs are closed under complementation, so MC/MWC reduce to MIS/MWIS in the complement), and the C_4-free remark is a subcase, not a different problem. Same classical open problem, with the source a slightly broader record of it.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:A hole in a graph is an induced cycle of length at least $4$, and an antihole is the complement of an induced cycle of length at least $4$. A hole or antihole is long if its length is at least $5$. For an integer $k$, the $k$-prism is the graph consisting of two cliques of size $k$ joined by a matching. The complexity of Maximum (Weight) Independent Set (MWIS) in long-hole-free graphs remains an important open problem. In this paper we give a polynomial time algorithm to solve MWIS in long-hole-free graphs with no $k$-prism (for any fixed integer $k$), and a subexponential algorithm for MWIS in long-hole-free graphs in general. As a special case this gives a polynomial time algorithm to find a maximum weight clique in perfect graphs with no long antihole, and no hole of length $6$. The algorithms use the framework of minimal chordal completions and potential maximal cliques.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1903.04761 [cs.DM]
 

 
  
 (or 
 arXiv:1903.04761v2 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1903.04761
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Marcin Pilipczuk [view email] 
 [v1]
 Tue, 12 Mar 2019 07:37:40 UTC (271 KB)

 [v2]
 Thu, 16 Jan 2020 08:49:20 UTC (402 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the Maximum Weight Independent Set Problem in graphs without induced cycles of length at least five, by Maria Chudnovsky and 3 other authors
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
 | 2019-03
 

 Change to browse by:
 
 cs
 cs.DS
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Maria Chudnovsky
Marcin Pilipczuk
Michal Pilipczuk
Stéphan Thomassé 

 

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
