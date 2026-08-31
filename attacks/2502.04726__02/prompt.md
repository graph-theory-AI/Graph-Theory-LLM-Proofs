Attack the following open graph-theory problem.

Catalog id: 2502.04726__02
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2502.04726__02/
Source paper: Lollipops, dense cycles and chords (arXiv:2502.04726)

=== Catalog page (statement + literature review) ===
Active vertices in optimal lollipop cycle — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Question 4.2 from arXiv:2502.04726 asks whether there is a simple way to compute all active vertices in the cycle of an optimal lollipop; it appears in the concluding open problems section of the paper. The paper itself establishes that finding an optimal lollipop is NP-hard (solving it in polynomial time would imply finding a Hamiltonian cycle in polynomial time), and provides a weaker polynomial-time procedure that finds only sufficiently many active paths with distinct ends. No follow-up work addressing this specific algorithmic question was found in a broad web search conducted in May 2026.

 Reviewer notes. No follow-up found. The question is inherently tied to NP-hardness of optimal lollipop computation, making a simple closed-form characterization of active vertices unlikely without additional structural assumptions. Paper 2502.10657 (Chords of longest cycles passing through a specified small set) uses related lollipop-style techniques but does not address Question 4.2.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. Is there a simple way to compute all the active vertices in the cycle of an optimal lollipop?

Context

Active vertices determine the number of distinct chords produced by the lollipop argument. In the lollipop argument, the number of distinct active vertices (and thus chords) increases with the girth $g$ of the host graph, motivating the search for an efficient procedure to identify them.

Source paper

 Lollipops, dense cycles and chords
 Zdeněk Dvořák, Beatriz Martins, Stéphan Thomassé, Nicolas Trotignon · 2025-10-10
 https://arxiv.org/abs/2502.04726

=== Source paper abstract / header ===
Abstract:In 1980, Gupta, Kahn and Robertson proved that every graph $G$ with minimum degree at least $k\geq 2$ contains a cycle $C$ containing at least $k+1$ vertices each having at least $k$ neighbors in $C$ (so $C$ has at least $\frac{(k+1)(k-2)}{2}$ chords). In this work, we go further by showing that some of its edges can be contracted to obtain a graph with high minimum degree (we call such a minor of $C$ a \emph{cyclic minor}). We then investigate further cycles having cliques as cyclic minors, and show that minimum degree at least $O(k^2)$ guarantees a cyclic $K_k$-minor.
 

 
 
 
 Comments:
 Added explanations, mostly about the application of Marcus Tardos Theorem
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C38
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:2502.04726 [math.CO]
 

 
  
 (or 
 arXiv:2502.04726v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2502.04726
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Nicolas Trotignon [view email] 
 [v1]
 Fri, 7 Feb 2025 07:50:53 UTC (15 KB)

 [v2]
 Thu, 6 Mar 2025 07:43:42 UTC (17 KB)

 [v3]
 Wed, 12 Mar 2025 13:49:27 UTC (17 KB)

 [v4]
 Fri, 10 Oct 2025 09:38:25 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Lollipops, dense cycles and chords, by Zden\v{e}k Dvo\v{r}\'ak and Beatriz Martins and St\'ephan Thomass\'e and Nicolas Trotignon
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
 | 2025-02
 

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
