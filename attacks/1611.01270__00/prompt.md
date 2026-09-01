Attack the following open graph-theory problem.

Catalog id: 1611.01270__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1611.01270__00/
Source paper: Fast property testing and metrics for permutations (arXiv:1611.01270)

=== Extracted statement (catalog JSON) ===
Title: Open Problem (better query complexity bounds for property testing)
It remains a major open problem if better bounds hold for the various property testing results.

Context:
General results in combinatorial property testing show that natural properties can be tested with constant query complexity depending only on $\varepsilon$ and the property, but the upper bounds arising from proofs are often enormous: wowzer-type or Ackermann-type in $1/\varepsilon$, or established only via compactness with no explicit bound at all. The paper makes progress on this problem for permutations by establishing a universal polynomial-in-$1/\varepsilon$ query complexity bound for two-sided testing of hereditary properties with respect to the rectangular distance.

=== Catalog page (statement + literature review) ===
Polynomial query complexity for permutation property testing — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Fox and Wei (arXiv:1611.01270) established a universal polynomial-in-1/ε query complexity bound for two-sided testing of hereditary permutation properties under rectangular distance, improving prior Ackermann-type bounds from Klimošová--Kráļ. The open problem asks whether similarly improved (polynomial or better) bounds hold for other metrics (e.g., Kendall's tau) and other testing regimes. A 2025 survey by Gishboliner and Shapira on polynomial property testing (arXiv:2508.16878) includes a section on permutations covering this area, but no paper found in the indexed literature definitively resolves the full open problem.

 Cited literature (1)

 
 
 
survey Polynomial Property Testing
 (2025)
 

 
 Lior Gishboliner, Asaf Shapira · arXiv preprint · arXiv:2508.16878

A 2025 survey on polynomial property testing includes a dedicated section on permutations (Section 6) covering hereditary permutation property testing under Kendall's tau distance and citing Fox-Wei's polynomial bounds, situating the open problem in the broader landscape of which properties admit poly(1/ε) testers.
 

 

 Reviewer notes. The open problem as stated is deliberately broad ('various property testing results'), making definitive resolution hard to pinpoint. Fox-Wei itself already established polynomial bounds for rectangular distance; the remaining question concerns other metrics and tighter bounds. The Gishboliner-Shapira 2025 survey (arXiv:2508.16878) covers this landscape but its full content on permutations was not accessible to verify whether it proves new results beyond surveying. No counterexample or full resolution was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It remains a major open problem if better bounds hold for the various property testing results.

Context

General results in combinatorial property testing show that natural properties can be tested with constant query complexity depending only on $\varepsilon$ and the property, but the upper bounds arising from proofs are often enormous: wowzer-type or Ackermann-type in $1/\varepsilon$, or established only via compactness with no explicit bound at all. The paper makes progress on this problem for permutations by establishing a universal polynomial-in-$1/\varepsilon$ query complexity bound for two-sided testing of hereditary properties with respect to the rectangular distance.

Notes. PDF source — paper text is truncated (ends mid-sentence in the introduction); this open problem is presented as a known community-level motivation rather than a fresh conjecture introduced by the paper's authors. No formal labelled environment. Any conjectures or questions posed in later sections of the paper are not visible in the supplied extract.

Source paper

 Fast property testing and metrics for permutations
 Jacob Fox, Fan Wei · 2018-04-04
 https://arxiv.org/abs/1611.01270
 PDF source

=== Source paper abstract / header ===
Abstract:The goal of property testing is to quickly distinguish between objects which satisfy a property and objects that are $\epsilon$-far from satisfying the property. There are now several general results in this area which show that natural properties of combinatorial objects can be tested with "constant" query complexity, depending only on $\epsilon$ and the property, and not on the size of the object being tested. The upper bound on the query complexity coming from the proof techniques are often enormous and impractical. It remains a major open problem if better bounds hold.
Maybe surprisingly, for testing with respect to the rectangular distance, we prove there is a universal (not depending on the property), polynomial in $1/\epsilon$ query complexity bound for two-sided testing hereditary properties of sufficiently large permutations. We further give a nearly linear bound with respect to a closely related metric which also depends on the smallest forbidden subpermutation for the property. Finally, we show that several different permutation metrics of interest are related to the rectangular distance, yielding similar results for testing with respect to these metrics.
 

 
 
 
 Comments:
 32 pages, 12 figures. The second version fixed some typos, and used the term "earth mover's distance" in replace of the term "planar footrule distance" used in v1
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM); Probability (math.PR)
 
 
 MSC classes:
 05, 60, 68
 

 Cite as:
 arXiv:1611.01270 [math.CO]
 

 
  
 (or 
 arXiv:1611.01270v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1611.01270
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Fan Wei [view email] 
 [v1]
 Fri, 4 Nov 2016 06:24:23 UTC (1,310 KB)

 [v2]
 Wed, 4 Apr 2018 13:48:14 UTC (1,311 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Fast property testing and metrics for permutations, by Jacob Fox and Fan Wei
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
 | 2016-11
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.PR
 

 

 

 
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
