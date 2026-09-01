Attack the following open graph-theory problem.

Catalog id: 2501.00567__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2501.00567__00/
Source paper: Local Shearer bound (arXiv:2501.00567)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.7
Every triangle-free graph $G$ satisfies $\chi(G)\leq(1+o(1))\frac{\rho(G)}{\ln\rho(G)}$.

Context:
Motivated by Harris's conjecture [27] that every triangle-free $d$-degenerate graph satisfies $\chi_f(G)\leq O(\frac{d}{\ln d})$ and by Molloy's bound $(1+o(1))\frac{\Delta(G)}{\ln\Delta(G)}$ in terms of the maximum degree. Since the spectral radius $\rho(G)$ is sandwiched between the degeneracy and the maximum degree, Theorem 1.6 of this paper (a new spectral upper bound on $\chi_f$) is presented as a first step toward interpolating between these two regimes.

=== Catalog page (statement + literature review) ===
χ(G) bound via spectral radius for triangle-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Martinsson and Steiner prove in Theorem 1.6 of arXiv:2501.00567 that every triangle-free graph G satisfies χ_f(G) ≤ (1+o(1))ρ(G)/ln ρ(G), where ρ(G) is the spectral radius. Conjecture 1.7 is the stronger statement that the same bound holds for the ordinary chromatic number χ(G). No subsequent paper resolving or disproving this conjecture was found in the indexed literature as of May 2026.

 Reviewer notes. The paper proves the analogous bound for fractional chromatic number χ_f(G) (Theorem 1.6) as the main result; Conjecture 1.7 extends this to the ordinary chromatic number χ(G). Closely related follow-up work includes arXiv:2501.18238 (Martinsson, resolving Harris' conjecture: every triangle-free d-degenerate graph satisfies χ_f(G) ≤ O(d/ln d)) and arXiv:2601.15245 (coloring small locally sparse degenerate graphs with ordinary chromatic number bounds); neither directly addresses the spectral radius upper bound for χ(G) stated in Conjecture 1.7. No resolution of the conjecture was found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Every triangle-free graph $G$ satisfies $\chi(G)\leq(1+o(1))\frac{\rho(G)}{\ln\rho(G)}$.

Context

Motivated by Harris's conjecture [27] that every triangle-free $d$-degenerate graph satisfies $\chi_f(G)\leq O(\frac{d}{\ln d})$ and by Molloy's bound $(1+o(1))\frac{\Delta(G)}{\ln\Delta(G)}$ in terms of the maximum degree. Since the spectral radius $\rho(G)$ is sandwiched between the degeneracy and the maximum degree, Theorem 1.6 of this paper (a new spectral upper bound on $\chi_f$) is presented as a first step toward interpolating between these two regimes.

Source paper

 Local Shearer bound
 Anders Martinsson, Raphael Steiner · 2024-12-31
 https://arxiv.org/abs/2501.00567

=== Source paper abstract / header ===
Abstract:We prove the following local strengthening of Shearer's classic bound on the independence number of triangle-free graphs: For every triangle-free graph $G$ there exists a probability distribution on its independent sets such that every vertex $v$ of $G$ is contained in a random independent set drawn from the distribution with probability $(1-o(1))\frac{\ln d(v)}{d(v)}$. This resolves the main conjecture raised by Kelly and Postle (2018) about fractional coloring with local demands, which in turn confirms a conjecture by Cames van Batenburg et al. (2018) stating that every $n$-vertex triangle-free graph has fractional chromatic number at most $(\sqrt{2}+o(1))\sqrt{\frac{n}{\ln(n)}}$. Addressing another conjecture posed by Cames van Batenburg et al., we also establish an analogous upper bound in terms of the number of edges.
To prove these results we establish a more general technical theorem that works in a weighted setting. As a further application of this more general result, we obtain a new spectral upper bound on the fractional chromatic number of triangle-free graphs: We show that every triangle-free graph $G$ satisfies $\chi_f(G)\le (1+o(1))\frac{\rho(G)}{\ln \rho(G)}$ where $\rho(G)$ denotes the spectral radius. This improves the bound implied by Wilf's classic spectral estimate for the chromatic number by a $\ln \rho(G)$ factor and makes progress towards a conjecture of Harris on fractional coloring of degenerate graphs.
 

 
 
 
 Comments:
 11 pages, comments welcome
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C07, 05C15, 05C69, 05C72
 

 Cite as:
 arXiv:2501.00567 [math.CO]
 

 
  
 (or 
 arXiv:2501.00567v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2501.00567
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Tue, 31 Dec 2024 17:53:17 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Local Shearer bound, by Anders Martinsson and 1 other authors
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
 | 2025-01
 

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
