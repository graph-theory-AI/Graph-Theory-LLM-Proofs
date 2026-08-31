Attack the following open graph-theory problem.

Catalog id: 2504.01548__00
Catalog status: open (triage tier 2, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2504.01548__00/
Source paper: Defective coloring of blowups (arXiv:2504.01548)

=== Catalog page (statement + literature review) ===
Optimal χ-to-χᵈ ratio in K_{d+1} blowups — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 1.4 asks for the smallest constant $c$ such that $\chi(G) \leq c \cdot \chi^d(G \boxtimes K_{d+1})$ holds for all graphs $G$ and $d \geq 0$. The paper itself establishes the bounds $30/29 \leq c \leq 2$: the lower bound comes from an explicit counterexample to the original Guo--Kang--Zwaneveld equality conjecture, while the upper bound $c \leq 2$ is proved as Theorem 1.3. No subsequent work narrowing this gap was found in a thorough web search conducted in May 2026.

 Reviewer notes. The paper was published in The Electronic Journal of Combinatorics 33(1), P1.17 (January 2026). Problem 1.4 is equivalent to determining the supremum of $\chi(G)/\chi^d(G \boxtimes K_{d+1})$ over all graphs $G$ and $d \geq 0$. The current bounds give $30/29 \leq c \leq 2$; no follow-up work narrowing this gap was found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the smallest value of $c$ for which the inequality $\chi(G)\leq c\cdot\chi^{d}(G\boxtimes K_{d+1})$ always holds.

Context

Theorem 1.2 (for $d=2$) provides a graph showing that $c\geq\frac{30}{29}$ is necessary, while Theorem 1.3 gives the upper bound $c\leq 2$. A bootstrapped version of Theorem 1.2 further shows that assuming $\chi(G)$ or $d$ to be large cannot reduce the constant factor arbitrarily close to $1$.

Notes. The theorem environment statement is truncated to 'Determine' in the source; the full problem is reconstructed from the immediately preceding context.

Source paper

 Defective coloring of blowups
 Sergey Norin, Raphael Steiner · 2025-04-02
 https://arxiv.org/abs/2504.01548

=== Source paper abstract / header ===
Abstract:Given a graph $G$ and an integer $d\ge 0$, its $d$-defective chromatic number $\chi^d(G)$ is the smallest size of a partition of the vertices into parts inducing subgraphs with maximum degree at most $d$. Guo, Kang and Zwaneveld recently studied the relationship between the $d$-defective chromatic number of the $(d+1)$-fold (clique) blowup $G\boxtimes K_{d+1}$ of a graph $G$ and its ordinary chromatic number, and conjectured that $\chi(G)=\chi^d(G\boxtimes K_{d+1})$ for every graph $G$ and $d\ge 0$. In this note we disprove this conjecture by constructing graphs $G$ of arbitrarily large chromatic number such that $\chi(G)\ge \frac{30}{29}\chi^d(G\boxtimes K_{d+1})$ for infinitely many $d$. On the positive side, we show that the conjecture holds with a constant factor correction, namely $\chi^d(G\boxtimes K_{d+1})\le \chi(G)\le 2\chi^d(G\boxtimes K_{d+1})$ for every graph $G$ and $d\ge 0$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C07, 05C15, 05C76
 

 Cite as:
 arXiv:2504.01548 [math.CO]
 

 
  
 (or 
 arXiv:2504.01548v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2504.01548
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Wed, 2 Apr 2025 09:44:52 UTC (10 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Defective coloring of blowups, by Sergey Norin and 1 other authors
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
 | 2025-04
 

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
