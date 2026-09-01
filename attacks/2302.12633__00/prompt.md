Attack the following open graph-theory problem.

Catalog id: 2302.12633__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2302.12633__00/
Source paper: Neighborhood complexity of planar graphs (arXiv:2302.12633)

=== Extracted statement (catalog JSON) ===
Title: Problem 41
Determine the profile and neighborhood complexities of planar graphs up to a constant factor. For profile complexity, it is known to be in $\Omega(r^{3})$ (Theorem 36) and in $\operatorname{\mathcal{O}}(r^{4})$ (Theorem 2). For neighborhood complexity, it is known to be in $\Omega(r^{2})$ (Theorem 36 and Lemma 8) and in $\operatorname{\mathcal{O}}(r^{4})$ (Theorem 2).

Context:
The paper closes with two open problems. The first asks for tight bounds on the profile and neighborhood complexities of planar graphs; the existing lower bounds ($\Omega(r^3)$ for profile, $\Omega(r^2)$ for neighborhood) and the paper's new upper bound ($\mathcal{O}(r^4)$ for both) leave a small gap that the authors consider tantalizingly close.

=== Catalog page (statement + literature review) ===
Profile and Neighborhood Complexity of Planar Graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Problem 41 asks to determine the profile and neighborhood complexities of planar graphs up to a constant factor; as of 2026 the gaps (profile: $\Omega(r^3)$ vs $\mathcal{O}(r^4)$; neighborhood: $\Omega(r^2)$ vs $\mathcal{O}(r^4)$) remain unresolved for planar graphs. A 2025 follow-up (arXiv:2501.08895) improves bounds for graphs of bounded treewidth and graphs excluding a fixed minor, answering the related Problem 42 from the same paper, but planar graphs in general have unbounded treewidth and the specific planar-graph question of Problem 41 is not addressed by that work.

 Cited literature (1)

 
 
 
partial Profile and neighbourhood complexity of graphs excluding a minor and tree-structured graphs
 (2025)
 

 
 Laurent Beaudou, Jan Bok, Florent Foucaud, Daniel A. Quiroz, Jean-Florent Raymond · arXiv preprint · arXiv:2501.08895

Improves profile and neighbourhood complexity bounds for graphs excluding a fixed minor and for graphs of bounded treewidth (answering Problem 42 of the source paper), but does not resolve the tight-bound question for general planar graphs (Problem 41).
 

 

 Reviewer notes. The source paper was published in Combinatorica 44, 1115–1148 (2024). The 2025 follow-up arXiv:2501.08895 makes partial progress by answering Problem 42 (bounds for minor-free and bounded-treewidth graph classes), but Problem 41 for planar graphs specifically remains open. Note that planar graphs have unbounded treewidth (e.g., grid graphs), so bounded-treewidth results do not transfer directly to all planar graphs.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the profile and neighborhood complexities of planar graphs up to a constant factor. For profile complexity, it is known to be in $\Omega(r^{3})$ (Theorem 36) and in $\operatorname{\mathcal{O}}(r^{4})$ (Theorem 2). For neighborhood complexity, it is known to be in $\Omega(r^{2})$ (Theorem 36 and Lemma 8) and in $\operatorname{\mathcal{O}}(r^{4})$ (Theorem 2).

Context

The paper closes with two open problems. The first asks for tight bounds on the profile and neighborhood complexities of planar graphs; the existing lower bounds ($\Omega(r^3)$ for profile, $\Omega(r^2)$ for neighborhood) and the paper's new upper bound ($\mathcal{O}(r^4)$ for both) leave a small gap that the authors consider tantalizingly close.

Source paper

 Neighborhood complexity of planar graphs
 Gwenaël Joret, Clément Rambaud · 2023-12-19
 https://arxiv.org/abs/2302.12633

=== Source paper abstract / header ===
Abstract:Reidl, Sánchez Villaamil, and Stravopoulos (2019) characterized graph classes of bounded expansion as follows: A class $\mathcal{C}$ closed under subgraphs has bounded expansion if and only if there exists a function $f:\mathbb{N} \to \mathbb{N}$ such that for every graph $G \in \mathcal{C}$, every nonempty subset $A$ of vertices in $G$ and every nonnegative integer $r$, the number of distinct intersections between $A$ and a ball of radius $r$ in $G$ is at most $f(r) |A|$. When $\mathcal{C}$ has bounded expansion, the function $f(r)$ coming from existing proofs is typically exponential. In the special case of planar graphs, it was conjectured by Sokołowski (2021) that $f(r)$ could be taken to be a polynomial.
In this paper, we prove this conjecture: For every nonempty subset $A$ of vertices in a planar graph $G$ and every nonnegative integer $r$, the number of distinct intersections between $A$ and a ball of radius $r$ in $G$ is $O(r^4 |A|)$. We also show that a polynomial bound holds more generally for every proper minor-closed class of graphs.
 

 
 
 
 Comments:
 v2: simpler proof for K_t-minor-free graphs; paper revised following the referees' comments
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2302.12633 [math.CO]
 

 
  
 (or 
 arXiv:2302.12633v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2302.12633
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Combinatorica, 44:1115--1148, 2024
 

 
 
 Related DOI:
 
 https://doi.org/10.1007/s00493-024-00110-6

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Gwenaël Joret [view email] 
 [v1]
 Fri, 24 Feb 2023 13:50:54 UTC (116 KB)

 [v2]
 Tue, 19 Dec 2023 08:31:10 UTC (90 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Neighborhood complexity of planar graphs, by Gwena\"el Joret and Cl\'ement Rambaud
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
 | 2023-02
 

 Change to browse by:
 
 cs
 cs.DM
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
