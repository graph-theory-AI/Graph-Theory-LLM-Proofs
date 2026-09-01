Attack the following open graph-theory problem.

Catalog id: 2110.15429__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2110.15429__00/
Source paper: Discrepancy of arithmetic progressions in grids (arXiv:2110.15429)

=== Extracted statement (catalog JSON) ===
Title: Conjecture (Section 7)
The lower bound for the discrepancy of arithmetic progressions in grids given in Theorem 1.3 is tight up to the constant factor, i.e., for any positive integer $d$ and $N = (N_1, \ldots, N_d)$ with $N_1 \cdots N_d \geq 3$, $$\mathrm{disc}(\mathcal{A}_N) = \Theta_d\!\left(\max_{I \subseteq [d]} \left(\prod_{i \in I} N_i\right)^{\frac{1}{2|I|+2}}\right).$$

Context:
Theorem 1.3 establishes matching lower and upper bounds for the discrepancy of arithmetic progressions in general grids of differing side lengths, but the upper bound carries an extra sub-logarithmic factor $\frac{\log(N_1 \cdots N_d)}{\log\log(N_1 \cdots N_d)}$ relative to the lower bound. The authors conjecture in their concluding remarks (Section 7) that this gap is an artifact of the proof and the lower bound is in fact tight up to a constant depending only on $d$.

=== Catalog page (statement + literature review) ===
Grid arithmetic progression discrepancy tightness — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture that the lower bound in Theorem 1.3 is tight up to a constant factor (i.e., no logarithmic factor) remains open. Li and Nikolov (2025, arXiv:2504.12598) improved the upper bound gap from a factor of log|Omega_N|/(log log|Omega_N|) to sqrt(log|Omega_N|), using factorization norms, but explicitly state that removing this final sqrt(log) factor is beyond their methods. The conjecture itself is restated as open in that paper.

 Cited literature (1)

 
 
 
partial Discrepancy of Arithmetic Progressions in Boxes and Convex Bodies
 (2025)
 

 
 Lily Li, Aleksandar Nikolov · arXiv preprint · arXiv:2504.12598

Improves the upper bound for disc(A_N) from a log|Omega_N|/(log log|Omega_N|) factor above the conjectured tight bound to a sqrt(log|Omega_N|) factor, via factorization norms; the tight constant-factor conjecture remains explicitly open.
 

 

 Reviewer notes. The source paper was published in Mathematika (2024). The main open question is whether the sqrt(log) gap in arXiv:2504.12598 can be removed to match the lower bound by a constant depending only on d.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. The lower bound for the discrepancy of arithmetic progressions in grids given in Theorem 1.3 is tight up to the constant factor, i.e., for any positive integer $d$ and $N = (N_1, \ldots, N_d)$ with $N_1 \cdots N_d \geq 3$, $$\mathrm{disc}(\mathcal{A}_N) = \Theta_d\!\left(\max_{I \subseteq [d]} \left(\prod_{i \in I} N_i\right)^{\frac{1}{2|I|+2}}\right).$$

Context

Theorem 1.3 establishes matching lower and upper bounds for the discrepancy of arithmetic progressions in general grids of differing side lengths, but the upper bound carries an extra sub-logarithmic factor $\frac{\log(N_1 \cdots N_d)}{\log\log(N_1 \cdots N_d)}$ relative to the lower bound. The authors conjecture in their concluding remarks (Section 7) that this gap is an artifact of the proof and the lower bound is in fact tight up to a constant depending only on $d$.

Notes. Section 7 is not reproduced in the PDF extraction; the conjecture is described by reference in the paper's organization paragraph. The statement above is reconstructed from Theorem 1.3 and the prose description 'a conjecture that the lower bound for the discrepancy for grids in Theorem 1.3 is tight up to the constant factor'.

Source paper

 Discrepancy of arithmetic progressions in grids
 Jacob Fox, Max Wenqiang Xu, Yunkun Zhou · 2021-10-28
 https://arxiv.org/abs/2110.15429
 PDF source

=== Source paper abstract / header ===
Abstract:We prove that the the discrepancy of arithmetic progressions in the $d$-dimensional grid $\{1, \dots, N\}^d$ is within a constant factor depending only on $d$ of $N^{\frac{d}{2d+2}}$. This extends the case $d=1$, which is a celebrated result of Roth and of Matoušek and Spencer, and removes the polylogarithmic factor from the previous upper bound of Valkó from about two decades ago. We further prove similarly tight bounds for grids of differing side lengths in many cases.
 

 
 
 
 Comments:
 25 pages
 

 Subjects:
 
 Combinatorics (math.CO); Number Theory (math.NT)
 

 Cite as:
 arXiv:2110.15429 [math.CO]
 

 
  
 (or 
 arXiv:2110.15429v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2110.15429
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Yunkun Zhou [view email] 
 [v1]
 Thu, 28 Oct 2021 20:38:30 UTC (26 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Discrepancy of arithmetic progressions in grids, by Jacob Fox and 2 other authors
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
 | 2021-10
 

 Change to browse by:
 
 math
 math.NT
 

 

 

 
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
