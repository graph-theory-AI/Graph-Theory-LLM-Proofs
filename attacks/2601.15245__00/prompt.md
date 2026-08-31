Attack the following open graph-theory problem.

Catalog id: 2601.15245__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2601.15245__00/
Source paper: Coloring small locally sparse degenerate graphs and related problems (arXiv:2601.15245)

=== Catalog page (statement + literature review) ===
Fractional chromatic number of K_r-free d-degenerate graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 4.1 asks for the maximum fractional chromatic number of a $d$-degenerate, $K_r$-free graph. The source paper itself establishes via Theorem 1.6 a lower bound of $\Omega_r(d/\log^{r-2} d)$, ruling out the $O_r(d\log\log d/\log d)$ bound one might expect by analogy with Johansson's theorem for bounded-degree $K_r$-free graphs. No subsequent paper resolving or settling the full question was found; the related paper arXiv:2603.17730 addresses fractional chromatic number of $d$-degenerate locally $r$-colorable graphs (a different condition from $K_r$-freeness) but does not settle Problem 4.1.

 Cited literature (1)

 
 
 
partial Fractional coloring via entropy
 (2026)
 

 
 Abhishek Dhawan · arXiv preprint · arXiv:2603.17730

Proves $\chi_f(G) = O(d\log(2r)/\log d)$ for $d$-degenerate locally $r$-colorable graphs using an entropy-based approach, addressing a related but distinct problem class from $K_r$-free $d$-degenerate graphs; does not directly resolve Problem 4.1.
 

 

 Reviewer notes. Problem 4.1 is posed as an open question in January 2026. The source paper provides a lower bound $\Omega_r(d/\log^{r-2} d)$ via Theorem 1.6, showing the answer exceeds the natural $O_r(d\log\log d/\log d)$ analogy. No follow-up paper directly resolving the $K_r$-free case was found as of 2026-05-14.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the maximum fractional chromatic number of a $d$-degenerate, $K_{r}$-free graph?

Context

Given the main theorem of Martinsson [26] on triangle-free $d$-degenerate graphs and its many applications, the authors seek a generalization of Harris' conjecture for $K_{r}$-free graphs. One might guess the answer is $O_{r}\left(\frac{d\log\log d}{\log d}\right)$ by analogy with Johansson's bound for $K_r$-free graphs of maximum degree $\Delta$, but Theorem 1.6 shows this is not the case.

Source paper

 Coloring small locally sparse degenerate graphs and related problems
 Domagoj Bradač, Jacob Fox, Raphael Steiner, Benny Sudakov, Shengtong Zhang · 2026-01-21
 https://arxiv.org/abs/2601.15245

=== Source paper abstract / header ===
Abstract:The classic upper bound on the chromatic number of $d$-degenerate graphs is $d+1$, shown to be tight by complete graphs. A natural question is whether this bound remains tight if one forbids large cliques. Classic constructions of Tutte and Zykov from the early 50s show that there exist $d$-degenerate $(d+1)$-chromatic graphs that are triangle-free, however these constructions grow rapidly with $d$. Motivated by this and addressing a problem posed by the second author at the Oberwolfach Graph Theory workshop, we prove that the minimum order $f(d)$ of a $d$-degenerate triangle-free graph of chromatic number $d+1$ satisfies $e^{\Omega(d)}\le f(d)\le e^{O(d^2\log d)}.$ The lower bound follows from a novel upper bound on the chromatic number of triangle-free graphs: Every triangle-free $d$-degenerate graph $G$ on $n \le e^{O(d)}$ vertices satisfies $$\chi(G)\le O\left(\frac{d}{\log\left(d/\log n\right)}\right).$$ We extend this to a more general result about degenerate graphs with sparse neighborhoods, which has applications to many graph coloring problems: For example, we prove that every counterexample to Hadwiger's conjecture with parameter $t$ must have a complete bipartite subgraph with one exponentially large side ($K_{a,b}$ where $a=(\log t)^{1/2-o(1)}$ and $b=e^{t^{1-o(1)}}$) or a small and very dense subgraph (of order $\le t$ with $t^{2-o(1)}$ edges) in some neighborhood.
For the upper bound on $f(d)$ we establish a surprising connection between $f(d)$ and the on-line-chromatic number $g(n)$ of $n$-vertex triangle-free graphs. We also give an asymptotic improvement of the previous best upper bound for $g(n)$ due to Lovász, Saks and Trotter from 1989.
Along the way we disprove a generalization of Harris' fractional coloring conjecture to graphs of bounded clique number and raise numerous problems which open up interesting directions to explore for future research.
 

 
 
 
 Comments:
 24 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15, 05C83
 

 Cite as:
 arXiv:2601.15245 [math.CO]
 

 
  
 (or 
 arXiv:2601.15245v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2601.15245
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Wed, 21 Jan 2026 18:26:40 UTC (37 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Coloring small locally sparse degenerate graphs and related problems, by Domagoj Brada\v{c} and 4 other authors
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
 | 2026-01
 

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
