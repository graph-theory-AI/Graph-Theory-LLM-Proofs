Attack the following open graph-theory problem.

Catalog id: 2404.02021__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2404.02021__00/
Source paper: On off-diagonal hypergraph Ramsey numbers (arXiv:2404.02021)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 4.1
There exists an absolute constant $a>0$ such that, for all $3$-graphs $G$ and $H$, $r^{p}(G,H)\geq r(G,H)^{a}$ whenever $p>r(G,H)^{o(1)}$.

Context:
The authors introduce the notion of pair constructions $\chi_{f,g}$ of complexity $p$, observing that stepping-up and inducibility constructions both fit this paradigm. They conjecture that any Ramsey coloring of order $N$ yields one of order $N^{\Omega(1)}$ with much smaller complexity, which would explain the prevalence of low-complexity constructions in Ramsey theory and potentially illuminate the possible growth rates of $r(H, K_{n}^{(3)})$.

=== Catalog page (statement + literature review) ===
Pair-complexity lower bound for 3-graph Ramsey — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 4.1 from arXiv:2404.02021 asks whether every Ramsey coloring of order N for 3-graphs G,H with pair-construction complexity p > r(G,H)^{o(1)} must have complexity at least r(G,H)^a for an absolute constant a>0. No follow-up paper confirming or refuting this conjecture was found. A related 2026 preprint by He (arXiv:2603.16069) constructs 3-graphs with quasipolynomial Ramsey growth rates in the same research area, but its abstract does not address the pair-construction complexity framework of Conjecture 4.1.

 Reviewer notes. The conjecture is a structural/framework-level claim asserting that pair constructions of low complexity are essentially universal for hypergraph Ramsey lower bounds. The source paper was published in IMRN (Volume 2025, Issue 11). A 2026 preprint arXiv:2603.16069 by He (a co-author) constructs 3-graphs with quasipolynomial Ramsey growth rates n^{Theta(log n)}, directly relevant to the surrounding discussion, but could not be confirmed to address Conjecture 4.1 specifically within the 5-call budget.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There exists an absolute constant $a>0$ such that, for all $3$-graphs $G$ and $H$, $r^{p}(G,H)\geq r(G,H)^{a}$ whenever $p>r(G,H)^{o(1)}$.

Context

The authors introduce the notion of pair constructions $\chi_{f,g}$ of complexity $p$, observing that stepping-up and inducibility constructions both fit this paradigm. They conjecture that any Ramsey coloring of order $N$ yields one of order $N^{\Omega(1)}$ with much smaller complexity, which would explain the prevalence of low-complexity constructions in Ramsey theory and potentially illuminate the possible growth rates of $r(H, K_{n}^{(3)})$.

Source paper

 On off-diagonal hypergraph Ramsey numbers
 David Conlon, Jacob Fox, Benjamin Gunby, Xiaoyu He, Dhruv Mubayi, Andrew Suk, Jacques Verstraete · 2024-04-02
 https://arxiv.org/abs/2404.02021

=== Source paper abstract / header ===
Abstract:A fundamental problem in Ramsey theory is to determine the growth rate in terms of $n$ of the Ramsey number $r(H, K_n^{(3)})$ of a fixed $3$-uniform hypergraph $H$ versus the complete $3$-uniform hypergraph with $n$ vertices. We study this problem, proving two main results. First, we show that for a broad class of $H$, including links of odd cycles and tight cycles of length not divisible by three, $r(H, K_n^{(3)}) \ge 2^{\Omega_H(n \log n)}$. This significantly generalizes and simplifies an earlier construction of Fox and He which handled the case of links of odd cycles and is sharp both in this case and for all but finitely many tight cycles of length not divisible by three. Second, disproving a folklore conjecture in the area, we show that there exists a linear hypergraph $H$ for which $r(H, K_n^{(3)})$ is superpolynomial in $n$. This provides the first example of a separation between $r(H,K_n^{(3)})$ and $r(H,K_{n,n,n}^{(3)})$, since the latter is known to be polynomial in $n$ when $H$ is linear.
 

 
 
 
 Comments:
 22 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2404.02021 [math.CO]
 

 
  
 (or 
 arXiv:2404.02021v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2404.02021
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Xiaoyu He [view email] 
 [v1]
 Tue, 2 Apr 2024 15:09:54 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On off-diagonal hypergraph Ramsey numbers, by David Conlon and 6 other authors
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
 | 2024-04
 

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
