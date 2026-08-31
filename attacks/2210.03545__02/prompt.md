Attack the following open graph-theory problem.

Catalog id: 2210.03545__02
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2210.03545__02/
Source paper: Hypergraph Ramsey numbers of cliques versus stars (arXiv:2210.03545)

=== Catalog page (statement + literature review) ===
3-uniform Ramsey K⁴⁻ vs star Θ(n²/log n) — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that $r(K^{(3)}_{4-e}, S^{(3)}_n) = \Theta(n^2/\log n)$ remains open. The source paper (Proposition 1.1) establishes the bounds $c\,n^2/\log^2 n \le r(K^{(3)}_{4-e}, S^{(3)}_n) \le c'\,n^2/\log n$, leaving a logarithmic gap. A targeted search of the 2022–2026 literature found no follow-up paper closing this gap; the two most relevant subsequent papers on off-diagonal hypergraph Ramsey numbers (arXiv:2404.02021 and arXiv:2411.13812) address clique-vs-clique settings rather than clique-vs-star.

 Reviewer notes. No follow-up resolving the conjecture found after 5 web calls. The closest related papers (arXiv:2404.02021, arXiv:2411.13812) concern off-diagonal Ramsey numbers against complete hypergraphs K_n^(3), not against stars S_n^(3). The conjecture is closely related to the classical result r(K_3, K_n) = Theta(n^2/log n) via the analogy noted by the authors; the suggested proof strategy via the (K^{(3)}_{4-e})-free process has not been carried out in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. The close connection between $r(K^{(3)}_{4-e}, S^{(3)}_n)$ and $r(K_3, K_n)$ suggests that $r(K^{(3)}_{4-e}, S^{(3)}_n) = \Theta\!\left(\frac{n^2}{\log n}\right)$.

Context

Proposition 1.1 gives bounds $c\,\frac{n^2}{\log^2 n} \le r(K^{(3)}_{4-e}, S^{(3)}_n) \le c'\,\frac{n^2}{\log n}$. The authors note 'it seems likely that a proof of this may be possible through a careful analysis of the $(K^{(3)}_{4-e})$-free process', drawing an analogy with $r(K_3,K_n)=\Theta(n^2/\log n)$, but they do not pursue it.

Notes. PDF source — conjectural language 'suggests' and 'it seems likely'; $K^{(3)}_{4-e}$ denotes the complete 3-uniform hypergraph on 4 vertices minus one edge; math notation reconstructed from PDF extraction.

Source paper

 Hypergraph Ramsey numbers of cliques versus stars
 David Conlon, Jacob Fox, Xiaoyu He, Dhruv Mubayi, Andrew Suk, Jacques Verstraete · 2022-10-07
 https://arxiv.org/abs/2210.03545
 PDF source

=== Source paper abstract / header ===
Abstract:Let $K_m^{(3)}$ denote the complete $3$-uniform hypergraph on $m$ vertices and $S_n^{(3)}$ the $3$-uniform hypergraph on $n+1$ vertices consisting of all $\binom{n}{2}$ edges incident to a given vertex. Whereas many hypergraph Ramsey numbers grow either at most polynomially or at least exponentially, we show that the off-diagonal Ramsey number $r(K_{4}^{(3)},S_n^{(3)})$ exhibits an unusual intermediate growth rate, namely, \[ 2^{c \log^2 n} \le r(K_{4}^{(3)},S_n^{(3)}) \le 2^{c' n^{2/3}\log n} \] for some positive constants $c$ and $c'$. The proof of these bounds brings in a novel Ramsey problem on grid graphs which may be of independent interest: what is the minimum $N$ such that any $2$-edge-coloring of the Cartesian product $K_N \square K_N$ contains either a red rectangle or a blue $K_n$?
 

 
 
 
 Comments:
 13 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2210.03545 [math.CO]
 

 
  
 (or 
 arXiv:2210.03545v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2210.03545
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Xiaoyu He [view email] 
 [v1]
 Fri, 7 Oct 2022 13:29:46 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Hypergraph Ramsey numbers of cliques versus stars, by David Conlon and 5 other authors
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
 | 2022-10
 

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
