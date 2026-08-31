Attack the following open graph-theory problem.

Catalog id: 2505.05997__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2505.05997__00/
Source paper: A Polynomial-Time Approximation Algorithm for Complete Interval Minors (arXiv:2505.05997)

=== Catalog page (statement + literature review) ===
Open: $f(\mathrm{OPT})$-approximation for largest (general) complete minor — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The best known polynomial-time approximation for the size of a largest complete minor remains O(\sqrt{n}), due to Alon, Lingas, and Wahlén, with no PTAS unless P=NP (Wahlén). The source paper (arXiv:2505.05997, APPROX-RANDOM 2025) resolves the analogous question for complete interval minors in ordered graphs via a polytime f(t)-approximation (f triply exponential), but the open problem for general complete minors is explicitly cited as unresolved motivation. No follow-up paper resolving the f(OPT)-approximation question for general complete minors was found in the indexed literature.

 Reviewer notes. Paper published at APPROX-RANDOM 2025 (LIPIcs vol. 353, article 15). The conjecture is very recent (May 2025); absence of follow-up in web search is consistent with open status. The O(\sqrt{n}) upper bound and no-PTAS lower bound are confirmed from the abstract and search results, but no paper closing the f(OPT)-approximation gap was found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. It is open whether finding the size of a largest complete minor admits a polynomial-time $f(\mathrm{OPT})$-approximation algorithm.

Context

The best known polynomial-time approximation factor for the size of a largest complete minor is $O(\sqrt{n})$, due to Alon, Lingas and Wahlén [1]. No PTAS exists unless $\mathsf{P}=\mathsf{NP}$ (Wahlén [32]). The authors cite this open problem as direct motivation for studying the analogous question for complete interval minors in ordered graphs, where they obtain a polytime $f(t)$-approximation.

Notes. Stated in the introduction as a known open problem without a labelled environment and without explicit attribution to specific authors; captured because the authors explicitly flag it as open and use it to motivate the paper.

Source paper

 A Polynomial-Time Approximation Algorithm for Complete Interval Minors
 Romain Bourneuf, Julien Cocquet, Chaoliang Tang, Stéphan Thomassé · 2025-05-09
 https://arxiv.org/abs/2505.05997

=== Source paper abstract / header ===
Abstract:As shown by Robertson and Seymour, deciding whether the complete graph $K_t$ is a minor of an input graph $G$ is a fixed parameter tractable problem when parameterized by $t$. From the approximation viewpoint, the gap to fill is quite large, as there is no PTAS for finding the largest complete minor unless $P = NP$, whereas a polytime $O(\sqrt n)$-approximation algorithm was given by Alon, Lingas and Wahlén.
We investigate the complexity of finding $K_t$ as interval minor in ordered graphs (i.e. graphs with a linear order on the vertices, in which intervals are contracted to form minors). Our main result is a polytime $f(t)$-approximation algorithm, where $f$ is triply exponential in $t$ but independent of $n$. The algorithm is based on delayed decompositions and shows that ordered graphs without a $K_t$ interval minor can be constructed via a bounded number of three operations: closure under substitutions, edge union, and concatenation of a stable set. As a byproduct, graphs avoiding $K_t$ as an interval minor have bounded chromatic number.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2505.05997 [cs.DS]
 

 
  
 (or 
 arXiv:2505.05997v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2505.05997
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Romain Bourneuf [view email] 
 [v1]
 Fri, 9 May 2025 12:25:12 UTC (45 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A Polynomial-Time Approximation Algorithm for Complete Interval Minors, by Romain Bourneuf and 3 other authors
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
 | 2025-05
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.CO
 

 

 

 
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
