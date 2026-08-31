Attack the following open graph-theory problem.

Catalog id: 2305.16258__00
Catalog status: partial (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2305.16258__00/
Source paper: Tree independence number I. (Even hole, diamond, pyramid)-free graphs (arXiv:2305.16258)

=== Catalog page (statement + literature review) ===
Bounded tree-α in (even hole, diamond)-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Conjecture 1.6 asks for a constant (n-independent) bound on tree-α for the class of (even hole, diamond)-free graphs. The source paper itself established this for the smaller class also excluding pyramids. The follow-up paper arXiv:2407.08927 (Tree Independence Number IV, 2024) proves that the strictly larger class of all even-hole-free graphs has tree-α at most O(log^10 n), a polylogarithmic bound that does not imply the conjectured constant bound. No verified source found establishes the constant bound for the full (even hole, diamond)-free class.

 Cited literature (1)

 
 
 
partial Tree independence number IV. Even-hole-free graphs
 (2024)
 

 
 Chudnovsky, M., Gartland, P., Hajebi, S., Lokshtanov, D., Spirkl, S. · arXiv preprint · arXiv:2407.08927

Proves that every n-vertex even-hole-free graph (a superclass of (even hole, diamond)-free) has tree-α at most c·log^10(n), giving a polylogarithmic but not a constant bound, hence partial progress toward Conjecture 1.6.
 

 

 Reviewer notes. The TIN series (papers I–IV by overlapping author groups) is the main research program. Paper IV (arXiv:2407.08927) handles even-hole-free graphs with a polylogarithmic bound, which is weaker than the constant bound conjectured for (even hole, diamond)-free graphs. Conjecture 1.6 remains open: no source confirming a constant tree-α for the (even hole, diamond)-free class was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. The class of (even hole, diamond)-free graph has bounded tree-$\alpha$.

Context

The paper's main result handles (even hole, diamond, pyramid)-free graphs; extending to (even hole, diamond)-free graphs (dropping the pyramid-free condition) is posed as the next natural step. No polynomial-time algorithm for MWIS is yet known for the larger (even hole, diamond)-free class, and the authors suggest that the methods developed here might be extendable to settle this conjecture.

Source paper

 Tree independence number I. (Even hole, diamond, pyramid)-free graphs
 Tara Abrishami, Bogdan Alecu, Maria Chudnovsky, Sepehr Hajebi, Sophie Spirkl, Kristina Vušković · 2024-02-22
 https://arxiv.org/abs/2305.16258

=== Source paper abstract / header ===
Abstract:The tree-independence number tree-$\alpha$, first defined and studied by Dallard, Milanič and Štorgel, is a variant of treewidth tailored to solving the maximum independent set problem.
Over a series of papers, Abrishami et al. developed the so-called central bag method to study induced obstructions to bounded treewidth. Among others, they showed that, in a certain superclass $\mathcal C$ of (even hole, diamond, pyramid)-free graphs, treewidth is bounded by a function of the clique number. In this paper, we relax the bounded clique number assumption, and show that $\mathcal C$ has bounded tree-$\alpha$. Via existing results, this yields a polynomial time algorithm for the maximum independent set problem in this class. Our result also corroborates, for this class of graphs, a conjecture of Dallard, Milanič and Štorgel that in a hereditary graph class, tree-$\alpha$ is bounded if and only if the treewidth is bounded by a function of the clique number.
 

 
 
 
 Comments:
 17 pages. arXiv admin note: text overlap with arXiv:2203.06775
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2305.16258 [math.CO]
 

 
  
 (or 
 arXiv:2305.16258v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2305.16258
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Graph Theory 106 (2024), 923-943
 

 
 
 Related DOI:
 
 https://doi.org/10.1002/jgt.23104

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Bogdan Alecu [view email] 
 [v1]
 Thu, 25 May 2023 17:13:38 UTC (37 KB)

 [v2]
 Mon, 26 Jun 2023 16:56:36 UTC (37 KB)

 [v3]
 Thu, 22 Feb 2024 15:16:59 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Tree independence number I. (Even hole, diamond, pyramid)-free graphs, by Tara Abrishami and 4 other authors
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
 | 2023-05
 

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
