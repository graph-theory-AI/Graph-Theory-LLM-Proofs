Attack the following open graph-theory problem.

Catalog id: 1903.04761__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1903.04761__01/
Source paper: On the Maximum Weight Independent Set Problem in graphs without induced… (arXiv:1903.04761)

=== Catalog page (statement + literature review) ===
FPT Algorithm for MWIS in (Long-Hole, k-Prism)-Free Graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 low confidence
 

 The source paper provides a polynomial-time n^{O(k)} algorithm for MWIS in (long-hole, k-prism)-free graphs and remarks that the authors do not see how to upgrade this to an FPT algorithm parameterized by k without invoking a structural result of Abrishami et al. Targeted searches across arXiv and related literature through 2026 found no follow-up paper that resolves this FPT question either positively or negatively. The problem is 6 years old, so absence of evidence may be indicative of genuine difficulty.

 Reviewer notes. No follow-up found. The open question is whether the n^{O(k)} algorithm of Theorem 1.1 can be made FPT in k for MWIS in (long-hole, k-prism)-free graphs. The authors note that invoking Abrishami et al. [1] (likely the series on induced subgraphs and tree decompositions of even-hole-free graphs) might be a path forward, but no paper appears to have completed this. Related progress exists on adjacent classes (no long claws, even-hole-free) but not on this specific class.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We do not see how to turn Theorem 1.1 into an FPT-algorithm (without using the result of [1]).

Context

Theorem 1.1 gives a polynomial-time algorithm running in time $n^{O(k)}$ for MWIS in (long-hole, $k$-prism)-free $n$-vertex graphs for any fixed integer $k > 0$. Immediately after stating the theorem the authors remark that extending this to a fixed-parameter tractable algorithm parameterized by $k$ appears to be out of reach with their techniques, unless the result of Abrishami et al. [1] is invoked.

Notes. Implicit open question stated in prose without a labelled environment. PDF source — math may be garbled.

Source paper

 On the Maximum Weight Independent Set Problem in graphs without induced cycles of length at least five
 Maria Chudnovsky, Marcin Pilipczuk, Michał Pilipczuk, Stéphan Thomassé · 2020-01-16
 https://arxiv.org/abs/1903.04761
 PDF source

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
