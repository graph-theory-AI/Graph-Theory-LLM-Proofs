Attack the following open graph-theory problem.

Catalog id: 2505.24100__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2505.24100__01/
Source paper: Halfway to induced saturation for even cycles (arXiv:2505.24100)

=== Catalog page (statement + literature review) ===
Polynomial size even-cycle induced saturation — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Question 1.8 from arXiv:2505.24100 asks whether a polynomial $f$ suffices to bound the size of an induced-saturated graph for $C_{2t-2}$, replacing the doubly-exponential construction of Theorem 1.6. The authors themselves state they have no rationale for expecting the vertex count to exceed linear in $t$, but no polynomial construction or impossibility result has been found in the literature as of May 2026.

 Reviewer notes. No follow-up paper resolving or making partial progress on Question 1.8 was found in five web calls. The paper is approximately 11 months old. The conjecture is open: the only known construction (Theorem 1.6 of the source paper) is doubly exponential in t, while the question asks whether polynomial size in t is achievable.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. Does there exist a polynomial $f$ such that for every $t\geq 3$, there is a graph $G$ on at most $f(t)$ vertices with $E(G)\neq\varnothing$, such that $G$ is $H$-free but $G-e$ has an induced subgraph isomorphic to $C_{2t-2}$ for every $e\in E(G)$?

Context

The construction of $G_t$ in Theorem 1.6 has doubly exponential size in $t$. The authors remark they do not even have a rationale for expecting the number of vertices to be more than linear in $t$, making this a natural question about the efficiency of the construction.

Source paper

 Halfway to induced saturation for even cycles
 Xinyue Fan, Sahab Hajebi, Sepehr Hajebi, Sophie Spirkl · 2025-06-02
 https://arxiv.org/abs/2505.24100

=== Source paper abstract / header ===
Abstract:For graphs $G$ and $H$, we say that $G$ is $H$-free if no induced subgraph of $G$ is isomorphic to $H$, and that $G$ is $H$-induced-saturated if $G$ is $H$-free but removing or adding any edge in $G$ creates an induced copy of $H$. A full characterization of graphs $H$ for which $H$-induced-saturated graphs exist remains elusive. Even the case where $H$ is a path -- now settled by the collective results of Martin and Smith, Bonamy et al., and Dvoŕǎk -- was already quite challenging.
What if $H$ is a cycle? The complete answer for odd cycles was given by Behren et al., leaving the case of even cycles (except for the $4$-cycle) wide open. Our main result is the first step toward closing this gap: We prove that for every even cycle $H$, there is a graph $G$ with at least one edge such that $G$ is $H$-free but removing any edge from $G$ creates an induced copy of $H$ (in fact, we construct $H$-induced-saturated graphs for every even cycle $H$ on at most 10 vertices).
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2505.24100 [math.CO]
 

 
  
 (or 
 arXiv:2505.24100v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2505.24100
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Sepehr Hajebi [view email] 
 [v1]
 Fri, 30 May 2025 01:03:32 UTC (208 KB)

 [v2]
 Mon, 2 Jun 2025 01:56:42 UTC (208 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Halfway to induced saturation for even cycles, by Xinyue Fan and 3 other authors
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
 | 2025-05
 

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
