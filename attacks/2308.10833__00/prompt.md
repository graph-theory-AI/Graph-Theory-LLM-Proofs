Attack the following open graph-theory problem.

Catalog id: 2308.10833__00
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2308.10833__00/
Source paper: Ramsey numbers of hypergraphs of a given size (arXiv:2308.10833)

=== Catalog page (statement + literature review) ===
Multi-color √m graph Ramsey bound — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture asks whether the two-color bound $r_2(G; 2) \leq 2^{c\sqrt{m}}$ for graphs $G$ with $m$ edges and no isolated vertices extends to $q \geq 3$ colors. The source paper itself resolves the analogous problem for $k$-uniform hypergraphs with $k \geq 3$, proving an upper bound of $\mathrm{tw}_k(O(\sqrt{m}))$ for all $q \geq 2$, but the argument is specific to $k \geq 3$ and does not apply to graphs ($k=2$). No follow-up paper resolving or substantially advancing this specific $k=2$, $q \geq 3$ problem was found in the literature.

 Reviewer notes. No follow-up resolving the k=2 multicolor case was found. The paper arXiv:2312.13965 (Bradač, Fox, Sudakov, 2024, Research in the Mathematical Sciences) addresses the growth rate of multicolor Ramsey numbers of 3-uniform hypergraphs but is a different question. The arXiv:2410.17197 improvement on multicolor Ramsey numbers concerns diagonal Ramsey numbers R_r(k) for complete graphs, not the general-graph sqrt(m) bound. The open problem remains: prove or disprove r_2(G; q) \leq 2^{c_q \sqrt{m}} for q \geq 3.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It would be interesting to extend the result $r_2(G; 2) \leq 2^{c\sqrt{m}}$ (for any graph $G$ with $m$ edges and no isolated vertices) to more than two colors.

Context

Sudakov [22] resolved Erdős's conjecture by showing $r_2(G; 2) \leq 2^{c\sqrt{m}}$, but the argument works only for two colors. The paper notes this gap immediately after mentioning the resolution of the conjecture.

Notes. Stated as a brief remark in the introduction without a labelled environment.

Source paper

 Ramsey numbers of hypergraphs of a given size
 Domagoj Bradač, Jacob Fox, Benny Sudakov · 2023-08-21
 https://arxiv.org/abs/2308.10833
 PDF source

=== Source paper abstract / header ===
Abstract:The $q$-color Ramsey number of a $k$-uniform hypergraph $H$ is the minimum integer $N$ such that any $q$-coloring of the complete $k$-uniform hypergraph on $N$ vertices contains a monochromatic copy of $H$. The study of these numbers is one of the central topics in Combinatorics. In 1973, Erdős and Graham asked to maximize the Ramsey number of a graph as a function of the number of its edges. Motivated by this problem, we study the analogous question for hypergaphs. For fixed $k \ge 3$ and $q \ge 2$ we prove that the largest possible $q$-color Ramsey number of a $k$-uniform hypergraph with $m$ edges is at most $\mathrm{tw}_k(O(\sqrt{m})),$ where $\mathrm{tw}$ denotes the tower function. We also present a construction showing that this bound is tight for $q \ge 4$. This resolves a problem by Conlon, Fox and Sudakov. They previously proved the upper bound for $k \geq 4$ and the lower bound for $k=3$. Although in the graph case the tightness follows simply by considering a clique of appropriate size, for higher uniformities the construction is rather involved and is obtained by using paths in expander graphs.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2308.10833 [math.CO]
 

 
  
 (or 
 arXiv:2308.10833v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2308.10833
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Domagoj Bradač [view email] 
 [v1]
 Mon, 21 Aug 2023 16:31:09 UTC (167 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Ramsey numbers of hypergraphs of a given size, by Domagoj Brada\v{c} and 2 other authors
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
 | 2023-08
 

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
