Attack the following open graph-theory problem.

Catalog id: 2409.18220__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2409.18220__00/
Source paper: A Linear Lower Bound for the Square Energy of Graphs (arXiv:2409.18220)

=== Catalog page (statement + literature review) ===
Square energy ⁴⁄₅n lower bound — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The paper proves s(G) ≥ 3n/4 for every connected graph G of order n ≥ 4, and informally conjectures this can be improved to 4n/5 via more intricate partitioning. The source paper was published in the Electronic Journal of Combinatorics (July 2025). No follow-up work proving or disproving the informal 4n/5 bound was found in the literature; the full conjecture s(G) ≥ n-1 (due to Elphick, Farber, Goldberg and Wocjan, 2016) also remains open.

 Reviewer notes. The 4n/5 bound is an informal conjecture stated within the paper without a formal label; it sits between the proven 3n/4 and the full conjectured n-1 bound. A related paper arXiv:2409.15504 (extremal square energies) does not cite 2409.18220. A September 2025 SDP-based paper arXiv:2509.05814 addresses graph energy lower bounds but does not reference this informal conjecture. No follow-up found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Informal. We believe the above bound can be improved to $\frac{4n}{5}$ using more intricate partitioning of the graph $G$ and applying Theorem 2.

Context

After establishing $s(G) \geq \frac{3n}{4}$, the authors note that a more refined partitioning argument could push the constant to $\frac{4n}{5}$, but that fully resolving Conjecture 1 ($s(G) \geq n-1$) requires fundamentally new ideas beyond those used in this paper.

Notes. PDF source — fractions are garbled by extraction; '4n − 5' and '3n − 4' in the raw text are interpreted as $\frac{4n}{5}$ and $\frac{3n}{4}$ respectively, consistent with the paper's proved result and the surrounding context.

Source paper

 A Linear Lower Bound for the Square Energy of Graphs
 Saieed Akbari, Hitesh Kumar, Bojan Mohar, Shivaramakrishna Pragada · 2024-09-26
 https://arxiv.org/abs/2409.18220
 PDF source

=== Source paper abstract / header ===
Abstract:Let $G$ be a graph of order $n$ with eigenvalues $\lambda_1 \geq \cdots \geq\lambda_n$. Let \[s^+(G)=\sum_{\lambda_i>0} \lambda_i^2, \qquad s^-(G)=\sum_{\lambda_i<0} \lambda_i^2.\] The smaller value, $s(G)=\min\{s^+(G), s^-(G)\}$ is called the \emph{square energy} of $G$. In 2016, Elphick, Farber, Goldberg and Wocjan conjectured that for every connected graph $G$ of order $n$, $s(G)\geq n-1.$ No linear bound for $s(G)$ in terms of $n$ is known. Let $H_1, \ldots, H_k$ be disjoint vertex-induced subgraphs of $G$. In this note, we prove that \[s^+(G)\geq\sum_{i=1}^{k} s^+(H_i) \quad \text{ and } \quad s^-(G)\geq\sum_{i=1}^{k} s^-(H_i),\] which implies that $s(G)\geq \frac{3n}{4}$ for every connected graph $G$ of order $n\ge 4$.
 

 
 
 
 Comments:
 5 pages, 1 figure
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C50
 

 Cite as:
 arXiv:2409.18220 [math.CO]
 

 
  
 (or 
 arXiv:2409.18220v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2409.18220
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Hitesh Kumar [view email] 
 [v1]
 Thu, 26 Sep 2024 18:58:48 UTC (6 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A Linear Lower Bound for the Square Energy of Graphs, by Saieed Akbari and 3 other authors
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
 | 2024-09
 

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
