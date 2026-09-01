Attack the following open graph-theory problem.

Catalog id: 1909.07141__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1909.07141__00/
Source paper: Disproportionate division (arXiv:1909.07141)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture (f(n) = 2n−2)
We suspect that the above construction reflects the truth and that $f(n) = 2n - 2$ for all $n \geq 2$.

Context:
The authors give a construction (attributed to Segal-Halevi [6]) showing $f(n) \geq 2n-2$ for all $n \geq 2$, where $f(n)$ is the maximum number of cuts needed for disproportionate division with $n$ agents. Theorem 1.1 establishes $f(n) \leq 3n-4$, leaving a gap. The authors believe the lower bound is tight and that the truth is $f(n) = 2n-2$.

=== Catalog page (statement + literature review) ===
Disproportionate division requires 2n−2 cuts — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that $f(n) = 2n-2$ for all $n \geq 2$ remains open as of May 2026. The source paper (published in Bulletin of the London Mathematical Society, 2020) establishes $f(n) \leq 3n-4$, improving the earlier O(n \log n) bound, while the matching lower bound $f(n) \geq 2n-2$ comes from a construction of Segal-Halevi. No follow-up paper closing the gap between $2n-2$ and $3n-4$ has been found in the indexed literature. Narayanan's publication list through 2026 contains no further work on this problem.

 Reviewer notes. The arXiv abstract mentions a topological conjecture (unproven) that would imply 2n-2 cuts suffice in general, which together with the Segal-Halevi lower bound would settle f(n)=2n-2. No paper resolving this topological conjecture or otherwise closing the gap was found after five web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We suspect that the above construction reflects the truth and that $f(n) = 2n - 2$ for all $n \geq 2$.

Context

The authors give a construction (attributed to Segal-Halevi [6]) showing $f(n) \geq 2n-2$ for all $n \geq 2$, where $f(n)$ is the maximum number of cuts needed for disproportionate division with $n$ agents. Theorem 1.1 establishes $f(n) \leq 3n-4$, leaving a gap. The authors believe the lower bound is tight and that the truth is $f(n) = 2n-2$.

Source paper

 Disproportionate division
 Logan Crew, Bhargav Narayanan, Sophie Spirkl · 2019-09-16
 https://arxiv.org/abs/1909.07141
 PDF source

=== Source paper abstract / header ===
Abstract:We study the disproportionate version of the classical cake-cutting problem: how efficiently can we divide a cake, here $[0,1]$, among $n$ agents with different demands $\alpha_1, \alpha_2, \dots, \alpha_n$ summing to $1$? When all the agents have equal demands of $\alpha_1 = \alpha_2 = \dots = \alpha_n = 1/n$, it is well-known that there exists a fair division with $n-1$ cuts, and this is optimal. For arbitrary demands on the other hand, folklore arguments from algebraic topology show that $O(n\log n)$ cuts suffice, and this has been the state of the art for decades. Here, we improve the state of affairs in two ways: we prove that disproportionate division may always be achieved with $3n-4$ cuts, and give an effective combinatorial procedure to construct such a division. We also offer a topological conjecture that implies that $2n-2$ cuts suffice in general, which would be optimal.
 

 
 
 
 Comments:
 8 pages, submitted
 

 Subjects:
 
 Combinatorics (math.CO); Computational Geometry (cs.CG); Algebraic Topology (math.AT)
 
 
 MSC classes:
 05D05 (Primary), 91B32 (Secondary)
 

 Cite as:
 arXiv:1909.07141 [math.CO]
 

 
  
 (or 
 arXiv:1909.07141v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1909.07141
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Bhargav Narayanan [view email] 
 [v1]
 Mon, 16 Sep 2019 12:05:26 UTC (8 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Disproportionate division, by Logan Crew and 2 other authors
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
 | 2019-09
 

 Change to browse by:
 
 cs
 cs.CG
 math
 math.AT
 

 

 

 
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
